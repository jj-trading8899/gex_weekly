# Options Flow Report (v1.3) — 2026-11-24

**Run stats:** 52/52 tickers fetched · 0 failed · 59,812 contracts

## Market Regime

**risk-off · backwardation (VIX/VIX3M=1.03, DoD -0.01) · negative gamma (moves amplified) · high vol · choppy/rangebound — momentum tilted**

`Vol: HIGH · Trend: CHOP · Risk: RISK_OFF · Gamma: NEGATIVE · SPY GEX: $-7,625M`

_Pipeline knobs: mom×0.85 · conviction≥0.88_

## Master Scoreboard (all tickers by composite)

| Rank   | Ticker   | Composite   | Trend%   | Mom%   | Flow%   | Rot%   | Conviction   | ΔRank   |
|:-------|:---------|:------------|:---------|:-------|:--------|:-------|:-------------|:--------|
| 1      | XLV      | 100.0       | 100      | 86     | N/A     | 100    | NEUTRAL      | 0       |
| 2      | XLE      | 98.4        | 98       | 90     | N/A     | 90     | CONFIRMED    | +1      |
| 3      | XLP      | 96.7        | 97       | 85     | N/A     | 92     | NEUTRAL      | -1      |
| 4      | BIL      | 91.8        | 92       | 68     | N/A     | 87     | NEUTRAL      | +2      |
| 5      | XLB      | 90.2        | 90       | 77     | N/A     | 77     | NEUTRAL      | 0       |
| 6      | XLRE     | 88.5        | 89       | 71     | N/A     | 82     | NEUTRAL      | +4      |
| 7      | XLY      | 83.6        | 84       | 65     | N/A     | 83     | NEUTRAL      | +1      |
| 8      | AI       | 83.0        | 66       | 60     | 98      | 68     | NEUTRAL      | -1      |
| 9      | SNDK     | 82.0        | 82       | 76     | N/A     | 72     | NEUTRAL      | 0       |
| 10     | XLK      | 77.0        | 77       | 81     | N/A     | 63     | NEUTRAL      | -6      |
| 11     | UNH      | 71.2        | 85       | 78     | 59      | 71     | NEUTRAL      | +26     |
| 12     | TSLA     | 68.0        | 75       | 58     | 62      | 83     | NEUTRAL      | +11     |
| 13     | IWM      | 67.2        | 67       | 65     | N/A     | 66     | NEUTRAL      | +5      |
| 14     | RIOT     | 66.5        | 48       | 44     | 83      | 51     | NEUTRAL      | +7      |
| 15     | INTC     | 65.8        | 56       | 69     | 74      | 46     | NEUTRAL      | +9      |
| 16     | AAPL     | 64.8        | 95       | 78     | 39      | 98     | NEUTRAL      | +3      |
| 17     | AMZN     | 64.3        | 80       | 63     | 51      | 84     | NEUTRAL      | -6      |
| 18     | HIMS     | 64.1        | 30       | 37     | 93      | 24     | CONFLICT     | +41     |
| 19     | SMCI     | 62.8        | 36       | 51     | 85      | 30     | CONFLICT     | -4      |
| 20     | HIVE     | 60.8        | 15       | 18     | 100     | 14     | CONFLICT     | 0       |
| 21     | XLI      | 60.7        | 61       | 62     | N/A     | 62     | NEUTRAL      | +5      |
| 22     | QCOM     | 59.8        | 69       | 55     | 52      | 76     | NEUTRAL      | -10     |
| 23     | LQD      | 59.0        | 59       | 49     | N/A     | 72     | NEUTRAL      | -1      |
| 24     | HYG      | 57.4        | 57       | 48     | N/A     | 73     | NEUTRAL      | +1      |
| 25     | WULF     | 56.8        | 33       | 41     | 77      | 29     | CONFLICT     | +13     |
| 26     | MRVL     | 56.3        | 79       | 79     | 37      | 68     | NEUTRAL      | -13     |
| 27     | CLSK     | 54.5        | 16       | 25     | 87      | 12     | CONFLICT     | +5      |
| 28     | SMR      | 54.0        | 5        | 6      | 96      | 4      | CONFLICT     | +1      |
| 29     | CIFR     | 53.5        | 11       | 17     | 89      | 5      | CONFLICT     | +2      |
| 30     | CPER     | 52.5        | 52       | 62     | N/A     | 50     | NEUTRAL      | +6      |
| 31     | NFLX     | 51.6        | 23       | 15     | 76      | 36     | CONFLICT     | +20     |
| 32     | GOOGL    | 50.5        | 44       | 41     | 56      | 47     | NEUTRAL      | +3      |
| 33     | SPY      | 50.1        | 87       | 69     | 19      | 80     | CONFLICT     | +11     |
| 34     | NVDA     | 50.1        | 54       | 74     | 47      | 41     | NEUTRAL      | -6      |
| 35     | XLC      | 49.2        | 49       | 43     | N/A     | 59     | NEUTRAL      | +5      |
| 36     | SLV      | 47.9        | 31       | 35     | 62      | 27     | NEUTRAL      | +5      |
| 37     | OKLO     | 47.2        | 8        | 7      | 80      | 11     | CONFLICT     | -3      |
| 38     | QQQ      | 46.6        | 70       | 69     | 26      | 63     | CONFLICT     | +9      |
| 39     | MARA     | 46.6        | 18       | 23     | 71      | 18     | CONFLICT     | +9      |
| 40     | TLT      | 44.2        | 64       | 54     | 27      | 71     | CONFLICT     | +10     |
| 41     | XLF      | 43.3        | 93       | 77     | 1       | 85     | CONFLICT     | +2      |
| 42     | RKLB     | 42.8        | 38       | 46     | 47      | 36     | NEUTRAL      | -15     |
| 43     | TSM      | 41.7        | 74       | 81     | 15      | 57     | CONFLICT     | -29     |
| 44     | GOOG     | 41.7        | 41       | 40     | 42      | 46     | NEUTRAL      | -28     |
| 45     | COIN     | 41.6        | 26       | 30     | 55      | 23     | NEUTRAL      | +7      |
| 46     | BABA     | 39.5        | 25       | 19     | 52      | 34     | NEUTRAL      | -13     |
| 47     | AVGO     | 38.4        | 46       | 39     | 32      | 49     | NEUTRAL      | +9      |
| 48     | ARM      | 38.4        | 51       | 66     | 28      | 44     | NEUTRAL      | -31     |
| 49     | OPEN     | 38.4        | 2        | 3      | 70      | 2      | CONFLICT     | -10     |
| 50     | RGTI     | 37.8        | 13       | 14     | 59      | 13     | NEUTRAL      | +10     |
| 51     | XLU      | 35.5        | 72       | 60     | 4       | 77     | CONFLICT     | -6      |
| 52     | SMH      | 34.9        | 62       | 72     | 12      | 52     | CONFLICT     | -6      |
| 53     | IBIT     | 34.2        | 39       | 45     | 30      | 40     | NEUTRAL      | +1      |
| 54     | MSTR     | 33.6        | 28       | 35     | 38      | 26     | NEUTRAL      | +7      |
| 55     | IONQ     | 33.2        | 20       | 24     | 45      | 21     | NEUTRAL      | -2      |
| 56     | ETHA     | 32.5        | 43       | 50     | 24      | 37     | NEUTRAL      | +1      |
| 57     | IREN     | 28.7        | 10       | 17     | 45      | 3      | NEUTRAL      | -2      |
| 58     | GLD      | 26.9        | 34       | 33     | 20      | 43     | NEUTRAL      | -9      |
| 59     | QBTS     | 25.3        | 7        | 10     | 41      | 8      | NEUTRAL      | -17     |
| 60     | CRWV     | 20.5        | 21       | 29     | 20      | 18     | NEUTRAL      | -2      |
| 61     | EOSE     | 19.1        | 3        | 7      | 33      | 2      | NEUTRAL      | -31     |
| N/A    | AAPX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDU     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | TSLL     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^GSPC    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^SKEW    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX     | N/A         | N/A      | N/A    | 40      | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX3M   | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VVIX    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |

## Sector Rotation / Relative Strength (top 15)

