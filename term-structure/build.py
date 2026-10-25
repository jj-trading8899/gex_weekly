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
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TOP_PER_COL = 9          # strikes kept per expiry column
WINDOW = 0.15            # only strikes within +/-15% of spot
STRIP_MAX = 4            # cells in the per-expiry strip


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


def build_ticker(t, v, snap_date):
    spot = float(v["spot"])
    kl = v.get("kl") or {}
    year = snap_date.year
    sums = {e: tuple(x) for e, x in v["sums"].items()}
    by_exp = {}
    for mmdd, strike, g, vex in v["rows"]:
        e = f"{year}-{mmdd}"
        if e < snap_date.isoformat():          # year rollover (Dec -> Jan)
            e = f"{year+1}-{mmdd}"
        by_exp.setdefault(e, []).append((float(strike), g, vex))
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

    flip = kl.get("flipPoint")
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

    # ---- regime ----
    if flip is not None and abs(spot - flip) / spot < 0.004:
        tone, regime = "mix", f"on the flip ${flip:.0f}"
    elif flip is not None and spot < flip:
        tone, regime = "neg", f"below flip ${flip:.0f} · moves amplify"
    elif opex_net > 0:
        tone, regime = "pos", f"pinning · ${strike_s(wall[0])} cap" if wall else "pinning"
    else:
        tone, regime = "neg", "net negative into opex"
    if v.get("rating") is not None and v["rating"] <= 3 and tone == "pos":
        tone = "mix"

    lo = sup[0] if sup else (neg[0] if neg else spot)
    hi = wall[0] if wall else (anchor or spot)
    rng = f"${strike_s(lo)}-{strike_s(hi)}"
    if flip is not None:
        rng += f" · flip ${flip:.0f}"

    # ---- plain-language read ----
    parts = [f"Closed ${spot:.2f}."]
    if biggest and biggest[1] > 0:
        parts.append(f"Into {md(lv_exp)} opex dealers net {fmt_k(k(opex_net))}, heaviest at "
                     f"${strike_s(biggest[0])} ({fmt_k(k(biggest[1]))}) — the level price is pulled toward.")
    if flip is not None:
        if spot >= flip:
            parts.append(f"Above the ${flip:.1f} flip, so dealer hedging leans against moves and dips tend to get bought.")
        else:
            parts.append(f"Below the ${flip:.1f} flip, so dealer hedging adds to moves — breaks can run.")
    if wall:
        parts.append(f"Cap at ${strike_s(wall[0])} ({fmt_k(k(wall[1]))}).")
    if sup and not sup_thin:
        parts.append(f"Support ${strike_s(sup[0])} ({fmt_k(k(sup[1]))}).")
    elif sup_thin or not sup:
        parts.append("Little real support below spot" + (f" — thin ${strike_s(sup[0])} only." if sup else "."))
    if neg:
        lead = f"Under ${strike_s(floor_k)}" if floor_k != spot else "Below spot"
        parts.append(f"{lead}, the ${strike_s(neg[0])} pocket ({fmt_k(k(neg[1]))}) is where selling speeds up.")
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
        "wall": f"${strike_s(wall[0])} cap" if wall else "none",
        "sup": (f"${strike_s(sup[0])}" + (" (thin)" if sup_thin else "")) if sup else "none",
        "flip": f"~${flip:.0f}" if flip is not None else "—",
        "range": rng, "read": " ".join(parts),
    }
    ts = {"t": t, "spot": spot, "chg": None, "flip": round(flip, 2) if flip is not None else None, "perCol": per_col,
          "ladder": trade_ladder(spot, flip, anchor, cols, by_exp, opex)}
    top_above = sorted(pos_above[:2], key=lambda r: r[0])
    card["_stats"] = {
        "t": t, "spot": spot, "flip": flip, "tone": tone, "rating": v.get("rating"),
        "opex_net": k(opex_net), "front_net": k(front_net), "front": md(cols[0]),
        "biggest": (biggest[0], k(biggest[1])) if biggest else None,
        "wall": wall[0] if wall else None, "sup": sup[0] if sup else None, "sup_thin": sup_thin,
        "neg": neg[0] if neg else None, "targets": [r[0] for r in top_above],
        "core": sorted(r[0] for r in sorted([r for r in lv if r[1] > 0], key=lambda r: -r[1])[:2]),
    }
    return card, ts, lv_exp


