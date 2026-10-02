/* M1 — Where the jet streams blow. Schematic positions from Ahrens
   pp. 199–200: the subtropical jet near 30° at about 13 km, the polar-front
   jet near the polar front at about 10 km, stronger and further towards the
   equator in winter. Switch January / July. */

import { baseMap } from '../maps.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('急流在哪里：切换 1 月和 7 月', 'Where the jet streams blow: switch January and July', 'Di mana aliran jet bertiup: tukar Januari dan Julai'),
  jan: T('1 月', 'January', 'Januari'), jul: T('7 月', 'July', 'Julai'),
  sub: T('副热带急流（约 13 km）', 'Subtropical jet (≈ 13 km)', 'Jet subtropika (≈ 13 km)'),
  polar: T('极地锋急流（约 10 km）', 'Polar-front jet (≈ 10 km)', 'Jet front kutub (≈ 10 km)'),
  note: T('线的位置是示意：真实的急流每天弯曲、断开、移动。', 'Positions are schematic: real jets meander, break and move from day to day.', 'Kedudukan ialah ilustrasi: jet sebenar berliku, terputus dan bergerak setiap hari.'),
};

const wave = (lat0, amp, k, phase) => { const pts = []; for (let lon = -180; lon <= 180; lon += 5) pts.push([lon, lat0 + amp * Math.sin((lon + phase) * k * Math.PI / 180)]); return pts; };

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const m = await baseMap('world', { width: W, label: p(L.title) });
  const legend = h('ul', { class: 'chart-legend' },
    h('li', {}, h('span', { class: 'swatch', style: '--c: var(--mercury)' }), p(L.sub)),
    h('li', {}, h('span', { class: 'swatch is-dashed', style: '--c: var(--sky)' }), p(L.polar)));
  const tabs = h('div', { class: 'stage-chips' });
  function show(month) {
    // In each hemisphere's winter the jets are stronger and lie closer to the equator.
    const nWinter = month === 'jan';
    m.setLayers([
      { type: 'lines', items: [
        { pts: wave(nWinter ? 27 : 33, 3, 2, 0), color: 'mercury' },
        { pts: wave(nWinter ? -32 : -27, 3, 2, 40), color: 'mercury' },
        { pts: wave(nWinter ? 45 : 55, 9, 3, 20), color: 'sky', dash: '6 5' },
        { pts: wave(nWinter ? -58 : -50, 7, 3, 70), color: 'sky', dash: '6 5' }] },
      { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'leaf', r: 3.5 }] },
    ]);
    tabs.replaceChildren(...['jan', 'jul'].map(k => { const b = h('button', { type: 'button', class: `chip${k === month ? ' is-on' : ''}` }, p(L[k])); b.addEventListener('click', () => show(k)); return b; }));
  }
  show('jan');
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 199–200; coastlines: Natural Earth', children: [tabs, legend, m.el, h('p', { class: 'w-source' }, p(L.note))] }));
  return { destroy() { el.replaceChildren(); } };
}
