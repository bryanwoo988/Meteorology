/* W18 — A Skew-T on a real morning sounding: KLIA Sepang, 8 am
   (00 UTC) 30 Sep 2026 (data/series/klia-sounding-2026-09-30.json).
   Temperature lines lean 45°; pressure falls logarithmically upwards.
   Slide the afternoon surface temperature: the sun heats the ground and
   mixes the bottom layer along a dry adiabat until it meets the morning
   profile, and the parcel from the surface then shows its LCL, CAPE and
   CIN. Physics: physics.js (parcelProfile, lclHeight, cape, cin). */

import { loadData } from '../content.js';
import { parcelProfile, lclHeight, cape, cin } from '../physics.js';
import { s, h, clamp, slider, readout, frame, fmt } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('Skew-T：早上 8 点的探空，推算下午', 'Skew-T: the 8 am sounding, and the afternoon', 'Skew-T: sonde jam 8 pagi, dan petang'),
  t: T('下午地面气温', 'Afternoon surface temperature', 'Suhu permukaan petang'), td: T('地面露点', 'Surface dew point', 'Takat embun permukaan'),
  env: T('气温（探空）', 'Temperature (sounding)', 'Suhu (sonde)'), dew: T('露点（探空）', 'Dew point (sounding)', 'Takat embun (sonde)'), parcel: T('地面气块', 'Surface parcel', 'Bungkusan permukaan'),
  lcl: T('云底（LCL）', 'Cloud base (LCL)', 'Dasar awan (LCL)'), cape: T('CAPE', 'CAPE', 'CAPE'), cin: T('CIN', 'CIN', 'CIN'),
  big: T('能量充足：午后很可能长出雷雨云', 'Plenty of energy: afternoon thunderstorms are likely', 'Tenaga mencukupi: ribut petir petang berkemungkinan'),
  push: T('有能量，但要先推开底下的“盖子”（CIN）', 'Energy is there, but the lid (CIN) must be pushed through first', 'Tenaga ada, tetapi ‘penutup’ (CIN) perlu ditembusi dahulu'),
  none: T('几乎没有对流能量：不太会有雷雨', 'Hardly any convective energy: storms unlikely', 'Hampir tiada tenaga perolakan: ribut tidak mungkin'),
  temp: T('温度 °C', 'Temperature °C', 'Suhu °C'),
};
const P0 = 1010, PTOP = 150;

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const snd = await loadData('series/klia-sounding-2026-09-30');
  const obs = snd.rows.map(([pr, z, t, td]) => ({ p: pr, z, t, td }));
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 620)), H = Math.round(clamp(W * 1.05, 300, 560));
  const M = { t: 14, r: 10, b: 30, l: 34 };
  const Y = pr => H - M.b - (H - M.t - M.b) * Math.log(P0 / pr) / Math.log(P0 / PTOP);
  const sx = (W - M.l - M.r) / 50;                                       // px per °C along the bottom
  const X = (t, pr) => M.l + (t + 10) * sx + (H - M.b - Y(pr));         // isotherms lean 45°
  const line = pts => pts.map(([t, pr], i) => `${i ? 'L' : 'M'}${X(t, pr).toFixed(1)},${Y(pr).toFixed(1)}`).join('');
  const interp = (pr, key) => {                                         // log-p interpolation in the sounding
    for (let i = 1; i < obs.length; i++) if (obs[i].p <= pr) {
      const a = obs[i - 1], b = obs[i], f = Math.log(a.p / pr) / Math.log(a.p / b.p);
      return a[key] + (b[key] - a[key]) * f;
    }
    return obs[obs.length - 1][key];
  };
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const defs = s('clipPath', { id: 'skewt-clip' }, s('rect', { x: M.l, y: M.t, width: W - M.l - M.r, height: H - M.t - M.b }));
  const bg = s('g', { 'clip-path': 'url(#skewt-clip)' });
  for (let t = -100; t <= 40; t += 10) bg.append(s('path', { d: line([[t, P0], [t, PTOP]]), class: t === 0 ? 'skewt-iso is-zero' : 'skewt-iso' }));
  for (let th = -20; th <= 100; th += 20) {                             // dry adiabats, labelled by their 1000 hPa temperature
    const pts = []; for (let pr = P0; pr >= PTOP; pr -= 20) pts.push([(th + 273.15) * (pr / 1000) ** 0.2857 - 273.15, pr]);
    bg.append(s('path', { d: line(pts), class: 'skewt-dry' }));
  }
  for (const t0 of [16, 20, 24, 28]) bg.append(s('path', { d: line(parcelProfile(t0, t0, 1000, PTOP, 10).map(q => [q.t, q.p])), class: 'skewt-moist' }));
  const axes = s('g', { class: 'chart-axes' });
  for (const pr of [1000, 850, 700, 500, 300, 200]) { axes.append(s('line', { x1: M.l, x2: W - M.r, y1: Y(pr), y2: Y(pr), class: 'grid' })); axes.append(s('text', { x: M.l - 4, y: Y(pr) + 4, 'text-anchor': 'end' }, String(pr))); }
  for (let t = -10; t <= 40; t += 10) axes.append(s('text', { x: X(t, P0), y: H - M.b + 14, 'text-anchor': 'middle' }, String(t)));
  axes.append(s('text', { x: M.l - 4, y: M.t - 2, 'text-anchor': 'end', class: 'unit' }, 'hPa'));
  axes.append(s('text', { x: (M.l + W - M.r) / 2, y: H - 2, 'text-anchor': 'middle', class: 'unit' }, p(L.temp)));
  const shade = s('g', { 'clip-path': 'url(#skewt-clip)' });
  const envP = s('path', { class: 'series', style: 'stroke: var(--mercury)', 'clip-path': 'url(#skewt-clip)' });
  const dewP = s('path', { class: 'series', style: 'stroke: var(--leaf)', 'clip-path': 'url(#skewt-clip)' });
  const parP = s('path', { class: 'series', style: 'stroke: var(--ink-2); stroke-dasharray: 5 4', 'clip-path': 'url(#skewt-clip)' });
  const lclL = s('line', { class: 'w-guide' }), lclT = s('text', { class: 'w-td-label', 'text-anchor': 'end' });
  svg.append(s('defs', {}, defs), bg, axes, shade, envP, dewP, parP, lclL, lclT);

  const surf = obs[0];
  let Ts = 31, Td = surf.td;
  const legend = h('ul', { class: 'chart-legend' },
    h('li', {}, h('span', { class: 'swatch', style: '--c: var(--mercury)' }), p(L.env)),
    h('li', {}, h('span', { class: 'swatch', style: '--c: var(--leaf)' }), p(L.dew)),
    h('li', {}, h('span', { class: 'swatch is-dashed', style: '--c: var(--ink-2)' }), p(L.parcel)));
  const rows = readout([['lcl', p(L.lcl)], ['cape', p(L.cape)], ['cin', p(L.cin)]]);
  const verdict = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  const tS = slider({ label: p(L.t), min: surf.t, max: 35, step: 0.5, value: Ts, unit: ' °C', onInput: v => { Ts = v; if (Td > Ts) { Td = Ts; tdS.set(Td); } update(); } });
  const tdS = slider({ label: p(L.td), min: 14, max: 26, step: 0.5, value: Td, unit: ' °C', onInput: v => { Td = Math.min(v, Ts); update(); } });

  function update() {
    // The sun mixes the bottom layer: a dry adiabat from the new surface temperature until it meets the morning sounding.
    const theta = (Ts + 273.15) * (1000 / surf.p) ** 0.2857;
    const envAt = pr => Math.max(interp(pr, 't'), theta * (pr / 1000) ** 0.2857 - 273.15);
    const parcel = parcelProfile(Ts, Td, surf.p, PTOP, 10);
    const env = parcel.map(q => ({ p: q.p, t: envAt(q.p) }));
    envP.setAttribute('d', line(env.map(q => [q.t, q.p])));
    dewP.setAttribute('d', line([[Td, surf.p], ...obs.slice(1).map(o => [o.td, o.p])]));
    parP.setAttribute('d', line(parcel.map(q => [q.t, q.p])));
    shade.replaceChildren();
    for (let i = 1; i < parcel.length; i++) {
      const a = parcel[i - 1], b = parcel[i], ea = env[i - 1], eb = env[i];
      shade.append(s('path', { d: `M${X(ea.t, ea.p)},${Y(ea.p)}L${X(a.t, a.p)},${Y(a.p)}L${X(b.t, b.p)},${Y(b.p)}L${X(eb.t, eb.p)},${Y(eb.p)}Z`, class: b.t > eb.t ? 'shade-warm' : 'shade-cold' }));
    }
    const lclM = lclHeight(Ts, Td), c = cape(env, parcel), n = cin(env, parcel);
    let pl = surf.p; for (const o of obs) if (o.z - surf.z <= lclM) pl = o.p;
    lclL.setAttribute('x1', M.l); lclL.setAttribute('x2', W - M.r); lclL.setAttribute('y1', Y(pl)); lclL.setAttribute('y2', Y(pl));
    lclT.setAttribute('x', W - M.r - 4); lclT.setAttribute('y', Y(pl) - 5); lclT.textContent = p(L.lcl);
    rows.set('lcl', `${fmt(lclM, 0)} m`); rows.set('cape', `${fmt(c, 0)} J/kg`); rows.set('cin', c < 1 ? '—' : `${fmt(n, 0)} J/kg`);
    verdict.textContent = c < 100 ? p(L.none) : n > 25 ? p(L.push) : p(L.big);
  }
  el.append(frame({ title: p(L.title), lang, source: 'Radiosonde KLIA Sepang (WMO 48650), 00 UTC 30 Sep 2026, University of Wyoming archive; physics.js', children: [legend, svg, h('div', { class: 'w-controls' }, tS, tdS), rows, verdict] }));
  update();
  return { destroy() { el.replaceChildren(); } };
}
