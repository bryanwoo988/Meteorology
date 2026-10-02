/* W8 — Why the wind blows where it does. Two isobars, high pressure above
   and low below. Drag the pressure difference and the latitude: in the
   upper air, away from the equator, the pressure push and the Coriolis
   effect balance and the wind blows along the isobars at the geostrophic
   speed (physics.geostrophicWind). Within 5° of the equator the Coriolis
   effect is too weak and air moves straight from high to low. */

import { geostrophicWind } from '../physics.js';
import { s, h, clamp, slider, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('风为什么这样吹：拖动气压差和纬度', 'Why the wind blows as it does: drag the pressure difference and latitude', 'Mengapa angin bertiup begitu: seret perbezaan tekanan dan latitud'),
  dp: T('每 100 公里的气压差', 'Pressure difference per 100 km', 'Perbezaan tekanan setiap 100 km'),
  lat: T('纬度', 'Latitude', 'Latitud'),
  speed: T('高空风速（地转风）', 'Upper-air wind (geostrophic)', 'Angin udara atas (geostrofik)'),
  dir: T('风向', 'Direction', 'Arah'),
  along: T('沿着等压线吹（北半球低压在左）', 'Along the isobars (low pressure on the left, northern hemisphere)', 'Sepanjang isobar (tekanan rendah di kiri, hemisfera utara)'),
  across: T('直接从高压吹向低压', 'Straight from high to low pressure', 'Terus dari tekanan tinggi ke rendah'),
  eq: T('离赤道 5° 以内：科里奥利力太弱，没有地转平衡', 'Within 5° of the equator: the Coriolis effect is too weak for geostrophic balance', 'Dalam 5° dari khatulistiwa: kesan Coriolis terlalu lemah untuk keseimbangan geostrofik'),
  pgf: T('气压梯度力', 'Pressure-gradient force', 'Daya kecerunan tekanan'), cor: T('科里奥利力', 'Coriolis', 'Coriolis'), wind: T('风', 'Wind', 'Angin'),
};

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.58);
  let dp = 2, lat = 30;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const yH = H * 0.2, yL = H * 0.8, mid = H * 0.5, cx = W * 0.5;
  svg.append(
    s('line', { x1: 12, x2: W - 12, y1: yH, y2: yH, class: 'isobar' }), s('text', { x: 16, y: yH - 6, class: 'isobar-label' }, 'H · 1012 hPa'),
    s('line', { x1: 12, x2: W - 12, y1: yL, y2: yL, class: 'isobar' }));
  const lowText = s('text', { x: 16, y: yL + 16, class: 'isobar-label' });
  svg.append(lowText);
  const defs = s('defs', {}, ...['ink-2', 'rain', 'mercury'].map(c => s('marker', { id: `ah-${c}`, viewBox: '0 0 10 10', refX: 8, refY: 5, markerWidth: 6, markerHeight: 6, orient: 'auto-start-reverse' }, s('path', { d: 'M0,0 L10,5 L0,10 Z', style: `fill: var(--${c})` }))));
  svg.append(defs);
  const arrow = (c, cls) => { const a = s('line', { class: cls, style: `stroke: var(--${c})`, 'marker-end': `url(#ah-${c})` }); svg.append(a); return a; };
  const pgf = arrow('ink-2', 'force'), cor = arrow('rain', 'force'), wind = arrow('mercury', 'wind-arrow');
  const pgfT = s('text', { class: 'force-label' }), corT = s('text', { class: 'force-label' }), windT = s('text', { class: 'force-label' });
  svg.append(pgfT, corT, windT);
  const rows = readout([['speed', p(L.speed)], ['dir', p(L.dir)]]);
  const note = h('p', { class: 'w-explain' });
  const dpS = slider({ label: p(L.dp), min: 0.5, max: 5, step: 0.5, value: dp, unit: ' hPa', onInput: v => { dp = v; update(); } });
  const latS = slider({ label: p(L.lat), min: 0, max: 60, step: 1, value: lat, unit: '°N', onInput: v => { lat = v; update(); } });
  const set = (a, x1, y1, x2, y2) => { a.setAttribute('x1', x1); a.setAttribute('y1', y1); a.setAttribute('x2', x2); a.setAttribute('y2', y2); };
  function update() {
    lowText.textContent = `L · ${fmt(1012 - dp, 1)} hPa`;
    const v = geostrophicWind(dp, lat), len = clamp(20 + dp * 18, 30, H * 0.28);
    set(pgf, cx, mid, cx, mid + len); pgfT.setAttribute('x', cx + 6); pgfT.setAttribute('y', mid + len - 4); pgfT.textContent = p(L.pgf);
    if (v === null) {
      set(cor, cx, mid, cx, mid); corT.textContent = '';
      set(wind, cx - 4, mid - len * 0.6, cx - 4, mid + len * 0.9); windT.setAttribute('x', cx - 10); windT.setAttribute('y', mid - len * 0.6); windT.setAttribute('text-anchor', 'end'); windT.textContent = p(L.wind);
      rows.set('speed', '—'); rows.set('dir', p(L.across)); note.textContent = p(L.eq);
    } else {
      set(cor, cx, mid, cx, mid - len); corT.setAttribute('x', cx + 6); corT.setAttribute('y', mid - len + 10); corT.textContent = p(L.cor);
      const wl = clamp(v * 3, 30, W * 0.38);
      set(wind, cx + wl / 2, mid, cx - wl / 2, mid); windT.setAttribute('x', cx - wl / 2); windT.setAttribute('y', mid - 8); windT.setAttribute('text-anchor', 'start'); windT.textContent = p(L.wind);
      rows.set('speed', `${fmt(v, 0)} m/s · ${fmt(v * 3.6, 0)} km/h`); rows.set('dir', p(L.along)); note.textContent = '';
    }
  }
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 161–165; Mote & Sahu, pp. 64–66; ρ = 1.2 kg/m³', children: [svg, h('div', { class: 'w-controls' }, dpS, latS), rows, note] }));
  update();
  return { destroy() { el.replaceChildren(); } };
}
