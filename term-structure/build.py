#!/usr/bin/env python3
"""Build the TradeEcho single-stock term-structure page from a capture snapshot.

Usage:
    python3 build.py                      # newest data/raw/*.json -> index.html
    python3 build.py data/raw/2026-10-09.json
"""
import calendar
import datetime as dt
import glob
import json
import os
import statistics
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
# In the gex_weekly repo the snapshots live in ../data/term-structure; in the Mac pipeline folder, in ./data
_REPO_DATA = os.path.join(ROOT, "..", "data", "term-structure")
DATA = os.path.normpath(_REPO_DATA) if os.path.isdir(_REPO_DATA) else os.path.join(ROOT, "data")
TOP_PER_COL = 9          # strikes kept per expiry column
WINDOW = 0.15            # only strikes within +/-15% of spot
STRIP_MAX = 4            # cells in the per-expiry strip
HORIZON = 5              # sessions a level is tested over when measuring odds
FLIP_DAYS = 3            # sessions used to smooth the flip into a zone
# chance of a close through a plain strike within HORIZON sessions, by distance bucket, before any history exists
PRIOR_THROUGH = [0.60, 0.35, 0.15, 0.07]


def third_friday(y, m):
    c = calendar.Calendar()
    fridays = [d for d in c.itermonthdates(y, m) if d.month == m and d.weekday() == 4]
    return fridays[2]


def next_monthly_opex(after: dt.date):
    y, m = after.year, after.month
    for _ in range(3):
        tf = third_friday(y, m)
        if tf > after:
            return tf
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return None


def k(g):  # contracts -> K, 1dp
    return round(g / 1000.0, 1)


def fmt_k(x):
    s = "+" if x >= 0 else "−"
    a = abs(x)
    if a >= 1000:
        return f"{s}{a/1000:.2f}M"
    return f"{s}{a:.0f}K" if a >= 100 else f"{s}{a:.1f}K"


def strike_s(x):
    return f"{x:.0f}" if x == int(x) else f"{x:g}"


def parse_rows(v, snap_date):
    """Per-strike rows -> {expiry: [(strike, positioning, vex)]}."""
    year, by_exp = snap_date.year, {}
    for mmdd, strike, g, vex in v["rows"]:
        e = f"{year}-{mmdd}"
        if e < snap_date.isoformat():          # year rollover (Dec -> Jan)
            e = f"{year+1}-{mmdd}"
        by_exp.setdefault(e, []).append((float(strike), g, vex))
    return by_exp


def matrix_cols(by_exp, snap_date):
    """Expiries shown in the matrix and used for the key levels: front expiry through the monthly opex."""
    future = sorted(e for e in by_exp if e > snap_date.isoformat())
    opex = next_monthly_opex(snap_date).isoformat()
    if opex in future:
        cols = future[: future.index(opex) + 1]
    else:
        cols = future[:3]
    if opex in cols and len(cols) > 3:
        # opex is weeks out: keep the real front expiry, the first Friday weekly after it, and opex
        fri = [e for e in cols[1:-1] if dt.date.fromisoformat(e).weekday() == 4]
        cols = [cols[0]] + fri[:1] + [opex]
    cols = cols[-4:] if len(cols) > 4 else cols
    if len(cols) < 3:   # opex is near: add the following Friday expiry to the matrix
        nxt = [e for e in future if e > cols[-1] and dt.date.fromisoformat(e).weekday() == 4]
        if nxt:
            cols.append(nxt[0])
    return cols, opex, future


def aggregate(spot, cols, by_exp, opex):
    """Positioning per strike summed across the matrix expiries (opex weighted 1.5)."""
    agg, sign_cnt = {}, {}
    for e in cols:
        w = 1.5 if e == opex else 1.0
        for strike, g, _ in by_exp[e]:
            if abs(strike - spot) > spot * WINDOW:
                continue
            agg[strike] = agg.get(strike, 0) + g * w
            sign_cnt[strike] = sign_cnt.get(strike, 0) + (1 if g > 0 else -1 if g < 0 else 0)
    max_pos = max((v for v in agg.values() if v > 0), default=1)
    max_neg = max((-v for v in agg.values() if v < 0), default=1)
    return agg, sign_cnt, max_pos, max_neg


