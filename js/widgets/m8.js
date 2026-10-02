/* M8 — The Indian Ocean Dipole. Positive: cooler water near Java and
   Sumatra, warmer in the west; Indonesia and Australia drier, East Africa
   wetter. Negative: the reverse. Boxes are the two Dipole Mode Index
   regions (climate.gov). Schematic shading. */

import { baseMap } from '../maps.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('印度洋偶极子：切换正负相位', 'The Indian Ocean Dipole: switch phase', 'Dwikutub Lautan Hindi: tukar fasa'),
  pos: T('正 IOD', 'Positive IOD', 'IOD positif'), neg: T('负 IOD', 'Negative IOD', 'IOD negatif'),
  text: { pos: T('东印度洋（苏门答腊、爪哇附近）偏冷，西印度洋偏暖：印尼和澳洲偏干、东非偏湿。', 'Cooler near Sumatra and Java, warmer in the west: Indonesia and Australia drier, East Africa wetter.', 'Lebih sejuk berhampiran Sumatera dan Jawa, lebih panas di barat: Indonesia dan Australia lebih kering, Afrika Timur lebih basah.'),
    neg: T('苏门答腊以西偏暖，西印度洋偏冷：印尼和澳洲偏湿、东非偏干。', 'Warmer west of Sumatra, cooler in the west: Indonesia and Australia wetter, East Africa drier.', 'Lebih panas di barat Sumatera, lebih sejuk di barat: Indonesia dan Australia lebih basah, Afrika Timur lebih kering.') },
};
const box = (lon0, lat0, lon1, lat1) => [[lon0, lat0], [lon1, lat0], [lon1, lat1], [lon0, lat1], [lon0, lat0]];

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const m = await baseMap('seasia', { width: W, bbox: [40, -25, 135, 25], label: p(L.title) });
  const tabs = h('div', { class: 'stage-chips' }), out = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  function show(k) {
    const westFill = k === 'pos' ? 'mercury' : 'rain', eastFill = k === 'pos' ? 'rain' : 'mercury';
    m.setLayers([{ type: 'regions', items: [{ ring: box(50, -10, 70, 10), fill: westFill, opacity: 0.45 }, { ring: box(90, -10, 108, 0), fill: eastFill, opacity: 0.45 }] },
      { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3 }] }]);
    out.textContent = p(L.text[k]);
    tabs.replaceChildren(...['pos', 'neg'].map(x => { const b = h('button', { type: 'button', class: `chip${x === k ? ' is-on' : ''}` }, p(L[x])); b.addEventListener('click', () => show(x)); return b; }));
  }
  show('pos');
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'NOAA climate.gov (IOD, Dipole Mode Index regions); coastlines: Natural Earth', children: [tabs, m.el, out] }));
  return { destroy() { el.replaceChildren(); } };
}
