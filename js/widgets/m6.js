/* M6 — Sea-surface temperature anomaly in three real Decembers: 2015
   (El Niño), 2013 (neutral), 2010 (La Niña). NOAA OI SST V2 vs the
   1991–2020 December mean (data/maps/sst-events.json). The box is the
   Niño 3.4 region (5°N–5°S, 120°–170°W). */

import { baseMap } from '../maps.js';
import { loadData } from '../content.js';
import { h, clamp, frame } from './kit.js';
import { anomColour } from './sstcolour.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('太平洋海温距平：三个真实的 12 月', 'Pacific sea-temperature anomaly: three real Decembers', 'Anomali suhu laut Pasifik: tiga Disember sebenar'),
  'elnino-2015-12': T('2015 年 12 月 · 厄尔尼诺', 'Dec 2015 · El Niño', 'Dis 2015 · El Niño'),
  'neutral-2013-12': T('2013 年 12 月 · 正常', 'Dec 2013 · neutral', 'Dis 2013 · neutral'),
  'lanina-2010-12': T('2010 年 12 月 · 拉尼娜', 'Dec 2010 · La Niña', 'Dis 2010 · La Niña'),
  box: T('Niño 3.4 区', 'Niño 3.4', 'Niño 3.4'), mean: T('Niño 3.4 区平均距平', 'Niño 3.4 average anomaly', 'Purata anomali Niño 3.4'),
};

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const [m, d] = await Promise.all([baseMap('world', { width: W, label: p(L.title) }), loadData('maps/sst-events')]);
  const tabs = h('div', { class: 'stage-chips' });
  const out = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  const legend = h('div', { class: 'map-legend' }, h('span', {}, '−3 °C'), h('span', { class: 'map-legend-bar', style: `background: linear-gradient(to right, ${[-3, -1.5, 0, 1.5, 3].map(anomColour).join(',')})` }), h('span', {}, '+3 °C'));
  const box = [[-170, -5], [-120, -5], [-120, 5], [-170, 5], [-170, -5]];
  function show(key) {
    const v = d.events[key];
    let sum = 0, n = 0;
    for (let j = 0; j < d.ny; j++) for (let i = 0; i < d.nx; i++) {
      const lon = d.lon0 + (i + 0.5) * d.dlon, lat = d.lat0 + (j + 0.5) * d.dlat, x = v[j * d.nx + i];
      if (x != null && lat >= -5 && lat <= 5 && lon >= -170 && lon <= -120) { sum += x; n++; }
    }
    m.setLayers([{ type: 'grid', lon0: d.lon0, lat0: d.lat0, dlon: d.dlon, dlat: d.dlat, nx: d.nx, ny: d.ny, values: v, colour: anomColour },
      { type: 'lines', items: [{ pts: box, color: 'ink' }] },
      { type: 'labels', items: [{ at: [-145, 9], text: p(L.box) }] },
      { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3 }] }]);
    out.textContent = `${p(L.mean)}: ${sum / n >= 0 ? '+' : ''}${(sum / n).toFixed(1)} °C`;
    tabs.replaceChildren(...Object.keys(d.events).map(k => { const b = h('button', { type: 'button', class: `chip${k === key ? ' is-on' : ''}` }, p(L[k])); b.addEventListener('click', () => show(k)); return b; }));
  }
  show('elnino-2015-12');
  el.append(frame({ title: p(L.title), lang, source: `${d.source} · fetched ${d.fetched}`, children: [tabs, m.el, legend, out] }));
  return { destroy() { el.replaceChildren(); } };
}