def size_class(v, max_pos, max_neg):
    """big / mid positive level, neg(ative) level, or none (a plain strike)."""
    s = v / max_pos if v > 0 else v / max_neg
    return "big" if s >= 0.4 else "mid" if s >= 0.1 else "neg" if s <= -0.3 else "none"


def dist_bucket(d, unit):
    """Distance from spot in typical daily moves: under 1, 1-2, 2-4, over 4."""
    x = d / unit
    return 0 if x < 1 else 1 if x < 2 else 2 if x < 4 else 3


def load_history(snap_date):
    """All saved snapshots up to and including snap_date, oldest first: [(date, tickers)]."""
    out = []
    for f in sorted(glob.glob(os.path.join(DATA, "raw/*.json"))):
        d = os.path.basename(f)[:10]
        if d <= snap_date.isoformat():
            out.append((d, json.load(open(f))["tickers"]))
    return out


def _ok(h, t):
    return t in h[1] and "error" not in h[1][t]


def typical_move(hist, t):
    """Median absolute close-to-close move (fraction) for the ticker across the saved snapshots."""
    px = [float(h[1][t]["spot"]) for h in hist if _ok(h, t)]
    ch = [abs(px[i + 1] / px[i] - 1) for i in range(len(px) - 1)]
    return max(0.005, statistics.median(ch)) if len(ch) >= 5 else 0.015


def flip_band(hist, t, spot, raw):
    """Smooth TradeEcho's flip over the last FLIP_DAYS snapshots: it jumps too much to use as a line."""
    fl = [h[1][t]["kl"]["flipPoint"] for h in hist[-FLIP_DAYS:]
          if _ok(h, t) and (h[1][t].get("kl") or {}).get("flipPoint") is not None]
    if raw is not None and (not fl or abs(fl[-1] - raw) > 1e-9):
        fl.append(raw)
    if not fl:
        return None
    mid = statistics.median(fl)
    lo, hi = min(min(fl), mid * 0.996), max(max(fl), mid * 1.004)
    prev = fl[-2] if len(fl) > 1 else fl[-1]
    return {"mid": mid, "lo": lo, "hi": hi, "raw": fl[-1], "prev": prev,
            "jump": abs(fl[-1] - prev) / spot > 0.03, "wide": (hi - lo) / spot > 0.03,
            "pos": "below" if spot < lo else "above" if spot > hi else "in"}


def calibrate(hist):
    """Measure, from past snapshots, how often a later close went through a strike within HORIZON sessions,
    by side, distance (in typical daily moves) and size of positioning at the strike."""
    counts, sessions = {}, 0
    units = {t: typical_move(hist, t) for t in (hist[-1][1] if hist else {})}
    for i in range(len(hist) - HORIZON):
        d, snap = hist[i]
        sd, used = dt.date.fromisoformat(d), False
        for t, v in snap.items():
            if "error" in v:
                continue
            fut = [float(hist[j][1][t]["spot"]) for j in range(i + 1, i + 1 + HORIZON) if _ok(hist[j], t)]
            if len(fut) < HORIZON:
                continue
            spot = float(v["spot"])
            by_exp = parse_rows(v, sd)
            cols, opex, _ = matrix_cols(by_exp, sd)
            agg, _, max_pos, max_neg = aggregate(spot, cols, by_exp, opex)
            hi, lo = max(fut), min(fut)
            for strike, g in agg.items():
                dd = (strike - spot) / spot
                if abs(dd) <= 0.003:
                    continue
                side = "up" if dd > 0 else "dn"
                key = (side, dist_bucket(abs(dd), units.get(t, 0.015)), size_class(g, max_pos, max_neg))
                c = counts.setdefault(key, [0, 0])
                c[0] += 1
                c[1] += (hi > strike) if side == "up" else (lo < strike)
            used = True
        sessions += used
    return {"counts": counts, "sessions": sessions, "units": units}


