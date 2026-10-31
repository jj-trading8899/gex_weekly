#!/usr/bin/env python3
"""Build the weekly expected-move page from Dealer Edge captures.

Usage:
    python3 expected-move/build.py                    # newest capture -> expected-move.html
    python3 expected-move/build.py 2026-10-16         # a specific capture date

Reads  data/dealer-edge/dealer-edge-YYYY-MM-DD.json
Writes expected-move.html at the repo root.

Charts: SPX (SPX/SPY blended, index points), SPY (standalone, dollars),
QQQ (standalone). Days already closed in the target week show actual closes;
remaining days are projected.
"""
import datetime as dt
import glob
import json
import os
import statistics as st
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "dealer-edge")
OUT = os.path.join(ROOT, "expected-move.html")

# ---------------------------------------------------------------- data access

def load(date=None):
    files = sorted(glob.glob(os.path.join(DATA, "dealer-edge-*.json")))
    if not files:
        sys.exit("no dealer-edge captures found in %s" % DATA)
    if date:
        hit = [f for f in files if date in f]
        if not hit:
            sys.exit("no capture for %s" % date)
        files = files[: files.index(hit[0]) + 1]
    return files


def series(files, ticker):
    out = []
    for f in files:
        d = json.load(open(f))
        r = next((x for x in d["rows"] if x["t"] == ticker), None)
        if r:
            out.append((os.path.basename(f)[12:22], r))
    return out

# ------------------------------------------------------------------- engine

def sigma(ser):
    """Mean absolute close-to-close move over the last 4 sessions."""
    sp = [r["spot"] for _, r in ser][-5:]
    return st.mean([abs(sp[i + 1] - sp[i]) for i in range(len(sp) - 1)]) if len(sp) > 1 else 0.0


def vex_weight(ser):
    """Week-level amplitude from the |VEX| ratio.

    A sign flip in net vol exposure is a regime signal, not an amplitude one,
    so take magnitude for the width and report the flip separately. Guards the
    square root against the negative readings that do occur in the captures.
    """
    v = [r["netVexM"] for _, r in ser]
    if len(v) < 2:
        return 1.0, False
    cur, prior = v[-1], st.mean([abs(x) for x in v[-5:-1]])
    flip = cur < 0
    if prior <= 0:
        return 1.0, flip
    return max(0.85, min(1.35, (abs(cur) / prior) ** 0.5)), flip


def damping(r):
    g = r["gexstr"]
    if g >= 4 and r["putwall"] <= r["spot"] <= r["callwall"]:
        f = 0.90
    elif g <= 2:
        f = 1.35
    else:
        f = 1.00
    if r["buydip"] is None or r["netK"] < -100:
        f *= 1.25
    return f


def directions(ser, gexstr, pin, spot):
    """gexstr>=4 mean-reverts (alternate); <=2 follows pin migration.

    The midweek day is turned toward the pin when it sits on the far side of
    spot; that is the mean-reversion component, not a directional call. The
    band centre itself only pulls toward the pin when pin_pull() allows it.
    """
    pins = [r["pin"] for _, r in ser][-4:]
    falling = len(pins) >= 2 and pins[-1] < pins[0]
    if gexstr >= 4:
        base = ["up", "down", "up", "down", "up"]
    elif gexstr <= 2:
        base = ["down"] * 5 if falling else ["up"] * 5
        if (pin > spot) == falling:
            base[2] = "up" if falling else "down"
    else:
        base = ["down", "up", "down", "up", "down"] if falling else ["up", "down", "up", "down", "up"]
    return base


