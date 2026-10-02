/* M11 — Where the north-east monsoon brings big floods: Kelantan,
   Terengganu, Pahang and East Johor on the Peninsula, plus Sarawak and
   Sabah (MetMalaysia, weather phenomena). Markers at state capitals; tap one. */

import { baseMap } from '../maps.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('东北季风的大水灾在哪里：点一个州', 'Where the north-east monsoon floods: tap a state', 'Di mana banjir monsun timur laut: ketik satu negeri'),
  hint: T('东北季风（11 月到 3 月）的大雨，常在这些地方造成大水灾。', 'The heavy rain of the north-east monsoon (November to March) often causes large floods in these places.', 'Hujan lebat monsun timur laut (November hingga Mac) sering menyebabkan banjir besar di tempat-tempat ini.'),
};
const STATES = [
  { id: 'kel', at: [102.24, 6.13], name: T('吉兰丹', 'Kelantan', 'Kelantan') },
  { id: 'trg', at: [103.14, 5.33], name: T('登嘉楼', 'Terengganu', 'Terengganu') },
  { id: 'phg', at: [103.33, 3.81], name: T('彭亨', 'Pahang', 'Pahang') },
  { id: 'jhr', at: [103.84, 2.45], name: T('柔佛东部', 'East Johor', 'Johor Timur') },
  { id: 'swk', at: [110.35, 1.55], name: T('砂拉越', 'Sarawak', 'Sarawak') },
  { id: 'sbh', at: [116.07, 5.98], name: T('沙巴', 'Sabah', 'Sabah') },
];

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const out = h('p', { class: 'w-explain', 'aria-live': 'polite' }, p(L.hint));
  const m = await baseMap('seasia', { width: W, bbox: [99, 0, 120, 8], label: p(L.title), onPick: id => {
    const st = STATES.find(x => x.id === id);
    if (st) out.textContent = `${p(st.name)} — ${p(L.hint)}`;
  } });
  m.setLayers([
    { type: 'arrows', items: [{ from: [108, 9.5], to: [105.5, 6.8], color: 'sky' }, { from: [113, 8.5], to: [111, 5.5], color: 'sky' }] },
    { type: 'points', items: STATES.map(st => ({ id: st.id, at: st.at, label: p(st.name), color: 'rain', r: 5 })) },
  ]);
  el.append(frame({ title: p(L.title), lang, source: 'MetMalaysia (weather phenomena: monsoon); coastlines: Natural Earth', children: [m.el, out] }));
  return { destroy() { el.replaceChildren(); } };
}
