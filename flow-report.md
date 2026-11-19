# Options Flow Report (v1.3) — 2026-11-18

**Run stats:** 52/52 tickers fetched · 0 failed · 53,827 contracts

## Market Regime

**neutral risk · backwardation (VIX/VIX3M=1.01, DoD -0.01) · negative gamma (moves amplified) · high vol · choppy/rangebound — momentum tilted**

`Vol: HIGH · Trend: CHOP · Risk: NEUTRAL · Gamma: NEGATIVE · SPY GEX: $-16,908M`

_Pipeline knobs: mom×0.85 · conviction≥0.88_

## Master Scoreboard (all tickers by composite)

| Rank   | Ticker   | Composite   | Trend%   | Mom%   | Flow%   | Rot%   | Conviction   | ΔRank   |
|:-------|:---------|:------------|:---------|:-------|:--------|:-------|:-------------|:--------|
| 1      | XLV      | 100.0       | 100      | 100    | N/A     | 95     | CONFIRMED    | 0       |
| 2      | XLP      | 98.3        | 98       | 93     | N/A     | 92     | CONFIRMED    | 0       |
| 3      | XLE      | 93.3        | 93       | 87     | N/A     | 84     | NEUTRAL      | 0       |
| 4      | XLY      | 90.0        | 90       | 71     | N/A     | 87     | NEUTRAL      | +4      |
| 5      | XLB      | 88.3        | 88       | 78     | N/A     | 80     | NEUTRAL      | -1      |
| 6      | XLK      | 86.7        | 87       | 82     | N/A     | 71     | NEUTRAL      | +1      |
| 7      | BIL      | 85.0        | 85       | 68     | N/A     | 83     | NEUTRAL      | -1      |
| 8      | XLRE     | 83.3        | 83       | 72     | N/A     | 79     | NEUTRAL      | -3      |
| 9      | AMZN     | 82.2        | 92       | 66     | 74      | 94     | NEUTRAL      | +3      |
| 10     | QCOM     | 71.7        | 65       | 52     | 77      | 69     | NEUTRAL      | +28     |
| 11     | IWM      | 71.7        | 72       | 66     | N/A     | 69     | NEUTRAL      | +4      |
| 12     | RIOT     | 71.2        | 55       | 50     | 85      | 62     | NEUTRAL      | +7      |
| 13     | HYG      | 63.3        | 63       | 50     | N/A     | 70     | NEUTRAL      | +3      |
| 14     | XLI      | 61.7        | 62       | 59     | N/A     | 57     | NEUTRAL      | +6      |
| 15     | HIVE     | 59.4        | 12       | 14     | 100     | 12     | CONFLICT     | +2      |
| 16     | TSLA     | 58.9        | 70       | 54     | 49      | 81     | NEUTRAL      | +10     |
| 17     | QQQ      | 57.9        | 75       | 70     | 43      | 69     | NEUTRAL      | +15     |
| 18     | UNH      | 57.3        | 80       | 73     | 38      | 77     | NEUTRAL      | -7      |
| 19     | INTC     | 57.1        | 50       | 66     | 63      | 41     | NEUTRAL      | +31     |
| 20     | AAPL     | 57.1        | 97       | 81     | 23      | 100    | CONFLICT     | +4      |
| 21     | SMCI     | 56.8        | 37       | 47     | 74      | 32     | CONFLICT     | +31     |
| 22     | GOOGL    | 56.2        | 47       | 48     | 64      | 46     | NEUTRAL      | +9      |
| 23     | MRVL     | 55.6        | 82       | 77     | 33      | 73     | CONFLICT     | -13     |
| 24     | XLU      | 55.2        | 73       | 63     | 40      | 73     | NEUTRAL      | +24     |
| 25     | NFLX     | 54.9        | 22       | 15     | 83      | 33     | CONFLICT     | +19     |
| 26     | GOOG     | 54.6        | 45       | 46     | 63      | 45     | NEUTRAL      | +21     |
| 27     | AVGO     | 54.5        | 60       | 51     | 50      | 63     | NEUTRAL      | +19     |
| 28     | OPEN     | 53.7        | 2        | 3      | 98      | 2      | CONFLICT     | +5      |
| 29     | CPER     | 53.3        | 53       | 62     | N/A     | 49     | NEUTRAL      | -15     |
| 30     | EOSE     | 53.3        | 3        | 7      | 96      | 2      | CONFLICT     | -2      |
| 31     | CLSK     | 53.2        | 17       | 24     | 84      | 15     | CONFLICT     | -8      |
| 32     | SMR      | 52.9        | 5        | 11     | 94      | 6      | CONFLICT     | +21     |
| 33     | QBTS     | 52.9        | 10       | 18     | 89      | 7      | CONFLICT     | +24     |
| 34     | LQD      | 51.7        | 52       | 47     | N/A     | 63     | NEUTRAL      | -12     |
| 35     | TSM      | 51.6        | 78       | 81     | 29      | 66     | CONFLICT     | -26     |
| 36     | XLC      | 48.3        | 48       | 45     | N/A     | 55     | NEUTRAL      | +3      |
| 37     | SPY      | 47.9        | 77       | 63     | 23      | 80     | CONFLICT     | -2      |
| 38     | NVDA     | 47.7        | 40       | 45     | 54      | 33     | NEUTRAL      | +3      |
| 39     | RGTI     | 47.1        | 15       | 21     | 74      | 14     | CONFLICT     | +19     |
| 40     | WULF     | 46.8        | 42       | 47     | 51      | 38     | NEUTRAL      | -11     |
| 41     | XLF      | 45.9        | 95       | 86     | 4       | 86     | CONFLICT     | -11     |
| 42     | TLT      | 45.9        | 58       | 52     | 35      | 61     | NEUTRAL      | -24     |
| 43     | CIFR     | 45.7        | 13       | 22     | 73      | 8      | CONFLICT     | -6      |
| 44     | SMH      | 45.7        | 68       | 75     | 26      | 57     | CONFLICT     | -4      |
| 45     | OKLO     | 42.9        | 8        | 10     | 72      | 10     | CONFLICT     | -2      |
| 46     | SLV      | 42.7        | 32       | 38     | 52      | 29     | NEUTRAL      | -21     |
| 47     | HIMS     | 42.5        | 30       | 37     | 53      | 25     | NEUTRAL      | +2      |
| 48     | ARM      | 42.2        | 67       | 70     | 21      | 53     | CONFLICT     | -14     |
| 49     | BABA     | 37.1        | 18       | 16     | 53      | 24     | NEUTRAL      | +7      |
| 50     | ETHA     | 36.8        | 38       | 40     | 35      | 38     | NEUTRAL      | +10     |
| 51     | IREN     | 35.1        | 7        | 16     | 59      | 2      | NEUTRAL      | -6      |
| 52     | MARA     | 34.5        | 25       | 25     | 43      | 24     | NEUTRAL      | -25     |
| 53     | CRWV     | 34.4        | 27       | 32     | 41      | 17     | NEUTRAL      | -17     |
| 54     | AI       | 32.9        | 57       | 57     | 13      | 56     | NEUTRAL      | -41     |
| 55     | GLD      | 29.3        | 33       | 35     | 26      | 42     | NEUTRAL      | -13     |
| 56     | IONQ     | 27.9        | 20       | 23     | 35      | 19     | NEUTRAL      | -5      |
| 57     | IBIT     | 27.4        | 43       | 43     | 14      | 44     | NEUTRAL      | -3      |
| 58     | RKLB     | 25.2        | 35       | 43     | 17      | 35     | NEUTRAL      | +1      |
| 59     | MSTR     | 24.2        | 28       | 30     | 21      | 30     | NEUTRAL      | -4      |
| 60     | COIN     | 23.8        | 23       | 26     | 24      | 22     | NEUTRAL      | +1      |
| N/A    | AAPX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDU     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | SNDK     | N/A         | N/A      | N/A    | 28      | N/A    | INSUFFICIENT | ·       |
| N/A    | TSLL     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^GSPC    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^SKEW    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX     | N/A         | N/A      | N/A    | 66      | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX3M   | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VVIX    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |

## Sector Rotation / Relative Strength (top 15)

