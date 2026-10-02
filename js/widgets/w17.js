/* W17 — Radar colours and rain rate. Tap a colour: the reflectivity in
   dBZ and roughly how many millimetres an hour it means, by the
   Marshall–Palmer relation (Z = 200 R^1.6) and by the US NWS tropical
   relation (Z = 250 R^1.2). The colour scale is a typical one, not any
   one agency's. physics.rainRateZR. */

import { rainRateZR } from '../physics.js';
import { h, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('雷达颜色和雨量：点一个颜色', 'Radar colours and rain rate: tap a colour', 'Warna radar dan kadar hujan: ketik satu warna'),
  mp: T('Marshall–Palmer 关系', 'Marshall–Palmer relation', 'Hubungan Marshall–Palmer'), trop: T('热带关系', 'Tropical relation', 'Hubungan tropika'),
  per: T('毫米/小时', 'mm an hour', 'mm sejam'),
  note: T('美国国家气象局的经验：热带对流时，一般默认的公式常常低估雨量，所以有另一条“热带关系”。雷达估计的雨量始终只是估计。', 'US National Weather Service experience: in tropical convection the usual default formula tends to underestimate rain, hence a separate tropical relation. Radar rainfall is always an estimate.', 'Pengalaman Perkhidmatan Cuaca Kebangsaan AS: dalam perolakan tropika formula lalai biasa cenderung meremehkan hujan, maka wujud hubungan tropika yang berasingan. Hujan radar sentiasa satu anggaran.'),
};
const STEPS = [[15, '#9ec9e8'], [20, '#5aa9e0'], [25, '#2f7fd1'], [30, '#3fbf5a'], [35, '#1f9a3a'], [40, '#f2d22e'], [45, '#f29d1f'], [50, '#e8541c'], [55, '#c8102e'], [60, '#a0148c'], [65, '#e8e8e8']];

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const row = h('div', { class: 'dbz-row', role: 'group', 'aria-label': p(L.title) });
  const out = h('div', { class: 'w-explain', 'aria-live': 'polite' });
  const r1 = v => (v < 10 ? v.toFixed(1) : v.toFixed(0));
  function show(i) {
    const [dbz] = STEPS[i];
    [...row.children].forEach((c, j) => c.setAttribute('aria-pressed', String(i === j)));
    out.replaceChildren(h('p', {}, h('strong', {}, `${dbz} dBZ`)),
      h('p', {}, `${p(L.mp)}: ≈ ${r1(rainRateZR(dbz, 200, 1.6))} ${p(L.per)}`),
      h('p', {}, `${p(L.trop)}: ≈ ${r1(rainRateZR(dbz, 250, 1.2))} ${p(L.per)}`));
  }
  STEPS.forEach(([dbz, c], i) => {
    const b = h('button', { type: 'button', class: 'dbz-step', style: `background: ${c}`, 'aria-label': `${dbz} dBZ` }, String(dbz));
    b.addEventListener('click', () => show(i)); row.append(b);
  });
  show(5);
  el.append(frame({ title: p(L.title), lang, schematic: true, source: 'AMS Glossary (Marshall–Palmer relation); NWS Tallahassee, Fournier 1999 (tropical Z–R)', children: [row, out, h('p', { class: 'w-source' }, p(L.note))] }));
  return { destroy() { el.replaceChildren(); } };
}
