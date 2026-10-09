// TradeEcho Dealer Edge capture — run in the browser on https://app.tradeecho.com while signed in
// (DevTools console, or Claude's browser javascript tool). Your session token never leaves the page.
//
// Output: compact JSON snapshot used by build.py.
//   - In DevTools: a file te_capture_YYYY-MM-DD.json is downloaded -> move it to data/raw/YYYY-MM-DD.json
//   - Via Claude: the JSON string is returned as the last expression
//
// Units kept raw-ish: gamma in contracts (build.py shows K), vex in $M (2dp).

(async () => {
  const TICKERS = (window.TE_TICKERS || ['NVDA', 'TSLA', 'AAPL', 'AMZN', 'GOOGL', 'AVGO']);
  const KEEP_EXPIRIES = window.TE_KEEP || 6;          // per-strike rows kept for the next N expiries
  const tok = localStorage.getItem('access_token');
  if (!tok) throw new Error('Not signed in to TradeEcho (no access_token in this tab)');

  const today = new Date().toISOString().slice(0, 10);
  const out = { capturedAt: new Date().toISOString(), source: 'tradeecho gamma-analysis', tickers: {} };

  for (const t of TICKERS) {
    const res = await fetch('https://api.tradeecho.com/api/gamma-analysis/' + t, {
      headers: { Authorization: 'Bearer ' + tok }, credentials: 'include'
    });
    const j = await res.json();
    if (!j || !j.data) { out.tickers[t] = { error: (j && j.message) || ('HTTP ' + res.status) }; continue; }
    const d = j.data, m = d.metadata;
    const exps = [...new Set(d.data.map(r => r.expiration.slice(0, 10)))].sort();
    const keep = exps.filter(e => e > today).slice(0, KEEP_EXPIRIES);
    const sums = {};
    for (const r of d.data) {
      const e = r.expiration.slice(0, 10);
      sums[e] = sums[e] || [0, 0];
      sums[e][0] += r.gamma; sums[e][1] += r.vex;
    }
    for (const e in sums) sums[e] = [Math.round(sums[e][0]), Math.round(sums[e][1] / 1e4) / 100];
    const rows = d.data
      .filter(r => keep.includes(r.expiration.slice(0, 10)))
      .map(r => [r.expiration.slice(5, 10), r.strike, Math.round(r.gamma), Math.round(r.vex / 1e4) / 100]);
    out.tickers[t] = {
      spot: m.currentPrice, rating: m.gexRating, kl: m.keyLevels,
      outlook: ((d.aiAnalysis && d.aiAnalysis.marketOutlook) || '').slice(0, 90),
      updated: d.dataUpdatedAt, posDate: d.freshness && d.freshness.positionsDate, stale: d.stale,
      sums, rows
    };
  }

  const json = JSON.stringify(out);
  if (!window.TE_NO_DOWNLOAD) {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([json], { type: 'application/json' }));
    a.download = 'te_capture_' + today + '.json';
    a.click();
  }
  return json;
})();
