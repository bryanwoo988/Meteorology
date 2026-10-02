/* W19 — The station model. A plotted surface observation, in °C as
   Malaysia would report it; tap any part to see what it means.
   Conventions: Ahrens 2010, Appendix C (pp. 461–462): temperature upper
   left, dew point lower left, sea-level pressure upper right as its last
   three digits in tenths, 3-hour tendency below it, sky cover in the
   circle, present weather left of the circle, wind barb pointing to where
   the wind comes from (half barb 5 kt, full barb 10 kt, pennant 50 kt). */

import { s, h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('站点模型：点一个部分', 'The station model: tap a part', 'Model stesen: ketik satu bahagian'),
  hint: T('这是一个下午的雷雨观测。点图上的数字或符号。', 'This is an afternoon thunderstorm report. Tap a number or symbol.', 'Ini laporan ribut petir petang. Ketik nombor atau simbol.'),
  part: {
    t: T('气温 31 °C（左上）', 'Temperature 31 °C (upper left)', 'Suhu 31 °C (kiri atas)'),
    td: T('露点 24 °C（左下）：和气温相差 7 °C，空气很湿', 'Dew point 24 °C (lower left): 7 °C below the temperature, very humid air', 'Takat embun 24 °C (kiri bawah): 7 °C di bawah suhu, udara sangat lembap'),
    p: T('海平面气压，只写最后三位、以 0.1 hPa 为单位：086 = 1008.6 hPa', 'Sea-level pressure, last three digits in tenths: 086 = 1008.6 hPa', 'Tekanan paras laut, tiga digit terakhir dalam persepuluh: 086 = 1008.6 hPa'),
    tend: T('过去 3 小时气压变化：−12 = 下降 1.2 hPa', 'Pressure change in the past 3 hours: −12 = fallen 1.2 hPa', 'Perubahan tekanan 3 jam lalu: −12 = turun 1.2 hPa'),
    sky: T('圆圈涂黑的部分 = 云量；这里 7/8（7 个八分之一）', 'The filled part of the circle is the sky cover: here 7/8 (7 oktas)', 'Bahagian bulatan yang dihitamkan ialah litupan langit: di sini 7/8 (7 okta)'),
    ww: T('现在天气：雷暴（R 形箭头符号），伴有阵雨', 'Present weather: thunderstorm (the arrow-like symbol), with showers', 'Cuaca semasa: ribut petir (simbol seperti anak panah), dengan hujan'),
    wind: T('风杆指向风吹来的方向：这里是南风；一根整羽 = 10 节，半羽 = 5 节，这里 15 节（约 28 km/h）', 'The shaft points to where the wind comes from: here, the south; a full barb is 10 knots, a half barb 5, so 15 knots (about 28 km/h)', 'Batang menunjuk ke arah angin datang: di sini, selatan; satu bulu penuh 10 knot, separuh 5, jadi 15 knot (kira-kira 28 km/j)'),
  },
};

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 520)), H = Math.round(W * 0.8);
  const cx = W * 0.5, cy = H * 0.36, r = Math.max(16, W * 0.065);
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'group', 'aria-label': p(L.title) });
  const out = h('p', { class: 'w-explain', 'aria-live': 'polite' }, p(L.hint));
  const fs = Math.round(clamp(W * 0.055, 14, 26));
  const parts = [];
  const hot = (id, node) => {
    const g = s('g', { class: 'sm-part', tabindex: '0', role: 'button', 'aria-label': p(L.part[id]) }, node);
    const go = () => { out.textContent = p(L.part[id]); parts.forEach(x => x.classList.toggle('is-on', x === g)); };
    g.addEventListener('click', go); g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); } });
    parts.push(g); return g;
  };
  // Wind from the south (180°): the shaft runs straight down out of the circle.
  const dir = 180 * Math.PI / 180, ux = Math.sin(dir), uy = -Math.cos(dir);          // unit vector towards where the wind comes from
  const sx0 = cx + ux * r, sy0 = cy + uy * r, ex = cx + ux * r * 5, ey = cy + uy * r * 5;
  const nx = -uy, ny = ux;                                                          // perpendicular to the shaft
  const barb = (back, k) => { const bx = ex - ux * back, by = ey - uy * back; return `M${bx},${by} L${bx + (nx * 1.6 + ux * 0.5) * r * k},${by + (ny * 1.6 + uy * 0.5) * r * k}`; };
  svg.append(
    hot('wind', s('path', { d: `M${sx0},${sy0} L${ex},${ey} ${barb(0, 1)} ${barb(r * 0.7, 0.5)}`, class: 'sm-ink', 'stroke-width': 2.5 })),
    hot('sky', s('g', {}, s('circle', { cx, cy, r, class: 'sm-circle' }),
      s('path', { d: `M${cx},${cy} L${cx},${cy - r} A${r},${r} 0 1,1 ${cx - r * Math.sin(Math.PI / 4)},${cy - r * Math.cos(Math.PI / 4)} Z`, class: 'sm-fill' }))),
    hot('t', s('text', { x: cx - r * 1.6, y: cy - r * 0.9, 'text-anchor': 'end', class: 'sm-num', 'font-size': fs }, '31')),
    hot('td', s('text', { x: cx - r * 1.6, y: cy + r * 2.1, 'text-anchor': 'end', class: 'sm-num', 'font-size': fs }, '24')),
    hot('p', s('text', { x: cx + r * 1.6, y: cy - r * 0.9, class: 'sm-num', 'font-size': fs }, '086')),
    hot('tend', s('text', { x: cx + r * 1.6, y: cy + r * 0.8, class: 'sm-num', 'font-size': fs }, '−12 ↘')),
    hot('ww', s('path', { d: `M${cx - r * 2.6},${cy - r * 0.6} l${r * 0.9},0 l-${r * 0.5},${r * 0.7} l${r * 0.7},${r * 0.5} m-${r * 0.25},-${r * 0.2} l${r * 0.25},${r * 0.2} l-${r * 0.3},0`, class: 'sm-red', 'stroke-width': 2.5 })),
  );
  el.append(frame({ title: p(L.title), lang, source: 'Ahrens 2010, Appendix C, pp. 461–462 (example values illustrative)', children: [svg, out] }));
  return { destroy() { el.replaceChildren(); } };
}
