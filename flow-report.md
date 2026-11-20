# Options Flow Report (v1.3) — 2026-11-19

**Run stats:** 52/52 tickers fetched · 0 failed · 53,219 contracts

## Market Regime

**risk-off · backwardation (VIX/VIX3M=1.05, DoD +0.04) · negative gamma (moves amplified) · high vol · choppy/rangebound — momentum tilted**

`Vol: HIGH · Trend: CHOP · Risk: RISK_OFF · Gamma: NEGATIVE · SPY GEX: $-8,704M`

_Pipeline knobs: mom×0.85 · conviction≥0.88_

## Master Scoreboard (all tickers by composite)

| Rank   | Ticker   | Composite   | Trend%   | Mom%   | Flow%   | Rot%   | Conviction   | ΔRank   |
|:-------|:---------|:------------|:---------|:-------|:--------|:-------|:-------------|:--------|
| 1      | XLV      | 100.0       | 100      | 96     | N/A     | 94     | CONFIRMED    | 0       |
| 2      | XLP      | 98.4        | 98       | 88     | N/A     | 93     | CONFIRMED    | 0       |
| 3      | XLE      | 95.1        | 95       | 86     | N/A     | 87     | NEUTRAL      | 0       |
| 4      | XLRE     | 91.8        | 92       | 73     | N/A     | 82     | NEUTRAL      | +4      |
| 5      | XLK      | 88.5        | 89       | 81     | N/A     | 72     | NEUTRAL      | +1      |
| 6      | SNDK     | 87.9        | 79       | 71     | 96      | 73     | NEUTRAL      | ·       |
| 7      | BIL      | 86.9        | 87       | 66     | N/A     | 86     | NEUTRAL      | 0       |
| 8      | XLB      | 85.2        | 85       | 75     | N/A     | 75     | NEUTRAL      | -3      |
| 9      | XLY      | 82.0        | 82       | 68     | N/A     | 81     | NEUTRAL      | -5      |
| 10     | MRVL     | 80.6        | 84       | 78     | 78      | 71     | NEUTRAL      | +13     |
| 11     | AMZN     | 74.7        | 90       | 67     | 61      | 88     | NEUTRAL      | -2      |
| 12     | TSLA     | 72.3        | 62       | 55     | 81      | 68     | NEUTRAL      | +4      |
| 13     | ARM      | 68.9        | 69       | 71     | N/A     | 60     | NEUTRAL      | +35     |
| 14     | AAPL     | 68.5        | 97       | 80     | 45      | 100    | NEUTRAL      | +6      |
| 15     | TLT      | 66.1        | 59       | 53     | 72      | 69     | NEUTRAL      | +27     |
| 16     | IWM      | 65.6        | 66       | 62     | N/A     | 63     | NEUTRAL      | -5      |
| 17     | HYG      | 63.9        | 64       | 51     | N/A     | 74     | NEUTRAL      | -4      |
| 18     | QCOM     | 63.7        | 72       | 54     | 57      | 79     | NEUTRAL      | -8      |
| 19     | NVDA     | 61.8        | 43       | 53     | 78      | 33     | CONFLICT     | +19     |
| 20     | RIOT     | 60.7        | 61       | 52     | N/A     | 70     | NEUTRAL      | -8      |
| 21     | TSM      | 59.3        | 74       | 79     | 47      | 53     | NEUTRAL      | +14     |
| 22     | LQD      | 57.4        | 57       | 48     | N/A     | 72     | NEUTRAL      | +12     |
| 23     | HIVE     | 57.2        | 11       | 15     | 96      | 11     | CONFLICT     | -8      |
| 24     | SLV      | 56.8        | 30       | 35     | 80      | 27     | CONFLICT     | +22     |
| 25     | XLI      | 55.7        | 56       | 59     | N/A     | 55     | NEUTRAL      | -11     |
| 26     | QQQ      | 55.5        | 75       | 70     | 39      | 65     | NEUTRAL      | -9      |
| 27     | AI       | 54.1        | 54       | 57     | N/A     | 57     | NEUTRAL      | +27     |
| 28     | SMCI     | 53.5        | 41       | 53     | 64      | 31     | NEUTRAL      | -7      |
| 29     | XLU      | 52.7        | 77       | 61     | 32      | 76     | CONFLICT     | -5      |
| 30     | CPER     | 52.5        | 52       | 62     | N/A     | 48     | NEUTRAL      | -1      |
| 31     | SPY      | 51.2        | 80       | 65     | 26      | 83     | CONFLICT     | +6      |
| 32     | GOOGL    | 50.5        | 39       | 41     | 60      | 42     | NEUTRAL      | -10     |
| 33     | AVGO     | 49.6        | 51       | 50     | 49      | 60     | NEUTRAL      | -6      |
| 34     | UNH      | 49.2        | 67       | 67     | 34      | 59     | CONFLICT     | -16     |
| 35     | XLC      | 47.5        | 48       | 46     | N/A     | 57     | NEUTRAL      | +1      |
| 36     | INTC     | 46.6        | 49       | 65     | 44      | 42     | NEUTRAL      | -17     |
| 37     | GOOG     | 45.9        | 46       | 46     | N/A     | 46     | NEUTRAL      | -11     |
| 38     | XLF      | 45.6        | 93       | 81     | 5       | 83     | CONFLICT     | +3      |
| 39     | SMH      | 45.2        | 70       | 76     | 24      | 56     | CONFLICT     | +5      |
| 40     | IBIT     | 44.3        | 44       | 44     | N/A     | 46     | NEUTRAL      | +17     |
| 41     | ETHA     | 37.7        | 38       | 43     | N/A     | 39     | NEUTRAL      | +9      |
| 42     | GLD      | 37.6        | 33       | 32     | 42      | 41     | NEUTRAL      | +13     |
| 43     | RKLB     | 34.4        | 34       | 41     | N/A     | 37     | NEUTRAL      | +15     |
| 44     | HIMS     | 31.1        | 31       | 40     | N/A     | 26     | NEUTRAL      | +3      |
| 45     | WULF     | 29.3        | 36       | 43     | 23      | 37     | NEUTRAL      | -5      |
| 46     | CRWV     | 26.2        | 26       | 33     | N/A     | 17     | NEUTRAL      | +7      |
| 47     | MARA     | 24.6        | 25       | 25     | N/A     | 25     | NEUTRAL      | +5      |
| 48     | COIN     | 23.0        | 23       | 26     | N/A     | 23     | NEUTRAL      | +12     |
| 49     | MSTR     | 22.1        | 28       | 29     | 17      | 27     | NEUTRAL      | +10     |
| 50     | IONQ     | 19.7        | 20       | 23     | N/A     | 19     | NEUTRAL      | +6      |
| 51     | NFLX     | 18.2        | 21       | 14     | 16      | 33     | NEUTRAL      | -26     |
| 52     | BABA     | 18.0        | 18       | 16     | N/A     | 25     | NEUTRAL      | -3      |
| 53     | CLSK     | 16.4        | 16       | 24     | N/A     | 15     | NEUTRAL      | -22     |
| 54     | RGTI     | 14.8        | 15       | 21     | N/A     | 14     | NEUTRAL      | -15     |
| 55     | CIFR     | 13.1        | 13       | 22     | N/A     | 8      | NEUTRAL      | -12     |
| 56     | QBTS     | 9.8         | 10       | 17     | N/A     | 7      | NEUTRAL      | -23     |
| 57     | OKLO     | 8.2         | 8        | 11     | N/A     | 10     | NEUTRAL      | -12     |
| 58     | IREN     | 6.6         | 7        | 15     | N/A     | 2      | NEUTRAL      | -7      |
| 59     | SMR      | 4.9         | 5        | 11     | N/A     | 6      | NEUTRAL      | -27     |
| 60     | EOSE     | 3.3         | 3        | 7      | N/A     | 2      | NEUTRAL      | -30     |
| 61     | OPEN     | 1.6         | 2        | 3      | N/A     | 2      | NEUTRAL      | -33     |
| N/A    | AAPX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDU     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | TSLL     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^GSPC    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^SKEW    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX     | N/A         | N/A      | N/A    | 84      | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX3M   | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VVIX    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |

## Sector Rotation / Relative Strength (top 15)

| Ticker   |   RS Rating |   Rel Str 63d | RS New-High   | Dual-Mom   |
|:---------|------------:|--------------:|:--------------|:-----------|
| AAPL     |          99 |          19.2 | Yes           | above cash |
| SNDK     |          97 |         -46.4 | No            | above cash |
| XLV      |          96 |           8.3 | No            | above cash |
| XLE      |          94 |           2.5 | No            | above cash |
| XLP      |          92 |          11.5 | No            | above cash |
| MRVL     |          91 |         -35.3 | No            | above cash |
| AMZN     |          89 |           5.8 | No            | above cash |
| XLF      |          88 |           3.3 | No            | above cash |
| BIL      |          86 |           7.2 | No            | below cash |
| XLRE     |          84 |           3.9 | No            | above cash |
| SPY      |          83 |           0   | Yes           | above cash |
| XLY      |          81 |           4.7 | No            | above cash |
| XLB      |          79 |          -1   | No            | above cash |
| XLK      |          78 |          -6   | No            | above cash |
| RIOT     |          76 |          -6.8 | No            | above cash |

## Option Skew — Extremes (top/bottom 8)

_Board-wide: protection demand rising across the board (typical name z +1.4 vs its own norm; 17 of 26 names at z +1 or more, 0 at −1 or less). Hedging arrows are measured net of this move._

| Ticker   | Group    | Tilt        |   Skew25 (vol pts) | 90-110   |   ATM IV % |   Skew/IV | Hedging          |    z | Flow        | Positioning   |
|:---------|:---------|:------------|-------------------:|:---------|-----------:|----------:|:-----------------|-----:|:------------|:--------------|
| SPY      | top 8    | put-skewed  |                8.8 | 16.3     |       23.4 |      0.38 | hedging easing ↓ | -1.4 | Neutral -4  |               |
| QQQ      | top 8    | put-skewed  |                9.3 | 14.2     |       32   |      0.29 | hedging easing ↓ | -1.3 | Neutral +0  |               |
| AAPL     | top 8    | put-skewed  |                5.5 | 12.0     |       24.7 |      0.22 | steady →         | -0.5 | Neutral +8  |               |
| TSM      | top 8    | put-skewed  |                9.2 | 9.5      |       50.1 |      0.18 | steady →         |  0.6 | Neutral +4  |               |
| MSTR     | top 8    | put-skewed  |               16.6 | 10.0     |       93.6 |      0.18 | steady →         |  0.4 | Neutral +5  |               |
| TSLA     | top 8    | put-skewed  |                9   | 9.4      |       50.8 |      0.18 | steady →         |  0   | Neutral +3  |               |
| IBIT     | top 8    | put-skewed  |                7.9 | 8.9      |       46.6 |      0.17 | steady →         |  0.4 | n/a         |               |
| GOOG     | top 8    | put-skewed  |                6.2 | 8.4      |       37   |      0.17 | steady →         |  0.7 | n/a         |               |
| TLT      | bottom 8 | call-skewed |               -0.5 | N/A      |       12.8 |     -0.04 | hedging easing ↓ | -2.1 | Bull +53    | speculative   |
| HIMS     | bottom 8 | put-skewed  |                3.4 | 2.8      |       76.1 |      0.04 | steady →         |  0.2 | n/a         |               |
| BABA     | bottom 8 | put-skewed  |                2.6 | 2.4      |       46   |      0.06 | steady →         |  0.1 | n/a         |               |
| MARA     | bottom 8 | put-skewed  |                8.7 | 5.6      |      104.2 |      0.08 | steady →         | -0.8 | n/a         |               |
| GLD      | bottom 8 | put-skewed  |                2.2 | 3.9      |       26.2 |      0.08 | steady →         | -0.5 | Neutral +2  |               |
| IREN     | bottom 8 | put-skewed  |               12.8 | 6.6      |      123.8 |      0.1  | steady →         | -0.6 | n/a         |               |
| RKLB     | bottom 8 | put-skewed  |                9.2 | 5.6      |       84.5 |      0.11 | steady →         |  0.4 | n/a         |               |
| SNDK     | bottom 8 | put-skewed  |               11.3 | 6.8      |      100.9 |      0.11 | steady →         | -0.4 | Neutral +15 |               |