def headline(tick, lv, spot, cont, buydip_null, ser, vexflip):
    pins = [r["pin"] for _, r in ser][-4:]
    ceils = [r["callwall"] for _, r in ser][-4:]
    gap_floor = spot - lv["putwall"]
    if cont < 1.0:
        return "The pin is too thin to hold."
    if spot < lv["putwall"]:
        return "The floor broke."
    if spot > lv["callwall"]:
        return "Above the ceiling — no cap left."
    if abs(lv["putwall"] - lv["brk"]) < 1e-9 and gap_floor <= 0.10 * (lv["callwall"] - lv["putwall"]):
        return "The floor and the trapdoor are the same line."
    if buydip_null:
        return "No bid underneath."
    if len(ceils) >= 3 and ceils[-1] < ceils[-2] < ceils[-3]:
        return "The ceiling keeps stepping down."
    if len(pins) >= 3 and pins[-1] > pins[-2] > pins[-3]:
        return "The corridor is lifting."
    gexstr = ser[-1][1]["gexstr"]
    # Spot resting on the put wall with no strength behind it is not a pin regime.
    if gexstr <= 2 and abs(spot - lv["putwall"]) <= 0.003 * spot:
        return "Standing on the floor."
    # The benign default only applies when the book actually has strength and
    # spot is above the bias boundary; otherwise say what is true instead.
    if gexstr <= 2 or spot < lv["flip"]:
        return "Under the pivot, nothing holding it."
    return "The pin's still in charge."


def pin_pull(row):
    """The pin only pulls price when the book is not short and has strength.

    Scored 12-30 Oct: with bias short and strength at the bottom of the scale the
    pin sat above spot every week and acted as a ceiling; centring toward it
    leaned the band up 9 of 9 times while the market fell 9 of 9.
    """
    return row["bias"] != "short" and row["gexstr"] >= 3


def project(lv, spot, sig, vw, dirs, dp, dampf, nobid, n_done, opex_friday=True, pull=True):
    C = lv["callwall"] - lv["putwall"]
    Ceff = C * dampf
    h_struct = 0.40 * Ceff
    h_real = 0.50 * sig
    floored = h_real > h_struct          # walls thinner than a normal session
    h0 = max(h_struct, h_real) * vw
    # The lower clip assumes dealers defend the put wall. With no bid near spot
    # and spot already sitting on that wall, there is no evidence of a defence.
    onfloor = nobid and (spot - lv["putwall"]) <= 0.10 * C

    ramp = [1.00, 1.04, 1.08, 1.12, 1.00]
    opex = [1, 1, 1, 1, 1.8 if opex_friday else 1.0]
    w = [0.2, 0.3, 0.5, 0.45, 0.1] if pull else [0.0] * 5
    # Mid-week: compress the remaining weights so the path still lands on Friday.
    days, carry = [], spot
    for i in range(n_done, 5):
        h = h0 * ramp[i] * opex[i]
        c = spot + (lv["pin"] - spot) * w[i]
        if floored:
            hi, lo = min(c + h, lv["callwall"] + 0.5 * h), max(c - h, lv["putwall"] - 0.5 * h)
        elif onfloor:
            hi, lo = min(c + h, lv["callwall"] + 0.0012 * spot), max(c - h, lv["putwall"] - 0.5 * h)
        else:
            hi, lo = min(c + h, lv["callwall"] + 0.0012 * spot), max(c - h, lv["putwall"])
        days.append(dict(d=["MON", "TUE", "WED", "THU", "FRI"][i],
                         lo=round(lo, dp), hi=round(hi, dp),
                         bodyLo=round(c - 0.25 * h, dp), bodyHi=round(c + 0.25 * h, dp),
                         dir=dirs[i], carry=round(carry, dp)))
        carry = c
    meta = dict(C=round(C, 2), dampf=round(dampf, 3), sigma=round(sig, 2),
                h_struct=round(h_struct, 2), h_real=round(h_real, 2), floored=floored,
                onfloor=onfloor, vexw=round(vw, 3), cont=round(C / sig, 2) if sig else None,
                pull=pull)
    return days, meta

# ------------------------------------------------------------------ renderer

W, H = 760, 680
PX0, PX1, AXR = 12, 748, 96
CL, CR, T, B, DAYY = 150, 736, 88, 536, 648
G, RD, A, M = "#3ddc84", "#ef5350", "#e8c14a", "#6a6a75"
STEPS = [0.25, 0.5, 1, 2, 2.5, 5, 10, 20, 25, 50, 100]
CHW = 0.60          # JetBrains Mono advance width per em


def tw(s, fs, ls=0):
    """Rendered text width; HTML entities count as one glyph."""
    n = len(s.replace("&#8594;", "X").replace("&#183;", "X").replace("&#215;", "X"))
    return n * fs * CHW + n * ls