def through_rate(cal, side, db, cls):
    """Chance (0-1) of a close through the level within HORIZON sessions, and the sample size behind it.
    Small samples are pulled toward the rate for all strikes at that side and distance."""
    c = cal["counts"]
    n0 = sum(v[0] for key, v in c.items() if key[0] == side and key[1] == db)
    b0 = sum(v[1] for key, v in c.items() if key[0] == side and key[1] == db)
    p0 = (b0 + 6 * PRIOR_THROUGH[db]) / (n0 + 6)
    n, b = c.get((side, db, cls), [0, 0])
    return (b + 8 * p0) / (n + 8), n


def build_ticker(t, v, snap_date, hist=None, cal=None):
    spot = float(v["spot"])
    kl = v.get("kl") or {}
    sums = {e: tuple(x) for e, x in v["sums"].items()}
    by_exp = parse_rows(v, snap_date)
    cols, opex, future = matrix_cols(by_exp, snap_date)
    cal = cal or {"counts": {}, "sessions": 0, "units": {}}
    unit = cal["units"].get(t, 0.015)

    # strip: matrix cols + following expiries from sums
    strip = list(cols)
    later = [e for e in sorted(sums) if e > cols[-1]]
    fridays = [e for e in later if dt.date.fromisoformat(e).weekday() == 4]
    for e in fridays + [e for e in later if e not in fridays]:   # prefer Friday weeklies
        if len(strip) >= STRIP_MAX:
            break
        strip.append(e)
    strip = sorted(strip)
    term = [[k(sums[e][0]), round(sums[e][1])] for e in strip]

    per_col = []
    for e in cols:
        rows = [r for r in by_exp[e] if abs(r[0] - spot) <= spot * WINDOW]
        top = sorted(rows, key=lambda r: -abs(r[1]))[:TOP_PER_COL]
        per_col.append({"code": e, "net": k(sums[e][0]), "opex": e == opex,
                        "strikes": [[r[0], k(r[1])] for r in sorted(top, key=lambda r: -r[0])]})

    # ---- levels from the opex (or last) column, full strike set ----
    lv_exp = opex if opex in by_exp else cols[-1]
    lv = [r for r in by_exp[lv_exp] if abs(r[0] - spot) <= spot * WINDOW]
    # a strike within 0.3% above spot is the pin price is sitting on, not a cap overhead
    pos_above = sorted([r for r in lv if r[0] > spot * 1.003 and r[1] > 0], key=lambda r: -r[1])
    pos_below = sorted([r for r in lv if r[0] <= spot and r[1] > 0], key=lambda r: -r[1])
    neg_below = sorted([r for r in lv if r[0] < spot and r[1] < 0], key=lambda r: r[1])
    biggest = max(lv, key=lambda r: r[1]) if lv else None
    max_abs = max((abs(r[1]) for r in lv), default=1)

    band = flip_band(hist or [], t, spot, kl.get("flipPoint"))
    flip = band["mid"] if band else None        # 3-session middle of the flip, not today's raw value
    pos = band["pos"] if band else "above"      # above / in / below the flip zone
    anchor = kl.get("anchorPoint")
    wall = pos_above[0] if pos_above else None
    sup = pos_below[0] if pos_below else None
    sup_thin = sup is not None and sup[1] < 0.10 * max_abs
    floor_k = sup[0] if (sup and not sup_thin) else spot
    neg_under = [r for r in neg_below if r[0] < floor_k]
    neg = neg_under[0] if neg_under else None
    opex_net = sums.get(lv_exp, (0, 0))[0]
    front_net = sums.get(cols[0], (0, 0))[0]
    md = lambda e: f"{int(e[5:7])}/{int(e[8:10])}"

    # ---- regime: net positioning into opex leads, the flip zone refines ----
    fz = f"${flip:.0f}" if flip is not None else ""
    if opex_net < 0:
        tone, regime = "neg", "net negative into opex · bigger swings" + (f" · below flip {fz}" if pos == "below" else "")
    elif pos == "below":
        tone, regime = "mix", f"positive board · below flip {fz}"
    elif pos == "in" and flip is not None:
        tone, regime = "mix", f"on the flip {fz}"
    else:
        tone, regime = "pos", f"steadier · ${strike_s(wall[0])} cap" if wall else "steadier"
    if v.get("rating") is not None and v["rating"] <= 3 and tone == "pos":
        tone = "mix"

    ladder = trade_ladder(spot, flip, anchor, cols, by_exp, opex, cal=cal, unit=unit,
                          supportive=(opex_net > 0 and pos == "above"), band=band)
    sells = [r for r in ladder if r["kind"] == "sell"]
    first_r = next((r for r in sells if r.get("tier") in ("first", "both")), None)
    major_r = next((r for r in sells if r.get("tier") in ("major", "both")), None)
    first_r = first_r or major_r
    sups = sorted([r for r in ladder if r["kind"] in ("buy", "weak")], key=lambda r: -r["k"])
    gaps = sorted([r for r in ladder if r["kind"] == "trigger"], key=lambda r: -r["k"])
    pockets = sorted([r for r in ladder if r["kind"] == "pocket"], key=lambda r: r["k"])
    down_r = sups[0] if sups else (gaps[0] if gaps else None)

    lo = sup[0] if sup else (neg[0] if neg else spot)
    hi = wall[0] if wall else (anchor or spot)
    rng = f"${strike_s(lo)}-{strike_s(hi)}"
    if flip is not None:
        rng += f" · flip ${flip:.0f}"

    # ---- plain-language read ----
    parts = [f"Closed ${spot:.2f}."]
    if biggest and biggest[1] > 0:
        parts.append(f"Into {md(lv_exp)} opex dealers net {fmt_k(k(opex_net))}, heaviest at "
                     f"${strike_s(biggest[0])} ({fmt_k(k(biggest[1]))}).")
    else:
        parts.append(f"Into {md(lv_exp)} opex dealers net {fmt_k(k(opex_net))}.")
    parts.append("Net negative into opex has gone with the biggest day-to-day swings." if opex_net < 0
                 else "Net positive into opex has gone with smaller day-to-day swings.")
    if flip is not None:
        zone = f"${band['lo']:.0f}–{band['hi']:.0f}"
        if band["jump"]:
            parts.append(f"The flip moved from ${band['prev']:.0f} to ${band['raw']:.0f} today, so treat {zone} as a zone, not a line.")
        if pos == "above":
            parts.append(f"Above the flip zone (about ${flip:.0f}), where moves have tended to be a little smaller.")
        elif pos == "below":
            parts.append(f"Below the flip zone (about ${flip:.0f}), where moves have tended to be bigger.")
        else:
            parts.append(f"Inside the flip zone ({zone}), so the next close decides which side it trades on.")
    if first_r and major_r and first_r is not major_r:
        parts.append(f"First resistance ${strike_s(first_r['k'])} (held {first_r['odds']}% of the time), "
                     f"major cap ${strike_s(major_r['k'])} (held {major_r['odds']}%).")
    elif first_r:
        parts.append(f"Resistance ${strike_s(first_r['k'])} (held {first_r['odds']}% of the time).")
    if pockets:
        parts.append(f"${strike_s(pockets[0]['k'])} above is an air pocket: rallies closed through levels like it "
                     f"{pockets[0]['odds']}% of the time.")
    if sups and sups[0]["kind"] == "buy":
        parts.append(f"Support ${strike_s(sups[0]['k'])} (held {sups[0]['odds']}% of the time).")
    elif sups:
        parts.append(f"Support at ${strike_s(sups[0]['k'])} is weak: levels like it held only {sups[0]['odds']}% of the time.")
    else:
        parts.append("No real support below spot.")
    if gaps:
        parts.append(f"There's no support at ${strike_s(gaps[0]['k'])}.")
    if k(front_net) < 0:  # ignore nets that round to 0.0K
        parts.append(f"The {md(cols[0])} front expiry is net negative ({fmt_k(k(front_net))}), "
                     "so near-term swings can overshoot before opex takes over.")
    if v.get("outlook"):
        parts.append(f"TradeEcho's own read: {v['outlook'].split(',')[0].split(' ')[0].rstrip('.:;')}.")

    card = {
        "t": t, "spot": spot, "chg": None, "cols": [md(e) for e in strip],
        "opexIdx": strip.index(lv_exp) if lv_exp in strip else -1,
        "regime": regime, "tone": tone, "term": term,
        "pin": f"${strike_s(anchor)}" if anchor else "—",
        "wall": (f"${strike_s(first_r['k'])} first · ${strike_s(major_r['k'])} cap" if first_r and major_r and first_r is not major_r
                 else f"${strike_s(first_r['k'])}" if first_r else "none"),
        "sup": (f"${strike_s(sups[0]['k'])}" + ("" if sups[0]["kind"] == "buy" else " (weak)")) if sups else "none",
        "flip": f"~${flip:.0f}" if flip is not None else "—",
        "range": rng, "read": " ".join(parts),
    }
    ts = {"t": t, "spot": spot, "chg": None, "flip": round(flip, 2) if flip is not None else None, "perCol": per_col,
          "ladder": ladder, "board": k(opex_net), "pos": pos, "dayMove": round(unit * 100, 2)}
    card["_stats"] = {
        "t": t, "spot": spot, "flip": flip, "tone": tone, "rating": v.get("rating"), "pos": pos, "band": band,
        "first": first_r["k"] if first_r else None,
        "major": major_r["k"] if major_r and major_r is not first_r else None,
        "down": down_r["k"] if down_r else None, "down_kind": down_r["kind"] if down_r else None,
        "gap": gaps[0]["k"] if gaps else None,
        "opex_net": k(opex_net), "front_net": k(front_net), "front": md(cols[0]),
        "biggest": (biggest[0], k(biggest[1])) if biggest else None,
        "wall": wall[0] if wall else None, "sup": sup[0] if sup else None, "sup_thin": sup_thin,
        "neg": neg[0] if neg else None, "targets": sorted({r["k"] for r in (first_r, major_r) if r}),
        "core": sorted(r[0] for r in sorted([r for r in lv if r[1] > 0], key=lambda r: -r[1])[:2]),
    }
    return card, ts, lv_exp