| Ticker   |   RS Rating |   Rel Str 63d | RS New-High   | Dual-Mom   |
|:---------|------------:|--------------:|:--------------|:-----------|
| AAPL     |          99 |          19   | No            | above cash |
| XLV      |          97 |          12.8 | Yes           | above cash |
| SNDK     |          96 |         -46.7 | No            | above cash |
| XLE      |          94 |           3.3 | No            | above cash |
| XLP      |          92 |          13.1 | No            | above cash |
| XLF      |          91 |           2.6 | No            | above cash |
| AMZN     |          89 |           2.9 | No            | above cash |
| BIL      |          88 |           6.9 | No            | below cash |
| MRVL     |          86 |         -40.4 | No            | above cash |
| XLRE     |          84 |           3.1 | No            | above cash |
| XLY      |          83 |           6.6 | No            | above cash |
| XLB      |          81 |          -0.1 | No            | above cash |
| TSLA     |          79 |          17.2 | No            | below cash |
| SPY      |          78 |           0   | Yes           | above cash |
| UNH      |          76 |          -8.3 | No            | above cash |

## Option Skew — Extremes (top/bottom 8)

_Board-wide: protection demand rising across the board (typical name z +1.3 vs its own norm; 22 of 33 names at z +1 or more, 1 at −1 or less). Hedging arrows are measured net of this move._

| Ticker   | Group    | Tilt        |   Skew25 (vol pts) | 90-110   |   ATM IV % |   Skew/IV | Hedging            |    z | Flow        | Positioning   |
|:---------|:---------|:------------|-------------------:|:---------|-----------:|----------:|:-------------------|-----:|:------------|:--------------|
| SPY      | top 8    | put-skewed  |                8.6 | 16.2     |       21.7 |      0.4  | steady →           | -0.6 | Neutral -4  |               |
| QQQ      | top 8    | put-skewed  |               10.1 | 15.6     |       32.1 |      0.31 | steady →           | -0.4 | Neutral -3  |               |
| AAPL     | top 8    | put-skewed  |                6.3 | 13.0     |       23.5 |      0.27 | steady →           |  0.2 | Neutral -4  |               |
| IBIT     | top 8    | put-skewed  |                9.5 | 9.9      |       52.1 |      0.18 | steady →           |  0   | Bull +34    |               |
| TSLA     | top 8    | put-skewed  |                9.3 | 9.8      |       52.7 |      0.18 | steady →           | -0.4 | Neutral -4  |               |
| AMZN     | top 8    | put-skewed  |                6.6 | 9.3      |       38.3 |      0.17 | steady →           | -0.3 | Neutral +0  |               |
| TSM      | top 8    | put-skewed  |               10   | 8.6      |       58.6 |      0.17 | steady →           | -0.4 | Neutral -18 |               |
| IREN     | top 8    | put-skewed  |               22.1 | 9.8      |      131.1 |      0.17 | steady →           |  0.6 | Neutral -2  |               |
| TLT      | bottom 8 | call-skewed |               -0.7 | N/A      |       11.6 |     -0.06 | hedging easing ↓   | -2.6 | Neutral +13 |               |
| BABA     | bottom 8 | put-skewed  |                3.5 | 4.9      |       45.9 |      0.08 | steady →           | -0   | Neutral -4  |               |
| HIMS     | bottom 8 | put-skewed  |                7.8 | 6.1      |       86.7 |      0.09 | hedging building ↑ |  1.3 | Neutral +13 |               |
| NFLX     | bottom 8 | put-skewed  |                4   | 5.2      |       36.4 |      0.11 | steady →           |  0.5 | Neutral -5  |               |
| MARA     | bottom 8 | put-skewed  |               12.9 | 5.5      |      111.2 |      0.12 | steady →           | -0.2 | Bull +26    |               |
| INTC     | bottom 8 | put-skewed  |               10   | 7.4      |       83.7 |      0.12 | steady →           | -0.4 | Neutral +14 |               |
| ARM      | bottom 8 | put-skewed  |               11.3 | 7.7      |       94   |      0.12 | steady →           | -0.4 | Neutral -11 |               |
| MRVL     | bottom 8 | put-skewed  |               12.2 | 7.3      |       99.3 |      0.12 | steady →           | -0.1 | Neutral +16 |               |

