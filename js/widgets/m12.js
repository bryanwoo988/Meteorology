/* M12 — Transboundary haze in the south-west monsoon. ASMC: during the
   south-west monsoon the low-level winds blow mainly from the south-east
   or south-west, the dry season of the southern ASEAN region; on
   2 Oct 2026 ASMC reported hotspot clusters in southern Sumatra and
   south-eastern Kalimantan and smoke haze over parts of Sarawak.
   Hotspot markers and arrows are schematic. */

import { baseMap } from '../maps.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('跨境烟霾：西南季风时的风和火点', 'Transboundary haze: south-west monsoon winds and hotspots', 'Jerebu rentas sempadan: angin monsun barat daya dan titik panas'),
  text: T('红点：火点群；箭头：西南季风期间把烟吹向马来西亚的风。', 'Red dots: hotspot clusters. Arrows: south-west-monsoon winds carrying the smoke towards Malaysia.', 'Titik merah: kelompok titik panas. Anak panah: angin monsun barat daya yang membawa asap ke arah Malaysia.'),
  hot: T('火点', 'Hotspots', 'Titik panas'),
};
const HOT = [[103.6, -3.0], [104.4, -3.4], [104.9, -2.7], [105.3, -4.1], [114.5, -3.2], [115.3, -2.6], [115.8, -3.6]];

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const m = await baseMap('seasia', { width: W, bbox: [96, -7, 120, 8], label: p(L.title) });
  m.setLayers([
    { type: 'circles', items: [{ at: [104.4, -3.3], km: 260, color: 'muted' }, { at: [115.1, -3.1], km: 240, color: 'muted' }] },
    { type: 'arrows', items: [{ from: [104, -2], to: [102.6, 1.6], color: 'ink-2' }, { from: [106, -1.5], to: [107, 1.2], color: 'ink-2' }, { from: [113.6, -1.6], to: [111.6, 1.4], color: 'ink-2' }] },
    { type: 'points', items: [...HOT.map(at => ({ at, color: 'warn', r: 3.5 })), { at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3 }, { at: [110.35, 1.55], label: 'Kuching', color: 'ink-2', r: 3 }] },
    { type: 'labels', items: [{ at: [104.6, -5.4], text: p(L.hot) }] },
  ]);
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'ASMC (seasonal outlook; regional haze situation, read 2 Oct 2026); coastlines: Natural Earth', children: [m.el, h('p', { class: 'w-explain' }, p(L.text))] }));
  return { destroy() { el.replaceChildren(); } };
}