| Ticker   |   RS Rating |   Rel Str 63d | RS New-High   | Dual-Mom   |
|:---------|------------:|--------------:|:--------------|:-----------|
| AAPL     |          99 |          17.3 | Yes           | above cash |
| XLV      |          97 |           9.5 | No            | above cash |
| AMZN     |          96 |           6.9 | No            | above cash |
| MRVL     |          94 |         -38   | No            | above cash |
| XLP      |          92 |          11.6 | No            | above cash |
| XLE      |          91 |           0.7 | No            | above cash |
| XLF      |          89 |           3.4 | No            | above cash |
| XLY      |          87 |           6.4 | No            | above cash |
| XLB      |          86 |           0.7 | No            | above cash |
| UNH      |          84 |          -4.5 | No            | above cash |
| BIL      |          82 |           4.9 | No            | below cash |
| XLRE     |          81 |           1.6 | No            | above cash |
| SPY      |          79 |           0   | Yes           | above cash |
| XLK      |          77 |          -6.4 | No            | above cash |
| TSLA     |          76 |          15.2 | No            | below cash |

## Option Skew — Extremes (top/bottom 8)

_Board-wide: protection demand rising across the board (typical name z +1.3 vs its own norm; 24 of 34 names at z +1 or more, 0 at −1 or less). Hedging arrows are measured net of this move._

| Ticker   | Group    | Tilt             |   Skew25 (vol pts) | 90-110   |   ATM IV % |   Skew/IV | Hedging            |    z | Flow        | Positioning   |
|:---------|:---------|:-----------------|-------------------:|:---------|-----------:|----------:|:-------------------|-----:|:------------|:--------------|
| SPY      | top 8    | put-skewed       |                7.4 | 14.8     |       20.2 |      0.37 | hedging easing ↓   | -1.3 | Neutral +7  |               |
| QQQ      | top 8    | put-skewed       |                8.2 | 13.6     |       28.9 |      0.28 | hedging easing ↓   | -1.4 | Neutral +1  |               |
| AAPL     | top 8    | put-skewed       |                5.5 | 10.4     |       24.4 |      0.23 | steady →           | -0.1 | Neutral +5  |               |
| SMH      | top 8    | put-skewed       |               10.1 | 10.4     |       51.4 |      0.2  | steady →           |  0.3 | Neutral -1  |               |
| MSTR     | top 8    | put-skewed       |               14.9 | 9.3      |       89.3 |      0.17 | steady →           |  0.5 | Neutral -11 |               |
| IBIT     | top 8    | put-skewed       |                7.4 | 8.4      |       46.5 |      0.16 | steady →           |  0.4 | Bull +31    |               |
| UNH      | top 8    | put-skewed       |                6.4 | 8.0      |       41.6 |      0.15 | steady →           |  1   | Neutral +7  |               |
| TSLL     | top 8    | put-skewed       |               14.9 | 10.4     |       98.7 |      0.15 | steady →           |  0.7 | n/a         |               |
| TLT      | bottom 8 | least put-skewed |                0   | N/A      |       12.3 |      0    | steady →           | -0.9 | Neutral +3  |               |
| HIMS     | bottom 8 | put-skewed       |                3.7 | 2.9      |       75.9 |      0.05 | steady →           |  0.8 | Neutral +12 |               |
| BABA     | bottom 8 | put-skewed       |                3.2 | 3.5      |       51.2 |      0.06 | steady →           |  0.7 | Neutral +7  |               |
| RIOT     | bottom 8 | put-skewed       |                6.6 | 4.1      |       93.9 |      0.07 | hedging building ↑ |  1.4 | Neutral +0  |               |
| GLD      | bottom 8 | put-skewed       |                1.9 | 3.6      |       25.7 |      0.07 | steady →           | -0.6 | Neutral +17 |               |
| NFLX     | bottom 8 | put-skewed       |                2.7 | 4.6      |       35.2 |      0.08 | steady →           |  0.2 | Neutral -1  |               |
| RKLB     | bottom 8 | put-skewed       |                7.1 | 4.6      |       84.6 |      0.08 | steady →           |  0   | Neutral +18 |               |
| SNDK     | bottom 8 | put-skewed       |                9.1 | 4.1      |       99.3 |      0.09 | steady →           | -0.6 | Neutral -5  |               |