_33 of 52 tickers had a fittable smile. Skew25 = how much more an out-of-the-money put costs than the matching out-of-the-money call, in vol points, at a constant 30-day tenor, re-derived from bid/ask mids (Yahoo's own IV field is not used). Positive = puts richer, the normal state — so read the *ranking*, not the level. Tilt is by sign: call-skewed = Skew/IV below 0; least put-skewed = 0 to 0.02; put-skewed above. Hedging = tonight's Skew/IV against the name's own previous 20 sessions (z = standard deviations from that average), net of the typical name's move tonight (the Board-wide line above): building when z is at least +1, easing at −1 or below, else steady; n/a until 10 prior sessions exist. It describes protection demand, not a price forecast._

## Mega-Cap Tech Skew

| Ticker   | Skew25 (vol pts)   |   90-110 |   ATM IV % | Skew/IV   | Rank     | Read                | Hedging              |    z | Flow       | Positioning   |
|:---------|:-------------------|---------:|-----------:|:----------|:---------|:--------------------|:---------------------|-----:|:-----------|:--------------|
| NVDA     | N/A                |      7   |       63.2 | N/A       | N/A      | put-skewed (90-110) | n/a (no fit tonight) |      | Neutral +4 |               |
| AAPL     | 6.3                |     13   |       23.5 | 0.27      | 3 of 33  | steep put skew      | steady →             |  0.2 | Neutral -4 |               |
| AMZN     | 6.6                |      9.3 |       38.3 | 0.17      | 6 of 33  | steep put skew      | steady →             | -0.3 | Neutral +0 |               |
| GOOGL    | 6.3                |      8.4 |       38   | 0.17      | 10 of 33 | put-skewed          | steady →             |  0   | Neutral +5 |               |
| TSLA     | 9.3                |      9.8 |       52.7 | 0.18      | 5 of 33  | steep put skew      | steady →             | -0.4 | Neutral -4 |               |
| AVGO     | 11.7               |      9.5 |       71.9 | 0.16      | 11 of 33 | put-skewed          | steady →             | -0   | Neutral -1 |               |

_Mega-cap tech: 5 of 6 fitted · median Skew/IV 0.17 vs 0.14 for the other names · richer downside protection than the rest of the board · steepest: AAPL, AMZN, TSLA._

_Flow = premium-weighted flow score: 100 × (bought calls + sold puts − sold calls − bought puts) ÷ total out-of-the-money premium, sides estimated from the last trade against bid/ask (a last trade outside the closing quote is left unsigned); Bull at +20 or more, Bear at −20 or less. Positioning: defensive = hedging building with Bear flow; speculative = hedging easing with Bull flow; blank otherwise. Positioning describes what is being hedged and flowed tonight. It is not a price forecast._

## Stretch & Reversal Watch (experimental)

| Watch             | Tonight      | Backtest (before live)                                       | Live since 2026-11-06                                               |
|:------------------|:-------------|:-------------------------------------------------------------|:--------------------------------------------------------------------|
| hedging unwinding | TLT (z -2.6) | 194 flags · +1.6% vs avg name · 59% beat it                  | 9 flags · +3.7% vs avg name · 56% beat it                           |
| stretched up      | none         | 597 flags · -1.5% vs avg name · 41% beat it                  | 66 flags · -2.9% vs avg name · 45% beat it                          |
| washed out        | none         | 118 flags · -0.1% vs avg name · 57% beat it (no edge so far) | 17 flags · +2.3% vs avg name · 71% beat it                          |
| puts closing      | none         | 821 flags · +0.7% vs avg name · 55% beat it (to 2026-11-16)  | 1 flags · -297.8% vs avg name · 0% beat it (counts from 2026-11-16) |

_Experimental, not proven. Hedging unwinding = tonight's Skew/IV at z -1.5 or lower against the name's own norm, net of the board (as the Hedging column): protection being sold off. Stretched up = price up 5% or more over the last 5 sessions. Washed out = down 5% or more with hedging at z +2 or more on its own norm. Puts closing = the fifth of names where puts made up most of the out-of-the-money positions closed in the previous session (volume matched against the drop in open interest): protection taken off. The record columns score each past flag 5 sessions later against the average name that night (prices from the option chains' implied forwards). The backtest is in-sample: the thresholds were picked on that same history, so it flatters the flags; the live column counts only flags raised since this block was added and is the one that matters. If the live record does not hold up, the block goes. Not a price forecast._

---

# Flow Detail

## T4 — OTM Flow Summary (ranked by OTM Call/Put premium ratio)

|   Rank | Ticker   |   Premium Ratio |   Premium Ratio All |   Total Call Premium |   Total Put Premium |   Net Signed Premium |   Close Price | 1-Day Return   | 1-Week Return   | % Close to MA20   | % Close to MA50   | % Close to High   | % Close to Low   |   52 Week High |   52 Week Low |   MA20 |   MA50 |
|-------:|:---------|----------------:|--------------------:|---------------------:|--------------------:|---------------------:|--------------:|:---------------|:----------------|:------------------|:------------------|:------------------|:-----------------|---------------:|--------------:|-------:|-------:|
|      1 | NFLX     |            3.23 |                0.06 |            6,141,243 |           1,901,138 |             -397,931 |         58.87 | 1.33%          | -5.28%          | -4.76%            | -11.58%           | -46.35%           | 4.08%            |         109.73 |         56.56 |  61.81 |  66.58 |
|      2 | CLSK     |            2.87 |                1.8  |              517,797 |             180,389 |              365,072 |          5.11 | -7.50%         | -23.08%         | -22.68%           | -45.90%           | -73.32%           | 5.79%            |          19.17 |          4.84 |   6.62 |   9.45 |
|      3 | SMCI     |            2.86 |                2.65 |            8,102,068 |           2,831,699 |              553,368 |         22.62 | -7.79%         | -15.82%         | -18.83%           | -34.41%           | -55.99%           | 16.12%           |          51.4  |         19.48 |  27.87 |  34.49 |
|      4 | WULF     |            2.57 |                1.08 |            4,614,770 |           1,798,536 |              514,360 |         10.01 | -8.25%         | -20.68%         | -15.31%           | -24.39%           | -66.45%           | 8.22%            |          29.84 |          9.25 |  11.82 |  13.24 |
|      5 | RIOT     |            2.52 |                1.98 |           13,246,993 |           5,266,737 |            1,480,023 |         16.34 | -4.72%         | -6.74%          | 1.22%             | -6.41%            | -46.11%           | 42.09%           |          30.32 |         11.5  |  16.14 |  17.46 |
|      6 | INTC     |            2.17 |                0.11 |           22,104,299 |          10,178,418 |            4,624,689 |         54.8  | -8.15%         | -8.15%          | -10.77%           | -38.17%           | -61.50%           | 58.02%           |         142.35 |         34.68 |  61.42 |  88.63 |
|      7 | SLV      |            2.1  |                0.02 |            5,314,847 |           2,529,462 |            1,443,716 |         36.84 | -5.32%         | -16.52%         | -16.36%           | -26.67%           | -66.46%           | 0.35%            |         109.83 |         36.71 |  44.05 |  50.24 |
|      8 | UNH      |            1.97 |                0.55 |            7,209,357 |           3,660,704 |            1,297,240 |        341.88 | 1.73%          | -16.09%         | -11.74%           | -11.67%           | -25.94%           | 33.56%           |         461.62 |        255.97 | 387.36 | 387.07 |
|      9 | QCOM     |            1.79 |                1.18 |            3,620,739 |           2,023,724 |              329,431 |        164.96 | -0.25%         | -4.35%          | -1.91%            | -6.57%            | -36.53%           | 35.22%           |         259.92 |        121.99 | 168.18 | 176.56 |
|     10 | GOOGL    |            1.77 |                0.26 |           20,410,899 |          11,525,504 |            1,642,528 |        279.05 | -1.08%         | -5.65%          | -2.31%            | -12.70%           | -31.71%           | 5.61%            |         408.61 |        264.22 | 285.64 | 319.64 |
|     10 | BABA     |            1.77 |                2.32 |            2,705,309 |           1,526,858 |             -182,924 |         84.86 | -1.37%         | -10.09%         | -11.54%           | -17.91%           | -53.14%           | 4.82%            |         181.1  |         80.96 |  95.92 | 103.38 |
|     12 | TSLA     |            1.66 |                1.58 |          106,594,699 |          64,298,652 |           -6,542,582 |        384.68 | -0.20%         | -1.42%          | 0.35%             | 2.11%             | -22.88%           | 29.36%           |         498.83 |        297.38 | 383.35 | 376.73 |
|     13 | COIN     |            1.63 |                0.01 |            4,374,825 |           2,690,474 |              774,093 |        102.35 | -5.91%         | -19.82%         | -21.36%           | -36.33%           | -64.05%           | 0.63%            |         284.74 |        101.71 | 130.15 | 160.74 |
|     14 | AMZN     |            1.59 |                0.75 |           29,928,023 |          18,878,001 |               92,950 |        252.29 | -1.21%         | -5.39%          | -2.10%            | -1.12%            | -12.16%           | 28.72%           |         287.2  |        196    | 257.7  | 255.15 |
|     15 | GOOG     |            1.45 |                0.38 |           15,723,691 |          10,820,650 |           -1,790,231 |        276.58 | -1.06%         | -5.45%          | -2.45%            | -12.66%           | -31.62%           | 5.46%            |         404.47 |        262.27 | 283.52 | 316.65 |
|     16 | IREN     |            1.41 |                0.47 |            6,488,931 |           4,604,102 |             -175,750 |         12.95 | -11.54%        | -28.73%         | -33.21%           | -56.67%           | -81.68%           | 10.21%           |          70.71 |         11.75 |  19.39 |  29.89 |
|     17 | RKLB     |            1.35 |                0.04 |            3,437,348 |           2,545,327 |              332,756 |         45.98 | -7.35%         | -25.27%         | -16.49%           | -24.29%           | -69.55%           | 15.01%           |         151    |         39.98 |  55.06 |  60.73 |
|     18 | ^VIX     |            1.31 |                1.25 |           23,409,793 |          30,564,324 |           -4,528,431 |         26.36 | -0.98%         | 36.58%          | 16.88%            | 40.15%            | -34.15%           | 97.01%           |          40.03 |         13.38 |  22.55 |  18.81 |
|     19 | MRVL     |            1.19 |                0.61 |           14,089,662 |          11,811,044 |            4,024,994 |        131.57 | -9.10%         | -16.07%         | -18.28%           | -39.37%           | -60.12%           | 86.12%           |         329.88 |         70.69 | 161    | 216.99 |
|     20 | NVDA     |            1.15 |                1.5  |          266,474,413 |         231,349,253 |           18,819,419 |        155.38 | -5.86%         | -4.59%          | -11.61%           | -24.19%           | -36.15%           | 24.80%           |         243.37 |        124.5  | 175.78 | 204.95 |
|     21 | ARM      |            1.05 |                0.06 |            7,275,995 |           6,919,428 |           -1,577,001 |        161.56 | -8.55%         | -15.20%         | -14.37%           | -31.76%           | -64.31%           | 61.53%           |         452.7  |        100.02 | 188.67 | 236.77 |
|     22 | MSTR     |            1.04 |                0.3  |           18,659,692 |          17,862,390 |           -1,621,097 |         77.55 | -8.12%         | -30.52%         | -32.42%           | -43.32%           | -60.91%           | 0.30%            |         198.4  |         77.32 | 114.76 | 136.82 |
|     23 | AAPL     |            0.93 |                1.88 |           33,830,680 |          36,367,241 |           -2,777,834 |        354.07 | 1.43%          | -0.62%          | 1.72%             | 3.35%             | -1.87%            | 45.46%           |         360.83 |        243.42 | 348.08 | 342.58 |
|     24 | AVGO     |            0.85 |                0.83 |           30,724,725 |          36,034,947 |             -834,308 |        301.08 | -3.98%         | -13.24%         | -8.64%            | -11.79%           | -39.18%           | 3.90%            |         495    |        289.77 | 329.54 | 341.32 |
|     25 | IBIT     |            0.83 |                0.32 |            6,996,983 |           8,457,301 |            5,250,695 |         33.76 | -2.48%         | -13.30%         | -16.04%           | -23.59%           | -39.28%           | 3.49%            |          55.6  |         32.62 |  40.21 |  44.18 |
|     26 | TLT      |            0.82 |                0.48 |            6,049,064 |           7,350,020 |            1,714,192 |         81.49 | -0.24%         | 2.66%           | 0.62%             | 1.73%             | -10.31%           | 6.62%            |          90.86 |         76.43 |  80.99 |  80.1  |
|     27 | TSM      |            0.71 |                0.53 |           25,720,530 |          36,413,469 |          -11,258,692 |        349.2  | -3.96%         | -12.42%         | -9.15%            | -16.81%           | -28.36%           | 27.87%           |         487.47 |        273.08 | 384.36 | 419.77 |
|     28 | CRWV     |            0.67 |                0.44 |           15,057,911 |          22,600,645 |            3,518,665 |         42.6  | -11.85%        | -19.81%         | -15.89%           | -35.96%           | -69.18%           | 8.46%            |         138.25 |         39.28 |  50.65 |  66.53 |
|     29 | GLD      |            0.61 |                0.03 |           16,543,137 |          27,036,450 |            2,485,272 |        325.45 | -2.27%         | -8.44%          | -8.67%            | -12.59%           | -36.15%           | 1.40%            |         509.7  |        320.95 | 356.34 | 372.33 |
|     30 | QQQ      |            0.57 |                0.18 |          243,951,526 |         431,409,413 |          -21,153,789 |        638.1  | -1.99%         | -6.15%          | -4.95%            | -9.93%            | -16.35%           | 14.85%           |         762.86 |        555.6  | 671.31 | 708.47 |
|     31 | SMH      |            0.49 |                0.19 |           38,504,812 |          77,934,380 |              444,077 |        426.75 | -7.26%         | -12.33%         | -11.80%           | -21.49%           | -36.48%           | 30.37%           |         671.83 |        327.35 | 483.86 | 543.58 |
|     32 | SPY      |            0.46 |                0.67 |          211,094,389 |         460,614,318 |          -27,722,239 |        718.78 | -0.49%         | -4.72%          | -3.27%            | -5.25%            | -8.04%            | 14.22%           |         781.62 |        629.28 | 743.11 | 758.64 |
|     33 | XLF      |            0.12 |                0.16 |              510,232 |           4,149,866 |              572,774 |         56.11 | 0.83%          | -4.38%          | -1.87%            | 0.50%             | -6.55%            | 17.71%           |          60.04 |         47.67 |  57.18 |  55.83 |

## T2 — Premium Ratio Leaderboard (all strikes, call subtotal ≥ $1,000,000)

|   Rank | Ticker   |   Premium Ratio |   Call Volume |   Call Premium |   Put Volume |   Put Premium |
|-------:|:---------|----------------:|--------------:|---------------:|-------------:|--------------:|
|      1 | SMCI     |            2.65 |        59,126 |      5,717,257 |       15,084 |     2,159,999 |
|      2 | BABA     |            2.32 |         2,751 |      3,592,637 |        3,045 |     1,550,340 |
|      3 | RIOT     |            1.98 |       183,984 |      9,879,447 |       33,620 |     4,999,102 |
|      4 | AAPL     |            1.88 |        90,889 |     30,099,111 |       89,541 |    16,035,841 |
|      5 | TSLA     |            1.58 |        66,664 |     61,351,730 |      120,288 |    38,721,463 |
|      6 | NVDA     |            1.5  |       378,999 |    131,793,090 |      419,450 |    88,010,375 |
|      7 | ^VIX     |            1.25 |        72,363 |     20,261,784 |       72,252 |    16,185,595 |
|      8 | QCOM     |            1.18 |         1,496 |      1,282,163 |          896 |     1,090,687 |
|      9 | WULF     |            1.08 |        53,617 |      3,472,551 |       20,050 |     3,219,192 |
|     10 | MARA     |            0.95 |        16,548 |      1,238,900 |       11,529 |     1,308,373 |
|     11 | AVGO     |            0.83 |         7,585 |     22,185,980 |       14,909 |    26,663,639 |
|     12 | AMZN     |            0.75 |        14,955 |     10,537,904 |        5,617 |    14,098,270 |
|     13 | SPY      |            0.67 |       128,430 |     54,679,971 |      212,093 |    82,033,772 |
|     14 | MRVL     |            0.61 |         6,994 |      4,680,348 |        4,296 |     7,658,013 |
|     15 | UNH      |            0.55 |         4,841 |      5,051,759 |        3,879 |     9,119,763 |
|     16 | TSM      |            0.53 |         2,818 |      9,389,638 |        8,109 |    17,607,903 |
|     17 | TLT      |            0.48 |        87,336 |      3,185,703 |      156,275 |     6,609,415 |
|     18 | IREN     |            0.47 |        19,891 |      2,280,650 |       12,229 |     4,835,360 |
|     19 | CRWV     |            0.44 |        16,703 |      7,206,201 |       18,204 |    16,377,880 |
|     20 | GOOG     |            0.38 |        14,783 |     15,262,219 |        6,802 |    40,161,914 |
|     21 | IBIT     |            0.32 |        17,642 |      2,821,026 |       43,041 |     8,752,004 |
|     22 | MSTR     |            0.3  |        14,100 |      9,167,104 |       29,617 |    30,847,718 |
|     23 | GOOGL    |            0.26 |        13,075 |      7,436,342 |        2,724 |    28,566,554 |
|     24 | SMH      |            0.19 |         6,479 |     11,807,465 |        9,244 |    63,233,056 |
|     25 | QQQ      |            0.18 |        94,832 |     62,674,932 |       41,754 |   341,284,635 |
|     26 | SNDK     |            0.16 |        15,346 |      8,034,062 |        4,861 |    49,535,048 |
|     27 | INTC     |            0.11 |        11,045 |      5,854,690 |        8,844 |    53,061,905 |
|     28 | NFLX     |            0.06 |        36,746 |      2,634,459 |       19,175 |    45,071,360 |
|     28 | ARM      |            0.06 |         4,999 |      3,635,466 |        3,812 |    57,504,842 |
|     30 | RKLB     |            0.04 |         6,329 |      1,171,160 |        8,324 |    30,220,478 |
|     31 | GLD      |            0.03 |         8,599 |      7,077,251 |       31,300 |   270,940,934 |
|     32 | SLV      |            0.02 |         8,877 |      1,321,144 |       11,449 |    53,644,240 |
|     33 | COIN     |            0.01 |         1,711 |      1,314,889 |       15,071 |   198,766,180 |

## T1 — Top 4 Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261125C00352500  |        30,913 |     10,510,420 | AAPL270115P00320000  |       14,938 |     5,004,230 |
| AAPL     | AAPL261125C00355000  |        46,562 |      8,986,466 | AAPL261125P00350000  |       48,167 |     4,479,531 |
| AAPL     | AAPL270115C00355000  |         4,315 |      5,825,250 | AAPL261125P00352500  |       24,203 |     3,872,480 |
| AAPL     | AAPL261125C00350000  |         9,099 |      4,776,975 | AAPL270115P00355000  |        2,233 |     2,679,600 |
| AMZN     | AMZN261231C00270000  |         5,928 |      2,964,000 | AMZN261218P00300000  |        1,659 |     8,236,935 |
| AMZN     | AMZN270115C00260000  |         2,621 |      2,883,100 | AMZN270115P00325000  |          302 |     2,172,890 |
| AMZN     | AMZN270115C00200000  |           456 |      2,489,304 | AMZN270115P00300000  |          385 |     1,905,750 |
| AMZN     | AMZN261211C00265000  |         5,950 |      2,201,500 | AMZN261218P00240000  |        3,271 |     1,782,695 |
| ARM      | ARM261218C00170000   |         1,383 |      1,659,600 | ARM270115P00420000   |        1,010 |    25,977,200 |
| ARM      | ARM270115C00200000   |           975 |        780,000 | ARM270115P00360000   |        1,174 |    23,148,932 |
| ARM      | ARM261218C00210000   |         2,450 |        637,000 | ARM270115P00190000   |        1,511 |     5,605,810 |
| ARM      | ARM261218C00140000   |           191 |        558,866 | ARM270115P00400000   |          117 |     2,772,900 |
| AVGO     | AVGO270115C00150000  |           826 |     12,798,870 | AVGO270115P00300000  |        3,612 |     9,842,700 |
| AVGO     | AVGO261218C00300000  |         1,560 |      3,783,000 | AVGO270115P00310000  |        2,088 |     6,817,320 |
| AVGO     | AVGO261204C00285000  |         1,301 |      3,109,390 | AVGO261125P00302500  |        8,319 |     5,415,669 |
| AVGO     | AVGO261125C00300000  |         3,898 |      2,494,720 | AVGO261127P00355000  |          890 |     4,587,950 |
| BABA     | BABA261127C00065000  |           703 |      1,381,395 | BABA261218P00150000  |           74 |       480,630 |
| BABA     | BABA261127C00070000  |           700 |      1,004,500 | BABA270115P00130000  |          102 |       466,140 |
| BABA     | BABA261127C00060000  |           351 |        831,870 | BABA270115P00120000  |           87 |       311,460 |
| BABA     | BABA270115C00090000  |           997 |        374,872 | BABA261218P00075000  |        2,782 |       292,110 |
| CIFR     | CIFR261204C00006000  |         4,866 |        155,712 | CIFR261218P00010500  |          967 |       468,995 |
| CLSK     | CLSK261218C00005500  |         5,077 |        299,543 | CLSK261218P00006000  |        1,425 |       166,725 |
| COIN     | COIN261127C00040000  |            75 |        471,450 | COIN270115P00250000  |        6,590 |    98,784,100 |
| COIN     | COIN261224C00105000  |           486 |        398,034 | COIN270115P00230000  |        6,459 |    80,285,370 |
| COIN     | COIN270115C00115000  |           329 |        231,945 | COIN270115P00210000  |        1,050 |    11,502,750 |
| COIN     | COIN261127C00103000  |           821 |        213,460 | COIN261218P00190000  |          972 |     8,193,960 |
| CRWV     | CRWV270115C00040000  |         2,736 |      2,394,000 | CRWV270115P00040000  |        8,686 |     5,037,880 |
| CRWV     | CRWV270115C00055000  |         6,828 |      2,048,400 | CRWV270115P00045000  |        5,829 |     4,954,650 |
| CRWV     | CRWV261218C00045000  |         3,458 |      1,493,856 | CRWV261127P00060000  |        1,929 |     3,375,750 |
| CRWV     | CRWV261204C00043000  |         3,681 |      1,269,945 | CRWV270115P00057500  |        1,760 |     3,009,600 |
| GLD      | GLD270115C00350000   |         4,758 |      2,640,690 | GLD270115P00425000   |       10,104 |   100,938,960 |
| GLD      | GLD270115C00325000   |         1,165 |      1,823,225 | GLD270115P00400000   |        9,501 |    71,675,544 |
| GLD      | GLD270115C00340000   |         1,608 |      1,415,040 | GLD261218P00385000   |        8,269 |    49,283,240 |
| GLD      | GLD261218C00325000   |         1,068 |      1,198,296 | GLD261218P00470000   |        3,426 |    49,043,190 |
| GOOG     | GOOG270115C00270000  |         3,943 |      7,609,990 | GOOG270115P00480000  |        1,484 |    30,533,300 |
| GOOG     | GOOG270115C00300000  |         8,807 |      5,680,515 | GOOG261127P00300000  |        1,641 |     4,159,935 |
| GOOG     | GOOG261218C00280000  |         1,291 |      1,239,360 | GOOG270115P00270000  |        3,293 |     3,961,479 |
| GOOG     | GOOG270115C00290000  |           742 |        732,354 | GOOG261218P00315000  |          384 |     1,507,200 |
| GOOGL    | GOOGL270115C00300000 |         3,312 |      2,467,440 | GOOGL261218P00400000 |          903 |    11,219,775 |
| GOOGL    | GOOGL261218C00280000 |         1,776 |      1,962,480 | GOOGL261218P00360000 |        1,043 |     8,534,869 |
| GOOGL    | GOOGL261125C00280000 |         7,184 |      1,745,712 | GOOGL270115P00390000 |          418 |     4,637,710 |
| GOOGL    | GOOGL270115C00280000 |           803 |      1,260,710 | GOOGL261218P00395000 |          360 |     4,174,200 |
| IBIT     | IBIT270115C00037000  |         6,507 |        845,910 | IBIT261127P00039000  |        6,033 |     3,197,490 |
| IBIT     | IBIT270115C00035000  |         4,117 |        843,985 | IBIT261127P00036000  |       10,587 |     2,435,010 |
| IBIT     | IBIT261218C00034000  |         3,845 |        680,565 | IBIT261127P00034500  |       17,128 |     1,781,312 |
| IBIT     | IBIT261224C00035000  |         3,173 |        450,566 | IBIT261224P00032500  |        9,293 |     1,338,192 |
| INTC     | INTC270115C00065000  |         5,375 |      1,574,875 | INTC261218P00130000  |        2,101 |    15,936,085 |
| INTC     | INTC261127C00044000  |         1,290 |      1,486,080 | INTC261218P00110000  |        2,853 |    15,934,005 |
| INTC     | INTC270115C00060000  |         3,255 |      1,454,985 | INTC261218P00105000  |        2,137 |    10,866,645 |
| INTC     | INTC261127C00043000  |         1,125 |      1,338,750 | INTC261218P00115000  |        1,753 |    10,325,170 |
| IONQ     | IONQ261218C00024000  |         1,071 |        176,715 | IONQ270115P00120000  |          219 |     2,119,701 |
| IONQ     | IONQ270115C00022500  |           409 |        133,334 | IONQ261127P00031500  |          338 |       298,792 |
| IONQ     | IONQ270115C00030000  |           663 |         66,300 | IONQ261127P00032000  |          305 |       285,785 |
| IONQ     | IONQ261127C00023000  |           977 |         56,666 | IONQ261218P00022500  |        1,144 |       260,832 |
| IREN     | IREN261127C00013000  |        11,476 |        677,084 | IREN261218P00025000  |        2,059 |     2,458,446 |
| IREN     | IREN261218C00013000  |         3,438 |        598,212 | IREN261224P00018000  |        1,758 |       975,690 |
| IREN     | IREN261127C00011000  |         2,731 |        551,662 | IREN270115P00010000  |        6,316 |       720,024 |
| IREN     | IREN270115C00014000  |         2,246 |        453,692 | IREN261127P00016000  |        2,096 |       681,200 |
| MARA     | MARA270115C00005000  |         3,086 |        336,374 | MARA270115P00006000  |        4,356 |       509,652 |
| MARA     | MARA261127C00005000  |         6,736 |        330,064 | MARA261218P00006000  |        3,278 |       317,966 |
| MARA     | MARA261211C00005000  |         3,736 |        306,352 | MARA261231P00006000  |        2,360 |       264,320 |
| MARA     | MARA261218C00005000  |         2,990 |        266,110 | MARA261224P00006500  |        1,535 |       216,435 |
| MRVL     | MRVL261218C00150000  |         3,046 |      2,177,890 | MRVL270115P00160000  |          622 |     2,173,890 |
| MRVL     | MRVL261218C00135000  |           929 |      1,190,978 | MRVL270115P00140000  |          938 |     2,057,034 |
| MRVL     | MRVL261127C00135000  |         2,083 |        749,880 | MRVL261218P00130000  |        1,459 |     1,911,290 |
| MRVL     | MRVL261127C00130000  |           936 |        561,600 | MRVL261211P00130000  |        1,277 |     1,515,799 |
| MSTR     | MSTR261204C00080000  |         8,532 |      3,924,720 | MSTR261127P00100000  |        5,150 |    11,639,000 |
| MSTR     | MSTR261127C00045000  |           700 |      2,299,500 | MSTR261127P00090000  |        7,719 |     9,803,130 |
| MSTR     | MSTR261127C00050000  |           700 |      1,950,900 | MSTR261204P00080000  |        8,006 |     5,524,140 |
| MSTR     | MSTR261127C00079000  |         4,168 |        991,984 | MSTR261127P00080000  |        8,742 |     3,881,448 |
| NFLX     | NFLX261127C00059000  |        13,378 |        936,460 | NFLX270115P00090000  |        4,755 |    14,464,710 |
| NFLX     | NFLX270115C00059000  |         1,771 |        646,415 | NFLX270115P00084000  |        5,266 |    12,506,750 |
| NFLX     | NFLX261127C00060000  |        20,166 |        625,146 | NFLX270115P00078000  |        5,256 |     9,329,400 |
| NFLX     | NFLX270115C00060000  |         1,431 |        426,438 | NFLX270115P00082000  |        3,898 |     8,770,500 |
| NVDA     | NVDA261125C00155000  |       114,462 |     41,778,630 | NVDA261125P00150000  |      182,925 |    24,329,025 |
| NVDA     | NVDA261125C00152500  |        63,867 |     31,933,500 | NVDA261125P00152500  |      109,115 |    22,914,150 |
| NVDA     | NVDA270115C00170000  |        37,332 |     31,620,204 | NVDA270115P00120000  |       63,305 |    20,574,125 |
| NVDA     | NVDA261125C00160000  |       163,338 |     26,460,756 | NVDA261125P00155000  |       64,105 |    20,193,075 |
| QCOM     | QCOM270115C00175000  |           407 |        384,208 | QCOM261218P00160000  |          425 |       334,475 |
| QCOM     | QCOM261218C00170000  |           464 |        366,560 | QCOM270115P00165000  |          202 |       272,700 |
| QCOM     | QCOM261204C00157500  |           252 |        272,160 | QCOM261127P00240000  |           34 |       264,962 |
| QCOM     | QCOM261224C00175000  |           373 |        259,235 | QCOM270115P00155000  |          235 |       218,550 |
| QQQ      | QQQ261218C00650000   |        15,221 |     23,866,528 | QQQ261218P00725000   |       12,077 |   110,190,548 |
| QQQ      | QQQ261125C00640000   |        38,900 |     15,560,000 | QQQ261218P00720000   |       12,390 |   104,918,520 |
| QQQ      | QQQ261125C00638000   |        23,632 |     11,839,632 | QQQ261127P00690000   |       12,172 |    66,836,452 |
| QQQ      | QQQ261125C00635000   |        17,079 |     11,408,772 | QQQ261218P00750000   |        5,115 |    59,339,115 |
| RIOT     | RIOT261211C00018000  |        50,145 |      4,262,325 | RIOT261218P00015500  |       20,219 |     2,749,784 |
| RIOT     | RIOT261211C00020000  |       100,258 |      3,709,546 | RIOT261218P00016000  |       10,524 |     1,673,316 |
| RIOT     | RIOT261127C00017000  |        26,167 |      1,151,348 | RIOT261204P00018000  |        1,579 |       341,064 |
| RIOT     | RIOT261127C00015500  |         7,414 |        756,228 | RIOT261127P00018000  |        1,298 |       234,938 |
| RKLB     | RKLB261127C00046000  |         2,445 |        381,420 | RKLB270115P00165000  |        1,500 |    18,007,500 |
| RKLB     | RKLB270115C00055000  |         1,220 |        347,700 | RKLB261218P00110000  |        1,507 |     9,803,035 |
| RKLB     | RKLB261204C00050000  |         1,912 |        239,000 | RKLB261218P00080000  |          498 |     1,653,360 |
| RKLB     | RKLB261218C00050000  |           752 |        203,040 | RKLB261127P00046000  |        4,819 |       756,583 |
| SLV      | SLV261218C00037500   |         2,209 |        379,948 | SLV270115P00095000   |        6,250 |    36,375,000 |
| SLV      | SLV270115C00043000   |         4,186 |        364,182 | SLV270115P00090000   |        1,818 |     9,735,390 |
| SLV      | SLV261218C00034000   |           735 |        294,000 | SLV270115P00100000   |          865 |     5,458,150 |
| SLV      | SLV270115C00040000   |         1,747 |        283,014 | SLV261127P00045000   |        2,516 |     2,075,700 |
| SMCI     | SMCI261204C00023000  |        27,670 |      3,790,790 | SMCI270115P00023000  |        3,283 |     1,076,824 |
| SMCI     | SMCI261204C00025500  |        24,219 |      1,428,921 | SMCI261127P00022000  |        6,876 |       412,560 |
| SMCI     | SMCI261218C00028000  |         5,040 |        282,240 | SMCI261127P00022500  |        4,479 |       380,715 |
| SMCI     | SMCI261127C00022500  |         2,197 |        215,306 | SMCI270115P00028000  |          446 |       289,900 |
| SMH      | SMH270115C00500000   |         3,407 |      3,526,245 | SMH261218P00635000   |        1,530 |    31,755,150 |
| SMH      | SMH270115C00100000   |           100 |      3,339,600 | SMH261218P00600000   |          916 |    15,713,980 |
| SMH      | SMH270115C00460000   |         1,191 |      2,679,750 | SMH261218P00430000   |        3,273 |     9,612,801 |
| SMH      | SMH261218C00465000   |         1,781 |      2,261,870 | SMH261218P00400000   |        3,525 |     6,151,125 |
| SNDK     | SNDK261127C00080000  |        10,385 |      2,783,180 | SNDK261218P00225000  |        1,350 |    19,855,800 |
| SNDK     | SNDK261218C00015000  |           316 |      1,982,584 | SNDK261218P00212500  |        1,358 |    18,275,964 |
| SNDK     | SNDK270115C00085000  |         1,828 |      1,764,020 | SNDK261204P00137500  |        1,084 |     6,276,360 |
| SNDK     | SNDK261127C00075000  |         2,817 |      1,504,278 | SNDK261127P00125000  |        1,069 |     5,126,924 |
| SPY      | SPY261125C00715000   |        30,929 |     18,031,607 | SPY261218P00610000   |      150,753 |    24,572,739 |
| SPY      | SPY261125C00720000   |        42,465 |     12,824,430 | SPY261218P00680000   |       34,423 |    23,132,256 |
| SPY      | SPY261125C00717000   |        26,006 |     12,066,784 | SPY261218P00715000   |       11,241 |    17,367,345 |
| SPY      | SPY261125C00718000   |        29,030 |     11,757,150 | SPY261218P00700000   |       15,676 |    16,961,432 |
| TLT      | TLT270115C00083000   |        13,810 |      1,021,940 | TLT270115P00079000   |       63,620 |     3,053,760 |
| TLT      | TLT261218C00081000   |         8,478 |        907,146 | TLT270115P00078000   |       60,742 |     1,943,744 |
| TLT      | TLT270115C00088000   |        43,505 |        739,585 | TLT261218P00081000   |       10,718 |     1,039,646 |
| TLT      | TLT261218C00084000   |        21,543 |        517,032 | TLT261125P00081500   |       21,195 |       572,265 |
| TSLA     | TSLA261127C00180000  |           849 |     17,502,135 | TSLA261125P00380000  |       49,027 |    15,492,532 |
| TSLA     | TSLA261218C00180000  |           829 |     17,139,575 | TSLA261125P00385000  |       17,416 |     8,690,584 |
| TSLA     | TSLA261125C00380000  |        16,970 |     13,745,700 | TSLA261125P00382500  |       20,596 |     8,320,784 |
| TSLA     | TSLA261125C00390000  |        48,016 |     12,964,320 | TSLA261125P00375000  |       33,249 |     6,217,563 |
| TSLL     | TSLL261127C00010000  |         5,613 |        162,777 | TSLL261127P00013000  |        1,181 |       377,920 |
| TSM      | TSM270115C00360000   |         1,352 |      3,281,304 | TSM270115P00340000   |        2,741 |     6,638,702 |
| TSM      | TSM270115C00350000   |           926 |      2,693,734 | TSM261218P00340000   |        2,373 |     4,226,313 |
| TSM      | TSM261224C00245000   |           198 |      2,104,740 | TSM270115P00360000   |        1,071 |     3,641,400 |
| TSM      | TSM261211C00320000   |           342 |      1,309,860 | TSM270115P00320000   |        1,924 |     3,101,488 |
| UNH      | UNH261218C00340000   |         1,020 |      1,494,300 | UNH261211P00350000   |        2,300 |     4,002,000 |
| UNH      | UNH261218C00350000   |         1,369 |      1,233,469 | UNH261218P00355000   |        1,171 |     2,269,398 |
| UNH      | UNH270115C00340000   |           581 |      1,220,100 | UNH261218P00410000   |          219 |     1,497,960 |
| UNH      | UNH261127C00340000   |         1,871 |      1,103,890 | UNH261218P00415000   |          189 |     1,350,405 |
| WULF     | WULF270115C00011000  |        10,469 |      1,360,970 | WULF261218P00014000  |        2,618 |     1,083,852 |
| WULF     | WULF270115C00012000  |         8,754 |        822,876 | WULF261218P00009000  |       11,175 |       804,600 |
| WULF     | WULF270115C00013000  |         9,621 |        644,607 | WULF261218P00011000  |        3,701 |       666,180 |
| WULF     | WULF270115C00016000  |        24,773 |        644,098 | WULF261218P00012000  |        2,556 |       664,560 |
| XLF      | XLF261204C00053000   |           623 |        204,344 | XLF261218P00058000   |       10,601 |     2,364,023 |
| XLF      | XLF261218C00037000   |            98 |        185,024 | XLF261218P00056000   |        5,606 |       644,690 |
| XLF      | XLF261125C00041000   |            92 |        136,344 | XLF270115P00054000   |        6,640 |       590,960 |
| XLF      | XLF261204C00052000   |           300 |        125,400 | XLF270115P00056000   |        3,662 |       549,300 |
| ^VIX     | VIX270120C00020000   |        15,058 |      7,529,000 | VIX270120P00024000   |       15,080 |     5,353,400 |
| ^VIX     | VIX270120C00024000   |        14,638 |      4,903,730 | VIX270120P00025000   |       11,895 |     5,055,375 |
| ^VIX     | VIX270120C00025000   |        13,686 |      4,119,486 | VIX261216P00025000   |       11,113 |     3,556,160 |
| ^VIX     | VIX270120C00040000   |        28,981 |      3,709,568 | VIX261216P00020000   |       34,164 |     2,220,660 |

## T3 — Top 3 OTM Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261125C00355000  |        46,562 |      8,986,466 | AAPL270115P00320000  |       14,938 |     5,004,230 |
| AAPL     | AAPL270115C00355000  |         4,315 |      5,825,250 | AAPL261125P00350000  |       48,167 |     4,479,531 |
| AAPL     | AAPL261218C00365000  |        11,172 |      4,524,660 | AAPL261125P00352500  |       24,203 |     3,872,480 |
| AMZN     | AMZN261231C00270000  |         5,928 |      2,964,000 | AMZN261218P00240000  |        3,271 |     1,782,695 |
| AMZN     | AMZN270115C00260000  |         2,621 |      2,883,100 | AMZN270115P00235000  |        2,055 |     1,448,775 |
| AMZN     | AMZN261211C00265000  |         5,950 |      2,201,500 | AMZN261218P00235000  |        3,375 |     1,410,750 |
| ARM      | ARM261218C00170000   |         1,383 |      1,659,600 | ARM261218P00140000   |        1,870 |     1,346,400 |
| ARM      | ARM270115C00200000   |           975 |        780,000 | ARM261218P00120000   |        2,376 |       677,160 |
| ARM      | ARM261218C00210000   |         2,450 |        637,000 | ARM261218P00150000   |          324 |       338,256 |
| AVGO     | AVGO270115C00310000  |           830 |      2,105,710 | AVGO270115P00300000  |        3,612 |     9,842,700 |
| AVGO     | AVGO261218C00330000  |         1,542 |      1,822,644 | AVGO261218P00300000  |        1,382 |     3,130,230 |
| AVGO     | AVGO261218C00320000  |         1,159 |      1,755,885 | AVGO270115P00260000  |        1,802 |     2,155,192 |
| BABA     | BABA270115C00090000  |           997 |        374,872 | BABA261218P00075000  |        2,782 |       292,110 |
| BABA     | BABA261127C00085000  |         2,444 |        366,600 | BABA261218P00080000  |          453 |       102,831 |
| BABA     | BABA270115C00095000  |         1,373 |        311,671 | BABA261127P00080000  |        3,499 |        83,976 |
| CLSK     | CLSK261218C00005500  |         5,077 |        299,543 | CLSK261218P00004500  |        1,438 |        50,330 |
| COIN     | COIN261224C00105000  |           486 |        398,034 | COIN261218P00075000  |        2,489 |       258,856 |
| CRWV     | CRWV270115C00055000  |         6,828 |      2,048,400 | CRWV270115P00040000  |        8,686 |     5,037,880 |
| CRWV     | CRWV261218C00045000  |         3,458 |      1,493,856 | CRWV261218P00040000  |        4,776 |     1,939,056 |
| CRWV     | CRWV261204C00043000  |         3,681 |      1,269,945 | CRWV261204P00040000  |        7,077 |     1,712,634 |
| GLD      | GLD270115C00350000   |         4,758 |      2,640,690 | GLD270115P00280000   |       36,281 |     9,142,812 |
| GLD      | GLD270115C00340000   |         1,608 |      1,415,040 | GLD261231P00320000   |        2,246 |     2,088,780 |
| GLD      | GLD261204C00330000   |         1,888 |        887,360 | GLD261218P00310000   |        4,024 |     1,927,496 |
| GOOG     | GOOG270115C00300000  |         8,807 |      5,680,515 | GOOG270115P00270000  |        3,293 |     3,961,479 |
| GOOG     | GOOG261218C00280000  |         1,291 |      1,239,360 | GOOG270115P00275000  |        1,041 |     1,443,867 |
| GOOG     | GOOG270115C00290000  |           742 |        732,354 | GOOG261127P00275000  |        1,771 |       575,575 |
| GOOGL    | GOOGL270115C00300000 |         3,312 |      2,467,440 | GOOGL270115P00250000 |        2,335 |     1,258,565 |
| GOOGL    | GOOGL261218C00280000 |         1,776 |      1,962,480 | GOOGL261127P00275000 |        4,823 |     1,109,290 |
| GOOGL    | GOOGL261125C00280000 |         7,184 |      1,745,712 | GOOGL261125P00277500 |        4,649 |       999,535 |
| IBIT     | IBIT270115C00037000  |         6,507 |        845,910 | IBIT261224P00032500  |        9,293 |     1,338,192 |
| IBIT     | IBIT270115C00035000  |         4,117 |        843,985 | IBIT270115P00030000  |        6,310 |       719,340 |
| IBIT     | IBIT261218C00034000  |         3,845 |        680,565 | IBIT261218P00033000  |        4,049 |       591,154 |
| INTC     | INTC270115C00065000  |         5,375 |      1,574,875 | INTC270115P00052500  |        4,569 |     2,357,604 |
| INTC     | INTC270115C00060000  |         3,255 |      1,454,985 | INTC270115P00050000  |        3,075 |     1,294,575 |
| INTC     | INTC261127C00057000  |        13,731 |      1,249,521 | INTC261127P00054000  |        6,383 |       906,386 |
| IREN     | IREN261127C00013000  |        11,476 |        677,084 | IREN270115P00010000  |        6,316 |       720,024 |
| IREN     | IREN261218C00013000  |         3,438 |        598,212 | IREN270115P00011000  |        2,203 |       334,856 |
| IREN     | IREN270115C00014000  |         2,246 |        453,692 | IREN261127P00012500  |        7,490 |       322,070 |
| MRVL     | MRVL261218C00150000  |         3,046 |      2,177,890 | MRVL261218P00130000  |        1,459 |     1,911,290 |
| MRVL     | MRVL261218C00135000  |           929 |      1,190,978 | MRVL261211P00130000  |        1,277 |     1,515,799 |
| MRVL     | MRVL261127C00135000  |         2,083 |        749,880 | MRVL270115P00130000  |          907 |     1,465,712 |
| MSTR     | MSTR261204C00080000  |         8,532 |      3,924,720 | MSTR261218P00075000  |        3,206 |     2,250,612 |
| MSTR     | MSTR261127C00079000  |         4,168 |        991,984 | MSTR261218P00065000  |        4,693 |     1,642,550 |
| MSTR     | MSTR261127C00080000  |         4,718 |        934,164 | MSTR261127P00077000  |        5,596 |     1,510,920 |
| NFLX     | NFLX261127C00059000  |        13,378 |        936,460 | NFLX270115P00055000  |        2,980 |       515,540 |
| NFLX     | NFLX270115C00059000  |         1,771 |        646,415 | NFLX261127P00058000  |        4,876 |       190,164 |
| NFLX     | NFLX261127C00060000  |        20,166 |        625,146 | NFLX270115P00058000  |          535 |       145,520 |
| NVDA     | NVDA270115C00170000  |        37,332 |     31,620,204 | NVDA261125P00150000  |      182,925 |    24,329,025 |
| NVDA     | NVDA261125C00160000  |       163,338 |     26,460,756 | NVDA261125P00152500  |      109,115 |    22,914,150 |
| NVDA     | NVDA261125C00157500  |        73,652 |     18,413,000 | NVDA270115P00120000  |       63,305 |    20,574,125 |
| QCOM     | QCOM270115C00175000  |           407 |        384,208 | QCOM261218P00160000  |          425 |       334,475 |
| QCOM     | QCOM261218C00170000  |           464 |        366,560 | QCOM270115P00155000  |          235 |       218,550 |
| QCOM     | QCOM261224C00175000  |           373 |        259,235 | QCOM261218P00130000  |        1,223 |       178,558 |
| QQQ      | QQQ261218C00650000   |        15,221 |     23,866,528 | QQQ261218P00605000   |       33,284 |    36,945,240 |
| QQQ      | QQQ261125C00640000   |        38,900 |     15,560,000 | QQQ261218P00635000   |        9,677 |    19,653,987 |
| QQQ      | QQQ261218C00690000   |        34,968 |     10,455,432 | QQQ261218P00625000   |       11,598 |    19,113,504 |
| RIOT     | RIOT261211C00018000  |        50,145 |      4,262,325 | RIOT261218P00015500  |       20,219 |     2,749,784 |
| RIOT     | RIOT261211C00020000  |       100,258 |      3,709,546 | RIOT261218P00016000  |       10,524 |     1,673,316 |
| RIOT     | RIOT261127C00017000  |        26,167 |      1,151,348 | RIOT261218P00015000  |        1,984 |       228,160 |
| RKLB     | RKLB261127C00046000  |         2,445 |        381,420 | RKLB261218P00043000  |        1,563 |       432,951 |
| RKLB     | RKLB270115C00055000  |         1,220 |        347,700 | RKLB270115P00045000  |          499 |       261,975 |
| SLV      | SLV261218C00037500   |         2,209 |        379,948 | SLV261130P00036500   |        2,901 |       232,080 |
| SLV      | SLV270115C00043000   |         4,186 |        364,182 | SLV261218P00035000   |        1,796 |       231,684 |
| SLV      | SLV270115C00040000   |         1,747 |        283,014 | SLV270115P00035000   |          928 |       179,104 |
| SMCI     | SMCI261204C00023000  |        27,670 |      3,790,790 | SMCI261127P00022000  |        6,876 |       412,560 |
| SMCI     | SMCI261204C00025500  |        24,219 |      1,428,921 | SMCI261127P00022500  |        4,479 |       380,715 |
| SMCI     | SMCI261218C00028000  |         5,040 |        282,240 | SMCI270115P00015000  |        3,215 |       196,115 |
| SMH      | SMH270115C00500000   |         3,407 |      3,526,245 | SMH261218P00400000   |        3,525 |     6,151,125 |
| SMH      | SMH270115C00460000   |         1,191 |      2,679,750 | SMH270115P00380000   |        3,122 |     5,838,140 |
| SMH      | SMH261218C00465000   |         1,781 |      2,261,870 | SMH261218P00425000   |        2,137 |     5,780,585 |
| SPY      | SPY261125C00720000   |        42,465 |     12,824,430 | SPY261218P00610000   |      150,753 |    24,572,739 |
| SPY      | SPY261127C00720000   |        22,411 |     10,465,937 | SPY261218P00680000   |       34,423 |    23,132,256 |
| SPY      | SPY261125C00719000   |        29,117 |     10,249,184 | SPY261218P00715000   |       11,241 |    17,367,345 |
| TLT      | TLT270115C00083000   |        13,810 |      1,021,940 | TLT270115P00079000   |       63,620 |     3,053,760 |
| TLT      | TLT270115C00088000   |        43,505 |        739,585 | TLT270115P00078000   |       60,742 |     1,943,744 |
| TLT      | TLT261218C00084000   |        21,543 |        517,032 | TLT261218P00081000   |       10,718 |     1,039,646 |
| TSLA     | TSLA261125C00390000  |        48,016 |     12,964,320 | TSLA261125P00380000  |       49,027 |    15,492,532 |
| TSLA     | TSLA261125C00385000  |        24,670 |     12,088,300 | TSLA261125P00382500  |       20,596 |     8,320,784 |
| TSLA     | TSLA261218C00400000  |         5,243 |      7,749,154 | TSLA261125P00375000  |       33,249 |     6,217,563 |
| TSM      | TSM270115C00360000   |         1,352 |      3,281,304 | TSM270115P00340000   |        2,741 |     6,638,702 |
| TSM      | TSM270115C00350000   |           926 |      2,693,734 | TSM261218P00340000   |        2,373 |     4,226,313 |
| TSM      | TSM261218C00370000   |         1,001 |      1,266,265 | TSM270115P00320000   |        1,924 |     3,101,488 |
| UNH      | UNH261218C00350000   |         1,369 |      1,233,469 | UNH270115P00310000   |          528 |       390,720 |
| UNH      | UNH270115C00350000   |           389 |        602,950 | UNH261218P00335000   |          251 |       242,215 |
| UNH      | UNH261127C00350000   |         2,520 |        378,000 | UNH270115P00300000   |          379 |       223,610 |
| WULF     | WULF270115C00011000  |        10,469 |      1,360,970 | WULF261218P00009000  |       11,175 |       804,600 |
| WULF     | WULF270115C00012000  |         8,754 |        822,876 | WULF261127P00010000  |        4,280 |       196,880 |
| WULF     | WULF270115C00013000  |         9,621 |        644,607 | WULF261218P00008000  |        3,797 |       167,068 |
| XLF      | XLF261218C00057500   |         1,790 |        102,030 | XLF261218P00056000   |        5,606 |       644,690 |
| XLF      | XLF261218C00056500   |           711 |         71,811 | XLF270115P00054000   |        6,640 |       590,960 |
| XLF      | XLF270115C00057000   |           481 |         57,239 | XLF270115P00056000   |        3,662 |       549,300 |
| ^VIX     | VIX270120C00040000   |        28,981 |      3,709,568 | VIX270120P00024000   |       15,080 |     5,353,400 |
| ^VIX     | VIX270120C00031000   |        15,138 |      3,088,152 | VIX270120P00025000   |       11,895 |     5,055,375 |
| ^VIX     | VIX261216C00029000   |        13,726 |      2,237,338 | VIX261216P00025000   |       11,113 |     3,556,160 |

*premium = volume × lastPrice × 100 · OTM = calls strike>spot, puts strike<spot · T4 uses the cleaned chain: ≥2 DTE, OTM only, leveraged ETFs folded into their underlying, ^VIX ratio inverted · Net Signed Premium = bought calls/sold puts minus sold calls/bought puts, side from lastPrice vs bid/ask (prints outside the closing quote are not signed) · generated by options-flow-pipeline*

---

**Data quality:** requested: 52 · fetched: 52 · failed: 0 · gated: 9 · stale volume: 21,749 contracts (28% of premium) dropped

_Signal check (next-day rank correlation, last 20 sessions): composite IC +0.072 (t +1.3, n=20) · flow_pct IC -0.064 (t -1.4, n=20) · trend_pct IC +0.129 (t +1.9, n=20)_

_Signal check, next 5 sessions (rank correlation, last 20 resolved sessions; windows overlap, so t is overstated): composite IC +0.030 (t +0.5, n=20) · flow_pct IC -0.160 (t -5.2, n=20) · trend_pct IC +0.152 (t +3.0, n=20)_