def svg(d):
    dp = d["dp"]
    f = lambda v: ("%%.%df" % dp) % v if dp else str(round(v))
    proj = [x for x in d["days"] if not x.get("actual")]
    acts = [x["close"] for x in d["days"] if x.get("actual")]
    lo0 = min([x["lo"] for x in proj] + acts + [d["putwall"], d["brk"]])
    hi0 = max([x["hi"] for x in proj] + acts + [d["callwall"]])
    sp = hi0 - lo0
    rl, rh = lo0 - sp * .20, hi0 + sp * .20
    step = next((s for s in STEPS if (rh - rl) / s <= 7), 100)
    y0, y1 = (rl // step) * step, -((-rh) // step) * step
    Y = lambda v: B - (v - y0) / (y1 - y0) * (B - T)
    n = len(d["days"])
    cw = (CR - CL) / n
    CX = lambda i: CL + cw * (i + .5)
    sg = lambda v: ("+" if v >= d["spot"] else "") + "%.2f%%" % ((v / d["spot"] - 1) * 100)

    o = ['<svg viewBox="0 0 %d %d" width="100%%" role="img" aria-label="%s: projected daily '
         'high and low bands against the ceiling, floor and breakdown levels">' % (W, H, d["ticker"])]
    o.append('<rect x="%d" y="44" width="%d" height="568" rx="14" fill="#0e0e11" stroke="#1d1d22"/>'
             % (PX0, PX1 - PX0))
    v = y0
    while v <= y1 + 1e-9:
        o.append('<line x1="104" y1="%.1f" x2="%d" y2="%.1f" stroke="#18181c"/>'
                 '<text x="%d" y="%.1f" text-anchor="end" fill="%s" font-size="20">%s</text>'
                 % (Y(v), CR + 4, Y(v), AXR, Y(v) + 7, M, f(v)))
        v += step

    boxes, dm = [], []
    for i, p in enumerate(d["days"]):
        x = CX(i)
        if p.get("actual"):
            cy, pc = Y(p["close"]), p["pct"]
            col = G if pc >= 0 else RD
            dm.append('<rect x="%.1f" y="52" width="%.1f" height="%.1f" fill="#ffffff" opacity=".022"/>'
                      '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="4" opacity=".85"/>'
                      '<circle cx="%.1f" cy="%.1f" r="7" fill="%s" opacity=".85"/>'
                      % (CL + cw * i, cw, DAYY - 30, x - 34, cy, x + 34, cy, col, x, cy, col))
            vy, py = cy - 30, cy + 32
            for s_, yy, fs in ((f(p["close"]), vy, 24), ("%+.2f%%" % pc, py, 19)):
                ww = tw(s_, fs)
                boxes.append((x - ww / 2, yy - fs * .78, x + ww / 2, yy + fs * .26))
            dm.append('<text x="%.1f" y="%.1f" text-anchor="middle" fill="%s" font-size="24" font-weight="700">%s</text>'
                      '<text x="%.1f" y="%.1f" text-anchor="middle" fill="%s" font-size="19" opacity=".8">%+.2f%%</text>'
                      % (x, vy, col, f(p["close"]), x, py, col, pc))
            dm.append('<text x="%.1f" y="%d" text-anchor="middle" fill="#5d5d66" font-size="24" '
                      'font-weight="700" letter-spacing="2">%s</text>' % (x, DAYY, p["d"]))
            continue
        up = p["dir"] == "up"
        c = G if up else RD
        hv, hp = Y(p["hi"]) - 38, Y(p["hi"]) - 16
        lv_, lp = Y(p["lo"]) + 34, Y(p["lo"]) + 56
        for s_, yy, fs in ((f(p["hi"]), hv, 24), (sg(p["hi"]), hp, 19),
                           (f(p["lo"]), lv_, 24), (sg(p["lo"]), lp, 19)):
            ww = tw(s_, fs)
            boxes.append((x - ww / 2, yy - fs * .78, x + ww / 2, yy + fs * .26))
        dm.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#4a4a52" stroke-width="2"/>'
                  '<rect x="%.1f" y="%.1f" width="38" height="5" fill="%s"/>'
                  '<rect x="%.1f" y="%.1f" width="38" height="5" fill="%s"/>'
                  % (x, Y(p["hi"]), x, Y(p["lo"]), x - 19, Y(p["hi"]) - 2.5, G, x - 19, Y(p["lo"]) - 2.5, RD))
        dm.append('<text x="%.1f" y="%.1f" text-anchor="middle" fill="%s" font-size="24" font-weight="700">%s</text>'
                  '<text x="%.1f" y="%.1f" text-anchor="middle" fill="%s" font-size="19">%s</text>'
                  '<text x="%.1f" y="%.1f" text-anchor="middle" fill="%s" font-size="24" font-weight="700">%s</text>'
                  '<text x="%.1f" y="%.1f" text-anchor="middle" fill="%s" font-size="19">%s</text>'
                  % (x, hv, G, f(p["hi"]), x, hp, G, sg(p["hi"]),
                     x, lv_, RD, f(p["lo"]), x, lp, RD, sg(p["lo"])))
        by = Y(p["bodyHi"])
        bh = max(Y(p["bodyLo"]) - by, 18)
        dm.append('<rect x="%.1f" y="%.1f" width="80" height="%.1f" rx="7" fill="%s" fill-opacity=".72" '
                  'stroke="%s" stroke-width="2.5"/>'
                  '<circle cx="%.1f" cy="%.1f" r="6" fill="none" stroke="#8a8a94" stroke-width="2"/>'
                  % (x - 40, by, bh, c, c, x - 46, Y(p["carry"])))
        dm.append('<path d="M%.1f %.1f l9 -12 l9 12 z" fill="#0b0b0d"/>' % (x + 18, by + bh / 2 + 6) if up
                  else '<path d="M%.1f %.1f l9 12 l9 -12 z" fill="#0b0b0d"/>' % (x + 18, by + bh / 2 - 6))
        dm.append('<text x="%.1f" y="%d" text-anchor="middle" fill="#c8c8d0" font-size="24" '
                  'font-weight="700" letter-spacing="2">%s</text>' % (x, DAYY, p["d"]))
    o += dm

    # level labels: de-collide vertically, then dodge the day text
    FS, LS = 19, 1.4
    # The spot level is carried by the dashed line and the NOW pill at the left;
    # it needs no gutter label of its own.
    marks = [(d["callwall"], d["ceilLabel"], RD, 0),
             (d["putwall"], d["floorLabel"], G, 0), (d["brk"], "IF FLOOR BREAKS &#8594;", M, 2)]
    if abs(d["callwall"] - d["pin"]) / d["spot"] >= .0015:
        marks.insert(1, (d["pin"], "PIN", A, 0))
    marks.sort(key=lambda m: -m[0])
    ys = [Y(m[0]) for m in marks]
    for i in range(1, len(ys)):
        if ys[i] - ys[i - 1] < 34:
            ys[i] = ys[i - 1] + 34
    shift = max(0, ys[-1] - (B + 58))
    ys = [y - shift for y in ys]
    widths = [tw(m[1], FS, LS) + 14 for m in marks]

    def clash(j, y):
        bx = (CR - widths[j], y - 16, CR + 2, y + 16)
        for b in boxes:
            if not (bx[2] < b[0] or bx[0] > b[2] or bx[3] < b[1] or bx[1] > b[3]):
                return True
        for k, yk in enumerate(ys):
            if k != j and abs(yk - y) < 34:
                return True
        return y < T - 28 or y > B + 58
    for j in range(len(ys)):
        if clash(j, ys[j]):
            for off in [o_ * s_ for o_ in range(6, 120, 6) for s_ in (-1, 1)]:
                if not clash(j, ys[j] + off):
                    ys[j] += off
                    break
    for (val, lab, col, kind), ya in zip(marks, ys):
        yt = Y(val)
        ww = tw(lab, FS, LS) + 14
        x0 = CR - ww
        dash = ' stroke-dasharray="4 5"' if kind == 2 else (' stroke-dasharray="7 6"' if kind == 1 else "")
        o.append('<line x1="104" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.4" opacity=".65"%s/>'
                 % (yt, CR + 4, yt, col, dash))
        if abs(ya - yt) > 2:
            o.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="1.2" opacity=".5" fill="none"/>'
                     '<path d="M%.1f %.1f L%.1f %.1f L104 %.1f" stroke="%s" stroke-width="1" opacity=".3" fill="none"/>'
                     % (x0 - 16, ya, x0 - 6, ya, col, x0 - 16, ya, x0 - 28, yt, yt, col))
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="32" rx="4" fill="#0b0b0d"/>'
                 '<text x="%d" y="%.1f" text-anchor="end" fill="%s" font-size="%d" letter-spacing="%s">%s</text>'
                 % (x0, ya - 16, ww + 4, CR, ya + 7, col, FS, LS, lab))

    nl = "NOW %s" % f(d["spot"])
    nw = tw(nl, 19) + 26
    ny = Y(d["spot"])
    # dashed spot line, previously drawn as part of the (now removed) gutter mark
    o.append('<line x1="104" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.4" '
             'opacity=".65" stroke-dasharray="7 6"/>' % (ny, CR + 4, ny, A))
    o.append('<rect x="16" y="%.1f" width="%.1f" height="32" rx="8" fill="%s"/>'
             '<text x="%.1f" y="%.1f" text-anchor="middle" fill="#231d05" font-size="19" font-weight="700">%s</text>'
             % (ny - 16, nw, A, 16 + nw / 2, ny + 7, nl))
    return "".join(o) + "</svg>"

