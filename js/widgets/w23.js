/* W23 — Reference evapotranspiration (ET₀) by the FAO-56 Penman–Monteith
   method, computed live (physics.et0) for a site at Kuala Lumpur's
   latitude and height on today's date. Drag the weather and see how many
   millimetres of water a well-watered grass surface would use today; set a
   crop coefficient to turn ET₀ into a crop's use (ETc = Kc × ET₀). */

import { et0 } from '../physics.js';
import { h, slider, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('ET₀ 计算：拖动今天的天气', 'ET₀ calculator: drag today\'s weather', 'Kalkulator ET₀: seret cuaca hari ini'),
  tmax: T('最高气温', 'Maximum temperature', 'Suhu maksimum'), tmin: T('最低气温', 'Minimum temperature', 'Suhu minimum'),
  rh: T('下午最低相对湿度', 'Lowest afternoon humidity', 'Kelembapan petang terendah'), wind: T('2 米风速', 'Wind at 2 m', 'Angin pada 2 m'),
  sun: T('日照时数', 'Sunshine hours', 'Jam cahaya matahari'), kc: T('作物系数 Kc', 'Crop coefficient Kc', 'Pekali tanaman Kc'),
  et0: T('ET₀（参考蒸散）', 'ET₀ (reference)', 'ET₀ (rujukan)'), etc: T('ETc（这种作物）', 'ETc (this crop)', 'ETc (tanaman ini)'),
  note: T('计算假设清晨湿度 95 %、地点在北纬 3.1°、海拔 60 米。', 'Assumes 95 % humidity at dawn, a site at 3.1°N and 60 m above sea level.', 'Mengandaikan kelembapan 95 % pada subuh, tapak pada 3.1°U dan 60 m dari paras laut.'),
};
const doy = () => { const d = new Date(), s = new Date(d.getFullYear(), 0, 0); return Math.floor((d - s) / 864e5); };

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const st = { tmax: 32, tmin: 24, rh: 60, wind: 1.5, sun: 6, kc: 1 };
  const rows = readout([['et0', p(L.et0)], ['etc', p(L.etc)]]);
  const mk = (k, min, max, step, unit) => slider({ label: p(L[k]), min, max, step, value: st[k], unit, onInput: v => { st[k] = v; if (st.tmin > st.tmax) st.tmin = st.tmax; draw(); } });
  const controls = h('div', { class: 'w-controls' },
    mk('tmax', 24, 38, 0.5, ' °C'), mk('tmin', 18, 28, 0.5, ' °C'), mk('rh', 30, 95, 1, ' %'), mk('wind', 0, 6, 0.1, ' m/s'), mk('sun', 0, 12, 0.5, ' h'), mk('kc', 0.3, 1.3, 0.05, ''));
  function draw() {
    const e = et0(st.tmax, st.tmin, 95, st.rh, st.wind, st.sun, 3.14, 60, doy());
    rows.set('et0', `${fmt(e, 1)} mm`); rows.set('etc', `${fmt(e * st.kc, 1)} mm`);
  }
  draw();
  el.append(frame({ title: p(L.title), lang, source: 'FAO Irrigation and Drainage Paper 56 (Allen et al. 1998), Penman–Monteith; physics.js', children: [controls, rows, h('p', { class: 'w-source' }, p(L.note))] }));
  return { destroy() { el.replaceChildren(); } };
}
