# Options Flow Report (v1.3) — 2026-11-25

**Run stats:** 52/52 tickers fetched · 0 failed · 57,623 contracts

## Market Regime

**risk-off · backwardation (VIX/VIX3M=1.08, DoD +0.04) · negative gamma (moves amplified) · high vol · choppy/rangebound — momentum tilted**

`Vol: HIGH · Trend: CHOP · Risk: RISK_OFF · Gamma: NEGATIVE · SPY GEX: $-7,710M`

_Pipeline knobs: mom×0.85 · conviction≥0.88_

## Master Scoreboard (all tickers by composite)

| Rank   | Ticker   | Composite   | Trend%   | Mom%   | Flow%   | Rot%   | Conviction   | ΔRank   |
|:-------|:---------|:------------|:---------|:-------|:--------|:-------|:-------------|:--------|
| 1      | XLV      | 100.0       | 100      | 86     | N/A     | 96     | NEUTRAL      | 0       |
| 2      | XLE      | 98.4        | 98       | 91     | N/A     | 89     | CONFIRMED    | 0       |
| 3      | XLP      | 96.7        | 97       | 85     | N/A     | 93     | NEUTRAL      | 0       |
| 4      | XLB      | 91.8        | 92       | 79     | N/A     | 83     | NEUTRAL      | +1      |
| 5      | XLRE     | 90.2        | 90       | 70     | N/A     | 87     | NEUTRAL      | +1      |
| 6      | BIL      | 86.9        | 87       | 70     | N/A     | 85     | NEUTRAL      | -2      |
| 7      | SNDK     | 85.2        | 85       | 76     | N/A     | 73     | NEUTRAL      | +2      |
| 8      | XLY      | 83.6        | 84       | 65     | N/A     | 84     | NEUTRAL      | -1      |
| 9      | AI       | 79.6        | 61       | 57     | 96      | 68     | NEUTRAL      | -1      |
| 10     | AMZN     | 78.7        | 79       | 60     | 79      | 80     | NEUTRAL      | +7      |
| 11     | QCOM     | 74.3        | 77       | 57     | 72      | 82     | NEUTRAL      | +11     |
| 12     | XLK      | 73.8        | 74       | 76     | N/A     | 59     | NEUTRAL      | -2      |
| 13     | TSM      | 72.3        | 70       | 77     | 74      | 55     | NEUTRAL      | +30     |
| 14     | IWM      | 72.1        | 72       | 67     | N/A     | 66     | NEUTRAL      | -1      |
| 15     | RIOT     | 70.6        | 48       | 44     | 90      | 51     | NEUTRAL      | -1      |
| 16     | TLT      | 67.9        | 69       | 56     | 67      | 73     | NEUTRAL      | +24     |
| 17     | SMCI     | 65.4        | 39       | 55     | 88      | 31     | CONFLICT     | +2      |
| 18     | XLI      | 63.9        | 64       | 64     | N/A     | 63     | NEUTRAL      | +3      |
| 19     | UNH      | 63.4        | 89       | 80     | 42      | 75     | NEUTRAL      | -8      |
| 20     | NVDA     | 62.8        | 51       | 69     | 73      | 38     | NEUTRAL      | +14     |
| 21     | LQD      | 62.3        | 62       | 52     | N/A     | 74     | NEUTRAL      | +2      |
| 22     | HYG      | 59.0        | 59       | 51     | N/A     | 73     | NEUTRAL      | +2      |
| 23     | EOSE     | 56.3        | 5        | 8      | 100     | 2      | CONFLICT     | +38     |
| 24     | CPER     | 55.7        | 56       | 64     | N/A     | 54     | NEUTRAL      | +6      |
| 25     | HIVE     | 55.0        | 15       | 18     | 89      | 14     | CONFLICT     | -5      |
| 26     | GOOGL    | 54.5        | 38       | 35     | 69      | 46     | NEUTRAL      | +6      |
| 27     | SPY      | 54.5        | 82       | 70     | 31      | 78     | CONFLICT     | +6      |
| 28     | OPEN     | 54.4        | 3        | 3      | 98      | 6      | CONFLICT     | +21     |
| 29     | XLC      | 52.5        | 52       | 47     | N/A     | 61     | NEUTRAL      | +6      |
| 30     | CLSK     | 52.2        | 16       | 24     | 83      | 13     | CONFLICT     | -3      |
| 31     | AAPL     | 50.6        | 95       | 77     | 13      | 98     | CONFLICT     | -15     |
| 32     | TSLA     | 50.2        | 66       | 56     | 37      | 72     | NEUTRAL      | -20     |
| 33     | RKLB     | 49.9        | 43       | 51     | 56      | 36     | NEUTRAL      | +9      |
| 34     | MRVL     | 48.3        | 75       | 77     | 25      | 59     | CONFLICT     | -8      |
| 35     | SLV      | 48.3        | 31       | 36     | 63      | 29     | NEUTRAL      | +1      |
| 36     | INTC     | 48.0        | 54       | 69     | 43      | 44     | NEUTRAL      | -21     |
| 37     | QQQ      | 47.8        | 67       | 68     | 31      | 61     | CONFLICT     | +1      |
| 38     | MSTR     | 46.1        | 28       | 34     | 62      | 25     | NEUTRAL      | +16     |
| 39     | COIN     | 46.0        | 23       | 28     | 66      | 23     | NEUTRAL      | +6      |
| 40     | OKLO     | 45.4        | 10       | 8      | 76      | 12     | CONFLICT     | -3      |
| 41     | MARA     | 44.0        | 18       | 22     | 66      | 17     | NEUTRAL      | -2      |
| 42     | XLU      | 44.0        | 80       | 62     | 13      | 80     | CONFLICT     | +9      |
| 43     | GOOG     | 43.6        | 36       | 34     | 50      | 46     | NEUTRAL      | +1      |
| 44     | XLF      | 42.9        | 93       | 76     | 0       | 86     | CONFLICT     | -3      |
| 45     | NFLX     | 41.6        | 25       | 16     | 56      | 36     | NEUTRAL      | -14     |
| 46     | GLD      | 41.6        | 34       | 35     | 48      | 43     | NEUTRAL      | +12     |
| 47     | WULF     | 40.2        | 33       | 37     | 47      | 29     | NEUTRAL      | -22     |
| 48     | BABA     | 39.7        | 30       | 24     | 48      | 35     | NEUTRAL      | -2      |
| 49     | SMH      | 38.1        | 57       | 72     | 22      | 51     | CONFLICT     | +3      |
| 50     | IBIT     | 37.1        | 46       | 49     | 30      | 41     | NEUTRAL      | +3      |
| 51     | IREN     | 36.7        | 8        | 17     | 61      | 2      | NEUTRAL      | +6      |
| 52     | AVGO     | 36.6        | 41       | 38     | 33      | 49     | NEUTRAL      | -5      |
| 53     | ARM      | 31.7        | 49       | 62     | 17      | 44     | NEUTRAL      | -5      |
| 54     | ETHA     | 29.6        | 44       | 50     | 17      | 37     | NEUTRAL      | +2      |
| 55     | RGTI     | 28.4        | 13       | 13     | 41      | 14     | NEUTRAL      | -5      |
| 56     | HIMS     | 25.8        | 26       | 35     | 25      | 23     | NEUTRAL      | -38     |
| 57     | IONQ     | 24.2        | 20       | 24     | 28      | 22     | NEUTRAL      | -2      |
| 58     | QBTS     | 24.2        | 7        | 9      | 39      | 9      | NEUTRAL      | +1      |
| 59     | CIFR     | 24.1        | 11       | 17     | 35      | 5      | NEUTRAL      | -30     |
| 60     | CRWV     | 19.4        | 21       | 33     | 18      | 18     | NEUTRAL      | 0       |
| 61     | SMR      | 4.1         | 2        | 6      | 6       | 2      | NEUTRAL      | -33     |
| N/A    | AAPX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDU     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | TSLL     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^GSPC    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^SKEW    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX     | N/A         | N/A      | N/A    | 70      | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX3M   | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VVIX    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |

## Sector Rotation / Relative Strength (top 15)