def trade_ladder(spot, flip, anchor, cols, by_exp, opex, cal=None, unit=0.015, supportive=False, band=None):
    """Key levels with measured odds.

    Positioning is summed per strike across the matrix expiries. Each level's odds come from the snapshot
    history (see calibrate): how often a level of this size, at this distance, held or was closed through
    within HORIZON sessions. `base` is the same measure for a plain strike, so odds - base is the level's edge.
    Kinds: sell (resistance; tier first / major / both), buy (support in a supportive setup), weak (support
    otherwise), pocket (negative level above spot), trigger (negative level below spot: no support), pin, flip.
    """
    cal = cal or {"counts": {}, "sessions": 0, "units": {}}
    agg, sign_cnt, max_pos, max_neg = aggregate(spot, cols, by_exp, opex)
    if not agg:
        return []
    cnt = {s: sum(1 for e in cols for st, g, _ in by_exp[e] if st == s and (g > 0) == (v > 0) and g != 0)
           for s, v in agg.items()}   # expiries that agree with the aggregate sign

    def row(s, v, kind, **extra):
        dist = abs(s - spot) / spot
        r = {"k": s, "kind": kind, "strength": round((v / max_pos) if v > 0 else (-v / max_neg), 2),
             "n": cnt.get(s, 0), "dm": round(dist / unit, 1), "odds": None}
        if kind != "pin":
            side, db = ("up" if s > spot else "dn"), dist_bucket(dist, unit)
            p, obs = through_rate(cal, side, db, size_class(v, max_pos, max_neg))
            p0, _ = through_rate(cal, side, db, "none")
            holds = kind in ("sell", "buy", "weak")      # odds = held; otherwise odds = closed through
            clamp = lambda x: int(round(min(95, max(5, 100 * x))))
            r.update(odds=clamp((1 - p) if holds else p), base=clamp((1 - p0) if holds else p0), obs=obs)
        r.update(extra)
        return r

    rows = []
    pos_up = [(s, v) for s, v in agg.items() if s > spot * 1.003 and v > 0]
    if pos_up:
        major = max(pos_up, key=lambda x: x[1])[0]
        first = min((s for s, v in pos_up if v / max_pos >= 0.25), default=major)   # nearest level that matters
        keep = [first] + ([major] if major != first else [])
        for s, _ in sorted(pos_up, key=lambda x: -x[1]):
            if len(keep) >= 3:
                break
            if s not in keep:
                keep.append(s)
        for s in keep:
            tier = "both" if s == first == major else "first" if s == first else "major" if s == major else None
            rows.append(row(s, agg[s], "sell", tier=tier))
    # negative levels above spot: little resistance, rallies have tended to close through them
    for s, v in sorted([(s, v) for s, v in agg.items() if s > spot * 1.003 and v < 0
                        and -v / max_neg >= 0.3 and (s - spot) / spot <= 0.08], key=lambda x: x[1])[:2]:
        rows.append(row(s, v, "pocket"))
    # a support must be near enough and big enough to matter
    for s, v in sorted([(s, v) for s, v in agg.items() if s <= spot and v > 0
                        and v / max_pos >= 0.05 and (spot - s) / spot <= 0.08], key=lambda x: -x[1])[:2]:
        r = row(s, v, "weak")
        # a buy zone needs a supportive setup AND measured evidence that levels like it hold
        if supportive and r["odds"] >= 50 and r["odds"] - r["base"] >= 5:
            r["kind"] = "buy"
        rows.append(r)
    for s, v in sorted([(s, v) for s, v in agg.items() if s < spot and v < 0], key=lambda x: x[1])[:2]:
        rows.append(row(s, v, "trigger"))
    if anchor is not None and not any(r["k"] == anchor for r in rows):
        rows.append(row(anchor, max(agg.get(anchor, 0), 0), "pin"))
    else:
        for r in rows:
            if r["k"] == anchor:
                r["pin"] = True
    if flip is not None:
        f = {"k": round(flip, 1), "kind": "flip", "strength": None, "n": None, "odds": None}
        if band:
            f.update(lo=round(band["lo"], 1), hi=round(band["hi"], 1), jump=band["jump"])
        rows.append(f)
    rows.sort(key=lambda r: -r["k"])
    return rows


