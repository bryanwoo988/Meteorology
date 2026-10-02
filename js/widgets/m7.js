/* M7 — The eight phases of the MJO. Drag the phase: the band of enhanced
   cloud and rain moves east; phases 4–5 sit over the Maritime Continent,
   including Malaysia. Phase regions: NOAA (RMM diagram); 30–60 days per
   circuit, eastward at about 4–8 m/s (Fundamentals of Meteorology p.175;
   climate.gov). Schematic band. */

import { baseMap } from '../maps.js';
import { h, clamp, slider, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('MJO 的 8 个相位：拖动相位', 'The 8 phases of the MJO: drag the phase', '8 fasa MJO: seret fasa'),
  phase: T('相位', 'Phase', 'Fasa'),
  region: { 1: T('西半球、非洲', 'Western Hemisphere, Africa', 'Hemisfera Barat, Afrika'), 2: T('印度洋', 'Indian Ocean', 'Lautan Hindi'), 3: T('印度洋', 'Indian Ocean', 'Lautan Hindi'), 4: T('海洋性大陆（马来西亚、印尼）', 'Maritime Continent (Malaysia, Indonesia)', 'Benua Maritim (Malaysia, Indonesia)'), 5: T('海洋性大陆（马来西亚、印尼）', 'Maritime Continent (Malaysia, Indonesia)', 'Benua Maritim (Malaysia, Indonesia)'), 6: T('西太平洋', 'Western Pacific', 'Pasifik Barat'), 7: T('西太平洋', 'Western Pacific', 'Pasifik Barat'), 8: T('西半球、非洲', 'Western Hemisphere, Africa', 'Hemisfera Barat, Afrika') },
  wet: T('多云多雨的一段', 'Enhanced cloud and rain', 'Lebih banyak awan dan hujan'), dry: T('少云少雨的一段', 'Suppressed', 'Dikurangkan'),
};
const CENTRE = { 1: 0, 2: 65, 3: 85, 4: 105, 5: 125, 6: 145, 7: 165, 8: -40 };

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const m = await baseMap('world', { width: W, label: p(L.title) });
  let phase = 4;
  const out = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  const band = (c, half) => { const r = []; for (let lon = c - half; lon <= c + half; lon += 5) r.push([lon, -12]); for (let lon = c + half; lon >= c - half; lon -= 5) r.push([lon, 12]); r.push([c - half, -12]); return r; };
  const ps = slider({ label: p(L.phase), min: 1, max: 8, step: 1, value: phase, onInput: v => { phase = v; draw(); } });
  function draw() {
    const c = CENTRE[phase], dry = ((c + 180 + 180) % 360) - 180;
    m.setLayers([{ type: 'regions', items: [{ ring: band(c, 25), fill: 'rain', opacity: 0.45 }, { ring: band(dry, 30), fill: 'sun', opacity: 0.3 }] },
      { type: 'labels', items: [{ at: [c, 18], text: p(L.wet) }] },
      { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'ink-2', r: 3 }] }]);
    out.textContent = `${p(L.phase)} ${phase}: ${p(L.region[phase])}`;
  }
  draw();
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'NOAA (RMM phases); climate.gov; Fundamentals of Meteorology p.175; MetMalaysia 2025', children: [m.el, h('div', { class: 'w-controls' }, ps), out] }));
  return { destroy() { el.replaceChildren(); } };
}
