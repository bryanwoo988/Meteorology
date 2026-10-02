/* W2 — Day length and the noon Sun. Pick a latitude and a date: the curve
   is day length through the year, the arc shows how high the Sun climbs at
   noon, and the clock time of solar noon is given for Kuala Lumpur.
   physics.dayLength / noonElevation / solarNoon. */

import { dayLength, noonElevation, solarNoon, declination as declinationAt } from '../physics.js';
import { s, h, scale, clamp, track, slider, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const L = {
  title: { zh: '日照：选纬度和日期', en: 'Sunshine: choose a latitude and a date', ms: 'Cahaya matahari: pilih latitud dan tarikh' },
  lat: { zh: '纬度', en: 'Latitude', ms: 'Latitud' },
  day: { zh: '日期', en: 'Date', ms: 'Tarikh' },
  len: { zh: '白天长度', en: 'Day length', ms: 'Panjang siang' },
  elev: { zh: '正午太阳高度', en: 'Noon Sun height', ms: 'Ketinggian Matahari tengah hari' },
  noon: { zh: '吉隆坡的正午（时钟）', en: 'Solar noon in Kuala Lumpur', ms: 'Tengah hari suria di Kuala Lumpur' },
  kl: { zh: '吉隆坡', en: 'Kuala Lumpur', ms: 'Kuala Lumpur' },
  yaxis: { zh: '白天长度（小时）', en: 'Day length (hours)', ms: 'Panjang siang (jam)' },
  source: 'Cooper 1969 (declination); NOAA equation of time; sunrise at −0.833°',
};
const MONTHS = {
  zh: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
  en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  ms: ['Jan', 'Feb', 'Mac', 'Apr', 'Mei', 'Jun', 'Jul', 'Ogo', 'Sep', 'Okt', 'Nov', 'Dis'],
};
const STARTS = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335];
const KL = { lat: 3.14, lon: 101.69 };

function dateLabel(doy, lang) {
  let m = 11; while (STARTS[m] > doy) m--;
  const d = doy - STARTS[m] + 1;
  return lang === 'zh' ? `${MONTHS.zh[m]}${d}日` : `${d} ${MONTHS[lang][m]}`;
}
const hm = hrs => `${Math.floor(hrs)}:${String(Math.round((hrs % 1) * 60) % 60).padStart(2, '0')}`;

