#!/usr/bin/env python3
"""Build the Key Levels page from a TradeEcho gamma-analysis keyLevels capture.

Usage: python3 key-levels/build.py [data/key-levels/raw/YYYY-MM-DD.json]
Writes key-levels/index.html. Uses the newest raw file when none is given.

Field map (same numbers TradeEcho's Cortex chat quotes):
  spot -> price reference, anchorPoint -> anchor, flipPoint -> flip,
  charmAnchor -> drift target, defenseLines -> defense lines (TradeEcho order),
  vannaAnchor / vannaFlip -> vol-shift magnet / pivot.
"""
import datetime as dt, glob, html, json, os, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
RAW = os.path.join(REPO, "data", "key-levels", "raw")
src = sys.argv[1] if len(sys.argv) > 1 else sorted(glob.glob(os.path.join(RAW, "*.json")))[-1]
D = json.load(open(src))
ET = ZoneInfo("America/New_York")
cap = dt.datetime.fromisoformat(D["capturedAt"].replace("Z", "+00:00")).astimezone(ET)
groups = D.get("groups") or {"Tickers": list(D["tickers"])}


def px(v):
    if v is None:
        return "—"
    return f"{v:,.0f}" if v >= 1000 else (f"{v:,.2f}".rstrip("0").rstrip(".") if v % 1 else f"{v:,.0f}")


def pct(a, b):
    return (a / b - 1) * 100


def derive(t, r):
    k, s = r["kl"], r["spot"]
    flip, anc, drift = k.get("flipPoint"), k.get("anchorPoint"), k.get("charmAnchor")
    dl = k.get("defenseLines") or []
    below = sorted([x for x in dl if x <= s], reverse=True)
    above = sorted([x for x in dl if x > s])
    fd = pct(s, flip) if flip else None
    if fd is None:
        regime, tone = "no flip", "mid"
    elif abs(fd) < 0.4:
        regime, tone = "on the flip", "mid"
    elif fd > 0:
        regime, tone = "above flip", "pos"
    else:
        regime, tone = "below flip", "neg"
    # plain-language read, built only from the numbers
    parts = []
    if fd is not None:
        if tone == "mid":
            parts.append(f"Sitting on the flip at {px(flip)}; direction undecided until it clears.")
        elif tone == "pos":
            parts.append(f"{fd:.1f}% above the flip at {px(flip)}: dips tend to get bought while it holds.")
        else:
            parts.append(f"{abs(fd):.1f}% below the flip at {px(flip)}: moves tend to run further until it is reclaimed.")
    if anc:
        ad = pct(anc, s)
        parts.append(f"On the anchor at {px(anc)}." if abs(ad) < 0.5 else
                     f"Anchor {px(anc)} is {abs(ad):.1f}% {'above' if ad > 0 else 'below'}.")
    if below:
        parts.append(f"First defense below {px(below[0])}" + (f", then {px(below[1])}." if len(below) > 1 else "."))
    else:
        parts.append("No defense line below price.")
    if above:
        parts.append(f"Nearest line above {px(above[0])}.")
    if drift:
        dd = pct(drift, s)
        parts.append(f"Drift target {px(drift)} ({dd:+.1f}%).")
    return dict(t=t, s=s, flip=flip, anc=anc, drift=drift, dl=dl, below=below, above=above, fd=fd,
                regime=regime, tone=tone, read=" ".join(parts), rating=r.get("rating"),
                vmag=k.get("vannaAnchor"), vsign=k.get("vannaAnchorSign"), vflip=k.get("vannaFlip"),
                vwalls=[w["strike"] for w in (k.get("vannaWalls") or [])], pos=r.get("posDate"))