| Ticker   |   RS Rating |   Rel Str 63d | RS New-High   | Dual-Mom   |
|:---------|------------:|--------------:|:--------------|:-----------|
| AAPL     |          99 |          19.9 | No            | above cash |
| XLV      |          97 |          14.3 | No            | above cash |
| SNDK     |          96 |         -45.9 | No            | above cash |
| XLE      |          94 |           5.2 | No            | above cash |
| XLP      |          92 |          16   | No            | above cash |
| XLF      |          91 |           4.8 | No            | above cash |
| XLRE     |          89 |           5.9 | No            | above cash |
| XLB      |          88 |           3.5 | No            | above cash |
| BIL      |          86 |           7.8 | No            | below cash |
| AMZN     |          84 |           2.2 | No            | above cash |
| XLY      |          83 |           8.4 | No            | below cash |
| UNH      |          81 |          -5   | No            | above cash |
| QCOM     |          79 |           9.7 | No            | above cash |
| XLU      |          78 |           8.6 | No            | below cash |
| SPY      |          76 |           0   | Yes           | above cash |

## Option Skew — Extremes (top/bottom 8)

_Board-wide: protection demand rising across the board (typical name z +1.3 vs its own norm; 21 of 29 names at z +1 or more, 1 at −1 or less). Hedging arrows are measured net of this move._

| Ticker   | Group    | Tilt        |   Skew25 (vol pts) | 90-110   |   ATM IV % |   Skew/IV | Hedging            |    z | Flow        | Positioning   |
|:---------|:---------|:------------|-------------------:|:---------|-----------:|----------:|:-------------------|-----:|:------------|:--------------|
| SPY      | top 8    | put-skewed  |                9.7 | 17.8     |       23.1 |      0.42 | steady →           | -0.1 | Neutral -12 |               |
| QQQ      | top 8    | put-skewed  |               10.7 | 15.7     |       34.2 |      0.31 | steady →           | -0.5 | Neutral -5  |               |
| AAPL     | top 8    | put-skewed  |                7.5 | 13.7     |       24.4 |      0.31 | steady →           |  0.9 | Neutral +6  |               |
| TSM      | top 8    | put-skewed  |               11.8 | 10.7     |       58.9 |      0.2  | steady →           |  0.1 | Neutral -4  |               |
| GOOGL    | top 8    | put-skewed  |                7.7 | 9.7      |       40.5 |      0.19 | steady →           |  0.2 | Neutral -1  |               |
| AMZN     | top 8    | put-skewed  |                7.3 | 8.6      |       40.3 |      0.18 | steady →           | -0.3 | Neutral +5  |               |
| IREN     | top 8    | put-skewed  |               23.9 | 10.5     |      134.1 |      0.18 | steady →           |  0.5 | Neutral -14 |               |
| AVGO     | top 8    | put-skewed  |               12.5 | 11.7     |       73   |      0.17 | steady →           |  0   | Neutral -10 |               |
| TLT      | bottom 8 | call-skewed |               -1.1 | N/A      |       11.7 |     -0.1  | hedging easing ↓   | -3.5 | Bull +30    | speculative   |
| BABA     | bottom 8 | put-skewed  |                4.7 | 5.5      |       47.1 |      0.1  | steady →           |  0.3 | Neutral -8  |               |
| NVDA     | bottom 8 | put-skewed  |                7.5 | 6.0      |       70.4 |      0.11 | hedging easing ↓   | -1.7 | Neutral -5  |               |
| OKLO     | bottom 8 | put-skewed  |               10.7 | 8.0      |      101.1 |      0.11 | hedging building ↑ |  1.5 | Neutral -7  |               |
| MARA     | bottom 8 | put-skewed  |               12.1 | 5.1      |      111.8 |      0.11 | steady →           | -0.4 | Neutral +3  |               |
| COIN     | bottom 8 | put-skewed  |                8.8 | 8.1      |       79.4 |      0.11 | steady →           | -0.1 | Neutral +0  |               |
| ETHA     | bottom 8 | put-skewed  |                8.4 | 7.7      |       66.1 |      0.13 | steady →           |  0.1 | Neutral -9  |               |
| INTC     | bottom 8 | put-skewed  |               10.8 | 8.2      |       84.9 |      0.13 | steady →           | -0.4 | Neutral +8  |               |

