/* W14 — Malaysia's Air Pollutant Index (API / IPU). Tap a band to see
   what it means and the health advice. Bands, effects and advice are the
   Department of Environment's (API calculation guide, 2021). */

import { h, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('空气污染指数（API）：点一个等级', 'Air Pollutant Index (API): tap a band', 'Indeks Pencemar Udara (IPU): ketik satu tahap'),
  effect: T('对健康的影响', 'Health effect', 'Kesan kepada kesihatan'), advice: T('健康建议', 'Health advice', 'Nasihat kesihatan'),
};
const BANDS = [
  { range: '0–50', color: 'leaf', name: T('良好', 'Good', 'Baik'),
    effect: T('污染低，对健康没有不良影响。', 'Low pollution without any bad effect on health.', 'Pencemaran rendah tanpa sebarang kesan buruk terhadap kesihatan.'),
    advice: T('户外活动不受限制，保持健康生活。', 'No restriction on outdoor activities; keep a healthy lifestyle.', 'Tiada sekatan untuk aktiviti luar; kekalkan gaya hidup sihat.') },
  { range: '51–100', color: 'sky', name: T('中等', 'Moderate', 'Sederhana'),
    effect: T('中等污染，对健康没有不良影响。', 'Moderate pollution that does not harm health.', 'Pencemaran sederhana yang tidak memberi kesan buruk kepada kesihatan.'),
    advice: T('户外活动不受限制，保持健康生活。', 'No restriction on outdoor activities; keep a healthy lifestyle.', 'Tiada sekatan untuk aktiviti luar; kekalkan gaya hidup sihat.') },
  { range: '101–200', color: 'sun', name: T('不健康', 'Unhealthy', 'Tidak sihat'),
    effect: T('会使老人、孕妇、儿童和有心肺疾病的人健康变差。', 'Worsens the health of the elderly, pregnant women, children and people with heart or lung problems.', 'Memburukkan kesihatan warga tua, wanita hamil, kanak-kanak dan orang yang mempunyai masalah jantung atau paru-paru.'),
    advice: T('高风险人群减少户外活动；一般人减少剧烈的户外活动。', 'High-risk people should limit outdoor activity; everyone should cut down on strenuous outdoor activity.', 'Orang berisiko tinggi hadkan aktiviti luar; orang ramai kurangkan aktiviti luar yang berat.') },
  { range: '201–300', color: 'mercury', name: T('非常不健康', 'Very unhealthy', 'Sangat tidak sihat'),
    effect: T('有心肺疾病的人病情加重、运动耐力下降；影响公众健康。', 'Worsens heart and lung conditions and lowers tolerance of exercise; affects public health.', 'Memburukkan keadaan jantung dan paru-paru serta merendahkan toleransi senaman; menjejaskan kesihatan awam.'),
    advice: T('老人和高风险人群留在室内、减少体力活动；有病的人去看医生。', 'The elderly and high-risk people should stay indoors and reduce physical activity; people with health problems should see a doctor.', 'Warga tua dan orang berisiko tinggi berada di dalam rumah dan kurangkan aktiviti fizikal; yang mempunyai masalah kesihatan berjumpa doktor.') },
  { range: '> 300', color: 'warn', name: T('危险', 'Hazardous', 'Merbahaya'),
    effect: T('对高风险人群和公众健康都有危险。', 'Hazardous to high-risk people and to public health.', 'Berbahaya kepada orang berisiko tinggi dan kesihatan awam.'),
    advice: T('老人和高风险人群禁止户外活动；公众避免户外活动。', 'The elderly and high-risk people must not go outdoors; everyone should avoid outdoor activity.', 'Warga tua dan orang berisiko tinggi dilarang beraktiviti luar; orang ramai elakkan aktiviti luar.') },
  { range: '> 500', color: 'ink', name: T('紧急', 'Emergency', 'Kecemasan'),
    effect: T('对高风险人群和公众健康都有危险。', 'Hazardous to high-risk people and to public health.', 'Berbahaya kepada orang berisiko tinggi dan kesihatan awam.'),
    advice: T('听从国家安全理事会的指示，留意大众媒体的公告。', 'Follow the orders of the National Security Council and the announcements in the media.', 'Ikuti arahan Majlis Keselamatan Negara dan pengumuman di media massa.') },
];

export function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const row = h('div', { class: 'api-bands', role: 'group', 'aria-label': p(L.title) });
  const out = h('div', { class: 'w-explain', 'aria-live': 'polite' });
  function show(i) {
    const b = BANDS[i];
    [...row.children].forEach((c, j) => c.setAttribute('aria-pressed', String(i === j)));
    out.replaceChildren(h('p', {}, h('strong', {}, `${b.range} · ${p(b.name)}`)),
      h('p', {}, h('strong', {}, `${p(L.effect)}: `), p(b.effect)), h('p', {}, h('strong', {}, `${p(L.advice)}: `), p(b.advice)));
  }
  BANDS.forEach((b, i) => {
    const btn = h('button', { type: 'button', class: 'api-band', style: `--band: var(--${b.color})` }, h('span', { class: 'api-range' }, b.range), h('span', {}, p(b.name)));
    btn.addEventListener('click', () => show(i));
    row.append(btn);
  });
  show(2);
  el.append(frame({ title: p(L.title), lang, source: 'Department of Environment Malaysia, Air Pollutant Index calculation (2021)', children: [row, out] }));
  return { destroy() { el.replaceChildren(); } };
}