_34 of 52 tickers had a fittable smile. Skew25 = how much more an out-of-the-money put costs than the matching out-of-the-money call, in vol points, at a constant 30-day tenor, re-derived from bid/ask mids (Yahoo's own IV field is not used). Positive = puts richer, the normal state — so read the *ranking*, not the level. Tilt is by sign: call-skewed = Skew/IV below 0; least put-skewed = 0 to 0.02; put-skewed above. Hedging = tonight's Skew/IV against the name's own previous 20 sessions (z = standard deviations from that average), net of the typical name's move tonight (the Board-wide line above): building when z is at least +1, easing at −1 or below, else steady; n/a until 10 prior sessions exist. It describes protection demand, not a price forecast._

## Mega-Cap Tech Skew

| Ticker   |   Skew25 (vol pts) |   90-110 |   ATM IV % |   Skew/IV | Rank     | Read           | Hedging          |    z | Flow        | Positioning   |
|:---------|-------------------:|---------:|-----------:|----------:|:---------|:---------------|:-----------------|-----:|:------------|:--------------|
| NVDA     |                5.3 |      5.9 |       51.4 |      0.1  | 22 of 34 | put-skewed     | hedging easing ↓ | -1.7 | Neutral -4  |               |
| AAPL     |                5.5 |     10.4 |       24.4 |      0.23 | 3 of 34  | steep put skew | steady →         | -0.1 | Neutral +5  |               |
| AMZN     |                5.3 |      7.7 |       36.2 |      0.15 | 12 of 34 | put-skewed     | steady →         | -0.3 | Neutral -5  |               |
| GOOGL    |                4.7 |      5.9 |       35.2 |      0.13 | 13 of 34 | put-skewed     | steady →         |  0.3 | Neutral +10 |               |
| TSLA     |                7.2 |      7.9 |       48.6 |      0.15 | 10 of 34 | put-skewed     | steady →         | -0.3 | Neutral +9  |               |
| AVGO     |                7.1 |      6.4 |       61.4 |      0.12 | 16 of 34 | put-skewed     | steady →         | -0.5 | Neutral +1  |               |

_Mega-cap tech: 6 of 6 fitted · median Skew/IV 0.14 vs 0.11 for the other names · richer downside protection than the rest of the board · steepest: AAPL._

_Flow = premium-weighted flow score: 100 × (bought calls + sold puts − sold calls − bought puts) ÷ total out-of-the-money premium, sides estimated from the last trade against bid/ask (a last trade outside the closing quote is left unsigned); Bull at +20 or more, Bear at −20 or less. Positioning: defensive = hedging building with Bear flow; speculative = hedging easing with Bull flow; blank otherwise. Positioning describes what is being hedged and flowed tonight. It is not a price forecast._

## Stretch & Reversal Watch (experimental)

| Watch             | Tonight                                                                          | Backtest (before live)                                       | Live since 2026-11-06                      |
|:------------------|:---------------------------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------|
| hedging unwinding | NVDA (z -1.7)                                                                    | 194 flags · +1.6% vs avg name · 59% beat it                  | 4 flags · -3.3% vs avg name · 25% beat it  |
| stretched up      | none                                                                             | 597 flags · -1.5% vs avg name · 41% beat it                  | 33 flags · -2.7% vs avg name · 48% beat it |
| washed out        | HIMS (-18%), UNH (-13%)                                                          | 118 flags · -0.1% vs avg name · 57% beat it (no edge so far) | 14 flags · +3.0% vs avg name · 71% beat it |
| puts closing      | SPY (97% puts), XLF (97% puts), COIN (96% puts), ETHA (95% puts), TLT (94% puts) | 805 flags · +0.7% vs avg name · 55% beat it (to 2026-11-16)  | none resolved yet (counts from 2026-11-16) |

_Experimental, not proven. Hedging unwinding = tonight's Skew/IV at z -1.5 or lower against the name's own norm, net of the board (as the Hedging column): protection being sold off. Stretched up = price up 5% or more over the last 5 sessions. Washed out = down 5% or more with hedging at z +2 or more on its own norm. Puts closing = the fifth of names where puts made up most of the out-of-the-money positions closed in the previous session (volume matched against the drop in open interest): protection taken off. The record columns score each past flag 5 sessions later against the average name that night (prices from the option chains' implied forwards). The backtest is in-sample: the thresholds were picked on that same history, so it flatters the flags; the live column counts only flags raised since this block was added and is the one that matters. If the live record does not hold up, the block goes. Not a price forecast._

---

# Flow Detail

## T4 — OTM Flow Summary (ranked by OTM Call/Put premium ratio)

|   Rank | Ticker   |   Premium Ratio |   Premium Ratio All |   Total Call Premium |   Total Put Premium |   Net Signed Premium |   Close Price | 1-Day Return   | 1-Week Return   | % Close to MA20   | % Close to MA50   | % Close to High   | % Close to Low   |   52 Week High |   52 Week Low | MA20   | MA50   |
|-------:|:---------|----------------:|--------------------:|---------------------:|--------------------:|---------------------:|--------------:|:---------------|:----------------|:------------------|:------------------|:------------------|:-----------------|---------------:|--------------:|:-------|:-------|
|      1 | CIFR     |            7    |                2.86 |            1,003,685 |             143,458 |              209,594 |          6.57 | 2.34%          | -3.52%          | -8.92%            | -43.85%           | -78.20%           | 29.56%           |          30.14 |          5.07 | 7.21   | 11.70  |
|      2 | NFLX     |            4.15 |                1.35 |            8,327,793 |           2,004,414 |              -68,126 |         59.82 | 0.23%          | -6.46%          | -5.30%            | -12.25%           | -47.22%           | 0.69%            |         113.34 |         59.41 | 63.17  | 68.17  |
|      3 | RIOT     |            3.92 |               13.74 |            5,063,098 |           1,292,978 |               14,081 |         18.24 | 6.98%          | 3.28%           | 18.83%            | 2.64%             | -39.84%           | 58.61%           |          30.32 |         11.5  | 15.35  | 17.77  |
|      4 | CLSK     |            3.79 |                2.75 |              641,309 |             169,261 |              -17,480 |          6.21 | 0.98%          | -10.13%         | -13.10%           | -38.36%           | -67.61%           | 12.30%           |          19.17 |          5.53 | 7.15   | 10.07  |
|      5 | SMCI     |            3.73 |                0.87 |            3,757,667 |           1,006,233 |               57,649 |         24.37 | 0.95%          | -14.79%         | -18.65%           | -31.61%           | -52.59%           | 25.10%           |          51.4  |         19.48 | 29.96  | 35.63  |
|      6 | QCOM     |            3.33 |                1.39 |            4,084,025 |           1,227,269 |              273,998 |        159.81 | -4.12%         | -6.80%          | -6.92%            | -10.34%           | -38.52%           | 31.00%           |         259.92 |        121.99 | 171.69 | 178.25 |
|      7 | AMZN     |            3.26 |                5.44 |           75,808,579 |          23,269,122 |           -5,068,264 |        267.74 | 3.82%          | 0.30%           | 4.13%             | 4.95%             | -6.78%            | 36.60%           |         287.2  |        196    | 257.13 | 255.12 |
|      8 | GOOG     |            3.02 |                0.12 |           16,166,010 |           5,358,257 |           -1,801,350 |        279.2  | 0.58%          | -2.38%          | -4.52%            | -13.26%           | -30.97%           | 2.82%            |         404.47 |        271.54 | 292.41 | 321.89 |
|      9 | GOOGL    |            2.55 |                0.31 |           25,996,203 |          10,187,434 |            3,775,852 |        282.44 | 0.80%          | -1.98%          | -4.18%            | -13.09%           | -30.88%           | 3.80%            |         408.61 |        272.11 | 294.77 | 324.96 |
|     10 | ^VIX     |            2.53 |                0.58 |           12,670,346 |          32,073,363 |           11,632,736 |         24.56 | -3.53%         | 23.29%          | 20.35%            | 37.81%            | -30.42%           | 83.56%           |          35.3  |         13.38 | 20.41  | 17.82  |
|     11 | IREN     |            2.5  |                1.75 |            5,500,039 |           2,196,166 |            1,953,205 |         15.24 | -3.57%         | -28.82%         | -30.29%           | -52.75%           | -78.45%           | 1.74%            |          70.71 |         14.98 | 21.86  | 32.26  |
|     12 | INTC     |            2.47 |                2.19 |           16,958,756 |           6,863,387 |           -6,990,273 |         54.67 | -0.91%         | -7.92%          | -19.81%           | -40.67%           | -61.59%           | 66.22%           |         142.35 |         32.89 | 68.18  | 92.15  |
|     13 | WULF     |            2.31 |                1.96 |            2,013,007 |             872,090 |            1,519,260 |         12    | 2.83%          | -3.07%          | -0.54%            | -12.08%           | -59.79%           | 26.18%           |          29.84 |          9.51 | 12.07  | 13.65  |
|     14 | BABA     |            2.25 |                0.57 |            7,044,974 |           3,136,291 |              691,732 |         84.37 | -2.63%         | -19.94%         | -15.00%           | -19.95%           | -53.41%           | 0.18%            |         181.1  |         84.22 | 99.26  | 105.40 |
|     15 | AVGO     |            1.92 |                1.53 |           45,147,808 |          23,463,777 |              641,112 |        354.05 | 3.64%          | 10.82%          | 6.62%             | 2.88%             | -28.47%           | 22.18%           |         495    |        289.77 | 332.07 | 344.15 |
|     16 | SLV      |            1.76 |                0.48 |            9,302,688 |           5,295,766 |            1,202,842 |         40.7  | -4.55%         | -15.45%         | -11.95%           | -21.41%           | -62.94%           | 0.74%            |         109.83 |         40.4  | 46.22  | 51.79  |
|     17 | TSLA     |            1.74 |                1.19 |           90,204,389 |          51,900,736 |           13,212,028 |        383.72 | 0.95%          | 1.50%           | -0.62%            | 2.10%             | -23.08%           | 29.03%           |         498.83 |        297.38 | 386.13 | 375.81 |
|     18 | MARA     |            1.67 |                0.67 |            1,200,289 |             718,770 |              759,529 |          6.56 | 2.18%          | -1.20%          | -4.67%            | -28.80%           | -60.07%           | 15.29%           |          16.43 |          5.69 | 6.88   | 9.21   |
|     19 | NVDA     |            1.51 |                0.38 |          208,868,061 |         138,173,600 |          -13,741,123 |        150.96 | -2.89%         | -15.51%         | -20.14%           | -28.22%           | -37.97%           | 1.45%            |         243.37 |        148.8  | 189.04 | 210.30 |
|     20 | IONQ     |            1.49 |                0.62 |              908,421 |             607,829 |              330,144 |         23.48 | -5.48%         | -33.56%         | -22.51%           | -33.83%           | -68.12%           | 1.25%            |          73.65 |         23.19 | 30.30  | 35.48  |
|     21 | TLT      |            1.45 |                1.08 |            4,834,997 |           3,327,466 |              264,544 |         80.22 | 0.84%          | -2.12%          | -1.03%            | 0.19%             | -11.71%           | 4.96%            |          90.86 |         76.43 | 81.06  | 80.07  |
|     22 | MRVL     |            1.42 |                0.13 |           13,705,006 |           9,656,908 |               29,776 |        145.54 | -2.15%         | -5.86%          | -19.42%           | -35.12%           | -55.88%           | 105.88%          |         329.88 |         70.69 | 180.61 | 224.32 |
|     22 | XLU      |            1.42 |                2.69 |            1,879,237 |           1,319,333 |              -29,162 |         43.55 | 0.30%          | -0.55%          | 0.43%             | 3.88%             | -8.89%            | 11.58%           |          47.8  |         39.03 | 43.36  | 41.93  |
|     24 | CRWV     |            1.41 |                0.82 |           18,413,130 |          13,043,950 |           -3,617,279 |         47.83 | -4.13%         | -2.35%          | -9.95%            | -31.54%           | -65.40%           | 17.87%           |         138.25 |         40.58 | 53.12  | 69.87  |
|     25 | QQQ      |            1.27 |                0.4  |          372,671,526 |         292,680,511 |            6,260,485 |        659.51 | 0.39%          | -2.92%          | -3.90%            | -7.68%            | -13.55%           | 18.70%           |         762.86 |        555.6  | 686.30 | 714.36 |
|     26 | ARM      |            1.2  |                0.72 |            3,256,108 |           2,706,682 |              208,489 |        182.76 | -0.34%         | -1.90%          | -8.07%            | -24.92%           | -59.63%           | 82.72%           |         452.7  |        100.02 | 198.81 | 243.41 |
|     26 | UNH      |            1.2  |                0.39 |           17,593,841 |          14,625,109 |            2,094,564 |        349.91 | -10.21%        | -12.00%         | -13.21%           | -10.43%           | -24.20%           | 36.70%           |         461.62 |        255.97 | 403.16 | 390.64 |
|     28 | SMH      |            1.11 |                0.3  |           38,386,674 |          34,595,042 |             -588,264 |        459.54 | -0.12%         | -5.72%          | -8.94%            | -16.92%           | -31.60%           | 45.86%           |         671.83 |        315.05 | 504.64 | 553.13 |
|     29 | TSM      |            1.05 |                0.58 |           23,414,913 |          22,392,650 |           -3,557,020 |        362.62 | 0.81%          | -6.69%          | -9.30%            | -14.87%           | -25.61%           | 35.90%           |         487.47 |        266.82 | 399.79 | 425.96 |
|     30 | RKLB     |            1.04 |                0.4  |            2,602,871 |           2,508,532 |              897,160 |         53.07 | -3.60%         | -9.84%          | -5.66%            | -14.28%           | -64.85%           | 41.26%           |         151    |         37.57 | 56.26  | 61.91  |
|     31 | GLD      |            1.03 |                0.06 |           22,584,460 |          21,904,424 |            7,685,393 |        341.19 | -3.20%         | -10.10%         | -6.34%            | -9.65%            | -33.06%           | 0.13%            |         509.7  |        340.76 | 364.30 | 377.64 |
|     32 | SNDK     |            1.01 |                0.09 |           81,241,155 |          80,746,357 |           -8,739,762 |        776.22 | -2.64%         | N/A             | N/A               | N/A               | -5.51%            | 3.58%            |         821.46 |        749.39 | N/A    | N/A    |
|     33 | AAPL     |            0.81 |                0.73 |           24,354,639 |          30,222,455 |            2,824,434 |        352.45 | 0.15%          | 0.50%           | 1.37%             | 3.31%             | -2.32%            | 44.79%           |         360.83 |        243.42 | 347.69 | 341.15 |
|     34 | COIN     |            0.59 |                0.04 |            3,662,403 |           6,222,989 |              703,924 |        110.51 | -3.92%         | -18.80%         | -22.05%           | -33.64%           | -61.19%           | 0.52%            |         284.74 |        109.94 | 141.76 | 166.53 |
|     35 | IBIT     |            0.56 |                0.37 |            7,229,625 |          12,976,153 |            6,177,657 |         35.36 | -2.16%         | -16.45%         | -16.86%           | -21.35%           | -36.40%           | 7.67%            |          55.6  |         32.84 | 42.53  | 44.96  |
|     36 | SPY      |            0.55 |                1.17 |          248,747,271 |         453,584,065 |           48,686,209 |        730.2  | -0.31%         | -2.99%          | -3.12%            | -4.24%            | -6.58%            | 16.04%           |         781.62 |        629.28 | 753.72 | 762.51 |
|     37 | MSTR     |            0.46 |                0.17 |           12,861,041 |          27,982,203 |           -4,656,813 |         90.32 | -6.40%         | -28.08%         | -28.95%           | -35.86%           | -55.71%           | 10.40%           |         203.95 |         81.81 | 127.12 | 140.82 |
|     38 | XLF      |            0.12 |                0.24 |              833,502 |           7,092,044 |            1,683,581 |         56.42 | -1.14%         | -2.71%          | -1.55%            | 0.84%             | -6.03%            | 18.36%           |          60.04 |         47.67 | 57.31  | 55.95  |

## T2 — Premium Ratio Leaderboard (all strikes, call subtotal ≥ $1,000,000)

|   Rank | Ticker   |   Premium Ratio |   Call Volume |   Call Premium |   Put Volume |   Put Premium |
|-------:|:---------|----------------:|--------------:|---------------:|-------------:|--------------:|
|      1 | RIOT     |           13.74 |       125,616 |     14,365,229 |       26,154 |     1,045,786 |
|      2 | AMZN     |            5.44 |        70,578 |     36,872,286 |       14,227 |     6,779,745 |
|      3 | XLU      |            2.69 |        50,620 |      2,533,521 |       23,593 |       940,097 |
|      4 | INTC     |            2.19 |        41,180 |      9,357,133 |       10,926 |     4,264,384 |
|      5 | WULF     |            1.96 |        16,823 |      1,377,185 |       13,098 |       704,348 |
|      6 | IREN     |            1.75 |        30,788 |      3,150,639 |       12,018 |     1,799,055 |
|      7 | AVGO     |            1.53 |        13,711 |     13,965,470 |        3,748 |     9,115,908 |
|      8 | QCOM     |            1.39 |         7,535 |      1,772,474 |        1,207 |     1,276,444 |
|      9 | NFLX     |            1.35 |        11,665 |      3,356,997 |        6,181 |     2,486,129 |
|     10 | TSLA     |            1.19 |        34,681 |     40,846,190 |       37,074 |    34,334,180 |
|     11 | SPY      |            1.17 |       155,293 |    161,144,221 |      151,469 |   137,558,126 |
|     12 | TLT      |            1.08 |        27,319 |      2,509,434 |       26,250 |     2,327,652 |
|     13 | SMCI     |            0.87 |        17,214 |      1,436,608 |        7,398 |     1,649,074 |
|     14 | CRWV     |            0.82 |        17,604 |      6,644,935 |        9,637 |     8,084,337 |
|     15 | AAPL     |            0.73 |        14,991 |     12,270,436 |       46,382 |    16,912,879 |
|     16 | ^VIX     |            0.58 |        55,423 |     13,345,863 |      106,159 |    23,207,892 |
|     16 | TSM      |            0.58 |         9,539 |     13,812,730 |       14,027 |    23,873,915 |
|     18 | BABA     |            0.57 |        12,077 |      3,172,710 |        3,653 |     5,602,901 |
|     19 | SLV      |            0.48 |        15,704 |      3,719,260 |       15,393 |     7,681,520 |
|     20 | QQQ      |            0.4  |        72,279 |     87,945,600 |       44,996 |   220,156,371 |
|     21 | UNH      |            0.39 |         6,777 |      6,258,247 |       12,839 |    15,951,582 |
|     22 | NVDA     |            0.38 |       209,202 |     51,524,919 |      147,536 |   137,380,132 |
|     23 | IBIT     |            0.37 |        70,055 |      4,247,622 |       50,781 |    11,608,099 |
|     24 | GOOGL    |            0.31 |         7,671 |      9,967,536 |        5,124 |    31,992,227 |
|     25 | SMH      |            0.3  |        15,802 |     18,345,784 |        6,333 |    61,338,290 |
|     26 | XLF      |            0.24 |         5,228 |      1,394,891 |       88,031 |     5,791,750 |
|     27 | MSTR     |            0.17 |         8,268 |      3,672,008 |        8,368 |    21,852,342 |
|     28 | MRVL     |            0.13 |         8,144 |      6,779,068 |        9,510 |    54,225,608 |
|     29 | GOOG     |            0.12 |        15,202 |      5,068,230 |        4,119 |    41,644,148 |
|     30 | SNDK     |            0.09 |        10,426 |     34,847,535 |        5,592 |   384,380,580 |
|     31 | GLD      |            0.06 |        12,403 |      8,970,140 |       30,140 |   158,869,264 |
|     32 | COIN     |            0.04 |         6,457 |      1,768,949 |        4,590 |    40,487,619 |

## T1 — Top 4 Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL270115C00270000  |           444 |      3,838,380 | AAPL261218P00350000  |        6,047 |     5,049,245 |
| AAPL     | AAPL270115C00250000  |           274 |      2,864,670 | AAPL261120P00350000  |       21,899 |     4,861,578 |
| AAPL     | AAPL261120C00355000  |        13,896 |      2,806,992 | AAPL261120P00355000  |        7,644 |     3,516,240 |
| AAPL     | AAPL261120C00280000  |           377 |      2,760,394 | AAPL261120P00352500  |       10,792 |     3,485,816 |
| AMZN     | AMZN261120C00270000  |        33,100 |     10,360,300 | AMZN270115P00270000  |        1,456 |     2,147,600 |
| AMZN     | AMZN261120C00265000  |        17,660 |     10,331,100 | AMZN261120P00265000  |        5,525 |     1,624,350 |
| AMZN     | AMZN261218C00280000  |        13,273 |      8,189,441 | AMZN261218P00300000  |          481 |     1,620,970 |
| AMZN     | AMZN270115C00275000  |         6,545 |      7,991,445 | AMZN261120P00262500  |        6,765 |     1,386,825 |
| ARM      | ARM261120C00185000   |         1,100 |        533,500 | ARM261120P00190000   |          438 |       473,040 |
| ARM      | ARM261120C00190000   |           653 |        195,900 | ARM261218P00200000   |          155 |       412,300 |
| ARM      | ARM261218C00200000   |           154 |        150,920 | ARM261120P00200000   |          178 |       342,650 |
| AVGO     | AVGO261120C00350000  |         4,390 |      4,675,350 | AVGO261120P00460000  |          275 |     2,857,250 |
| AVGO     | AVGO261120C00360000  |         6,840 |      3,796,200 | AVGO261218P00360000  |          854 |     2,311,778 |
| AVGO     | AVGO261218C00350000  |         1,030 |      2,853,100 | AVGO261218P00350000  |          905 |     2,027,200 |
| AVGO     | AVGO261218C00370000  |         1,451 |      2,640,820 | AVGO261120P00360000  |        1,714 |     1,919,680 |
| BABA     | BABA261218C00090000  |         3,576 |        986,976 | BABA270115P00090000  |        1,848 |     1,727,880 |
| BABA     | BABA270115C00090000  |         2,273 |        975,117 | BABA270115P00120000  |          430 |     1,522,200 |
| BABA     | BABA261120C00085000  |         2,855 |        708,040 | BABA261120P00120000  |          368 |     1,262,240 |
| BABA     | BABA261218C00095000  |         3,373 |        502,577 | BABA261127P00095000  |        1,007 |     1,090,581 |
| CIFR     | CIFR261218C00007000  |         4,258 |        340,640 | CIFR261204P00010500  |          294 |       119,070 |
| CLSK     | CLSK261127C00006500  |        10,661 |        362,474 | CLSK261218P00010000  |          345 |       131,790 |
| COIN     | COIN261218C00110000  |           710 |        710,000 | COIN270115P00250000  |        1,200 |    16,512,000 |
| COIN     | COIN261127C00120000  |         2,604 |        463,512 | COIN270115P00230000  |        1,050 |    12,348,000 |
| COIN     | COIN261120C00115000  |         2,271 |        333,837 | COIN261120P00165000  |        1,153 |     6,327,664 |
| COIN     | COIN261218C00130000  |           872 |        261,600 | COIN261120P00155000  |        1,187 |     5,299,955 |
| CRWV     | CRWV261218C00050000  |         4,376 |      2,034,840 | CRWV261218P00075000  |          798 |     2,189,712 |
| CRWV     | CRWV270115C00060000  |         5,767 |      1,891,576 | CRWV270115P00040000  |        5,560 |     2,085,000 |
| CRWV     | CRWV261127C00048000  |         4,910 |      1,522,100 | CRWV261120P00058000  |        1,845 |     1,909,575 |
| CRWV     | CRWV270115C00055000  |         2,551 |      1,196,419 | CRWV261120P00061000  |        1,434 |     1,900,050 |
| ETHA     | ETHA270115C00020000  |           222 |        448,440 | ETHA261120P00045500  |        4,716 |     2,829,600 |
| ETHA     | ETHA261218C00025000  |           222 |        323,010 | ETHA261120P00044000  |        4,715 |     2,145,325 |
| GLD      | GLD270115C00355000   |         3,762 |      3,254,130 | GLD270115P00425000   |        5,538 |    47,061,924 |
| GLD      | GLD270115C00345000   |         2,433 |      3,153,168 | GLD270115P00420000   |        5,620 |    44,566,600 |
| GLD      | GLD270115C00370000   |         2,911 |      1,359,437 | GLD261120P00375000   |       11,028 |    36,601,932 |
| GLD      | GLD270115C00375000   |         3,297 |      1,203,405 | GLD261120P00380000   |        7,954 |    30,638,808 |
| GOOG     | GOOG261218C00310000  |         8,165 |      1,714,650 | GOOG270115P00480000  |        1,250 |    24,850,000 |
| GOOG     | GOOG270115C00330000  |         6,287 |      1,194,530 | GOOG261120P00340000  |        1,703 |    10,047,700 |
| GOOG     | GOOG261218C00150000  |            88 |      1,134,936 | GOOG261120P00330000  |          691 |     3,457,073 |
| GOOG     | GOOG270115C00280000  |           662 |      1,024,114 | GOOG261120P00350000  |          475 |     3,289,375 |
| GOOGL    | GOOGL270115C00300000 |         3,585 |      3,011,400 | GOOGL261120P00340000 |        1,913 |    11,038,010 |
| GOOGL    | GOOGL261218C00290000 |         3,602 |      2,946,436 | GOOGL261120P00345000 |        1,641 |    10,111,842 |
| GOOGL    | GOOGL270115C00200000 |           256 |      2,170,880 | GOOGL261120P00355000 |          795 |     5,704,125 |
| GOOGL    | GOOGL270115C00205000 |           228 |      1,838,820 | GOOGL261120P00350000 |          775 |     5,138,250 |
| IBIT     | IBIT261127C00037000  |        51,488 |      2,162,496 | IBIT261120P00039500  |       10,132 |     4,225,044 |
| IBIT     | IBIT261218C00036000  |         5,957 |        947,163 | IBIT270115P00035000  |       14,558 |     3,260,992 |
| IBIT     | IBIT261127C00036000  |         9,559 |        716,925 | IBIT261120P00038000  |       10,672 |     2,934,800 |
| IBIT     | IBIT261130C00035000  |         3,051 |        421,038 | IBIT270115P00030000  |       15,419 |     1,187,263 |
| INTC     | INTC261218C00060000  |        18,287 |      4,498,602 | INTC261127P00055000  |        5,937 |     1,686,108 |
| INTC     | INTC261127C00055000  |        10,745 |      2,696,995 | INTC261204P00065000  |          809 |       938,440 |
| INTC     | INTC261120C00054000  |         6,284 |      1,281,936 | INTC261218P00055000  |        1,936 |       906,048 |
| INTC     | INTC261120C00055000  |         5,864 |        879,600 | INTC261127P00056000  |        2,244 |       733,788 |
| IONQ     | IONQ270115C00030000  |         2,272 |        284,000 | IONQ270115P00050000  |          115 |       303,715 |
| IONQ     | IONQ261204C00025000  |           677 |         81,240 | IONQ261120P00030000  |          422 |       281,896 |
| IREN     | IREN261120C00016000  |        24,222 |      1,017,324 | IREN261120P00034000  |          265 |       497,670 |
| IREN     | IREN261218C00015000  |         4,135 |        922,105 | IREN270115P00017000  |        1,183 |       451,906 |
| IREN     | IREN261218C00008000  |         1,001 |        740,740 | IREN261120P00015000  |        6,907 |       428,234 |
| IREN     | IREN261120C00012000  |         1,430 |        470,470 | IREN261120P00016000  |        3,663 |       421,245 |
| MARA     | MARA261120C00006500  |        10,168 |        294,872 | MARA261218P00014000  |          691 |       518,250 |
| MARA     | MARA270115C00007000  |         3,363 |        275,766 | MARA261231P00007500  |        2,391 |       334,740 |
| MRVL     | MRVL270115C00155000  |         3,055 |      4,383,925 | MRVL261120P00200000  |        4,557 |    25,815,405 |
| MRVL     | MRVL261120C00150000  |         3,531 |      1,091,079 | MRVL261120P00195000  |        3,307 |    16,948,375 |
| MRVL     | MRVL261218C00150000  |           541 |        681,660 | MRVL261120P00210000  |          960 |     6,249,600 |
| MRVL     | MRVL261127C00150000  |         1,017 |        622,404 | MRVL261120P00220000  |          686 |     5,212,228 |
| MSTR     | MSTR261120C00092000  |         3,861 |        965,250 | MSTR261127P00135000  |        1,368 |     6,038,352 |
| MSTR     | MSTR261120C00090000  |         2,655 |        929,250 | MSTR261127P00140000  |        1,199 |     5,902,677 |
| MSTR     | MSTR270115C00100000  |         1,082 |        913,208 | MSTR261127P00145000  |          924 |     5,009,928 |
| MSTR     | MSTR270115C00090000  |           670 |        864,300 | MSTR261120P00100000  |        4,877 |     4,901,385 |
| NFLX     | NFLX270115C00060000  |         3,220 |      1,159,200 | NFLX270115P00060000  |        2,282 |       730,240 |
| NFLX     | NFLX261120C00002500  |           144 |        827,136 | NFLX261218P00060000  |        2,675 |       631,300 |
| NFLX     | NFLX261211C00060000  |         3,828 |        811,536 | NFLX270115P00068000  |          687 |       607,995 |
| NFLX     | NFLX261218C00063000  |         4,473 |        559,125 | NFLX270115P00069000  |          537 |       516,594 |
| NVDA     | NVDA261218C00170000  |        70,153 |     18,099,474 | NVDA261218P00200000  |        9,275 |    45,735,025 |
| NVDA     | NVDA261120C00155000  |        75,374 |     12,888,954 | NVDA261120P00240000  |        4,701 |    41,796,591 |
| NVDA     | NVDA261120C00150000  |        28,742 |     11,209,380 | NVDA261120P00150000  |       95,562 |    27,999,666 |
| NVDA     | NVDA261120C00152500  |        34,933 |      9,327,111 | NVDA261120P00155000  |       37,998 |    21,848,850 |
| NVDX     | NVDX261120C00009000  |           533 |         11,726 | NVDX270115P00019430  |          760 |       828,400 |
| QCOM     | QCOM261204C00165000  |         2,255 |      1,095,930 | QCOM261218P00160000  |          632 |       647,800 |
| QCOM     | QCOM261127C00175000  |         3,718 |        353,210 | QCOM261120P00165000  |          473 |       334,884 |
| QCOM     | QCOM261218C00185000  |         1,562 |        323,334 | QCOM270115P00185000  |          102 |       293,760 |
| QQQ      | QQQ261218C00660000   |        12,103 |     27,836,900 | QQQ261120P00720000   |       11,877 |    71,618,310 |
| QQQ      | QQQ261218C00680000   |        15,860 |     20,459,400 | QQQ261120P00725000   |        9,123 |    62,930,454 |
| QQQ      | QQQ261119C00660000   |        34,670 |     20,212,610 | QQQ261120P00730000   |        6,315 |    44,552,325 |
| QQQ      | QQQ261218C00665000   |         9,646 |     19,436,690 | QQQ261218P00665000   |       17,681 |    41,055,282 |
| RIOT     | RIOT261120C00017000  |        41,487 |      6,223,050 | RIOT261224P00013000  |        9,308 |       335,088 |
| RIOT     | RIOT261120C00016000  |        14,765 |      3,440,245 | RIOT261127P00017000  |        5,042 |       317,646 |
| RIOT     | RIOT261120C00017500  |        24,130 |      2,847,340 | RIOT261218P00013000  |        9,992 |       289,768 |
| RIOT     | RIOT261120C00019000  |        45,234 |      1,854,594 | RIOT261120P00018000  |        1,812 |       103,284 |
| RKLB     | RKLB261218C00055000  |           869 |        384,967 | RKLB261218P00055000  |        1,313 |       761,540 |
| RKLB     | RKLB261127C00057000  |         1,199 |        159,467 | RKLB270115P00047000  |        1,371 |       493,560 |
| RKLB     | RKLB261211C00057000  |           451 |        137,555 | RKLB261120P00055000  |        1,679 |       404,639 |
| RKLB     | RKLB261211C00052000  |           247 |        136,591 | RKLB270115P00100000  |           80 |       363,760 |
| SLV      | SLV270115C00040000   |         4,762 |      1,595,270 | SLV261218P00046000   |        8,171 |     4,673,812 |
| SLV      | SLV270115C00041000   |         3,053 |        857,893 | SLV261218P00047000   |        1,588 |     1,059,196 |
| SLV      | SLV270115C00043000   |         3,317 |        653,449 | SLV270115P00061000   |          512 |     1,047,040 |
| SLV      | SLV270115C00045000   |         4,572 |        612,648 | SLV261218P00040000   |        5,122 |       901,472 |
| SMCI     | SMCI261127C00025000  |         5,876 |        687,492 | SMCI261120P00025000  |        4,131 |       491,589 |
| SMCI     | SMCI261127C00027000  |         5,808 |        272,976 | SMCI261120P00026000  |        2,460 |       467,400 |
| SMCI     | SMCI261120C00025000  |         4,515 |        252,840 | SMCI261127P00034000  |          404 |       385,820 |
| SMCI     | SMCI261218C00025000  |         1,015 |        223,300 | SMCI261127P00032000  |          403 |       304,265 |
| SMH      | SMH270115C00500000   |         5,660 |      9,989,900 | SMH261120P00550000   |        3,041 |    28,889,500 |
| SMH      | SMH261218C00500000   |         3,488 |      3,707,744 | SMH261120P00557500   |        2,250 |    23,062,500 |
| SMH      | SMH270115C00550000   |         5,181 |      3,160,410 | SMH261120P00545000   |          675 |     5,837,400 |
| SMH      | SMH261120C00460000   |         1,473 |      1,487,730 | SMH261120P00555000   |          367 |     3,548,890 |
| SNDK     | SNDK261120C00800000  |         5,339 |     11,345,375 | SNDK261120P01450000  |        1,608 |   110,164,080 |
| SNDK     | SNDK261127C00800000  |         2,629 |     10,823,593 | SNDK261120P01350000  |        1,785 |   102,780,300 |
| SNDK     | SNDK261120C00770000  |         1,849 |      6,534,366 | SNDK261120P01500000  |        1,284 |    94,759,200 |
| SNDK     | SNDK261127C00700000  |           609 |      6,144,201 | SNDK261120P01600000  |          915 |    76,677,000 |
| SPY      | SPY261120C00725000   |        62,615 |     57,104,880 | SPY261127P00727000   |       64,750 |    51,800,000 |
| SPY      | SPY261120C00730000   |        90,903 |     54,178,188 | SPY261120P00730000   |       60,138 |    33,316,452 |
| SPY      | SPY261218C00495000   |         1,227 |     29,500,761 | SPY261218P00730000   |       17,574 |    28,663,194 |
| SPY      | SPY261218C00360000   |           548 |     20,360,392 | SPY261218P00750000   |        9,007 |    23,778,480 |
| TLT      | TLT270115C00082000   |        10,111 |        798,769 | TLT261231P00079000   |       11,394 |       945,702 |
| TLT      | TLT261231C00081000   |         7,117 |        604,945 | TLT261218P00080000   |        5,454 |       594,486 |
| TLT      | TLT261218C00081000   |         7,779 |        560,088 | TLT261130P00081000   |        5,251 |       509,347 |
| TLT      | TLT261130C00078000   |         2,312 |        545,632 | TLT261218P00079000   |        4,151 |       278,117 |
| TSLA     | TSLA261120C00370000  |         8,896 |     15,541,312 | TSLA261120P00390000  |       17,850 |    18,671,100 |
| TSLA     | TSLA261120C00380000  |         9,339 |      8,685,270 | TSLA261120P00380000  |       10,190 |     5,706,400 |
| TSLA     | TSLA270115C00400000  |         3,947 |      8,620,248 | TSLA261120P00385000  |        7,269 |     5,597,130 |
| TSLA     | TSLA261120C00385000  |        12,499 |      7,999,360 | TSLA270115P00380000  |        1,765 |     4,359,550 |
| TSLL     | TSLL261218C00011000  |         4,306 |        284,196 | TSLL261120P00010000  |          729 |        24,057 |
| TSM      | TSM270115C00370000   |         2,675 |      6,072,250 | TSM261120P00470000   |          903 |     9,816,513 |
| TSM      | TSM270115C00400000   |         3,816 |      4,579,200 | TSM261120P00430000   |          981 |     6,740,451 |
| TSM      | TSM261120C00360000   |         1,814 |      1,705,160 | TSM261120P00360000   |        6,858 |     4,711,446 |
| TSM      | TSM261218C00380000   |         1,234 |      1,456,120 | TSM261218P00310000   |        5,285 |     2,605,505 |
| UNH      | UNH261218C00370000   |         3,207 |      2,453,355 | UNH261120P00360000   |        4,330 |     5,187,340 |
| UNH      | UNH261218C00360000   |         1,253 |      1,439,697 | UNH261120P00350000   |        5,647 |     3,704,432 |
| UNH      | UNH261218C00350000   |           798 |      1,324,680 | UNH261120P00405000   |          656 |     3,673,600 |
| UNH      | UNH261120C00350000   |         1,519 |      1,040,515 | UNH261120P00365000   |        2,206 |     3,386,210 |
| WULF     | WULF261218C00013000  |         5,599 |        582,296 | WULF261224P00009500  |        9,583 |       440,818 |
| WULF     | WULF261211C00011500  |         3,047 |        533,225 | WULF261218P00011000  |        1,805 |       166,060 |
| WULF     | WULF261120C00012500  |         8,177 |        261,664 | WULF261218P00010000  |        1,710 |        97,470 |
| XLF      | XLF270115C00034000   |           217 |        497,364 | XLF270115P00056000   |       18,140 |     2,575,880 |
| XLF      | XLF261218C00038000   |           174 |        327,468 | XLF261120P00057000   |       18,861 |     1,320,270 |
| XLF      | XLF261218C00058000   |         4,620 |        286,440 | XLF261218P00055000   |       13,475 |       956,725 |
| XLF      | XLF270115C00044000   |           217 |        283,619 | XLF261120P00056000   |       37,555 |       938,875 |
| XLU      | XLU261120C00043000   |        14,588 |      1,035,748 | XLU270115P00043000   |        5,893 |       518,584 |
| XLU      | XLU261218C00044500   |        16,130 |        741,980 | XLU261218P00042000   |        5,051 |       141,428 |
| XLU      | XLU261218C00045000   |        15,695 |        486,545 | XLU261218P00041000   |       10,008 |       140,112 |
| XLU      | XLU261218C00044000   |         4,207 |        269,248 | XLU261218P00043000   |        2,641 |       139,973 |
| ^VIX     | VIX261216C00010000   |         3,723 |      4,143,699 | VIX261216P00021000   |       36,195 |     7,709,535 |
| ^VIX     | VIX261216C00021500   |        14,364 |      3,907,008 | VIX261216P00022000   |       26,934 |     7,299,114 |
| ^VIX     | VIX261216C00033000   |        29,724 |      3,239,916 | VIX261216P00021500   |       19,173 |     4,620,693 |
| ^VIX     | VIX261216C00022000   |         7,612 |      2,055,240 | VIX261216P00020000   |       23,857 |     3,578,550 |

## T3 — Top 3 OTM Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261120C00355000  |        13,896 |      2,806,992 | AAPL261218P00350000  |        6,047 |     5,049,245 |
| AAPL     | AAPL261120C00357500  |        14,327 |      1,719,240 | AAPL261120P00350000  |       21,899 |     4,861,578 |
| AAPL     | AAPL270115C00360000  |         1,590 |      1,694,940 | AAPL261218P00345000  |        2,236 |     1,431,040 |
| AMZN     | AMZN261120C00270000  |        33,100 |     10,360,300 | AMZN261120P00265000  |        5,525 |     1,624,350 |
| AMZN     | AMZN261218C00280000  |        13,273 |      8,189,441 | AMZN261120P00262500  |        6,765 |     1,386,825 |
| AMZN     | AMZN270115C00275000  |         6,545 |      7,991,445 | AMZN270115P00250000  |        1,857 |     1,374,180 |
| ARM      | ARM261120C00185000   |         1,100 |        533,500 | ARM261218P00160000   |          305 |       227,225 |
| AVGO     | AVGO261120C00360000  |         6,840 |      3,796,200 | AVGO261218P00350000  |          905 |     2,027,200 |
| AVGO     | AVGO261218C00370000  |         1,451 |      2,640,820 | AVGO261218P00340000  |          774 |     1,395,522 |
| AVGO     | AVGO270115C00360000  |           941 |      2,620,685 | AVGO261120P00350000  |        1,987 |     1,283,602 |
| BABA     | BABA261218C00090000  |         3,576 |        986,976 | BABA261218P00080000  |        2,244 |       648,516 |
| BABA     | BABA270115C00090000  |         2,273 |        975,117 | BABA261218P00075000  |        4,314 |       629,844 |
| BABA     | BABA261120C00085000  |         2,855 |        708,040 | BABA261120P00080000  |        5,362 |       563,010 |
| CIFR     | CIFR261218C00007000  |         4,258 |        340,640 | CIFR261120P00006500  |        1,028 |        31,868 |
| CLSK     | CLSK261127C00006500  |        10,661 |        362,474 | CLSK261218P00006000  |        1,635 |       116,085 |
| COIN     | COIN261127C00120000  |         2,604 |        463,512 | COIN261218P00110000  |        1,802 |     1,594,770 |
| COIN     | COIN261120C00115000  |         2,271 |        333,837 | COIN261120P00110000  |        3,357 |       973,530 |
| COIN     | COIN261218C00130000  |           872 |        261,600 | COIN261127P00110000  |          976 |       475,312 |
| CRWV     | CRWV261218C00050000  |         4,376 |      2,034,840 | CRWV270115P00040000  |        5,560 |     2,085,000 |
| CRWV     | CRWV270115C00060000  |         5,767 |      1,891,576 | CRWV261218P00040000  |        4,285 |     1,028,400 |
| CRWV     | CRWV261127C00048000  |         4,910 |      1,522,100 | CRWV261127P00047000  |        3,602 |       986,948 |
| GLD      | GLD270115C00355000   |         3,762 |      3,254,130 | GLD261218P00340000   |        7,020 |     6,247,800 |
| GLD      | GLD270115C00345000   |         2,433 |      3,153,168 | GLD261218P00335000   |        3,304 |     2,253,328 |
| GLD      | GLD270115C00370000   |         2,911 |      1,359,437 | GLD261218P00330000   |        3,123 |     1,645,821 |
| GOOG     | GOOG261218C00310000  |         8,165 |      1,714,650 | GOOG270115P00265000  |          898 |       736,360 |
| GOOG     | GOOG270115C00330000  |         6,287 |      1,194,530 | GOOG261218P00270000  |          667 |       456,895 |
| GOOG     | GOOG270115C00280000  |           662 |      1,024,114 | GOOG270115P00275000  |          341 |       410,905 |
| GOOGL    | GOOGL270115C00300000 |         3,585 |      3,011,400 | GOOGL261120P00280000 |        3,924 |     1,177,200 |
| GOOGL    | GOOGL261218C00290000 |         3,602 |      2,946,436 | GOOGL261218P00270000 |        1,305 |       809,100 |
| GOOGL    | GOOGL270115C00290000 |         1,238 |      1,535,120 | GOOGL261218P00280000 |          781 |       773,971 |
| IBIT     | IBIT261127C00037000  |        51,488 |      2,162,496 | IBIT270115P00035000  |       14,558 |     3,260,992 |
| IBIT     | IBIT261218C00036000  |         5,957 |        947,163 | IBIT270115P00030000  |       15,419 |     1,187,263 |
| IBIT     | IBIT261127C00036000  |         9,559 |        716,925 | IBIT261120P00035000  |       22,598 |     1,084,704 |
| INTC     | INTC261218C00060000  |        18,287 |      4,498,602 | INTC261120P00054000  |        5,018 |       682,448 |
| INTC     | INTC261127C00055000  |        10,745 |      2,696,995 | INTC261127P00054000  |        2,818 |       665,048 |
| INTC     | INTC261120C00055000  |         5,864 |        879,600 | INTC261120P00053000  |        6,775 |       643,625 |
| IONQ     | IONQ270115C00030000  |         2,272 |        284,000 | IONQ261204P00023000  |          634 |        98,270 |
| IREN     | IREN261120C00016000  |        24,222 |      1,017,324 | IREN261120P00015000  |        6,907 |       428,234 |
| IREN     | IREN261120C00016500  |        14,457 |        404,796 | IREN261127P00015000  |        2,808 |       292,032 |
| IREN     | IREN261218C00020000  |         4,044 |        266,904 | IREN261120P00014000  |        6,313 |       189,390 |
| MARA     | MARA270115C00007000  |         3,363 |        275,766 | MARA261120P00006500  |        9,356 |       215,188 |
| MRVL     | MRVL270115C00155000  |         3,055 |      4,383,925 | MRVL261218P00140000  |        1,092 |     1,310,400 |
| MRVL     | MRVL261120C00150000  |         3,531 |      1,091,079 | MRVL261218P00145000  |          706 |       998,990 |
| MRVL     | MRVL261218C00150000  |           541 |        681,660 | MRVL261218P00130000  |        1,110 |       910,200 |
| MSTR     | MSTR261120C00092000  |         3,861 |        965,250 | MSTR261120P00090000  |       14,772 |     4,579,320 |
| MSTR     | MSTR270115C00100000  |         1,082 |        913,208 | MSTR270115P00075000  |        7,520 |     4,339,040 |
| MSTR     | MSTR261218C00105000  |         2,066 |        816,070 | MSTR270115P00090000  |        1,815 |     2,123,550 |
| NFLX     | NFLX270115C00060000  |         3,220 |      1,159,200 | NFLX270115P00058000  |        1,539 |       377,055 |
| NFLX     | NFLX261211C00060000  |         3,828 |        811,536 | NFLX270115P00057000  |        1,047 |       215,682 |
| NFLX     | NFLX261218C00063000  |         4,473 |        559,125 | NFLX261120P00059000  |        5,349 |       197,913 |
| NVDA     | NVDA261218C00170000  |        70,153 |     18,099,474 | NVDA261120P00150000  |       95,562 |    27,999,666 |
| NVDA     | NVDA261120C00155000  |        75,374 |     12,888,954 | NVDA270115P00150000  |       15,262 |    16,406,650 |
| NVDA     | NVDA261120C00152500  |        34,933 |      9,327,111 | NVDA261218P00150000  |       12,335 |    10,213,380 |
| QCOM     | QCOM261204C00165000  |         2,255 |      1,095,930 | QCOM270115P00155000  |          153 |       157,590 |
| QCOM     | QCOM261127C00175000  |         3,718 |        353,210 | QCOM261218P00155000  |          154 |       127,050 |
| QCOM     | QCOM261218C00185000  |         1,562 |        323,334 | QCOM261218P00145000  |          232 |       102,080 |
| QQQ      | QQQ261218C00660000   |        12,103 |     27,836,900 | QQQ261218P00640000   |       18,966 |    26,836,890 |
| QQQ      | QQQ261218C00680000   |        15,860 |     20,459,400 | QQQ261120P00655000   |       20,880 |    13,237,920 |
| QQQ      | QQQ261119C00660000   |        34,670 |     20,212,610 | QQQ261218P00650000   |        6,912 |    11,943,936 |
| RIOT     | RIOT261120C00019000  |        45,234 |      1,854,594 | RIOT261224P00013000  |        9,308 |       335,088 |
| RIOT     | RIOT261127C00020500  |        21,013 |        714,442 | RIOT261127P00017000  |        5,042 |       317,646 |
| RIOT     | RIOT270115C00020000  |         1,818 |        370,872 | RIOT261218P00013000  |        9,992 |       289,768 |
| RKLB     | RKLB261218C00055000  |           869 |        384,967 | RKLB270115P00047000  |        1,371 |       493,560 |
| RKLB     | RKLB261127C00057000  |         1,199 |        159,467 | RKLB261218P00047000  |        1,351 |       330,995 |
| SLV      | SLV270115C00041000   |         3,053 |        857,893 | SLV261218P00040000   |        5,122 |       901,472 |
| SLV      | SLV270115C00043000   |         3,317 |        653,449 | SLV261218P00039000   |        3,531 |       476,685 |
| SLV      | SLV270115C00045000   |         4,572 |        612,648 | SLV261120P00040000   |       10,333 |       392,654 |
| SMCI     | SMCI261127C00025000  |         5,876 |        687,492 | SMCI261218P00024000  |          703 |       151,848 |
| SMCI     | SMCI261127C00027000  |         5,808 |        272,976 | SMCI261120P00024000  |        2,233 |       145,145 |
| SMCI     | SMCI261120C00025000  |         4,515 |        252,840 | SMCI261218P00023000  |          456 |        79,800 |
| SMH      | SMH270115C00500000   |         5,660 |      9,989,900 | SMH270115P00450000   |          976 |     2,976,800 |
| SMH      | SMH261218C00500000   |         3,488 |      3,707,744 | SMH261218P00450000   |        1,267 |     2,850,750 |
| SMH      | SMH270115C00550000   |         5,181 |      3,160,410 | SMH261218P00445000   |        1,174 |     2,324,520 |
| SNDK     | SNDK261120C00800000  |         5,339 |     11,345,375 | SNDK261120P00750000  |        3,390 |     7,254,600 |
| SNDK     | SNDK261127C00800000  |         2,629 |     10,823,593 | SNDK261120P00770000  |        2,264 |     6,610,880 |
| SNDK     | SNDK261120C00780000  |         1,298 |      3,927,748 | SNDK261218P00700000  |          847 |     4,482,324 |
| SPY      | SPY261127C00733000   |        16,061 |     13,619,728 | SPY261127P00727000   |       64,750 |    51,800,000 |
| SPY      | SPY261119C00731000   |        33,237 |     12,430,638 | SPY261120P00730000   |       60,138 |    33,316,452 |
| SPY      | SPY261218C00731000   |         6,722 |     11,561,840 | SPY261218P00730000   |       17,574 |    28,663,194 |
| TLT      | TLT270115C00082000   |        10,111 |        798,769 | TLT261231P00079000   |       11,394 |       945,702 |
| TLT      | TLT261231C00081000   |         7,117 |        604,945 | TLT261218P00080000   |        5,454 |       594,486 |
| TLT      | TLT261218C00081000   |         7,779 |        560,088 | TLT261218P00079000   |        4,151 |       278,117 |
| TSLA     | TSLA270115C00400000  |         3,947 |      8,620,248 | TSLA261120P00380000  |       10,190 |     5,706,400 |
| TSLA     | TSLA261120C00385000  |        12,499 |      7,999,360 | TSLA270115P00380000  |        1,765 |     4,359,550 |
| TSLA     | TSLA261120C00390000  |        12,151 |      5,322,138 | TSLA261120P00382500  |        6,186 |     4,070,388 |
| TSLL     | TSLL261218C00011000  |         4,306 |        284,196 | TSLL261120P00009500  |        1,459 |        21,885 |
| TSM      | TSM270115C00370000   |         2,675 |      6,072,250 | TSM261120P00360000   |        6,858 |     4,711,446 |
| TSM      | TSM270115C00400000   |         3,816 |      4,579,200 | TSM261218P00310000   |        5,285 |     2,605,505 |
| TSM      | TSM261218C00380000   |         1,234 |      1,456,120 | TSM261218P00360000   |        1,052 |     2,001,956 |
| UNH      | UNH261218C00370000   |         3,207 |      2,453,355 | UNH261120P00340000   |        6,939 |     2,123,334 |
| UNH      | UNH261218C00360000   |         1,253 |      1,439,697 | UNH261218P00340000   |        1,271 |     1,569,685 |
| UNH      | UNH261218C00350000   |           798 |      1,324,680 | UNH261120P00345000   |        2,969 |     1,350,895 |
| WULF     | WULF261218C00013000  |         5,599 |        582,296 | WULF261224P00009500  |        9,583 |       440,818 |
| WULF     | WULF261120C00012500  |         8,177 |        261,664 | WULF261218P00011000  |        1,805 |       166,060 |
| XLF      | XLF261218C00058000   |         4,620 |        286,440 | XLF270115P00056000   |       18,140 |     2,575,880 |
| XLF      | XLF261218C00057000   |         1,760 |        186,560 | XLF261218P00055000   |       13,475 |       956,725 |
| XLF      | XLF261218C00059000   |         1,758 |         56,256 | XLF261120P00056000   |       37,555 |       938,875 |
| XLU      | XLU261218C00044500   |        16,130 |        741,980 | XLU270115P00043000   |        5,893 |       518,584 |
| XLU      | XLU261218C00045000   |        15,695 |        486,545 | XLU261218P00042000   |        5,051 |       141,428 |
| XLU      | XLU261218C00044000   |         4,207 |        269,248 | XLU261218P00041000   |       10,008 |       140,112 |
| ^VIX     | VIX261216C00033000   |        29,724 |      3,239,916 | VIX261216P00021000   |       36,195 |     7,709,535 |
| ^VIX     | VIX261216C00025000   |         4,649 |        897,257 | VIX261216P00022000   |       26,934 |     7,299,114 |
| ^VIX     | VIX261216C00050000   |        12,883 |        682,799 | VIX261216P00021500   |       19,173 |     4,620,693 |

*premium = volume × lastPrice × 100 · OTM = calls strike>spot, puts strike<spot · T4 uses the cleaned chain: ≥2 DTE, OTM only, leveraged ETFs folded into their underlying, ^VIX ratio inverted · Net Signed Premium = bought calls/sold puts minus sold calls/bought puts, side from lastPrice vs bid/ask (prints outside the closing quote are not signed) · generated by options-flow-pipeline*

---

**Data quality:** requested: 52 · fetched: 52 · failed: 0 · gated: 10 · stale volume: 21,636 contracts (27% of premium) dropped

_Signal check (next-day rank correlation, last 20 sessions): composite IC +0.049 (t +0.9, n=20) · flow_pct IC -0.071 (t -1.6, n=20) · trend_pct IC +0.124 (t +1.9, n=20)_

_Signal check, next 5 sessions (rank correlation, last 20 resolved sessions; windows overlap, so t is overstated): composite IC -0.010 (t -0.2, n=20) · flow_pct IC -0.129 (t -3.8, n=20) · trend_pct IC +0.095 (t +2.2, n=20)_