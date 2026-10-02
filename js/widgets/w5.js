/* W5 — Humidity. The saturation vapour pressure curve, with the air as a
   point you drag: right = warmer, up = more vapour. Following the point
   left until it meets the curve gives the dew point. Formulas: physics.js
   (Magnus; Stull 2011 for the wet-bulb). */

import { satVapPres, dewPoint, wetBulbStull } from '../physics.js';
import { s, h, scale, clamp, track, slider, readout, frame, fmt, niceTicks } from './kit.js';
import { pick } from '../i18n.js';

const L = {
  title: { zh: '空气里的水汽：拖动圆点', en: 'Water vapour in the air: drag the dot', ms: 'Wap air dalam udara: seret titik itu' },
  curve: { zh: '饱和水汽压', en: 'saturation vapour pressure', ms: 'tekanan wap tepu' },
  temp: { zh: '气温', en: 'Temperature', ms: 'Suhu' },
  rh: { zh: '相对湿度', en: 'Relative humidity', ms: 'Kelembapan relatif' },
  es: { zh: '饱和水汽压', en: 'Saturation vapour pressure', ms: 'Tekanan wap tepu' },
  e: { zh: '实际水汽压', en: 'Actual vapour pressure', ms: 'Tekanan wap sebenar' },
  td: { zh: '露点', en: 'Dew point', ms: 'Takat embun' },
  tw: { zh: '湿球温度', en: 'Wet-bulb', ms: 'Bebuli basah' },
  spread: { zh: '气温 − 露点', en: 'Temperature − dew point', ms: 'Suhu − takat embun' },
  xaxis: { zh: '气温 °C', en: 'Temperature °C', ms: 'Suhu °C' },
  source: 'Magnus (Alduchov & Eskridge 1996); Stull 2011',
};

const M = { t: 28, r: 14, b: 40, l: 40 };
const TMIN = 0, TMAX = 45, EMAX = 100;

export function mount(el, { lang }) {
  const p = k => pick(L[k], lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W < 480 ? W * 0.8 : W * 0.5);
  const x = scale(TMIN, TMAX, M.l, W - M.r);
  const y = scale(0, EMAX, H - M.b, M.t);
  let T = 30, RH = 70;

  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p('title') });
  const axes = s('g', { class: 'chart-axes' });
  for (const v of niceTicks(0, EMAX, 5)) {
    axes.append(s('line', { x1: M.l, x2: W - M.r, y1: y(v), y2: y(v), class: 'grid' }));
    axes.append(s('text', { x: M.l - 8, y: y(v) + 4, 'text-anchor': 'end' }, String(v)));
  }
  for (const v of niceTicks(TMIN, TMAX, W < 480 ? 5 : 9)) axes.append(s('text', { x: x(v), y: H - M.b + 18, 'text-anchor': 'middle' }, String(v)));
  axes.append(s('text', { x: M.l - 8, y: M.t - 14, 'text-anchor': 'end', class: 'unit' }, 'hPa'));
  axes.append(s('text', { x: (M.l + W - M.r) / 2, y: H - 6, 'text-anchor': 'middle', class: 'unit' }, p('xaxis')));
  svg.append(axes);

  let d = '';
  for (let tc = TMIN; tc <= TMAX; tc += 0.5) d += `${tc === TMIN ? 'M' : 'L'}${x(tc).toFixed(1)},${y(satVapPres(tc)).toFixed(1)}`;
  svg.append(s('path', { d, class: 'series', style: 'stroke: var(--sky)' }));
  svg.append(s('text', { x: x(38) - 6, y: y(satVapPres(38)) - 6, 'text-anchor': 'end', class: 'curve-label' }, p('curve')));

  // Saturated region above the curve is unreachable for the point.
  const guide = s('line', { class: 'w-guide' });
  const drop = s('line', { class: 'w-guide' });
  const tdDot = s('circle', { r: 5, class: 'w-td' });
  const tdText = s('text', { class: 'w-td-label', 'text-anchor': 'middle' });
  const dot = s('circle', { r: 9, class: 'w-dot' });
  svg.append(guide, drop, tdDot, tdText, dot);

  const rows = readout([['es', p('es')], ['e', p('e')], ['td', p('td')], ['tw', p('tw')], ['spread', p('spread')]]);

  const tSlider = slider({ label: p('temp'), min: TMIN, max: TMAX, step: 0.5, value: T, unit: ' °C', onInput: v => { T = v; update(); } });
  const rSlider = slider({ label: p('rh'), min: 1, max: 100, step: 1, value: RH, unit: ' %', onInput: v => { RH = v; update(); } });

  function update() {
    const es = satVapPres(T), e = es * RH / 100, td = dewPoint(T, RH), tw = wetBulbStull(T, RH);
    const px = x(T), py = y(e);
    dot.setAttribute('cx', px); dot.setAttribute('cy', py);
    if (td !== null) {
      const tx = x(clamp(td, TMIN - 30, TMAX));
      guide.setAttribute('x1', Math.max(tx, M.l)); guide.setAttribute('x2', px); guide.setAttribute('y1', py); guide.setAttribute('y2', py);
      const visible = td >= TMIN;
      tdDot.style.display = tdText.style.display = drop.style.display = visible ? '' : 'none';
      tdDot.setAttribute('cx', tx); tdDot.setAttribute('cy', py);
      drop.setAttribute('x1', tx); drop.setAttribute('x2', tx); drop.setAttribute('y1', py); drop.setAttribute('y2', H - M.b);
      tdText.setAttribute('x', tx); tdText.setAttribute('y', py - 12);
      tdText.textContent = `${p('td')} ${fmt(td, 1)} °C`;
    }
    rows.set('es', `${fmt(es, 1)} hPa`);
    rows.set('e', `${fmt(e, 1)} hPa (${RH} %)`);
    rows.set('td', `${fmt(td, 1)} °C`);
    rows.set('tw', tw === null ? '—' : `${fmt(tw, 1)} °C`);
    rows.set('spread', td === null ? '—' : `${fmt(T - td, 1)} °C`);
    tSlider.set(T); rSlider.set(RH);
  }

  track(svg, pt => {
    T = clamp(Math.round(x.invert(pt.x) * 2) / 2, TMIN, TMAX);
    const es = satVapPres(T);
    RH = clamp(Math.round(100 * y.invert(pt.y) / es), 1, 100);
    update();
  });
  svg.style.touchAction = 'none';

  el.append(frame({ title: p('title'), lang, source: L.source, children: [svg, h('div', { class: 'w-controls' }, tSlider, rSlider), rows] }));
  update();
  return { destroy() { el.replaceChildren(); } };
}
