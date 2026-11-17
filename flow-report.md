# Options Flow Report (v1.3) — 2026-11-16

**Run stats:** 52/52 tickers fetched · 0 failed · 56,320 contracts

## Market Regime

**neutral risk · contango (VIX/VIX3M=1.00, DoD +0.06) · negative gamma (moves amplified) · high vol · choppy/rangebound — momentum tilted**

`Vol: HIGH · Trend: CHOP · Risk: NEUTRAL · Gamma: NEGATIVE · SPY GEX: $-12,876M`

_Pipeline knobs: mom×0.85 · conviction≥0.80_

## Master Scoreboard (all tickers by composite)

| Rank   | Ticker   | Composite   | Trend%   | Mom%   | Flow%   | Rot%   | Conviction   | ΔRank   |
|:-------|:---------|:------------|:---------|:-------|:--------|:-------|:-------------|:--------|
| 1      | XLV      | 100.0       | 100      | 99     | N/A     | 99     | CONFIRMED    | 0       |
| 2      | XLP      | 96.7        | 97       | 93     | N/A     | 89     | CONFIRMED    | 0       |
| 3      | XLE      | 93.4        | 93       | 85     | N/A     | 88     | CONFIRMED    | 0       |
| 4      | XLRE     | 90.2        | 90       | 77     | N/A     | 80     | NEUTRAL      | +3      |
| 5      | XLB      | 88.5        | 89       | 76     | N/A     | 80     | NEUTRAL      | -1      |
| 6      | XLK      | 82.0        | 82       | 79     | N/A     | 65     | NEUTRAL      | +2      |
| 7      | BIL      | 80.3        | 80       | 70     | N/A     | 74     | NEUTRAL      | +2      |
| 8      | XLY      | 78.7        | 79       | 66     | N/A     | 76     | NEUTRAL      | +2      |
| 9      | AI       | 78.0        | 77       | 59     | 79      | 83     | NEUTRAL      | -4      |
| 10     | UNH      | 77.2        | 95       | 83     | 62      | 91     | NEUTRAL      | +11     |
| 11     | AMZN     | 72.2        | 74       | 58     | 71      | 81     | NEUTRAL      | +1      |
| 12     | RIOT     | 68.2        | 54       | 47     | 80      | 56     | NEUTRAL      | +19     |
| 13     | TSLA     | 67.2        | 67       | 52     | 67      | 76     | NEUTRAL      | +6      |
| 14     | TLT      | 66.9        | 52       | 46     | 79      | 56     | NEUTRAL      | +10     |
| 15     | IWM      | 63.9        | 64       | 64     | N/A     | 63     | NEUTRAL      | +3      |
| 16     | INTC     | 63.4        | 48       | 62     | 77      | 38     | NEUTRAL      | -2      |
| 17     | CPER     | 62.3        | 62       | 65     | N/A     | 61     | NEUTRAL      | +5      |
| 18     | HIVE     | 60.1        | 13       | 16     | 100     | 14     | CONFLICT     | +26     |
| 19     | HYG      | 59.0        | 59       | 54     | N/A     | 62     | NEUTRAL      | +6      |
| 20     | CLSK     | 57.7        | 18       | 26     | 91      | 17     | CONFLICT     | +32     |
| 21     | GOOGL    | 57.4        | 44       | 47     | 69      | 43     | NEUTRAL      | -1      |
| 22     | XLI      | 57.4        | 57       | 57     | N/A     | 54     | NEUTRAL      | +5      |
| 23     | MRVL     | 56.0        | 87       | 79     | 30      | 72     | CONFLICT     | 0       |
| 24     | QBTS     | 55.9        | 11       | 16     | 94      | 8      | CONFLICT     | +31     |
| 25     | LQD      | 55.7        | 56       | 44     | N/A     | 59     | NEUTRAL      | +10     |
| 26     | SLV      | 55.3        | 28       | 38     | 79      | 29     | CONFLICT     | +12     |
| 27     | SNDK     | 54.2        | 84       | 71     | 29      | 73     | CONFLICT     | -21     |
| 28     | AAPL     | 53.8        | 98       | 82     | 16      | 100    | CONFLICT     | -13     |
| 29     | IONQ     | 53.1        | 21       | 26     | 80      | 19     | CONFLICT     | +22     |
| 30     | QQQ      | 52.1        | 70       | 69     | 36      | 62     | NEUTRAL      | +3      |
| 31     | MSTR     | 51.1        | 46       | 39     | 56      | 53     | NEUTRAL      | +14     |
| 32     | QCOM     | 50.1        | 69       | 52     | 34      | 80     | NEUTRAL      | -19     |
| 33     | SMR      | 49.4        | 5        | 10     | 87      | 7      | CONFLICT     | +26     |
| 34     | XLC      | 49.2        | 49       | 47     | N/A     | 54     | NEUTRAL      | +3      |
| 35     | TSM      | 49.2        | 85       | 80     | 19      | 69     | CONFLICT     | -19     |
| 36     | SPY      | 49.1        | 75       | 62     | 27      | 79     | CONFLICT     | 0       |
| 37     | OPEN     | 49.1        | 2        | 2      | 89      | 0      | CONFLICT     | +24     |
| 38     | GLD      | 46.8        | 38       | 35     | 55      | 43     | NEUTRAL      | +9      |
| 39     | IBIT     | 46.2        | 51       | 46     | 42      | 54     | NEUTRAL      | -13     |
| 40     | XLF      | 46.2        | 92       | 86     | 7       | 85     | CONFLICT     | -1      |
| 41     | HIMS     | 46.0        | 30       | 38     | 60      | 31     | NEUTRAL      | +5      |
| 42     | NVDA     | 45.5        | 36       | 47     | 54      | 30     | NEUTRAL      | -8      |
| 43     | EOSE     | 44.4        | 3        | 6      | 79      | 3      | CONFLICT     | +17     |
| 44     | SMCI     | 41.7        | 31       | 43     | 51      | 27     | NEUTRAL      | -16     |
| 45     | NFLX     | 41.5        | 20       | 15     | 60      | 29     | NEUTRAL      | -28     |
| 46     | ARM      | 41.5        | 61       | 72     | 25      | 46     | CONFLICT     | -35     |
| 47     | XLU      | 40.4        | 72       | 66     | 13      | 71     | CONFLICT     | -6      |
| 48     | CRWV     | 39.9        | 23       | 31     | 54      | 15     | NEUTRAL      | +2      |
| 49     | AVGO     | 39.8        | 39       | 40     | 40      | 47     | NEUTRAL      | -9      |
| 50     | CIFR     | 39.5        | 10       | 19     | 65      | 6      | NEUTRAL      | +8      |
| 51     | GOOG     | 37.0        | 41       | 47     | 34      | 41     | NEUTRAL      | -9      |
| 52     | SMH      | 36.2        | 66       | 73     | 11      | 54     | CONFLICT     | -20     |
| 53     | RKLB     | 35.5        | 33       | 39     | 38      | 34     | NEUTRAL      | -10     |
| 54     | BABA     | 34.4        | 16       | 16     | 50      | 23     | NEUTRAL      | -1      |
| 55     | OKLO     | 33.7        | 8        | 11     | 55      | 11     | NEUTRAL      | +2      |
| 56     | WULF     | 32.3        | 34       | 43     | 31      | 33     | NEUTRAL      | -26     |
| 57     | MARA     | 31.4        | 25       | 26     | 37      | 27     | NEUTRAL      | -8      |
| 58     | IREN     | 27.6        | 7        | 15     | 45      | 3      | NEUTRAL      | -2      |
| 59     | ETHA     | 26.9        | 43       | 45     | 14      | 44     | NEUTRAL      | -30     |
| 60     | COIN     | 26.2        | 26       | 30     | 26      | 27     | NEUTRAL      | -12     |
| 61     | RGTI     | 21.7        | 15       | 20     | 28      | 12     | NEUTRAL      | -7      |
| N/A    | AAPX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDU     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | NVDX     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | TSLL     | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^GSPC    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^SKEW    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX     | N/A         | N/A      | N/A    | 13      | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VIX3M   | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |
| N/A    | ^VVIX    | N/A         | N/A      | N/A    | N/A     | N/A    | INSUFFICIENT | ·       |

## Sector Rotation / Relative Strength (top 15)

