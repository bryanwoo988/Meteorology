/* W20 — Grid resolution. The same afternoon: a 20 km cluster of
   thunderstorms and a 30 km wide mountain range under a 9, 25 or 100 km
   model grid. Each box can hold only one value, the average over the box,
   so a coarse grid smears the storm and flattens the hills. Schematic;
   Ahrens 2010, pp. 254–256 (grid points, resolution, thunderstorms too
   small for coarse grids). */

import { s, h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('网格分辨率：切换格子大小', 'Grid resolution: switch the box size', 'Resolusi grid: tukar saiz kotak'),
  storm: T('雷雨（约 20 公里）', 'Storm cluster (about 20 km)', 'Kelompok ribut (kira-kira 20 km)'), hill: T('山脉（约 30 公里宽）', 'Mountain range (about 30 km wide)', 'Banjaran (kira-kira 30 km lebar)'),
  text: {
    9: T('9 公里：雷雨占了好几格，最大雨量还看得出来；山脉的起伏也大致保留。ECMWF 的 ENS 约是这个分辨率。', '9 km: the storm fills several boxes and its peak still shows; the mountains keep their shape. ECMWF\'s ENS runs at about this spacing.', '9 km: ribut memenuhi beberapa kotak dan puncaknya masih kelihatan; banjaran mengekalkan bentuknya. ENS ECMWF berjalan pada jarak kira-kira ini.'),
    25: T('25 公里：雷雨只剩一两格，雨量被平均掉一大半；山被削低了。', '25 km: the storm is down to a box or two and most of its peak is averaged away; the hills are cut down.', '25 km: ribut tinggal satu dua kotak dan kebanyakan puncaknya dipuratakan; bukit menjadi rendah.'),
    100: T('100 公里：整场雷雨被摊在一大格里，看起来只是小雨；山几乎不见了。所以这么粗的模型只能用“参数化”估计雷雨的效果。', '100 km: the whole storm is spread across one big box and looks like light rain; the mountains almost vanish. A model this coarse can only estimate storms through parameterisation.', '100 km: seluruh ribut tersebar dalam satu kotak besar dan kelihatan seperti hujan renyai; banjaran hampir hilang. Model sekasar ini hanya boleh menganggar ribut melalui parameterisasi.'),
  },
};
const SPAN = 200;                                           // km shown across
const rain = x => 60 * Math.exp(-(((x - 120) / 8) ** 2));   // mm/h, a storm about 20 km across
const hill = x => 1500 * Math.exp(-(((x - 55) / 12) ** 2)); // m, a range about 30 km wide

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.55);
  const X = km => 10 + (W - 20) * km / SPAN, base = H - 26, top = 30;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const tabs = h('div', { class: 'stage-chips' }), out = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  const curve = (f, scale) => Array.from({ length: 201 }, (_, i) => `${i ? 'L' : 'M'}${X(i)},${base - f(i) * scale}`).join('');
  function draw(dx) {
    const rs = (base - top) / 70, hs = (base - top) / 2600, kids = [];
    for (let x0 = 0; x0 < SPAN; x0 += dx) {
      const n = 20; let rr = 0, hh = 0;
      for (let k = 0; k < n; k++) { const x = Math.min(SPAN, x0 + dx * (k + 0.5) / n); rr += rain(x) / n; hh += hill(x) / n; }
      const w = X(Math.min(SPAN, x0 + dx)) - X(x0);
      kids.push(s('rect', { x: X(x0), y: base - hh * hs, width: w, height: hh * hs, class: 'grid-hill' }),
        s('rect', { x: X(x0), y: base - rr * rs, width: w, height: rr * rs, class: 'grid-rain' }),
        s('line', { x1: X(x0), x2: X(x0), y1: top - 6, y2: base, class: 'grid-line' }));
    }
    svg.replaceChildren(...kids,
      s('path', { d: curve(hill, hs), class: 'series', style: 'stroke: var(--leaf); stroke-dasharray: 4 3' }),
      s('path', { d: curve(rain, rs), class: 'series', style: 'stroke: var(--rain)' }),
      s('line', { x1: X(0), x2: X(SPAN), y1: base, y2: base, class: 'grid-line' }),
      s('text', { x: X(120), y: top - 10, 'text-anchor': 'middle', class: 'band-label' }, p(L.storm)),
      s('text', { x: X(55), y: top + 34, 'text-anchor': 'middle', class: 'band-label' }, p(L.hill)),
      s('text', { x: X(SPAN), y: H - 6, 'text-anchor': 'end', class: 'band-label' }, `${SPAN} km`));
    out.textContent = p(L.text[dx]);
    tabs.replaceChildren(...[9, 25, 100].map(k => { const b = h('button', { type: 'button', class: `chip${k === dx ? ' is-on' : ''}` }, `${k} km`); b.addEventListener('click', () => draw(k)); return b; }));
  }
  draw(25);
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 254–256; ECMWF (ENS ≈ 9 km)', children: [tabs, svg, out] }));
  return { destroy() { el.replaceChildren(); } };
}
