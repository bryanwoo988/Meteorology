/* M3 — Where tropical cyclones form, and what they are called. Formation
   mostly between 5° and 20° latitude over warm (≥ 26.5 °C) ocean; none on
   the equator, where the Coriolis effect vanishes (Ahrens pp. 314–317).
   Regions are schematic boxes. Tap one. */

import { baseMap } from '../maps.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('热带气旋在哪里形成：点一个海域', 'Where tropical cyclones form: tap a region', 'Di mana siklon tropika terbentuk: ketik satu kawasan'),
  band: T('赤道南北 5° 以内：几乎不会形成', 'Within 5° of the equator: they almost never form', 'Dalam 5° dari khatulistiwa: hampir tidak pernah terbentuk'),
  hint: T('点一个海域，看当地怎么称呼这种风暴。', 'Tap a region to see what the storms are called there.', 'Ketik satu kawasan untuk melihat nama ribut itu di sana.'),
};
const box = (lon0, lat0, lon1, lat1) => [[lon0, lat0], [lon1, lat0], [lon1, lat1], [lon0, lat1], [lon0, lat0]];
const REGIONS = [
  { id: 'wp', ring: box(110, 6, 170, 22), name: T('西北太平洋：台风', 'Western North Pacific: typhoons', 'Pasifik Barat Laut: taufan') },
  { id: 'at', ring: box(-80, 8, -20, 22), name: T('北大西洋：飓风', 'North Atlantic: hurricanes', 'Atlantik Utara: hurikan') },
  { id: 'ep', ring: box(-130, 8, -90, 20), name: T('东北太平洋：飓风', 'Eastern North Pacific: hurricanes', 'Pasifik Timur Laut: hurikan') },
  { id: 'ni', ring: box(60, 7, 95, 20), name: T('北印度洋：气旋', 'North Indian Ocean: cyclones', 'Lautan Hindi Utara: siklon') },
  { id: 'si', ring: box(45, -20, 100, -7), name: T('南印度洋：热带气旋', 'South Indian Ocean: tropical cyclones', 'Lautan Hindi Selatan: siklon tropika') },
  { id: 'au', ring: box(105, -20, 175, -8), name: T('澳洲和南太平洋：热带气旋', 'Australia and the South Pacific: tropical cyclones', 'Australia dan Pasifik Selatan: siklon tropika') },
];

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const caption = h('p', { class: 'w-explain', 'aria-live': 'polite' }, p(L.hint));
  const m = await baseMap('world', { width: W, label: p(L.title), onPick: id => {
    const r = REGIONS.find(x => x.id === id);
    caption.textContent = r ? p(r.name) : p(L.band);
    for (const n of m.svg.querySelectorAll('.map-regions path')) n.classList.toggle('is-on', n.dataset.id === id);
  } });
  m.setLayers([
    { type: 'regions', items: [{ id: 'eq', ring: box(-180, -5, 180, 5), fill: 'sky', opacity: 0.18 }, ...REGIONS.map(r => ({ ...r, fill: 'mercury', opacity: 0.35 }))] },
    { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3.5 }] },
  ]);
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 314–317; coastlines: Natural Earth', children: [m.el, caption] }));
  return { destroy() { el.replaceChildren(); } };
}