| Ticker   |   RS Rating |   Rel Str 63d | RS New-High   | Dual-Mom   |
|:---------|------------:|--------------:|:--------------|:-----------|
| SNDK     |          99 |         -46.9 | No            | above cash |
| AAPL     |          97 |          17.2 | Yes           | above cash |
| XLV      |          96 |          14.5 | Yes           | above cash |
| UNH      |          94 |           8.6 | No            | above cash |
| XLE      |          92 |           4   | No            | above cash |
| MRVL     |          91 |         -29.3 | No            | above cash |
| XLP      |          89 |          12.3 | No            | above cash |
| XLF      |          88 |           4.3 | No            | above cash |
| AMZN     |          86 |           2.7 | No            | above cash |
| XLB      |          84 |           3.2 | No            | above cash |
| XLRE     |          83 |           3.3 | No            | above cash |
| AI       |          81 |          11.6 | No            | below cash |
| SPY      |          79 |           0   | Yes           | above cash |
| QCOM     |          78 |           9.1 | No            | below cash |
| TSM      |          76 |          -6.1 | No            | above cash |

## Option Skew — Extremes (top/bottom 8)

_Board-wide: protection demand rising across the board (typical name z +1.1 vs its own norm; 21 of 32 names at z +1 or more, 1 at −1 or less). Hedging arrows are measured net of this move._

| Ticker   | Group    | Tilt        |   Skew25 (vol pts) | 90-110   |   ATM IV % |   Skew/IV | Hedging            |    z | Flow        | Positioning   |
|:---------|:---------|:------------|-------------------:|:---------|-----------:|----------:|:-------------------|-----:|:------------|:--------------|
| SPY      | top 8    | put-skewed  |                7.2 | 15.0     |       18.4 |      0.39 | steady →           | -0.5 | Neutral +7  |               |
| QQQ      | top 8    | put-skewed  |                8.6 | 14.5     |       28.6 |      0.3  | steady →           | -0.7 | Neutral -2  |               |
| AAPL     | top 8    | put-skewed  |                5.7 | 10.2     |       24.1 |      0.24 | hedging building ↑ |  1.2 | Neutral -10 |               |
| SMH      | top 8    | put-skewed  |                9.6 | 9.8      |       52.9 |      0.18 | steady →           |  0.2 | Neutral -2  |               |
| IBIT     | top 8    | put-skewed  |                7.1 | 8.7      |       44.2 |      0.16 | hedging building ↑ |  1.3 | Neutral +14 |               |
| TSLA     | top 8    | put-skewed  |                7.1 | 7.6      |       49.7 |      0.14 | steady →           | -0.1 | Neutral +0  |               |
| AMZN     | top 8    | put-skewed  |                5.2 | 7.7      |       36.8 |      0.14 | steady →           |  0   | Neutral -12 |               |
| TSM      | top 8    | put-skewed  |                6.7 | 7.5      |       48.3 |      0.14 | steady →           | -0.1 | Neutral +1  |               |
| HIMS     | bottom 8 | call-skewed |               -0.8 | -0.3     |       73.3 |     -0.01 | steady →           | -0.5 | Neutral +3  |               |
| TLT      | bottom 8 | call-skewed |               -0   | N/A      |       13.1 |     -0    | steady →           | -0.8 | Neutral +11 |               |
| CIFR     | bottom 8 | put-skewed  |                4.9 | 3.8      |      130.1 |      0.04 | hedging building ↑ |  1.6 | Neutral +5  |               |
| OKLO     | bottom 8 | put-skewed  |                3.2 | 1.6      |       85.2 |      0.04 | steady →           | -0.2 | Neutral -6  |               |
| ETHA     | bottom 8 | put-skewed  |                3.5 | 3.1      |       56.6 |      0.06 | hedging easing ↓   | -1.9 | Neutral -3  |               |
| GLD      | bottom 8 | put-skewed  |                1.6 | 3.0      |       24.5 |      0.06 | steady →           | -0.7 | Neutral +10 |               |
| NVDA     | bottom 8 | put-skewed  |                4.3 | 3.7      |       63.5 |      0.07 | hedging easing ↓   | -2.6 | Neutral -4  |               |
| NFLX     | bottom 8 | put-skewed  |                2.6 | 2.8      |       35.7 |      0.07 | steady →           |  0.6 | Neutral +4  |               |

