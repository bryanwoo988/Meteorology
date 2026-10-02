/* W3 — The Earth's yearly energy budget, in units where 100 = all the
   sunlight arriving at the top of the atmosphere. Tap an arrow to read it;
   switch between sunlight (shortwave) and heat (longwave and the rest).
   Numbers: Ahrens, Essentials of Meteorology, pp. 44–45. Redrawn diagram. */

import { s, h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('地球一年的能量收支：点箭头', 'The Earth’s yearly energy budget: tap an arrow', 'Imbangan tenaga tahunan Bumi: ketik anak panah'),
  sw: T('阳光（短波）', 'Sunlight (shortwave)', 'Cahaya matahari (gelombang pendek)'),
  lw: T('热（长波和其他）', 'Heat (longwave and other)', 'Haba (gelombang panjang dan lain-lain)'),
  space: T('太空', 'Space', 'Angkasa'), atm: T('大气和云', 'Atmosphere and clouds', 'Atmosfera dan awan'), ground: T('地面', 'Surface', 'Permukaan'),
  hint: T('单位：到达大气顶端的阳光 = 100', 'Units: sunlight reaching the top of the atmosphere = 100', 'Unit: cahaya matahari di bahagian atas atmosfera = 100'),
};
const ARROWS = {
  sw: [
    { id: 'in', n: 100, from: [0.18, 0.04], to: [0.18, 0.40], color: 'sun', text: T('从太阳来的阳光，全部算作 100。', 'Sunlight arriving from the Sun: call it 100.', 'Cahaya matahari dari Matahari: anggap 100.') },
    { id: 'refl', n: 30, from: [0.30, 0.40], to: [0.30, 0.04], color: 'cloud-ink', text: T('30 被云、空气和地面反射或散射回太空：地球整体的反照率约 30 %。', '30 is reflected or scattered back to space by clouds, air and the surface: the Earth’s overall albedo is about 30 %.', '30 dipantul atau diserakkan kembali ke angkasa oleh awan, udara dan permukaan: albedo keseluruhan Bumi kira-kira 30 %.') },
    { id: 'abs', n: 19, from: [0.42, 0.30], to: [0.42, 0.52], color: 'sun', text: T('19 被大气和云吸收。', '19 is absorbed by the atmosphere and clouds.', '19 diserap oleh atmosfera dan awan.') },
    { id: 'surf', n: 51, from: [0.18, 0.52], to: [0.18, 0.90], color: 'sun', text: T('51 到达地面并被吸收（直接的和散射的阳光都有）。', '51 reaches the surface and is absorbed, both direct and scattered (diffuse) sunlight.', '51 sampai ke permukaan dan diserap, sama ada cahaya terus atau terserak.') },
  ],
  lw: [
    { id: 'lat', n: 23, from: [0.16, 0.90], to: [0.16, 0.56], color: 'rain', text: T('23 用来蒸发水：这些热量藏在水汽里，等水汽凝结成云时才放出来，叫潜热。', '23 goes into evaporating water. The heat travels hidden in the vapour and is released when it condenses into cloud: latent heat.', '23 digunakan untuk menyejatkan air. Haba itu tersembunyi dalam wap dan dilepaskan apabila ia terkondensasi menjadi awan: haba pendam.') },
    { id: 'sens', n: 7, from: [0.30, 0.90], to: [0.30, 0.56], color: 'mercury', text: T('7 通过传导和对流直接加热空气，叫感热。', '7 heats the air directly by conduction and convection: sensible heat.', '7 memanaskan udara secara terus melalui konduksi dan perolakan: haba deria.') },
    { id: 'up', n: 117, from: [0.50, 0.90], to: [0.50, 0.56], color: 'mercury', text: T('地面日夜不停向上发出 117 的红外线（比它收到的阳光还多），其中 111 被水汽、二氧化碳和云吸收。', 'The surface radiates 117 units of infrared upward, day and night — more than the sunlight it absorbs. 111 of it is absorbed by water vapour, CO₂ and clouds.', 'Permukaan memancarkan 117 unit inframerah ke atas, siang dan malam — lebih daripada cahaya matahari yang diserapnya. 111 daripadanya diserap oleh wap air, CO₂ dan awan.') },
    { id: 'win', n: 6, from: [0.62, 0.90], to: [0.62, 0.04], color: 'mercury', text: T('只有 6 直接穿过大气逃到太空（经过“大气窗口”）。', 'Only 6 passes straight through to space, through the ‘atmospheric window’.', 'Hanya 6 terus ke angkasa melalui ‘tingkap atmosfera’.') },
    { id: 'back', n: 96, from: [0.76, 0.56], to: [0.76, 0.90], color: 'leaf', text: T('大气把 96 的红外线送回地面：这就是温室效应。地面收到的大气红外线，几乎是收到阳光的两倍。', 'The atmosphere sends 96 units of infrared back down: the greenhouse effect. The surface gets nearly twice as much infrared from the air as sunlight from the Sun.', 'Atmosfera menghantar 96 unit inframerah kembali ke bawah: kesan rumah hijau. Permukaan menerima hampir dua kali lebih banyak inframerah daripada udara berbanding cahaya Matahari.') },
    { id: 'out', n: 64, from: [0.88, 0.40], to: [0.88, 0.04], color: 'mercury', text: T('大气向太空发出 64。加上从地面漏出去的 6，正好等于吸收的 51 + 19 = 70，收支平衡。', 'The atmosphere radiates 64 to space. With the 6 that leaks from the surface, that is exactly the 51 + 19 = 70 absorbed: the budget balances.', 'Atmosfera memancarkan 64 ke angkasa. Bersama 6 yang terlepas dari permukaan, jumlahnya tepat 51 + 19 = 70 yang diserap: imbangan seimbang.') },
  ],
};

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680)), H = Math.round(W * 0.78);
  const X = f => f * W, Y = f => f * H;
  let mode = 'sw';
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'w-svg w-budget', role: 'img', 'aria-label': p(L.title) });
  const caption = h('p', { class: 'w-explain', 'aria-live': 'polite' });
  const tabs = h('div', { class: 'stage-chips' });

  function draw() {
    svg.replaceChildren(
      s('rect', { x: 0, y: 0, width: W, height: Y(0.06), class: 'zone-space' }),
      s('text', { x: 8, y: Y(0.045), class: 'zone-label' }, p(L.space)),
      s('rect', { x: 0, y: Y(0.30), width: W, height: Y(0.26), class: 'zone-atm', rx: 8 }),
      s('text', { x: 8, y: Y(0.34), class: 'zone-label' }, p(L.atm)),
      s('rect', { x: 0, y: Y(0.90), width: W, height: Y(0.10), class: 'zone-ground' }),
      s('text', { x: 8, y: Y(0.97), class: 'zone-label' }, p(L.ground)));
    for (const a of ARROWS[mode]) {
      const [x1, y1] = [X(a.from[0]), Y(a.from[1])], [x2, y2] = [X(a.to[0]), Y(a.to[1])];
      const dir = Math.sign(y2 - y1), w = clamp(3 + a.n / 10, 3, 14);
      const g = s('g', { class: 'budget-arrow', tabindex: '0', role: 'button', 'aria-label': `${a.n}: ${p(a.text)}` },
        s('line', { x1, y1, x2, y2: y2 - dir * 10, style: `stroke: var(--${a.color}); stroke-width: ${w}` }),
        s('path', { d: `M${x2 - w - 4},${y2 - dir * 12} L${x2},${y2} L${x2 + w + 4},${y2 - dir * 12} Z`, style: `fill: var(--${a.color})` }),
        s('text', { x: x1 + w / 2 + 6, y: (y1 + y2) / 2 + 4, class: 'budget-n' }, String(a.n)));
      const pickIt = () => { for (const n of svg.querySelectorAll('.budget-arrow')) n.classList.remove('is-on'); g.classList.add('is-on'); caption.textContent = `${a.n} — ${p(a.text)}`; };
      g.addEventListener('click', pickIt);
      g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pickIt(); } });
      svg.append(g);
    }
    caption.textContent = p(L.hint);
    tabs.replaceChildren(...['sw', 'lw'].map(m => {
      const b = h('button', { type: 'button', class: `chip${m === mode ? ' is-on' : ''}` }, p(L[m]));
      b.addEventListener('click', () => { mode = m; draw(); });
      return b;
    }));
  }
  el.append(frame({ title: p(L.title), lang, source: 'Ahrens 2010, pp. 44–45', children: [tabs, svg, caption] }));
  draw();
  return { destroy() { el.replaceChildren(); } };
}