def trade_ladder(spot, flip, anchor, cols, by_exp, opex):
    """Buy / sell / trigger levels with a heuristic odds score (not a calibrated probability).

    Aggregates positioning per strike across the matrix expiries. A level is stronger when
    it is large relative to the board, shows up in several expiries, and sits close to spot.
    Odds = chance the level holds on first test (buy/sell/pin) or that a break accelerates (trigger).
    """
    agg, cnt, sign_cnt = {}, {}, {}
    n_cols = len(cols)
    for e in cols:
        w = 1.5 if e == opex else 1.0   # opex positions are the stickiest
        for strike, g, _ in by_exp[e]:
            if abs(strike - spot) > spot * WINDOW:
                continue
            agg[strike] = agg.get(strike, 0) + g * w
            sign_cnt[strike] = sign_cnt.get(strike, 0) + (1 if g > 0 else -1 if g < 0 else 0)
    for strike, v in agg.items():   # expiries that agree with the aggregate sign
        cnt[strike] = sum(1 for e in cols for st, g, _ in by_exp[e] if st == strike and (g > 0) == (v > 0) and g != 0)
    if not agg:
        return []
    max_pos = max((v for v in agg.values() if v > 0), default=1)
    max_neg = max((-v for v in agg.values() if v < 0), default=1)

    def odds(strike, v, kind):
        strength = (v / max_pos) if v > 0 else (-v / max_neg)
        agree = abs(sign_cnt[strike]) / n_cols
        dist = min(abs(strike - spot) / spot, 0.15) / 0.15
        p = 38 + 34 * strength + 14 * agree - 12 * dist
        if flip is not None:
            if kind == "buy" and spot < flip: p -= 10     # buying below the flip: dealers add to moves
            if kind == "sell" and spot > flip: p += 4
            if kind == "trigger" and spot < flip: p += 8
        return int(max(18, min(88, round(p))))

    rows = []
    sells = sorted([(s, v) for s, v in agg.items() if s > spot * 1.003 and v > 0], key=lambda x: -x[1])[:3]
    buys = sorted([(s, v) for s, v in agg.items() if s <= spot and v > 0], key=lambda x: -x[1])[:2]
    trigs = sorted([(s, v) for s, v in agg.items() if s < spot and v < 0], key=lambda x: x[1])[:2]
    for s, v in sells:
        rows.append({"k": s, "kind": "sell", "strength": round(v / max_pos, 2), "n": cnt[s], "odds": odds(s, v, "sell")})
    for s, v in buys:
        rows.append({"k": s, "kind": "buy", "strength": round(v / max_pos, 2), "n": cnt[s], "odds": odds(s, v, "buy")})
    for s, v in trigs:
        rows.append({"k": s, "kind": "trigger", "strength": round(-v / max_neg, 2), "n": cnt[s], "odds": odds(s, v, "trigger")})
    if anchor is not None and not any(r["k"] == anchor for r in rows):
        v = agg.get(anchor, 0)
        rows.append({"k": anchor, "kind": "pin", "strength": round(max(v, 0) / max_pos, 2), "n": cnt.get(anchor, 0),
                     "odds": odds(anchor, v, "sell" if anchor > spot else "buy") if v > 0 else None})
    else:
        for r in rows:
            if r["k"] == anchor:
                r["pin"] = True
    if flip is not None:
        rows.append({"k": round(flip, 1), "kind": "flip", "strength": None, "n": None, "odds": None})
    rows.sort(key=lambda r: -r["k"])
    return rows


