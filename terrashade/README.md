# TerraShade monitor

Self-contained. Pulls key levels from TerraShade, grades each ticker, writes a
dated snapshot and rebuilds a dark-mode page.

**This folder never reads or writes Dealer Edge / TradeEcho data.** Keeping the two
apart is the point — compare them deliberately, not by accident.

## No credentials

TerraShade's API is open: no key, no cookie, no login, `access-control-allow-origin: *`.
Nothing here needs a secret and nothing should be added. (Skylit and TradeEcho do need
auth — those are different pipelines.)

## Layout

```
terrashade/
  config.json        tickers, thresholds, holiday list
  fetch_levels.py    pulls /api/levels, grades rows, writes a snapshot
  build_page.py      renders index.html from the newest snapshot
  index.html         generated — do not hand-edit
  data/
    terrashade-YYYY-MM-DD.json                   end-of-day sweep
    gexhist/terrashade-gexhist-YYYY-MM-DD.json   intraday wall path, captured once
    intraday/terrashade-intraday-YYYY-MM-DD.json only if hourly polling is enabled
```

## Running

```bash
python terrashade/fetch_levels.py --mode eod     # full list, weekday guard applies
python terrashade/fetch_levels.py --mode eod --force
python terrashade/fetch_levels.py --mode intraday
python terrashade/build_page.py
```

Stdlib only. No `pip install`. The sweep takes about four minutes — TerraShade's
origin is a single-threaded Python server on a free Render tier, so requests are
serialised with a delay rather than fired in parallel.

## Schedule

`.github/workflows/terrashade.yml` runs the full sweep at **21:50 UTC, Mon–Fri**.
That is after the US close in both DST regimes (17:50 ET summer, 16:50 ET winter),
so one cron entry covers the year. Weekends and the holiday list in `config.json`
are skipped by the script, which is belt-and-braces on top of the `1-5` cron.

## Quality flags

Graded at write time, so the stored JSON is already marked up.

| Flag | Meaning |
|---|---|
| `stale` | `chain_as_of` older than `stale_minutes` at pull time |
| `wide` | corridor (ceiling − floor) over `wide_corridor_pct` of spot |
| `no_boundary` | no bias boundary found within ±15% of spot |
| `band_excludes` | the daily expected-move band does not contain spot |
| `no_data` | the ticker returned a build-pending response and never resolved |

`band_excludes` is the most useful of these. It catches a chain that is out of date
even when the timestamp looks acceptable, because the expected-move band is derived
from the chain while spot is live — if the band no longer contains the price, the
levels behind it are old. On the 2026-10-15 seed run it caught GLD, SOXL, AAOI and SNDK.

Baseline from that run: **60 requested, 52 returned, 30 clean, 8 no data.**

## Why there is no hourly job by default

TerraShade already records its own intraday history. `/api/gexhist` returns today's
opening snapshot plus roughly 120 timestamped points of wall migration — the whole
intraday path in **one** request. The end-of-day job captures that for the index
names, which is strictly better than seven hourly polls: more granular, cheaper, and
no commit churn.

Hourly polling only earns its place as a backstop, because TerraShade's history
resets if their server restarts (free Render tier, documented in their own guide).
If you want that insurance, uncomment the second cron in the workflow. It sweeps the
8-ticker index subset and appends to one file per day, so it costs about 40 seconds
and one commit per run.

Do **not** run the full 60-ticker list hourly. Non-index chains refresh far more
slowly than TerraShade's guide claims — observed lags on 2026-10-15 ran from 25
minutes to over 5 hours — so most hourly rows would be byte-identical re-records of
a chain that has not moved.

## Known limitations

- Open interest only. Same-session flow is not reflected, which matters most on 0DTE.
- Chain completeness is unstable per ticker. A name can serve a full chain one hour
  and a two-expiry chain the next, with no indication in the UI.
- The unavailable set moves between runs. Treat coverage as a per-run fact.
- The endpoints are undocumented and can change without notice. If a run returns
  mostly `transport:` or `http_` errors, check the API shape before trusting output.
