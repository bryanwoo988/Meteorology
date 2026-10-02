/* W24 — A day of afternoon showers on Malaysia's west coast. Drag the
   hour from 6 am to 8 pm: the ground heats, thermals rise, the sea breeze
   pushes moist air inland, cumulus grows into a thunderstorm, it rains,
   and the sky clears in the evening. Schematic; sequence from Ahrens
   (thermals p. 32, sea breeze p. 182, tropical wet climate p. 352) and
   MetMalaysia (storms on land in the afternoon and at dusk). */

import { s, h, clamp, slider, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('午后阵雨的一天：拖动时间', 'A day of afternoon showers: drag the hour', 'Sehari hujan petang: seret jam'),
  hour: T('时间', 'Time', 'Masa'),
  sea: T('海', 'Sea', 'Laut'), land: T('陆地', 'Land', 'Darat'), breeze: T('海风', 'Sea breeze', 'Bayu laut'),
  step: [
    [6, T('清晨：天空晴朗，地面经过一夜已经冷下来，风很弱。', 'Early morning: a clear sky, the ground cooled overnight, light wind.', 'Awal pagi: langit cerah, tanah sejuk selepas malam, angin lemah.')],
    [9, T('上午：太阳把地面晒热，贴地的空气变暖、变轻，一团团热泡往上升。', 'Morning: the sun heats the ground; the air touching it warms, lightens and rises in bubbles called thermals.', 'Pagi: matahari memanaskan tanah; udara yang menyentuhnya menjadi panas, ringan dan naik dalam gelembung yang dipanggil terma.')],
    [11, T('近中午：热泡升到抬升凝结高度，水汽凝结，出现一朵朵小积云。', 'Late morning: thermals reach the lifting condensation level, the vapour condenses, and small cumulus appear.', 'Lewat pagi: terma mencapai aras pemeluwapan angkatan, wap memeluwap, dan kumulus kecil muncul.')],
    [13, T('中午过后：陆地比海暖得多，海风把海上潮湿的空气吹进内陆，和上升气流汇合。', 'Early afternoon: the land is now much warmer than the sea; the sea breeze pushes moist sea air inland, where it meets the rising air.', 'Awal petang: darat kini jauh lebih panas daripada laut; bayu laut menolak udara laut yang lembap ke pedalaman, bertemu udara yang naik.')],
    [15, T('下午：积云越长越高，变成积雨云，云顶摊开成砧状。', 'Afternoon: the cumulus towers higher and becomes a cumulonimbus, its top spreading into an anvil.', 'Petang: kumulus menjulang lebih tinggi menjadi kumulonimbus, puncaknya merebak menjadi bentuk andas.')],
    [17, T('傍晚前后：雷雨。大雨、闪电，下沉的冷空气让气温一下子降低。', 'Late afternoon to dusk: the thunderstorm. Heavy rain and lightning; the cold downdraught makes the temperature drop suddenly.', 'Lewat petang hingga senja: ribut petir. Hujan lebat dan kilat; aliran turun yang sejuk menurunkan suhu dengan tiba-tiba.')],
    [19, T('晚上：太阳下山，没有热泡补充，云慢慢散去，天空转晴。', 'Evening: after sunset no new thermals feed the storm; the cloud dies away and the sky clears.', 'Malam: selepas matahari terbenam tiada terma baharu; awan beransur hilang dan langit cerah.')],
  ],
};

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.62);
  const ground = H * 0.8, coast = W * 0.28;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const out = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  let hour = 15;
  const hs = slider({ label: p(L.hour), min: 6, max: 20, step: 1, value: hour, unit: ':00', onInput: v => { hour = v; draw(); } });
  function draw() {
    const day = clamp((hour - 6) / 12.5, 0, 1);                          // 6:00 → 0, 18:30 → 1
    const sunX = W * (0.05 + 0.9 * day), sunY = H * 0.62 - Math.sin(Math.PI * day) * H * 0.52;
    const up = hour >= 18.5 ? 0 : clamp((hour - 8) / 4, 0, 1);         // strength of heating
    const cloud = hour < 10 ? 0 : hour <= 16 ? clamp((hour - 10) / 6, 0, 1) : clamp(1 - (hour - 18) / 2, 0, 1);
    const raining = hour >= 16 && hour <= 18, breeze = hour >= 12 && hour <= 18;
    const cx = W * 0.62, base = H * 0.42, top = base - cloud * H * 0.34, cw = W * (0.08 + 0.12 * cloud);
    svg.replaceChildren(
      s('rect', { x: 0, y: ground, width: coast, height: H - ground, class: 'walker-sea' }),
      s('rect', { x: coast, y: ground, width: W - coast, height: H - ground, class: 'walker-land' }),
      s('text', { x: 6, y: H - 8, class: 'band-label' }, p(L.sea)), s('text', { x: W - 6, y: H - 8, 'text-anchor': 'end', class: 'band-label' }, p(L.land)),
      hour <= 18 ? s('circle', { cx: sunX, cy: sunY, r: 11, style: 'fill: var(--sun)' }) : null,
      ...(up > 0 ? [0.45, 0.62, 0.8].map((f, i) => s('path', { d: `M${W * f},${ground - 4} q-6,${-H * 0.08 * up} 0,${-H * 0.16 * up} q6,${-H * 0.06 * up} 0,${-H * 0.12 * up}`, class: 'walker-loop', style: `opacity:${0.35 + 0.5 * up}` })) : []),
      breeze ? s('g', {}, s('path', { d: `M${coast - W * 0.18},${ground - 14} L${coast + W * 0.14},${ground - 14}`, class: 'walker-loop', 'marker-end': 'url(#w24-ah)' }),
        s('text', { x: coast - W * 0.18, y: ground - 22, class: 'force-label' }, p(L.breeze))) : null,
      cloud > 0 ? s('ellipse', { cx, cy: (base + top) / 2, rx: cw, ry: (base - top) / 2 + 10, class: raining ? 'cl-dark' : 'cl-white' }) : null,
      cloud > 0.8 && hour <= 18 ? s('ellipse', { cx, cy: top, rx: cw * 1.8, ry: 9, class: raining ? 'cl-dark' : 'cl-white' }) : null,
      ...(raining ? [0, 1, 2, 3, 4].map(i => s('line', { x1: cx - cw * 0.7 + i * cw * 0.35, x2: cx - cw * 0.8 + i * cw * 0.35, y1: base + 8, y2: ground - 2, class: 'cl-rain' })) : []),
      s('defs', {}, s('marker', { id: 'w24-ah', viewBox: '0 0 10 10', refX: 8, refY: 5, markerWidth: 6, markerHeight: 6, orient: 'auto' }, s('path', { d: 'M0,0 L10,5 L0,10 Z', style: 'fill: var(--ink-2)' }))),
    );
    let text = L.step[0][1];
    for (const [hh, tx] of L.step) if (hour >= hh) text = tx;
    out.textContent = `${String(hour).padStart(2, '0')}:00 — ${p(text)}`;
  }
  draw();
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 32, 182, 352; MetMalaysia (weather phenomena)', children: [svg, h('div', { class: 'w-controls' }, hs), out] }));
  return { destroy() { el.replaceChildren(); } };
}
