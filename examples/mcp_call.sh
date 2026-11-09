#!/usr/bin/env bash
# Talk to the Swiftedge MCP server with plain curl (Streamable HTTP, stateless, no key).
#   bash mcp_call.sh            # key levels for gold
#   bash mcp_call.sh btc        # any market code
set -euo pipefail
URL="https://swiftedge.uk/mcp"
MARKET="${1:-gold}"
H=(-H "Content-Type: application/json" -H "Accept: application/json, text/event-stream")

echo "== initialize"
curl -s "${H[@]}" "$URL" -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"curl-example","version":"1.0"}}}'
echo; echo "== tools/list"
curl -s "${H[@]}" "$URL" -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
echo; echo "== tools/call get_key_levels ($MARKET)"
curl -s "${H[@]}" "$URL" -d "{\"jsonrpc\":\"2.0\",\"id\":3,\"method\":\"tools/call\",\"params\":{\"name\":\"get_key_levels\",\"arguments\":{\"market\":\"$MARKET\"}}}"
echo
