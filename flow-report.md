# Options Flow Report (v1.3) — 2026-11-17

**Run stats:** 52/52 tickers fetched · 0 failed · 55,604 contracts

## Market Regime

**risk-off · backwardation (VIX/VIX3M=1.02, DoD +0.02, flipped from contango) · negative gamma (moves amplified) · high vol · choppy/rangebound — momentum tilted**

`Vol: HIGH · Trend: CHOP · Risk: RISK_OFF · Gamma: NEGATIVE · SPY GEX: $-15,320M`

_Pipeline knobs: mom×0.85 · conviction≥0.88_

## Master Scoreboard (all tickers by composite)

| Rank   | Ticker   | Composite   | Trend%   | Mom%   | Flow%   | Rot%   | Conviction   | ΔRank   |
|:-------|:---------|:------------|:---------|:-------|:--------|:-------|:-------------|:--------|
| 1      | XLV      | 100.0       | 100      | 98     | N/A     | 94     | CONFIRMED    | 0       |
| 2      | XLP      | 98.4        | 98       | 94     | N/A     | 90     | CONFIRMED    | 0       |
| 3      | XLE      | 95.1        | 95       | 87     | N/A     | 89     | NEUTRAL      | 0       |
| 4      | XLB      | 90.2        | 90       | 78     | N/A     | 81     | NEUTRAL      | +1      |
| 5      | XLRE     | 88.5        | 89       | 75     | N/A     | 80     | NEUTRAL      | -1      |
| 6      | BIL      | 86.9        | 87       | 69     | N/A     | 84     | NEUTRAL      | +1      |
| 7      | XLK      | 83.6        | 84       | 79     | N/A     | 67     | NEUTRAL      | -1      |
| 8      | XLY      | 77.0        | 77       | 66     | N/A     | 76     | NEUTRAL      | 0       |
| 9      | TSM      | 73.9        | 74       | 77     | 74      | 60     | NEUTRAL      | +26     |
| 10     | MRVL     | 71.5        | 85       | 77     | 60      | 74     | NEUTRAL      | +13     |
| 11     | UNH      | 70.3        | 93       | 83     | 51      | 90     | NEUTRAL      | -1      |
| 12     | AMZN     | 68.8        | 79       | 61     | 60      | 82     | NEUTRAL      | -1      |
| 13     | AI       | 65.3        | 57       | 56     | 72      | 54     | NEUTRAL      | -4      |
| 14     | CPER     | 63.9        | 64       | 69     | N/A     | 60     | NEUTRAL      | +3      |
| 15     | IWM      | 62.3        | 62       | 63     | N/A     | 62     | NEUTRAL      | 0       |
| 16     | HYG      | 60.7        | 61       | 56     | N/A     | 70     | NEUTRAL      | +3      |
| 17     | HIVE     | 60.1        | 13       | 18     | 100     | 13     | CONFLICT     | +1      |
| 18     | TLT      | 59.3        | 54       | 48     | 64      | 58     | NEUTRAL      | -4      |
| 19     | RIOT     | 59.2        | 51       | 47     | 66      | 53     | NEUTRAL      | -7      |
| 20     | XLI      | 59.0        | 59       | 57     | N/A     | 56     | NEUTRAL      | +2      |
| 21     | SNDK     | 58.7        | 82       | 70     | 39      | 74     | NEUTRAL      | +6      |
| 22     | LQD      | 55.7        | 56       | 47     | N/A     | 63     | NEUTRAL      | +3      |
| 23     | CLSK     | 55.4        | 18       | 26     | 87      | 16     | CONFLICT     | -3      |
| 24     | AAPL     | 55.2        | 97       | 80     | 20      | 100    | CONFLICT     | +4      |
| 25     | SLV      | 54.9        | 30       | 39     | 77      | 30     | CONFLICT     | +1      |
| 26     | TSLA     | 54.5        | 69       | 53     | 42      | 78     | NEUTRAL      | -13     |
| 27     | MARA     | 53.8        | 25       | 24     | 79      | 25     | CONFLICT     | +30     |
| 28     | EOSE     | 53.3        | 3        | 5      | 96      | 1      | CONFLICT     | +15     |
| 29     | WULF     | 52.2        | 41       | 46     | 62      | 37     | NEUTRAL      | +27     |
| 30     | XLF      | 51.6        | 92       | 86     | 17      | 86     | CONFLICT     | +10     |
| 31     | GOOGL    | 51.0        | 44       | 47     | 57      | 43     | NEUTRAL      | -10     |
| 32     | QQQ      | 50.6        | 67       | 69     | 36      | 61     | NEUTRAL      | -2      |
| 33     | OPEN     | 50.2        | 2        | 1      | 91      | 1      | CONFLICT     | +4      |
| 34     | ARM      | 50.0        | 75       | 73     | 28      | 65     | CONFLICT     | +12     |
| 35     | SPY      | 49.6        | 80       | 64     | 23      | 81     | CONFLICT     | +1      |
| 36     | CRWV     | 48.9        | 26       | 33     | 68      | 17     | CONFLICT     | +12     |
| 37     | CIFR     | 48.4        | 11       | 21     | 80      | 7      | CONFLICT     | +13     |
| 38     | QCOM     | 48.4        | 72       | 54     | 28      | 81     | CONFLICT     | -6      |
| 39     | XLC      | 47.5        | 48       | 45     | N/A     | 54     | NEUTRAL      | -5      |
| 40     | SMH      | 47.2        | 66       | 74     | 32      | 55     | CONFLICT     | +12     |
| 41     | NVDA     | 46.9        | 38       | 47     | 55      | 33     | NEUTRAL      | +1      |
| 42     | GLD      | 46.4        | 36       | 38     | 55      | 41     | NEUTRAL      | -4      |
| 43     | OKLO     | 46.3        | 8        | 11     | 79      | 9      | CONFLICT     | +12     |
| 44     | NFLX     | 45.4        | 21       | 16     | 66      | 29     | NEUTRAL      | +1      |
| 45     | IREN     | 45.1        | 7        | 15     | 78      | 4      | CONFLICT     | +13     |
| 46     | AVGO     | 43.8        | 49       | 45     | 39      | 54     | NEUTRAL      | +3      |
| 47     | GOOG     | 43.1        | 43       | 47     | 44      | 41     | NEUTRAL      | +4      |
| 48     | XLU      | 40.5        | 70       | 61     | 15      | 72     | CONFLICT     | -1      |
| 49     | HIMS     | 40.0        | 28       | 34     | 50      | 25     | NEUTRAL      | -8      |
| 50     | INTC     | 39.9        | 52       | 63     | 29      | 40     | NEUTRAL      | -34     |
| 51     | IONQ     | 38.9        | 20       | 24     | 55      | 19     | NEUTRAL      | -22     |
| 52     | SMCI     | 38.6        | 31       | 43     | 45      | 28     | NEUTRAL      | -8      |
| 53     | SMR      | 36.8        | 5        | 10     | 64      | 5      | NEUTRAL      | -20     |
| 54     | IBIT     | 35.7        | 46       | 44     | 27      | 49     | NEUTRAL      | -15     |
| 55     | MSTR     | 35.3        | 33       | 33     | 37      | 40     | NEUTRAL      | -24     |
| 56     | BABA     | 31.6        | 16       | 16     | 44      | 23     | NEUTRAL      | -2      |
| 57     | QBTS     | 29.8        | 10       | 19     | 47      | 9      | NEUTRAL      | -33     |
| 58     | RGTI     | 29.1        | 15       | 20     | 41      | 12     | NEUTRAL      | +3      |
| 59     | RKLB     | 25.5        | 34       | 39     | 18      | 35     | NEUTRAL      | -6      |
| 60     | ETHA     | 25.3        | 39       | 41     | 13      | 41     | NEUTRAL      | -1      |
| 61     | COIN     | 19.1        | 23       | 23     | 16      | 25     | NEUTRAL      | -1      |
| N/A    | AAPX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDU     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | TSLL     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^GSPC    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^SKEW    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX     | N/A         | N/A      | N/A    | 9       | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX3M   | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VVIX    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |

## Sector Rotation / Relative Strength (top 15)

