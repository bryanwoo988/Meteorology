/* M13 — Buoys that watch the tropical oceans: the TAO array in the
   Pacific (built 1985–94 to understand and predict ENSO), with RAMA in
   the Indian Ocean and PIRATA in the Atlantic. Real positions from NOAA
   NDBC (data/maps/buoys.json). */

import { baseMap } from '../maps.js';
import { loadData } from '../content.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('守着热带海洋的浮标', 'Buoys that watch the tropical oceans', 'Boya yang memerhati lautan tropika'),
  tao: T('TAO（太平洋）', 'TAO (Pacific)', 'TAO (Pasifik)'), rama: T('RAMA（印度洋）', 'RAMA (Indian Ocean)', 'RAMA (Lautan Hindi)'), pirata: T('PIRATA（大西洋）', 'PIRATA (Atlantic)', 'PIRATA (Atlantik)'),
};

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const [m, b] = await Promise.all([baseMap('world', { width: W, label: p(L.title) }), loadData('maps/buoys')]);
  m.setLayers([{ type: 'points', items: [
    ...b.tao.map(at => ({ at, color: 'sky', r: 2.6 })), ...b.rama.map(at => ({ at, color: 'leaf', r: 2.6 })), ...b.pirata.map(at => ({ at, color: 'sun', r: 2.6 })),
    { at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3 }] }]);
  const legend = h('ul', { class: 'chart-legend' }, ...[['tao', 'sky', b.tao.length], ['rama', 'leaf', b.rama.length], ['pirata', 'sun', b.pirata.length]]
    .map(([k, c, n]) => h('li', {}, h('span', { class: 'swatch', style: `--c: var(--${c})` }), `${p(L[k])} · ${n}`)));
  el.append(frame({ title: p(L.title), lang, source: 'NOAA NDBC station lists (positions, Oct 2026); coastlines: Natural Earth', children: [legend, m.el] }));
  return { destroy() { el.replaceChildren(); } };
}