_26 of 52 tickers had a fittable smile. Skew25 = how much more an out-of-the-money put costs than the matching out-of-the-money call, in vol points, at a constant 30-day tenor, re-derived from bid/ask mids (Yahoo's own IV field is not used). Positive = puts richer, the normal state — so read the *ranking*, not the level. Tilt is by sign: call-skewed = Skew/IV below 0; least put-skewed = 0 to 0.02; put-skewed above. Hedging = tonight's Skew/IV against the name's own previous 20 sessions (z = standard deviations from that average), net of the typical name's move tonight (the Board-wide line above): building when z is at least +1, easing at −1 or below, else steady; n/a until 10 prior sessions exist. It describes protection demand, not a price forecast._

## Mega-Cap Tech Skew

| Ticker   | Skew25 (vol pts)   |   90-110 |   ATM IV % | Skew/IV   | Rank     | Read                | Hedging              |    z | Flow       | Positioning   |
|:---------|:-------------------|---------:|-----------:|:----------|:---------|:--------------------|:---------------------|-----:|:-----------|:--------------|
| NVDA     | 7.5                |      7.6 |       53.5 | 0.14      | 12 of 26 | put-skewed          | steady →             | -1   | Neutral +3 |               |
| AAPL     | 5.5                |     12   |       24.7 | 0.22      | 3 of 26  | steep put skew      | steady →             | -0.5 | Neutral +8 |               |
| AMZN     | 6.2                |      8.8 |       38.4 | 0.16      | 9 of 26  | put-skewed          | steady →             | -0.1 | Neutral +6 |               |
| GOOGL    | 6.0                |      8   |       37.6 | 0.16      | 10 of 26 | put-skewed          | steady →             |  0.5 | Neutral +3 |               |
| TSLA     | 9.0                |      9.4 |       50.8 | 0.18      | 6 of 26  | steep put skew      | steady →             |  0   | Neutral +3 |               |
| AVGO     | N/A                |      7.7 |       63.2 | N/A       | N/A      | put-skewed (90-110) | n/a (no fit tonight) |      | Neutral +7 |               |

_Mega-cap tech: 5 of 6 fitted · median Skew/IV 0.16 vs 0.11 for the other names · richer downside protection than the rest of the board · steepest: AAPL, TSLA._

_Flow = premium-weighted flow score: 100 × (bought calls + sold puts − sold calls − bought puts) ÷ total out-of-the-money premium, sides estimated from the last trade against bid/ask (a last trade outside the closing quote is left unsigned); Bull at +20 or more, Bear at −20 or less. Positioning: defensive = hedging building with Bear flow; speculative = hedging easing with Bull flow; blank otherwise. Positioning describes what is being hedged and flowed tonight. It is not a price forecast._

## Stretch & Reversal Watch (experimental)

| Watch             | Tonight                                                                          | Backtest (before live)                                       | Live since 2026-11-06                      |
|:------------------|:---------------------------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------|
| hedging unwinding | TLT (z -2.1)                                                                     | 194 flags · +1.6% vs avg name · 59% beat it                  | 6 flags · -1.5% vs avg name · 50% beat it  |
| stretched up      | none                                                                             | 597 flags · -1.5% vs avg name · 41% beat it                  | 55 flags · -2.1% vs avg name · 49% beat it |
| washed out        | SMCI (-12%), GOOG (-8%)                                                          | 118 flags · -0.1% vs avg name · 57% beat it (no edge so far) | 15 flags · +2.4% vs avg name · 67% beat it |
| puts closing      | COIN (93% puts), RKLB (91% puts), TLT (89% puts), SPY (89% puts), XLU (83% puts) | 813 flags · +0.7% vs avg name · 55% beat it (to 2026-11-16)  | none resolved yet (counts from 2026-11-16) |

_Experimental, not proven. Hedging unwinding = tonight's Skew/IV at z -1.5 or lower against the name's own norm, net of the board (as the Hedging column): protection being sold off. Stretched up = price up 5% or more over the last 5 sessions. Washed out = down 5% or more with hedging at z +2 or more on its own norm. Puts closing = the fifth of names where puts made up most of the out-of-the-money positions closed in the previous session (volume matched against the drop in open interest): protection taken off. The record columns score each past flag 5 sessions later against the average name that night (prices from the option chains' implied forwards). The backtest is in-sample: the thresholds were picked on that same history, so it flatters the flags; the live column counts only flags raised since this block was added and is the one that matters. If the live record does not hold up, the block goes. Not a price forecast._

---

# Flow Detail

## T4 — OTM Flow Summary (ranked by OTM Call/Put premium ratio)

|   Rank | Ticker   |   Premium Ratio |   Premium Ratio All |   Total Call Premium |   Total Put Premium |   Net Signed Premium |   Close Price | 1-Day Return   | 1-Week Return   | % Close to MA20   | % Close to MA50   | % Close to High   | % Close to Low   |   52 Week High |   52 Week Low |   MA20 |   MA50 |
|-------:|:---------|----------------:|--------------------:|---------------------:|--------------------:|---------------------:|--------------:|:---------------|:----------------|:------------------|:------------------|:------------------|:-----------------|---------------:|--------------:|-------:|-------:|
|      1 | SNDK     |         3560.02 |                0.02 |           71,364,132 |              20,045 |           10,712,132 |         94.39 | -2.71%         | -12.19%         | -25.41%           | -44.70%           | -67.93%           | 312.66%          |         294.3  |         22.88 | 126.56 | 170.69 |
|      2 | SLV      |            2.66 |                0.03 |            6,972,239 |           2,623,904 |            1,801,107 |         39.64 | -2.60%         | -14.72%         | -13.33%           | -22.93%           | -63.91%           | 0.13%            |         109.83 |         39.59 |  45.74 |  51.43 |
|      3 | MRVL     |            2.62 |                0.01 |           11,692,951 |           4,460,973 |              526,782 |        138.47 | -4.86%         | -10.31%         | -21.49%           | -37.78%           | -58.02%           | 95.88%           |         329.88 |         70.69 | 176.36 | 222.55 |
|      4 | ^VIX     |            2.58 |                1.52 |           10,056,680 |          25,990,030 |           -4,168,425 |         28.44 | 15.80%         | 46.15%          | 36.23%            | 57.70%            | -19.43%           | 112.56%          |          35.3  |         13.38 |  20.88 |  18.03 |
|      5 | TSLA     |            2.25 |                0.4  |           95,286,447 |          42,424,570 |            4,410,397 |        374.41 | -2.43%         | -1.41%          | -3.03%            | -0.43%            | -24.94%           | 25.90%           |         498.83 |        297.38 | 386.12 | 376.03 |
|      6 | NVDA     |            2.22 |                0.04 |          163,303,667 |          73,587,410 |            7,105,904 |        145.98 | -3.30%         | -13.57%         | -21.40%           | -30.10%           | -40.02%           | 0.19%            |         243.37 |        145.71 | 185.73 | 208.86 |
|      7 | TLT      |            2.05 |                1.19 |           11,773,351 |           5,744,408 |            9,200,092 |         80.35 | 0.16%          | -0.66%          | -0.79%            | 0.36%             | -11.57%           | 5.13%            |          90.86 |         76.43 |  80.99 |  80.06 |
|      7 | QCOM     |            2.05 |                0.5  |            3,184,881 |           1,554,015 |             -192,046 |        162.01 | 1.38%          | -6.64%          | -5.34%            | -8.96%            | -37.67%           | 32.81%           |         259.92 |        121.99 | 171.15 | 177.95 |
|      9 | AMZN     |            2.01 |                0.27 |           54,974,620 |          27,392,898 |            5,336,870 |        257.37 | -3.87%         | -4.98%          | -0.04%            | 0.84%             | -10.39%           | 31.31%           |         287.2  |        196    | 257.48 | 255.23 |
|     10 | SMCI     |            1.91 |                0.43 |            3,398,294 |           1,779,944 |              747,670 |         23.84 | -2.17%         | -14.21%         | -19.08%           | -32.58%           | -53.62%           | 22.38%           |          51.4  |         19.48 |  29.46 |  35.36 |
|     11 | GOOGL    |            1.85 |                0.03 |           30,589,660 |          16,508,381 |            1,410,628 |        272.66 | -3.46%         | -5.12%          | -6.69%            | -15.78%           | -33.27%           | 0.20%            |         408.61 |        272.11 | 292.2  | 323.76 |
|     12 | AVGO     |            1.49 |                0.31 |           45,404,973 |          30,523,527 |            5,510,682 |        346.65 | -2.09%         | 4.42%           | 4.02%             | 0.81%             | -29.97%           | 19.63%           |         495    |        289.77 | 333.24 | 343.86 |
|     13 | TSM      |            1.38 |                0.09 |           16,297,420 |          11,822,607 |            1,070,608 |        352.09 | -2.90%         | -11.20%         | -11.26%           | -17.05%           | -27.77%           | 31.96%           |         487.47 |        266.82 | 396.77 | 424.44 |
|     14 | INTC     |            1.34 |                0.03 |           14,279,554 |          10,682,068 |            3,564,447 |         55.72 | 1.92%          | -4.15%          | -16.45%           | -38.94%           | -60.86%           | 69.41%           |         142.35 |         32.89 |  66.69 |  91.26 |
|     15 | XLU      |            1.18 |                2.64 |              790,845 |             668,926 |              -39,801 |         43.01 | -1.24%         | -1.65%          | -0.83%            | 2.56%             | -10.02%           | 10.20%           |          47.8  |         39.03 |  43.37 |  41.93 |
|     16 | GLD      |            1.13 |                0.02 |           14,341,810 |          12,654,574 |              556,378 |        335.18 | -1.76%         | -9.25%          | -7.56%            | -10.96%           | -34.24%           | 0.04%            |         509.7  |        335.05 | 362.61 | 376.42 |
|     17 | AAPL     |            1.12 |                0.75 |           42,015,577 |          37,480,318 |            6,146,249 |        349.21 | -0.92%         | 0.20%           | 0.42%             | 2.23%             | -3.22%            | 43.46%           |         360.83 |        243.42 | 347.74 | 341.6  |
|     18 | WULF     |            1.01 |                0.24 |            2,102,679 |           2,085,468 |             -187,599 |         11.58 | -3.50%         | -7.80%          | -4.13%            | -14.58%           | -61.19%           | 21.77%           |          29.84 |          9.51 |  12.08 |  13.56 |
|     19 | QQQ      |            1    |                0.11 |          365,425,740 |         363,662,123 |           -3,450,412 |        645.04 | -2.19%         | -4.40%          | -5.60%            | -9.54%            | -15.44%           | 16.10%           |         762.86 |        555.6  | 683.33 | 713.09 |
|     20 | UNH      |            0.74 |                0.05 |            7,331,547 |           9,920,881 |             -295,070 |        330.48 | -5.55%         | -18.42%         | -17.05%           | -15.15%           | -28.41%           | 29.11%           |         461.62 |        255.97 | 398.43 | 389.48 |
|     21 | SMH      |            0.67 |                0.02 |           31,056,679 |          46,663,228 |            5,105,928 |        447.48 | -2.62%         | -7.47%          | -10.66%           | -18.77%           | -33.39%           | 42.03%           |         671.83 |        315.05 | 500.85 | 550.88 |
|     22 | NFLX     |            0.64 |                0.02 |            5,735,450 |           8,892,296 |              932,310 |         58.46 | -2.27%         | -7.59%          | -6.82%            | -13.80%           | -47.38%           | 0.48%            |         111.1  |         58.18 |  62.74 |  67.82 |
|     23 | SPY      |            0.54 |                0.18 |          359,206,402 |         667,729,956 |          -37,429,969 |        715.87 | -1.96%         | -4.54%          | -4.72%            | -6.01%            | -8.41%            | 13.76%           |         781.62 |        629.28 | 751.32 | 761.67 |
|     24 | MSTR     |            0.53 |                0.03 |            7,478,163 |          14,006,935 |            1,038,320 |         86.13 | -4.64%         | -28.86%         | -30.62%           | -38.47%           | -56.59%           | 5.28%            |         198.4  |         81.81 | 124.13 | 139.97 |
|     25 | XLF      |            0.43 |                0.4  |            2,352,248 |           5,474,592 |              185,840 |         55.58 | -1.49%         | -4.65%          | -2.92%            | -0.62%            | -7.43%            | 16.59%           |          60.04 |         47.67 |  57.25 |  55.93 |

## T2 — Premium Ratio Leaderboard (all strikes, call subtotal ≥ $1,000,000)

|   Rank | Ticker   |   Premium Ratio |   Call Volume |   Call Premium |   Put Volume |   Put Premium |
|-------:|:---------|----------------:|--------------:|---------------:|-------------:|--------------:|
|      1 | RIOT     |            2.91 |        66,645 |      3,628,004 |        6,587 |     1,247,786 |
|      2 | ^VIX     |            1.52 |       147,367 |     21,482,535 |      415,797 |    14,138,227 |
|      3 | TLT      |            1.19 |       313,656 |      9,129,425 |       45,441 |     7,695,943 |
|      4 | AAPL     |            0.75 |        43,714 |     22,501,410 |       95,578 |    30,199,540 |
|      5 | CRWV     |            0.57 |        28,876 |      5,226,298 |       11,367 |     9,142,738 |
|      6 | QCOM     |            0.5  |         3,769 |      1,373,044 |        1,997 |     2,745,580 |
|      7 | RKLB     |            0.44 |         8,269 |      1,437,523 |        6,821 |     3,248,264 |
|      8 | SMCI     |            0.43 |        31,849 |      1,225,169 |       14,575 |     2,860,634 |
|      9 | XLF      |            0.4  |        44,627 |      2,588,613 |       55,075 |     6,498,082 |
|      9 | TSLA     |            0.4  |       109,564 |     32,432,214 |       85,834 |    80,968,915 |
|     11 | AVGO     |            0.31 |         7,990 |     14,302,818 |        7,300 |    46,825,433 |
|     12 | AMZN     |            0.27 |        43,851 |     25,918,842 |      109,165 |    95,377,348 |
|     13 | WULF     |            0.24 |        24,078 |      1,184,886 |       19,031 |     5,009,330 |
|     14 | SPY      |            0.18 |        84,707 |     66,198,444 |      151,701 |   372,456,805 |
|     15 | QQQ      |            0.11 |        98,862 |     81,627,292 |      109,604 |   758,366,574 |
|     16 | TSM      |            0.09 |         7,654 |      5,740,293 |        7,770 |    62,487,970 |
|     17 | UNH      |            0.05 |         2,172 |     13,013,036 |       38,984 |   281,337,691 |
|     17 | IREN     |            0.05 |        17,916 |      2,641,939 |       35,121 |    54,550,048 |
|     19 | NVDA     |            0.04 |       186,697 |     51,289,657 |      220,863 | 1,348,953,536 |
|     20 | GOOGL    |            0.03 |        21,334 |     10,869,850 |       53,067 |   329,704,804 |
|     20 | INTC     |            0.03 |        41,566 |      5,923,950 |       59,865 |   235,336,658 |
|     20 | SLV      |            0.03 |        11,135 |      2,271,987 |       24,067 |    81,234,710 |
|     20 | IBIT     |            0.03 |        34,970 |      1,990,625 |       58,980 |    71,198,701 |
|     20 | MSTR     |            0.03 |         5,296 |      4,292,145 |       29,329 |   150,503,860 |
|     25 | GOOG     |            0.02 |         7,876 |      6,095,252 |       31,304 |   294,076,890 |
|     25 | GLD      |            0.02 |         4,264 |      5,200,255 |       39,363 |   243,703,550 |
|     25 | HIMS     |            0.02 |        15,563 |      1,064,876 |       12,111 |    70,804,280 |
|     25 | NFLX     |            0.02 |         8,902 |      2,750,744 |       38,384 |   110,453,035 |
|     25 | SNDK     |            0.02 |        11,086 |     17,065,166 |       17,645 |   861,990,370 |
|     25 | SMH      |            0.02 |         9,061 |     10,511,550 |       56,488 |   548,430,614 |
|     31 | MRVL     |            0.01 |         7,352 |      4,564,600 |       84,083 |   449,565,464 |
|     31 | BABA     |            0.01 |        14,903 |      1,589,510 |       29,484 |   148,344,615 |

## T1 — Top 4 Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261120C00350000  |        33,034 |      7,234,446 | AAPL261120P00350000  |       36,485 |    10,945,500 |
| AAPL     | AAPL270115C00350000  |         3,912 |      5,594,160 | AAPL261120P00347500  |       36,418 |     6,919,420 |
| AAPL     | AAPL270115C00330000  |         1,807 |      5,014,425 | AAPL261218P00350000  |        6,467 |     6,337,660 |
| AAPL     | AAPL261231C00355000  |         4,961 |      4,658,379 | AAPL261218P00330000  |       16,208 |     5,996,960 |
| AI       | AI261120C00011000    |        19,146 |         38,292 | AI261120P00013000    |        1,002 |       284,568 |
| AMZN     | AMZN261218C00260000  |         9,978 |     10,187,538 | AMZN261120P00270000  |       31,259 |    40,636,700 |
| AMZN     | AMZN270115C00270000  |         8,714 |      8,496,150 | AMZN261120P00265000  |       32,710 |    26,756,780 |
| AMZN     | AMZN261218C00275000  |         8,415 |      3,618,450 | AMZN261120P00260000  |       33,438 |    15,849,612 |
| AMZN     | AMZN261120C00260000  |        16,744 |      3,616,704 | AMZN261120P00267500  |       11,758 |    12,134,256 |
| ARM      | ARM261218C00200000   |           509 |        417,380 | ARM270115P00360000   |        7,690 |   138,727,600 |
| ARM      | ARM261120C00180000   |           546 |        174,720 | ARM261120P00250000   |       11,611 |    81,857,550 |
| ARM      | ARM261120C00185000   |         1,059 |        168,381 | ARM261120P00230000   |       10,404 |    53,622,216 |
| ARM      | ARM270115C00310000   |         2,002 |        160,160 | ARM270115P00420000   |        1,900 |    45,695,000 |
| AVGO     | AVGO270115C00400000  |         3,325 |      3,840,375 | AVGO261120P00460000  |        1,628 |    18,201,040 |
| AVGO     | AVGO261218C00350000  |         1,542 |      3,693,090 | AVGO261120P00420000  |        1,787 |    12,821,725 |
| AVGO     | AVGO261218C00360000  |         1,793 |      3,444,353 | AVGO261120P00430000  |          969 |     8,197,740 |
| AVGO     | AVGO270115C00360000  |         1,330 |      3,325,000 | AVGO261218P00350000  |        2,916 |     7,604,928 |
| BABA     | BABA261204C00092000  |         6,710 |        523,380 | BABA261218P00130000  |       13,933 |    64,091,800 |
| BABA     | BABA261120C00085000  |         5,710 |        445,380 | BABA261218P00135000  |        6,406 |    32,446,390 |
| BABA     | BABA270115C00090000  |           832 |        313,664 | BABA261218P00140000  |        5,032 |    28,506,280 |
| BABA     | BABA261127C00085000  |         1,651 |        307,086 | BABA270115P00140000  |        4,113 |    23,300,145 |
| COIN     | COIN261127C00121000  |         2,200 |        275,000 | COIN270115P00250000  |        6,900 |    94,674,900 |
| COIN     | COIN261218C00130000  |         1,041 |        260,250 | COIN270115P00230000  |        4,805 |    57,732,075 |
| COIN     | COIN270115C00140000  |           799 |        247,690 | COIN261120P00165000  |        9,196 |    49,704,380 |
| COIN     | COIN261127C00120000  |         1,654 |        188,556 | COIN261120P00150000  |        7,388 |    30,290,800 |
| CRWV     | CRWV261218C00055000  |        13,608 |      2,762,424 | CRWV261218P00050000  |        2,906 |     2,435,228 |
| CRWV     | CRWV261120C00046000  |        11,594 |      1,043,460 | CRWV261120P00160000  |          200 |     2,299,000 |
| CRWV     | CRWV261218C00047500  |         1,751 |        770,440 | CRWV261218P00045000  |        4,205 |     2,279,110 |
| CRWV     | CRWV261218C00050000  |         1,923 |        649,974 | CRWV261120P00050000  |        4,056 |     2,129,400 |
| GLD      | GLD270115C00340000   |         2,471 |      3,026,975 | GLD270115P00425000   |       10,690 |    94,392,700 |
| GLD      | GLD270115C00350000   |           953 |        771,930 | GLD261218P00400000   |        7,899 |    50,237,640 |
| GLD      | GLD270115C00345000   |           734 |        726,660 | GLD261120P00365000   |       17,074 |    49,770,710 |
| GLD      | GLD270115C00276000   |           106 |        674,690 | GLD261218P00470000   |        3,700 |    49,302,500 |
| GOOG     | GOOG270115C00300000  |         4,630 |      2,338,150 | GOOG270115P00480000  |        5,770 |   117,765,700 |
| GOOG     | GOOG261218C00280000  |         1,896 |      1,422,000 | GOOG261120P00340000  |       12,716 |    87,613,240 |
| GOOG     | GOOG270115C00250000  |           392 |      1,215,200 | GOOG261120P00330000  |        8,462 |    49,798,870 |
| GOOG     | GOOG270115C00280000  |           958 |      1,119,902 | GOOG261218P00360000  |        4,356 |    38,899,080 |
| GOOGL    | GOOGL261218C00300000 |        13,507 |      3,579,355 | GOOGL261120P00330000 |       25,701 |   141,535,407 |
| GOOGL    | GOOGL270115C00300000 |         5,571 |      3,147,615 | GOOGL261120P00335000 |       14,035 |    84,659,120 |
| GOOGL    | GOOGL261218C00250000 |           864 |      2,388,960 | GOOGL261120P00355000 |        6,668 |    54,077,480 |
| GOOGL    | GOOGL270115C00280000 |         1,392 |      1,753,920 | GOOGL261120P00350000 |        6,663 |    49,432,797 |
| HIMS     | HIMS261127C00017000  |        13,041 |        495,558 | HIMS270115P00080000  |        4,390 |    27,766,750 |
| HIMS     | HIMS270115C00017000  |         1,676 |        264,808 | HIMS270115P00105000  |        3,006 |    26,618,130 |
| HIMS     | HIMS270115C00015000  |           754 |        192,270 | HIMS270115P00075000  |        1,512 |     8,860,320 |
| HIMS     | HIMS261120C00004000  |            92 |        112,240 | HIMS270115P00040000  |        3,203 |     7,559,080 |
| IBIT     | IBIT261211C00036000  |         4,902 |        578,436 | IBIT261218P00050000  |       19,283 |    28,635,255 |
| IBIT     | IBIT261127C00037000  |        19,385 |        542,780 | IBIT261120P00048000  |       15,021 |    19,136,754 |
| IBIT     | IBIT261127C00036000  |         7,689 |        438,273 | IBIT261120P00045000  |       15,730 |    15,446,860 |
| IBIT     | IBIT261218C00036000  |         2,994 |        431,136 | IBIT261120P00044000  |        8,946 |     7,979,832 |
| INTC     | INTC261120C00057000  |        26,236 |      2,046,408 | INTC270115P00100000  |       18,017 |    79,635,140 |
| INTC     | INTC261218C00065000  |         8,564 |      1,387,368 | INTC270115P00105000  |       12,424 |    61,126,080 |
| INTC     | INTC261218C00060000  |         4,152 |      1,274,664 | INTC261120P00080000  |       21,486 |    51,630,858 |
| INTC     | INTC270115C00060000  |         2,614 |      1,215,510 | INTC270115P00110000  |        7,938 |    42,944,580 |
| IONQ     | IONQ270115C00030000  |         1,614 |        182,382 | IONQ270115P00120000  |        8,958 |    87,116,550 |
| IONQ     | IONQ261218C00025000  |           497 |         75,544 | IONQ261120P00040000  |        7,751 |    13,292,965 |
| IONQ     | IONQ261204C00024000  |           316 |         42,976 | IONQ261120P00030000  |        9,088 |     6,452,480 |
| IONQ     | IONQ270115C00020000  |            82 |         39,278 | IONQ261120P00035000  |        4,939 |     6,074,970 |
| IREN     | IREN261218C00015000  |         5,231 |        915,425 | IREN261218P00038000  |       15,182 |    35,890,248 |
| IREN     | IREN270115C00017000  |         3,283 |        584,374 | IREN270115P00045000  |        2,820 |     8,615,100 |
| IREN     | IREN270115C00015000  |         2,294 |        573,500 | IREN261120P00020000  |       12,934 |     7,307,710 |
| IREN     | IREN261127C00015000  |         7,108 |        568,640 | IREN261120P00021000  |        4,185 |     2,736,990 |
| MARA     | MARA261218C00006000  |         3,470 |        308,830 | MARA261218P00007000  |        5,069 |       588,004 |
| MARA     | MARA270115C00007000  |         3,517 |        249,707 | MARA261211P00007000  |        4,715 |       509,220 |
| MARA     | MARA270115C00006000  |         1,722 |        191,142 | MARA261120P00007000  |        5,900 |       460,200 |
| MARA     | MARA270115C00008000  |         4,217 |        181,331 | MARA261120P00006500  |       11,864 |       415,240 |
| MRVL     | MRVL261204C00150000  |         2,725 |      1,907,500 | MRVL261120P00200000  |       39,734 |   238,602,670 |
| MRVL     | MRVL261218C00150000  |         1,315 |      1,236,100 | MRVL261120P00195000  |       18,747 |   104,420,790 |
| MRVL     | MRVL261204C00155000  |         1,198 |        712,810 | MRVL261120P00190000  |       10,963 |    54,749,222 |
| MRVL     | MRVL261127C00150000  |         2,114 |        708,190 | MRVL261120P00175000  |       14,639 |    51,792,782 |
| MSTR     | MSTR261127C00040000  |           383 |      1,782,099 | MSTR261120P00120000  |       15,828 |    53,577,780 |
| MSTR     | MSTR261120C00080000  |         1,357 |      1,017,750 | MSTR261120P00130000  |        8,599 |    37,061,690 |
| MSTR     | MSTR261218C00090000  |         1,040 |        772,720 | MSTR270115P00200000  |        2,675 |    30,200,750 |
| MSTR     | MSTR261218C00105000  |         2,516 |        719,576 | MSTR270115P00220000  |        2,227 |    29,663,640 |
| NFLX     | NFLX261120C00002500  |           197 |      1,099,851 | NFLX270115P00100000  |        9,750 |    40,560,000 |
| NFLX     | NFLX270115C00060000  |         2,085 |        612,990 | NFLX270115P00082000  |       11,792 |    27,947,040 |
| NFLX     | NFLX261218C00062000  |         4,601 |        529,115 | NFLX270115P00090000  |        6,761 |    21,229,540 |
| NFLX     | NFLX270115C00061000  |         2,019 |        508,788 | NFLX270115P00079000  |       10,081 |    20,716,455 |
| NVDA     | NVDA261218C00130000  |         8,275 |     16,194,175 | NVDA261120P00200000  |       80,735 |   437,341,495 |
| NVDA     | NVDA261218C00150000  |        21,261 |     14,989,005 | NVDA261120P00205000  |       65,259 |   386,268,021 |
| NVDA     | NVDA261218C00170000  |        66,144 |     10,913,760 | NVDA261120P00215000  |       41,568 |   282,246,720 |
| NVDA     | NVDA261120C00150000  |        91,017 |      9,192,717 | NVDA261120P00220000  |       33,301 |   243,097,300 |
| OKLO     | OKLO261218C00022500  |         1,103 |        161,038 | OKLO261120P00035000  |        7,537 |    10,589,485 |
| OKLO     | OKLO270115C00030000  |           825 |         49,500 | OKLO261120P00030000  |        8,564 |     7,733,292 |
| OKLO     | OKLO270115C00022500  |           220 |         48,400 | OKLO261120P00026500  |        1,009 |       524,680 |
| QCOM     | QCOM270115C00180000  |           597 |        389,244 | QCOM261120P00185000  |          360 |       824,760 |
| QCOM     | QCOM261127C00175000  |         2,495 |        389,220 | QCOM261120P00200000  |          185 |       706,700 |
| QCOM     | QCOM261218C00170000  |           464 |        321,088 | QCOM261120P00167500  |          988 |       661,960 |
| QCOM     | QCOM261120C00150000  |           213 |        273,492 | QCOM261218P00165000  |          464 |       552,160 |
| QQQ      | QQQ261218C00655000   |        16,196 |     31,096,320 | QQQ261120P00710000   |       39,686 |   258,673,348 |
| QQQ      | QQQ270115C00700000   |        24,682 |     21,720,160 | QQQ261120P00705000   |       29,346 |   183,383,154 |
| QQQ      | QQQ261120C00650000   |        41,658 |     18,329,520 | QQQ261120P00725000   |       20,971 |   169,655,390 |
| QQQ      | QQQ261120C00646000   |        16,326 |     10,481,292 | QQQ261120P00720000   |       19,601 |   146,654,682 |
| RIOT     | RIOT261120C00015000  |         4,051 |      1,154,535 | RIOT261120P00019500  |        2,324 |       415,996 |
| RIOT     | RIOT261120C00017500  |        15,498 |        960,876 | RIOT261218P00021000  |        1,001 |       400,400 |
| RIOT     | RIOT261120C00018000  |        21,545 |        797,165 | RIOT261218P00016000  |        1,954 |       220,802 |
| RIOT     | RIOT261127C00020000  |        25,551 |        715,428 | RIOT261204P00018000  |        1,308 |       210,588 |
| RKLB     | RKLB270115C00065000  |         2,665 |        586,300 | RKLB261218P00050000  |        5,487 |     2,370,384 |
| RKLB     | RKLB270115C00070000  |         3,347 |        451,845 | RKLB270115P00150000  |           30 |       297,000 |
| RKLB     | RKLB270115C00050000  |           296 |        207,200 | RKLB261120P00058000  |          409 |       294,480 |
| RKLB     | RKLB270115C00075000  |         1,961 |        192,178 | RKLB261204P00050000  |          895 |       286,400 |
| SLV      | SLV261218C00041000   |         4,307 |        676,199 | SLV270115P00095000   |        6,242 |    34,455,840 |
| SLV      | SLV261218C00040000   |         2,866 |        573,200 | SLV261218P00060000   |       10,900 |    22,345,000 |
| SLV      | SLV270115C00040000   |         1,896 |        530,880 | SLV270115P00070000   |        5,092 |    15,250,540 |
| SLV      | SLV270115C00041000   |         2,066 |        491,708 | SLV270115P00090000   |        1,833 |     9,183,330 |
| SMCI     | SMCI261127C00026500  |        11,544 |        473,304 | SMCI261120P00026000  |        4,913 |     1,090,686 |
| SMCI     | SMCI261127C00026000  |         7,126 |        391,930 | SMCI261120P00025000  |        5,858 |       790,830 |
| SMCI     | SMCI261127C00028500  |        10,615 |        180,455 | SMCI261218P00023000  |        3,179 |       610,368 |
| SMCI     | SMCI261127C00025500  |         2,564 |        179,480 | SMCI261120P00030000  |          625 |       368,750 |
| SMH      | SMH261218C00500000   |         6,246 |      5,215,410 | SMH261120P00530000   |       20,774 |   161,019,274 |
| SMH      | SMH270115C00500000   |         1,596 |      2,394,000 | SMH261120P00540000   |       16,041 |   145,010,640 |
| SMH      | SMH270115C00450000   |           506 |      1,846,900 | SMH261120P00600000   |        9,382 |   139,181,970 |
| SMH      | SMH261127C00450000   |           713 |      1,055,240 | SMH261120P00550000   |       10,291 |   103,218,730 |
| SNDK     | SNDK261218C00800000  |           797 |      5,300,050 | SNDK261120P01450000  |        3,935 |   266,124,050 |
| SNDK     | SNDK261120C00765000  |         2,933 |      5,021,296 | SNDK261120P01150000  |        5,697 |   224,319,375 |
| SNDK     | SNDK261120C00760000  |         1,751 |      3,414,450 | SNDK261120P01250000  |        3,958 |   193,942,000 |
| SNDK     | SNDK261120C00800000  |         5,605 |      3,329,370 | SNDK261120P01200000  |        4,055 |   177,604,945 |
| SPY      | SPY261120C00720000   |        64,412 |     21,255,960 | SPY261125P00734000   |       59,940 |   126,413,460 |
| SPY      | SPY261218C00721000   |        10,647 |     17,716,608 | SPY261120P00750000   |       36,241 |   124,379,112 |
| SPY      | SPY261120C00395000   |           428 |     13,773,896 | SPY261120P00765000   |       12,443 |    61,356,433 |
| SPY      | SPY261218C00725000   |         9,220 |     13,451,980 | SPY261120P00730000   |       43,077 |    60,307,800 |
| TLT      | TLT261218C00082000   |        52,684 |      2,581,516 | TLT261218P00080000   |       28,564 |     3,142,040 |
| TLT      | TLT270115C00088000   |       207,837 |      2,494,044 | TLT261120P00085000   |        4,000 |     1,860,000 |
| TLT      | TLT270115C00080000   |        13,080 |      2,171,280 | TLT261120P00084000   |        4,000 |     1,460,000 |
| TLT      | TLT261120C00080000   |        40,055 |      1,882,585 | TLT270115P00080000   |        8,877 |     1,233,903 |
| TSLA     | TSLA261120C00380000  |        29,659 |      9,461,221 | TSLA261120P00380000  |       31,877 |    26,617,295 |
| TSLA     | TSLA261120C00175000  |           417 |      8,320,401 | TSLA261120P00390000  |       13,078 |    21,055,580 |
| TSLA     | TSLA261218C00175000  |           400 |      8,007,200 | TSLA261120P00385000  |       15,255 |    18,306,000 |
| TSLA     | TSLA261120C00390000  |        79,088 |      6,643,392 | TSLA261120P00375000  |       25,624 |    14,990,040 |
| TSM      | TSM261218C00360000   |         1,136 |      2,027,760 | TSM261120P00450000   |        2,702 |    25,263,700 |
| TSM      | TSM261127C00372500   |         3,369 |      1,408,242 | TSM261120P00410000   |        2,851 |    16,122,405 |
| TSM      | TSM261127C00365000   |         1,821 |      1,192,755 | TSM261120P00470000   |        1,200 |    13,632,000 |
| TSM      | TSM261127C00360000   |         1,328 |      1,111,536 | TSM261120P00430000   |        1,017 |     7,469,865 |
| UNH      | UNH261218C00300000   |         1,838 |      6,671,940 | UNH261120P00400000   |       19,635 |   132,143,550 |
| UNH      | UNH261120C00150000   |           174 |      3,173,934 | UNH261120P00420000   |       11,012 |    96,255,892 |
| UNH      | UNH261120C00135000   |            91 |      1,781,780 | UNH261120P00390000   |        6,683 |    39,957,657 |
| UNH      | UNH261120C00130000   |            69 |      1,385,382 | UNH261120P00410000   |        1,654 |    12,980,592 |
| WULF     | WULF270115C00015000  |         6,266 |        457,418 | WULF261120P00016000  |        4,012 |     1,825,460 |
| WULF     | WULF261218C00013000  |         4,321 |        345,680 | WULF261120P00015000  |        4,935 |     1,727,250 |
| WULF     | WULF261120C00012000  |        12,340 |        234,460 | WULF261218P00011000  |        9,200 |       966,000 |
| WULF     | WULF270115C00013000  |         1,151 |        147,328 | WULF261120P00017000  |          884 |       490,620 |
| XLF      | XLF261218C00056000   |        10,635 |      1,350,645 | XLF261218P00057000   |       14,186 |     2,851,386 |
| XLF      | XLF261120C00056000   |        27,582 |        524,058 | XLF261120P00058000   |        5,620 |     1,320,700 |
| XLF      | XLF261218C00057000   |         6,276 |        470,700 | XLF261218P00054000   |       17,488 |     1,259,136 |
| XLF      | XLF261218C00038000   |           134 |        243,210 | XLF261120P00056000   |       17,781 |     1,066,860 |
| XLU      | XLU261218C00044000   |         9,433 |        433,918 | XLU270115P00040500   |        7,476 |       239,232 |
| XLU      | XLU261218C00040500   |         1,510 |        424,310 | XLU270115P00043500   |          624 |        86,112 |
| ^VIX     | VIX261216C00022000   |        21,910 |      9,202,200 | VIX261216P00018000   |      190,063 |     5,701,890 |
| ^VIX     | VIX261216C00065000   |       103,387 |      5,065,963 | VIX261216P00019000   |       66,664 |     3,866,512 |
| ^VIX     | VIX261216C00023000   |        10,028 |      4,011,200 | VIX261216P00024000   |        7,941 |     2,302,890 |
| ^VIX     | VIX261216C00027000   |        12,042 |      3,203,172 | VIX261216P00017000   |      151,129 |     2,266,935 |

## T3 — Top 3 OTM Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261120C00350000  |        33,034 |      7,234,446 | AAPL261120P00347500  |       36,418 |     6,919,420 |
| AAPL     | AAPL270115C00350000  |         3,912 |      5,594,160 | AAPL261218P00330000  |       16,208 |     5,996,960 |
| AAPL     | AAPL261231C00355000  |         4,961 |      4,658,379 | AAPL261120P00345000  |       46,366 |     5,378,456 |
| AMZN     | AMZN261218C00260000  |         9,978 |     10,187,538 | AMZN261120P00255000  |       15,988 |     3,741,192 |
| AMZN     | AMZN270115C00270000  |         8,714 |      8,496,150 | AMZN261127P00250000  |        6,222 |     2,084,370 |
| AMZN     | AMZN261218C00275000  |         8,415 |      3,618,450 | AMZN261218P00240000  |        4,350 |     2,022,750 |
| AVGO     | AVGO270115C00400000  |         3,325 |      3,840,375 | AVGO261120P00340000  |       14,012 |     5,268,512 |
| AVGO     | AVGO261218C00350000  |         1,542 |      3,693,090 | AVGO261218P00320000  |        2,673 |     3,688,740 |
| AVGO     | AVGO261218C00360000  |         1,793 |      3,444,353 | AVGO261218P00340000  |        1,752 |     3,663,432 |
| GLD      | GLD270115C00340000   |         2,471 |      3,026,975 | GLD261218P00335000   |        2,391 |     2,247,540 |
| GLD      | GLD270115C00350000   |           953 |        771,930 | GLD261120P00335000   |        5,594 |     1,241,868 |
| GLD      | GLD270115C00345000   |           734 |        726,660 | GLD261218P00325000   |        2,088 |     1,160,928 |
| GOOGL    | GOOGL261218C00300000 |        13,507 |      3,579,355 | GOOGL261218P00270000 |        2,231 |     2,242,155 |
| GOOGL    | GOOGL270115C00300000 |         5,571 |      3,147,615 | GOOGL261120P00272500 |        4,437 |     1,419,840 |
| GOOGL    | GOOGL270115C00280000 |         1,392 |      1,753,920 | GOOGL261120P00270000 |        6,032 |     1,266,720 |
| INTC     | INTC261120C00057000  |        26,236 |      2,046,408 | INTC261127P00055000  |        8,834 |     2,031,820 |
| INTC     | INTC261218C00065000  |         8,564 |      1,387,368 | INTC261120P00055000  |       19,614 |     1,882,944 |
| INTC     | INTC261218C00060000  |         4,152 |      1,274,664 | INTC261127P00053000  |        7,744 |     1,246,784 |
| MRVL     | MRVL261204C00150000  |         2,725 |      1,907,500 | MRVL261218P00130000  |          569 |       584,363 |
| MRVL     | MRVL261218C00150000  |         1,315 |      1,236,100 | MRVL270115P00130000  |          334 |       435,202 |
| MRVL     | MRVL261204C00155000  |         1,198 |        712,810 | MRVL261218P00135000  |          361 |       433,200 |
| MSTR     | MSTR261218C00090000  |         1,040 |        772,720 | MSTR261218P00085000  |        2,785 |     2,353,325 |
| MSTR     | MSTR261218C00105000  |         2,516 |        719,576 | MSTR261120P00085000  |        7,760 |     1,451,120 |
| MSTR     | MSTR261127C00090000  |         1,960 |        617,400 | MSTR261127P00085000  |        3,279 |     1,406,691 |
| NFLX     | NFLX270115C00060000  |         2,085 |        612,990 | NFLX261218P00056000  |       43,158 |     6,128,436 |
| NFLX     | NFLX261218C00062000  |         4,601 |        529,115 | NFLX261218P00055000  |        5,617 |       612,253 |
| NFLX     | NFLX270115C00061000  |         2,019 |        508,788 | NFLX261218P00057000  |        1,702 |       287,638 |
| NVDA     | NVDA261218C00150000  |        21,261 |     14,989,005 | NVDA261120P00145000  |       91,259 |    19,073,131 |
| NVDA     | NVDA261218C00170000  |        66,144 |     10,913,760 | NVDA261123P00145000  |       21,844 |     7,208,520 |
| NVDA     | NVDA261120C00150000  |        91,017 |      9,192,717 | NVDA261218P00145000  |        7,659 |     6,257,403 |
| QCOM     | QCOM270115C00180000  |           597 |        389,244 | QCOM261218P00160000  |          199 |       190,045 |
| QCOM     | QCOM261127C00175000  |         2,495 |        389,220 | QCOM261120P00160000  |          883 |       187,196 |
| QCOM     | QCOM261218C00170000  |           464 |        321,088 | QCOM261127P00145000  |        1,444 |       164,616 |
| QQQ      | QQQ261218C00655000   |        16,196 |     31,096,320 | QQQ261120P00640000   |       75,328 |    36,232,768 |
| QQQ      | QQQ270115C00700000   |        24,682 |     21,720,160 | QQQ261120P00645000   |       45,833 |    30,478,945 |
| QQQ      | QQQ261120C00650000   |        41,658 |     18,329,520 | QQQ261218P00620000   |       17,951 |    24,987,792 |
| SLV      | SLV261218C00041000   |         4,307 |        676,199 | SLV261218P00035000   |        8,755 |       560,320 |
| SLV      | SLV261218C00040000   |         2,866 |        573,200 | SLV261218P00039000   |        2,756 |       496,080 |
| SLV      | SLV270115C00040000   |         1,896 |        530,880 | SLV261218P00030000   |       11,535 |       161,490 |
| SMCI     | SMCI261127C00026500  |        11,544 |        473,304 | SMCI261218P00023000  |        3,179 |       610,368 |
| SMCI     | SMCI261127C00026000  |         7,126 |        391,930 | SMCI270115P00019000  |        1,885 |       209,235 |
| SMH      | SMH261218C00500000   |         6,246 |      5,215,410 | SMH270115P00400000   |        5,226 |     9,145,500 |
| SMH      | SMH270115C00500000   |         1,596 |      2,394,000 | SMH261218P00390000   |        5,161 |     4,748,120 |
| SMH      | SMH270115C00450000   |           506 |      1,846,900 | SMH270115P00370000   |        3,511 |     3,493,445 |
| SNDK     | SNDK261218C00800000  |           797 |      5,300,050 | SNDK261218P00080000  |        2,500 |        12,500 |
| SNDK     | SNDK261120C00765000  |         2,933 |      5,021,296 | SNDK261218P00085000  |        1,500 |         7,500 |
| SNDK     | SNDK261120C00760000  |         1,751 |      3,414,450 | SNDK261218P00090000  |            9 |            45 |
| SPY      | SPY261120C00720000   |        64,412 |     21,255,960 | SPY261218P00700000   |       45,638 |    59,694,504 |
| SPY      | SPY261218C00721000   |        10,647 |     17,716,608 | SPY261120P00715000   |      105,660 |    46,701,720 |
| SPY      | SPY261218C00725000   |         9,220 |     13,451,980 | SPY261120P00710000   |      125,306 |    35,085,680 |
| TLT      | TLT261218C00082000   |        52,684 |      2,581,516 | TLT261218P00080000   |       28,564 |     3,142,040 |
| TLT      | TLT270115C00088000   |       207,837 |      2,494,044 | TLT270115P00080000   |        8,877 |     1,233,903 |
| TLT      | TLT270115C00082000   |        20,843 |      1,813,341 | TLT270115P00076000   |       13,172 |       316,128 |
| TSLA     | TSLA261120C00380000  |        29,659 |      9,461,221 | TSLA261120P00370000  |       23,144 |     8,794,720 |
| TSLA     | TSLA261120C00390000  |        79,088 |      6,643,392 | TSLA261120P00372500  |       14,581 |     6,925,975 |
| TSLA     | TSLA261127C00380000  |         7,176 |      6,207,240 | TSLA261120P00365000  |       12,870 |     3,088,800 |
| TSM      | TSM261218C00360000   |         1,136 |      2,027,760 | TSM261218P00350000   |          925 |     1,752,875 |
| TSM      | TSM261127C00372500   |         3,369 |      1,408,242 | TSM270115P00350000   |          555 |     1,311,465 |
| TSM      | TSM261127C00365000   |         1,821 |      1,192,755 | TSM261120P00350000   |        1,770 |       897,390 |
| UNH      | UNH270115C00370000   |         1,945 |      1,328,435 | UNH261120P00330000   |       16,776 |     6,878,160 |
| UNH      | UNH261218C00370000   |         3,264 |      1,047,744 | UNH261120P00325000   |        6,876 |     1,691,496 |
| UNH      | UNH261120C00340000   |         4,793 |        647,055 | UNH261120P00320000   |        8,424 |     1,086,696 |
| WULF     | WULF270115C00015000  |         6,266 |        457,418 | WULF261218P00011000  |        9,200 |       966,000 |
| WULF     | WULF261218C00013000  |         4,321 |        345,680 | WULF261211P00011500  |        3,075 |       344,400 |
| WULF     | WULF261120C00012000  |        12,340 |        234,460 | WULF261218P00010000  |        4,661 |       312,287 |
| XLF      | XLF261218C00056000   |        10,635 |      1,350,645 | XLF261218P00054000   |       17,488 |     1,259,136 |
| XLF      | XLF261120C00056000   |        27,582 |        524,058 | XLF270115P00054000   |        4,612 |       521,156 |
| XLF      | XLF261218C00057000   |         6,276 |        470,700 | XLF261218P00055000   |        4,182 |       434,928 |
| XLU      | XLU261218C00044000   |         9,433 |        433,918 | XLU270115P00040500   |        7,476 |       239,232 |
| ^VIX     | VIX261216C00065000   |       103,387 |      5,065,963 | VIX261216P00018000   |      190,063 |     5,701,890 |
| ^VIX     | VIXW261124C00030000  |        14,004 |      1,428,408 | VIX261216P00019000   |       66,664 |     3,866,512 |
| ^VIX     | VIX261216C00080000   |        12,185 |        402,105 | VIX261216P00024000   |        7,941 |     2,302,890 |

*premium = volume × lastPrice × 100 · OTM = calls strike>spot, puts strike<spot · T4 uses the cleaned chain: ≥2 DTE, OTM only, leveraged ETFs folded into their underlying, ^VIX ratio inverted · Net Signed Premium = bought calls/sold puts minus sold calls/bought puts, side from lastPrice vs bid/ask (prints outside the closing quote are not signed) · generated by options-flow-pipeline*

---

**Data quality:** requested: 52 · fetched: 52 · failed: 0 · gated: 9 · stale volume: 21,275 contracts (11% of premium) dropped

_Signal check (next-day rank correlation, last 20 sessions): composite IC +0.071 (t +1.3, n=20) · flow_pct IC -0.052 (t -1.1, n=20) · trend_pct IC +0.128 (t +2.0, n=20)_

_Signal check, next 5 sessions (rank correlation, last 20 resolved sessions; windows overlap, so t is overstated): composite IC -0.008 (t -0.2, n=20) · flow_pct IC -0.156 (t -4.9, n=20) · trend_pct IC +0.114 (t +2.5, n=20)_