/* W6 — The ten cloud types, drawn at their usual heights in the tropics.
   Tap one to read about it. Heights: Ahrens Table 4.3 (tropical region)
   and Mote & Sahu (vertical clouds to about 16 km). Schematic drawing. */

import { s, h, scale, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('十种云：点一种看看', 'The ten cloud types: tap one', 'Sepuluh jenis awan: ketik satu'),
  high: T('高云', 'High', 'Tinggi'), middle: T('中云', 'Middle', 'Sederhana'), low: T('低云', 'Low', 'Rendah'),
  hint: T('点一朵云，看它的名字、高度和会不会下雨。', 'Tap a cloud for its name, height and whether it rains.', 'Ketik awan untuk nama, ketinggian dan sama ada ia menurunkan hujan.'),
};
// [abbr, name, x (0–1), base km, top km, shape, description]
const CLOUDS = [
  ['Ci', T('卷云', 'Cirrus', 'Sirus'), 0.10, 10.5, 11, 'wisp', T('高云。细丝状，全是冰晶，不下雨。', 'High. Thin wisps made entirely of ice crystals; no rain.', 'Tinggi. Jalur halus daripada hablur ais sepenuhnya; tiada hujan.')],
  ['Cs', T('卷层云', 'Cirrostratus', 'Sirostratus'), 0.42, 9.2, 9.6, 'sheet', T('高云。薄薄一层白纱，常在太阳或月亮周围形成日晕、月晕。', 'High. A thin milky veil, often making a halo round the Sun or Moon.', 'Tinggi. Selaput nipis seperti susu, sering membentuk halo di sekeliling Matahari atau Bulan.')],
  ['Cc', T('卷积云', 'Cirrocumulus', 'Sirokumulus'), 0.62, 8.2, 8.6, 'dots', T('高云。一排排细小的白色云块，像鱼鳞。', 'High. Rows of tiny white puffs, like fish scales.', 'Tinggi. Barisan gumpalan putih kecil, seperti sisik ikan.')],
  ['As', T('高层云', 'Altostratus', 'Altostratus'), 0.26, 5.2, 5.8, 'sheet', T('中云。灰色一大片，透过它太阳看起来朦朦胧胧。', 'Middle. A grey sheet through which the Sun looks dim and watery.', 'Sederhana. Lapisan kelabu yang menjadikan Matahari kelihatan malap.')],
  ['Ac', T('高积云', 'Altocumulus', 'Altokumulus'), 0.52, 4.0, 4.6, 'puffs', T('中云。灰白色的团块，一片片排列。', 'Middle. Grey-white patches arranged in rows or sheets.', 'Sederhana. Tompok putih kelabu tersusun dalam barisan atau lapisan.')],
  ['Ns', T('雨层云', 'Nimbostratus', 'Nimbostratus'), 0.24, 0.6, 3.4, 'thick', T('低到中层。又厚又暗，带来持续的雨。', 'Low to middle. Thick and dark; brings steady, prolonged rain.', 'Rendah hingga sederhana. Tebal dan gelap; membawa hujan berterusan.')],
  ['Sc', T('层积云', 'Stratocumulus', 'Stratokumulus'), 0.60, 1.4, 1.9, 'lumpy', T('低云。灰色的团块连成一片，很少下大雨。', 'Low. Lumpy grey layer; seldom more than light rain.', 'Rendah. Lapisan kelabu berketul; jarang lebih daripada hujan renyai.')],
  ['St', T('层云', 'Stratus', 'Stratus'), 0.40, 0.3, 0.7, 'sheet', T('低云。灰色、底部平整，像离地的雾；最多下毛毛雨。', 'Low. Grey with a flat base, like fog off the ground; drizzle at most.', 'Rendah. Kelabu dengan dasar rata, seperti kabus di atas tanah; paling banyak gerimis.')],
  ['Cu', T('积云', 'Cumulus', 'Kumulus'), 0.38, 0.8, 2.2, 'cumulus', T('直展云。底平、顶像棉花；小的是晴天积云，长高后会下阵雨。', 'Vertical. Flat base, cotton-wool top; small ones mean fair weather, tall ones give showers.', 'Menegak. Dasar rata, puncak seperti kapas; yang kecil bermaksud cuaca baik, yang tinggi membawa hujan lebat sekejap.')],
  ['Cb', T('积雨云', 'Cumulonimbus', 'Kumulonimbus'), 0.82, 0.8, 15, 'cb', T('直展云。雷雨云，可以长到对流层顶，顶部摊开像铁砧；带来暴雨、雷电、强风，有时冰雹。', 'Vertical. The thundercloud: grows to the tropopause and spreads into an anvil; brings downpours, lightning, gusts, sometimes hail.', 'Menegak. Awan ribut petir: tumbuh hingga tropopaus dan merebak seperti andas; membawa hujan lebat, kilat, angin kencang, kadangkala hujan batu.')],
];

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(clamp(W * 1.0, 300, 480));
  const M = { t: 30, r: 8, b: 14, l: 34 };
  const x = f => M.l + f * (W - M.l - M.r), y = scale(0, 16, H - M.b, M.t);
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg w-clouds', role: 'img', 'aria-label': p(L.title) });
  const ax = s('g', { class: 'chart-axes' });
  for (let k = 0; k <= 16; k += 2) ax.append(s('text', { x: M.l - 6, y: y(k) + 4, 'text-anchor': 'end' }, String(k)));
  ax.append(s('text', { x: M.l - 6, y: M.t - 10, 'text-anchor': 'end', class: 'unit' }, 'km'));
  for (const [lo, hi, k] of [[6, 16, 'high'], [2, 6, 'middle'], [0, 2, 'low']]) {
    ax.append(s('rect', { x: M.l, y: y(hi), width: W - M.l - M.r, height: y(lo) - y(hi), class: k === 'middle' ? 'band-0' : 'band-1' }));
    ax.append(s('text', { x: M.l + 4, y: y(hi) + 13, class: 'band-label' }, p(L[k])));
  }
  svg.append(ax);
  const caption = h('p', { class: 'w-explain', 'aria-live': 'polite' }, p(L.hint));
  const sz = W / 640;

  for (const [abbr, name, fx, base, top, shape, text] of CLOUDS) {
    const cx = x(fx), yb = y(base), yt = y(top), g = s('g', { class: 'cloud', tabindex: '0', role: 'button', 'aria-label': `${p(name)} ${abbr}` });
    const w = 90 * sz;
    if (shape === 'wisp') for (let i = 0; i < 4; i++) g.append(s('path', { d: `M${cx - w / 2 + i * 10},${yb + i * 3} q${w * .4},-12 ${w * .8},-4`, class: 'cl-ice' }));
    else if (shape === 'sheet') g.append(s('rect', { x: cx - w * .8, y: yt, width: w * 1.6, height: Math.max(6, yb - yt), rx: 4, class: abbr === 'As' || abbr === 'St' ? 'cl-grey' : 'cl-ice' }));
    else if (shape === 'dots') for (let i = 0; i < 9; i++) g.append(s('circle', { cx: cx - w * .6 + (i % 5) * w * .3, cy: yt + Math.floor(i / 5) * 8, r: 4, class: 'cl-ice' }));
    else if (shape === 'puffs') for (let i = 0; i < 5; i++) g.append(s('ellipse', { cx: cx - w * .6 + i * w * .3, cy: (yt + yb) / 2, rx: w * .14, ry: 8, class: 'cl-white' }));
    else if (shape === 'lumpy') for (let i = 0; i < 5; i++) g.append(s('ellipse', { cx: cx - w * .55 + i * w * .28, cy: (yt + yb) / 2, rx: w * .18, ry: 10, class: 'cl-grey' }));
    else if (shape === 'thick') { g.append(s('rect', { x: cx - w * .7, y: yt, width: w * 1.4, height: yb - yt, rx: 8, class: 'cl-dark' })); for (let i = 0; i < 6; i++) g.append(s('line', { x1: cx - w * .55 + i * w * .22, x2: cx - w * .62 + i * w * .22, y1: yb + 3, y2: y(0) - 2, class: 'cl-rain' })); }
    else if (shape === 'cumulus') { g.append(s('path', { d: `M${cx - w * .5},${yb} q0,-${(yb - yt) * .6} ${w * .25},-${(yb - yt) * .7} q${w * .1},-${(yb - yt) * .4} ${w * .3},-${(yb - yt) * .2} q${w * .25},${(yb - yt) * .1} ${w * .2},${(yb - yt) * .5} q${w * .1},0 ${w * .25},${(yb - yt) * .4}Z`, class: 'cl-white' })); }
    else if (shape === 'cb') {
      // Tower narrowing upward, then an anvil spreading along the tropopause.
      const body = w * .32, anvil = w * .78;
      g.append(s('path', { d: `M${cx - body},${yb} C${cx - body * 1.1},${y(6)} ${cx - body * .7},${y(11)} ${cx - body * .55},${y(12.5)} L${cx - anvil * .55},${yt + 10} Q${cx},${yt - 6} ${cx + anvil},${yt + 6} L${cx + body * .6},${y(12.5)} C${cx + body * .8},${y(11)} ${cx + body * 1.1},${y(6)} ${cx + body},${yb} Z`, class: 'cl-dark' }));
      for (let i = 0; i < 5; i++) g.append(s('line', { x1: cx - body * .8 + i * body * .4, x2: cx - body * .9 + i * body * .4, y1: yb + 3, y2: y(0) - 2, class: 'cl-rain' }));
    }
    const ly = shape === 'cb' ? y(7) : shape === 'thick' ? y(2) : (yt + yb) / 2 + 4;
    g.append(s('text', { x: cx, y: ly, 'text-anchor': 'middle', class: 'cl-label' }, abbr));
    const choose = () => {
      for (const n of svg.querySelectorAll('.cloud')) n.classList.remove('is-on');
      g.classList.add('is-on');
      caption.textContent = `${p(name)} (${abbr}) — ${p(text)}`;
    };
    g.addEventListener('click', choose);
    g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); choose(); } });
    svg.append(g);
  }
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, Table 4.3 (tropical heights); Mote & Sahu', children: [svg, caption] }));
  return { destroy() { el.replaceChildren(); } };
}
