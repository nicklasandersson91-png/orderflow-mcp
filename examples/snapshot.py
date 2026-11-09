"""Print the order book walls and key levels for one Swiftedge market.

    python snapshot.py            # Bitcoin
    python snapshot.py gold       # btc, eth, sol, xrp, gold, silver, us500, us100, oil

Free, no key. Data: https://swiftedge.uk/developers
"""
import json
import sys
import urllib.request

API = "https://swiftedge.uk/api/v1"


def get(path, **params):
    params["src"] = "github"
    query = "&".join("%s=%s" % kv for kv in params.items())
    # Send a named User-Agent: the default "Python-urllib" agent is refused by the site's bot protection.
    req = urllib.request.Request("%s/%s?%s" % (API, path, query), headers={"User-Agent": "swiftedge-api-example/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def usd(v):
    return "$%s" % format(round(v), ",")


def main():
    market = sys.argv[1] if len(sys.argv) > 1 else "btc"
    snap = get("snapshot", market=market)
    print("%s  %s  (%s)" % (snap["name"], snap["price_usd"], snap["updated"]))
    walls = snap.get("order_book_walls", {})
    for side in ("asks", "bids"):
        for w in walls.get(side, [])[:3]:
            print("  %-4s wall  %-12s %s" % (side[:-1], w["price"], usd(w["size_usd"])))
    levels = get("key-levels", market=market)
    print("Key levels above:")
    for lv in levels.get("above", [])[:5]:
        print("  %-12s %-45s %+.2f %%" % (lv["price"], lv["level"], lv["distance_pct"]))
    print("Key levels below:")
    for lv in levels.get("below", [])[:5]:
        print("  %-12s %-45s %+.2f %%" % (lv["price"], lv["level"], -abs(lv["distance_pct"])))
    print("Live heatmap:", snap["links"]["live_heatmap"])


if __name__ == "__main__":
    main()
