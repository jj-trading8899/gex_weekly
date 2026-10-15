#!/usr/bin/env python3
"""
Pull key levels from TerraShade and write a dated snapshot.

TerraShade is an open, unauthenticated JSON API. There are no credentials here
and none are needed. Endpoints are undocumented and may change without notice,
so every run records what it actually received and flags what looks unusable.

Modes
  eod       full ticker list, one snapshot per trading day  -> data/terrashade-YYYY-MM-DD.json
            also captures intraday wall history             -> data/gexhist/terrashade-gexhist-YYYY-MM-DD.json
  intraday  index subset only, appended to one file per day -> data/intraday/terrashade-intraday-YYYY-MM-DD.json

Quality flags (computed at write time, so the stored file is already graded)
  stale          chain_as_of older than thresholds.stale_minutes at pull time
  wide           (call_wall - put_wall) / spot over thresholds.wide_corridor_pct
  no_boundary    no bias boundary found within +/-15% of spot
  band_excludes  the daily expected-move band does not contain spot, which means
                 the chain behind the levels is out of date regardless of its timestamp

Stdlib only. No pip install needed.
"""

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "gex_weekly/terrashade-monitor (+https://github.com/jj-trading8899/gex_weekly)"


def load_config():
    with open(os.path.join(HERE, "config.json")) as fh:
        return json.load(fh)


def utcnow():
    return dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)


