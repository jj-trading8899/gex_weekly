#!/usr/bin/env python3
"""
Render terrashade/index.html from the most recent snapshot written by fetch_levels.py.

TerraShade data only. Nothing from Dealer Edge or TradeEcho is read or displayed here.
Stdlib only.
"""

import datetime as dt
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "index.html")

FLAG_TEXT = {
    "stale": "chain {age} old",
    "wide": "corridor {width}% wide",
    "no_boundary": "no bias boundary",
    "band_excludes": "day range excludes spot",
}


def latest_snapshot():
    files = sorted(glob.glob(os.path.join(HERE, "data", "terrashade-*.json")))
    if not files:
        print("no snapshots in terrashade/data", file=sys.stderr)
        sys.exit(1)
    with open(files[-1]) as fh:
        return json.load(fh), os.path.basename(files[-1])


def num(v, dp=2):
    if v is None:
        return "&mdash;"
    s = "{:,.{}f}".format(v, dp)
    return s.rstrip("0").rstrip(".") if "." in s else s


def age_str(mins):
    if mins is None:
        return "&mdash;"
    return "%dh%02dm" % (mins // 60, mins % 60)


def flag_pills(row):
    if not row.get("flags"):
        return '<span class="flag ok">clean</span>'
    out = []
    for f in row["flags"]:
        txt = FLAG_TEXT.get(f, f).format(
            age=age_str(row.get("chain_age_min")),
            width="%.0f" % (row.get("corridor_width_pct") or 0))
        out.append('<span class="flag %s">%s</span>' % (f, txt))
    return "".join(out)


def row_html(r):
    chg = r.get("chg_pct") or 0
    chg_cls = "up" if chg > 0 else ("dn" if chg < 0 else "")
    bias = {"long": '<span class="bias long">Long</span>',
            "short": '<span class="bias short">Short</span>'}.get(
                r.get("bias"), '<span class="bias none">&mdash;</span>')

    pos, bar = None, ""
    pw, cw, spot = r.get("put_wall"), r.get("call_wall"), r.get("spot")
    if None not in (pw, cw, spot) and cw > pw:
        pos = max(0.0, min(1.0, (spot - pw) / (cw - pw)))
        bar = ('<div class="bar"><div class="bar-dot" style="left:%.1f%%"></div></div>' % (pos * 100))

    em = r.get("expected_moves") or {}
    d, m = em.get("daily") or {}, em.get("monthly") or {}
    return """<tr>
<td class="tk">{t}</td><td class="n">{spot}</td><td class="n {cc}">{chg:+.2f}%</td>
<td class="n sup">{pw}</td><td class="n res">{cw}</td><td class="barcell">{bar}</td>
<td class="n">{bb}</td><td>{bias}</td><td class="n">{anchor}</td>
<td class="n dim">{dl} &ndash; {dh}</td><td class="n dim">{ml} &ndash; {mh}</td>
<td class="n dim">{age}</td><td class="flags">{flags}</td></tr>""".format(
        t=r["ticker"], spot=num(spot), cc=chg_cls, chg=chg,
        pw=num(pw), cw=num(cw), bar=bar, bb=num(r.get("bias_boundary")), bias=bias,
        anchor=num(r.get("anchor_strike")),
        dl=num(d.get("low")), dh=num(d.get("high")),
        ml=num(m.get("low")), mh=num(m.get("high")),
        age=age_str(r.get("chain_age_min")), flags=flag_pills(r))


def section(title, sub, items, tone):
    if not items:
        return ""
    return """<section class="grp {tone}">
<div class="grp-head"><h2>{title}<span class="cnt">{n}</span></h2><p>{sub}</p></div>
<div class="tablewrap"><table><thead><tr>
<th>Ticker</th><th class="n">Spot</th><th class="n">Chg</th><th class="n">Floor</th>
<th class="n">Ceiling</th><th>Position</th><th class="n">Bias line</th><th>Bias</th>
<th class="n">Anchor</th><th class="n">Day range</th><th class="n">Month range</th>
<th class="n">Chain age</th><th>Quality</th>
</tr></thead><tbody>{body}</tbody></table></div></section>""".format(
        tone=tone, title=title, n=len(items), sub=sub,
        body="".join(row_html(r) for r in items))


def build():
    doc, fname = latest_snapshot()
    rows = doc["rows"]
    ok = [r for r in rows if r["status"] == "ok"]
    missing = [r["ticker"] for r in rows if r["status"] != "ok"]

    clean = sorted([r for r in ok if len(r["flags"]) == 0], key=lambda r: r["ticker"])
    warn = sorted([r for r in ok if len(r["flags"]) == 1], key=lambda r: r["ticker"])
    bad = sorted([r for r in ok if len(r["flags"]) > 1], key=lambda r: r["ticker"])

    th = doc.get("thresholds", {"stale_minutes": 60, "wide_corridor_pct": 12})
    built = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M")

    nodata = ""
    if missing:
        nodata = """<section class="grp bad">
<div class="grp-head"><h2>No data<span class="cnt">%d</span></h2>
<p>Returned a build-pending response and never resolved on retry.</p></div>
<div class="nodata"><div class="syms">%s</div>
<p>The unavailable set moves between runs. Some of these serve levels on other days,
so treat coverage as a per-run fact rather than a fixed list.</p></div></section>""" % (
            len(missing), " &middot; ".join(missing))

    html = HEAD + """
<header>
<h1>TerraShade &mdash; Key Levels</h1>
<p class="src">SOURCE <b>terrashade.onrender.com</b> &middot; PULLED {pulled} &middot; SNAPSHOT <b>{fname}</b> &middot; PAGE BUILT {built}Z</p>
</header>

<div class="kpis">
<div class="kpi g"><div class="v">{nclean}</div><div class="k">Clean</div></div>
<div class="kpi a"><div class="v">{nwarn}</div><div class="k">One flag</div></div>
<div class="kpi r"><div class="v">{nbad}</div><div class="k">Multiple flags</div></div>
<div class="kpi r"><div class="v">{nmiss}</div><div class="k">No data</div></div>
<div class="kpi"><div class="v">{nok}</div><div class="k">Returned</div></div>
</div>

{s1}{s2}{s3}{nodata}

<footer>
<b>Floor / Ceiling</b> &mdash; heaviest put-side support at or below spot, heaviest call-side resistance at or above spot.
<b>Position</b> &mdash; where spot sits between the two.
<b>Bias line</b> &mdash; the price where dealer positioning flips; above it hedging dampens moves, below it hedging extends them.
<b>Anchor</b> &mdash; single largest positioning strike across all expirations.<br>
<b>Flag rules</b> &mdash; stale: chain older than {stale} min at pull &middot;
wide: corridor over {wide:.0f}% of spot &middot;
no bias boundary: none found within &plusmn;15% of spot &middot;
day range excludes spot: expected-move band does not contain the live price, which indicates the chain behind it is out of date.<br>
Open interest only; same-session flow is not reflected. TerraShade data exclusively &mdash; no other provider is mixed in.
</footer>

</div></body></html>""".format(
        pulled=doc.get("pulled_at", "?"), fname=fname, built=built,
        nclean=len(clean), nwarn=len(warn), nbad=len(bad), nmiss=len(missing), nok=len(ok),
        s1=section("Clean", "Chain fresh, corridor usable, bias line present, day range brackets spot.", clean, "good"),
        s2=section("One flag", "Usable with the noted caveat in mind.", warn, "warn"),
        s3=section("Multiple flags", "Do not trade off these levels without re-pulling first.", bad, "bad"),
        nodata=nodata, stale=th["stale_minutes"], wide=th["wide_corridor_pct"])

    with open(OUT, "w") as fh:
        fh.write(html)
    print("wrote %s  (clean %d / warn %d / bad %d / missing %d)" % (
        OUT, len(clean), len(warn), len(bad), len(missing)), file=sys.stderr)


HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TerraShade Key Levels</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0d1117;--card:#161b22;--line:#222b36;--line2:#1b232d;
--txt:#e6edf3;--dim:#8b949e;--faint:#5c6672;
--grn:#3fb950;--red:#f85149;--amb:#d29922;--cyan:#39c5cf;--violet:#a371f7;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--txt);
font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:14px;line-height:1.5;
-webkit-font-smoothing:antialiased;padding:28px 20px 60px}
.wrap{max-width:1340px;margin:0 auto}
header{border-bottom:1px solid var(--line);padding-bottom:18px;margin-bottom:24px}
h1{font-size:21px;font-weight:600;margin:0 0 4px;letter-spacing:-.01em}
.src{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--dim);margin:0}
.src b{color:var(--cyan);font-weight:500}
.kpis{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0 26px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 16px;min-width:132px;flex:1}
.kpi .v{font-family:'JetBrains Mono',monospace;font-size:22px;font-weight:700;line-height:1.1}
.kpi .k{font-size:11px;color:var(--dim);text-transform:uppercase;letter-spacing:.07em;margin-top:5px}
.kpi.g .v{color:var(--grn)} .kpi.a .v{color:var(--amb)} .kpi.r .v{color:var(--red)}
.grp{margin-bottom:30px}
.grp-head{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:10px;
padding-left:11px;border-left:3px solid var(--line)}
.grp.good .grp-head{border-color:var(--grn)}
.grp.warn .grp-head{border-color:var(--amb)}
.grp.bad .grp-head{border-color:var(--red)}
.grp h2{font-size:14.5px;font-weight:600;margin:0;display:flex;align-items:center;gap:9px}
.cnt{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--dim);
background:var(--card);border:1px solid var(--line);border-radius:20px;padding:1px 9px}
.grp-head p{margin:0;font-size:12.5px;color:var(--dim)}
.tablewrap{background:var(--card);border:1px solid var(--line);border-radius:9px;overflow-x:auto}
table{width:100%;border-collapse:collapse;white-space:nowrap}
th{font-size:10.5px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;
color:var(--faint);text-align:left;padding:11px 13px;border-bottom:1px solid var(--line);
background:#12171e;position:sticky;top:0}
td{padding:9px 13px;border-bottom:1px solid var(--line2);font-size:13px}
tr:last-child td{border-bottom:none}
tbody tr:hover{background:#1a212b}
.n{font-family:'JetBrains Mono',monospace;text-align:right}
th.n{text-align:right}
.tk{font-family:'JetBrains Mono',monospace;font-weight:700;letter-spacing:.02em}
.up{color:var(--grn)} .dn{color:var(--red)}
.sup{color:var(--grn)} .res{color:var(--red)}
.dim{color:var(--dim);font-size:12px}
.bias{font-family:'JetBrains Mono',monospace;font-size:10.5px;font-weight:700;
padding:2px 8px;border-radius:4px;letter-spacing:.04em}
.bias.long{background:rgba(63,185,80,.14);color:var(--grn)}
.bias.short{background:rgba(248,81,73,.14);color:var(--red)}
.bias.none{color:var(--faint)}
.barcell{width:96px;min-width:96px}
.bar{position:relative;height:5px;border-radius:3px;
background:linear-gradient(90deg,rgba(63,185,80,.45),rgba(130,130,140,.3),rgba(248,81,73,.45))}
.bar-dot{position:absolute;top:50%;width:8px;height:8px;border-radius:50%;
background:var(--txt);border:1.5px solid var(--bg);transform:translate(-50%,-50%)}
.flags{white-space:normal;min-width:210px}
.flag{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:10px;
padding:2px 7px;border-radius:4px;margin:1px 3px 1px 0;letter-spacing:.02em}
.flag.ok{background:rgba(63,185,80,.11);color:var(--grn)}
.flag.stale{background:rgba(210,153,34,.13);color:var(--amb)}
.flag.wide{background:rgba(163,113,247,.13);color:var(--violet)}
.flag.no_boundary{background:rgba(139,148,158,.13);color:var(--dim)}
.flag.band_excludes{background:rgba(248,81,73,.13);color:var(--red)}
.nodata{background:var(--card);border:1px solid var(--line);border-radius:9px;padding:15px 17px}
.nodata .syms{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--red);
font-weight:500;letter-spacing:.04em;margin-bottom:6px}
.nodata p{margin:0;font-size:12.5px;color:var(--dim)}
footer{margin-top:34px;padding-top:16px;border-top:1px solid var(--line);
font-size:11.5px;color:var(--faint);line-height:1.7}
footer b{color:var(--dim);font-weight:500}
@media(max-width:720px){body{padding:18px 12px 44px} .kpi{min-width:104px}}
</style></head>
<body><div class="wrap">"""


if __name__ == "__main__":
    build()
