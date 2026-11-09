# TradeEcho single-stock term structure

Builds the "TradeEcho Single Stocks Term Structure" page (NVDA, TSLA, AAPL, AMZN, GOOGL, AVGO) from TradeEcho Dealer Edge data.

## Layout

```
capture/capture.js   browser snippet: pulls Dealer Edge data for the 6 tickers (runs in your signed-in TradeEcho tab)
data/raw/DATE.json   one compact snapshot per run (input)
data/built-DATE.json derived levels and text for that run (audit trail)
template.html        page layout and rendering
build.py             snapshot -> index.html
index.html           the finished page (served by GitHub Pages at /term-structure/)
capture/save_from_transcript.py  Claude-run helper: saves the snippet's returned JSON to data/raw/
```

## Daily run (after the 4 pm ET close; TradeEcho refreshes about 4:05 pm ET)

1. **Capture**: open https://app.tradeecho.com while signed in, open DevTools Console, paste `capture/capture.js`, press Enter.
   A file `te_capture_YYYY-MM-DD.json` downloads. Move it to `data/raw/YYYY-MM-DD.json`.
   (Claude can do this step in its browser: it runs the same snippet and saves the result.)
2. **Build**: `python3 build.py` (uses the newest file in `data/raw/`), or `python3 build.py data/raw/2026-10-09.json`.
3. **Publish**: commit `data/` and `index.html` and push to `main` (GitHub Pages serves it), and republish the artifact.

A daily Claude scheduled task does all three on weekdays at 4:20 pm ET.

Change tickers by setting `window.TE_TICKERS = ['NVDA', ...]` before pasting the snippet.

## What the build works out

- Columns: the next expiries up to and including the next monthly opex (third Friday); the strip adds the first Friday weekly after it.
- Per expiry: net positioning in K contracts (TradeEcho units ÷ 1000) and VEX in $M.
- Matrix: the 9 largest strikes per expiry within ±15% of spot, labelled resist / support / anchor / trigger.
- Levels (from the opex expiry): pin = TradeEcho anchor; cap = largest positive strike above spot; support = largest positive strike below spot ("thin" if under 10% of the biggest strike); flip = TradeEcho flip point.
- Regime pill: "on the flip" within 0.4% of it, "below flip" if spot is under it, otherwise "pinning". TradeEcho rating 3 or lower downgrades "pinning" to amber.
- Key levels: positioning summed per strike across the matrix expiries (opex weighted 1.5). Resistance comes in two tiers: first (nearest level at least 25% of the biggest) and major cap (the biggest). Negative levels above spot are air pockets; negative levels below are "no support". A support is only called a buy zone when the board is positive, price is above the flip zone, and the measured hold rate is at least 50% and 5 points better than a plain strike; otherwise it is "weak support".
- Odds are measured, not modelled: `calibrate()` replays every saved snapshot up to the build date and counts how often a later close went through a strike within 5 sessions, by side, distance (in the stock's typical daily move) and size of positioning. Small samples are pulled toward the rate for all strikes at that distance. Each level shows its rate next to the plain-strike rate.
- Flip: the middle of the last 3 sessions' TradeEcho flip, shown as a zone (low to high of those sessions) and flagged when it moved more than 3% of price in a day.
- Lean: net positioning into opex leads (negative = bigger swings), the flip zone refines it. The pin is shown for reference only.
- The read paragraph is generated from these numbers. No hand-written text, so every run is reproducible.

## Notes

- The snippet uses the TradeEcho session already in the browser tab. No password or token is stored in these files.
- Positions are TradeEcho's prior-session open interest; spot is the price at capture time.
- Informational only, not investment advice.
