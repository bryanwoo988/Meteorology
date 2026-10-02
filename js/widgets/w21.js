/* W21 — Chaos, live. 51 runs of the Lorenz-63 equations start from
   almost the same point (differences of 0.001); drag the time and watch
   them stay together, then fan out. A DEMONSTRATION of sensitive
   dependence on initial conditions — the three Lorenz equations are a toy,
   not a weather model. physics.lorenzEnsemble; Ahrens 2010, p. 256. */

import { lorenzEnsemble } from '../physics.js';
import { s, h, clamp, slider, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('混沌演示：51 条几乎一样的起点', 'Chaos demo: 51 almost identical starts', 'Demo kekacauan: 51 titik mula yang hampir sama'),
  time: T('时间', 'Time', 'Masa'), spread: T('离散度（最大减最小）', 'Spread (highest minus lowest)', 'Serakan (tertinggi tolak terendah)'),
  demo: T('这是 Lorenz 方程的演示，不是天气模型；它只说明一个道理：起点差一点点，后来就差很远。', 'This is the Lorenz equations, not a weather model; it shows one idea only: a tiny difference at the start grows into a large one.', 'Ini persamaan Lorenz, bukan model cuaca; ia menunjukkan satu idea sahaja: perbezaan kecil di permulaan menjadi besar.'),
  ctl: T('control（没有扰动的那一条）', 'Control (the unperturbed run)', 'Kawalan (larian tanpa gangguan)'),
};
const STEPS = 2500;

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const runs = lorenzEnsemble(51, STEPS, 1e-3, 2026);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.56);
  const M = { l: 8, r: 8, t: 10, b: 10 };
  const X = k => M.l + (W - M.l - M.r) * k / (STEPS - 1), Y = v => M.t + (H - M.t - M.b) * (1 - (v + 22) / 44);
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const paths = runs.map((r, m) => s('path', { class: m === 0 ? 'ens-ctl' : 'ens-mem' }));
  const cursor = s('line', { y1: M.t, y2: H - M.b, class: 'w-guide' });
  svg.append(...paths.slice(1), paths[0], cursor);
  const rows = readout([['spread', p(L.spread)]]);
  let t = 900;
  const ts = slider({ label: p(L.time), min: 50, max: STEPS - 1, step: 10, value: t, onInput: v => { t = v; draw(); } });
  function draw() {
    runs.forEach((r, m) => {
      let d = ''; for (let k = 0; k <= t; k += 5) d += `${k ? 'L' : 'M'}${X(k).toFixed(1)},${Y(r[k]).toFixed(1)}`;
      paths[m].setAttribute('d', d);
    });
    cursor.setAttribute('x1', X(t)); cursor.setAttribute('x2', X(t));
    const vals = runs.map(r => r[t]);
    rows.set('spread', fmt(Math.max(...vals) - Math.min(...vals), 1));
  }
  draw();
  const legend = h('ul', { class: 'chart-legend' }, h('li', {}, h('span', { class: 'swatch', style: '--c: var(--ink)' }), p(L.ctl)));
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Lorenz (1963) equations computed live (physics.js); Ahrens 2010, p. 256', children: [legend, svg, h('div', { class: 'w-controls' }, ts), rows, h('p', { class: 'w-source' }, p(L.demo))] }));
  return { destroy() { el.replaceChildren(); } };
}
