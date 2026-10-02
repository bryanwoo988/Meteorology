/* W7 — A rising parcel of air. The parcel starts with the surface air's
   temperature and dew point, cools at the dry rate to its cloud base (LCL),
   then at the moist rate. Where it is warmer than the air around it (red)
   it rises by itself; where colder (blue) it must be pushed.
   Presets are Kuala Lumpur's 2025 averages at 6 am and 3 pm (ERA5). The
   environment above 1 km is an illustrative tropical profile, not a real
   sounding; below 1 km it follows the surface air. physics.js throughout. */

import { parcelProfile, pressureToHeight, lclHeight, cape, cin } from '../physics.js';
import { s, h, scale, clamp, slider, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('上升的气块：清晨与午后', 'A rising parcel of air: morning and afternoon', 'Bungkusan udara yang naik: pagi dan petang'),
  morning: T('清晨 6 点', '6 am', '6 pagi'), afternoon: T('下午 3 点', '3 pm', '3 petang'),
  t: T('地面气温', 'Surface temperature', 'Suhu permukaan'), td: T('地面露点', 'Surface dew point', 'Takat embun permukaan'),
  lcl: T('云底（LCL）', 'Cloud base (LCL)', 'Dasar awan (LCL)'), top: T('云顶约', 'Cloud top about', 'Puncak awan kira-kira'),
  cape: T('CAPE（上冲能量）', 'CAPE (lift energy)', 'CAPE (tenaga angkat)'), cin: T('CIN（要推的能量）', 'CIN (push needed)', 'CIN (tolakan diperlukan)'),
  env: T('周围空气（示意）', 'Surrounding air (illustrative)', 'Udara sekeliling (ilustrasi)'), parcel: T('气块', 'Parcel', 'Bungkusan'),
  verdictBig: T('午后对流旺盛：可以长成积雨云', 'Strong convection: can grow into a cumulonimbus', 'Perolakan kuat: boleh menjadi kumulonimbus'),
  verdictPush: T('要有东西把空气推上去（例如海风相撞），才会长云', 'Needs something to push the air up (such as colliding sea breezes)', 'Perlu sesuatu menolak udara ke atas (seperti bayu laut yang bertembung)'),
  verdictNone: T('空气太稳定，不会自己上升', 'Too stable: the air will not rise by itself', 'Terlalu stabil: udara tidak akan naik sendiri'),
  xaxis: T('温度 °C', 'Temperature °C', 'Suhu °C'),
  source: 'Presets: ERA5 via Open-Meteo (Kuala Lumpur 2025); parcel physics: physics.js',
};
const PRESETS = { morning: [24.2, 22.9], afternoon: [31.6, 22.2] };   // data/series/kl-humidity-2025.json, 06:00 and 15:00

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(clamp(W * 1.0, 300, 480));
  const M = { t: 34, r: 12, b: 34, l: 34 };
  const x = scale(-70, 40, M.l, W - M.r), y = scale(0, 16, H - M.b, M.t);
  const z0 = pressureToHeight(1000);
  const km = pr => (pressureToHeight(pr) - z0) / 1000;
  let Ts = PRESETS.afternoon[0], Td = PRESETS.afternoon[1];

  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const axes = s('g', { class: 'chart-axes' });
  for (let k = 0; k <= 16; k += 4) { axes.append(s('line', { x1: M.l, x2: W - M.r, y1: y(k), y2: y(k), class: 'grid' })); axes.append(s('text', { x: M.l - 6, y: y(k) + 4, 'text-anchor': 'end' }, String(k))); }
  for (const t of [-60, -40, -20, 0, 20, 40]) axes.append(s('text', { x: x(t), y: H - M.b + 16, 'text-anchor': 'middle' }, String(t)));
  axes.append(s('line', { x1: x(0), x2: x(0), y1: M.t, y2: H - M.b, class: 'grid', 'stroke-dasharray': '2 3' }));
  axes.append(s('text', { x: M.l - 6, y: M.t - 12, 'text-anchor': 'end', class: 'unit' }, 'km'));
  axes.append(s('text', { x: (M.l + W - M.r) / 2, y: H - 4, 'text-anchor': 'middle', class: 'unit' }, p(L.xaxis)));
  svg.append(axes);
  const shade = s('g'), envPath = s('path', { class: 'series', style: 'stroke: var(--ink-2); stroke-dasharray: 5 4' }), parcelPath = s('path', { class: 'series', style: 'stroke: var(--mercury)' });
  const lclLine = s('line', { class: 'w-guide' }), lclText = s('text', { class: 'w-td-label', 'text-anchor': 'end' });
  svg.append(shade, envPath, parcelPath, lclLine, lclText);

  const legend = h('ul', { class: 'chart-legend' },
    h('li', {}, h('span', { class: 'swatch is-dashed', style: '--c: var(--ink-2)' }), p(L.env)),
    h('li', {}, h('span', { class: 'swatch', style: '--c: var(--mercury)' }), p(L.parcel)));
  const rows = readout([['lcl', p(L.lcl)], ['top', p(L.top)], ['cape', p(L.cape)], ['cin', p(L.cin)]]);
  const verdict = h('p', { class: 'w-explain' });
  const tS = slider({ label: p(L.t), min: 20, max: 38, step: 0.5, value: Ts, unit: ' °C', onInput: v => { Ts = v; if (Td > Ts) { Td = Ts; tdS.set(Td); } update(); } });
  const tdS = slider({ label: p(L.td), min: 10, max: 30, step: 0.5, value: Td, unit: ' °C', onInput: v => { Td = Math.min(v, Ts); update(); } });
  const presets = h('div', { class: 'stage-chips' }, ['morning', 'afternoon'].map(k => {
    const b = h('button', { type: 'button', class: 'chip' }, `${p(L[k])} · ${PRESETS[k][0]}/${PRESETS[k][1]} °C`);
    b.addEventListener('click', () => { [Ts, Td] = PRESETS[k]; tS.set(Ts); tdS.set(Td); update(); });
    return b;
  }));

  function environment(levels) {
    // Above 1 km: 28 °C at sea level falling 6.5 °C/km. Below 1 km: blend from the surface air to that profile.
    return levels.map(pr => {
      const z = Math.min(km(pr), 16), aloft = 28 - 6.5 * z;
      return { p: pr, t: z >= 1 ? aloft : Ts + (28 - 6.5 - Ts) * z };
    });
  }
  function update() {
    const parcel = parcelProfile(Ts, Td, 1000, 100, 10);
    const env = environment(parcel.map(q => q.p));
    const path = arr => arr.map((q, i) => `${i ? 'L' : 'M'}${x(q.t).toFixed(1)},${y(km(q.p)).toFixed(1)}`).join('');
    envPath.setAttribute('d', path(env)); parcelPath.setAttribute('d', path(parcel));
    shade.replaceChildren();
    for (let i = 1; i < parcel.length; i++) {
      const a = parcel[i - 1], b = parcel[i], ea = env[i - 1], eb = env[i];
      const warm = b.t > eb.t;
      shade.append(s('path', { d: `M${x(ea.t)},${y(km(ea.p))}L${x(a.t)},${y(km(a.p))}L${x(b.t)},${y(km(b.p))}L${x(eb.t)},${y(km(eb.p))}Z`, class: warm ? 'shade-warm' : 'shade-cold' }));
    }
    const lcl = lclHeight(Ts, Td) / 1000, c = cape(env, parcel), n = cin(env, parcel);
    let topKm = null;
    for (let i = parcel.length - 1; i > 0; i--) if (parcel[i].t > env[i].t) { topKm = km(parcel[i].p); break; }
    lclLine.setAttribute('x1', M.l); lclLine.setAttribute('x2', W - M.r); lclLine.setAttribute('y1', y(lcl)); lclLine.setAttribute('y2', y(lcl));
    lclText.setAttribute('x', W - M.r - 4); lclText.setAttribute('y', y(lcl) - 5); lclText.textContent = p(L.lcl);
    rows.set('lcl', `${fmt(lcl * 1000, 0)} m`);
    rows.set('top', topKm === null || c < 1 ? '—' : `${fmt(topKm, 1)} km`);
    rows.set('cape', `${fmt(c, 0)} J/kg`);
    rows.set('cin', `${fmt(n, 0)} J/kg`);
    verdict.textContent = c < 50 ? p(L.verdictNone) : n > 10 ? p(L.verdictPush) : p(L.verdictBig);
  }
  el.append(frame({ title: p(L.title), lang, schematic: true, source: L.source, children: [presets, legend, svg, h('div', { class: 'w-controls' }, tS, tdS), rows, verdict] }));
  update();
  return { destroy() { el.replaceChildren(); } };
}
