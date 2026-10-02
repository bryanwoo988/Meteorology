/* W27 — How forecast skill falls with lead time, and how it has improved.
   SCHEMATIC curves of a skill score (anomaly correlation of 500 hPa
   height, where 100 % is perfect and 80 % is ECMWF's headline threshold
   for a useful forecast), shifted by about one day per decade —
   Simmons & Hollingsworth (2002); ECMWF (headline scores; forecast
   performance 2017). The curve shapes are illustrative, not ECMWF data. */

import { s, h, clamp, slider, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('预报准确度：滑动预报天数', 'Forecast skill: slide the lead time', 'Kemahiran ramalan: seret tempoh ramalan'),
  day: T('预报第几天', 'Forecast day', 'Hari ramalan'), useful: T('80 % 门槛', '80 % threshold', 'Ambang 80 %'),
  score: T('准确度（示意）', 'Skill (schematic)', 'Kemahiran (skematik)'),
  note: T('曲线形状是示意，不是 ECMWF 的真实数据；真实情况是：大约每十年，同样准确度的预报可以多看一天。', 'The curve shapes are a sketch, not ECMWF data; what is real is the trend — about one more day of equally good forecasts every decade.', 'Bentuk lengkung ialah lakaran, bukan data ECMWF; yang benar ialah aliran — kira-kira satu hari lagi ramalan sama baik setiap dekad.'),
};
const ERAS = [[1985, 'muted'], [2005, 'sky'], [2025, 'mercury']];
const skill = (day, era) => { const d80 = 6 + (era - 1985) / 10; return 100 / (1 + Math.exp((day - d80 - 1.55) / 1.1)) ; };  // reaches ~80 % at d80

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.56);
  const M = { l: 34, r: 10, t: 12, b: 26 };
  const X = d => M.l + (W - M.l - M.r) * d / 15, Y = v => M.t + (H - M.t - M.b) * (1 - v / 100);
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  for (const v of [0, 50, 80, 100]) svg.append(s('line', { x1: M.l, x2: W - M.r, y1: Y(v), y2: Y(v), class: v === 80 ? 'ref-line' : 'grid' }), s('text', { x: M.l - 4, y: Y(v) + 4, 'text-anchor': 'end', class: 'chart-tick' }, `${v}`));
  svg.append(s('text', { x: W - M.r - 4, y: Y(80) - 4, 'text-anchor': 'end', class: 'ref-label' }, p(L.useful)));
  for (let d = 0; d <= 15; d += 3) svg.append(s('text', { x: X(d), y: H - 8, 'text-anchor': 'middle', class: 'chart-tick' }, String(d)));
  for (const [era, c] of ERAS) {
    let path = ''; for (let d = 0; d <= 15; d += 0.25) path += `${d ? 'L' : 'M'}${X(d).toFixed(1)},${Y(skill(d, era)).toFixed(1)}`;
    svg.append(s('path', { d: path, class: 'series', style: `stroke: var(--${c})` }));
  }
  const cursor = s('line', { y1: M.t, y2: H - M.b, class: 'w-guide' }); svg.append(cursor);
  const rows = readout(ERAS.map(([era]) => [String(era), String(era)]));
  let day = 7;
  const ds = slider({ label: p(L.day), min: 0, max: 15, step: 0.5, value: day, onInput: v => { day = v; draw(); } });
  function draw() { cursor.setAttribute('x1', X(day)); cursor.setAttribute('x2', X(day)); for (const [era] of ERAS) rows.set(String(era), `${fmt(skill(day, era), 0)} %`); }
  draw();
  const legend = h('ul', { class: 'chart-legend' }, ...ERAS.map(([era, c]) => h('li', {}, h('span', { class: 'swatch', style: `--c: var(--${c})` }), String(era))));
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Simmons & Hollingsworth 2002 (QJRMS 128); ECMWF headline scores', children: [legend, svg, h('div', { class: 'w-controls' }, ds), rows, h('p', { class: 'w-source' }, p(L.note))] }));
  return { destroy() { el.replaceChildren(); } };
}
