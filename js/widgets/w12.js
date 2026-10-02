/* W12 — The Walker circulation in three states: La Niña, neutral, El Niño.
   A cross-section along the equatorial Pacific from Malaysia to South
   America. Ahrens pp. 204–206; drawn schematically. */

import { s, h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('赤道太平洋的剖面：切换三种状态', 'A slice along the equatorial Pacific: switch states', 'Keratan sepanjang Pasifik khatulistiwa: tukar keadaan'),
  lanina: T('拉尼娜', 'La Niña', 'La Niña'), neutral: T('正常', 'Neutral', 'Neutral'), elnino: T('厄尔尼诺', 'El Niño', 'El Niño'),
  west: T('马来西亚、印尼', 'Malaysia, Indonesia', 'Malaysia, Indonesia'), east: T('秘鲁、厄瓜多尔', 'Peru, Ecuador', 'Peru, Ecuador'),
  warm: T('暖水', 'Warm water', 'Air panas'),
  text: {
    lanina: T('信风特别强，暖水被推得更集中在西边；东南亚上空空气上升更旺盛，云更多、雨更大。东太平洋更冷更干。', 'The trades are extra strong and pile warm water further west; air rises more vigorously over South-East Asia, with more cloud and heavier rain. The eastern Pacific is colder and drier.', 'Angin pasat sangat kuat dan mengumpul air panas lebih jauh ke barat; udara naik lebih kuat di atas Asia Tenggara, dengan lebih banyak awan dan hujan lebih lebat. Pasifik timur lebih sejuk dan kering.'),
    neutral: T('信风把暖水推向西太平洋：西边空气上升、多雨；东边冷水上涌、空气下沉、干燥。', 'The trades push warm water to the western Pacific: rising air and rain in the west; cold upwelling, sinking air and dry weather in the east.', 'Angin pasat menolak air panas ke Pasifik barat: udara naik dan hujan di barat; air sejuk naik, udara turun dan kering di timur.'),
    elnino: T('信风减弱甚至反向，暖水往东流；雨带跟着东移。东南亚上空空气反而下沉，常常偏干，强厄尔尼诺时印尼一带容易干旱。', 'The trades weaken or even reverse and warm water flows east; the rain moves east with it. Over South-East Asia the air tends to sink instead, often bringing drier weather; strong El Niños bring drought to Indonesia.', 'Angin pasat melemah atau berbalik dan air panas mengalir ke timur; hujan bergerak ke timur bersamanya. Di atas Asia Tenggara udara cenderung turun, sering membawa cuaca lebih kering; El Niño kuat membawa kemarau ke Indonesia.'),
  },
};

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.6);
  const sea = H * 0.62;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg', role: 'img', 'aria-label': p(L.title) });
  const caption = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  const tabs = h('div', { class: 'stage-chips' });
  function draw(state) {
    const centre = { lanina: 0.18, neutral: 0.25, elnino: 0.6 }[state];   // where the rising branch sits (fraction across)
    const warmTo = { lanina: 0.4, neutral: 0.5, elnino: 0.85 }[state];
    const loop = (x0, x1, up) => s('path', { d: `M${W * x0},${sea - 12} C${W * x0},${H * 0.12} ${W * x1},${H * 0.12} ${W * x1},${sea - 12}`, class: 'walker-loop', 'marker-end': 'url(#walk-ah)' });
    svg.replaceChildren(
      s('defs', {}, s('marker', { id: 'walk-ah', viewBox: '0 0 10 10', refX: 8, refY: 5, markerWidth: 6, markerHeight: 6, orient: 'auto-start-reverse' }, s('path', { d: 'M0,0 L10,5 L0,10 Z', style: 'fill: var(--ink-2)' }))),
      s('rect', { x: 0, y: sea, width: W, height: H - sea, class: 'walker-sea' }),
      s('path', { d: `M0,${sea} L${W * warmTo},${sea} L${W * warmTo - 20},${sea + (H - sea) * 0.55} L0,${sea + (H - sea) * 0.7} Z`, class: 'walker-warm' }),
      s('text', { x: 8, y: sea + 18, class: 'force-label' }, p(L.warm)),
      s('rect', { x: 0, y: sea - 18, width: W * 0.08, height: 18, class: 'walker-land' }), s('rect', { x: W * 0.92, y: sea - 22, width: W * 0.08, height: 22, class: 'walker-land' }),
      s('text', { x: 4, y: H - 6, class: 'band-label' }, p(L.west)), s('text', { x: W - 4, y: H - 6, 'text-anchor': 'end', class: 'band-label' }, p(L.east)),
      loop(centre + 0.08, 0.85, true),
      s('ellipse', { cx: W * centre, cy: H * 0.3, rx: W * 0.09, ry: H * 0.14, class: 'cl-dark' }),
      ...[0, 1, 2, 3].map(i => s('line', { x1: W * (centre - 0.05 + i * 0.033), x2: W * (centre - 0.06 + i * 0.033), y1: H * 0.44, y2: sea - 4, class: 'cl-rain' })),
    );
    caption.textContent = p(L.text[state]);
    tabs.replaceChildren(...['lanina', 'neutral', 'elnino'].map(k => { const b = h('button', { type: 'button', class: `chip${k === state ? ' is-on' : ''}` }, p(L[k])); b.addEventListener('click', () => draw(k)); return b; }));
  }
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'Ahrens 2010, pp. 204–206; MetMalaysia (La Niña)', children: [tabs, svg, caption] }));
  draw('neutral');
  return { destroy() { el.replaceChildren(); } };
}
