/* W26 — An EPSgram for Kuala Lumpur from a real ECMWF ENS forecast
   (51 members, open data at 0.25°, via Open-Meteo, issued for 3 Oct 2026;
   data/series/kl-ens-2026-10-03.json). Each day is a box: the line in the
   middle is the median, the box spans the 25th–75th percentiles and the
   whiskers the 10th–90th. Switch to "control only" to see what a single
   run would have told you, or to all 51 members. Tap or drag a day. */

import { loadData } from '../content.js';
import { s, h, clamp, track, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('EPSgram：吉隆坡的 51 个成员预报', 'EPSgram: 51 members for Kuala Lumpur', 'EPSgram: 51 ahli untuk Kuala Lumpur'),
  rain: T('每日雨量（毫米）', 'Daily rain (mm)', 'Hujan harian (mm)'), tmax: T('最高气温（°C）', 'Maximum temperature (°C)', 'Suhu maksimum (°C)'),
  boxes: T('箱形图', 'Boxes', 'Kotak'), ctl: T('只看 control', 'Control only', 'Kawalan sahaja'), all: T('全部 51 个成员', 'All 51 members', 'Semua 51 ahli'),
  read: { med: T('中位数', 'median', 'median'), p10: T('10%', '10th', 'ke-10'), p90: T('90%', '90th', 'ke-90'), ctl: T('control', 'control', 'kawalan'), wet: T('有几成成员超过 10 毫米', 'members above 10 mm', 'ahli melebihi 10 mm') },
};
const q = (arr, f) => { const a = [...arr].sort((x, y) => x - y), i = (a.length - 1) * f, lo = Math.floor(i); return a[lo] + (a[Math.min(a.length - 1, lo + 1)] - a[lo]) * (i - lo); };

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const d = await loadData('series/kl-ens-2026-10-03');
  const n = d.days.length;
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), PH = Math.round(W * 0.34), H = PH * 2 + 40;
  const M = { l: 34, r: 8 };
  const x = i => M.l + (W - M.l - M.r) * (i + 0.5) / n, bw = (W - M.l - M.r) / n * 0.6;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const tabs = h('div', { class: 'stage-chips' }), out = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  let mode = 'boxes', at = 0;
  const panel = (key, y0, lo, hi, ticks, colour) => {
    const Y = v => y0 + PH - (PH - 8) * (v - lo) / (hi - lo);
    const g = [s('text', { x: M.l, y: y0 - 4, class: 'unit' }, p(L[key]))];
    for (const t of ticks) g.push(s('line', { x1: M.l, x2: W - M.r, y1: Y(t), y2: Y(t), class: 'grid' }), s('text', { x: M.l - 4, y: Y(t) + 4, 'text-anchor': 'end', class: 'chart-tick' }, String(t)));
    d[key].forEach((m, i) => {
      if (mode === 'ctl') g.push(s('circle', { cx: x(i), cy: Y(m[0]), r: 3.5, style: `fill: var(--${colour})` }));
      else if (mode === 'all') m.forEach((v, j) => g.push(s('circle', { cx: x(i) + (j % 7 - 3) * bw / 8, cy: Y(v), r: j ? 1.6 : 3, style: `fill: var(--${j ? colour : 'ink'}); fill-opacity: ${j ? 0.55 : 1}` })));
      else {
        const [a, b, c, e, f] = [0.1, 0.25, 0.5, 0.75, 0.9].map(k => q(m, k));
        g.push(s('line', { x1: x(i), x2: x(i), y1: Y(a), y2: Y(f), style: `stroke: var(--${colour})` }),
          s('rect', { x: x(i) - bw / 2, y: Y(e), width: bw, height: Math.max(1, Y(b) - Y(e)), style: `fill: var(--${colour}); fill-opacity: .3; stroke: var(--${colour})` }),
          s('line', { x1: x(i) - bw / 2, x2: x(i) + bw / 2, y1: Y(c), y2: Y(c), style: 'stroke: var(--ink); stroke-width: 2' }));
      }
    });
    return g;
  };
  function draw() {
    const rmax = Math.max(20, Math.ceil(Math.max(...d.rain.flat()) / 10) * 10);
    const sel = s('rect', { x: x(at) - bw * 0.85, y: 6, width: bw * 1.7, height: H - 22, class: 'ens-sel' });
    const labels = d.days.map((day, i) => (i % 2 === 0 ? s('text', { x: x(i), y: H - 4, 'text-anchor': 'middle', class: 'chart-tick' }, `${Number(day.slice(8))}/${Number(day.slice(5, 7))}`) : null));
    svg.replaceChildren(sel, ...panel('tmax', 16, 26, 35, [28, 31, 34], 'mercury'), ...panel('rain', PH + 34, 0, rmax, [0, rmax / 2, rmax], 'rain'), ...labels);
    const r = d.rain[at], t = d.tmax[at];
    const wet = r.filter(v => v > 10).length;
    out.textContent = `${d.days[at]} · ${p(L.tmax)}: ${p(L.read.med)} ${fmt(q(t, 0.5), 1)} (${p(L.read.ctl)} ${t[0]}) · ${p(L.rain)}: ${p(L.read.med)} ${fmt(q(r, 0.5), 1)}, ${p(L.read.p10)}–${p(L.read.p90)} ${fmt(q(r, 0.1), 1)}–${fmt(q(r, 0.9), 1)} (${p(L.read.ctl)} ${r[0]}) · ${wet}/51 ${p(L.read.wet)}`;
    tabs.replaceChildren(...['boxes', 'ctl', 'all'].map(k => { const b = h('button', { type: 'button', class: `chip${k === mode ? ' is-on' : ''}` }, p(L[k])); b.addEventListener('click', () => { mode = k; draw(); }); return b; }));
  }
  track(svg, pt => { const i = clamp(Math.floor((pt.x - M.l) / ((W - M.l - M.r) / n)), 0, n - 1); if (i !== at) { at = i; draw(); } });
  svg.setAttribute('tabindex', '0');
  svg.addEventListener('keydown', e => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { at = clamp(at + (e.key === 'ArrowRight' ? 1 : -1), 0, n - 1); draw(); e.preventDefault(); } });
  draw();
  el.append(frame({ title: p(L.title), lang, source: 'ECMWF IFS ENS open data (CC BY 4.0) via Open-Meteo Ensemble API, fetched 3 Oct 2026', children: [tabs, svg, out] }));
  return { destroy() { el.replaceChildren(); } };
}
