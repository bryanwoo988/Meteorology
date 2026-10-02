/* Dataset cards: what a real dataset contains, what its numbers look like,
   and where to get it — so a reader can go from a chapter straight to the
   data. Links are ordered by effort: look (view), try in the browser (try),
   download the raw files (pro). */

import { pick, t } from './i18n.js';
import { el } from './content.js';

const LEVEL = {
  view: { zh: '直接看', en: 'Look', ms: 'Lihat' },
  try: { zh: '一键试试', en: 'Try it', ms: 'Cuba' },
  pro: { zh: '专业下载', en: 'Download', ms: 'Muat turun' },
};
const LABEL = {
  provider: { zh: '提供者', en: 'Provider', ms: 'Penyedia' },
  resolution: { zh: '分辨率', en: 'Resolution', ms: 'Resolusi' },
  update: { zh: '更新', en: 'Updated', ms: 'Dikemas kini' },
  format: { zh: '格式', en: 'Format', ms: 'Format' },
  licence: { zh: '授权', en: 'Licence', ms: 'Lesen' },
  params: { zh: '参数', en: 'Parameters', ms: 'Parameter' },
  raw: { zh: '原始名称', en: 'Name in the data', ms: 'Nama dalam data' },
  meaning: { zh: '意思', en: 'Meaning', ms: 'Maksud' },
  unit: { zh: '单位', en: 'Unit', ms: 'Unit' },
  learnt: { zh: '在哪章学', en: 'Taught in', ms: 'Diajar dalam' },
  sample: { zh: '数据长什么样', en: 'What the data looks like', ms: 'Rupa data' },
  where: { zh: '去哪里拿', en: 'Where to get it', ms: 'Di mana mendapatkannya' },
  card: { zh: '数据卡片', en: 'Dataset', ms: 'Set data' },
};

const outside = (url, text, level) => {
  const a = el('a', { href: url, target: '_blank', rel: 'noopener noreferrer', class: 'ds-link', 'data-level': level }, text, ' ↗');
  return a;
};

export function renderDataset(d, { lang }) {
  const L = k => pick(LABEL[k], lang);
  const offline = el('span', { class: 'ds-offline' }, t('needsNet', null, lang));
  const syncOnline = () => { offline.hidden = navigator.onLine; };
  syncOnline();
  addEventListener('online', syncOnline);
  addEventListener('offline', syncOnline);

  return el('section', { class: 'dataset' },
    el('p', { class: 'ds-kicker' }, L('card')),
    el('h3', {}, d.name),
    el('p', {}, pick(d.what, lang)),
    el('dl', { class: 'keyval ds-meta' },
      el('dt', {}, L('provider')), el('dd', {}, d.provider),
      d.resolution ? [el('dt', {}, L('resolution')), el('dd', {}, pick(d.resolution, lang))] : null,
      d.update ? [el('dt', {}, L('update')), el('dd', {}, pick(d.update, lang))] : null,
      el('dt', {}, L('format')), el('dd', {}, pick(d.format, lang)),
      d.licence ? [el('dt', {}, L('licence')), el('dd', {}, d.licence.url ? outside(d.licence.url, d.licence.text, 'licence') : d.licence.text)] : null),
    d.params?.length ? el('div', { class: 'table-scroll' }, el('table', { class: 'ds-params' },
      el('caption', {}, L('params')),
      el('thead', {}, el('tr', {}, ['raw', 'meaning', 'unit', 'learnt'].map(k => el('th', { scope: 'col' }, L(k))))),
      el('tbody', {}, d.params.map(p => el('tr', {},
        el('td', {}, el('code', {}, p.raw)),
        el('td', {}, pick(p.meaning, lang)),
        el('td', {}, p.unit),
        el('td', {}, p.chapter ? el('a', { href: `#/ch/ch${String(p.chapter).padStart(2, '0')}` }, t('chapterN', { n: p.chapter }, lang)) : '—')))))) : null,
    d.sample ? el('figure', { class: 'ds-sample' },
      el('figcaption', {}, L('sample')),
      el('div', { class: 'table-scroll' }, el('table', {},
        el('thead', {}, el('tr', {}, d.sample.columns.map(c => el('th', { scope: 'col' }, el('code', {}, c))))),
        el('tbody', {}, d.sample.rows.map(r => el('tr', {}, r.map(c => el('td', {}, String(c)))))))),
      el('p', { class: 'ds-note' }, `${t('source', null, lang)}: ${d.sample.source} · ${d.sample.fetched}`)) : null,
    el('div', { class: 'ds-where' },
      el('p', { class: 'ds-where-title' }, L('where'), ' ', offline),
      el('ul', { class: 'ds-links' }, ['view', 'try', 'pro'].flatMap(level => (d.links ?? []).filter(l => l.level === level).map(l =>
        el('li', { class: `ds-level-${level}` }, el('span', { class: 'ds-level' }, pick(LEVEL[level], lang)), outside(l.url, pick(l.label, lang), level), l.note ? el('span', { class: 'ds-note' }, pick(l.note, lang)) : null))))));
}

export async function renderDatasetById(host, id, ctx, loadData) {
  const all = await loadData('datasets');
  const d = all.find(x => x.id === id);
  if (d) host.replaceChildren(renderDataset(d, ctx));
}