# ------------------------------------------------------------------- assembly

CSS = """/* single column: thin masthead, then headline + stat line + full-bleed chart per index */
:root{
 --bg:#09090b; --panel:#0e0e11; --line:#1d1d22; --ink:#e8e8ec; --dim:#72727d;
 --up:#3ddc84; --dn:#ef5350; --mark:#e8c14a;
 --mono:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
 color-scheme:dark;
}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--mono);margin:0}
.wrap{max-width:860px;margin:0 auto;padding-block:24px 48px;padding-left:16px;padding-right:16px;
 display:flex;flex-direction:column;gap:40px}
.stamp{font-size:10.5px;color:var(--dim);letter-spacing:1.4px;line-height:1.8;margin:0;
 border-bottom:1px solid var(--line);padding-bottom:14px}
.stamp b{color:var(--dn);font-weight:700}
section{display:flex;flex-direction:column;gap:10px}
h2{font-size:26px;font-weight:700;letter-spacing:-.6px;margin:0;text-wrap:balance;line-height:1.2}
h2.dn{color:var(--dn)} h2.up{color:var(--up)}
.ssub{font-size:12px;color:var(--dim);margin:0}
.rail{font-size:11px;color:var(--ink);margin:2px 0 4px;line-height:2.1}
.rail em{font-style:normal;color:var(--dim);letter-spacing:.6px}
.rail .sep{color:#2e2e34}
.rail .warn{color:var(--mark)} .rail .warn em{color:var(--mark);opacity:.6}
.rail .bad{color:var(--dn);font-weight:700} .rail .bad em{color:var(--dn);opacity:.6;font-weight:400}
.plot svg{display:block;width:100%;height:auto}
.note{font-size:11px;color:var(--dim);line-height:1.85;margin:4px 0 0;max-width:70ch}
footer{border-top:1px solid var(--line);padding-top:16px;font-size:11px;color:var(--dim);
 line-height:1.9;max-width:76ch}
footer b{color:#9a9aa4;font-weight:500}
@media (max-width:520px){h2{font-size:20px} .wrap{gap:32px}}"""