def headlines(stats):
    """One plain-language line per ticker: watch-list first, weakest last."""
    S = {s["t"]: s for s in stats}
    used, out = set(), []
    span = lambda ks: f"${strike_s(ks[0])}" if len(ks) == 1 or ks[0] == ks[-1] else f"${strike_s(ks[0])}–{strike_s(ks[-1])}"
    # 1) on or below the flip -> one to watch
    for s in sorted(stats, key=lambda s: abs(s["spot"] - (s["flip"] or s["spot"])) / s["spot"]):
        if s["flip"] is None:
            continue
        if abs(s["spot"] - s["flip"]) / s["spot"] < 0.004 or s["spot"] < s["flip"]:
            where = "right on its flip" if abs(s["spot"] - s["flip"]) / s["spot"] < 0.004 else "below its flip"
            line = f"<b>{s['t']}</b> is the one to watch. It's sitting {where} at about ${s['flip']:.0f}"
            if s["biggest"] and s["biggest"][0] > s["spot"]:
                size = "a very large" if s["biggest"][1] >= 100 else "its largest"
                line += f", under {size} ${strike_s(s['biggest'][0])} level ({fmt_k(s['biggest'][1])})"
            line += "."
            if s["sup_thin"] or s["sup"] is None:
                line += " There's almost no support below it"
                line += f", and selling would speed up around ${strike_s(s['neg'])}." if s["neg"] else "."
            elif s["neg"]:
                line += f" Support is ${strike_s(s['sup'])}; below that, selling would speed up around ${strike_s(s['neg'])}."
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
        if big["flip"] is not None and big["spot"] < big["flip"]:
            line += f" It closed just below its ${big['flip']:.0f} flip, so moves can run until it gets back above."
        elif big["flip"] is not None and abs(big["spot"] - big["flip"]) / big["spot"] < 0.004:
            line += f" It's also sitting right on its ${big['flip']:.0f} flip."
        out.append(line); used.add(big["t"])
    # 3) the rest: boxed in, or pulled toward a level
    boxed, pulled, below = [], [], []
    for s in stats:
        if s["t"] in used or s is weakest:
            continue
        if s["flip"] is not None and s["spot"] < s["flip"]:   # below its flip: not a "pulled toward" name
            below.append(s); used.add(s["t"])
            continue
        if s["sup"] and s["wall"] and not s["sup_thin"] and (s["wall"] - s["sup"]) / s["spot"] < 0.03:
            boxed.append(f"<b>{s['t']}</b> is boxed between ${strike_s(s['sup'])} and ${strike_s(s['wall'])}")
        elif s["targets"]:
            pulled.append((s["t"], span(s["targets"])))
        used.add(s["t"])
    sentences = [b + "." for b in boxed]
    if pulled:
        S = {s["t"]: s for s in stats}
        def on_flip(t):   # a "pulled" name sitting on its flip: the pull only holds while it stays above
            s = S[t]
            return s["flip"] is not None and abs(s["spot"] - s["flip"]) / s["spot"] < 0.004
        p = [f"<b>{t}</b> toward {lv}" + (f" (only while it holds its ${S[t]['flip']:.0f} flip)" if on_flip(t) else "")
             for t, lv in pulled]
        p[0] = p[0].replace("</b> toward", "</b> is pulled toward")
        sentences.append((p[0] if len(p) == 1 else ", ".join(p[:-1]) + ", and " + p[-1]) + ".")
    if sentences:
        out.append(" ".join(sentences))
    if below:
        names = " and ".join(f"<b>{s['t']}</b>" for s in below) if len(below) <= 2 else \
            ", ".join(f"<b>{s['t']}</b>" for s in below[:-1]) + f", and <b>{below[-1]['t']}</b>"
        flips = " and ".join(f"${s['flip']:.0f}" for s in below)
        line = f"{names} closed below {'its flip' if len(below) == 1 else 'their flips'} ({flips})"
        if all(s["opex_net"] < 0 for s in below):
            line += f", with net negative positioning into opex"
        out.append(line + (", so moves can run until it gets back above." if len(below) == 1
                           else ", so moves can run until they get back above."))
    # 4) weakest
    if weakest:
        line = f"<b>{weakest['t']}</b> is the weakest board, at only {fmt_k(weakest['opex_net'])} into opex."
        if weakest["flip"] is not None:
            rel = "just above" if 0 <= weakest["spot"] - weakest["flip"] < weakest["spot"] * 0.01 else ("above" if weakest["spot"] > weakest["flip"] else "below")
            line += f" It's {rel} its ${weakest['flip']:.0f} flip"
            line += f", and TradeEcho rates it {weakest['rating']}/5." if weakest.get("rating") and weakest["rating"] <= 3 else "."
        out.append(line)
    return out


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else sorted(glob.glob(os.path.join(ROOT, "data/raw/*.json")))[-1]
    snap = json.load(open(src))
    snap_date = dt.date.fromisoformat(os.path.basename(src)[:10])
    cards, ts, opex = [], [], None
    for t, v in snap["tickers"].items():
        if "error" in v:
            print(f"skip {t}: {v['error']}")
            continue
        c, s, opex = build_ticker(t, v, snap_date)
        cards.append(c)
        ts.append(s)
    updated = max(v.get("updated", "") for v in snap["tickers"].values() if "error" not in v)
    stats = [c.pop("_stats") for c in cards]
    payload = {"snapshot": snap_date.isoformat(), "nextOpex": opex, "dataUpdatedAt": updated,
               "capturedAt": snap["capturedAt"], "headlines": headlines(stats), "cards": cards, "ts": ts}
    tpl = open(os.path.join(ROOT, "template.html")).read()
    html = tpl.replace("/*__PAYLOAD__*/null", json.dumps(payload, separators=(",", ":")))
    out = os.path.join(ROOT, "index.html")
    open(out, "w").write(html)
    json.dump(payload, open(os.path.join(ROOT, f"data/built-{snap_date.isoformat()}.json"), "w"), indent=1)
    print(f"built {out} from {os.path.basename(src)} · {len(cards)} tickers · opex {opex}")


if __name__ == "__main__":
    main()
