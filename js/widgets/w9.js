/* W9 — The pressure levels forecasters look at, at their real heights over
   Kuala Lumpur (Open-Meteo forecasts, Aug–Oct 2026 average,
   data/series/kl-levels-2026.json). Tap a level to see what it shows. */

import { s, h, scale, clamp, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';
import { loadData } from '../content.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('高空的几个气压层：点一层看看', 'The pressure levels aloft: tap one', 'Aras tekanan di udara atas: ketik satu'),
  height: T('平均高度', 'Average height', 'Ketinggian purata'), temp: T('平均气温', 'Average temperature', 'Suhu purata'), use: T('看什么', 'What it shows', 'Apa yang ditunjukkan'),
};
const USE = {
  850: T('低空的风和水汽：季风有多强、湿空气从哪里来', 'Low-level wind and moisture: how strong the monsoon is and where moist air comes from', 'Angin dan lembapan aras rendah: kekuatan monsun dan dari mana udara lembap datang'),
  700: T('中低层的水汽：这一层干，雷雨云比较难长高', 'Moisture in the lower-middle air: if it is dry, storm clouds struggle to grow', 'Lembapan udara tengah bawah: jika kering, awan ribut sukar tumbuh tinggi'),
  500: T('大约一半空气在下面；天气系统的移动方向主要跟着这一层的风', 'About half the air lies below; weather systems are mostly steered by the wind here', 'Kira-kira separuh udara di bawah; sistem cuaca kebanyakannya dipandu angin di sini'),
  250: T('急流所在的高度，也接近飞机巡航的高度；雷雨云的顶部在这附近摊开', 'Where the jet streams blow and airliners cruise; storm tops spread out near here', 'Tempat aliran jet bertiup dan pesawat terbang; puncak ribut merebak di sekitar sini'),
};

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const data = await loadData('series/kl-levels-2026');
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(clamp(W * 0.9, 280, 420));
  const M = { t: 30, b: 16, l: 40 };
  const y = scale(0, 12000, H - M.b, M.t);
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const ax = s('g', { class: 'chart-axes' });
  for (let k = 0; k <= 12; k += 2) ax.append(s('text', { x: M.l - 6, y: y(k * 1000) + 4, 'text-anchor': 'end' }, String(k)));
  ax.append(s('text', { x: M.l - 6, y: M.t - 14, 'text-anchor': 'end', class: 'unit' }, 'km'));
  ax.append(s('rect', { x: M.l, y: y(1500) , width: W - M.l - 8, height: y(0) - y(1500), class: 'band-0' }));
  svg.append(ax, s('line', { x1: M.l, x2: W - 8, y1: y(0), y2: y(0), class: 'gauge-ground' }));
  const rows = readout([['height', p(L.height)], ['temp', p(L.temp)], ['use', p(L.use)]]);
  const groups = [];
  for (const [lv, z, t] of data.rows) {
    const yy = y(z);
    const g = s('g', { class: 'level', tabindex: '0', role: 'button', 'aria-label': `${lv} hPa` },
      s('line', { x1: M.l, x2: W - 8, y1: yy, y2: yy }),
      s('text', { x: M.l + 8, y: yy - 6, class: 'level-label' }, `${lv} hPa`),
      s('text', { x: W - 12, y: yy - 6, 'text-anchor': 'end', class: 'level-sub' }, `≈ ${fmt(z / 1000, 1)} km`));
    const choose = () => {
      for (const n of groups) n.classList.remove('is-on');
      g.classList.add('is-on');
      rows.set('height', `${fmt(z, 0)} m`); rows.set('temp', `${fmt(t, 1)} °C`); rows.set('use', p(USE[lv]));
    };
    g.addEventListener('click', choose);
    g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); choose(); } });
    groups.push(g); svg.append(g);
  }
  el.append(frame({ title: p(L.title), lang, source: data.source, children: [svg, rows] }));
  groups[2].dispatchEvent(new Event('click'));
  return { destroy() { el.replaceChildren(); } };
}