DAYNAMES = ["MON", "TUE", "WED", "THU", "FRI"]


def rail(items):
    return ('<p class="rail">' + ' <span class="sep">&#183;</span> '.join(
        '<span class="s%s"><em>%s</em> %s</span>' % ((" " + c) if c else "", k, v)
        for k, v, c in items) + "</p>")


def fmt(v, dp):
    return ("%%.%df" % dp) % v if dp else str(int(round(v)))


def one(tag, ser, lv, spot, dp, dampf, sig, vw, vexflip, nobid, wk_start, cap_date,
        blend=None, extra="", pull=None):
    """Assemble one chart's data object, rail and note."""
    if pull is None:
        pull = pin_pull(ser[-1][1])
    # week[0] is the next trading day; its weekday is how many days already closed.
    monday = wk_start - dt.timedelta(days=wk_start.weekday())
    n_done = wk_start.weekday()
    dates = [d for d, _ in ser]
    by_date = {d: r for d, r in ser}
    actuals = []
    for i in range(n_done):
        key = (monday + dt.timedelta(days=i)).isoformat()
        if key not in by_date:                     # holiday or missing capture
            continue
        j = dates.index(key)
        prev = ser[j - 1][1]["spot"] if j else by_date[key]["spot"]
        cur = by_date[key]["spot"]
        actuals.append(dict(d=DAYNAMES[i], actual=1, close=round(cur, dp),
                            pct=(cur / prev - 1) * 100))
    n_done = len(actuals)
    gexstr = ser[-1][1]["gexstr"]
    dirs = directions(ser, gexstr, lv["pin"], spot)
    days, meta = project(lv, spot, sig, vw, dirs, dp, dampf, nobid, n_done, pull=pull)
    cont = meta["cont"]
    d = dict(ticker=tag, dp=dp, spot=round(spot, dp), pin=round(lv["pin"], dp),
             callwall=round(lv["callwall"], dp), putwall=round(lv["putwall"], dp),
             brk=round(lv["brk"], dp), ceilLabel="CALL WALL / PIN",
             floorLabel="PUT WALL / FLOOR", days=actuals + days,
             headline=headline(tag, lv, spot, cont or 99, nobid, ser, vexflip))
    scores = [r["score"] for _, r in ser][-5:]
    tight = lambda a, b: "bad" if abs(a - b) <= 0.0015 * spot else ""
    r = rail([("CEILING / PIN", fmt(lv["callwall"], dp), ""),
              ("FLOOR", fmt(lv["putwall"], dp), tight(spot, lv["putwall"])),
              ("BREAKDOWN", fmt(lv["brk"], dp), tight(spot, lv["brk"])),
              ("BIAS", fmt(lv["flip"], dp), "warn" if spot < lv["flip"] else ""),
              ("CORRIDOR", "%s vs %s daily" % (fmt(meta["C"], dp), fmt(meta["sigma"], dp)), ""),
              ("SETUP SCORE", "%d &#8594; %d" % (scores[0], scores[-1]),
               "bad" if scores[-1] < scores[0] - 20 else "")])
    bits = []
    if blend:
        bits.append("Blended read: SPX %.1f%% / SPY %.1f%% by positioning strength, SPY scaled at "
                    "the live %.4f basis." % (blend[0] * 100, blend[1] * 100, blend[2]))
    else:
        bits.append("Standalone, no blend.")
    if meta["floored"]:
        bits.append("The corridor is narrower than a normal session, so bands are floored to "
                    "realised movement and the wall clip is released.")
    else:
        bits.append("Structural width governs: %s of corridor against %s of average daily movement."
                    % (fmt(meta["C"], dp), fmt(meta["sigma"], dp)))
    if not pull:
        bits.append("Positioning is short or weak, so the bands are centred on the close and the "
                    "pin is treated as a ceiling, not a target.")
    if meta["onfloor"]:
        bits.append("No bid near spot and spot already on the put wall, so the lower clip is "
                    "released rather than printing identical lows.")
    if spot < lv["flip"]:
        bits.append("Spot sits %s under the bias boundary." % fmt(lv["flip"] - spot, dp))
    if vexflip:
        bits.append("Net vol exposure turned negative in this capture — used as magnitude for "
                    "band width and flagged as a regime signal.")
    if extra:
        bits.append(extra)
    return d, r, " ".join(bits), meta


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else None
    files = load(date)
    cap = json.load(open(files[-1]))
    cap_date = dt.date.fromisoformat(os.path.basename(files[-1])[12:22])
    wk_start = dt.date.fromisoformat(cap["week"][0])
    wk_end = dt.date.fromisoformat(cap["week"][1])
    spx, spy, qqq = series(files, "SPX"), series(files, "SPY"), series(files, "QQQ")
    S, Y, Q = spx[-1][1], spy[-1][1], qqq[-1][1]

    # SPX / SPY blended, at the live basis and weighted by positioning strength
    k = S["spot"] / Y["spot"]
    wS = S["gexstr"] / (S["gexstr"] + Y["gexstr"])
    wY = 1 - wS
    bl = lambda fld: wS * S[fld] + wY * (Y[fld] * k)
    lvS = dict(pin=bl("pin"), callwall=bl("callwall"), putwall=bl("putwall"),
               brk=bl("brk"), flip=bl("flip"))
    vS, fS = vex_weight(spx)
    vY, fY = vex_weight(spy)
    dS, rS, nS, mS = one("SPX", spx, lvS, S["spot"], 0,
                         wS * damping(S) + wY * damping(Y),
                         wS * sigma(spx) + wY * (sigma(spy) * k), wS * vS + wY * vY,
                         fS or fY, S["buydip"] is None and Y["buydip"] is None,
                         wk_start, cap_date, blend=(wS, wY, k),
                         pull=pin_pull(S) and pin_pull(Y))
    lvY = dict(pin=Y["pin"], callwall=Y["callwall"], putwall=Y["putwall"],
               brk=Y["brk"], flip=Y["flip"])
    dY, rY, nY, mY = one("SPY", spy, lvY, Y["spot"], 2, damping(Y), sigma(spy), vY, fY,
                         Y["buydip"] is None, wk_start, cap_date,
                         extra="The same book that supplies part of the blend above, shown on its "
                               "own scale; net contracts %sK." % round(Y["netK"], 1))
    lvQ = dict(pin=Q["pin"], callwall=Q["callwall"], putwall=Q["putwall"],
               brk=Q["brk"], flip=Q["flip"])
    vQ, fQ = vex_weight(qqq)
    dQ, rQ, nQ, mQ = one("QQQ", qqq, lvQ, Q["spot"], 2, damping(Q), sigma(qqq), vQ, fQ,
                         Q["buydip"] is None, wk_start, cap_date)

    mid = wk_start.weekday() > 0
    monday = wk_start - dt.timedelta(days=wk_start.weekday())
    friday = monday + dt.timedelta(days=4)
    wk_end = max(wk_end, friday)
    stamp = ("WEEKLY EXPECTED MOVE &#183; %s&#8211;%s %s<br>DEALER EDGE %s &#183; EXPIRY %s%s<br>%s"
             % (monday.strftime("%d").lstrip("0"), wk_end.strftime("%d").lstrip("0"),
                wk_end.strftime("%b %Y").upper(), cap_date.isoformat(), S["exp"],
                " &#183; <b>MID-WEEK REBUILD</b>" if mid else "",
                "DAYS CLOSED SHOW ACTUALS &#183; REMAINDER PROJECTED" if mid
                else "ALL FIVE DAYS PROJECTED"))

    secs = []
    for d, r, note in ((dS, rS, nS), (dY, rY, nY), (dQ, rQ, nQ)):
        cls = "dn" if d["headline"] not in ("The corridor is lifting.", "The pin's still in charge.") else "up"
        secs.append('<section><h2 class="%s">%s</h2>'
                    '<p class="ssub">%s &#183; spot %s at the %s close</p>%s'
                    '<div class="plot">%s</div><p class="note">%s</p></section>'
                    % (cls, d["headline"], d["ticker"], fmt(d["spot"], d["dp"]),
                       cap_date.strftime("%A"), r, svg(d), note))

    html = ("""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Weekly Expected Move %s</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap">
<style>%s</style></head><body><div class="wrap">
<p class="stamp">%s</p>
%s
<footer>
<b>SPX and SPY.</b> The first chart blends both books at the live basis and prints in index points;
the second is SPY alone in dollars. One underlying, two order books &#8212; read the blend for the
level and SPY for the cash instrument. QQQ is standalone.<br>
<b>Reading the chart.</b> The whisker is the projected daily high and low; percentages are against
the capture&#8217;s close. The filled box is the expected settlement band, green for an up-biased day
and red for a down-biased one, with the hollow circle carrying in the previous day&#8217;s projected
close. Days already closed show the actual close against a lighter column &#8212; the captures carry
no intraday range, so no high or low is drawn for those. Friday widens for its expiry.<br>
<b>Where the bands come from.</b> 40%% of the corridor between ceiling and floor, damped for regime,
floored to realised movement when the walls are narrower than a normal session.<br>
<b>Built</b> %s from dealer-edge-%s.json. Rebuilt automatically whenever a new capture lands.
</footer></div></body></html>""" % (monday.strftime("%-d %b"), CSS, stamp, "\n".join(secs),
                                    dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%MZ"),
                                    cap_date.isoformat()))
    open(OUT, "w").write(html)
    print("wrote %s  (%d bytes)" % (OUT, len(html)))
    for t, m in (("SPX", mS), ("SPY", mY), ("QQQ", mQ)):
        print("  %-4s %s" % (t, json.dumps(m)))


if __name__ == "__main__":
    main()