| Ticker   |   RS Rating |   Rel Str 63d | RS New-High   | Dual-Mom   |
|:---------|------------:|--------------:|:--------------|:-----------|
| SNDK     |          99 |         -44.7 | No            | above cash |
| AAPL     |          97 |          15.7 | Yes           | above cash |
| XLV      |          96 |          10.4 | No            | above cash |
| MRVL     |          94 |         -32.8 | No            | above cash |
| UNH      |          92 |           5.4 | No            | above cash |
| XLE      |          91 |           4.8 | No            | above cash |
| XLP      |          89 |          10.9 | No            | above cash |
| XLF      |          88 |           4.2 | No            | above cash |
| AMZN     |          86 |           1.5 | No            | above cash |
| XLB      |          84 |           1.8 | No            | above cash |
| BIL      |          83 |           5.4 | No            | below cash |
| XLRE     |          81 |           2.2 | No            | above cash |
| SPY      |          79 |           0   | Yes           | above cash |
| QCOM     |          78 |           8   | No            | below cash |
| ARM      |          76 |         -21.9 | No            | above cash |

## Option Skew — Extremes (top/bottom 8)

_Board-wide: protection demand rising across the board (typical name z +1.6 vs its own norm; 22 of 30 names at z +1 or more, 0 at −1 or less). Hedging arrows are measured net of this move._

| Ticker   | Group    | Tilt        |   Skew25 (vol pts) | 90-110   |   ATM IV % |   Skew/IV | Hedging            |    z | Flow        | Positioning   |
|:---------|:---------|:------------|-------------------:|:---------|-----------:|----------:|:-------------------|-----:|:------------|:--------------|
| SPY      | top 8    | put-skewed  |                8.1 | 16.2     |       20.6 |      0.4  | steady →           | -0.9 | Neutral +14 |               |
| QQQ      | top 8    | put-skewed  |                9   | 14.7     |       30.3 |      0.3  | hedging easing ↓   | -1.1 | Neutral +5  |               |
| AAPL     | top 8    | put-skewed  |                6.9 | 11.8     |       25.5 |      0.27 | hedging building ↑ |  1.7 | Neutral -1  |               |
| MSTR     | top 8    | put-skewed  |               16.2 | 10.0     |       86.5 |      0.19 | hedging building ↑ |  1.1 | Neutral -6  |               |
| TSM      | top 8    | put-skewed  |                9.2 | 9.5      |       52.2 |      0.18 | steady →           |  0.4 | Neutral -16 |               |
| IBIT     | top 8    | put-skewed  |                7.3 | 8.6      |       45.7 |      0.16 | steady →           |  0.4 | Neutral -11 |               |
| AMZN     | top 8    | put-skewed  |                6   | 8.5      |       38.1 |      0.16 | steady →           | -0.2 | Neutral -7  |               |
| TSLA     | top 8    | put-skewed  |                8   | 8.4      |       51.4 |      0.16 | steady →           | -0.4 | Neutral +0  |               |
| TLT      | bottom 8 | call-skewed |               -0.1 | N/A      |       13   |     -0.01 | hedging easing ↓   | -1.5 | Neutral -18 |               |
| HIMS     | bottom 8 | put-skewed  |                1.8 | 2.1      |       76   |      0.02 | steady →           | -0.1 | Neutral +12 |               |
| GLD      | bottom 8 | put-skewed  |                0.8 | 2.3      |       24.4 |      0.03 | hedging easing ↓   | -2.4 | Neutral -5  |               |
| WULF     | bottom 8 | put-skewed  |                7.8 | 3.1      |      105.5 |      0.07 | steady →           | -0.8 | Neutral -10 |               |
| SLV      | bottom 8 | put-skewed  |                3.5 | 4.8      |       43.3 |      0.08 | steady →           | -0.8 | Bear -35    |               |
| NVDA     | bottom 8 | put-skewed  |                5.5 | 5.1      |       65.4 |      0.08 | hedging easing ↓   | -2.5 | Neutral -5  |               |
| NFLX     | bottom 8 | put-skewed  |                3   | 4.7      |       35.8 |      0.08 | steady →           |  0.3 | Neutral -3  |               |
| BABA     | bottom 8 | put-skewed  |                4.7 | 4.6      |       53.9 |      0.09 | hedging building ↑ |  2   | Neutral -5  |               |

