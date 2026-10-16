# data/

Saved JSON snapshots, one subfolder per source.

| Folder | Contents | Written by |
|---|---|---|
| `dealer-edge/` | `dealer-edge-DATE.json` TradeEcho Dealer Edge GEX/VEX per day | watchlist routine |
| `term-structure/` | `raw/DATE.json` captures + `built-DATE.json` page data for the single-stock term structure | term-structure daily task (`term-structure/build.py`) |
| `terrashade/` | `terrashade-DATE.json` key-level snapshots | TerraShade Monitor |

The `tidy_data.yml` workflow moves any JSON still written to the old flat paths
(`data/dealer-edge-*.json`, `term-structure/data/...`) into these folders on push.
