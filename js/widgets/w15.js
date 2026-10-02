/* W15 — The geostationary family. Pick a place (or slide the longitude):
   the globe turns to it and the list shows which geostationary weather
   satellites can see it, and how high each stands in its sky. Positions
   and status: WMO OSCAR/Space, checked 2 Oct 2026. Viewing geometry from
   physics.geoView. */

import { baseMap } from '../maps.js';
import { geoView } from '../physics.js';
import { h, clamp, slider, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('同步卫星全家福：选一个地方', 'The geostationary family: pick a place', 'Keluarga satelit geopegun: pilih satu tempat'),
  lon: T('经度', 'Longitude', 'Longitud'),
  sees: T('看得到这里', 'can see here', 'boleh melihat di sini'), none: T('看不到（在地平线下）', 'below the horizon', 'di bawah ufuk'),
  elev: T('仰角', 'elevation', 'altitud'),
  low: T('角度很低，图像很斜', 'very low: a slanted view', 'sangat rendah: pandangan condong'),
  note: { fy4b: T('成像仪 2026 年 7 月 30 日故障', 'imager failed 30 Jul 2026', 'pengimej rosak 30 Jul 2026') },
};
const SATS = [
  { name: 'Himawari-9', by: 'JMA', lon: 140.7 },
  { name: 'GEO-KOMPSAT-2A', by: 'KMA', lon: 128.2 },
  { name: 'FY-4A', by: 'CMA', lon: 123.5 },
  { name: 'FY-4B', by: 'CMA', lon: 105, note: 'fy4b' },
  { name: 'INSAT-3DS', by: 'IMD', lon: 82 },
  { name: 'INSAT-3DR', by: 'IMD', lon: 74 },
  { name: 'Meteosat-12', by: 'EUMETSAT', lon: -0.3 },
  { name: 'GOES-19 (East)', by: 'NOAA', lon: -75.2 },
  { name: 'GOES-18 (West)', by: 'NOAA', lon: -137 },
];
const PLACES = [
  { id: 'kl', name: T('吉隆坡', 'Kuala Lumpur', 'Kuala Lumpur'), at: [101.69, 3.14] },
  { id: 'kk', name: T('亚庇', 'Kota Kinabalu', 'Kota Kinabalu'), at: [116.07, 5.98] },
  { id: 'tokyo', name: T('东京', 'Tokyo', 'Tokyo'), at: [139.7, 35.7] },
  { id: 'delhi', name: T('新德里', 'New Delhi', 'New Delhi'), at: [77.2, 28.6] },
  { id: 'london', name: T('伦敦', 'London', 'London'), at: [-0.13, 51.5] },
  { id: 'ny', name: T('纽约', 'New York', 'New York'), at: [-74.0, 40.7] },
];

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 520));
  let place = PLACES[0].at.slice();
  const m = await baseMap('globe', { width: W, centre: place, label: p(L.title) });
  const chips = h('div', { class: 'stage-chips' }), list = h('ul', { class: 'sat-list', 'aria-live': 'polite' });
  const ls = slider({ label: p(L.lon), min: -180, max: 180, step: 1, value: Math.round(place[0]), unit: '°', onInput: v => { place = [v, place[1]]; draw(null); } });
  function draw(activeId) {
    m.rotateTo([place[0], clamp(place[1], -60, 60)]);
    const rows = SATS.map(st => ({ st, v: geoView(place[1], place[0], st.lon) })).sort((a, b) => b.v.elevation - a.v.elevation);
    m.setLayers([{ type: 'points', items: [
      ...SATS.map(st => ({ at: [st.lon, 0], color: 'sky', r: 4 })),
      { at: place, color: 'mercury', r: 5 }] }]);
    list.replaceChildren(...rows.map(({ st, v }) => h('li', { class: v.visible ? 'is-on' : 'is-off' },
      h('strong', {}, st.name), ` · ${st.by} · ${Math.abs(st.lon)}°${st.lon >= 0 ? 'E' : 'W'} — `,
      v.visible ? `${p(L.sees)}, ${p(L.elev)} ${v.elevation.toFixed(0)}°${v.elevation < 20 ? ` (${p(L.low)})` : ''}` : p(L.none),
      st.note ? ` · ${p(L.note[st.note])}` : '')));
    chips.replaceChildren(...PLACES.map(pl => { const b = h('button', { type: 'button', class: `chip${pl.id === activeId ? ' is-on' : ''}` }, p(pl.name)); b.addEventListener('click', () => { place = pl.at.slice(); ls.set(Math.round(place[0])); draw(pl.id); }); return b; }));
  }
  draw('kl');
  el.append(frame({ title: p(L.title), lang, source: 'WMO OSCAR/Space (positions and status, Oct 2026); coastlines: Natural Earth', children: [chips, m.el, h('div', { class: 'w-controls' }, ls), list] }));
  return { destroy() { el.replaceChildren(); } };
}
