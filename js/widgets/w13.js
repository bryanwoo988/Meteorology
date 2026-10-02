/* W13 — Malaysia's monsoon calendar. Drag the month: the prevailing
   10 m wind over the region and the month's average rainfall in four
   towns. Real ERA5 averages for 1991–2020 (data/maps/monsoon-normals.json);
   season names and dates follow MetMalaysia. */

import { baseMap } from '../maps.js';
import { loadData } from '../content.js';
import { h, s, clamp, slider, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const MONTHS = {
  zh: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
  en: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
  ms: ['Januari', 'Februari', 'Mac', 'April', 'Mei', 'Jun', 'Julai', 'Ogos', 'September', 'Oktober', 'November', 'Disember'],
};
const L = {
  title: T('季风月历：拖动月份', 'The monsoon calendar: drag the month', 'Kalendar monsun: seret bulan'),
  month: T('月份', 'Month', 'Bulan'),
  rain: T('这个月的平均雨量（1991–2020）', 'Average rain this month (1991–2020)', 'Purata hujan bulan ini (1991–2020)'),
  towns: { kl: T('吉隆坡', 'Kuala Lumpur', 'Kuala Lumpur'), kotabharu: T('哥打巴鲁', 'Kota Bharu', 'Kota Bharu'), kuching: T('古晋', 'Kuching', 'Kuching'), kotakinabalu: T('亚庇', 'Kota Kinabalu', 'Kota Kinabalu') },
  season: {
    ne: T('东北季风（11 月到 3 月）：主要雨季，东海岸、砂拉越西部和沙巴东部雨最多', 'North-east monsoon (November to March): the main rainy season, wettest on the east coast, western Sarawak and eastern Sabah', 'Monsun timur laut (November hingga Mac): musim hujan utama, paling basah di pantai timur, barat Sarawak dan timur Sabah'),
    inter: T('季风转换期：风弱、风向不定；早上晴朗，下午容易有雷雨', 'Inter-monsoon: light, variable winds; clear mornings help afternoon thunderstorms form', 'Peralihan monsun: angin lemah dan berubah-ubah; pagi yang cerah membantu ribut petir terbentuk pada sebelah petang'),
    sw: T('西南季风（5 月底到 9 月）：比较干，大部分州每月雨量较少；沙巴例外', 'South-west monsoon (late May to September): relatively dry, with low monthly rain in most states; Sabah is the exception', 'Monsun barat daya (akhir Mei hingga September): agak kering, dengan hujan bulanan rendah di kebanyakan negeri; Sabah pengecualian'),
  },
};
// MetMalaysia: SW monsoon late May–September, NE monsoon November–March, inter-monsoon between.
const SEASON = ['ne', 'ne', 'ne', 'inter', 'inter', 'sw', 'sw', 'sw', 'sw', 'inter', 'ne', 'ne'];
const KMH_TO_DEG = 0.17;  // arrow length on the map: 30 km/h ≈ 5°

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const [m, d] = await Promise.all([baseMap('seasia', { width: W, bbox: [93, -6, 124, 13], label: p(L.title) }), loadData('maps/monsoon-normals')]);
  let month = new Date().getMonth();
  const head = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  const BW = W, rowH = 26, BH = rowH * 4 + 8, labW = Math.min(110, BW * 0.32);
  const bars = s('svg', { viewBox: `0 0 ${BW} ${BH}`, class: 'w-svg', role: 'img', 'aria-label': p(L.rain) });
  const ms = slider({ label: p(L.month), min: 1, max: 12, step: 1, value: month + 1, onInput: v => { month = v - 1; draw(); } });
  function draw() {
    const arrows = d.winds.map(w => {
      const u = w.u[month], v = w.v[month], len = Math.max(0.6, Math.hypot(u, v) * KMH_TO_DEG), k = len / (Math.hypot(u, v) || 1);
      return { from: [w.at[0] - u * k / 2, w.at[1] - v * k / 2], to: [w.at[0] + u * k / 2, w.at[1] + v * k / 2], color: 'sky' };
    });
    const towns = Object.entries(d.towns);
    m.setLayers([{ type: 'arrows', items: arrows }, { type: 'points', items: towns.map(([k, t]) => ({ at: t.at, label: p(L.towns[k]), color: 'ink-2', r: 3 })) }]);
    const max = 450, x0 = labW, x1 = BW - 46;
    bars.replaceChildren(...towns.flatMap(([k, t], i) => {
      const y = 4 + i * rowH, mm = t.rain[month], w = (x1 - x0) * Math.min(mm, max) / max;
      return [s('text', { x: 0, y: y + 15, class: 'band-label' }, p(L.towns[k])),
        s('rect', { x: x0, y: y + 4, width: Math.max(1, w), height: 14, rx: 3, style: 'fill: var(--rain)' }),
        s('text', { x: x0 + w + 6, y: y + 15, class: 'band-label' }, `${mm} mm`)];
    }));
    head.textContent = `${MONTHS[lang][month]} — ${p(L.season[SEASON[month]])}`;
  }
  draw();
  el.append(frame({ title: p(L.title), lang, source: 'ERA5 1991–2020 via Open-Meteo (10 m wind, monthly rain); seasons: MetMalaysia', children: [m.el, h('div', { class: 'w-controls' }, ms), head, h('p', { class: 'w-source' }, p(L.rain)), bars] }));
  return { destroy() { el.replaceChildren(); } };
}