_30 of 52 tickers had a fittable smile. Skew25 = how much more an out-of-the-money put costs than the matching out-of-the-money call, in vol points, at a constant 30-day tenor, re-derived from bid/ask mids (Yahoo's own IV field is not used). Positive = puts richer, the normal state — so read the *ranking*, not the level. Tilt is by sign: call-skewed = Skew/IV below 0; least put-skewed = 0 to 0.02; put-skewed above. Hedging = tonight's Skew/IV against the name's own previous 20 sessions (z = standard deviations from that average), net of the typical name's move tonight (the Board-wide line above): building when z is at least +1, easing at −1 or below, else steady; n/a until 10 prior sessions exist. It describes protection demand, not a price forecast._

## Mega-Cap Tech Skew

| Ticker   |   Skew25 (vol pts) |   90-110 |   ATM IV % |   Skew/IV | Rank     | Read           | Hedging            |    z | Flow        | Positioning   |
|:---------|-------------------:|---------:|-----------:|----------:|:---------|:---------------|:-------------------|-----:|:------------|:--------------|
| NVDA     |                5.5 |      5.1 |       65.4 |      0.08 | 25 of 30 | put-skewed     | hedging easing ↓   | -2.5 | Neutral -5  |               |
| AAPL     |                6.9 |     11.8 |       25.5 |      0.27 | 3 of 30  | steep put skew | hedging building ↑ |  1.7 | Neutral -1  |               |
| AMZN     |                6   |      8.5 |       38.1 |      0.16 | 7 of 30  | steep put skew | steady →           | -0.2 | Neutral -7  |               |
| GOOGL    |                5.3 |      7   |       37.4 |      0.14 | 10 of 30 | put-skewed     | steady →           |  0.4 | Neutral -8  |               |
| TSLA     |                8   |      8.4 |       51.4 |      0.16 | 8 of 30  | steep put skew | steady →           | -0.4 | Neutral +0  |               |
| AVGO     |                9.8 |      8.8 |       64.8 |      0.15 | 9 of 30  | put-skewed     | steady →           |  0.2 | Neutral -12 |               |

_Mega-cap tech: 6 of 6 fitted · median Skew/IV 0.15 vs 0.12 for the other names · richer downside protection than the rest of the board · steepest: AAPL, AMZN, TSLA · flattest: NVDA._

_Flow = premium-weighted flow score: 100 × (bought calls + sold puts − sold calls − bought puts) ÷ total out-of-the-money premium, sides estimated from the last trade against bid/ask (a last trade outside the closing quote is left unsigned); Bull at +20 or more, Bear at −20 or less. Positioning: defensive = hedging building with Bear flow; speculative = hedging easing with Bull flow; blank otherwise. Positioning describes what is being hedged and flowed tonight. It is not a price forecast._

## Stretch & Reversal Watch (experimental)

| Watch             | Tonight                                                                          | Backtest (before live)                                       | Live since 2026-11-06                      |
|:------------------|:---------------------------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------|
| hedging unwinding | NVDA (z -2.5), GLD (z -2.4), TLT (z -1.5)                                        | 194 flags · +1.6% vs avg name · 59% beat it                  | 4 flags · -3.3% vs avg name · 25% beat it  |
| stretched up      | none                                                                             | 597 flags · -1.5% vs avg name · 41% beat it                  | 21 flags · -4.1% vs avg name · 48% beat it |
| washed out        | MSTR (-20%), BABA (-15%), COIN (-13%), TSM (-9%)                                 | 118 flags · -0.1% vs avg name · 57% beat it (no edge so far) | 14 flags · +3.0% vs avg name · 71% beat it |
| puts closing      | COIN (97% puts), ARM (94% puts), QQQ (91% puts), MARA (90% puts), SPY (89% puts) | 797 flags · +0.7% vs avg name · 55% beat it (to 2026-11-16)  | none resolved yet (counts from 2026-11-16) |

_Experimental, not proven. Hedging unwinding = tonight's Skew/IV at z -1.5 or lower against the name's own norm, net of the board (as the Hedging column): protection being sold off. Stretched up = price up 5% or more over the last 5 sessions. Washed out = down 5% or more with hedging at z +2 or more on its own norm. Puts closing = the fifth of names where puts made up most of the out-of-the-money positions closed in the previous session (volume matched against the drop in open interest): protection taken off. The record columns score each past flag 5 sessions later against the average name that night (prices from the option chains' implied forwards). The backtest is in-sample: the thresholds were picked on that same history, so it flatters the flags; the live column counts only flags raised since this block was added and is the one that matters. If the live record does not hold up, the block goes. Not a price forecast._

---

# Flow Detail

## T4 — OTM Flow Summary (ranked by OTM Call/Put premium ratio)

|   Rank | Ticker   |   Premium Ratio |   Premium Ratio All |   Total Call Premium |   Total Put Premium |   Net Signed Premium |   Close Price | 1-Day Return   | 1-Week Return   | % Close to MA20   | % Close to MA50   | % Close to High   | % Close to Low   |   52 Week High |   52 Week Low |    MA20 |    MA50 |
|-------:|:---------|----------------:|--------------------:|---------------------:|--------------------:|---------------------:|--------------:|:---------------|:----------------|:------------------|:------------------|:------------------|:-----------------|---------------:|--------------:|--------:|--------:|
|      1 | CIFR     |           11.69 |                1.72 |            1,355,176 |             115,896 |             -687,274 |          6.42 | -1.83%         | -1.91%          | -12.55%           | -46.08%           | -78.70%           | 26.60%           |          30.14 |          5.07 |    7.34 |   11.91 |
|      2 | MARA     |            4.41 |                0.95 |            1,427,581 |             323,564 |              699,819 |          6.42 | -3.31%         | 1.10%           | -7.53%            | -31.12%           | -60.93%           | 12.83%           |          16.43 |          5.69 |    6.94 |    9.32 |
|      3 | SLV      |            2.72 |                0.23 |            5,054,601 |           1,857,396 |           -2,397,237 |         42.64 | 0.59%          | -9.02%          | -8.89%            | -18.30%           | -61.18%           | 1.50%            |         109.83 |         42.01 |   46.8  |   52.19 |
|      4 | RIOT     |            2.69 |                2.48 |            1,557,256 |             578,413 |              -54,647 |         17.05 | -0.06%         | 2.03%           | 12.63%            | -4.47%            | -43.77%           | 48.26%           |          30.32 |         11.5  |   15.14 |   17.85 |
|      5 | IREN     |            2.46 |                1.29 |            7,858,203 |           3,189,582 |            2,104,851 |         15.81 | -3.57%         | -26.96%         | -29.73%           | -51.90%           | -77.65%           | 4.19%            |          70.71 |         15.17 |   22.49 |   32.86 |
|      6 | CRWV     |            2.33 |                1.73 |           29,984,804 |          12,843,053 |           -3,277,438 |         49.89 | 0.02%          | 7.52%           | -7.29%            | -29.54%           | -63.91%           | 22.94%           |         138.25 |         40.58 |   53.82 |   70.81 |
|      7 | NFLX     |            1.9  |                0.26 |            5,760,380 |           3,029,689 |             -275,475 |         59.68 | -1.76%         | -5.88%          | -5.91%            | -12.87%           | -48.22%           | 0.45%            |         115.25 |         59.41 |   63.43 |   68.49 |
|      8 | TLT      |            1.86 |                0.77 |            5,419,613 |           2,907,933 |           -1,499,655 |         79.55 | 0.21%          | -2.89%          | -1.86%            | -0.69%            | -12.45%           | 4.08%            |          90.86 |         76.43 |   81.06 |   80.1  |
|      9 | TSM      |            1.85 |                0.16 |           47,646,757 |          25,777,856 |          -12,084,499 |        359.69 | -3.68%         | -4.20%          | -10.80%           | -15.85%           | -26.21%           | 34.81%           |         487.47 |        266.82 |  403.25 |  427.41 |
|     10 | MRVL     |            1.77 |                0.27 |           18,763,245 |          10,608,952 |           -1,333,643 |        148.74 | 2.33%          | 5.34%           | -19.85%           | -34.22%           | -54.91%           | 110.41%          |         329.88 |         70.69 |  185.58 |  226.11 |
|     10 | WULF     |            1.77 |                1.28 |            3,281,428 |           1,856,211 |             -507,515 |         11.67 | -1.77%         | 2.64%           | -3.58%            | -15.13%           | -60.89%           | 22.71%           |          29.84 |          9.51 |   12.1  |   13.75 |
|     12 | AMZN     |            1.63 |                1.47 |           33,411,073 |          20,456,902 |           -3,862,060 |        257.89 | 0.05%          | -0.54%          | 0.40%             | 1.21%             | -10.21%           | 31.58%           |         287.2  |        196    |  256.86 |  254.81 |
|     13 | HIMS     |            1.62 |                0.85 |            1,159,289 |             714,059 |              229,657 |         17.55 | -5.44%         | -32.50%         | -29.00%           | -35.51%           | -57.18%           | 27.73%           |          40.99 |         13.74 |   24.72 |   27.21 |
|     14 | UNH      |            1.56 |                0.82 |            7,904,348 |           5,052,347 |             -278,368 |        389.68 | -5.42%         | -1.13%          | -4.14%            | -0.47%            | -15.58%           | 52.24%           |         461.62 |        255.97 |  406.51 |  391.5  |
|     15 | GLD      |            1.49 |                0.04 |           14,079,010 |           9,449,007 |           -1,134,960 |        352.48 | -0.13%         | -5.38%          | -3.74%            | -6.97%            | -30.85%           | 0.15%            |         509.7  |        351.96 |  366.19 |  378.88 |
|     16 | GOOGL    |            1.42 |                0.37 |           24,228,078 |          17,111,748 |           -3,122,633 |        280.2  | -1.24%         | -1.61%          | -5.78%            | -14.03%           | -31.43%           | 2.97%            |         408.61 |        272.11 |  297.39 |  325.93 |
|     17 | NVDA     |            1.31 |                1.21 |          289,436,997 |         221,352,620 |          -25,343,797 |        155.46 | -0.44%         | -16.71%         | -19.28%           | -26.59%           | -36.12%           | 4.48%            |         243.37 |        148.8  |  192.59 |  211.76 |
|     18 | GOOG     |            1.19 |                0.2  |           13,165,276 |          11,089,857 |           -1,503,785 |        277.6  | -1.30%         | -2.23%          | -5.90%            | -14.02%           | -31.37%           | 2.23%            |         404.47 |        271.54 |  295    |  322.87 |
|     19 | BABA     |            1.18 |                0.28 |            6,414,761 |           5,442,741 |             -559,690 |         86.65 | -4.38%         | -20.83%         | -13.57%           | -18.18%           | -52.15%           | 0.18%            |         181.1  |         86.49 |  100.26 |  105.9  |
|     20 | SMCI     |            1.16 |                1.53 |            4,966,687 |           4,295,732 |              -84,590 |         24.14 | -3.56%         | -16.06%         | -20.89%           | -32.80%           | -53.04%           | 23.92%           |          51.4  |         19.48 |   30.52 |   35.92 |
|     21 | SNDK     |            1.09 |                0.11 |          106,525,815 |          97,737,338 |           17,633,274 |        797.24 | -1.47%         | -4.53%          | -25.34%           | -43.22%           | -66.14%           | 335.65%          |        2354.39 |        183    | 1067.84 | 1404    |
|     22 | QCOM     |            1.07 |                1.35 |            2,946,417 |           2,766,433 |           -1,593,651 |        166.67 | -1.10%         | 0.76%           | -3.43%            | -6.67%            | -35.88%           | 36.63%           |         259.92 |        121.99 |  172.59 |  178.58 |
|     23 | AVGO     |            1    |                0.7  |           36,608,633 |          36,507,044 |           -9,076,729 |        341.6  | 2.46%          | 16.31%          | 3.12%             | -0.80%            | -30.99%           | 17.89%           |         495    |        289.77 |  331.26 |  344.35 |
|     24 | TSLA     |            0.97 |                1.09 |           57,271,923 |          59,201,537 |             -156,512 |        380.11 | 0.10%          | 6.11%           | -1.59%            | 1.23%             | -23.80%           | 27.82%           |         498.83 |        297.38 |  386.26 |  375.49 |
|     25 | MSTR     |            0.96 |                0.17 |           17,580,902 |          18,269,457 |           -2,251,007 |         96.5  | -6.34%         | -25.15%         | -25.93%           | -31.88%           | -54.87%           | 17.96%           |         213.83 |         81.81 |  130.28 |  141.67 |
|     26 | ARM      |            0.91 |                0.17 |            5,187,507 |           5,719,635 |           -1,908,955 |        183.39 | 4.76%          | 5.02%           | -8.76%            | -25.16%           | -59.49%           | 83.35%           |         452.7  |        100.02 |  201    |  245.04 |
|     27 | INTC     |            0.81 |                0.29 |           17,703,729 |          21,762,697 |           -2,821,793 |         55.17 | -0.54%         | -1.97%          | -21.29%           | -40.79%           | -61.24%           | 67.74%           |         142.35 |         32.89 |   70.09 |   93.18 |
|     27 | QQQ      |            0.81 |                0.37 |          437,797,132 |         541,348,498 |           44,187,164 |        656.95 | -0.73%         | 0.13%           | -4.73%            | -8.18%            | -13.88%           | 18.24%           |         762.86 |        555.6  |  689.58 |  715.49 |
|     29 | SMH      |            0.78 |                1.36 |           49,124,006 |          62,706,066 |          -18,818,283 |        460.1  | -0.39%         | -0.83%          | -9.70%            | -17.16%           | -31.52%           | 46.04%           |         671.83 |        315.05 |  509.5  |  555.43 |
|     29 | RKLB     |            0.78 |                0.72 |            3,185,710 |           4,110,523 |             -500,236 |         55.05 | -4.04%         | 3.73%           | -2.20%            | -11.37%           | -63.54%           | 46.53%           |         151    |         37.57 |   56.29 |   62.11 |
|     31 | IBIT     |            0.58 |                0.63 |            7,820,904 |          13,499,897 |           -2,331,028 |         36.14 | -1.77%         | -15.72%         | -16.26%           | -19.93%           | -35.00%           | 10.05%           |          55.6  |         32.84 |   43.16 |   45.14 |
|     31 | XLU      |            0.58 |                3.39 |              602,894 |           1,038,614 |              172,500 |         43.42 | -1.59%         | 0.67%           | 0.31%             | 3.60%             | -9.16%            | 11.25%           |          47.8  |         39.03 |   43.29 |   41.91 |
|     33 | COIN     |            0.56 |                0.1  |            4,933,711 |           8,739,614 |              341,569 |        115.02 | -4.02%         | -14.65%         | -20.73%           | -31.46%           | -59.61%           | 0.80%            |         284.74 |        114.11 |  145.09 |  167.81 |
|     34 | ^VIX     |            0.46 |                2.33 |           32,004,775 |          14,820,426 |           11,270,415 |         25.46 | 11.13%         | -0.70%          | 27.22%            | 44.17%            | -27.88%           | 90.28%           |          35.3  |         13.38 |   20.01 |   17.66 |
|     35 | AAPL     |            0.45 |                1.32 |           20,799,622 |          46,197,124 |             -965,353 |        351.91 | -0.25%         | 2.79%           | 1.34%             | 3.38%             | -2.47%            | 44.57%           |         360.83 |        243.42 |  347.26 |  340.41 |
|     36 | SPY      |            0.33 |                0.39 |          265,068,150 |         809,166,884 |          145,610,067 |        732.44 | -1.01%         | -0.39%          | -3.10%            | -4.02%            | -6.29%            | 16.39%           |         781.62 |        629.28 |  755.86 |  763.15 |
|     37 | ETHA     |            0.2  |                0.16 |              386,250 |           1,905,146 |             -135,566 |         40.65 | -1.17%         | -19.23%         | -18.53%           | -25.78%           | -48.06%           | 17.57%           |          78.27 |         34.58 |   49.89 |   54.77 |
|     38 | XLF      |            0.09 |                0.16 |            1,566,976 |          18,386,637 |            2,798,151 |         57.07 | -1.91%         | -0.16%          | -0.38%            | 1.98%             | -4.95%            | 19.72%           |          60.04 |         47.67 |   57.29 |   55.96 |

## T2 — Premium Ratio Leaderboard (all strikes, call subtotal ≥ $1,000,000)

|   Rank | Ticker   |   Premium Ratio |   Call Volume |   Call Premium |   Put Volume |   Put Premium |
|-------:|:---------|----------------:|--------------:|---------------:|-------------:|--------------:|
|      1 | XLU      |            3.39 |        13,205 |      2,292,880 |       17,581 |       677,094 |
|      2 | ^VIX     |            2.33 |       237,189 |     56,971,698 |      248,064 |    24,449,343 |
|      3 | CRWV     |            1.73 |        40,181 |     12,401,377 |       16,875 |     7,158,753 |
|      4 | SMCI     |            1.53 |        50,062 |      3,379,001 |       10,588 |     2,203,280 |
|      5 | AMZN     |            1.47 |        29,281 |     12,865,478 |       21,326 |     8,722,954 |
|      6 | SMH      |            1.36 |        10,127 |     25,634,030 |        9,433 |    18,846,370 |
|      7 | QCOM     |            1.35 |         1,713 |      1,002,289 |        1,470 |       742,741 |
|      8 | AAPL     |            1.32 |        88,660 |     37,131,800 |      109,014 |    28,195,484 |
|      9 | IREN     |            1.29 |        12,684 |      3,290,690 |        4,164 |     2,551,623 |
|     10 | WULF     |            1.28 |        25,652 |      1,926,641 |       17,182 |     1,503,373 |
|     11 | NVDA     |            1.21 |       187,767 |    110,898,030 |      190,165 |    91,691,724 |
|     12 | TSLA     |            1.09 |        86,213 |     40,815,081 |       76,225 |    37,514,713 |
|     13 | UNH      |            0.82 |         6,343 |      3,356,857 |        2,212 |     4,105,110 |
|     14 | TLT      |            0.77 |        33,307 |      3,250,909 |       17,455 |     4,234,657 |
|     15 | RKLB     |            0.72 |         7,634 |      1,014,656 |        3,566 |     1,412,851 |
|     16 | AVGO     |            0.7  |        13,222 |     15,256,832 |        4,551 |    21,882,012 |
|     17 | IBIT     |            0.63 |        57,819 |      4,228,483 |       49,936 |     6,681,949 |
|     18 | SPY      |            0.39 |       145,647 |    102,582,534 |      250,579 |   262,852,457 |
|     19 | GOOGL    |            0.37 |         9,216 |     10,528,299 |        3,825 |    28,557,410 |
|     19 | QQQ      |            0.37 |        66,725 |     91,898,000 |       63,573 |   250,685,927 |
|     21 | INTC     |            0.29 |        33,527 |      9,259,340 |        7,500 |    32,438,789 |
|     22 | BABA     |            0.28 |        10,877 |      2,849,058 |        9,501 |    10,323,547 |
|     23 | MRVL     |            0.27 |        10,867 |      7,864,190 |        8,369 |    29,199,575 |
|     24 | NFLX     |            0.26 |        17,312 |      1,444,481 |       16,694 |     5,612,853 |
|     25 | SLV      |            0.23 |        17,776 |      1,838,918 |       16,562 |     7,966,247 |
|     26 | GOOG     |            0.2  |         3,200 |      2,907,460 |        2,093 |    14,233,640 |
|     27 | ARM      |            0.17 |         3,814 |      3,582,290 |       11,046 |    21,021,830 |
|     27 | MSTR     |            0.17 |        14,645 |      5,829,615 |        6,728 |    33,746,630 |
|     29 | TSM      |            0.16 |        10,337 |     19,181,252 |       18,289 |   118,118,255 |
|     29 | XLF      |            0.16 |        13,748 |      1,710,273 |      207,105 |    10,882,517 |
|     31 | SNDK     |            0.11 |         9,065 |     41,015,403 |        5,311 |   357,301,988 |
|     32 | COIN     |            0.1  |         4,822 |      1,404,141 |        8,823 |    13,600,290 |
|     33 | GLD      |            0.04 |        12,364 |      3,848,526 |       14,976 |   100,930,530 |

## T1 — Top 4 Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261120C00270000  |         2,329 |     18,909,151 | AAPL261118P00350000  |       61,182 |    10,095,030 |
| AAPL     | AAPL270115C00250000  |           624 |      6,480,240 | AAPL261118P00352500  |       24,239 |     6,689,964 |
| AAPL     | AAPL261118C00355000  |        59,828 |      6,281,940 | AAPL261120P00350000  |       17,289 |     5,705,370 |
| AAPL     | AAPL261118C00352500  |        25,879 |      5,460,469 | AAPL261218P00350000  |        6,304 |     5,705,120 |
| AI       | AI261120C00012000    |        40,618 |         81,236 | AI261120P00013000    |        1,062 |       318,600 |
| AMZN     | AMZN270115C00240000  |         1,450 |      3,893,250 | AMZN261118P00287500  |          858 |     2,661,516 |
| AMZN     | AMZN261118C00260000  |        15,805 |      3,287,440 | AMZN261118P00255000  |       11,330 |     2,198,020 |
| AMZN     | AMZN261120C00260000  |         7,375 |      2,950,000 | AMZN261118P00257500  |        6,875 |     2,028,125 |
| AMZN     | AMZN261127C00260000  |         4,651 |      2,734,788 | AMZN261218P00250000  |        2,263 |     1,835,293 |
| ARM      | ARM261120C00182500   |         1,293 |      1,131,375 | ARM261218P00220000   |        1,893 |     8,187,225 |
| ARM      | ARM261120C00185000   |         1,321 |        990,750 | ARM261120P00185000   |        6,107 |     5,710,045 |
| ARM      | ARM261120C00180000   |           941 |        955,115 | ARM261218P00185000   |        2,920 |     5,504,200 |
| ARM      | ARM261218C00180000   |           259 |        505,050 | ARM270115P00310000   |          126 |     1,620,360 |
| AVGO     | AVGO261118C00340000  |         6,259 |      4,932,092 | AVGO261120P00460000  |          642 |     7,861,290 |
| AVGO     | AVGO261120C00330000  |         2,123 |      3,778,940 | AVGO261120P00420000  |          813 |     6,791,802 |
| AVGO     | AVGO261120C00345000  |         3,731 |      3,507,140 | AVGO261120P00410000  |          511 |     3,855,495 |
| AVGO     | AVGO270115C00350000  |         1,109 |      3,038,660 | AVGO261120P00342500  |        2,585 |     3,373,425 |
| BABA     | BABA270115C00090000  |         1,433 |        796,748 | BABA270115P00120000  |        1,007 |     3,364,387 |
| BABA     | BABA270115C00100000  |         3,185 |        796,250 | BABA261120P00120000  |          919 |     3,046,485 |
| BABA     | BABA261218C00100000  |         4,690 |        628,460 | BABA270115P00080000  |        6,554 |     2,457,750 |
| BABA     | BABA261218C00090000  |         1,569 |        627,600 | BABA261120P00101000  |        1,021 |     1,454,925 |
| CIFR     | CIFR261218C00007000  |         7,612 |        548,064 | CIFR261120P00014000  |          503 |       383,286 |
| CIFR     | CIFR270115C00007000  |         2,612 |        276,872 | CIFR270115P00015000  |          111 |        95,904 |
| COIN     | COIN261218C00130000  |         1,096 |        499,776 | COIN270115P00340000  |          210 |     4,750,200 |
| COIN     | COIN261120C00120000  |         1,908 |        389,232 | COIN261218P00110000  |        6,479 |     4,729,670 |
| COIN     | COIN261218C00140000  |         1,077 |        261,711 | COIN270115P00250000  |          210 |     2,860,200 |
| COIN     | COIN270115C00150000  |           741 |        253,422 | COIN261120P00120000  |        1,924 |     1,260,220 |
| CRWV     | CRWV261218C00055000  |        17,086 |      7,569,098 | CRWV261120P00050000  |       10,692 |     3,367,980 |
| CRWV     | CRWV261120C00050000  |         6,036 |      1,871,160 | CRWV270115P00060000  |        1,241 |     1,768,425 |
| CRWV     | CRWV261120C00055000  |        12,126 |      1,515,750 | CRWV261218P00050000  |        1,674 |     1,071,360 |
| CRWV     | CRWV261218C00060000  |         4,933 |      1,445,369 | CRWV261120P00049500  |        3,268 |       950,988 |
| ETHA     | ETHA261218C00047000  |         1,120 |         95,200 | ETHA261127P00040000  |        5,402 |       702,260 |
| ETHA     | ETHA261218C00041000  |           303 |         81,810 | ETHA261218P00040000  |        1,544 |       378,280 |
| GLD      | GLD270115C00296000   |           177 |      1,050,141 | GLD270115P00425000   |        3,700 |    26,640,000 |
| GLD      | GLD261120C00360000   |         7,940 |        992,500 | GLD261218P00400000   |        5,550 |    26,307,000 |
| GLD      | GLD261231C00387000   |         4,103 |        964,205 | GLD270115P00420000   |        3,800 |    25,536,000 |
| GLD      | GLD270115C00297000   |           144 |        841,680 | GLD261218P00470000   |        1,926 |    22,447,530 |
| GOOG     | GOOG270115C00300000  |         1,148 |        849,520 | GOOG261120P00340000  |          859 |     5,463,240 |
| GOOG     | GOOG270115C00280000  |           482 |        748,546 | GOOG261120P00350000  |          630 |     4,627,350 |
| GOOG     | GOOG261218C00290000  |           964 |        655,520 | GOOG261218P00340000  |          414 |     2,546,100 |
| GOOG     | GOOG270115C00290000  |           606 |        653,874 | GOOG261120P00360000  |          190 |     1,596,950 |
| GOOGL    | GOOGL270115C00295000 |         3,147 |      3,084,060 | GOOGL261120P00350000 |        1,780 |    12,549,000 |
| GOOGL    | GOOGL270115C00300000 |         3,607 |      3,033,487 | GOOGL261120P00355000 |        1,060 |     7,876,860 |
| GOOGL    | GOOGL261218C00285000 |         2,358 |      2,358,000 | GOOGL261120P00365000 |          543 |     4,555,770 |
| GOOGL    | GOOGL261120C00085000 |           104 |      2,052,752 | GOOGL261120P00360000 |          442 |     3,575,780 |
| HIMS     | HIMS270115C00015000  |           721 |        261,002 | HIMS270115P00050000  |           95 |       307,610 |
| HIMS     | HIMS261218C00018000  |         1,728 |        247,104 | HIMS261218P00017000  |        2,388 |       291,336 |
| IBIT     | IBIT261127C00038000  |        35,726 |      1,500,492 | IBIT261218P00036000  |       15,554 |     2,830,828 |
| IBIT     | IBIT261218C00037000  |         8,740 |      1,372,180 | IBIT261127P00036000  |       12,797 |     1,382,076 |
| IBIT     | IBIT261127C00037000  |        10,908 |        839,916 | IBIT261120P00037000  |       10,630 |     1,296,860 |
| IBIT     | IBIT261218C00036000  |         2,445 |        515,895 | IBIT261218P00034000  |       10,955 |     1,172,185 |
| INTC     | INTC261218C00060000  |        13,060 |      3,918,000 | INTC261120P00100000  |        2,211 |    10,082,160 |
| INTC     | INTC261120C00055000  |        11,099 |      2,663,760 | INTC261120P00120000  |        1,504 |     9,994,080 |
| INTC     | INTC261120C00054000  |         4,788 |      1,436,400 | INTC261218P00080000  |        2,681 |     6,726,629 |
| INTC     | INTC261127C00056000  |         4,580 |      1,241,180 | INTC261120P00105000  |        1,104 |     5,635,920 |
| IREN     | IREN261204C00007000  |         1,276 |      1,133,088 | IREN261218P00025000  |          774 |       731,430 |
| IREN     | IREN261218C00010000  |         1,144 |        742,456 | IREN261218P00016000  |        2,705 |       646,495 |
| IREN     | IREN261120C00016000  |         7,613 |        723,235 | IREN261120P00033000  |          359 |       614,608 |
| IREN     | IREN261231C00016000  |         2,651 |        691,911 | IREN261211P00033000  |          326 |       559,090 |
| MARA     | MARA261218C00007000  |         6,733 |        356,849 | MARA261218P00007000  |        2,857 |       314,270 |
| MARA     | MARA261120C00006500  |         6,037 |        181,110 | MARA261120P00007000  |        3,573 |       250,110 |
| MRVL     | MRVL261120C00155000  |         5,205 |      2,342,250 | MRVL261218P00230000  |          975 |     8,458,125 |
| MRVL     | MRVL261218C00165000  |         2,351 |      2,209,940 | MRVL261120P00240000  |          804 |     7,557,600 |
| MRVL     | MRVL261218C00150000  |         1,266 |      1,962,300 | MRVL261218P00150000  |        3,870 |     6,791,850 |
| MRVL     | MRVL261120C00150000  |         2,045 |      1,349,700 | MRVL261218P00160000  |        2,720 |     6,392,000 |
| MSTR     | MSTR261120C00100000  |         8,607 |      2,177,571 | MSTR261120P00140000  |        3,540 |    15,402,540 |
| MSTR     | MSTR270115C00105000  |         1,646 |      1,570,284 | MSTR261120P00145000  |        1,490 |     7,144,550 |
| MSTR     | MSTR261120C00090000  |         1,240 |      1,041,600 | MSTR261127P00150000  |        1,071 |     5,702,004 |
| MSTR     | MSTR261120C00098000  |         3,152 |      1,040,160 | MSTR261218P00185000  |          627 |     5,497,536 |
| NFLX     | NFLX261218C00060000  |         1,619 |        391,798 | NFLX270115P00080000  |        1,068 |     2,180,856 |
| NFLX     | NFLX261120C00060000  |         5,017 |        391,326 | NFLX270115P00060000  |        4,136 |     1,472,416 |
| NFLX     | NFLX261218C00063000  |         2,761 |        336,842 | NFLX261218P00060000  |        4,669 |     1,209,271 |
| NFLX     | NFLX261120C00061000  |         7,915 |        324,515 | NFLX261120P00060000  |        6,821 |       750,310 |
| NVDA     | NVDA261118C00155000  |        51,866 |     34,490,890 | NVDA261118P00155000  |       41,450 |    24,870,000 |
| NVDA     | NVDA261118C00160000  |        60,168 |     26,774,760 | NVDA261118P00150000  |       63,677 |    24,834,030 |
| NVDA     | NVDA261120C00155000  |        34,390 |     26,480,300 | NVDA261118P00152500  |       45,582 |    22,654,254 |
| NVDA     | NVDA261120C00160000  |        41,343 |     23,152,080 | NVDA261120P00150000  |       39,456 |    19,333,440 |
| QCOM     | QCOM261218C00185000  |         1,064 |        425,600 | QCOM261120P00165000  |          564 |       267,900 |
| QCOM     | QCOM270115C00160000  |           182 |        313,768 | QCOM261127P00170000  |          263 |       253,006 |
| QCOM     | QCOM270115C00190000  |           467 |        262,921 | QCOM270115P00130000  |          643 |       221,835 |
| QQQ      | QQQ261218C00660000   |        11,630 |     26,446,620 | QQQ261120P00720000   |       12,079 |    79,745,558 |
| QQQ      | QQQ261218C00650000   |         7,929 |     23,057,532 | QQQ261120P00725000   |       10,413 |    71,860,113 |
| QQQ      | QQQ261118C00655000   |        30,359 |     22,981,763 | QQQ261120P00680000   |       20,845 |    52,112,500 |
| QQQ      | QQQ270115C00700000   |        16,807 |     19,412,085 | QQQ261218P00660000   |       20,236 |    46,967,756 |
| RGTI     | RGTI261127C00008500  |           716 |         37,948 | RGTI261218P00009000  |        3,901 |       483,724 |
| RGTI     | RGTI261120C00001000  |            44 |         32,956 | RGTI261218P00010000  |        1,887 |       369,852 |
| RIOT     | RIOT261127C00018000  |         4,808 |        394,256 | RIOT261218P00023000  |          250 |       158,250 |
| RIOT     | RIOT261218C00020000  |         3,031 |        284,914 | RIOT261120P00016500  |        1,900 |       114,000 |
| RIOT     | RIOT261120C00017500  |         3,790 |        250,140 | RIOT261127P00018000  |          592 |       102,416 |
| RKLB     | RKLB261120C00060000  |         6,753 |        452,451 | RKLB261218P00055000  |        1,357 |       739,565 |
| RKLB     | RKLB270115C00030000  |           117 |        302,445 | RKLB261120P00055000  |        1,951 |       460,436 |
| RKLB     | RKLB261218C00060000  |           764 |        259,760 | RKLB261218P00060000  |          258 |       212,850 |
| SLV      | SLV261218C00043000   |         3,971 |        802,142 | SLV261120P00072000   |        1,001 |     2,922,920 |
| SLV      | SLV270115C00045000   |         2,308 |        454,676 | SLV261218P00043000   |       11,708 |     2,622,592 |
| SLV      | SLV261218C00048000   |         5,963 |        322,002 | SLV261218P00046000   |        3,129 |     1,298,535 |
| SLV      | SLV261120C00043500   |         5,534 |        260,098 | SLV261120P00058000   |          724 |     1,122,200 |
| SMCI     | SMCI261127C00024000  |         9,415 |      1,647,625 | SMCI261120P00025000  |        3,974 |       675,580 |
| SMCI     | SMCI261120C00027500  |        30,463 |        731,112 | SMCI261218P00024000  |        2,310 |       595,980 |
| SMCI     | SMCI261120C00025000  |         6,955 |        577,265 | SMCI270115P00030000  |          716 |       519,100 |
| SMCI     | SMCI261120C00024000  |         3,229 |        422,999 | SMCI261120P00024000  |        3,588 |       412,620 |
| SMH      | SMH261218C00100000   |           400 |     14,219,200 | SMH261218P00400000   |        5,884 |     5,772,204 |
| SMH      | SMH261218C00500000   |         3,542 |      4,749,822 | SMH270115P00450000   |        1,869 |     5,704,188 |
| SMH      | SMH261218C00520000   |         5,251 |      4,043,270 | SMH270115P00470000   |          973 |     4,164,440 |
| SMH      | SMH270115C00475000   |           934 |      2,621,738 | SMH270115P00475000   |          707 |     3,205,538 |
| SNDK     | SNDK261120C00800000  |         2,944 |     12,953,600 | SNDK261120P01500000  |        1,953 |   138,663,000 |
| SNDK     | SNDK261120C00780000  |         2,266 |     12,265,858 | SNDK261120P01450000  |        2,093 |   138,297,068 |
| SNDK     | SNDK261120C00790000  |         1,613 |      7,960,155 | SNDK261120P01600000  |          527 |    42,497,280 |
| SNDK     | SNDK261120C00820000  |         2,242 |      7,835,790 | SNDK261120P01300000  |          738 |    37,844,640 |
| SPY      | SPY261120C00730000   |        66,318 |     60,017,790 | SPY261120P00740000   |       94,642 |   108,175,806 |
| SPY      | SPY261118C00730000   |        29,025 |     17,211,825 | SPY261120P00750000   |       37,703 |    70,994,749 |
| SPY      | SPY261118C00731000   |        24,653 |     13,066,090 | SPY261127P00725000   |       59,360 |    45,825,920 |
| SPY      | SPY261118C00732000   |        25,651 |     12,286,829 | SPY261120P00730000   |       58,874 |    37,855,982 |
| TLT      | TLT270115C00080000   |        13,783 |      1,860,705 | TLT261231P00079000   |       13,018 |     1,562,160 |
| TLT      | TLT261231C00082000   |        10,542 |        495,474 | TLT261120P00085000   |        2,010 |     1,079,370 |
| TLT      | TLT261224C00077000   |         1,610 |        452,410 | TLT261120P00084000   |        2,026 |       885,362 |
| TLT      | TLT261218C00081000   |         7,372 |        442,320 | TLT270115P00097000   |          401 |       707,765 |
| TSLA     | TSLA261118C00380000  |        27,403 |     14,934,635 | TSLA261118P00380000  |       25,702 |    13,750,570 |
| TSLA     | TSLA261118C00382500  |        23,990 |      9,955,850 | TSLA261118P00377500  |       20,132 |     8,717,156 |
| TSLA     | TSLA261118C00385000  |        26,437 |      8,195,470 | TSLA261120P00380000  |        8,433 |     7,581,267 |
| TSLA     | TSLA261120C00380000  |         8,383 |      7,729,126 | TSLA261118P00375000  |       21,958 |     7,465,720 |
| TSM      | TSM270115C00380000   |         5,366 |     10,249,060 | TSM261204P00430000   |        7,330 |    51,383,300 |
| TSM      | TSM270115C00400000   |         2,936 |      3,749,272 | TSM261218P00400000   |        7,076 |    33,292,580 |
| TSM      | TSM270115C00370000   |         1,112 |      2,635,440 | TSM261120P00450000   |        1,893 |    17,273,625 |
| TSM      | TSM261218C00350000   |           923 |      2,547,480 | TSM261120P00440000   |        1,990 |    16,168,750 |
| UNH      | UNH270115C00450000   |         2,711 |        989,515 | UNH261218P00390000   |          653 |     1,091,816 |
| UNH      | UNH261120C00130000   |            36 |        939,348 | UNH261218P00410000   |          358 |     1,067,914 |
| UNH      | UNH261120C00400000   |         3,197 |        748,098 | UNH270115P00390000   |          471 |     1,040,910 |
| UNH      | UNH270115C00400000   |           399 |        679,896 | UNH261218P00380000   |          730 |       904,470 |
| WULF     | WULF261218C00013000  |         8,796 |        791,640 | WULF261218P00011000  |        7,187 |       761,822 |
| WULF     | WULF261127C00012000  |         6,029 |        452,175 | WULF261204P00014000  |        1,223 |       319,203 |
| WULF     | WULF270115C00015000  |         4,913 |        393,040 | WULF261120P00011000  |        6,947 |       236,198 |
| WULF     | WULF261120C00012000  |         5,914 |        289,786 | WULF270115P00010000  |        1,825 |       186,150 |
| XLF      | XLF261211C00058000   |         6,688 |        568,480 | XLF270115P00050000   |      142,095 |     5,541,705 |
| XLF      | XLF261120C00056000   |         3,221 |        447,719 | XLF261218P00056000   |       20,108 |     1,829,828 |
| XLF      | XLF261218C00058000   |         3,699 |        392,094 | XLF261218P00055000   |       28,264 |     1,780,632 |
| XLF      | XLF270115C00036000   |           140 |        301,980 | XLF270115P00055000   |       16,638 |     1,730,352 |
| XLU      | XLU270115C00042000   |         7,507 |      1,651,540 | XLU261218P00043000   |        4,925 |       320,125 |
| XLU      | XLU261218C00044000   |         4,214 |        337,120 | XLU261218P00041000   |       10,067 |       191,273 |
| XLU      | XLU261218C00042000   |         1,484 |        304,220 | XLU270115P00042000   |        2,589 |       165,696 |
| ^VIX     | VIX261216C00014000   |        30,139 |     25,618,150 | VIX261118P00025000   |      112,578 |    13,396,782 |
| ^VIX     | VIX261118C00025000   |       141,524 |     11,604,968 | VIX261216P00019000   |       46,059 |     4,283,487 |
| ^VIX     | VIXW261201C00024000  |        45,585 |     10,575,720 | VIX261118P00024000   |       57,603 |     4,032,210 |
| ^VIX     | VIX261118C00020000   |        19,941 |      9,172,860 | VIX261118P00024500   |       31,824 |     2,736,864 |

## T3 — Top 3 OTM Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261118C00355000  |        59,828 |      6,281,940 | AAPL261118P00350000  |       61,182 |    10,095,030 |
| AAPL     | AAPL261118C00352500  |        25,879 |      5,460,469 | AAPL261120P00350000  |       17,289 |     5,705,370 |
| AAPL     | AAPL270115C00355000  |         2,233 |      3,010,084 | AAPL261218P00350000  |        6,304 |     5,705,120 |
| AMZN     | AMZN261118C00260000  |        15,805 |      3,287,440 | AMZN261118P00255000  |       11,330 |     2,198,020 |
| AMZN     | AMZN261120C00260000  |         7,375 |      2,950,000 | AMZN261118P00257500  |        6,875 |     2,028,125 |
| AMZN     | AMZN261127C00260000  |         4,651 |      2,734,788 | AMZN261218P00250000  |        2,263 |     1,835,293 |
| ARM      | ARM261120C00185000   |         1,321 |        990,750 | ARM261120P00180000   |          824 |       622,120 |
| ARM      | ARM261120C00200000   |         1,445 |        381,480 | ARM261218P00180000   |          340 |       551,140 |
| ARM      | ARM261120C00190000   |           681 |        365,697 | ARM261120P00177500   |          792 |       468,072 |
| AVGO     | AVGO261120C00345000  |         3,731 |      3,507,140 | AVGO270115P00320000  |        1,146 |     2,452,440 |
| AVGO     | AVGO270115C00350000  |         1,109 |      3,038,660 | AVGO261120P00332500  |        2,781 |     2,361,069 |
| AVGO     | AVGO261218C00380000  |         2,561 |      2,855,515 | AVGO261218P00340000  |          921 |     2,259,213 |
| BABA     | BABA270115C00090000  |         1,433 |        796,748 | BABA270115P00080000  |        6,554 |     2,457,750 |
| BABA     | BABA270115C00100000  |         3,185 |        796,250 | BABA270115P00070000  |        3,516 |       485,208 |
| BABA     | BABA261218C00100000  |         4,690 |        628,460 | BABA270115P00085000  |          676 |       385,320 |
| CIFR     | CIFR261218C00007000  |         7,612 |        548,064 | CIFR261120P00006000  |        1,604 |        40,100 |
| CIFR     | CIFR270115C00007000  |         2,612 |        276,872 | CIFR261218P00006000  |          317 |        24,092 |
| COIN     | COIN261218C00130000  |         1,096 |        499,776 | COIN261218P00110000  |        6,479 |     4,729,670 |
| COIN     | COIN261120C00120000  |         1,908 |        389,232 | COIN261120P00110000  |        4,630 |       949,150 |
| COIN     | COIN261218C00140000  |         1,077 |        261,711 | COIN261120P00105000  |        4,491 |       431,136 |
| CRWV     | CRWV261218C00055000  |        17,086 |      7,569,098 | CRWV261120P00049500  |        3,268 |       950,988 |
| CRWV     | CRWV261120C00050000  |         6,036 |      1,871,160 | CRWV270115P00040000  |        2,354 |       870,980 |
| CRWV     | CRWV261120C00055000  |        12,126 |      1,515,750 | CRWV261218P00040000  |        3,461 |       847,945 |
| ETHA     | ETHA261218C00047000  |         1,120 |         95,200 | ETHA261127P00040000  |        5,402 |       702,260 |
| ETHA     | ETHA261218C00041000  |           303 |         81,810 | ETHA261218P00040000  |        1,544 |       378,280 |
| GLD      | GLD261120C00360000   |         7,940 |        992,500 | GLD261218P00350000   |        2,051 |     1,671,565 |
| GLD      | GLD261231C00387000   |         4,103 |        964,205 | GLD261218P00345000   |        1,588 |       976,620 |
| GLD      | GLD261218C00365000   |         1,306 |        709,158 | GLD261231P00320000   |        4,191 |       838,200 |
| GOOG     | GOOG270115C00300000  |         1,148 |        849,520 | GOOG261120P00277500  |        2,317 |     1,177,036 |
| GOOG     | GOOG270115C00280000  |           482 |        748,546 | GOOG261218P00270000  |        1,093 |       956,375 |
| GOOG     | GOOG261218C00290000  |           964 |        655,520 | GOOG261127P00270000  |        2,002 |       836,836 |
| GOOGL    | GOOGL270115C00295000 |         3,147 |      3,084,060 | GOOGL261118P00280000 |       10,671 |     3,297,339 |
| GOOGL    | GOOGL270115C00300000 |         3,607 |      3,033,487 | GOOGL270115P00280000 |        1,417 |     2,135,419 |
| GOOGL    | GOOGL261218C00285000 |         2,358 |      2,358,000 | GOOGL261120P00277500 |        4,050 |     1,599,750 |
| HIMS     | HIMS261218C00018000  |         1,728 |        247,104 | HIMS261218P00017000  |        2,388 |       291,336 |
| IBIT     | IBIT261127C00038000  |        35,726 |      1,500,492 | IBIT261218P00036000  |       15,554 |     2,830,828 |
| IBIT     | IBIT261218C00037000  |         8,740 |      1,372,180 | IBIT261127P00036000  |       12,797 |     1,382,076 |
| IBIT     | IBIT261127C00037000  |        10,908 |        839,916 | IBIT261218P00034000  |       10,955 |     1,172,185 |
| INTC     | INTC261218C00060000  |        13,060 |      3,918,000 | INTC261120P00054000  |       17,416 |     3,152,296 |
| INTC     | INTC261127C00056000  |         4,580 |      1,241,180 | INTC270115P00055000  |        4,632 |     2,844,048 |
| INTC     | INTC261120C00056000  |         6,094 |      1,151,766 | INTC261120P00055000  |        8,338 |     1,867,712 |
| IREN     | IREN261120C00016000  |         7,613 |        723,235 | IREN261120P00015000  |        8,070 |       548,760 |
| IREN     | IREN261231C00016000  |         2,651 |        691,911 | IREN270115P00010000  |        5,229 |       407,862 |
| IREN     | IREN261218C00016000  |         2,831 |        653,961 | IREN261218P00015000  |        1,874 |       356,060 |
| MARA     | MARA261218C00007000  |         6,733 |        356,849 | MARA270115P00006000  |        1,161 |        89,397 |
| MRVL     | MRVL261120C00155000  |         5,205 |      2,342,250 | MRVL270115P00145000  |        1,121 |     2,000,985 |
| MRVL     | MRVL261218C00165000  |         2,351 |      2,209,940 | MRVL261120P00147000  |          946 |       718,960 |
| MRVL     | MRVL261218C00150000  |         1,266 |      1,962,300 | MRVL270115P00130000  |          555 |       603,840 |
| MSTR     | MSTR261120C00100000  |         8,607 |      2,177,571 | MSTR261120P00095000  |        7,586 |     2,556,482 |
| MSTR     | MSTR270115C00105000  |         1,646 |      1,570,284 | MSTR261120P00090000  |        8,372 |     1,439,984 |
| MSTR     | MSTR261120C00098000  |         3,152 |      1,040,160 | MSTR261127P00095000  |        2,246 |     1,170,166 |
| NFLX     | NFLX261218C00060000  |         1,619 |        391,798 | NFLX270115P00058000  |        1,838 |       485,232 |
| NFLX     | NFLX261120C00060000  |         5,017 |        391,326 | NFLX261218P00059000  |        2,194 |       473,904 |
| NFLX     | NFLX261218C00063000  |         2,761 |        336,842 | NFLX261120P00059000  |        4,880 |       317,200 |
| NVDA     | NVDA261118C00160000  |        60,168 |     26,774,760 | NVDA261118P00155000  |       41,450 |    24,870,000 |
| NVDA     | NVDA261120C00160000  |        41,343 |     23,152,080 | NVDA261118P00150000  |       63,677 |    24,834,030 |
| NVDA     | NVDA270115C00170000  |        18,203 |     15,654,580 | NVDA261118P00152500  |       45,582 |    22,654,254 |
| QCOM     | QCOM261218C00185000  |         1,064 |        425,600 | QCOM261120P00165000  |          564 |       267,900 |
| QCOM     | QCOM270115C00190000  |           467 |        262,921 | QCOM270115P00130000  |          643 |       221,835 |
| QQQ      | QQQ261218C00660000   |        11,630 |     26,446,620 | QQQ261120P00650000   |       42,690 |    33,042,060 |
| QQQ      | QQQ270115C00700000   |        16,807 |     19,412,085 | QQQ270115P00645000   |        9,454 |    21,602,390 |
| QQQ      | QQQ261218C00665000   |         9,135 |     18,498,375 | QQQ261218P00645000   |       12,262 |    21,495,286 |
| RIOT     | RIOT261127C00018000  |         4,808 |        394,256 | RIOT261120P00016500  |        1,900 |       114,000 |
| RIOT     | RIOT261218C00020000  |         3,031 |        284,914 | RIOT261218P00014000  |        1,093 |        74,324 |
| RIOT     | RIOT261120C00017500  |         3,790 |        250,140 | RIOT261120P00017000  |          735 |        60,270 |
| RKLB     | RKLB261120C00060000  |         6,753 |        452,451 | RKLB261218P00055000  |        1,357 |       739,565 |
| RKLB     | RKLB261218C00060000  |           764 |        259,760 | RKLB261120P00055000  |        1,951 |       460,436 |
| SLV      | SLV261218C00043000   |         3,971 |        802,142 | SLV270115P00042000   |        1,277 |       310,311 |
| SLV      | SLV270115C00045000   |         2,308 |        454,676 | SLV261218P00042000   |          605 |       110,110 |
| SLV      | SLV261218C00048000   |         5,963 |        322,002 | SLV261127P00042500   |          745 |        87,165 |
| SMCI     | SMCI261120C00027500  |        30,463 |        731,112 | SMCI261218P00024000  |        2,310 |       595,980 |
| SMCI     | SMCI261120C00025000  |         6,955 |        577,265 | SMCI261120P00024000  |        3,588 |       412,620 |
| SMCI     | SMCI261120C00029000  |        30,491 |        304,910 | SMCI270115P00020000  |        2,420 |       396,880 |
| SMH      | SMH261218C00500000   |         3,542 |      4,749,822 | SMH261218P00400000   |        5,884 |     5,772,204 |
| SMH      | SMH261218C00520000   |         5,251 |      4,043,270 | SMH270115P00450000   |        1,869 |     5,704,188 |
| SMH      | SMH270115C00475000   |           934 |      2,621,738 | SMH261204P00455000   |        1,261 |     2,875,080 |
| SNDK     | SNDK261120C00800000  |         2,944 |     12,953,600 | SNDK261120P00750000  |        2,690 |     6,832,600 |
| SNDK     | SNDK261120C00820000  |         2,242 |      7,835,790 | SNDK261120P00790000  |        1,492 |     6,281,320 |
| SNDK     | SNDK261120C00850000  |         2,400 |      5,772,000 | SNDK261120P00770000  |        1,668 |     5,439,348 |
| SPY      | SPY261118C00733000   |        24,019 |     10,087,980 | SPY261127P00725000   |       59,360 |    45,825,920 |
| SPY      | SPY261118C00735000   |        25,935 |      8,428,875 | SPY261120P00730000   |       58,874 |    37,855,982 |
| SPY      | SPY261120C00740000   |        19,788 |      7,974,564 | SPY261204P00700000   |       62,692 |    31,032,540 |
| TLT      | TLT270115C00080000   |        13,783 |      1,860,705 | TLT261231P00079000   |       13,018 |     1,562,160 |
| TLT      | TLT261231C00082000   |        10,542 |        495,474 | TLT261231P00075000   |       15,766 |       283,788 |
| TLT      | TLT261218C00081000   |         7,372 |        442,320 | TLT261118P00079500   |       17,898 |       250,572 |
| TSLA     | TSLA261118C00382500  |        23,990 |      9,955,850 | TSLA261118P00380000  |       25,702 |    13,750,570 |
| TSLA     | TSLA261118C00385000  |        26,437 |      8,195,470 | TSLA261118P00377500  |       20,132 |     8,717,156 |
| TSLA     | TSLA261118C00390000  |        27,543 |      4,406,880 | TSLA261120P00380000  |        8,433 |     7,581,267 |
| TSM      | TSM270115C00380000   |         5,366 |     10,249,060 | TSM261218P00350000   |        2,558 |     4,361,390 |
| TSM      | TSM270115C00400000   |         2,936 |      3,749,272 | TSM261120P00350000   |        3,720 |     2,250,600 |
| TSM      | TSM270115C00370000   |         1,112 |      2,635,440 | TSM261218P00340000   |        1,185 |     1,659,000 |
| UNH      | UNH270115C00450000   |         2,711 |        989,515 | UNH261218P00380000   |          730 |       904,470 |
| UNH      | UNH261120C00400000   |         3,197 |        748,098 | UNH261218P00360000   |          805 |       512,785 |
| UNH      | UNH270115C00400000   |           399 |        679,896 | UNH261120P00377500   |        1,572 |       345,840 |
| WULF     | WULF261218C00013000  |         8,796 |        791,640 | WULF261218P00011000  |        7,187 |       761,822 |
| WULF     | WULF261127C00012000  |         6,029 |        452,175 | WULF261120P00011000  |        6,947 |       236,198 |
| WULF     | WULF270115C00015000  |         4,913 |        393,040 | WULF270115P00010000  |        1,825 |       186,150 |
| XLF      | XLF261211C00058000   |         6,688 |        568,480 | XLF270115P00050000   |      142,095 |     5,541,705 |
| XLF      | XLF261218C00058000   |         3,699 |        392,094 | XLF261218P00056000   |       20,108 |     1,829,828 |
| XLF      | XLF270115C00058000   |           901 |        127,041 | XLF261218P00055000   |       28,264 |     1,780,632 |
| XLU      | XLU261218C00044000   |         4,214 |        337,120 | XLU261218P00043000   |        4,925 |       320,125 |
| ^VIX     | VIX261216C00035000   |        67,013 |      7,505,456 | VIX261118P00025000   |      112,578 |    13,396,782 |
| ^VIX     | VIXW261201C00028000  |        45,829 |      6,278,573 | VIX261216P00019000   |       46,059 |     4,283,487 |
| ^VIX     | VIX261216C00040000   |        71,592 |      6,156,912 | VIX261118P00024000   |       57,603 |     4,032,210 |

*premium = volume × lastPrice × 100 · OTM = calls strike>spot, puts strike<spot · T4 uses the cleaned chain: ≥2 DTE, OTM only, leveraged ETFs folded into their underlying, ^VIX ratio inverted · Net Signed Premium = bought calls/sold puts minus sold calls/bought puts, side from lastPrice vs bid/ask (prints outside the closing quote are not signed) · generated by options-flow-pipeline*

---

**Data quality:** requested: 52 · fetched: 52 · failed: 0 · gated: 9 · stale volume: 21,139 contracts (24% of premium) dropped

_Signal check (next-day rank correlation, last 20 sessions): composite IC +0.022 (t +0.4, n=20) · flow_pct IC -0.082 (t -2.0, n=20) · trend_pct IC +0.106 (t +1.6, n=20)_

_Signal check, next 5 sessions (rank correlation, last 20 resolved sessions; windows overlap, so t is overstated): composite IC -0.039 (t -0.8, n=20) · flow_pct IC -0.135 (t -4.0, n=20) · trend_pct IC +0.059 (t +1.4, n=20)_