_29 of 52 tickers had a fittable smile. Skew25 = how much more an out-of-the-money put costs than the matching out-of-the-money call, in vol points, at a constant 30-day tenor, re-derived from bid/ask mids (Yahoo's own IV field is not used). Positive = puts richer, the normal state — so read the *ranking*, not the level. Tilt is by sign: call-skewed = Skew/IV below 0; least put-skewed = 0 to 0.02; put-skewed above. Hedging = tonight's Skew/IV against the name's own previous 20 sessions (z = standard deviations from that average), net of the typical name's move tonight (the Board-wide line above): building when z is at least +1, easing at −1 or below, else steady; n/a until 10 prior sessions exist. It describes protection demand, not a price forecast._

## Mega-Cap Tech Skew

| Ticker   |   Skew25 (vol pts) |   90-110 |   ATM IV % |   Skew/IV | Rank     | Read           | Hedging          |    z | Flow        | Positioning   |
|:---------|-------------------:|---------:|-----------:|----------:|:---------|:---------------|:-----------------|-----:|:------------|:--------------|
| NVDA     |                7.5 |      6   |       70.4 |      0.11 | 27 of 29 | put-skewed     | hedging easing ↓ | -1.7 | Neutral -5  |               |
| AAPL     |                7.5 |     13.7 |       24.4 |      0.31 | 3 of 29  | steep put skew | steady →         |  0.9 | Neutral +6  |               |
| AMZN     |                7.3 |      8.6 |       40.3 |      0.18 | 6 of 29  | steep put skew | steady →         | -0.3 | Neutral +5  |               |
| GOOGL    |                7.7 |      9.7 |       40.5 |      0.19 | 5 of 29  | steep put skew | steady →         |  0.2 | Neutral -1  |               |
| TSLA     |                8.8 |      8.7 |       55.2 |      0.16 | 13 of 29 | put-skewed     | steady →         | -0.8 | Neutral +1  |               |
| AVGO     |               12.5 |     11.7 |       73   |      0.17 | 8 of 29  | steep put skew | steady →         |  0   | Neutral -10 |               |

_Mega-cap tech: 6 of 6 fitted · median Skew/IV 0.18 vs 0.14 for the other names · richer downside protection than the rest of the board · steepest: AAPL, AMZN, GOOGL, AVGO · flattest: NVDA._

_Flow = premium-weighted flow score: 100 × (bought calls + sold puts − sold calls − bought puts) ÷ total out-of-the-money premium, sides estimated from the last trade against bid/ask (a last trade outside the closing quote is left unsigned); Bull at +20 or more, Bear at −20 or less. Positioning: defensive = hedging building with Bear flow; speculative = hedging easing with Bull flow; blank otherwise. Positioning describes what is being hedged and flowed tonight. It is not a price forecast._

## Stretch & Reversal Watch (experimental)

| Watch             | Tonight                                                                           | Backtest (before live)                                       | Live since 2026-11-06                      |
|:------------------|:----------------------------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------|
| hedging unwinding | TLT (z -3.5), NVDA (z -1.7)                                                       | 194 flags · +1.6% vs avg name · 59% beat it                  | 7 flags · -1.9% vs avg name · 43% beat it  |
| stretched up      | none                                                                              | 595 flags · -1.5% vs avg name · 41% beat it                  | 65 flags · -2.1% vs avg name · 46% beat it |
| washed out        | none                                                                              | 118 flags · -0.1% vs avg name · 57% beat it (no edge so far) | 17 flags · +2.0% vs avg name · 65% beat it |
| puts closing      | AAPL (98% puts), SPY (95% puts), NVDA (92% puts), CRWV (91% puts), SMH (91% puts) | 819 flags · +0.7% vs avg name · 55% beat it (to 2026-11-16)  | none resolved yet (counts from 2026-11-16) |

_Experimental, not proven. Hedging unwinding = tonight's Skew/IV at z -1.5 or lower against the name's own norm, net of the board (as the Hedging column): protection being sold off. Stretched up = price up 5% or more over the last 5 sessions. Washed out = down 5% or more with hedging at z +2 or more on its own norm. Puts closing = the fifth of names where puts made up most of the out-of-the-money positions closed in the previous session (volume matched against the drop in open interest): protection taken off. The record columns score each past flag 5 sessions later against the average name that night (prices from the option chains' implied forwards). The backtest is in-sample: the thresholds were picked on that same history, so it flatters the flags; the live column counts only flags raised since this block was added and is the one that matters. If the live record does not hold up, the block goes. Not a price forecast._

---

# Flow Detail

## T4 — OTM Flow Summary (ranked by OTM Call/Put premium ratio)

|   Rank | Ticker   |   Premium Ratio |   Premium Ratio All |   Total Call Premium |   Total Put Premium |   Net Signed Premium |   Close Price | 1-Day Return   | 1-Week Return   | % Close to MA20   | % Close to MA50   | % Close to High   | % Close to Low   |   52 Week High |   52 Week Low |   MA20 |   MA50 |
|-------:|:---------|----------------:|--------------------:|---------------------:|--------------------:|---------------------:|--------------:|:---------------|:----------------|:------------------|:------------------|:------------------|:-----------------|---------------:|--------------:|-------:|-------:|
|      1 | RIOT     |            3.55 |                4.29 |            6,149,919 |           1,732,805 |              234,467 |         16.65 | 1.90%          | -2.40%          | 2.44%             | -4.23%            | -45.09%           | 44.78%           |          30.32 |         11.5  |  16.25 |  17.38 |
|      2 | SMCI     |            3.33 |                8.85 |            6,849,630 |           2,058,780 |              230,052 |         23.31 | 3.05%          | -6.87%          | -14.43%           | -31.88%           | -54.65%           | 19.66%           |          51.4  |         19.48 |  27.24 |  34.22 |
|      3 | QCOM     |            2.99 |                4.03 |            5,913,944 |           1,978,175 |             -741,993 |        168.66 | 2.24%          | 0.08%           | 0.72%             | -4.30%            | -35.11%           | 38.26%           |         259.92 |        121.99 | 167.46 | 176.23 |
|      4 | AMZN     |            2.79 |                3.18 |          102,375,492 |          36,640,630 |            6,259,060 |        244.43 | -3.12%         | -5.17%          | -4.96%            | -4.19%            | -14.89%           | 24.71%           |         287.2  |        196    | 257.19 | 255.12 |
|      5 | TSM      |            2.52 |                3.62 |          123,907,587 |          49,213,833 |           -7,499,083 |        342.34 | -1.96%         | -8.33%          | -9.79%            | -18.15%           | -29.77%           | 24.45%           |         487.47 |        275.08 | 379.5  | 418.26 |
|      6 | NVDA     |            2.41 |                1.55 |          417,947,390 |         173,686,089 |          -31,959,550 |        149.3  | -3.91%         | -4.38%          | -13.44%           | -26.69%           | -38.65%           | 19.92%           |         243.37 |        124.5  | 172.48 | 203.65 |
|      7 | TLT      |            2.27 |                3.61 |            9,315,982 |           4,101,576 |            3,997,526 |         82.24 | 0.92%          | 3.60%           | 1.47%             | 2.63%             | -9.49%            | 7.60%            |          90.86 |         76.43 |  81.05 |  80.13 |
|      8 | ^VIX     |            2.25 |                0.62 |           23,998,171 |          54,024,500 |           13,933,960 |         28.29 | 7.32%          | 23.48%          | 22.35%            | 48.74%            | -29.33%           | 111.43%          |          40.03 |         13.38 |  23.12 |  19.02 |
|      9 | GOOGL    |            2.04 |                0.09 |           39,231,823 |          19,264,773 |             -335,858 |        273.1  | -2.13%         | -3.74%          | -3.51%            | -14.18%           | -33.16%           | 3.95%            |         408.61 |        262.73 | 283.05 | 318.24 |
|     10 | IREN     |            2    |                0.91 |            7,638,648 |           3,811,791 |           -1,550,518 |         12.85 | -0.77%         | -21.60%         | -30.88%           | -56.13%           | -81.83%           | 13.29%           |          70.71 |         11.34 |  18.59 |  29.29 |
|     11 | NFLX     |            1.95 |                0.03 |            4,738,751 |           2,429,950 |              500,804 |         59.41 | 0.92%          | -2.21%          | -3.68%            | -10.31%           | -45.86%           | 5.04%            |         109.73 |         56.56 |  61.68 |  66.24 |
|     12 | COIN     |            1.85 |                0.05 |           13,266,872 |           7,157,187 |              -43,022 |        103.72 | 1.34%          | -13.45%         | -18.47%           | -34.98%           | -63.57%           | 9.32%            |         284.74 |         94.88 | 127.22 | 159.53 |
|     13 | SLV      |            1.71 |                0.32 |           10,681,282 |           6,237,811 |             -505,734 |         37.1  | 0.71%          | -12.48%         | -14.61%           | -25.56%           | -66.22%           | 7.60%            |         109.83 |         34.48 |  43.45 |  49.84 |
|     14 | MSTR     |            1.68 |                0.41 |           61,850,224 |          36,829,388 |           -6,289,073 |         79.96 | 3.11%          | -22.39%         | -28.29%           | -41.16%           | -59.70%           | 13.63%           |         198.4  |         70.37 | 111.5  | 135.89 |
|     15 | WULF     |            1.63 |                2.15 |            2,134,097 |           1,310,374 |               64,063 |         10.03 | 0.20%          | -15.57%         | -13.90%           | -23.62%           | -66.39%           | 10.83%           |          29.84 |          9.05 |  11.65 |  13.13 |
|     16 | BABA     |            1.62 |                0.02 |            5,603,348 |           3,460,474 |             -753,477 |         86.26 | 1.65%          | -4.81%          | -9.38%            | -16.22%           | -52.37%           | 6.55%            |         181.1  |         80.96 |  95.19 | 102.96 |
|     17 | GLD      |            1.61 |                0.07 |           47,678,912 |          29,568,883 |            8,652,304 |        327.45 | 0.61%          | -7.22%          | -7.51%            | -11.75%           | -35.76%           | 4.30%            |         509.7  |        313.96 | 354.04 | 371.04 |
|     18 | GOOG     |            1.58 |                0.05 |           25,283,453 |          15,984,761 |            1,886,540 |        270.98 | -2.02%         | -3.65%          | -3.56%            | -14.05%           | -33.00%           | 3.95%            |         404.47 |        260.69 | 280.97 | 315.29 |
|     19 | RKLB     |            1.57 |                0.1  |            4,395,549 |           2,790,885 |              102,176 |         47.02 | 2.26%          | -18.04%         | -13.69%           | -22.15%           | -68.86%           | 17.61%           |         151    |         39.98 |  54.48 |  60.4  |
|     20 | UNH      |            1.49 |                0.83 |            5,305,952 |           3,566,379 |             -617,630 |        346.19 | 1.26%          | -15.98%         | -9.92%            | -10.43%           | -25.01%           | 35.25%           |         461.62 |        255.97 | 384.32 | 386.49 |
|     21 | INTC     |            1.43 |                0.05 |           22,142,774 |          15,537,606 |            2,852,870 |         54.47 | -0.60%         | -1.80%          | -8.24%            | -37.89%           | -61.74%           | 55.85%           |         142.35 |         34.95 |  59.36 |  87.7  |
|     22 | TSLA     |            1.29 |                2.86 |          133,146,025 |         103,399,505 |            1,970,355 |        380.14 | -1.18%         | 0.11%           | -0.53%            | 0.79%             | -23.79%           | 27.83%           |         498.83 |        297.38 | 382.15 | 377.17 |
|     23 | AVGO     |            1.11 |                1.69 |           44,291,433 |          39,975,510 |           -8,356,137 |        300.86 | -0.07%         | -9.76%          | -7.99%            | -11.66%           | -39.22%           | 8.22%            |         495    |        278    | 326.99 | 340.55 |
|     24 | HIMS     |            1.07 |                0.01 |            1,166,329 |           1,092,777 |               60,988 |         14.65 | -0.61%         | -21.07%         | -29.50%           | -43.01%           | -64.26%           | 8.84%            |          40.99 |         13.46 |  20.78 |  25.71 |
|     25 | MRVL     |            0.87 |                0.03 |           13,176,762 |          15,213,345 |           -1,547,088 |        130.93 | -0.49%         | -9.93%          | -15.51%           | -39.11%           | -60.31%           | 85.22%           |         329.88 |         70.69 | 154.97 | 215.01 |
|     26 | IBIT     |            0.72 |                0.33 |            8,778,690 |          12,196,847 |              724,384 |         34.07 | 0.92%          | -7.39%          | -13.97%           | -22.57%           | -38.72%           | 5.32%            |          55.6  |         32.35 |  39.6  |  44    |
|     27 | QQQ      |            0.68 |                0.25 |          561,267,445 |         829,393,610 |          -76,221,318 |        633.93 | -0.65%         | -4.20%          | -4.92%            | -10.34%           | -16.90%           | 14.10%           |         762.86 |        555.6  | 666.73 | 707.05 |
|     28 | SPY      |            0.63 |                1.29 |          508,719,221 |         803,490,780 |         -154,547,881 |        716.7  | -0.29%         | -3.14%          | -3.19%            | -5.43%            | -8.31%            | 13.89%           |         781.62 |        629.28 | 740.33 | 757.89 |
|     29 | ARM      |            0.49 |                0.01 |            4,967,652 |          10,085,143 |           -2,624,623 |        161.51 | -0.03%         | -7.73%          | -12.67%           | -31.31%           | -64.32%           | 61.48%           |         452.7  |        100.02 | 184.95 | 235.12 |
|     30 | CRWV     |            0.36 |                0.1  |           17,042,871 |          46,853,254 |           22,047,698 |         42.57 | -0.08%         | -14.66%         | -14.15%           | -35.22%           | -69.21%           | 13.82%           |         138.25 |         37.4  |  49.59 |  65.72 |
|     31 | AAPL     |            0.34 |                1.18 |           26,766,146 |          77,681,446 |            6,445,498 |        355.58 | 0.43%          | 0.79%           | 1.98%             | 3.65%             | -1.45%            | 46.08%           |         360.83 |        243.42 | 348.67 | 343.05 |
|     32 | SMH      |            0.3  |                0.09 |           42,465,414 |         141,750,281 |          -17,446,948 |        422.46 | -1.01%         | -8.54%          | -11.36%           | -21.93%           | -37.12%           | 24.97%           |         671.83 |        338.06 | 476.59 | 541.11 |
|     33 | XLF      |            0.13 |                0.12 |              879,924 |           6,705,867 |              -52,400 |         56.51 | 0.71%          | -2.87%          | -1.20%            | 1.20%             | -5.88%            | 18.54%           |          60.04 |         47.67 |  57.2  |  55.84 |

## T2 — Premium Ratio Leaderboard (all strikes, call subtotal ≥ $1,000,000)

|   Rank | Ticker   |   Premium Ratio |   Call Volume |   Call Premium |   Put Volume |   Put Premium |
|-------:|:---------|----------------:|--------------:|---------------:|-------------:|--------------:|
|      1 | SMCI     |            8.85 |        82,706 |     13,208,396 |        2,583 |     1,492,106 |
|      2 | RIOT     |            4.29 |       109,441 |      5,915,828 |       13,885 |     1,379,080 |
|      3 | QCOM     |            4.03 |        12,088 |      3,604,362 |          652 |       893,491 |
|      4 | TSM      |            3.62 |        81,743 |     90,121,370 |       18,378 |    24,907,811 |
|      5 | TLT      |            3.61 |        74,981 |      9,219,744 |       32,377 |     2,551,611 |
|      6 | AMZN     |            3.18 |        54,575 |     42,614,006 |        7,618 |    13,404,752 |
|      7 | TSLA     |            2.86 |        39,822 |     68,136,849 |       10,315 |    23,813,449 |
|      8 | WULF     |            2.15 |        19,982 |      1,290,130 |        5,938 |       599,576 |
|      9 | AVGO     |            1.69 |         8,139 |     23,962,528 |        4,063 |    14,168,281 |
|     10 | NVDA     |            1.55 |       206,052 |    108,888,564 |       56,496 |    70,333,648 |
|     11 | SPY      |            1.29 |       258,849 |    182,371,731 |      129,353 |   141,716,393 |
|     12 | AAPL     |            1.18 |        54,179 |     25,905,919 |       33,656 |    21,885,366 |
|     13 | MARA     |            1.16 |        15,545 |      1,326,675 |        7,097 |     1,146,015 |
|     14 | IREN     |            0.91 |        46,922 |      2,561,426 |       14,884 |     2,830,208 |
|     15 | UNH      |            0.83 |         3,277 |      3,616,224 |          324 |     4,368,765 |
|     16 | ^VIX     |            0.62 |        55,389 |     14,979,290 |       83,103 |    24,112,471 |
|     17 | MSTR     |            0.41 |        44,704 |     18,558,298 |        7,999 |    45,575,245 |
|     18 | IBIT     |            0.33 |        45,638 |      6,079,133 |       19,945 |    18,185,240 |
|     19 | SLV      |            0.32 |        20,828 |      3,911,150 |        3,002 |    12,395,330 |
|     20 | QQQ      |            0.25 |       104,251 |    117,902,439 |       54,452 |   468,751,873 |
|     21 | XLF      |            0.12 |         7,963 |      1,022,034 |       82,387 |     8,408,707 |
|     22 | RKLB     |            0.1  |        24,053 |      5,574,985 |        6,321 |    53,571,365 |
|     22 | CRWV     |            0.1  |        16,937 |      6,937,210 |       68,201 |    66,912,679 |
|     24 | SMH      |            0.09 |         5,924 |     17,195,660 |       28,993 |   195,627,509 |
|     24 | GOOGL    |            0.09 |        33,369 |     10,226,033 |       13,461 |   119,027,500 |
|     26 | SNDK     |            0.08 |        27,411 |     44,088,183 |       48,723 |   555,723,545 |
|     27 | GLD      |            0.07 |        19,412 |     15,797,146 |       24,792 |   238,180,170 |
|     28 | INTC     |            0.05 |        40,687 |     14,982,055 |       62,222 |   312,729,790 |
|     28 | GOOG     |            0.05 |        22,068 |     12,402,623 |       16,722 |   248,596,200 |
|     28 | COIN     |            0.05 |        28,255 |     12,423,790 |       23,331 |   275,819,475 |
|     31 | NFLX     |            0.03 |        21,227 |      2,809,273 |       38,690 |   104,555,179 |
|     31 | MRVL     |            0.03 |         8,410 |      8,085,315 |       24,455 |   289,461,627 |
|     33 | BABA     |            0.02 |        18,864 |      3,905,459 |       62,833 |   249,993,346 |
|     34 | ARM      |            0.01 |         1,901 |      2,721,517 |       16,750 |   342,931,700 |
|     34 | HIMS     |            0.01 |         7,357 |      1,288,125 |       21,367 |   104,089,345 |

## T1 — Top 4 Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261127C00350000  |        14,196 |      9,298,380 | AAPL270115P00350000  |        8,046 |     7,965,540 |
| AAPL     | AAPL261127C00352500  |        14,149 |      6,282,156 | AAPL261218P00350000  |        9,693 |     6,155,055 |
| AAPL     | AAPL261127C00355000  |        20,143 |      5,277,466 | AAPL261218P00340000  |       12,214 |     4,702,390 |
| AAPL     | AAPL261127C00347500  |         5,691 |      5,047,917 | AAPL270115P00345000  |        3,703 |     3,062,381 |
| AMZN     | AMZN270115C00255000  |        17,364 |     17,607,096 | AMZN270115P00235000  |        4,265 |     4,222,350 |
| AMZN     | AMZN261218C00250000  |        11,081 |      8,753,990 | AMZN270115P00325000  |          529 |     4,133,606 |
| AMZN     | AMZN270115C00245000  |         5,646 |      8,469,000 | AMZN270115P00285000  |          566 |     2,734,346 |
| AMZN     | AMZN270115C00275000  |        20,484 |      7,783,920 | AMZN261218P00245000  |        2,258 |     2,314,450 |
| ARM      | ARM261211C00165000   |           893 |      1,031,415 | ARM270115P00360000   |        9,550 |   190,092,750 |
| ARM      | ARM270115C00160000   |           426 |        954,666 | ARM270115P00420000   |        4,070 |   105,413,000 |
| ARM      | ARM270115C00145000   |           125 |        370,750 | ARM261218P00310000   |        2,400 |    35,808,000 |
| ARM      | ARM270115C00200000   |           457 |        364,686 | ARM261218P00320000   |          730 |    11,617,950 |
| AVGO     | AVGO270115C00150000  |           802 |     10,951,310 | AVGO261218P00470000  |          223 |     3,888,005 |
| AVGO     | AVGO261218C00330000  |         4,504 |      5,404,800 | AVGO261218P00300000  |        1,648 |     3,785,456 |
| AVGO     | AVGO270115C00320000  |         1,972 |      4,050,488 | AVGO261218P00460000  |          220 |     3,615,700 |
| AVGO     | AVGO270115C00280000  |           861 |      3,555,930 | AVGO261218P00280000  |        1,972 |     2,879,120 |
| BABA     | BABA270115C00100000  |        11,589 |      1,923,774 | BABA261218P00120000  |       23,065 |    79,666,510 |
| BABA     | BABA261204C00087000  |         3,636 |        858,096 | BABA270115P00140000  |       11,513 |    62,262,304 |
| BABA     | BABA270115C00085000  |           811 |        563,645 | BABA261218P00130000  |       13,188 |    57,499,680 |
| BABA     | BABA261127C00085000  |         2,828 |        559,944 | BABA270115P00120000  |       15,067 |    50,564,852 |
| COIN     | COIN261204C00101000  |         7,323 |      5,016,255 | COIN270115P00250000  |        6,565 |    96,676,190 |
| COIN     | COIN261204C00105000  |         7,555 |      3,603,735 | COIN270115P00230000  |        7,195 |    89,865,550 |
| COIN     | COIN261204C00100000  |         2,737 |      2,080,120 | COIN270115P00200000  |        6,490 |    61,564,140 |
| COIN     | COIN270115C00145000  |        10,640 |      1,723,680 | COIN270115P00195000  |        3,081 |    27,713,595 |
| CRWV     | CRWV261127C00040000  |         6,321 |      2,085,930 | CRWV270115P00047500  |       20,694 |    21,211,350 |
| CRWV     | CRWV270115C00045000  |         2,727 |      1,786,185 | CRWV270115P00120000  |        2,140 |    16,777,600 |
| CRWV     | CRWV261204C00043000  |         4,600 |      1,568,600 | CRWV270115P00110000  |        2,244 |    15,339,984 |
| CRWV     | CRWV270115C00050000  |         3,289 |      1,496,495 | CRWV261218P00037500  |       43,123 |    13,583,745 |
| ETHA     | ETHA261218C00041500  |           936 |         98,280 | ETHA261218P00043000  |        1,000 |       585,000 |
| ETHA     | ETHA261218C00035000  |           132 |         59,400 | ETHA261127P00043000  |        1,043 |       521,500 |
| ETHA     | ETHA270115C00042000  |           240 |         51,600 | ETHA261218P00042000  |        1,007 |       503,500 |
| ETHA     | ETHA261218C00045000  |           840 |         46,200 | ETHA261218P00041000  |        1,013 |       415,330 |
| GLD      | GLD270115C00350000   |         8,723 |      5,888,025 | GLD270115P00425000   |       13,750 |   133,925,000 |
| GLD      | GLD261218C00340000   |         8,011 |      4,766,545 | GLD270115P00420000   |        4,011 |    37,161,915 |
| GLD      | GLD270115C00320000   |         1,383 |      2,831,001 | GLD270115P00400000   |        4,730 |    34,292,500 |
| GLD      | GLD261231C00320000   |         1,295 |      2,311,575 | GLD261218P00470000   |        2,301 |    32,800,755 |
| GOOG     | GOOG270115C00300000  |         6,857 |      3,565,640 | GOOG270115P00480000  |        8,091 |   170,720,100 |
| GOOG     | GOOG261127C00270000  |         9,194 |      3,144,348 | GOOG261218P00360000  |        4,518 |    40,639,410 |
| GOOG     | GOOG261127C00265000  |         4,107 |      2,936,505 | GOOG261218P00340000  |        2,778 |    19,320,990 |
| GOOG     | GOOG270115C00275000  |         1,910 |      2,756,130 | GOOG261218P00405000  |        1,335 |    17,915,700 |
| GOOGL    | GOOGL261218C00300000 |        12,822 |      3,013,170 | GOOGL270115P00360000 |        6,385 |    56,826,500 |
| GOOGL    | GOOGL261204C00275000 |         3,838 |      2,513,890 | GOOGL270115P00370000 |        4,121 |    40,076,725 |
| GOOGL    | GOOGL261127C00275000 |        12,018 |      2,367,546 | GOOGL261218P00345000 |        1,700 |    12,580,000 |
| GOOGL    | GOOGL261127C00270000 |         4,691 |      2,331,427 | GOOGL261218P00350000 |        1,255 |     9,544,275 |
| HIMS     | HIMS270115C00003000  |           450 |        491,850 | HIMS270115P00080000  |        5,820 |    38,033,700 |
| HIMS     | HIMS270115C00015000  |         2,252 |        398,604 | HIMS270115P00105000  |        4,000 |    36,140,000 |
| HIMS     | HIMS261127C00014000  |         2,937 |        237,897 | HIMS270115P00040000  |       10,627 |    26,939,445 |
| HIMS     | HIMS261204C00014500  |         1,718 |        159,774 | HIMS270115P00047000  |          920 |     2,976,200 |
| IBIT     | IBIT270115C00033000  |         6,189 |      2,042,370 | IBIT261218P00050000  |        6,808 |    11,165,120 |
| IBIT     | IBIT261204C00033500  |        11,915 |      1,727,675 | IBIT261218P00047000  |        2,220 |     2,930,400 |
| IBIT     | IBIT261204C00034500  |        15,477 |      1,501,269 | IBIT270115P00056000  |          940 |     2,094,320 |
| IBIT     | IBIT270115C00040000  |        12,057 |        807,819 | IBIT270115P00033000  |        9,977 |     1,995,400 |
| INTC     | INTC261127C00050000  |        10,640 |      4,734,800 | INTC270115P00110000  |       14,854 |    84,667,800 |
| INTC     | INTC261218C00060000  |        17,668 |      4,505,340 | INTC270115P00105000  |       16,270 |    84,359,950 |
| INTC     | INTC261127C00051000  |         7,176 |      2,906,280 | INTC261218P00100000  |       15,915 |    74,163,900 |
| INTC     | INTC261218C00052500  |         5,203 |      2,835,635 | INTC270115P00100000  |       15,183 |    69,538,140 |
| IONQ     | IONQ270115C00030000  |         1,848 |        229,152 | IONQ270115P00120000  |          242 |     2,323,200 |
| IONQ     | IONQ270115C00022500  |           399 |        147,630 | IONQ270115P00050000  |          200 |       520,000 |
| IREN     | IREN261127C00013000  |        20,009 |        760,342 | IREN270115P00015000  |        2,612 |       953,380 |
| IREN     | IREN270115C00015000  |         4,324 |        691,840 | IREN261127P00015000  |        3,523 |       771,537 |
| IREN     | IREN261218C00015000  |         6,662 |        599,580 | IREN270115P00010000  |        5,416 |       655,336 |
| IREN     | IREN261231C00020000  |        15,927 |        509,664 | IREN261218P00012000  |        3,333 |       449,955 |
| MARA     | MARA270115C00005000  |         4,088 |        449,680 | MARA261231P00006000  |        2,798 |       313,376 |
| MARA     | MARA261204C00005000  |         5,030 |        316,890 | MARA270115P00007000  |        1,575 |       303,975 |
| MARA     | MARA261218C00005000  |         3,536 |        297,024 | MARA270115P00006000  |        2,354 |       284,834 |
| MARA     | MARA261224C00005000  |         2,891 |        263,081 | MARA261218P00012000  |          370 |       243,830 |
| MRVL     | MRVL261218C00125000  |         2,646 |      4,220,370 | MRVL270115P00250000  |       13,437 |   160,639,335 |
| MRVL     | MRVL261218C00160000  |         3,435 |      1,408,350 | MRVL261218P00230000  |        6,938 |    70,143,180 |
| MRVL     | MRVL261204C00100000  |           516 |      1,341,600 | MRVL270115P00280000  |        2,556 |    38,633,940 |
| MRVL     | MRVL261218C00150000  |         1,813 |      1,114,995 | MRVL270115P00260000  |        1,524 |    20,045,172 |
| MSTR     | MSTR261204C00082000  |        13,374 |      6,539,886 | MSTR261218P00180000  |        2,259 |    22,793,310 |
| MSTR     | MSTR261204C00085000  |        11,711 |      4,333,070 | MSTR261218P00280000  |          450 |     9,049,500 |
| MSTR     | MSTR261204C00087000  |        13,276 |      3,942,972 | MSTR261218P00160000  |          885 |     7,080,885 |
| MSTR     | MSTR261127C00075000  |         6,343 |      3,742,370 | MSTR261127P00093000  |        4,405 |     6,651,550 |
| NFLX     | NFLX261127C00059000  |         9,609 |        797,547 | NFLX270115P00100000  |       10,336 |    41,757,440 |
| NFLX     | NFLX261204C00059000  |         4,630 |        787,100 | NFLX270115P00090000  |        7,187 |    22,351,570 |
| NFLX     | NFLX261127C00058000  |         4,554 |        701,316 | NFLX261218P00075000  |       13,409 |    20,663,269 |
| NFLX     | NFLX261218C00060000  |         2,434 |        523,310 | NFLX270115P00084000  |        7,758 |    19,782,900 |
| NVDA     | NVDA270115C00170000  |        63,433 |     43,641,904 | NVDA270115P00150000  |       32,247 |    46,596,915 |
| NVDA     | NVDA261127C00150000  |        76,562 |     22,585,790 | NVDA261218P00140000  |       14,074 |     9,809,578 |
| NVDA     | NVDA261204C00152500  |        31,971 |     22,379,700 | NVDA270115P00145000  |        5,847 |     7,045,635 |
| NVDA     | NVDA261127C00145000  |        34,086 |     20,281,170 | NVDA261127P00165000  |        4,328 |     6,881,520 |
| NVDX     | NVDX261127C00007000  |           201 |         14,070 | NVDX261224P00019500  |          532 |       643,720 |
| OKLO     | OKLO261127C00018000  |         2,053 |        293,579 | OKLO270115P00075000  |        3,270 |    18,053,670 |
| OKLO     | OKLO270115C00020000  |           880 |        224,400 | OKLO261218P00075000  |        1,840 |    10,386,800 |
| OKLO     | OKLO261127C00019000  |         2,806 |        202,032 | OKLO261218P00040000  |        2,753 |     5,792,312 |
| OKLO     | OKLO261127C00017500  |           776 |        155,200 | OKLO261218P00045000  |        2,062 |     5,196,240 |
| QCOM     | QCOM261127C00170000  |         9,536 |      2,097,920 | QCOM270115P00175000  |          177 |       306,210 |
| QCOM     | QCOM261127C00160000  |           746 |        615,450 | QCOM270115P00150000  |          342 |       241,452 |
| QCOM     | QCOM270115C00200000  |         1,268 |        455,212 | QCOM261127P00255000  |           22 |       205,414 |
| QCOM     | QCOM261204C00165000  |           538 |        435,780 | QCOM261218P00172500  |          111 |       140,415 |
| QQQ      | QQQ270115C00680000   |        31,147 |     32,797,791 | QQQ261218P00725000   |       13,708 |   133,392,548 |
| QQQ      | QQQ261127C00620000   |        19,532 |     30,977,752 | QQQ261218P00735000   |       11,369 |   116,816,475 |
| QQQ      | QQQ261127C00630000   |        32,326 |     27,994,316 | QQQ261130P00700000   |       17,060 |   112,510,700 |
| QQQ      | QQQ261127C00625000   |        21,246 |     26,132,580 | QQQ261204P00720000   |       12,315 |   106,032,150 |
| RIOT     | RIOT261204C00018000  |        41,052 |      2,216,808 | RIOT261218P00015000  |       10,069 |       986,762 |
| RIOT     | RIOT261127C00016000  |        16,625 |      1,463,000 | RIOT261218P00014000  |        2,233 |       136,213 |
| RIOT     | RIOT261127C00017000  |        44,339 |      1,330,170 | RIOT261204P00018000  |          708 |       130,980 |
| RIOT     | RIOT261127C00015500  |         7,425 |        905,850 | RIOT261127P00018000  |          875 |       125,125 |
| RKLB     | RKLB261127C00045500  |        18,545 |      3,838,815 | RKLB270115P00165000  |        2,500 |    29,475,000 |
| RKLB     | RKLB261127C00045000  |         2,525 |        641,350 | RKLB261218P00110000  |        3,331 |    20,951,990 |
| RKLB     | RKLB270115C00055000  |         1,743 |        592,620 | RKLB261218P00100000  |          337 |     1,865,295 |
| RKLB     | RKLB261127C00043000  |         1,240 |        502,200 | RKLB270115P00130000  |          153 |     1,279,080 |
| SLV      | SLV270115C00040000   |         6,550 |      1,277,250 | SLV270115P00095000   |        1,000 |     5,865,000 |
| SLV      | SLV261127C00036000   |         6,340 |        900,280 | SLV270115P00070000   |        1,002 |     3,371,730 |
| SLV      | SLV270115C00038000   |         3,283 |        886,410 | SLV270115P00090000   |          300 |     1,609,500 |
| SLV      | SLV261218C00038000   |         4,655 |        847,210 | SLV261231P00059000   |          700 |     1,549,100 |
| SMCI     | SMCI261204C00021500  |        25,810 |      6,091,160 | SMCI261218P00035000  |          572 |       674,960 |
| SMCI     | SMCI261204C00023000  |        27,785 |      4,390,030 | SMCI261218P00040000  |          179 |       298,930 |
| SMCI     | SMCI261204C00023500  |        13,668 |      1,831,512 | SMCI270115P00020000  |        1,553 |       267,116 |
| SMCI     | SMCI261204C00025500  |        15,443 |        895,694 | SMCI261218P00032000  |          279 |       251,100 |
| SMH      | SMH261204C00400000   |         1,410 |      4,829,250 | SMH261218P00585000   |        5,350 |    89,612,500 |
| SMH      | SMH261218C00397500   |         1,050 |      4,436,250 | SMH261218P00635000   |        1,990 |    42,556,150 |
| SMH      | SMH261218C00410000   |         1,285 |      4,280,335 | SMH261218P00565000   |        2,550 |    37,612,500 |
| SMH      | SMH261218C00450000   |         2,179 |      3,649,825 | SMH270115P00350000   |       19,103 |    25,846,359 |
| SMR      | SMR261218C00002000   |           161 |         19,642 | SMR270115P00012000   |        1,455 |     1,271,670 |
| SMR      | SMR261211C00003000   |           252 |         10,332 | SMR270115P00017000   |          350 |       481,250 |
| SMR      | SMR261127C00003000   |           295 |          8,555 | SMR270115P00011000   |          505 |       383,800 |
| SNDK     | SNDK261218C00015000  |         4,792 |     27,855,896 | SNDK270115P00207500  |       19,981 |   268,944,260 |
| SNDK     | SNDK261127C00070000  |        18,142 |      8,345,320 | SNDK261218P00150000  |       15,385 |   121,741,505 |
| SNDK     | SNDK270115C00065000  |         2,651 |      4,413,915 | SNDK261218P00175000  |        8,407 |    88,609,780 |
| SNDK     | SNDK270115C00055000  |         1,826 |      3,473,052 | SNDK261218P00225000  |        4,950 |    76,428,000 |
| SPY      | SPY261127C00700000   |        27,735 |     49,368,300 | SPY261211P00700000   |       47,811 |    44,655,474 |
| SPY      | SPY261127C00720000   |       137,896 |     46,884,640 | SPY261130P00750000   |        9,212 |    33,071,080 |
| SPY      | SPY261127C00715000   |        71,369 |     43,535,090 | SPY261207P00700000   |       45,649 |    32,319,492 |
| SPY      | SPY261127C00699000   |        21,849 |     42,583,701 | SPY261218P00700000   |       26,681 |    31,670,347 |
| TLT      | TLT261218C00080000   |        13,506 |      3,173,910 | TLT270115P00081000   |       10,822 |       995,624 |
| TLT      | TLT270115C00083000   |        20,097 |      2,069,991 | TLT270115P00080000   |       13,538 |       798,742 |
| TLT      | TLT270115C00082000   |        14,037 |      2,007,291 | TLT261204P00082500   |        5,636 |       507,240 |
| TLT      | TLT270115C00084000   |        27,341 |      1,968,552 | TLT261218P00082000   |        2,381 |       250,005 |
| TSLA     | TSLA261224C00360000  |         6,722 |     24,871,400 | TSLA261224P00390000  |        2,829 |     7,924,029 |
| TSLA     | TSLA261204C00385000  |        15,504 |     18,465,264 | TSLA270115P00350000  |        3,324 |     5,534,460 |
| TSLA     | TSLA261127C00370000  |        10,717 |     13,449,835 | TSLA270115P00500000  |          459 |     5,429,970 |
| TSLA     | TSLA261127C00365000  |         6,879 |     11,350,350 | TSLA261231P00350000  |        3,703 |     4,924,990 |
| TSLL     | TSLL261127C00009000  |         5,498 |        384,860 | TSLL270115P00010000  |          821 |       138,749 |
| TSLL     | TSLL270115C00006000  |           641 |        253,836 | TSLL261127P00009500  |        5,385 |       118,470 |
| TSM      | TSM270115C00350000   |        18,079 |     46,101,450 | TSM261218P00330000   |        8,701 |    14,539,371 |
| TSM      | TSM270115C00420000   |        39,394 |     19,697,000 | TSM261218P00310000   |        5,602 |     5,602,000 |
| TSM      | TSM270115C00360000   |         6,062 |     12,487,720 | TSM270115P00320000   |        1,547 |     2,908,360 |
| TSM      | TSM270115C00410000   |        18,208 |     11,835,200 | TSM261218P00300000   |        2,528 |     1,858,080 |
| UNH      | UNH270115C00340000   |           617 |      1,326,550 | UNH261218P00460000   |          133 |     1,532,825 |
| UNH      | UNH261204C00352500   |         1,608 |        860,280 | UNH261218P00470000   |           77 |       962,500 |
| UNH      | UNH270115C00350000   |           493 |        830,705 | UNH261218P00520000   |           54 |       945,540 |
| UNH      | UNH261218C00350000   |           559 |        598,689 | UNH261218P00500000   |           60 |       927,900 |
| WULF     | WULF270115C00011000  |         4,070 |        508,750 | WULF261218P00010000  |        1,864 |       214,360 |
| WULF     | WULF270115C00013000  |         7,119 |        491,211 | WULF261218P00009000  |        2,950 |       206,500 |
| WULF     | WULF261127C00010000  |         8,793 |        290,169 | WULF270115P00010000  |        1,124 |       178,716 |
| XLF      | XLF261218C00057000   |         2,922 |        306,810 | XLF261218P00058000   |       27,037 |     5,218,141 |
| XLF      | XLF270115C00035000   |           124 |        265,980 | XLF261218P00053000   |       37,415 |     1,272,110 |
| XLF      | XLF261218C00055000   |         1,038 |        239,778 | XLF270115P00056000   |        7,087 |       963,832 |
| XLF      | XLF261204C00057000   |         3,879 |        209,466 | XLF261218P00056000   |       10,848 |       954,624 |
| ^VIX     | VIX261216C00020000   |         8,636 |      4,741,164 | VIX261216P00025000   |       29,205 |     8,381,835 |
| ^VIX     | VIX261216C00029000   |        22,675 |      4,126,850 | VIX270120P00022000   |       31,464 |     6,387,192 |
| ^VIX     | VIX270120C00035000   |        21,075 |      3,582,750 | VIX270120P00025000   |       14,897 |     5,914,109 |
| ^VIX     | VIX270120C00018000   |         3,003 |      2,528,526 | VIX270120P00026000   |        7,537 |     3,429,335 |

## T3 — Top 3 OTM Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261218C00365000  |         8,900 |      4,218,600 | AAPL270115P00350000  |        8,046 |     7,965,540 |
| AAPL     | AAPL261218C00360000  |         3,714 |      2,618,370 | AAPL261218P00350000  |        9,693 |     6,155,055 |
| AAPL     | AAPL261127C00357500  |        16,043 |      2,470,622 | AAPL261218P00340000  |       12,214 |     4,702,390 |
| AMZN     | AMZN270115C00255000  |        17,364 |     17,607,096 | AMZN270115P00235000  |        4,265 |     4,222,350 |
| AMZN     | AMZN261218C00250000  |        11,081 |      8,753,990 | AMZN261218P00210000  |       12,639 |     2,237,103 |
| AMZN     | AMZN270115C00245000  |         5,646 |      8,469,000 | AMZN261218P00240000  |        2,688 |     2,206,848 |
| ARM      | ARM261211C00165000   |           893 |      1,031,415 | ARM270115P00135000   |        1,638 |     1,670,760 |
| ARM      | ARM270115C00200000   |           457 |        364,686 | ARM270115P00140000   |        1,272 |     1,481,880 |
| ARM      | ARM270115C00250000   |         1,198 |        232,412 | ARM261218P00150000   |          888 |       927,960 |
| AVGO     | AVGO261218C00330000  |         4,504 |      5,404,800 | AVGO261218P00300000  |        1,648 |     3,785,456 |
| AVGO     | AVGO270115C00320000  |         1,972 |      4,050,488 | AVGO261218P00280000  |        1,972 |     2,879,120 |
| AVGO     | AVGO261204C00305000  |         2,704 |      3,217,760 | AVGO270115P00250000  |        2,157 |     2,236,809 |
| BABA     | BABA270115C00100000  |        11,589 |      1,923,774 | BABA270115P00080000  |        3,884 |     1,242,880 |
| BABA     | BABA261204C00087000  |         3,636 |        858,096 | BABA270115P00070000  |        3,823 |       389,946 |
| BABA     | BABA261218C00090000  |         1,790 |        470,770 | BABA270115P00075000  |        1,511 |       282,557 |
| COIN     | COIN261204C00105000  |         7,555 |      3,603,735 | COIN261204P00100000  |        3,677 |     1,360,490 |
| COIN     | COIN270115C00145000  |        10,640 |      1,723,680 | COIN270115P00100000  |        1,253 |     1,284,325 |
| COIN     | COIN261204C00107000  |         3,649 |      1,386,620 | COIN261204P00096000  |        3,014 |       747,472 |
| CRWV     | CRWV270115C00045000  |         2,727 |      1,786,185 | CRWV261218P00037500  |       43,123 |    13,583,745 |
| CRWV     | CRWV261204C00043000  |         4,600 |      1,568,600 | CRWV270115P00035000  |       20,322 |     7,702,038 |
| CRWV     | CRWV270115C00050000  |         3,289 |      1,496,495 | CRWV270115P00040000  |       10,980 |     6,313,500 |
| GLD      | GLD270115C00350000   |         8,723 |      5,888,025 | GLD270115P00320000   |        6,480 |     7,128,000 |
| GLD      | GLD261218C00340000   |         8,011 |      4,766,545 | GLD270115P00290000   |        8,393 |     3,138,982 |
| GLD      | GLD270115C00330000   |         1,427 |      2,090,555 | GLD261218P00310000   |        3,709 |     1,761,775 |
| GOOG     | GOOG270115C00300000  |         6,857 |      3,565,640 | GOOG270115P00270000  |        1,433 |     2,049,190 |
| GOOG     | GOOG270115C00275000  |         1,910 |      2,756,130 | GOOG261204P00265000  |        2,339 |     1,075,940 |
| GOOG     | GOOG261204C00275000  |         3,284 |      1,724,100 | GOOG270115P00265000  |          848 |     1,072,720 |
| GOOGL    | GOOGL261218C00300000 |        12,822 |      3,013,170 | GOOGL270115P00260000 |        1,588 |     1,580,060 |
| GOOGL    | GOOGL261204C00275000 |         3,838 |      2,513,890 | GOOGL261204P00270000 |        1,810 |     1,047,990 |
| GOOGL    | GOOGL261127C00275000 |        12,018 |      2,367,546 | GOOGL261218P00265000 |        1,175 |       898,875 |
| HIMS     | HIMS270115C00015000  |         2,252 |        398,604 | HIMS270115P00014000  |        5,254 |       756,576 |
| IBIT     | IBIT261204C00034500  |        15,477 |      1,501,269 | IBIT270115P00033000  |        9,977 |     1,995,400 |
| IBIT     | IBIT270115C00040000  |        12,057 |        807,819 | IBIT270115P00030000  |        8,441 |       920,069 |
| IBIT     | IBIT270115C00035000  |         3,403 |        762,272 | IBIT261218P00030000  |       11,245 |       640,965 |
| INTC     | INTC261218C00060000  |        17,668 |      4,505,340 | INTC261218P00050000  |       15,489 |     4,321,431 |
| INTC     | INTC270115C00065000  |         5,359 |      1,479,084 | INTC261204P00050000  |        5,537 |       802,865 |
| INTC     | INTC270115C00062500  |         4,304 |      1,398,800 | INTC261204P00053000  |        2,999 |       749,750 |
| IREN     | IREN261127C00013000  |        20,009 |        760,342 | IREN270115P00010000  |        5,416 |       655,336 |
| IREN     | IREN270115C00015000  |         4,324 |        691,840 | IREN261218P00012000  |        3,333 |       449,955 |
| IREN     | IREN261218C00015000  |         6,662 |        599,580 | IREN270115P00012000  |        1,246 |       256,676 |
| MRVL     | MRVL261218C00160000  |         3,435 |      1,408,350 | MRVL261218P00120000  |        3,865 |     3,721,995 |
| MRVL     | MRVL261218C00150000  |         1,813 |      1,114,995 | MRVL261204P00125000  |        2,304 |     1,728,000 |
| MRVL     | MRVL261204C00135000  |         1,055 |        886,200 | MRVL270115P00120000  |          941 |     1,199,775 |
| MSTR     | MSTR261204C00082000  |        13,374 |      6,539,886 | MSTR270115P00060000  |       13,242 |     5,349,768 |
| MSTR     | MSTR261204C00085000  |        11,711 |      4,333,070 | MSTR270115P00075000  |        3,071 |     2,960,444 |
| MSTR     | MSTR261204C00087000  |        13,276 |      3,942,972 | MSTR261204P00070000  |       10,968 |     2,467,800 |
| NFLX     | NFLX261218C00060000  |         2,434 |        523,310 | NFLX270115P00050000  |        4,816 |       303,408 |
| NFLX     | NFLX270115C00060000  |         1,529 |        515,273 | NFLX270115P00057000  |        1,265 |       292,215 |
| NFLX     | NFLX261204C00061000  |         5,152 |        396,704 | NFLX261204P00058000  |        1,830 |       151,890 |
| NVDA     | NVDA270115C00170000  |        63,433 |     43,641,904 | NVDA261218P00140000  |       14,074 |     9,809,578 |
| NVDA     | NVDA261127C00150000  |        76,562 |     22,585,790 | NVDA270115P00145000  |        5,847 |     7,045,635 |
| NVDA     | NVDA261204C00152500  |        31,971 |     22,379,700 | NVDA261218P00145000  |        7,520 |     6,700,320 |
| QCOM     | QCOM261127C00170000  |         9,536 |      2,097,920 | QCOM270115P00150000  |          342 |       241,452 |
| QCOM     | QCOM270115C00200000  |         1,268 |        455,212 | QCOM270115P00165000  |          111 |       134,754 |
| QCOM     | QCOM261204C00172500  |           763 |        358,610 | QCOM261218P00160000  |          134 |        96,480 |
| QQQ      | QQQ270115C00680000   |        31,147 |     32,797,791 | QQQ261218P00600000   |       33,591 |    39,603,789 |
| QQQ      | QQQ261218C00650000   |        17,190 |     25,527,150 | QQQ261218P00610000   |       26,963 |    37,748,200 |
| QQQ      | QQQ261218C00640000   |        11,334 |     22,429,986 | QQQ270115P00600000   |       18,194 |    32,312,544 |
| RIOT     | RIOT261204C00018000  |        41,052 |      2,216,808 | RIOT261218P00015000  |       10,069 |       986,762 |
| RIOT     | RIOT261127C00017000  |        44,339 |      1,330,170 | RIOT261218P00014000  |        2,233 |       136,213 |
| RIOT     | RIOT261204C00019500  |        40,389 |        888,558 | RIOT270115P00015000  |          589 |        91,295 |
| RKLB     | RKLB270115C00055000  |         1,743 |        592,620 | RKLB261204P00040000  |        4,081 |       285,670 |
| RKLB     | RKLB261204C00050000  |         1,929 |        316,356 | RKLB270115P00047000  |          429 |       268,125 |
| RKLB     | RKLB261211C00048000  |           779 |        292,125 | RKLB270115P00040000  |          594 |       184,140 |
| SLV      | SLV270115C00040000   |         6,550 |      1,277,250 | SLV270115P00035000   |        3,401 |       687,002 |
| SLV      | SLV270115C00038000   |         3,283 |        886,410 | SLV270115P00036000   |        2,279 |       562,913 |
| SLV      | SLV261218C00038000   |         4,655 |        847,210 | SLV261218P00035000   |        2,831 |       373,692 |
| SMCI     | SMCI261204C00023500  |        13,668 |      1,831,512 | SMCI270115P00020000  |        1,553 |       267,116 |
| SMCI     | SMCI261204C00025500  |        15,443 |        895,694 | SMCI261218P00023000  |          645 |       138,675 |
| SMCI     | SMCI261204C00024000  |         8,064 |        895,104 | SMCI261127P00023000  |        2,831 |       133,057 |
| SMH      | SMH261218C00450000   |         2,179 |      3,649,825 | SMH270115P00350000   |       19,103 |    25,846,359 |
| SMH      | SMH261204C00425000   |         1,116 |      2,062,368 | SMH270115P00400000   |        7,021 |    19,005,847 |
| SMH      | SMH261218C00425000   |           664 |      1,925,600 | SMH261218P00420000   |        5,739 |    15,403,476 |
| SPY      | SPY261127C00720000   |       137,896 |     46,884,640 | SPY261211P00700000   |       47,811 |    44,655,474 |
| SPY      | SPY261218C00720000   |        13,871 |     21,999,406 | SPY261207P00700000   |       45,649 |    32,319,492 |
| SPY      | SPY261127C00725000   |       126,899 |     20,176,941 | SPY261218P00700000   |       26,681 |    31,670,347 |
| TLT      | TLT270115C00083000   |        20,097 |      2,069,991 | TLT270115P00081000   |       10,822 |       995,624 |
| TLT      | TLT270115C00084000   |        27,341 |      1,968,552 | TLT270115P00080000   |       13,538 |       798,742 |
| TLT      | TLT261218C00083000   |        10,654 |        617,932 | TLT261218P00082000   |        2,381 |       250,005 |
| TSLA     | TSLA261204C00385000  |        15,504 |     18,465,264 | TSLA270115P00350000  |        3,324 |     5,534,460 |
| TSLA     | TSLA261211C00400000  |         7,445 |      7,660,905 | TSLA261231P00350000  |        3,703 |     4,924,990 |
| TSLA     | TSLA261218C00400000  |         4,342 |      5,718,414 | TSLA261127P00380000  |        8,989 |     4,899,005 |
| TSM      | TSM270115C00350000   |        18,079 |     46,101,450 | TSM261218P00330000   |        8,701 |    14,539,371 |
| TSM      | TSM270115C00420000   |        39,394 |     19,697,000 | TSM261218P00310000   |        5,602 |     5,602,000 |
| TSM      | TSM270115C00360000   |         6,062 |     12,487,720 | TSM270115P00320000   |        1,547 |     2,908,360 |
| UNH      | UNH261204C00352500   |         1,608 |        860,280 | UNH261218P00320000   |          709 |       326,140 |
| UNH      | UNH270115C00350000   |           493 |        830,705 | UNH270115P00300000   |          603 |       298,485 |
| UNH      | UNH261218C00350000   |           559 |        598,689 | UNH270115P00310000   |          396 |       258,588 |
| WULF     | WULF270115C00011000  |         4,070 |        508,750 | WULF261218P00010000  |        1,864 |       214,360 |
| WULF     | WULF270115C00013000  |         7,119 |        491,211 | WULF261218P00009000  |        2,950 |       206,500 |
| XLF      | XLF261218C00057000   |         2,922 |        306,810 | XLF261218P00053000   |       37,415 |     1,272,110 |
| XLF      | XLF261204C00057000   |         3,879 |        209,466 | XLF270115P00056000   |        7,087 |       963,832 |
| XLF      | XLF261204C00057500   |         2,626 |         89,284 | XLF261218P00056000   |       10,848 |       954,624 |
| ^VIX     | VIX261216C00029000   |        22,675 |      4,126,850 | VIX261216P00025000   |       29,205 |     8,381,835 |
| ^VIX     | VIX270120C00035000   |        21,075 |      3,582,750 | VIX270120P00022000   |       31,464 |     6,387,192 |
| ^VIX     | VIX270120C00034000   |         8,403 |      1,630,182 | VIX270120P00025000   |       14,897 |     5,914,109 |

*premium = volume × lastPrice × 100 · OTM = calls strike>spot, puts strike<spot · T4 uses the cleaned chain: ≥2 DTE, OTM only, leveraged ETFs folded into their underlying, ^VIX ratio inverted · Net Signed Premium = bought calls/sold puts minus sold calls/bought puts, side from lastPrice vs bid/ask (prints outside the closing quote are not signed) · generated by options-flow-pipeline*

---

**Data quality:** requested: 52 · fetched: 52 · failed: 0 · gated: 9 · stale volume: 21,458 contracts (15% of premium) dropped

_Signal check (next-day rank correlation, last 20 sessions): composite IC +0.060 (t +1.0, n=20) · flow_pct IC -0.064 (t -1.4, n=20) · trend_pct IC +0.110 (t +1.5, n=20)_

_Signal check, next 5 sessions (rank correlation, last 20 resolved sessions; windows overlap, so t is overstated): composite IC +0.048 (t +0.8, n=20) · flow_pct IC -0.163 (t -5.4, n=20) · trend_pct IC +0.176 (t +3.4, n=20)_