def get_json(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_levels(symbol, http):
    """Return (payload, error). Retries only the build-pending response."""
    url = "https://terrashade.onrender.com/api/levels?symbol=" + symbol
    attempts = http["building_retries"] + 1
    last = "unknown"
    for i in range(attempts):
        try:
            data = get_json(url, http["timeout_seconds"])
        except urllib.error.HTTPError as exc:
            return None, "http_%d" % exc.code
        except Exception as exc:                                  # noqa: BLE001
            return None, "transport:%s" % type(exc).__name__
        if "error" not in data:
            return data, None
        last = data["error"]
        if last != "building" or i == attempts - 1:
            break
        time.sleep(http["building_backoff_seconds"])
    return None, last


def parse_chain_age(chain_as_of, now):
    if not chain_as_of:
        return None
    try:
        stamp = dt.datetime.strptime(chain_as_of.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None
    return int((now - stamp).total_seconds() // 60)


def grade(row, thresholds):
    flags = []
    spot, pw, cw = row.get("spot"), row.get("put_wall"), row.get("call_wall")
    age = row.get("chain_age_min")

    if age is not None and age > thresholds["stale_minutes"]:
        flags.append("stale")

    width = None
    if spot and pw is not None and cw is not None and spot > 0:
        width = round((cw - pw) / spot * 100, 2)
        if width > thresholds["wide_corridor_pct"]:
            flags.append("wide")
    row["corridor_width_pct"] = width

    if row.get("bias_boundary") is None:
        flags.append("no_boundary")

    daily = (row.get("expected_moves") or {}).get("daily") or {}
    lo, hi = daily.get("low"), daily.get("high")
    if lo is not None and hi is not None and spot is not None and not (lo <= spot <= hi):
        flags.append("band_excludes")

    row["flags"] = flags
    row["usable"] = not flags
    return row


def to_row(symbol, payload, now, thresholds):
    boundary = payload.get("zero_gamma")
    spot = payload.get("spot")
    row = {
        "ticker": symbol,
        "status": "ok",
        "spot": spot,
        "prev_close": payload.get("prev_close"),
        "chain_as_of": (payload.get("chain_as_of") or "").replace(" UTC", ""),
        "chain_age_min": parse_chain_age(payload.get("chain_as_of"), now),
        "put_wall": payload.get("put_wall"),
        "call_wall": payload.get("call_wall"),
        "bias_boundary": boundary,
        "anchor_strike": payload.get("king"),
        "anchor_value": payload.get("king_gex"),
        "expected_moves": payload.get("em") or {},
    }
    if boundary is not None and spot is not None:
        row["bias"] = "long" if spot > boundary else "short"
    else:
        row["bias"] = None
    if row["prev_close"]:
        row["chg_pct"] = round((spot - row["prev_close"]) / row["prev_close"] * 100, 2)
    else:
        row["chg_pct"] = None
    return grade(row, thresholds)


def sweep(tickers, cfg, now):
    rows, http = [], cfg["http"]
    for symbol in tickers:
        payload, err = fetch_levels(symbol, http)
        if err:
            rows.append({"ticker": symbol, "status": err, "usable": False, "flags": ["no_data"]})
            print("  %-6s %s" % (symbol, err), file=sys.stderr)
        else:
            row = to_row(symbol, payload, now, cfg["thresholds"])
            rows.append(row)
            print("  %-6s ok  %s" % (symbol, ",".join(row["flags"]) or "clean"), file=sys.stderr)
        time.sleep(http["delay_seconds"])
    return rows


def capture_gexhist(tickers, http):
    """One call per ticker returns the whole intraday wall path TerraShade recorded today."""
    out = {}
    for symbol in tickers:
        try:
            data = get_json(
                "https://terrashade.onrender.com/api/gexhist?symbol=" + symbol,
                http["timeout_seconds"])
            if "error" in data:
                out[symbol] = {"status": data["error"]}
            else:
                out[symbol] = {"status": "ok", "demo": data.get("demo"), "pts": data.get("pts", [])}
        except Exception as exc:                                  # noqa: BLE001
            out[symbol] = {"status": "transport:%s" % type(exc).__name__}
        time.sleep(http["delay_seconds"])
    return out


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=1, sort_keys=False)
    print("wrote %s" % path, file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["eod", "intraday"], default="eod")
    ap.add_argument("--force", action="store_true", help="run even on a weekend or market holiday")
    args = ap.parse_args()

    cfg = load_config()
    now = utcnow()
    day = now.strftime("%Y-%m-%d")

    if not args.force:
        if now.weekday() >= 5:
            print("weekend, nothing to do", file=sys.stderr)
            return 0
        if day in cfg["market_holidays"]:
            print("market holiday, nothing to do", file=sys.stderr)
            return 0

    tickers = cfg["tickers"] if args.mode == "eod" else cfg["intraday_tickers"]
    print("%s sweep, %d tickers, %sZ" % (args.mode, len(tickers), now.isoformat(timespec="seconds")),
          file=sys.stderr)

    rows = sweep(tickers, cfg, now)
    ok = [r for r in rows if r["status"] == "ok"]
    usable = [r for r in ok if r["usable"]]

    summary = {
        "requested": len(rows),
        "returned": len(ok),
        "usable": len(usable),
        "no_data": [r["ticker"] for r in rows if r["status"] != "ok"],
        "stale": [r["ticker"] for r in ok if "stale" in r["flags"]],
        "wide": [r["ticker"] for r in ok if "wide" in r["flags"]],
        "band_excludes": [r["ticker"] for r in ok if "band_excludes" in r["flags"]],
    }
    print("returned %d/%d, usable %d" % (len(ok), len(rows), len(usable)), file=sys.stderr)

    meta = {
        "pulled_at": now.isoformat(timespec="seconds") + "Z",
        "mode": args.mode,
        "source": cfg["source"],
        "thresholds": cfg["thresholds"],
        "note": "TerraShade only. No other provider is mixed into this file.",
    }

    if args.mode == "eod":
        write_json(os.path.join(HERE, "data", "terrashade-%s.json" % day),
                   {**meta, "summary": summary, "rows": rows})
        hist = capture_gexhist(cfg["gexhist_tickers"], cfg["http"])
        write_json(os.path.join(HERE, "data", "gexhist", "terrashade-gexhist-%s.json" % day),
                   {**meta, "tickers": hist})
    else:
        path = os.path.join(HERE, "data", "intraday", "terrashade-intraday-%s.json" % day)
        if os.path.exists(path):
            with open(path) as fh:
                doc = json.load(fh)
        else:
            doc = {"day": day, "source": cfg["source"], "snapshots": []}
        doc["snapshots"].append({"pulled_at": meta["pulled_at"], "summary": summary, "rows": rows})
        write_json(path, doc)

    return 0


if __name__ == "__main__":
    sys.exit(main())
