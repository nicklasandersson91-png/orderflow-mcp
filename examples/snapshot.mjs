// Print the order book walls and key levels for one Swiftedge market (Node 18+).
//
//   node snapshot.mjs          # Bitcoin
//   node snapshot.mjs gold     # btc, eth, sol, xrp, gold, silver, us500, us100, oil
//
// Free, no key. Data: https://swiftedge.uk/developers

const API = "https://swiftedge.uk/api/v1";

async function get(path, params = {}) {
  const q = new URLSearchParams({ ...params, src: "github" });
  const r = await fetch(`${API}/${path}?${q}`);
  if (!r.ok) throw new Error(`${path}: HTTP ${r.status}`);
  return r.json();
}

const usd = (v) => "$" + Math.round(v).toLocaleString("en-US");

const market = process.argv[2] || "btc";
const snap = await get("snapshot", { market });
console.log(`${snap.name}  ${snap.price_usd}  (${snap.updated})`);
for (const side of ["asks", "bids"]) {
  for (const w of (snap.order_book_walls?.[side] || []).slice(0, 3)) {
    console.log(`  ${side.slice(0, -1).padEnd(4)} wall  ${String(w.price).padEnd(12)} ${usd(w.size_usd)}`);
  }
}
const levels = await get("key-levels", { market });
console.log("Key levels above:");
for (const lv of (levels.above || []).slice(0, 5)) console.log(`  ${String(lv.price).padEnd(12)} ${lv.level.padEnd(45)} +${lv.distance_pct} %`);
console.log("Key levels below:");
for (const lv of (levels.below || []).slice(0, 5)) console.log(`  ${String(lv.price).padEnd(12)} ${lv.level.padEnd(45)} -${Math.abs(lv.distance_pct)} %`);
console.log("Live heatmap:", snap.links.live_heatmap);