def glance(stats):
    """At-a-glance lean per ticker into opex (plain directional language, no forecasts).
    Net positioning into opex leads (it tracked the size of the next day's move best); the flip zone refines."""
    out = []
    for s in stats:
        spot, net, pos, b = s["spot"], s["opex_net"], s["pos"], s["band"]
        boxed = s["down_kind"] in ("buy", "weak") and s["first"] and (s["first"] - s["down"]) / spot < 0.03
        if net < 0:
            lean = "down" if pos == "below" else "swing"
        elif pos == "below":
            lean = "shaky"
        elif pos == "in":
            lean = "edge"
        else:
            lean = "range" if boxed else "up"
        out.append({"t": s["t"], "spot": spot, "lean": lean, "flip": round(s["flip"], 2) if s["flip"] is not None else None,
                    "flipLo": round(b["lo"], 1) if b else None, "flipHi": round(b["hi"], 1) if b else None,
                    "flipWide": bool(b and b["wide"]), "flipJump": bool(b and b["jump"]),
                    "up": s["first"], "cap": s["major"], "down": s["down"], "downKind": s["down_kind"],
                    "board": net, "thin": abs(net) < 2})
    return out


def headlines(stats):
    """One plain-language line per ticker: watch-list first, weakest last."""
    S = {s["t"]: s for s in stats}
    used, out = set(), []
    def fl(s, own="its"):   # "its $283 flip", or the zone when the flip has been moving
        b = s["band"]
        return f"{own} ${b['lo']:.0f}–{b['hi']:.0f} flip zone" if b["wide"] else f"{own} ${s['flip']:.0f} flip"
    span = lambda ks: f"${strike_s(ks[0])}" if len(ks) == 1 or ks[0] == ks[-1] else f"${strike_s(ks[0])}–{strike_s(ks[-1])}"
    # 1) on or below the flip -> one to watch
    # net negative names first (bigger swings), then whichever is closest to its flip
    for s in sorted(stats, key=lambda s: (s["opex_net"] >= 0, abs(s["spot"] - (s["flip"] or s["spot"])) / s["spot"])):
        if s["flip"] is None:
            continue
        if s["pos"] != "above":
            where = "right on its flip" if s["pos"] == "in" else "below its flip"
            line = f"<b>{s['t']}</b> is the one to watch. It's sitting {where} at about ${s['flip']:.0f}"
            if s["pos"] == "in" and s["band"]["wide"]:
                line = (f"<b>{s['t']}</b> is the one to watch. It's inside a flip zone that has been moving "
                        f"(${s['band']['lo']:.0f}–{s['band']['hi']:.0f})")
            if s["biggest"] and s["biggest"][0] > s["spot"]:
                size = "a very large" if s["biggest"][1] >= 100 else "its largest"
                line += f", under {size} ${strike_s(s['biggest'][0])} level ({fmt_k(s['biggest'][1])})"
            line += "."
            if s["down_kind"] not in ("buy", "weak"):
                line += " There's almost no support below it"
                line += f", and none at all around ${strike_s(s['gap'])}." if s["gap"] else "."
            else:
                line += (f" Support is ${strike_s(s['down'])}" if s["down_kind"] == "buy"
                         else f" Support at ${strike_s(s['down'])} is weak")
                line += f"; below that there's none around ${strike_s(s['gap'])}." if s["gap"] else "."
            if s["opex_net"] < 0:
                most = s is min(stats, key=lambda x: x["opex_net"])
                line += (f" It's also the most negative board ({fmt_k(s['opex_net'])} into opex), so swings are likely to be big."
                         if most else f" It's net negative into opex ({fmt_k(s['opex_net'])}), so swings are likely to be bigger.")
            out.append(line); used.add(s["t"])
            break
    # weakest board (smallest opex net) is reserved for the end
    rest = [s for s in stats if s["t"] not in used]
    weakest = min(rest, key=lambda s: s["opex_net"]) if len(rest) > 2 else None
    # 2) most positioning into opex
    big = max((s for s in rest if s is not weakest), key=lambda s: s["opex_net"], default=None)
    if big:
        top = max(stats, key=lambda s: s["opex_net"])
        if top is big:
            line = f"<b>{big['t']}</b> has the most positioning into opex ({fmt_k(big['opex_net'])}), centred on {span(big['core'])}."
        else:
            line = (f"<b>{big['t']}</b> has the next-most positioning into opex ({fmt_k(big['opex_net'])}, after "
                    f"<b>{top['t']}</b>'s {fmt_k(top['opex_net'])}), centred on {span(big['core'])}.")
        if big["front_net"] < 0:
            line += f" The {big['front']} expiry is net negative, though, so the next few sessions could be choppy."
        if big["flip"] is not None and big["pos"] == "below":
            line += f" It closed below {fl(big)}, so moves can run until it gets back above."
        elif big["flip"] is not None and big["pos"] == "in":
            line += f" It's also sitting on {fl(big)}."
        out.append(line); used.add(big["t"])
    # 3) the rest: boxed in, or pulled toward a level
    boxed, pulled, below = [], [], []
    for s in stats:
        if s["t"] in used or s is weakest:
            continue
        if s["flip"] is not None and s["pos"] == "below":   # below its flip zone
            below.append(s); used.add(s["t"])
            continue
        if s["opex_net"] < 0:   # above its flip but net negative into opex: nothing is pulling it up
            where = "above" if s["pos"] == "above" else "on"
            boxed.append(f"<b>{s['t']}</b> is {where} {fl(s)} but net negative into opex ({fmt_k(s['opex_net'])}), "
                         f"so swings are likely to be bigger")
        elif s["sup"] and s["wall"] and not s["sup_thin"] and (s["wall"] - s["sup"]) / s["spot"] < 0.03:
            boxed.append(f"<b>{s['t']}</b> is boxed between ${strike_s(s['sup'])} and ${strike_s(s['wall'])}")
        elif s["targets"]:
            pulled.append((s["t"], span(s["targets"])))
        used.add(s["t"])
    sentences = [b + "." for b in boxed]
    if pulled:
        S = {s["t"]: s for s in stats}
        def on_flip(t):   # a "pulled" name sitting on its flip: the pull only holds while it stays above
            s = S[t]
            return s["flip"] is not None and s["pos"] == "in"
        def note(t):   # keep the pull honest when the name is on its flip or has little underneath it
            if on_flip(t):
                return f" (and it's sitting on {fl(S[t])})"
            if not S[t]["sup"] or S[t]["sup_thin"]:
                return " (with little support underneath)"
            return ""
        p = [f"<b>{t}</b> at {lv}" + note(t) for t, lv in pulled]
        p[0] = p[0].replace("</b> at", "</b> faces resistance at")
        sentences.append((p[0] if len(p) == 1 else ", ".join(p[:-1]) + ", and " + p[-1]) + ".")
    if sentences:
        out.append(" ".join(sentences))
    if below:
        names = " and ".join(f"<b>{s['t']}</b>" for s in below) if len(below) <= 2 else \
            ", ".join(f"<b>{s['t']}</b>" for s in below[:-1]) + f", and <b>{below[-1]['t']}</b>"
        fz = lambda s: f"${s['band']['lo']:.0f}–{s['band']['hi']:.0f}" if s["band"]["wide"] else f"${s['flip']:.0f}"
        flips = " and ".join(fz(s) for s in below) if len(below) <= 2 else \
            ", ".join(fz(s) for s in below[:-1]) + f", and {fz(below[-1])}"
        line = f"{names} closed below {'its flip' if len(below) == 1 else 'their flips'} ({flips})"
        if all(s["opex_net"] < 0 for s in below):
            line += f", with net negative positioning into opex"
        out.append(line + (", so moves can run until it gets back above." if len(below) == 1
                           else ", so moves can run until they get back above."))
    # 4) weakest
    if weakest:
        rank = "the weakest board" if weakest is min(stats, key=lambda s: s["opex_net"]) else "the next-weakest board"
        line = f"<b>{weakest['t']}</b> is {rank}, at only {fmt_k(weakest['opex_net'])} into opex."
        if weakest["flip"] is not None:
            rel = "inside" if weakest["pos"] == "in" and weakest["band"]["wide"] else "on" if weakest["pos"] == "in" else \
                "below" if weakest["pos"] == "below" else \
                "just above" if weakest["spot"] - weakest["band"]["hi"] < weakest["spot"] * 0.01 else "above"
            line += f" It's {rel} {fl(weakest)}"
            line += f", and TradeEcho rates it {weakest['rating']}/5." if weakest.get("rating") and weakest["rating"] <= 3 else "."
        out.append(line)
    return out


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else sorted(glob.glob(os.path.join(DATA, "raw/*.json")))[-1]
    snap = json.load(open(src))
    snap_date = dt.date.fromisoformat(os.path.basename(src)[:10])
    hist = load_history(snap_date)
    cal = calibrate(hist)
    cards, ts, opex = [], [], None
    for t, v in snap["tickers"].items():
        if "error" in v:
            print(f"skip {t}: {v['error']}")
            continue
        c, s, opex = build_ticker(t, v, snap_date, hist, cal)
        cards.append(c)
        ts.append(s)
    updated = max(v.get("updated", "") for v in snap["tickers"].values() if "error" not in v)
    stats = [c.pop("_stats") for c in cards]
    payload = {"snapshot": snap_date.isoformat(), "nextOpex": opex, "dataUpdatedAt": updated,
               "capturedAt": snap["capturedAt"],
               "cal": {"sessions": cal["sessions"], "horizon": HORIZON}, "headlines": headlines(stats), "glance": glance(stats), "cards": cards, "ts": ts}
    tpl = open(os.path.join(ROOT, "template.html")).read()
    html = tpl.replace("/*__PAYLOAD__*/null", json.dumps(payload, separators=(",", ":")))
    out = os.path.join(ROOT, "index.html")
    open(out, "w").write(html)
    json.dump(payload, open(os.path.join(DATA, f"built-{snap_date.isoformat()}.json"), "w"), indent=1)
    print(f"built {out} from {os.path.basename(src)} · {len(cards)} tickers · opex {opex}")


if __name__ == "__main__":
    main()
