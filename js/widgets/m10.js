/* M10 — Two west-coast rhythms. Sumatras: during the south-west monsoon
   the wind crosses Sumatra's mountains, thunderstorms merge over the warm
   Strait of Malacca into a squall line, and it is driven north-east onto
   the west coast before dawn and in the early morning (April–November).
   Sea breeze: by day, air flows from the cooler sea onto the warmer land.
   MetMalaysia (squall lines); Ahrens p. 182 (sea breeze). Schematic. */

import { baseMap } from '../maps.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('西海岸的两种节奏：切换', 'Two west-coast rhythms: switch', 'Dua irama pantai barat: tukar'),
  squall: T('苏门答腊飑线', 'Sumatra squall line', 'Garis badai Sumatera'), breeze: T('海风', 'Sea breeze', 'Bayu laut'),
  text: {
    squall: T('西南季风越过苏门答腊的山脉，在温暖的马六甲海峡上空形成雷雨，连成一条飑线，被西南风推向东北，凌晨到早上打到半岛西海岸。4 月到 11 月最常见。上岸后很快减弱，大约一小时后天气恢复正常。', 'The south-west monsoon crosses Sumatra\'s mountains; thunderstorms form over the warm Strait of Malacca and merge into a squall line, which the south-west wind drives north-east onto the Peninsula\'s west coast before dawn and in the early morning. It is commonest from April to November, weakens quickly over land, and the weather is back to normal about an hour later.', 'Monsun barat daya merentasi banjaran Sumatera; ribut petir terbentuk di atas Selat Melaka yang panas dan bergabung menjadi garis badai, yang ditolak angin barat daya ke timur laut ke pantai barat Semenanjung menjelang subuh dan awal pagi. Ia paling kerap dari April hingga November, cepat lemah di darat, dan cuaca kembali normal kira-kira sejam kemudian.'),
    breeze: T('白天陆地比海热得快，陆地上空气压较低，海上较凉的空气就吹向陆地。海风把潮湿的空气带进内陆，帮助下午的积云长高。', 'By day the land heats faster than the sea, pressure falls over the land, and cooler sea air flows inland. The sea breeze carries moist air inland and helps the afternoon cumulus grow.', 'Pada siang hari darat menjadi panas lebih cepat daripada laut, tekanan turun di atas darat, dan udara laut yang lebih sejuk mengalir ke darat. Bayu laut membawa udara lembap ke pedalaman dan membantu kumulus petang tumbuh.'),
  },
  strait: T('马六甲海峡', 'Strait of Malacca', 'Selat Melaka'), sumatra: T('苏门答腊', 'Sumatra', 'Sumatera'),
};

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const m = await baseMap('seasia', { width: W, bbox: [95, -1, 106, 7], label: p(L.title) });
  const tabs = h('div', { class: 'stage-chips' }), out = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  function show(k) {
    const common = [{ type: 'labels', items: [{ at: [99.6, 3.3], text: p(L.strait) }, { at: [100.3, 0.4], text: p(L.sumatra) }] },
      { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3 }, { at: [100.33, 5.41], label: 'Penang', color: 'ink-2', r: 3 }] }];
    if (k === 'squall') m.setLayers([
      { type: 'lines', items: [{ pts: [[98.6, 5.4], [99.6, 4.2], [100.6, 3.0], [101.6, 1.8]], color: 'mercury' }] },
      { type: 'arrows', items: [{ from: [97.6, 1.6], to: [98.9, 2.9], color: 'sky' }, { from: [98.6, 0.6], to: [99.9, 1.9], color: 'sky' }, { from: [99.9, 3.6], to: [100.9, 4.6], color: 'mercury' }] },
      ...common]);
    else m.setLayers([
      { type: 'arrows', items: [[99.6, 4.6, 100.5, 4.4], [100.2, 3.2, 101.1, 3.1], [100.9, 2.2, 101.6, 2.5], [104.9, 4.2, 103.7, 4.0], [104.6, 2.8, 103.6, 2.9]].map(([a, b, c, d]) => ({ from: [a, b], to: [c, d], color: 'sky' })) },
      ...common]);
    out.textContent = p(L.text[k]);
    tabs.replaceChildren(...['squall', 'breeze'].map(x => { const b = h('button', { type: 'button', class: `chip${x === k ? ' is-on' : ''}` }, p(L[x])); b.addEventListener('click', () => show(x)); return b; }));
  }
  show('squall');
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'MetMalaysia (squall lines, Sumatras); Ahrens 2010, p. 182; coastlines: Natural Earth', children: [tabs, m.el, out] }));
  return { destroy() { el.replaceChildren(); } };
}