export function mount(el, { lang }) {
  const p = k => pick(L[k], lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W < 480 ? W * 0.62 : W * 0.42);
  const M = { t: 26, r: 12, b: 30, l: 34 };
  const x = scale(1, 365, M.l, W - M.r), y = scale(0, 24, H - M.b, M.t);
  let lat = KL.lat, doy = 172;

  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p('title') });
  const axes = s('g', { class: 'chart-axes' });
  for (const v of [0, 6, 12, 18, 24]) {
    axes.append(s('line', { x1: M.l, x2: W - M.r, y1: y(v), y2: y(v), class: 'grid' }));
    axes.append(s('text', { x: M.l - 6, y: y(v) + 4, 'text-anchor': 'end' }, String(v)));
  }
  STARTS.forEach((d, i) => { if (i % (W < 480 ? 3 : 2) === 0) axes.append(s('text', { x: x(d + 14), y: H - M.b + 16, 'text-anchor': 'middle' }, MONTHS[lang][i])); });
  axes.append(s('text', { x: M.l - 6, y: M.t - 12, 'text-anchor': 'end', class: 'unit' }, 'h'));
  svg.append(axes);

  const curve = (la, cls, style) => {
    let d = '';
    for (let k = 1; k <= 365; k += 2) d += `${k === 1 ? 'M' : 'L'}${x(k).toFixed(1)},${y(dayLength(la, k)).toFixed(1)}`;
    return s('path', { d, class: cls, style });
  };
  svg.append(curve(KL.lat, 'series', 'stroke: var(--leaf); stroke-dasharray: 5 4'));
  const main = curve(lat, 'series', 'stroke: var(--sun)');
  svg.append(main);
  const cursor = s('line', { y1: M.t, y2: H - M.b, class: 'w-level' });
  const dot = s('circle', { r: 7, class: 'w-dot' });
  svg.append(cursor, dot);
  svg.style.touchAction = 'none';

  // Noon Sun gauge: a quarter circle, the Sun at its noon elevation.
  const G = 120;
  const gauge = s('svg', { viewBox: `0 0 ${G} ${G * 0.62}`, class: 'w-gauge', 'aria-hidden': 'true' });
  gauge.append(s('path', { d: `M10,${G * 0.56} A${G * 0.45},${G * 0.45} 0 0 1 ${G - 10},${G * 0.56}`, class: 'gauge-arc' }));
  gauge.append(s('line', { x1: 10, x2: G - 10, y1: G * 0.56, y2: G * 0.56, class: 'gauge-ground' }));
  const ray = s('line', { x1: G / 2, y1: G * 0.56, class: 'gauge-ray' });
  const sun = s('circle', { r: 7, class: 'gauge-sun' });
  const SIDE = { zh: ['南', '北'], en: ['S', 'N'], ms: ['S', 'U'] }[lang];
  gauge.append(s('text', { x: 6, y: G * 0.56 + 12, class: 'gauge-side' }, SIDE[0]), s('text', { x: G - 6, y: G * 0.56 + 12, 'text-anchor': 'end', class: 'gauge-side' }, SIDE[1]));
  gauge.append(ray, sun);

  const rows = readout([['len', p('len')], ['elev', p('elev')], ['noon', p('noon')]]);
  const latS = slider({ label: p('lat'), min: -66, max: 66, step: 0.5, value: lat, unit: '°', onInput: v => { lat = v; redrawCurve(); update(); } });
  const dayS = slider({ label: p('day'), min: 1, max: 365, step: 1, value: doy, onInput: v => { doy = v; update(); } });
  const klBtn = h('button', { type: 'button', class: 'chip' }, `${p('kl')} 3.1°N`);
  klBtn.addEventListener('click', () => { lat = KL.lat; latS.set(lat); redrawCurve(); update(); });

  function redrawCurve() { main.setAttribute('d', curve(lat).getAttribute('d')); }
  function update() {
    const len = dayLength(lat, doy), el2 = noonElevation(lat, doy);
    cursor.setAttribute('x1', x(doy)); cursor.setAttribute('x2', x(doy));
    dot.setAttribute('cx', x(doy)); dot.setAttribute('cy', y(len));
    // The noon Sun is due south when it is south of the zenith, due north otherwise.
    const north = declinationAt(doy) > lat;
    const a = (north ? 180 - clamp(el2, 0, 90) : clamp(el2, 0, 90)) * Math.PI / 180, r = G * 0.45;
    const sx = G / 2 + r * Math.cos(Math.PI - a), sy = G * 0.56 - r * Math.sin(a);
    ray.setAttribute('x2', sx); ray.setAttribute('y2', sy);
    sun.setAttribute('cx', sx); sun.setAttribute('cy', sy);
    rows.set('len', `${hm(len)} h`);
    rows.set('elev', `${fmt(el2, 0)}°`);
    rows.set('noon', `${hm(solarNoon(KL.lon, doy, 8))} (${dateLabel(doy, lang)})`);
    dayS.querySelector('output').textContent = dateLabel(doy, lang);
    latS.set(lat);
  }
  track(svg, pt => { doy = clamp(Math.round(x.invert(pt.x)), 1, 365); dayS.set(doy); update(); });
  el.append(frame({ title: p('title'), lang, source: L.source, children: [svg, h('div', { class: 'w-row' }, gauge, h('div', { class: 'w-controls' }, latS, dayS, klBtn)), rows] }));
  update();
  return { destroy() { el.replaceChildren(); } };
}
