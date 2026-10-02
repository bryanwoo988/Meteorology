/* W25 — Forecast time scales. Drag from hours to months and see which
   ECMWF product (and which other tool) covers that range. Facts: ECMWF
   documentation pages (medium range up to 15 days, sub-seasonal up to
   46 days, seasonal up to 7 months, annual 13 months), GloFAS on the
   Copernicus EWDS (river forecasts to 30 days), ESS p. 258 (persistence
   and trend forecasts for the first hours). */

import { h, slider, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('预报的时间尺度：拖动看多远', 'Forecast time scales: drag how far ahead', 'Skala masa ramalan: seret sejauh mana'),
  ahead: T('预报多远', 'How far ahead', 'Sejauh mana'),
};
// Stops along a log-like scale: [label, product, explanation]
const STOPS = [
  [T('0–2 小时', '0–2 hours', '0–2 jam'), T('雷达和卫星外推（临近预报）', 'Radar and satellite extrapolation (nowcasting)', 'Ekstrapolasi radar dan satelit (ramalan kini)'), T('雷雨区按现在的方向和速度往前推；只在头几个小时最准。', 'Rain areas are moved on at their present speed and direction; best for the first few hours.', 'Kawasan hujan digerakkan pada kelajuan dan arah semasa; terbaik untuk beberapa jam pertama.')],
  [T('1–4 天', '1–4 days', '1–4 hari'), T('区域模型（例如 MetMalaysia 的 3 公里 WRF）和全球模型', 'Regional models (e.g. MetMalaysia\'s 3 km WRF) and global models', 'Model serantau (cth. WRF 3 km MetMalaysia) dan model global'), T('格子越细，越能画出雷雨和地形；MetMalaysia 的区域模型预报 4 天。', 'Finer grids draw storms and terrain better; MetMalaysia\'s regional model runs 4 days ahead.', 'Grid yang lebih halus melukis ribut dan rupa bumi dengan lebih baik; model serantau MetMalaysia meramal 4 hari.')],
  [T('到 15 天', 'Up to 15 days', 'Hingga 15 hari'), T('ECMWF ENS（51 个成员、约 9 公里）', 'ECMWF ENS (51 members, about 9 km)', 'ECMWF ENS (51 ahli, kira-kira 9 km)'), T('每天 00 和 12 UTC 各跑一次，另有 06、18 UTC 的较短预报；越往后越要看概率。', 'Run from 00 and 12 UTC each day, with shorter runs from 06 and 18 UTC; further out, look at the probabilities.', 'Dijalankan dari 00 dan 12 UTC setiap hari, dengan larian lebih pendek dari 06 dan 18 UTC; lebih jauh, lihat kebarangkalian.')],
  [T('到 30 天', 'Up to 30 days', 'Hingga 30 hari'), T('GloFAS 全球洪水预报', 'GloFAS global flood forecasts', 'Ramalan banjir global GloFAS'), T('把 ECMWF 的集合预报喂进水文模型，预报河流流量。', 'Feeds ECMWF ensemble forecasts into a hydrological model to forecast river flow.', 'Memasukkan ramalan ensemble ECMWF ke dalam model hidrologi untuk meramal aliran sungai.')],
  [T('到 46 天', 'Up to 46 days', 'Hingga 46 hari'), T('ECMWF 次季节预报', 'ECMWF sub-seasonal forecasts', 'Ramalan sub-musim ECMWF'), T('每天发布，约 36 公里；看的是每一星期比平常偏暖偏湿还是偏冷偏干。', 'Issued daily at about 36 km; they show whether each week is likely warmer, wetter, cooler or drier than normal.', 'Dikeluarkan setiap hari pada kira-kira 36 km; ia menunjukkan sama ada setiap minggu lebih panas, basah, sejuk atau kering daripada biasa.')],
  [T('到 7 个月', 'Up to 7 months', 'Hingga 7 bulan'), T('ECMWF SEAS5 季节预报', 'ECMWF SEAS5 seasonal forecast', 'Ramalan bermusim ECMWF SEAS5'), T('每月一次，51 个成员；给的是“偏高、正常、偏低”的概率，也预报厄尔尼诺。', 'Monthly, 51 members; gives the chances of above, near or below normal, and forecasts El Niño.', 'Bulanan, 51 ahli; memberi peluang di atas, hampir atau di bawah normal, dan meramal El Niño.')],
  [T('到 13 个月', 'Up to 13 months', 'Hingga 13 bulan'), T('ECMWF 年度预报', 'ECMWF annual forecast', 'Ramalan tahunan ECMWF'), T('同一个系统每三个月跑一次，延长到 13 个月。', 'The same system, run every three months out to 13 months.', 'Sistem yang sama, dijalankan setiap tiga bulan hingga 13 bulan.')],
];

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const ladder = h('ol', { class: 'ts-ladder' });
  const out = h('div', { class: 'w-explain', 'aria-live': 'polite' });
  let k = 2;
  const sl = slider({ label: p(L.ahead), min: 0, max: STOPS.length - 1, step: 1, value: k, onInput: v => { k = v; draw(); } });
  function draw() {
    const [range, prod, why] = STOPS[k];
    sl.querySelector('output').textContent = p(range);
    ladder.replaceChildren(...STOPS.map(([r, pr], i) => h('li', { class: i === k ? 'is-on' : '' }, h('strong', {}, p(r)), ` — ${p(pr)}`)));
    out.replaceChildren(h('p', {}, h('strong', {}, p(prod))), h('p', {}, p(why)));
  }
  draw();
  el.append(frame({ title: p(L.title), lang, source: 'ECMWF (medium, sub-seasonal and seasonal forecast pages); Copernicus EWDS (GloFAS); MetMalaysia TN 1/2022; Ahrens 2010, p. 258', children: [h('div', { class: 'w-controls' }, sl), out, ladder] }));
  return { destroy() { el.replaceChildren(); } };
}
