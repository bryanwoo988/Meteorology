/* W11 — Spring and neap tides. Drag through the Moon's cycle: when Sun,
   Earth and Moon line up (new and full moon) their pulls add and the tidal
   range is largest — spring tides; at the quarters they pull at right
   angles — neap tides (NOAA). Schematic: bulges not to scale. */

import { s, h, clamp, slider, readout, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('大潮与小潮：拖动月相', 'Spring and neap tides: drag the Moon', 'Pasang besar dan pasang perbani: seret Bulan'),
  day: T('农历天数（月龄）', 'Days since new moon', 'Hari sejak bulan baharu'),
  phase: T('月相', 'Moon phase', 'Fasa bulan'), tide: T('潮汐', 'Tide', 'Pasang surut'),
  new: T('新月（初一）', 'New moon', 'Bulan baharu'), first: T('上弦月', 'First quarter', 'Suku pertama'), full: T('满月（十五）', 'Full moon', 'Bulan purnama'), last: T('下弦月', 'Last quarter', 'Suku akhir'),
  spring: T('大潮：涨得最高、退得最低', 'Spring tide: highest highs and lowest lows', 'Pasang besar: pasang tertinggi dan surut terendah'),
  neap: T('小潮：涨落都比较温和', 'Neap tide: moderate rise and fall', 'Pasang perbani: naik turun sederhana'),
  between: T('介于大潮和小潮之间', 'Between spring and neap', 'Antara pasang besar dan perbani'),
  sun: T('太阳在这边', 'Sun this way', 'Matahari di sebelah sini'),
};
const MONTH = 29.53;

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.62);
  const cx = W * 0.55, cy = H / 2, R = Math.min(W, H) * 0.12, orbit = Math.min(W * 0.36, H * 0.42);
  let day = 0;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  svg.append(s('text', { x: 10, y: cy - 10, class: 'force-label' }, `☀ ${p(L.sun)}`), s('line', { x1: 10, x2: W * 0.16, y1: cy, y2: cy, class: 'gauge-ray' }));
  svg.append(s('circle', { cx, cy, r: orbit, class: 'gauge-arc' }));
  const water = s('ellipse', { cx, cy, class: 'tide-water' });
  svg.append(water, s('circle', { cx, cy, r: R, class: 'tide-earth' }));
  const moon = s('circle', { r: R * 0.32, class: 'tide-moon' });
  svg.append(moon);
  const rows = readout([['phase', p(L.phase)], ['tide', p(L.tide)]]);
  const ds = slider({ label: p(L.day), min: 0, max: 29.5, step: 0.5, value: day, onInput: v => { day = v; update(); } });
  function update() {
    const a = 2 * Math.PI * day / MONTH;              // 0 = new moon, between Earth and Sun (Sun to the left)
    const mx = cx - orbit * Math.cos(a), my = cy - orbit * Math.sin(a);
    moon.setAttribute('cx', mx); moon.setAttribute('cy', my);
    // Lunar bulge along the Earth–Moon line; the solar bulge (about half as strong) stays along the Sun line.
    const align = Math.abs(Math.cos(a));               // 1 at new/full, 0 at quarters
    const stretch = R * (1.25 + 0.25 * align), squeeze = R * (1.1 - 0.05 * align);
    water.setAttribute('rx', stretch); water.setAttribute('ry', squeeze);
    water.setAttribute('transform', `rotate(${(a * 180 / Math.PI).toFixed(1)} ${cx} ${cy})`);
    const ph = day < 3.7 || day > 25.8 ? 'new' : day < 11.1 ? 'first' : day < 18.5 ? 'full' : 'last';
    const near = [0, MONTH / 4, MONTH / 2, 3 * MONTH / 4, MONTH].map(d => Math.abs(day - d));
    const nearest = near.indexOf(Math.min(...near)) % 4;
    rows.set('phase', p(L[ph]));
    rows.set('tide', Math.min(...near) > 2.5 ? p(L.between) : nearest % 2 === 0 ? p(L.spring) : p(L.neap));
  }
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'NOAA Ocean Service: spring and neap tides', children: [svg, h('div', { class: 'w-controls' }, ds), rows] }));
  update();
  return { destroy() { el.replaceChildren(); } };
}
