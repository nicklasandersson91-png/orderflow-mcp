# Swiftedge order flow: free MCP server and API

Free, live **order flow data** for AI assistants and your own code: order book depth and walls, candles with buy/sell volume and
CVD, large trades, real liquidations, an estimated liquidation map, funding, open interest and key price levels for **Bitcoin,
Ethereum, Solana, XRP, gold, silver, the US 500, the US 100 and WTI crude oil**.

- **MCP server:** `https://swiftedge.uk/mcp` (Streamable HTTP, no key, no account)
- **REST API:** `https://swiftedge.uk/api/v1/...` (JSON, no key, no account)
- **OpenAPI 3.1:** [`/api/v1/openapi.json`](https://swiftedge.uk/api/v1/openapi.json) (also works as a ChatGPT GPT action)
- **Docs:** [swiftedge.uk/developers](https://swiftedge.uk/developers?utm_source=github&utm_medium=readme)
- **Listed in the official MCP Registry** as `uk.swiftedge/orderflow`

The same numbers are drawn live in [Swiftedge Depth](https://swiftedge.uk/depth?utm_source=github&utm_medium=readme), a free
order book heatmap with every trade, a footprint chart and 30+ indicators in the browser.

## Live pages for every market

Every market trades 24/7 on Swiftedge. Each one has a free live order book heatmap and a levels page that is updated all day.
The sessions pages show when the underlying market opens, closes and releases data, in your own time zone.

| Market | Live heatmap | Levels today | Trading sessions | Guide |
|---|---|---|---|---|
| Bitcoin | [/depth](https://swiftedge.uk/depth) | [/btc/levels](https://swiftedge.uk/btc/levels) | [/btc/sessions](https://swiftedge.uk/btc/sessions) | [Bitcoin levels explained](https://swiftedge.uk/guide/bitcoin-levels-explained) |
| Gold | [/gold/depth](https://swiftedge.uk/gold/depth) | [/gold/levels](https://swiftedge.uk/gold/levels) | [/gold/sessions](https://swiftedge.uk/gold/sessions) | [Gold order flow](https://swiftedge.uk/guide/gold-order-flow) |
| Silver | [/silver/depth](https://swiftedge.uk/silver/depth) | [/silver/levels](https://swiftedge.uk/silver/levels) | [/silver/sessions](https://swiftedge.uk/silver/sessions) | [Silver order flow](https://swiftedge.uk/guide/silver-order-flow) |
| WTI crude oil | [/wti/depth](https://swiftedge.uk/wti/depth) | [/wti/levels](https://swiftedge.uk/wti/levels) | [/wti/sessions](https://swiftedge.uk/wti/sessions) | [Oil order flow](https://swiftedge.uk/guide/oil-order-flow) |
| US 100 | [/us100/depth](https://swiftedge.uk/us100/depth) | [/us100/levels](https://swiftedge.uk/us100/levels) | [/us100/sessions](https://swiftedge.uk/us100/sessions) | [US 100 order flow](https://swiftedge.uk/guide/us-100-order-flow) |
| US 500 | [/sp500/depth](https://swiftedge.uk/sp500/depth) | [/sp500/levels](https://swiftedge.uk/sp500/levels) | | |
| Ethereum | [/eth/depth](https://swiftedge.uk/eth/depth) | [/eth/levels](https://swiftedge.uk/eth/levels) | | |
| Solana | [/sol/depth](https://swiftedge.uk/sol/depth) | [/sol/levels](https://swiftedge.uk/sol/levels) | | |
| XRP | [/xrp/depth](https://swiftedge.uk/xrp/depth) | [/xrp/levels](https://swiftedge.uk/xrp/levels) | | |

More guides: [silver levels](https://swiftedge.uk/guide/silver-levels-explained),
[oil levels](https://swiftedge.uk/guide/oil-levels-explained), [US 100 levels](https://swiftedge.uk/guide/us-100-levels-explained)
and [Bitcoin trading sessions](https://swiftedge.uk/guide/bitcoin-trading-sessions). The weekly
[COT report](https://swiftedge.uk/cot) covers all nine markets, and the [economic calendar](https://swiftedge.uk/economic-calendar)
shows how much past releases moved the markets in the first hour.

## Connect it to your AI app

**Claude** (claude.ai or the desktop app): Settings → Connectors → Add custom connector, and paste `https://swiftedge.uk/mcp`.

**Claude Code:**

```bash
claude mcp add --transport http swiftedge https://swiftedge.uk/mcp
```

**Cursor and other clients with an `mcp.json`:**

```json
{
  "mcpServers": {
    "swiftedge": { "url": "https://swiftedge.uk/mcp" }
  }
}
```

**ChatGPT:** import [`openapi.json`](https://swiftedge.uk/api/v1/openapi.json) as a GPT action.

Then ask, for example:

- "Where are the biggest bid walls on gold right now?"
- "Show me Bitcoin's CVD on the 4-hour chart."
- "Where would longs on Solana get liquidated?"
- "How much does CPI usually move gold in the first hour?"

## Tools

Every tool is read-only. Each one is also a plain GET endpoint on `https://swiftedge.uk`.

| MCP tool | REST endpoint | What you get |
|---|---|---|
| `list_markets` | `/api/v1/markets` | The markets and their codes |
| `get_market_snapshot` | `/api/v1/snapshot?market=btc` | Price, today's range, order book walls, resting liquidity, positioning levels, funding, open interest, large trades and liquidations near price |
| `get_markets_overview` | `/api/v1/markets-overview` | Every market in one table: price, change since 00:00 UTC, funding, 24-hour open interest change and the positioning flip |
| `get_order_book` | `/api/v1/order-book?market=btc` | The live order book grouped by price level: largest bids and asks, resting USD per side and the imbalance |
| `get_candles` | `/api/v1/candles?market=btc&timeframe=4h` | OHLC candles with volume split into aggressive buying and selling, delta and cumulative volume delta (CVD) |
| `get_large_trades` | `/api/v1/large-trades?market=btc` | Large aggressive market orders in the last 24 hours: totals, per hour, the 10 largest and the 10 latest |
| `get_liquidations` | `/api/v1/liquidations?market=btc` | Liquidations that really happened in the last 1-24 hours, longs and shorts in USD |
| `get_liquidation_heatmap` | `/api/v1/liquidation-heatmap?market=btc` | Where leveraged positions would be liquidated within 5 % of price, with the largest clusters |
| `get_funding_and_open_interest` | `/api/v1/funding-and-open-interest?market=btc` | Funding (8-hour and annualized), next funding time, open interest and its 1/4/24-hour change |
| `get_key_levels` | `/api/v1/key-levels?market=gold` | Today's important prices above and below the live price: walls, positioning levels, high, low and open |
| `get_economic_calendar` | `/api/v1/economic-calendar?days=7` | Upcoming releases (CPI, jobs, central banks) with how much markets moved in the first hour after past releases |
| `get_research_studies` | `/api/v1/research-studies` | Swiftedge's published studies with links and headline findings |

Market codes: `btc`, `eth`, `sol`, `xrp`, `gold`, `silver`, `us500`, `us100`, `oil`. `/api/v1/markets` always lists the current set.

## Use the REST API

```bash
curl "https://swiftedge.uk/api/v1/snapshot?market=btc&src=github"
curl "https://swiftedge.uk/api/v1/key-levels?market=gold&src=github"
```

Python ([`examples/snapshot.py`](examples/snapshot.py)) and JavaScript ([`examples/snapshot.mjs`](examples/snapshot.mjs)) examples
print the order book walls and key levels for any market. [`examples/mcp_call.sh`](examples/mcp_call.sh) talks to the MCP server
with plain `curl`.

## Good to know

- **Free, no key.** Please link to [swiftedge.uk](https://swiftedge.uk/?utm_source=github&utm_medium=readme) when you show the
  data, for example under a chart or in a bot's reply.
- **Freshness.** A snapshot is at most about 15 seconds old, the order book about 10 seconds and the liquidation map about
  5 minutes. Responses are cached for 15 seconds, so polling faster returns the same numbers.
- **Fair use.** The same limit as the rest of the site.
- **What the numbers are.** Swiftedge's own calculations on public perpetual futures order books and trades. Positioning levels
  and the liquidation map are estimates, not measurements and not a forecast. The data is descriptive and places no orders.
- **Live chart.** For tick-by-tick data, open the [live heatmap](https://swiftedge.uk/depth?utm_source=github&utm_medium=readme).
  You can also [paper trade](https://swiftedge.uk/paper-trading?utm_source=github&utm_medium=readme) on the live order book and
  join the free [Order Flow Cup](https://swiftedge.uk/trading-competition?utm_source=github&utm_medium=readme).

## License

The example code and this README are MIT licensed (see [LICENSE](LICENSE)). The API and MCP server are a free service run by
Swiftedge, provided as is.
