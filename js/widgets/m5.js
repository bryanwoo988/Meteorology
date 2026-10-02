/* M5 — Average sea-surface temperature by month (1991–2020), real data:
   NOAA OI SST V2 via data/maps/sst-clim.json. Drag the month. */

import { baseMap } from '../maps.js';
import { loadData } from '../content.js';
import { h, clamp, slider, frame } from './kit.js';
import { sstColour } from './sstcolour.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = { title: T('全球海表温度（1991–2020 月平均）：拖动月份', 'Sea-surface temperature, 1991–2020 monthly average: drag the month', 'Suhu permukaan laut, purata bulanan 1991–2020: seret bulan'), month: T('月份', 'Month', 'Bulan') };
const MONTHS = { zh: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'], en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ms: ['Jan', 'Feb', 'Mac', 'Apr', 'Mei', 'Jun', 'Jul', 'Ogo', 'Sep', 'Okt', 'Nov', 'Dis'] };

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const [m, d] = await Promise.all([baseMap('world', { width: W, label: p(L.title) }), loadData('maps/sst-clim')]);
  let month = 1;
  const legend = h('div', { class: 'map-legend' }, h('span', {}, '0 °C'), h('span', { class: 'map-legend-bar', style: `background: linear-gradient(to right, ${[0, 8, 16, 22, 26, 28, 30, 32].map(sstColour).join(',')})` }), h('span', {}, '32 °C'));
  const ms = slider({ label: p(L.month), min: 1, max: 12, step: 1, value: 1, onInput: v => { month = v; draw(); } });
  function draw() {
    m.setLayers([{ type: 'grid', lon0: d.lon0, lat0: d.lat0, dlon: d.dlon, dlat: d.dlat, nx: d.nx, ny: d.ny, values: d.months[month - 1], colour: sstColour },
      { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3 }] }]);
    ms.querySelector('output').textContent = MONTHS[lang][month - 1];
  }
  draw();
  el.append(frame({ title: p(L.title), lang, source: `${d.source} · fetched ${d.fetched}`, children: [m.el, legend, h('div', { class: 'w-controls' }, ms)] }));
  return { destroy() { el.replaceChildren(); } };
}
