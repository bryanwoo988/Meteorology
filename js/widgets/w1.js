/* W1 — The layers of the atmosphere. Drag up and down: the standard
   atmosphere's temperature, pressure and the share of all air below you.
   US Standard Atmosphere 1976 (physics.atmosphereAt). */

import { atmosphereAt } from '../physics.js';
import { s, h, scale, clamp, track, slider, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const L = {
  title: { zh: '大气的分层：上下拖动', en: 'Layers of the atmosphere: drag up and down', ms: 'Lapisan atmosfera: seret ke atas dan ke bawah' },
  alt: { zh: '高度', en: 'Height', ms: 'Ketinggian' },
  temp: { zh: '气温', en: 'Temperature', ms: 'Suhu' },
  pres: { zh: '气压', en: 'Pressure', ms: 'Tekanan' },
  below: { zh: '在你下面的空气', en: 'Air below you', ms: 'Udara di bawah anda' },
  layer: { zh: '所在的层', en: 'Layer', ms: 'Lapisan' },
  troposphere: { zh: '对流层', en: 'Troposphere', ms: 'Troposfera' },
  stratosphere: { zh: '平流层', en: 'Stratosphere', ms: 'Stratosfera' },
  mesosphere: { zh: '中间层', en: 'Mesosphere', ms: 'Mesosfera' },
  thermosphere: { zh: '热层', en: 'Thermosphere', ms: 'Termosfera' },
  tropics: { zh: '热带的对流层顶约 16 km', en: 'Tropical tropopause ≈ 16 km', ms: 'Tropopaus tropika ≈ 16 km' },
  xaxis: { zh: '气温 °C', en: 'Temperature °C', ms: 'Suhu °C' },
  note: { zh: '标准大气是中纬度的平均情况', en: 'The standard atmosphere is a mid-latitude average', ms: 'Atmosfera piawai ialah purata latitud sederhana' },
  source: 'US Standard Atmosphere 1976; Mote & Sahu (tropical tropopause)',
};
const BANDS = [[0, 11, 'troposphere'], [11, 50, 'stratosphere'], [50, 85, 'mesosphere'], [85, 90, 'thermosphere']];

export function mount(el, { lang }) {
  const p = k => pick(L[k], lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(clamp(W * 1.05, 300, 520));
  const M = { t: 26, r: 12, b: 36, l: 40 };
  const x = scale(-100, 20, M.l, W - M.r), y = scale(0, 90, H - M.b, M.t);
  let z = 5;

  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p('title') });
  BANDS.forEach(([a, b, name], i) => {
    svg.append(s('rect', { x: M.l, width: W - M.l - M.r, y: y(b), height: y(a) - y(b), class: `band band-${i % 2}` }));
    // The curve runs along the right side in the troposphere, so that label goes left.
    const left = name === 'troposphere';
    svg.append(s('text', { x: left ? M.l + 6 : W - M.r - 6, y: (y(a) + y(b)) / 2 + 4, 'text-anchor': left ? 'start' : 'end', class: 'band-label' }, p(name)));
  });
  const axes = s('g', { class: 'chart-axes' });
  for (let km = 0; km <= 90; km += 10) axes.append(s('text', { x: M.l - 6, y: y(km) + 4, 'text-anchor': 'end' }, String(km)));
  axes.append(s('text', { x: M.l - 6, y: M.t - 12, 'text-anchor': 'end', class: 'unit' }, 'km'));
  for (const tc of [-80, -40, 0]) {
    axes.append(s('line', { x1: x(tc), x2: x(tc), y1: M.t, y2: H - M.b, class: 'grid' }));
    axes.append(s('text', { x: x(tc), y: H - M.b + 16, 'text-anchor': 'middle' }, String(tc)));
  }
  axes.append(s('text', { x: (M.l + W - M.r) / 2, y: H - 4, 'text-anchor': 'middle', class: 'unit' }, p('xaxis')));
  svg.append(axes);

  let d = '';
  for (let km = 0; km <= 90; km += 0.5) { const a = atmosphereAt(km * 1000); d += `${km ? 'L' : 'M'}${x(a.tC).toFixed(1)},${y(km).toFixed(1)}`; }
  svg.append(s('path', { d, class: 'series', style: 'stroke: var(--mercury)' }));
  svg.append(s('line', { x1: M.l, x2: W - M.r, y1: y(16), y2: y(16), class: 'w-guide', style: 'stroke: var(--leaf)' }));
  svg.append(s('text', { x: M.l + 6, y: y(16) - 5, class: 'w-td-label', style: 'fill: var(--leaf)' }, p('tropics')));

  const level = s('line', { x1: M.l, x2: W - M.r, class: 'w-level' });
  const dot = s('circle', { r: 8, class: 'w-dot' });
  svg.append(level, dot);
  svg.style.touchAction = 'none';

  const rows = readout([['alt', p('alt')], ['temp', p('temp')], ['pres', p('pres')], ['below', p('below')], ['layer', p('layer')]]);
  const zs = slider({ label: p('alt'), min: 0, max: 90, step: 0.5, value: z, unit: ' km', onInput: v => { z = v; update(); } });

  function update() {
    const a = atmosphereAt(z * 1000);
    level.setAttribute('y1', y(z)); level.setAttribute('y2', y(z));
    dot.setAttribute('cx', x(a.tC)); dot.setAttribute('cy', y(z));
    rows.set('alt', `${fmt(z, 1)} km`);
    rows.set('temp', `${fmt(a.tC, 1)} °C`);
    rows.set('pres', a.pHpa >= 10 ? `${fmt(a.pHpa, 0)} hPa` : `${a.pHpa.toPrecision(2)} hPa`);
    rows.set('below', `${fmt(100 * (1 - a.pHpa / 1013.25), z > 30 ? 2 : 1)} %`);
    rows.set('layer', p(a.layer));
    zs.set(z);
  }
  track(svg, pt => { z = clamp(Math.round(y.invert(pt.y) * 2) / 2, 0, 90); update(); });
  el.append(frame({ title: p('title'), lang, source: L.source, children: [svg, h('p', { class: 'w-source' }, p('note')), h('div', { class: 'w-controls' }, zs), rows] }));
  update();
  return { destroy() { el.replaceChildren(); } };
}
