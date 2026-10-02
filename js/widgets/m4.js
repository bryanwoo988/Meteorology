/* M4 — The major surface ocean currents: warm currents (red) usually run
   poleward along the east coasts of continents, cold currents (blue)
   equatorward along the west coasts. Ahrens pp. 202–203. Schematic paths. */

import { baseMap } from '../maps.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('主要洋流：点一条看看', 'The main ocean currents: tap one', 'Arus lautan utama: ketik satu'),
  hint: T('红色是暖流，蓝色是寒流。点一条洋流看名字。', 'Red: warm currents. Blue: cold currents. Tap one for its name.', 'Merah: arus panas. Biru: arus sejuk. Ketik satu untuk namanya.'),
};
const C = [
  ['gulf', 'mercury', [[-80, 25], [-75, 35], [-60, 40], [-40, 45], [-20, 50]], T('墨西哥湾流（暖）', 'Gulf Stream (warm)', 'Arus Teluk (panas)')],
  ['kuroshio', 'mercury', [[122, 22], [130, 30], [140, 35], [155, 38]], T('黑潮（暖）', 'Kuroshio (warm)', 'Kuroshio (panas)')],
  ['brazil', 'mercury', [[-35, -8], [-40, -20], [-48, -32]], T('巴西暖流', 'Brazil Current (warm)', 'Arus Brazil (panas)')],
  ['eac', 'mercury', [[155, -15], [154, -25], [152, -34]], T('东澳暖流', 'East Australian Current (warm)', 'Arus Australia Timur (panas)')],
  ['agulhas', 'mercury', [[40, -15], [35, -28], [25, -36]], T('厄加勒斯暖流', 'Agulhas Current (warm)', 'Arus Agulhas (panas)')],
  ['california', 'sky', [[-130, 45], [-125, 35], [-115, 25]], T('加利福尼亚寒流', 'California Current (cold)', 'Arus California (sejuk)')],
  ['canary', 'sky', [[-15, 40], [-18, 28], [-22, 18]], T('加那利寒流', 'Canary Current (cold)', 'Arus Canary (sejuk)')],
  ['peru', 'sky', [[-75, -40], [-77, -25], [-82, -8]], T('秘鲁（洪堡）寒流', 'Peru (Humboldt) Current (cold)', 'Arus Peru/Humboldt (sejuk)')],
  ['benguela', 'sky', [[15, -35], [12, -25], [8, -15]], T('本格拉寒流', 'Benguela Current (cold)', 'Arus Benguela (sejuk)')],
  ['westwind', 'sky', [[-60, -55], [0, -52], [60, -50], [120, -52], [180, -55]], T('南极绕极流（西风漂流）', 'Antarctic Circumpolar Current', 'Arus Lilitan Kutub Antartika')],
];

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const caption = h('p', { class: 'w-explain', 'aria-live': 'polite' }, p(L.hint));
  const m = await baseMap('world', { width: W, label: p(L.title) });
  m.setLayers([{ type: 'lines', items: C.map(([, color, pts]) => ({ pts, color })) }]);
  // Arrowheads at the end of each current; tapping anywhere on the line names it.
  const lines = m.svg.querySelectorAll('.map-lines path');
  C.forEach(([, , pts, name], i) => {
    const n = lines[i]; if (!n) return;
    n.classList.add('current', 'is-pickable'); n.setAttribute('tabindex', '0'); n.setAttribute('role', 'button'); n.setAttribute('aria-label', p(name));
    const pickIt = () => { for (const x of lines) x.classList.remove('is-on'); n.classList.add('is-on'); caption.textContent = p(name); };
    n.addEventListener('click', pickIt); n.addEventListener('keydown', e => { if (e.key === 'Enter') pickIt(); });
  });
  m.addLayer({ type: 'arrows', items: C.map(([, color, pts]) => ({ from: pts[pts.length - 2], to: pts[pts.length - 1], color })) });
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 202–203; coastlines: Natural Earth', children: [m.el, caption] }));
  return { destroy() { el.replaceChildren(); } };
}