def ladder(d):
    pts = [d["s"]] + [x for x in [d["flip"], d["anc"], d["drift"]] + d["dl"] if x]
    lo, hi = min(pts), max(pts)
    pad = (hi - lo) * 0.06 or d["s"] * 0.02
    lo, hi = lo - pad, hi + pad
    W, H = 320, 46
    X = lambda v: round(8 + (v - lo) / (hi - lo) * (W - 16), 1)
    g = [f'<line x1="8" y1="24" x2="{W-8}" y2="24" class="ax"/>']
    for v in d["dl"]:
        g.append(f'<line x1="{X(v)}" y1="15" x2="{X(v)}" y2="33" class="{"dl-b" if v <= d["s"] else "dl-a"}"/>')
    if d["flip"]:
        g.append(f'<line x1="{X(d["flip"])}" y1="6" x2="{X(d["flip"])}" y2="42" class="fl"/>')
    if d["drift"]:
        x = X(d["drift"]); g.append(f'<path d="M{x-5} 8 L{x+5} 8 L{x} 15 Z" class="dr"/>')
    if d["anc"]:
        x = X(d["anc"]); g.append(f'<path d="M{x} 33 L{x+5} 38 L{x} 43 L{x-5} 38 Z" class="an"/>')
    g.append(f'<circle cx="{X(d["s"])}" cy="24" r="5" class="sp"/>')
    return (f'<svg viewBox="0 0 {W} {H}" class="lad" role="img" aria-label="Level ladder for {d["t"]}">'
            + "".join(g) + "</svg>")


rows, sections = [], []
for gname, tks in groups.items():
    cards = []
    for t in tks:
        r = D["tickers"].get(t)
        if not r or "error" in r:
            cards.append(f'<article class="card"><h3>{t}</h3><p class="read">No data: {html.escape(str(r and r.get("error")))}</p></article>')
            continue
        d = derive(t, r)
        rows.append(
            f'<tr data-tk="{t}" data-group="{html.escape(gname)}"><th>{t}</th><td>{px(d["s"])}</td><td><span class="pill {d["tone"]}">{d["regime"]}</span></td>'
            f'<td>{px(d["flip"])}</td><td>{px(d["anc"])}</td><td>{px(d["drift"])}</td>'
            f'<td>{px(d["below"][0]) if d["below"] else "—"}</td><td>{px(d["above"][0]) if d["above"] else "—"}</td>'
            '</tr>')
        chips = "".join(f'<span class="chip {"b" if v <= d["s"] else "a"}">{px(v)}</span>' for v in d["dl"])
        vm = px(d["vmag"]) + (" (pushes away)" if d["vsign"] == -1 else "")
        cards.append(f'''<article class="card">
  <header><h3>{t}</h3><span class="spot">{px(d["s"])}</span><span class="pill {d["tone"]}">{d["regime"]}</span><span class="rt" title="Rating, 1 to 5">rating {d["rating"]}/5</span></header>
  {ladder(d)}
  <dl class="kv">
    <div><dt>Anchor</dt><dd>{px(d["anc"])}</dd></div>
    <div><dt>Flip</dt><dd>{px(d["flip"])}</dd></div>
    <div><dt>Drift target</dt><dd>{px(d["drift"])}</dd></div>
    <div class="wide"><dt>Defense lines</dt><dd class="chips">{chips}</dd></div>
    <div><dt>Vol-shift magnet</dt><dd>{vm}</dd></div>
    <div><dt>Vol-shift pivot</dt><dd>{px(d["vflip"])}</dd></div>
    <div><dt>Vol-shift walls</dt><dd>{", ".join(px(w) for w in d["vwalls"]) or "—"}</dd></div>
  </dl>
  <p class="read">{html.escape(d["read"])}</p>
</article>''')
    sections.append(f'<section><h2>{gname}</h2><div class="grid">{"".join(cards)}</div></section>')

pos = {r.get("posDate") for r in D["tickers"].values() if isinstance(r, dict)} - {None}
stamp = cap.strftime("%a %d %b %Y, %-I:%M %p ET")
tpl = open(os.path.join(HERE, "template.html")).read()
out = (tpl.replace("{{STAMP}}", stamp)
          .replace("{{POSDATE}}", ", ".join(sorted(pos)) or "—")
          .replace("{{ROWS}}", "\n".join(rows))
          .replace("{{OPTIONS}}", "".join(
              f'<optgroup label="{html.escape(g)}"><option value="g:{html.escape(g)}">All {html.escape(g.lower())}</option>'
              + "".join(f'<option value="t:{t}">{t}</option>' for t in tks if t in D["tickers"]) + "</optgroup>"
              for g, tks in groups.items()))
          .replace("{{SECTIONS}}", "\n".join(sections)))
dst = os.path.join(HERE, "index.html")
open(dst, "w").write(out)
print(dst)