_32 of 52 tickers had a fittable smile. Skew25 = how much more an out-of-the-money put costs than the matching out-of-the-money call, in vol points, at a constant 30-day tenor, re-derived from bid/ask mids (Yahoo's own IV field is not used). Positive = puts richer, the normal state — so read the *ranking*, not the level. Tilt is by sign: call-skewed = Skew/IV below 0; least put-skewed = 0 to 0.02; put-skewed above. Hedging = tonight's Skew/IV against the name's own previous 20 sessions (z = standard deviations from that average), net of the typical name's move tonight (the Board-wide line above): building when z is at least +1, easing at −1 or below, else steady; n/a until 10 prior sessions exist. It describes protection demand, not a price forecast._

## Mega-Cap Tech Skew

| Ticker   |   Skew25 (vol pts) |   90-110 |   ATM IV % |   Skew/IV | Rank     | Read           | Hedging            |    z | Flow        | Positioning   |
|:---------|-------------------:|---------:|-----------:|----------:|:---------|:---------------|:-------------------|-----:|:------------|:--------------|
| NVDA     |                4.3 |      3.7 |       63.5 |      0.07 | 26 of 32 | put-skewed     | hedging easing ↓   | -2.6 | Neutral -4  |               |
| AAPL     |                5.7 |     10.2 |       24.1 |      0.24 | 3 of 32  | steep put skew | hedging building ↑ |  1.2 | Neutral -10 |               |
| AMZN     |                5.2 |      7.7 |       36.8 |      0.14 | 7 of 32  | steep put skew | steady →           |  0   | Neutral -12 |               |
| GOOGL    |                3.6 |      5.2 |       36.1 |      0.1  | 16 of 32 | put-skewed     | steady →           |  0   | Neutral -11 |               |
| TSLA     |                7.1 |      7.6 |       49.7 |      0.14 | 6 of 32  | steep put skew | steady →           | -0.1 | Neutral +0  |               |
| AVGO     |                7.7 |      7.1 |       63.2 |      0.12 | 10 of 32 | put-skewed     | steady →           |  0.1 | Neutral -3  |               |

_Mega-cap tech: 6 of 6 fitted · median Skew/IV 0.13 vs 0.09 for the other names · richer downside protection than the rest of the board · steepest: AAPL, AMZN, TSLA · flattest: NVDA._

_Flow = premium-weighted flow score: 100 × (bought calls + sold puts − sold calls − bought puts) ÷ total out-of-the-money premium, sides estimated from the last trade against bid/ask (a last trade outside the closing quote is left unsigned); Bull at +20 or more, Bear at −20 or less. Positioning: defensive = hedging building with Bear flow; speculative = hedging easing with Bull flow; blank otherwise. Positioning describes what is being hedged and flowed tonight. It is not a price forecast._

## Stretch & Reversal Watch (experimental)

| Watch             | Tonight                                                                          | Backtest (before live)                                       | Live since 2026-11-06                      |
|:------------------|:---------------------------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------------|
| hedging unwinding | NVDA (z -2.6), ETHA (z -1.9)                                                     | 194 flags · +1.6% vs avg name · 59% beat it                  | 3 flags · -4.5% vs avg name · 0% beat it   |
| stretched up      | none                                                                             | 597 flags · -1.5% vs avg name · 41% beat it                  | 14 flags · -3.4% vs avg name · 50% beat it |
| washed out        | IBIT (-13%)                                                                      | 118 flags · -0.1% vs avg name · 57% beat it (no edge so far) | 13 flags · +3.2% vs avg name · 69% beat it |
| puts closing      | ETHA (98% puts), SPY (97% puts), GLD (93% puts), MSTR (88% puts), ARM (85% puts) | 789 flags · +0.7% vs avg name · 55% beat it (to 2026-11-16)  | none resolved yet (counts from 2026-11-16) |

_Experimental, not proven. Hedging unwinding = tonight's Skew/IV at z -1.5 or lower against the name's own norm, net of the board (as the Hedging column): protection being sold off. Stretched up = price up 5% or more over the last 5 sessions. Washed out = down 5% or more with hedging at z +2 or more on its own norm. Puts closing = the fifth of names where puts made up most of the out-of-the-money positions closed in the previous session (volume matched against the drop in open interest): protection taken off. The record columns score each past flag 5 sessions later against the average name that night (prices from the option chains' implied forwards). The backtest is in-sample: the thresholds were picked on that same history, so it flatters the flags; the live column counts only flags raised since this block was added and is the one that matters. If the live record does not hold up, the block goes. Not a price forecast._

---

# Flow Detail

## T4 — OTM Flow Summary (ranked by OTM Call/Put premium ratio)

|   Rank | Ticker   |   Premium Ratio |   Premium Ratio All |   Total Call Premium |   Total Put Premium |   Net Signed Premium |   Close Price | 1-Day Return   | 1-Week Return   | % Close to MA20   | % Close to MA50   | % Close to High   | % Close to Low   |   52 Week High |   52 Week Low |    MA20 |    MA50 |
|-------:|:---------|----------------:|--------------------:|---------------------:|--------------------:|---------------------:|--------------:|:---------------|:----------------|:------------------|:------------------|:------------------|:-----------------|---------------:|--------------:|--------:|--------:|
|      1 | TLT      |            6.45 |                0.62 |            6,546,524 |           1,015,203 |              866,961 |         79.38 | 0.00%          | -3.11%          | -2.11%            | -0.96%            | -12.63%           | 3.86%            |          90.86 |         76.43 |   81.09 |   80.15 |
|      2 | RIOT     |            3.95 |                9.83 |            4,631,233 |           1,171,713 |           -3,330,970 |         17.06 | -2.63%         | 15.58%          | 13.93%            | -4.97%            | -43.73%           | 48.35%           |          30.32 |         11.5  |   14.97 |   17.95 |
|      3 | IONQ     |            2.75 |                0.7  |            1,734,822 |             630,614 |              -77,054 |         26.45 | -8.41%         | 0.08%           | -14.84%           | -26.71%           | -64.09%           | 6.16%            |          73.65 |         24.92 |   31.06 |   36.09 |
|      4 | SLV      |            1.94 |                0.49 |            7,273,692 |           3,741,041 |            1,862,678 |         42.39 | -3.94%         | -9.67%          | -10.33%           | -19.29%           | -61.40%           | 0.90%            |         109.83 |         42.01 |   47.27 |   52.52 |
|      5 | INTC     |            1.83 |                0.41 |           23,350,855 |          12,748,007 |              995,650 |         55.47 | -7.02%         | 6.16%           | -22.87%           | -41.09%           | -61.03%           | 68.65%           |         142.35 |         32.89 |   71.92 |   94.17 |
|      6 | UNH      |            1.77 |                4.35 |            8,125,933 |           4,589,095 |           -2,802,638 |        412.02 | 1.12%          | 4.12%           | 0.99%             | 5.18%             | -10.74%           | 60.96%           |         461.62 |        255.97 |  407.99 |  391.73 |
|      7 | GOOGL    |            1.73 |                0.49 |           30,831,569 |          17,872,411 |           -5,189,816 |        283.72 | -4.07%         | 0.41%           | -5.55%            | -13.26%           | -30.56%           | 4.27%            |         408.61 |        272.11 |  300.39 |  327.09 |
|      7 | AMZN     |            1.73 |                0.71 |           40,886,625 |          23,580,569 |           -8,003,960 |        257.75 | -3.34%         | -0.95%          | 0.25%             | 1.16%             | -10.25%           | 31.51%           |         287.2  |        196    |  257.1  |  254.8  |
|      9 | NFLX     |            1.7  |                0.24 |            7,808,972 |           4,605,114 |              458,203 |         60.75 | -2.25%         | -7.34%          | -4.90%            | -11.74%           | -47.29%           | 0.45%            |         115.25 |         60.48 |   63.88 |   68.83 |
|     10 | TSLA     |            1.69 |                1.18 |          120,612,582 |          71,447,434 |              315,939 |        379.74 | -2.69%         | 10.49%          | -1.61%            | 1.20%             | -23.87%           | 27.70%           |         498.83 |        297.38 |  385.94 |  375.25 |
|     11 | GLD      |            1.62 |                0.09 |           15,811,672 |           9,735,492 |            2,674,764 |        352.93 | -0.71%         | -6.01%          | -3.95%            | -7.08%            | -30.76%           | 0.28%            |         509.7  |        351.96 |  367.45 |  379.83 |
|     12 | BABA     |            1.58 |                0.07 |            4,480,105 |           2,831,228 |              277,056 |         90.62 | -3.98%         | -16.15%         | -10.59%           | -14.85%           | -49.96%           | 0.06%            |         181.1  |         90.57 |  101.36 |  106.42 |
|     13 | NVDA     |            1.5  |                1    |          268,703,334 |         179,295,452 |          -16,509,242 |        156.14 | -4.12%         | -14.02%         | -20.19%           | -26.75%           | -35.84%           | 4.93%            |         243.37 |        148.8  |  195.64 |  213.16 |
|     13 | MSTR     |            1.5  |                1.61 |           38,850,262 |          25,943,987 |             -827,852 |        103.03 | -7.70%         | -20.32%         | -22.29%           | -27.68%           | -51.82%           | 25.94%           |         213.83 |         81.81 |  132.59 |  142.47 |
|     15 | SMCI     |            1.42 |                1.34 |            4,766,094 |           3,366,525 |               78,764 |         25.03 | -6.85%         | -7.57%          | -19.08%           | -30.94%           | -51.30%           | 28.49%           |          51.4  |         19.48 |   30.93 |   36.25 |
|     16 | CRWV     |            1.35 |                0.3  |           14,877,747 |          10,987,234 |           -2,477,599 |         49.88 | -6.12%         | 14.25%          | -8.35%            | -30.54%           | -63.92%           | 22.92%           |         138.25 |         40.58 |   54.43 |   71.81 |
|     17 | RKLB     |            1.31 |                0.05 |            3,717,075 |           2,828,342 |               62,716 |         57.37 | -6.76%         | 24.74%          | 2.30%             | -7.96%            | -62.01%           | 52.70%           |         151    |         37.57 |   56.08 |   62.33 |
|     18 | IREN     |            1.28 |                0.84 |            7,520,698 |           5,891,815 |           -1,928,191 |         16.39 | -9.80%         | -9.10%          | -28.84%           | -51.05%           | -76.82%           | 2.37%            |          70.71 |         16.01 |   23.03 |   33.48 |
|     19 | AVGO     |            1.17 |                0.63 |           40,866,181 |          34,967,714 |           -2,147,538 |        333.4  | -3.92%         | 14.36%          | 0.76%             | -3.33%            | -32.65%           | 15.06%           |         495    |        289.77 |  330.9  |  344.89 |
|     19 | QCOM     |            1.17 |                1.43 |            2,990,043 |           2,558,845 |             -344,679 |        168.52 | -2.29%         | 7.51%           | -2.62%            | -5.71%            | -35.16%           | 38.14%           |         259.92 |        121.99 |  173.05 |  178.73 |
|     21 | GOOG     |            1.15 |                0.04 |           14,024,419 |          12,147,327 |             -917,261 |        281.26 | -3.85%         | -0.17%          | -5.60%            | -13.20%           | -30.46%           | 3.58%            |         404.47 |        271.54 |  297.94 |  324.03 |
|     22 | MRVL     |            1.11 |                0.41 |           12,487,155 |          11,241,288 |            1,817,882 |        145.36 | -7.27%         | 8.84%           | -23.56%           | -36.15%           | -55.94%           | 105.63%          |         329.88 |         70.69 |  190.16 |  227.64 |
|     23 | IBIT     |            1.08 |                0.53 |           10,839,716 |          10,055,358 |            2,909,310 |         36.79 | -5.52%         | -14.50%         | -15.78%           | -18.79%           | -33.83%           | 12.03%           |          55.6  |         32.84 |   43.68 |   45.3  |
|     24 | ARM      |            1    |                0.71 |            6,940,407 |           6,919,342 |              642,474 |        175.05 | -8.12%         | 5.00%           | -13.72%           | -29.02%           | -61.33%           | 75.02%           |         452.7  |        100.02 |  202.88 |  246.6  |
|     25 | SNDK     |            0.99 |                0.51 |          100,466,029 |         101,330,447 |            7,412,728 |        809.11 | -8.58%         | 0.33%           | -26.19%           | -43.13%           | -65.63%           | 342.14%          |        2354.39 |        183    | 1096.25 | 1422.81 |
|     26 | QQQ      |            0.92 |                0.3  |          346,374,640 |         375,351,401 |          -15,352,689 |        661.75 | -2.67%         | 2.27%           | -4.46%            | -7.67%            | -13.25%           | 19.11%           |         762.86 |        555.6  |  692.62 |  716.72 |
|     27 | WULF     |            0.84 |                0.68 |            2,232,705 |           2,645,530 |              987,621 |         11.88 | -5.86%         | 17.86%          | -1.98%            | -14.38%           | -60.19%           | 24.92%           |          29.84 |          9.51 |   12.12 |   13.87 |
|     28 | COIN     |            0.81 |                0.09 |            7,117,497 |           8,733,469 |             -844,424 |        119.84 | -6.12%         | -12.41%         | -18.96%           | -29.13%           | -57.91%           | 2.15%            |         284.74 |        117.32 |  147.88 |  169.09 |
|     29 | XLU      |            0.8  |                1.05 |              788,814 |             984,046 |                1,342 |         44.12 | 0.18%          | 1.89%           | 2.10%             | 5.26%             | -7.70%            | 13.04%           |          47.8  |         39.03 |   43.21 |   41.91 |
|     30 | ^VIX     |            0.75 |                1.58 |           25,512,731 |          19,010,834 |            5,697,812 |         22.91 | 18.70%         | -18.70%         | 16.86%            | 31.17%            | -35.10%           | 71.23%           |          35.3  |         13.38 |   19.61 |   17.47 |
|     31 | TSM      |            0.68 |                0.43 |           23,656,342 |          34,814,879 |              729,158 |        373.45 | -6.34%         | 5.76%           | -8.13%            | -12.95%           | -23.39%           | 39.96%           |         487.47 |        266.82 |  406.52 |  429    |
|     32 | SPY      |            0.64 |                0.26 |          307,866,596 |         483,109,129 |           55,349,172 |        739.95 | -1.91%         | 0.95%           | -2.34%            | -3.13%            | -5.33%            | 17.59%           |         781.62 |        629.28 |  757.69 |  763.82 |
|     33 | ETHA     |            0.52 |                0.44 |              797,893 |           1,544,084 |              -58,860 |         41.13 | -6.57%         | -18.99%         | -18.74%           | -25.33%           | -47.45%           | 18.96%           |          78.27 |         34.58 |   50.61 |   55.08 |
|     34 | SMH      |            0.46 |                0.28 |           34,209,493 |          74,351,157 |           -2,652,218 |        461.9  | -5.11%         | 3.16%           | -10.10%           | -17.18%           | -31.25%           | 46.61%           |         671.83 |        315.05 |  513.81 |  557.7  |
|     35 | AAPL     |            0.39 |                0.68 |           19,171,532 |          49,544,974 |           -6,563,455 |        352.78 | -0.98%         | 2.50%           | 1.77%             | 3.85%             | -2.23%            | 44.93%           |         360.83 |        243.42 |  346.64 |  339.69 |
|     36 | XLF      |            0.07 |                0.31 |              391,080 |           5,752,225 |              -52,207 |         58.18 | -0.85%         | 1.18%           | 1.68%             | 3.95%             | -3.10%            | 22.05%           |          60.04 |         47.67 |   57.22 |   55.97 |

## T2 — Premium Ratio Leaderboard (all strikes, call subtotal ≥ $1,000,000)

|   Rank | Ticker   |   Premium Ratio |   Call Volume |   Call Premium |   Put Volume |   Put Premium |
|-------:|:---------|----------------:|--------------:|---------------:|-------------:|--------------:|
|      1 | RIOT     |            9.83 |       106,519 |      7,604,584 |       11,189 |       773,308 |
|      2 | UNH      |            4.35 |         4,698 |     11,725,770 |        1,402 |     2,695,290 |
|      3 | MSTR     |            1.61 |        31,247 |     26,424,335 |        4,206 |    16,401,444 |
|      4 | ^VIX     |            1.58 |       125,297 |     21,955,575 |      129,237 |    13,853,361 |
|      5 | QCOM     |            1.43 |         1,508 |      1,880,284 |        2,669 |     1,317,379 |
|      6 | SMCI     |            1.34 |        18,199 |      2,184,398 |        8,207 |     1,624,090 |
|      7 | TSLA     |            1.18 |        54,045 |     30,983,627 |       26,333 |    26,182,285 |
|      8 | NVDA     |            1    |       115,479 |     68,843,595 |       78,944 |    68,878,782 |
|      9 | IREN     |            0.84 |        22,988 |      2,803,165 |       17,092 |     3,348,566 |
|     10 | ARM      |            0.71 |         1,863 |      2,522,510 |        4,065 |     3,555,850 |
|     10 | AMZN     |            0.71 |        14,355 |     11,825,677 |       14,273 |    16,710,992 |
|     12 | IONQ     |            0.7  |        12,720 |      1,473,904 |        1,641 |     2,110,788 |
|     13 | AAPL     |            0.68 |         6,054 |     12,855,828 |       45,369 |    18,827,451 |
|     13 | WULF     |            0.68 |        13,132 |      1,633,737 |       27,020 |     2,406,020 |
|     15 | AVGO     |            0.63 |         9,640 |      9,034,180 |        3,749 |    14,356,700 |
|     16 | TLT      |            0.62 |        51,870 |      4,198,200 |       19,285 |     6,760,987 |
|     17 | IBIT     |            0.53 |        23,421 |      3,558,931 |       35,772 |     6,699,906 |
|     18 | SNDK     |            0.51 |         6,398 |     25,793,990 |        7,094 |    50,216,298 |
|     19 | GOOGL    |            0.49 |        19,436 |      9,423,785 |        4,709 |    19,393,450 |
|     19 | SLV      |            0.49 |        10,354 |      2,468,392 |        5,771 |     5,026,440 |
|     21 | TSM      |            0.43 |        12,884 |      6,923,020 |       17,175 |    16,139,838 |
|     22 | INTC     |            0.41 |        52,920 |     10,598,970 |        5,141 |    26,134,051 |
|     22 | MRVL     |            0.41 |         8,276 |      3,169,202 |        1,649 |     7,638,575 |
|     24 | QQQ      |            0.3  |        47,214 |     56,674,734 |       37,488 |   189,302,692 |
|     24 | CRWV     |            0.3  |        21,242 |      5,920,536 |       23,981 |    19,829,140 |
|     26 | SMH      |            0.28 |        12,585 |     10,591,187 |       13,141 |    38,021,540 |
|     27 | SPY      |            0.26 |        91,722 |     54,773,069 |      233,085 |   210,408,697 |
|     28 | NFLX     |            0.24 |        20,104 |      2,195,856 |        4,069 |     9,233,513 |
|     29 | COIN     |            0.09 |         3,572 |      1,841,626 |       12,071 |    21,205,189 |
|     29 | GLD      |            0.09 |        16,108 |      6,234,219 |       38,311 |    71,428,366 |
|     31 | BABA     |            0.07 |         8,260 |      3,634,345 |       10,713 |    54,666,848 |
|     32 | RKLB     |            0.05 |         3,112 |      1,400,454 |        4,442 |    26,586,290 |
|     33 | GOOG     |            0.04 |         6,119 |      3,233,891 |        5,728 |    76,067,178 |

## T1 — Top 4 Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL270115C00350000  |         2,260 |      3,661,200 | AAPL261120P00350000  |       25,066 |     7,394,470 |
| AAPL     | AAPL261120C00325000  |         1,230 |      3,386,190 | AAPL261218P00355000  |        3,908 |     4,169,836 |
| AAPL     | AAPL270115C00280000  |           417 |      3,135,423 | AAPL261218P00350000  |        4,994 |     4,105,068 |
| AAPL     | AAPL261218C00350000  |         2,147 |      2,673,015 | AAPL261118P00352500  |       11,401 |     3,158,077 |
| AMZN     | AMZN261118C00250000  |         3,821 |      3,328,091 | AMZN261118P00272500  |        3,744 |     5,559,840 |
| AMZN     | AMZN261218C00260000  |         3,203 |      3,283,075 | AMZN261118P00270000  |        3,997 |     5,124,154 |
| AMZN     | AMZN270115C00260000  |         1,964 |      2,826,196 | AMZN261120P00267500  |        2,970 |     3,341,250 |
| AMZN     | AMZN261218C00275000  |         5,367 |      2,388,315 | AMZN261218P00250000  |        3,562 |     2,685,748 |
| ARM      | ARM270115C00200000   |           747 |        956,160 | ARM261218P00170000   |        1,006 |     1,378,220 |
| ARM      | ARM270115C00145000   |           152 |        616,360 | ARM261218P00140000   |        1,911 |       840,840 |
| ARM      | ARM261218C00200000   |           694 |        527,440 | ARM270115P00160000   |          651 |       839,790 |
| ARM      | ARM261218C00180000   |           270 |        422,550 | ARM270115P00150000   |          497 |       497,000 |
| AVGO     | AVGO270115C00400000  |         2,628 |      2,391,480 | AVGO261218P00330000  |        2,287 |     5,145,750 |
| AVGO     | AVGO261120C00340000  |         2,950 |      2,256,750 | AVGO261120P00460000  |          275 |     3,492,500 |
| AVGO     | AVGO261218C00320000  |           680 |      2,204,560 | AVGO261120P00420000  |          332 |     2,888,400 |
| AVGO     | AVGO261218C00390000  |         3,382 |      2,181,390 | AVGO261218P00350000  |          855 |     2,830,050 |
| BABA     | BABA270115C00075000  |           810 |      1,543,050 | BABA270115P00145000  |        5,106 |    27,843,018 |
| BABA     | BABA261218C00090000  |         1,515 |        893,850 | BABA261218P00135000  |        3,361 |    14,990,060 |
| BABA     | BABA261218C00100000  |         2,738 |        618,788 | BABA261218P00140000  |        2,056 |    10,156,640 |
| BABA     | BABA261120C00095000  |         3,197 |        578,657 | BABA261218P00180000  |          190 |     1,677,130 |
| CIFR     | CIFR261120C00006500  |         3,985 |        183,310 | CIFR270115P00012000  |        2,058 |     1,148,364 |
| COIN     | COIN261120C00120000  |         1,439 |        625,965 | COIN261218P00160000  |        2,031 |     8,262,108 |
| COIN     | COIN261218C00125000  |           612 |        507,960 | COIN261218P00110000  |        9,239 |     5,423,293 |
| COIN     | COIN261120C00005000  |            32 |        366,720 | COIN261120P00180000  |          648 |     4,133,592 |
| COIN     | COIN261120C00125000  |         1,489 |        340,981 | COIN270115P00340000  |          153 |     3,386,196 |
| CRWV     | CRWV261120C00053000  |        12,339 |      2,023,596 | CRWV261218P00060000  |       13,022 |    16,316,566 |
| CRWV     | CRWV261218C00045000  |         2,154 |      1,882,596 | CRWV261120P00050000  |        5,470 |     1,624,590 |
| CRWV     | CRWV261120C00050000  |         4,133 |      1,190,304 | CRWV261218P00050000  |        1,735 |     1,058,350 |
| CRWV     | CRWV261120C00049500  |         2,616 |        824,040 | CRWV261218P00040000  |        3,754 |       829,634 |
| EOSE     | EOSE270115C00001500  |           302 |         13,590 | EOSE270115P00005500  |       75,671 |    28,603,638 |
| ETHA     | ETHA261120C00030000  |           222 |        249,750 | ETHA261120P00040000  |        6,388 |       427,996 |
| ETHA     | ETHA261120C00042000  |         2,716 |        187,404 | ETHA261204P00043000  |        1,009 |       308,754 |
| ETHA     | ETHA261120C00044000  |         3,491 |         87,275 | ETHA261127P00043000  |        1,110 |       307,470 |
| ETHA     | ETHA261218C00044000  |           363 |         60,984 | ETHA261120P00042000  |        1,795 |       288,995 |
| GLD      | GLD261218C00370000   |         7,917 |      3,364,725 | GLD270115P00355000   |       35,335 |    47,490,240 |
| GLD      | GLD270115C00295000   |           163 |      1,007,666 | GLD261218P00470000   |          750 |     8,703,750 |
| GLD      | GLD261218C00390000   |         7,880 |        969,240 | GLD261120P00420000   |        1,150 |     7,647,500 |
| GLD      | GLD270115C00296000   |           148 |        892,588 | GLD261218P00425000   |        1,076 |     7,586,876 |
| GOOG     | GOOG270115C00300000  |         1,123 |        971,395 | GOOG270115P00480000  |        2,716 |    54,146,176 |
| GOOG     | GOOG261218C00300000  |         1,646 |        813,124 | GOOG261120P00350000  |        1,413 |     9,799,155 |
| GOOG     | GOOG270115C00310000  |         1,306 |        733,972 | GOOG261120P00340000  |        1,159 |     6,760,447 |
| GOOG     | GOOG261120C00285000  |         2,044 |        715,400 | GOOG261218P00405000  |          440 |     5,361,400 |
| GOOGL    | GOOGL261218C00300000 |         4,552 |      2,635,608 | GOOGL261120P00350000 |          951 |     6,176,745 |
| GOOGL    | GOOGL270115C00300000 |         2,635 |      2,555,950 | GOOGL261120P00355000 |          785 |     5,491,075 |
| GOOGL    | GOOGL270115C00320000 |         4,786 |      2,120,198 | GOOGL261120P00365000 |          528 |     4,229,280 |
| GOOGL    | GOOGL261120C00290000 |         7,463 |      2,112,029 | GOOGL261218P00290000 |        2,445 |     3,496,350 |
| HIMS     | HIMS270115C00015000  |           745 |        327,800 | HIMS261218P00045000  |          186 |       480,066 |
| HIMS     | HIMS261211C00015000  |           453 |        172,140 | HIMS261120P00032000  |          223 |       289,900 |
| IBIT     | IBIT261218C00035000  |         4,049 |      1,255,190 | IBIT261218P00037000  |       10,728 |     2,091,960 |
| IBIT     | IBIT261218C00036000  |         3,301 |        808,745 | IBIT261120P00039000  |        8,531 |     1,970,661 |
| IBIT     | IBIT261120C00037000  |        11,401 |        752,466 | IBIT261218P00035000  |       13,727 |     1,578,605 |
| IBIT     | IBIT261224C00038000  |         4,670 |        742,530 | IBIT261218P00040000  |        2,786 |     1,058,680 |
| INTC     | INTC261120C00056000  |        17,180 |      3,607,800 | INTC261120P00100000  |        1,921 |     8,358,271 |
| INTC     | INTC270115C00070000  |        18,384 |      3,511,344 | INTC261120P00120000  |        1,000 |     6,375,000 |
| INTC     | INTC261127C00060000  |        13,791 |      1,875,576 | INTC261218P00105000  |        1,280 |     6,233,600 |
| INTC     | INTC270115C00060000  |         3,565 |      1,604,250 | INTC261218P00110000  |          940 |     5,167,180 |
| IONQ     | IONQ261120C00027000  |         8,672 |        789,152 | IONQ261218P00055000  |          298 |       837,082 |
| IONQ     | IONQ261120C00025500  |         2,270 |        365,470 | IONQ261120P00045000  |          282 |       510,420 |
| IONQ     | IONQ270115C00030000  |           912 |        200,640 | IONQ261120P00034000  |          534 |       416,520 |
| IONQ     | IONQ261218C00030000  |           866 |        118,642 | IONQ261120P00033000  |          527 |       346,766 |
| IREN     | IREN261120C00017000  |        11,392 |        888,576 | IREN261218P00025000  |        1,331 |     1,188,583 |
| IREN     | IREN261120C00016500  |         6,811 |        681,100 | IREN261120P00016000  |        9,264 |       833,760 |
| IREN     | IREN261218C00017000  |         3,246 |        668,676 | IREN261218P00017000  |        2,483 |       667,927 |
| IREN     | IREN261120C00013000  |         1,539 |        564,813 | IREN261218P00015000  |        4,014 |       658,296 |
| MARA     | MARA261120C00006500  |         7,034 |        309,496 | MARA270115P00006000  |        2,770 |       196,670 |
| MRVL     | MRVL261120C00155000  |         2,670 |        897,120 | MRVL261120P00240000  |          325 |     3,040,375 |
| MRVL     | MRVL261120C00160000  |         3,695 |        775,950 | MRVL270115P00145000  |        1,024 |     1,843,200 |
| MRVL     | MRVL261120C00150000  |         1,499 |        773,484 | MRVL261120P00230000  |          175 |     1,461,250 |
| MRVL     | MRVL270115C00150000  |           412 |        722,648 | MRVL261120P00250000  |          125 |     1,293,750 |
| MSTR     | MSTR270115C00110000  |        18,829 |     19,864,595 | MSTR261120P00150000  |          948 |     4,446,120 |
| MSTR     | MSTR261120C00104000  |         6,104 |      2,472,120 | MSTR261120P00145000  |        1,012 |     4,227,124 |
| MSTR     | MSTR261120C00103000  |         5,184 |      2,358,720 | MSTR261120P00140000  |        1,082 |     4,003,400 |
| MSTR     | MSTR270115C00100000  |         1,130 |      1,728,900 | MSTR261120P00135000  |        1,164 |     3,724,800 |
| NFLX     | NFLX261120C00062000  |        10,404 |        624,240 | NFLX261120P00080000  |        1,627 |     3,075,030 |
| NFLX     | NFLX270115C00062000  |         1,799 |        599,067 | NFLX261218P00090000  |          869 |     2,460,139 |
| NFLX     | NFLX261120C00061000  |         5,551 |        549,549 | NFLX261218P00080000  |        1,161 |     2,298,780 |
| NFLX     | NFLX261218C00063000  |         2,350 |        423,000 | NFLX261218P00095000  |          412 |     1,399,564 |
| NVDA     | NVDA261218C00170000  |        33,358 |     20,848,750 | NVDA270115P00180000  |        8,162 |    23,873,850 |
| NVDA     | NVDA261120C00160000  |        31,270 |     18,230,410 | NVDA261118P00155000  |       25,984 |    15,330,560 |
| NVDA     | NVDA261118C00160000  |        37,555 |     18,063,955 | NVDA261218P00155000  |       14,039 |    15,063,847 |
| NVDA     | NVDA270115C00170000  |        13,296 |     11,700,480 | NVDA261120P00150000  |       30,759 |    14,610,525 |
| QCOM     | QCOM261120C00065000  |            48 |        511,440 | QCOM261120P00162500  |        1,460 |       421,940 |
| QCOM     | QCOM261218C00185000  |         1,038 |        487,860 | QCOM261120P00170000  |          594 |       356,400 |
| QCOM     | QCOM261120C00070000  |            48 |        487,536 | QCOM261120P00200000  |           91 |       284,375 |
| QCOM     | QCOM261218C00170000  |           374 |        393,448 | QCOM261120P00167500  |          524 |       254,664 |
| QQQ      | QQQ261218C00665000   |        10,074 |     22,011,690 | QQQ261120P00760000   |        6,054 |    59,728,764 |
| QQQ      | QQQ261218C00700000   |        19,947 |     13,703,589 | QQQ261120P00730000   |        7,375 |    51,794,625 |
| QQQ      | QQQ261218C00680000   |         8,094 |     11,469,198 | QQQ261218P00660000   |       19,107 |    38,920,959 |
| QQQ      | QQQ261123C00666000   |         9,099 |      9,490,257 | QQQ261120P00740000   |        4,952 |    38,858,344 |
| RIOT     | RIOT261120C00017000  |        37,650 |      3,463,800 | RIOT261120P00016500  |        4,602 |       312,936 |
| RIOT     | RIOT261120C00018000  |        64,456 |      3,351,712 | RIOT261218P00014000  |        2,573 |       180,110 |
| RIOT     | RIOT270115C00017000  |         1,567 |        410,554 | RIOT261120P00016000  |        2,903 |       148,053 |
| RIOT     | RIOT261127C00017000  |         2,846 |        378,518 | RIOT261120P00017500  |        1,111 |       132,209 |
| RKLB     | RKLB270115C00030000  |           170 |        522,920 | RKLB270115P00165000  |        1,500 |    16,221,000 |
| RKLB     | RKLB270115C00065000  |         1,038 |        451,530 | RKLB261218P00110000  |        1,652 |     8,780,380 |
| RKLB     | RKLB270115C00075000  |           993 |        216,474 | RKLB270115P00130000  |          152 |     1,112,640 |
| RKLB     | RKLB261127C00060000  |           911 |        209,530 | RKLB261120P00060000  |        1,138 |       472,270 |
| SLV      | SLV270115C00030000   |           750 |        963,750 | SLV261231P00075000   |          762 |     2,480,310 |
| SLV      | SLV261218C00045000   |         5,127 |        625,494 | SLV270115P00058000   |          622 |       970,320 |
| SLV      | SLV270115C00045000   |         2,355 |        456,870 | SLV270115P00061000   |          432 |       792,720 |
| SLV      | SLV261218C00043000   |         2,122 |        422,278 | SLV261218P00042000   |        3,955 |       783,090 |
| SMCI     | SMCI261127C00025500  |         7,331 |      1,026,340 | SMCI261120P00025000  |        6,304 |       762,784 |
| SMCI     | SMCI261127C00026000  |         3,388 |        467,544 | SMCI261120P00035000  |          359 |       350,025 |
| SMCI     | SMCI261120C00026000  |         4,642 |        352,792 | SMCI261218P00028000  |          573 |       257,850 |
| SMCI     | SMCI261120C00025000  |         2,838 |        337,722 | SMCI261218P00025000  |          971 |       253,431 |
| SMH      | SMH270115C00550000   |         6,278 |      4,928,230 | SMH270115P00450000   |        4,794 |    14,549,790 |
| SMH      | SMH270115C00495000   |           976 |      2,128,656 | SMH261218P00450000   |        5,444 |    12,521,200 |
| SMH      | SMH261218C00520000   |         2,242 |      1,838,440 | SMH270115P00475000   |        1,336 |     5,544,400 |
| SMH      | SMH261211C00525000   |         3,089 |      1,695,861 | SMH261218P00475000   |        1,567 |     5,406,150 |
| SNDK     | SNDK261120C00850000  |         2,381 |      7,071,570 | SNDK261120P00800000  |        3,473 |    14,544,924 |
| SNDK     | SNDK261120C00820000  |         1,608 |      6,753,600 | SNDK261120P00820000  |        2,516 |    13,156,164 |
| SNDK     | SNDK261120C00800000  |         1,196 |      6,219,200 | SNDK261218P01000000  |          523 |    11,365,836 |
| SNDK     | SNDK261120C00810000  |         1,213 |      5,749,620 | SNDK261120P01000000  |          582 |    11,149,374 |
| SPY      | SPY261218C00745000   |        14,568 |     20,511,744 | SPY261120P00750000   |      105,212 |   133,619,240 |
| SPY      | SPY261120C00750000   |        41,163 |     13,007,508 | SPY261127P00725000   |       56,891 |    28,388,609 |
| SPY      | SPY261117C00740000   |        30,721 |     11,889,027 | SPY261120P00740000   |       36,432 |    26,012,448 |
| SPY      | SPY261218C00739000   |         5,270 |      9,364,790 | SPY261117P00745000   |       34,550 |    22,388,400 |
| TLT      | TLT261218C00080000   |        21,999 |      2,001,909 | TLT261120P00083000   |        6,780 |     2,420,460 |
| TLT      | TLT270115C00083000   |        20,852 |      1,000,896 | TLT261120P00084000   |        3,840 |     1,758,720 |
| TLT      | TLT261218C00079000   |         4,585 |        618,975 | TLT261120P00085000   |        2,941 |     1,608,727 |
| TLT      | TLT270115C00080000   |         4,434 |        576,420 | TLT261218P00080000   |        5,724 |       973,080 |
| TSLA     | TSLA261120C00400000  |        35,372 |      9,550,440 | TSLA270115P00350000  |        5,527 |     8,732,660 |
| TSLA     | TSLA261120C00380000  |         8,959 |      8,824,615 | TSLA261120P00377500  |        7,157 |     6,298,160 |
| TSLA     | TSLA261218C00300000  |           791 |      6,630,162 | TSLA261120P00380000  |        6,083 |     5,930,925 |
| TSLA     | TSLA261118C00380000  |         8,923 |      5,978,410 | TSLA261118P00380000  |        7,566 |     5,220,540 |
| TSM      | TSM261120C00380000   |         3,214 |      2,641,908 | TSM261218P00380000   |        2,001 |     4,818,408 |
| TSM      | TSM270115C00400000   |         1,029 |      1,726,662 | TSM270115P00320000   |        5,209 |     4,401,605 |
| TSM      | TSM261127C00400000   |         2,891 |      1,300,950 | TSM261120P00360000   |        7,510 |     4,280,700 |
| TSM      | TSM261120C00400000   |         5,750 |      1,253,500 | TSM270115P00330000   |        2,455 |     2,639,125 |
| UNH      | UNH261218C00410000   |         2,373 |      4,129,020 | UNH261218P00400000   |          651 |       781,851 |
| UNH      | UNH261211C00410000   |         2,159 |      3,065,780 | UNH261218P00410000   |          427 |       716,079 |
| UNH      | UNH261120C00135000   |            83 |      2,286,235 | UNH261218P00510000   |           63 |       638,820 |
| UNH      | UNH261120C00140000   |            83 |      2,244,735 | UNH261218P00420000   |          261 |       558,540 |
| WULF     | WULF261211C00011500  |         3,149 |        510,138 | WULF261218P00011000  |       15,204 |     1,474,788 |
| WULF     | WULF261120C00012000  |         7,343 |        447,923 | WULF261211P00011500  |        3,002 |       345,230 |
| WULF     | WULF270115C00011000  |         1,604 |        372,128 | WULF261120P00012000  |        4,029 |       294,117 |
| WULF     | WULF270115C00010000  |         1,036 |        303,548 | WULF261218P00010000  |        4,785 |       291,885 |
| XLF      | XLF261218C00040000   |           170 |        317,390 | XLF261218P00057000   |       18,843 |     1,526,283 |
| XLF      | XLF270115C00039000   |           142 |        279,030 | XLF261120P00057000   |       21,163 |       507,912 |
| XLF      | XLF270115C00038000   |            78 |        160,758 | XLF261120P00057500   |       18,214 |       473,564 |
| XLF      | XLF261218C00050000   |           170 |        148,580 | XLF261218P00056000   |        6,629 |       377,853 |
| XLU      | XLU261218C00045000   |        12,408 |        620,400 | XLU270115P00044000   |        3,111 |       342,210 |
| XLU      | XLU261218C00047500   |        12,031 |         84,217 | XLU261218P00042500   |       11,439 |       331,731 |
| ^VIX     | VIX261216C00029000   |        63,064 |      8,198,320 | VIX261216P00021000   |       21,984 |     5,539,968 |
| ^VIX     | VIX261118C00020500   |        39,355 |      7,989,065 | VIX261216P00018000   |       42,248 |     3,337,592 |
| ^VIX     | VIX261216C00023000   |        15,770 |      3,138,230 | VIX261216P00020000   |       15,826 |     2,959,462 |
| ^VIX     | VIX261118C00019000   |         7,108 |      2,629,960 | VIX261216P00017000   |       49,179 |     2,016,339 |

## T3 — Top 3 OTM Premiums per Ticker (rows ≥ $250,000)

| Ticker   | Call Contract        |   Call Volume |   Call Premium | Put Contract         |   Put Volume |   Put Premium |
|:---------|:---------------------|--------------:|---------------:|:---------------------|-------------:|--------------:|
| AAPL     | AAPL261118C00355000  |        12,190 |      2,364,860 | AAPL261120P00350000  |       25,066 |     7,394,470 |
| AAPL     | AAPL261218C00360000  |         2,342 |      1,630,032 | AAPL261218P00350000  |        4,994 |     4,105,068 |
| AAPL     | AAPL261120C00355000  |         4,878 |      1,585,350 | AAPL261118P00352500  |       11,401 |     3,158,077 |
| AMZN     | AMZN261218C00260000  |         3,203 |      3,283,075 | AMZN261218P00250000  |        3,562 |     2,685,748 |
| AMZN     | AMZN270115C00260000  |         1,964 |      2,826,196 | AMZN261218P00240000  |        5,390 |     2,457,840 |
| AMZN     | AMZN261218C00275000  |         5,367 |      2,388,315 | AMZN261120P00250000  |        5,762 |     1,313,736 |
| ARM      | ARM270115C00200000   |           747 |        956,160 | ARM261218P00170000   |        1,006 |     1,378,220 |
| ARM      | ARM261218C00200000   |           694 |        527,440 | ARM261218P00140000   |        1,911 |       840,840 |
| ARM      | ARM261218C00180000   |           270 |        422,550 | ARM270115P00160000   |          651 |       839,790 |
| AVGO     | AVGO270115C00400000  |         2,628 |      2,391,480 | AVGO261218P00330000  |        2,287 |     5,145,750 |
| AVGO     | AVGO261120C00340000  |         2,950 |      2,256,750 | AVGO261120P00330000  |        2,503 |     2,290,245 |
| AVGO     | AVGO261218C00390000  |         3,382 |      2,181,390 | AVGO261120P00320000  |        3,358 |     1,863,690 |
| BABA     | BABA261218C00100000  |         2,738 |        618,788 | BABA261120P00090000  |        1,606 |       481,800 |
| BABA     | BABA261120C00095000  |         3,197 |        578,657 | BABA261218P00090000  |          894 |       434,484 |
| BABA     | BABA270115C00095000  |           975 |        516,750 | BABA261120P00085000  |        2,421 |       309,888 |
| COIN     | COIN261120C00120000  |         1,439 |        625,965 | COIN261218P00110000  |        9,239 |     5,423,293 |
| COIN     | COIN261218C00125000  |           612 |        507,960 | COIN261218P00115000  |        1,438 |     1,118,764 |
| COIN     | COIN261120C00125000  |         1,489 |        340,981 | COIN261120P00110000  |        2,265 |       269,535 |
| CRWV     | CRWV261120C00053000  |        12,339 |      2,023,596 | CRWV261218P00040000  |        3,754 |       829,634 |
| CRWV     | CRWV261120C00050000  |         4,133 |      1,190,304 | CRWV270115P00040000  |        2,380 |       785,400 |
| CRWV     | CRWV261120C00055000  |         7,487 |        816,083 | CRWV261204P00045000  |        2,982 |       766,374 |
| ETHA     | ETHA261120C00042000  |         2,716 |        187,404 | ETHA261120P00040000  |        6,388 |       427,996 |
| GLD      | GLD261218C00370000   |         7,917 |      3,364,725 | GLD261218P00350000   |        1,877 |     1,556,033 |
| GLD      | GLD261218C00390000   |         7,880 |        969,240 | GLD261231P00350000   |        1,254 |     1,185,030 |
| GLD      | GLD261218C00367000   |         1,039 |        540,280 | GLD261218P00340000   |        2,396 |     1,150,080 |
| GOOG     | GOOG270115C00300000  |         1,123 |        971,395 | GOOG261120P00280000  |        2,630 |     1,196,650 |
| GOOG     | GOOG261218C00300000  |         1,646 |        813,124 | GOOG261211P00280000  |          754 |       723,840 |
| GOOG     | GOOG270115C00310000  |         1,306 |        733,972 | GOOG261120P00275000  |        2,435 |       681,800 |
| GOOGL    | GOOGL261218C00300000 |         4,552 |      2,635,608 | GOOGL261118P00282500 |        4,091 |     1,370,485 |
| GOOGL    | GOOGL270115C00300000 |         2,635 |      2,555,950 | GOOGL261120P00280000 |        3,520 |     1,337,600 |
| GOOGL    | GOOGL270115C00320000 |         4,786 |      2,120,198 | GOOGL270115P00265000 |        1,250 |     1,005,000 |
| IBIT     | IBIT261120C00037000  |        11,401 |        752,466 | IBIT261218P00035000  |       13,727 |     1,578,605 |
| IBIT     | IBIT261224C00038000  |         4,670 |        742,530 | IBIT270115P00035000  |        6,050 |     1,016,400 |
| IBIT     | IBIT270115C00037000  |         2,741 |        723,624 | IBIT261218P00036000  |        5,288 |       793,200 |
| INTC     | INTC261120C00056000  |        17,180 |      3,607,800 | INTC261120P00055000  |       11,007 |     2,289,456 |
| INTC     | INTC270115C00070000  |        18,384 |      3,511,344 | INTC270115P00050000  |        4,441 |     1,576,555 |
| INTC     | INTC261127C00060000  |        13,791 |      1,875,576 | INTC270115P00047000  |        4,860 |     1,249,020 |
| IONQ     | IONQ261120C00027000  |         8,672 |        789,152 | IONQ261127P00026000  |          805 |       112,700 |
| IREN     | IREN261120C00017000  |        11,392 |        888,576 | IREN261120P00016000  |        9,264 |       833,760 |
| IREN     | IREN261120C00016500  |         6,811 |        681,100 | IREN261218P00015000  |        4,014 |       658,296 |
| IREN     | IREN261218C00017000  |         3,246 |        668,676 | IREN270115P00016000  |        2,155 |       599,090 |
| MRVL     | MRVL261120C00155000  |         2,670 |        897,120 | MRVL270115P00145000  |        1,024 |     1,843,200 |
| MRVL     | MRVL261120C00160000  |         3,695 |        775,950 | MRVL261120P00145000  |        1,535 |     1,059,150 |
| MRVL     | MRVL261120C00150000  |         1,499 |        773,484 | MRVL261218P00120000  |        1,710 |       906,300 |
| MSTR     | MSTR270115C00110000  |        18,829 |     19,864,595 | MSTR261127P00100000  |        6,586 |     3,095,420 |
| MSTR     | MSTR261120C00104000  |         6,104 |      2,472,120 | MSTR261120P00100000  |        9,531 |     2,992,734 |
| MSTR     | MSTR261120C00105000  |         4,638 |      1,674,318 | MSTR261127P00090000  |       11,951 |     2,318,494 |
| NFLX     | NFLX261120C00062000  |        10,404 |        624,240 | NFLX270115P00052000  |       16,337 |     1,274,286 |
| NFLX     | NFLX270115C00062000  |         1,799 |        599,067 | NFLX261120P00059000  |       13,127 |       538,207 |
| NFLX     | NFLX261120C00061000  |         5,551 |        549,549 | NFLX261120P00060000  |        6,755 |       520,135 |
| NVDA     | NVDA261218C00170000  |        33,358 |     20,848,750 | NVDA261118P00155000  |       25,984 |    15,330,560 |
| NVDA     | NVDA261120C00160000  |        31,270 |     18,230,410 | NVDA261218P00155000  |       14,039 |    15,063,847 |
| NVDA     | NVDA261118C00160000  |        37,555 |     18,063,955 | NVDA261120P00150000  |       30,759 |    14,610,525 |
| QCOM     | QCOM261218C00185000  |         1,038 |        487,860 | QCOM261120P00162500  |        1,460 |       421,940 |
| QCOM     | QCOM261218C00170000  |           374 |        393,448 | QCOM261120P00167500  |          524 |       254,664 |
| QCOM     | QCOM261120C00175000  |         1,209 |        325,221 | QCOM261218P00155000  |          326 |       177,670 |
| QQQ      | QQQ261218C00665000   |        10,074 |     22,011,690 | QQQ261218P00660000   |       19,107 |    38,920,959 |
| QQQ      | QQQ261218C00700000   |        19,947 |     13,703,589 | QQQ261120P00660000   |       23,528 |    23,386,832 |
| QQQ      | QQQ261218C00680000   |         8,094 |     11,469,198 | QQQ261218P00655000   |       12,289 |    22,685,494 |
| RIOT     | RIOT261120C00018000  |        64,456 |      3,351,712 | RIOT261120P00016500  |        4,602 |       312,936 |
| RKLB     | RKLB270115C00065000  |         1,038 |        451,530 | RKLB261120P00057000  |        1,830 |       453,840 |
| RKLB     | RKLB270115C00075000  |           993 |        216,474 | RKLB261218P00055000  |          913 |       401,720 |
| SLV      | SLV261218C00045000   |         5,127 |        625,494 | SLV261218P00042000   |        3,955 |       783,090 |
| SLV      | SLV270115C00045000   |         2,355 |        456,870 | SLV261218P00040000   |        2,589 |       310,680 |
| SLV      | SLV261218C00043000   |         2,122 |        422,278 | SLV261120P00042000   |        3,469 |       267,113 |
| SMCI     | SMCI261127C00025500  |         7,331 |      1,026,340 | SMCI261120P00025000  |        6,304 |       762,784 |
| SMCI     | SMCI261127C00026000  |         3,388 |        467,544 | SMCI261218P00025000  |          971 |       253,431 |
| SMCI     | SMCI261120C00026000  |         4,642 |        352,792 | SMCI270115P00020000  |        1,290 |       176,730 |
| SMH      | SMH270115C00550000   |         6,278 |      4,928,230 | SMH270115P00450000   |        4,794 |    14,549,790 |
| SMH      | SMH270115C00495000   |           976 |      2,128,656 | SMH261218P00450000   |        5,444 |    12,521,200 |
| SMH      | SMH261218C00520000   |         2,242 |      1,838,440 | SMH261120P00450000   |        3,431 |     3,431,000 |
| SNDK     | SNDK261120C00850000  |         2,381 |      7,071,570 | SNDK261120P00800000  |        3,473 |    14,544,924 |
| SNDK     | SNDK261120C00820000  |         1,608 |      6,753,600 | SNDK261218P00600000  |        4,742 |     9,626,260 |
| SNDK     | SNDK261120C00810000  |         1,213 |      5,749,620 | SNDK261127P00800000  |        1,136 |     6,279,808 |
| SPY      | SPY261218C00745000   |        14,568 |     20,511,744 | SPY261127P00725000   |       56,891 |    28,388,609 |
| SPY      | SPY261120C00750000   |        41,163 |     13,007,508 | SPY261218P00712000   |       25,223 |    20,405,407 |
| SPY      | SPY261117C00740000   |        30,721 |     11,889,027 | SPY261127P00710000   |       66,572 |    17,841,296 |
| TLT      | TLT261218C00080000   |        21,999 |      2,001,909 | TLT261218P00079000   |        1,894 |       215,916 |
| TLT      | TLT270115C00083000   |        20,852 |      1,000,896 | TLT270115P00079000   |        1,010 |       142,410 |
| TLT      | TLT270115C00080000   |         4,434 |        576,420 | TLT261118P00079000   |       11,718 |       140,616 |
| TSLA     | TSLA261120C00400000  |        35,372 |      9,550,440 | TSLA270115P00350000  |        5,527 |     8,732,660 |
| TSLA     | TSLA261120C00380000  |         8,959 |      8,824,615 | TSLA261120P00377500  |        7,157 |     6,298,160 |
| TSLA     | TSLA261118C00380000  |         8,923 |      5,978,410 | TSLA270115P00310000  |        5,068 |     3,436,104 |
| TSM      | TSM261120C00380000   |         3,214 |      2,641,908 | TSM270115P00320000   |        5,209 |     4,401,605 |
| TSM      | TSM270115C00400000   |         1,029 |      1,726,662 | TSM261120P00360000   |        7,510 |     4,280,700 |
| TSM      | TSM261127C00400000   |         2,891 |      1,300,950 | TSM270115P00330000   |        2,455 |     2,639,125 |
| UNH      | UNH261120C00420000   |         2,042 |        765,750 | UNH261218P00400000   |          651 |       781,851 |
| UNH      | UNH261204C00425000   |           828 |        583,740 | UNH261218P00410000   |          427 |       716,079 |
| UNH      | UNH261218C00430000   |           679 |        580,545 | UNH261211P00410000   |          272 |       397,120 |
| WULF     | WULF261120C00012000  |         7,343 |        447,923 | WULF261218P00011000  |       15,204 |     1,474,788 |
| WULF     | WULF261218C00013000  |         2,471 |        252,042 | WULF261211P00011500  |        3,002 |       345,230 |
| WULF     | WULF261218C00014000  |         3,495 |        248,145 | WULF261218P00010000  |        4,785 |       291,885 |
| XLF      | XLF261218C00059000   |           560 |         50,960 | XLF261218P00057000   |       18,843 |     1,526,283 |
| XLF      | XLF261218C00060000   |           857 |         47,135 | XLF261120P00057000   |       21,163 |       507,912 |
| XLF      | XLF270115C00060000   |           389 |         32,676 | XLF261120P00057500   |       18,214 |       473,564 |
| XLU      | XLU261218C00045000   |        12,408 |        620,400 | XLU270115P00044000   |        3,111 |       342,210 |
| XLU      | XLU261218C00047500   |        12,031 |         84,217 | XLU261218P00042500   |       11,439 |       331,731 |
| ^VIX     | VIX261216C00029000   |        63,064 |      8,198,320 | VIX261216P00021000   |       21,984 |     5,539,968 |
| ^VIX     | VIX261216C00023000   |        15,770 |      3,138,230 | VIX261216P00018000   |       42,248 |     3,337,592 |
| ^VIX     | VIX261216C00030000   |        22,975 |      2,573,200 | VIX261216P00020000   |       15,826 |     2,959,462 |

*premium = volume × lastPrice × 100 · OTM = calls strike>spot, puts strike<spot · T4 uses the cleaned chain: ≥2 DTE, OTM only, leveraged ETFs folded into their underlying, ^VIX ratio inverted · Net Signed Premium = bought calls/sold puts minus sold calls/bought puts, side from lastPrice vs bid/ask (prints outside the closing quote are not signed) · generated by options-flow-pipeline*

---

**Data quality:** requested: 52 · fetched: 52 · failed: 0 · gated: 9 · stale volume: 20,407 contracts (30% of premium) dropped

_Signal check (next-day rank correlation, last 20 sessions): composite IC -0.002 (t -0.0, n=20) · flow_pct IC -0.089 (t -2.1, n=20) · trend_pct IC +0.090 (t +1.4, n=20)_

_Signal check, next 5 sessions (rank correlation, last 20 resolved sessions; windows overlap, so t is overstated): composite IC -0.063 (t -1.4, n=20) · flow_pct IC -0.103 (t -3.1, n=20) · trend_pct IC +0.018 (t +0.4, n=20)_