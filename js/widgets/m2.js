/* M2 — The global circulation on a map: pressure belts, trade winds,
   westerlies, polar easterlies, and the ITCZ moving with the seasons.
   Ahrens pp. 194–199; Mote & Sahu pp. 67–71. The belts shift north in July
   and south in January by roughly 10–15° a year (Ahrens p. 199); the
   ITCZ line here is schematic. Drag the month. */

import { baseMap } from '../maps.js';
import { h, clamp, slider, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('全球环流：拖动月份看 ITCZ 移动', 'The global circulation: drag the month to move the ITCZ', 'Peredaran global: seret bulan untuk menggerakkan ITCZ'),
  month: T('月份', 'Month', 'Bulan'),
  itcz: T('ITCZ（热带辐合带）', 'ITCZ', 'ITCZ'), sth: T('副热带高压（约 30°）', 'Subtropical highs (≈ 30°)', 'Tekanan tinggi subtropika (≈ 30°)'),
  spl: T('副极地低压（约 60°）', 'Subpolar lows (≈ 60°)', 'Tekanan rendah subkutub (≈ 60°)'),
  trades: T('信风', 'Trade winds', 'Angin pasat'), west: T('西风带', 'Westerlies', 'Angin barat'), east: T('极地东风', 'Polar easterlies', 'Angin timur kutub'),
};
const MONTHS = {
  zh: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
  en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  ms: ['Jan', 'Feb', 'Mac', 'Apr', 'Mei', 'Jun', 'Jul', 'Ogo', 'Sep', 'Okt', 'Nov', 'Dis'],
};

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const m = await baseMap('world', { width: W, label: p(L.title) });
  let month = 1;
  // Belts and the ITCZ shift north in July, south in January; ±6° is an illustrative swing.
  const shift = mo => 6 * Math.cos((mo - 7) * Math.PI / 6);
  const parallel = lat => { const pts = []; for (let lon = -180; lon <= 180; lon += 6) pts.push([lon, lat]); return pts; };
  // Fewer, longer arrows on a narrow screen so the coastlines stay readable.
  const step = W < 480 ? 72 : 40, k = W < 480 ? 1.3 : 1;
  const arrows = (lat, dLon, dLat) => { const a = []; for (let lon = -150; lon <= 160; lon += step) a.push({ from: [lon, lat], to: [lon + dLon * k, lat + dLat * k], color: 'leaf' }); return a; };
  const legend = h('ul', { class: 'chart-legend' },
    h('li', {}, h('span', { class: 'swatch', style: '--c: var(--mercury)' }), p(L.itcz)),
    h('li', {}, h('span', { class: 'swatch is-dashed', style: '--c: var(--sun)' }), p(L.sth)),
    h('li', {}, h('span', { class: 'swatch is-dashed', style: '--c: var(--sky)' }), p(L.spl)),
    h('li', {}, h('span', { class: 'swatch', style: '--c: var(--leaf)' }), `${p(L.trades)} · ${p(L.west)} · ${p(L.east)}`));
  const ms = slider({ label: p(L.month), min: 1, max: 12, step: 1, value: month, onInput: v => { month = v; draw(); } });
  function draw() {
    const s = shift(month);
    m.setLayers([
      { type: 'lines', items: [
        { pts: parallel(5 + s), color: 'mercury' },
        { pts: parallel(30 + s), color: 'sun', dash: '6 5' }, { pts: parallel(-30 + s), color: 'sun', dash: '6 5' },
        { pts: parallel(60 + s), color: 'sky', dash: '6 5' }, { pts: parallel(-60 + s), color: 'sky', dash: '6 5' }] },
      // NE trades north of the ITCZ, SE trades south, westerlies 30–60°, polar easterlies beyond.
      { type: 'arrows', items: [...arrows(20 + s, -12, -7), ...arrows(-12 + s, -12, 7), ...arrows(44 + s, 14, 4), ...arrows(-44 + s, 14, -4), ...arrows(70 + s, -12, -3), ...arrows(-70 + s, -12, 3)] },
      { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3.5 }] },
    ]);
    ms.querySelector('output').textContent = MONTHS[lang][month - 1];
  }
  draw();
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 194–199; Mote & Sahu, pp. 67–71; coastlines: Natural Earth', children: [legend, m.el, h('div', { class: 'w-controls' }, ms)] }));
  return { destroy() { el.replaceChildren(); } };
}
