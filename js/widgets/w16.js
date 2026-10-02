/* W16 — One scene, three satellite images. Visible shows reflected
   sunlight: thick cloud is bright whatever its height, and night is
   black. Infrared shows temperature: cold, high tops white, warm low
   cloud grey. Water vapour shows moisture in the middle and upper air:
   moist bright, dry dark; low cloud does not show. Ahrens pp. 251–253.
   Schematic. */

import { s, h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('同一片天空，三种卫星图像', 'One sky, three satellite images', 'Satu langit, tiga imej satelit'),
  vis: T('可见光', 'Visible', 'Cahaya nampak'), ir: T('红外线', 'Infrared', 'Inframerah'), wv: T('水汽', 'Water vapour', 'Wap air'),
  night: T('夜间', 'Night', 'Malam'),
  labels: { cb: T('雷雨云', 'Thunderstorm', 'Ribut petir'), cu: T('低积云', 'Low cumulus', 'Kumulus rendah'), ci: T('薄卷云', 'Thin cirrus', 'Sirus nipis'), dry: T('高空干空气', 'Dry air aloft', 'Udara kering di atas') },
  text: {
    vis: T('可见光看的是反射的太阳光：厚云亮，薄云暗；高云和低云差不多亮，分不出高低。晚上没有阳光，整张图是黑的。', 'Visible shows reflected sunlight: thick cloud bright, thin cloud dim; high and low cloud look equally bright, so height cannot be told. At night there is no sunlight and the image is black.', 'Cahaya nampak menunjukkan cahaya matahari yang dipantulkan: awan tebal terang, awan nipis malap; awan tinggi dan rendah sama terang, jadi ketinggian tidak dapat dibezakan. Pada waktu malam tiada cahaya matahari dan imej menjadi hitam.'),
    ir: T('红外线看的是温度，白天晚上都能用：云顶越高越冷，显示越白；低云比较暖，是灰色；海面最暖，最暗。', 'Infrared shows temperature and works day and night: the higher a cloud top, the colder and whiter it shows; low cloud is warmer and grey; the sea is warmest and darkest.', 'Inframerah menunjukkan suhu dan berfungsi siang dan malam: semakin tinggi puncak awan, semakin sejuk dan putih; awan rendah lebih panas dan kelabu; laut paling panas dan paling gelap.'),
    wv: T('水汽图看的是中、高层空气里的水汽：潮湿的地方亮，干燥的地方暗；低云在这张图上几乎看不到。', 'Water vapour shows moisture in the middle and upper air: moist areas bright, dry areas dark; low cloud hardly shows at all.', 'Wap air menunjukkan lembapan di udara tengah dan atas: kawasan lembap terang, kawasan kering gelap; awan rendah hampir tidak kelihatan.'),
  },
};
// Grey level (0 black … 1 white) of each feature in each image.
const LOOK = {
  vis: { bg: 0.12, cb: 0.97, cu: 0.85, ci: 0.4, dry: 0.12 },
  ir: { bg: 0.18, cb: 1, cu: 0.5, ci: 0.82, dry: 0.18 },
  wv: { bg: 0.5, cb: 0.95, cu: 0.5, ci: 0.75, dry: 0.12 },
};

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.56);
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const tabs = h('div', { class: 'stage-chips' }), out = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  const grey = g => { const v = Math.round(g * 255); return `rgb(${v},${v},${v})`; };
  function draw(kind, night) {
    const lk = LOOK[kind], dark = kind === 'vis' && night;
    const f = k => grey(dark ? 0.03 : lk[k]);
    const lbl = (x, y, k) => s('text', { x, y, 'text-anchor': 'middle', class: 'sat-label', style: `fill: ${(dark ? 0.03 : lk[k]) > 0.55 ? '#111' : '#eee'}` }, p(L.labels[k]));
    svg.replaceChildren(
      s('rect', { x: 0, y: 0, width: W, height: H, style: `fill: ${f('bg')}` }),
      s('ellipse', { cx: W * 0.78, cy: H * 0.32, rx: W * 0.17, ry: H * 0.2, style: `fill: ${f('dry')}` }),
      s('path', { d: `M${W * 0.05},${H * 0.75} C${W * 0.25},${H * 0.55} ${W * 0.45},${H * 0.62} ${W * 0.6},${H * 0.5} L${W * 0.62},${H * 0.58} C${W * 0.45},${H * 0.72} ${W * 0.25},${H * 0.68} ${W * 0.07},${H * 0.85} Z`, style: `fill: ${f('ci')}` }),
      ...[[0.18, 0.3], [0.27, 0.36], [0.22, 0.42], [0.33, 0.28]].map(([x, y]) => s('circle', { cx: W * x, cy: H * y, r: W * 0.035, style: `fill: ${f('cu')}` })),
      s('circle', { cx: W * 0.5, cy: H * 0.3, r: W * 0.09, style: `fill: ${f('cb')}` }),
      lbl(W * 0.5, H * 0.31, 'cb'), lbl(W * 0.25, H * 0.53, 'cu'), lbl(W * 0.3, H * 0.8, 'ci'), lbl(W * 0.78, H * 0.33, 'dry'),
    );
    out.textContent = p(L.text[kind]);
    tabs.replaceChildren(...['vis', 'ir', 'wv'].map(k => { const b = h('button', { type: 'button', class: `chip${k === kind && !(k === 'vis' && night) ? ' is-on' : ''}` }, p(L[k])); b.addEventListener('click', () => draw(k, false)); return b; }),
      (() => { const b = h('button', { type: 'button', class: `chip${night ? ' is-on' : ''}` }, `${p(L.vis)} · ${p(L.night)}`); b.addEventListener('click', () => draw('vis', true)); return b; })());
  }
  draw('ir', false);
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 251–253', children: [tabs, svg, out] }));
  return { destroy() { el.replaceChildren(); } };
}
