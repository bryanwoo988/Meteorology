/* The study tools: glossary, abbreviations, concept map, flashcards,
   self-tests, °C ⇄ °F, the Beaufort scale and the data catalogue.
   Each export builds one page; app.js routes to them. */

import { pick, t } from './i18n.js';
import { el, loadData } from './content.js';
import { scoreQuiz, questionsFor, cardsFor } from './quiz.js';
import { cToF, fToC } from './physics.js';
import { renderDataset } from './datasets.js';
import { s } from './widgets/kit.js';
import * as prefs from './prefs.js';

const cid = n => `ch${String(n).padStart(2, '0')}`;
const page = (title, ...kids) => el('div', { class: 'page page-tool' }, el('p', { class: 'kicker' }, el('a', { href: '#/tools' }, t('tools'))), el('h1', {}, title), ...kids);

const TOOLS = [
  ['glossary', 'glossary'], ['abbr', 'abbr'], ['map', 'conceptMap'], ['cards', 'flashcards'],
  ['quiz', 'quiz'], ['convert', 'converter'], ['beaufort', 'beaufort'], ['data', 'dataCatalogue'],
];

export function toolsIndex(lang) {
  return el('div', { class: 'page' }, el('h1', {}, t('tools', null, lang)),
    el('ul', { class: 'tool-list' }, TOOLS.map(([route, key]) => el('li', {}, el('a', { href: `#/tools/${route}` }, t(key, null, lang))))));
}

/* ---------- Glossary ---------- */
function termRow(term, lang, { showAbbr = false } = {}) {
  return el('li', { class: 'gloss-item', id: `term-${term.id}` },
    el('div', { class: 'gloss-head' },
      el('span', { class: 'gloss-name' }, showAbbr && term.abbr ? term.abbr : pick(term.name, lang)),
      showAbbr && term.abbr ? el('span', { class: 'muted' }, pick(term.name, lang)) : term.abbr ? el('span', { class: 'muted' }, term.abbr) : null,
      el('a', { class: 'gloss-ch', href: `#/ch/${cid(term.chapter)}` }, t('chapterN', { n: term.chapter }, lang))),
    el('p', {}, pick(term.short, lang)));
}

export async function glossary(lang, { abbrOnly = false } = {}) {
  let terms = await loadData('terms');
  if (abbrOnly) terms = terms.filter(x => x.abbr);
  const key = x => (abbrOnly ? x.abbr : pick(x.name, lang));
  // Chinese has no alphabet order a reader would scan; keep the teaching order there.
  const sorted = [...terms].sort((a, b) => (lang === 'zh' && !abbrOnly ? a.chapter - b.chapter : key(a).localeCompare(key(b), lang)));
  const list = el('ul', { class: 'gloss-list' }, sorted.map(x => termRow(x, lang, { showAbbr: abbrOnly })));
  const filter = el('input', { type: 'search', class: 'field', placeholder: t('search', null, lang), 'aria-label': t('search', null, lang) });
  filter.addEventListener('input', () => {
    const q = filter.value.trim().toLowerCase();
    for (const li of list.children) li.hidden = q && !li.textContent.toLowerCase().includes(q);
  });
  return page(t(abbrOnly ? 'abbr' : 'glossary', null, lang), filter, terms.length ? list : el('p', { class: 'muted' }, '—'));
}

/* ---------- Concept map ---------- */
export async function conceptMap(lang, { openSheet }) {
  const terms = await loadData('terms');
  const byChapter = new Map();
  for (const x of terms) (byChapter.get(x.chapter) ?? byChapter.set(x.chapter, []).get(x.chapter)).push(x);
  const cols = [...byChapter.keys()].sort((a, b) => a - b);
  const CW = 150, RH = 34, PAD = 20;
  const W = Math.max(320, cols.length * CW + PAD * 2), H = Math.max(...cols.map(c => byChapter.get(c).length)) * RH + 60;
  const pos = new Map();
  cols.forEach((c, i) => byChapter.get(c).forEach((x, j) => pos.set(x.id, [PAD + i * CW, 50 + j * RH])));
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, width: W, height: H, class: 'cmap-svg', role: 'img', 'aria-label': t('conceptMap', null, lang) });
  cols.forEach((c, i) => svg.append(s('text', { x: PAD + i * CW, y: 24, class: 'cmap-col' }, t('chapterN', { n: c }, lang))));
  const edges = s('g', { class: 'cmap-edges' });
  const nodes = s('g', { class: 'cmap-nodes' });
  for (const x of terms) for (const to of x.see ?? []) {
    const a = pos.get(to), b = pos.get(x.id);
    if (a && b) edges.append(s('path', { d: `M${a[0] + 120},${a[1]} C${a[0] + 140},${a[1]} ${b[0] - 20},${b[1]} ${b[0]},${b[1]}`, 'data-from': to, 'data-to': x.id }));
  }
  const prereqs = id => { const out = new Set(); const walk = k => { for (const p of terms.find(x => x.id === k)?.see ?? []) if (!out.has(p)) { out.add(p); walk(p); } }; walk(id); return out; };
  for (const x of terms) {
    const [px, py] = pos.get(x.id);
    const g = s('g', { class: 'cmap-node', tabindex: '0', 'data-id': x.id, transform: `translate(${px},${py})` },
      s('rect', { x: 0, y: -13, width: 124, height: 26, rx: 13 }),
      s('text', { x: 62, y: 4, 'text-anchor': 'middle' }, pick(x.name, lang)));
    const select = () => {
      const need = prereqs(x.id);
      for (const n of nodes.children) n.classList.toggle('is-on', n.dataset.id === x.id || need.has(n.dataset.id));
      for (const e of edges.children) e.classList.toggle('is-on', need.has(e.dataset.from) && (need.has(e.dataset.to) || e.dataset.to === x.id));
      openSheet(el('div', {}, el('h3', {}, pick(x.name, lang)), el('p', {}, pick(x.short, lang)),
        el('a', { class: 'button', href: `#/ch/${cid(x.chapter)}` }, t('openChapter', null, lang))));
    };
    g.addEventListener('click', select);
    g.addEventListener('keydown', e => { if (e.key === 'Enter') select(); });
    nodes.append(g);
  }
  svg.append(edges, nodes);
  return page(t('conceptMap', null, lang), el('div', { class: 'cmap' }, svg));
}

/* ---------- Flashcards ---------- */
export async function flashcards(lang, { stage }) {
  const [terms, index] = await Promise.all([loadData('terms'), loadData('index')]);
  const n = stage || index.stages.find(st => cardsFor(terms, index.stages, st.n).length)?.n || 1;
  const cards = cardsFor(terms, index.stages, n);
  let i = 0;
  const card = el('button', { type: 'button', class: 'flashcard' });
  const counter = el('p', { class: 'muted fc-count' });
  const show = () => {
    const x = cards[i];
    card.classList.remove('is-flipped');
    card.replaceChildren(el('span', { class: 'fc-front' }, pick(x.name, lang)), el('span', { class: 'fc-back' }, pick(x.short, lang)));
    counter.textContent = `${i + 1} / ${cards.length}`;
  };
  card.addEventListener('click', () => card.classList.toggle('is-flipped'));
  const nav = el('div', { class: 'fc-nav' },
    el('button', { type: 'button', class: 'button button-quiet', onclick: () => { i = (i - 1 + cards.length) % cards.length; show(); } }, t('prev', null, lang)),
    el('button', { type: 'button', class: 'button', onclick: () => { i = (i + 1) % cards.length; show(); } }, t('next', null, lang)));
  const chips = el('div', { class: 'stage-chips' }, index.stages.map(st => {
    const has = cardsFor(terms, index.stages, st.n).length > 0;
    return has ? el('a', { class: `chip${st.n === n ? ' is-on' : ''}`, href: `#/tools/cards/${st.n}` }, t('stageN', { n: st.n }, lang)) : null;
  }));
  if (cards.length) show();
  return page(t('flashcards', null, lang), chips, cards.length ? el('div', { class: 'fc-wrap' }, card, counter, nav) : el('p', { class: 'muted' }, '—'));
}

/* ---------- Self-test ---------- */
export async function quizPage(lang, { stage }) {
  const [quiz, index] = await Promise.all([loadData('quiz'), loadData('index')]);
  if (!stage) {
    const best = prefs.get().quiz;
    return page(t('quiz', null, lang), el('ul', { class: 'tool-list' }, index.stages.map(st => {
      const qs = questionsFor(quiz, st.n);
      if (!qs.length) return null;
      return el('li', {}, el('a', { href: `#/tools/quiz/${st.n}` }, `${t('stageN', { n: st.n }, lang)} · ${pick(st.title, lang)}`,
        el('span', { class: 'muted' }, best[st.n] != null ? ` — ${best[st.n]}/${qs.length}` : ` — ${qs.length}`)));
    })));
  }
  const qs = questionsFor(quiz, stage);
  const answers = new Array(qs.length);
  const result = el('div', { class: 'quiz-result', 'aria-live': 'polite' });
  const list = el('ol', { class: 'quiz-list' }, qs.map((q, qi) => {
    const why = el('p', { class: 'quiz-why', hidden: true }, pick(q.why, lang));
    const li = el('li', { class: 'quiz-q', 'data-answer': String(q.answer) }, el('p', { class: 'quiz-text' }, pick(q.q, lang)));
    const opts = el('div', { class: 'quiz-opts' }, q.options.map((o, oi) => el('button', {
      type: 'button', class: 'quiz-opt',
      onclick: e => {
        if (answers[qi] !== undefined) return;
        answers[qi] = oi;
        for (const [k, b] of [...opts.children].entries()) { b.disabled = true; if (k === q.answer) b.classList.add('is-right'); }
        if (oi !== q.answer) e.currentTarget.classList.add('is-wrong');
        why.hidden = false;
        if (answers.filter(a => a !== undefined).length === qs.length) {
          const { correct, total } = scoreQuiz(answers, qs);
          prefs.setQuizBest(stage, correct);
          result.replaceChildren(el('p', { class: 'quiz-score' }, `${correct}/${total}`),
            el('a', { class: 'button button-quiet', href: `#/stage/${stage}` }, t('stageN', { n: stage }, lang)));
        }
      },
    }, pick(o, lang))));
    li.append(opts, why);
    return li;
  }));
  return page(`${t('quiz', null, lang)} · ${t('stageN', { n: stage }, lang)}`, list, result);
}

/* ---------- °C ⇄ °F ---------- */
export function converter(lang) {
  const c = el('input', { id: 'conv-c', class: 'field', inputmode: 'decimal', type: 'text', value: '30', 'aria-label': '°C' });
  const f = el('input', { id: 'conv-f', class: 'field', inputmode: 'decimal', type: 'text', value: '86', 'aria-label': '°F' });
  const fmt = v => String(Math.round(v * 10) / 10);
  const link = (from, to, fn) => from.addEventListener('input', () => {
    const v = Number(from.value.replace(',', '.'));
    to.value = from.value.trim() !== '' && Number.isFinite(v) ? fmt(fn(v)) : '';
  });
  link(c, f, cToF); link(f, c, fToC);
  return page(t('converter', null, lang),
    el('div', { class: 'conv' }, el('label', {}, c, el('span', {}, '°C')), el('span', { class: 'conv-eq' }, '='), el('label', {}, f, el('span', {}, '°F'))),
    el('p', { class: 'muted' }, '°F = °C × 9 ⁄ 5 + 32 · °C = (°F − 32) × 5 ⁄ 9'));
}

/* ---------- Beaufort ---------- */
// Knots and km/h from Ahrens, Essentials of Meteorology, 6th ed., Table F.1 (over land).
const BEAUFORT = [
  [0, '0–1', '0–2', { zh: '无风', en: 'Calm', ms: 'Tenang' }, { zh: '烟直直往上升', en: 'Smoke rises straight up', ms: 'Asap naik tegak' }],
  [1, '1–3', '2–6', { zh: '软风', en: 'Light air', ms: 'Angin sepoi' }, { zh: '烟会飘，风向标不动', en: 'Smoke drifts; wind vanes do not move', ms: 'Asap hanyut; penunjuk arah tidak bergerak' }],
  [2, '4–6', '7–11', { zh: '轻风', en: 'Light breeze', ms: 'Bayu lemah' }, { zh: '脸上感觉有风，树叶沙沙响', en: 'Felt on the face; leaves rustle', ms: 'Terasa di muka; daun berdesir' }],
  [3, '7–10', '12–19', { zh: '微风', en: 'Gentle breeze', ms: 'Bayu lembut' }, { zh: '树叶和小枝一直在动，小旗展开', en: 'Leaves and twigs move; a light flag extends', ms: 'Daun dan ranting bergerak; bendera ringan berkibar' }],
  [4, '11–16', '20–29', { zh: '和风', en: 'Moderate breeze', ms: 'Bayu sederhana' }, { zh: '吹起灰尘和纸张，小树枝摇动', en: 'Raises dust and paper; small branches move', ms: 'Menerbangkan debu dan kertas; dahan kecil bergerak' }],
  [5, '17–21', '30–39', { zh: '清劲风', en: 'Fresh breeze', ms: 'Bayu segar' }, { zh: '有叶的小树开始摇摆', en: 'Small leafy trees sway', ms: 'Pokok kecil berdaun bergoyang' }],
  [6, '22–27', '40–50', { zh: '强风', en: 'Strong breeze', ms: 'Bayu kuat' }, { zh: '大树枝摇动，电线呼呼作响，打伞困难', en: 'Large branches move; wires whistle; umbrellas hard to use', ms: 'Dahan besar bergerak; wayar berdesing; payung sukar digunakan' }],
  [7, '28–33', '51–61', { zh: '疾风', en: 'Near gale', ms: 'Angin hampir badai' }, { zh: '整棵树都在动，逆风走路吃力', en: 'Whole trees move; walking into the wind is hard', ms: 'Seluruh pokok bergerak; sukar berjalan melawan angin' }],
  [8, '34–40', '62–74', { zh: '大风', en: 'Gale', ms: 'Badai' }, { zh: '小枝被吹断，走路困难', en: 'Twigs break off; walking is difficult', ms: 'Ranting patah; sukar berjalan' }],
  [9, '41–47', '75–87', { zh: '烈风', en: 'Strong gale', ms: 'Badai kuat' }, { zh: '招牌、天线被吹倒，建筑轻微损坏', en: 'Signs and aerials blown down; slight damage', ms: 'Papan tanda dan antena tumbang; kerosakan kecil' }],
  [10, '48–55', '88–101', { zh: '狂风', en: 'Storm', ms: 'Ribut' }, { zh: '树被连根拔起，损坏严重', en: 'Trees uprooted; considerable damage', ms: 'Pokok tercabut; kerosakan besar' }],
  [11, '56–64', '102–119', { zh: '暴风', en: 'Violent storm', ms: 'Ribut ganas' }, { zh: '大范围破坏', en: 'Widespread damage', ms: 'Kerosakan meluas' }],
  [12, '≥ 65', '≥ 120', { zh: '飓风级', en: 'Hurricane force', ms: 'Kekuatan taufan' }, { zh: '极大破坏', en: 'Extensive damage', ms: 'Kerosakan teruk' }],
];

export function beaufort(lang) {
  const H = { zh: ['级', '名称', '节', 'km/h', '陆地上看到的情况'], en: ['Force', 'Name', 'knots', 'km/h', 'What you see on land'], ms: ['Skala', 'Nama', 'knot', 'km/j', 'Apa yang dilihat di darat'] }[lang];
  return page(t('beaufort', null, lang),
    el('div', { class: 'table-scroll' }, el('table', { class: 'beaufort' },
      el('thead', {}, el('tr', {}, H.map(x => el('th', { scope: 'col' }, x)))),
      el('tbody', {}, BEAUFORT.map(([n, kt, kmh, name, obs]) => el('tr', {}, el('td', {}, String(n)), el('td', {}, pick(name, lang)), el('td', {}, kt), el('td', {}, kmh), el('td', {}, pick(obs, lang))))))),
    el('p', { class: 'muted' }, `${t('source', null, lang)}: Ahrens 2010, Table F.1`));
}

/* ---------- Data catalogue ---------- */
export async function catalogue(lang) {
  const all = await loadData('datasets');
  return page(t('dataCatalogue', null, lang), all.length ? all.map(d => renderDataset(d, { lang })) : el('p', { class: 'muted' }, '—'));
}
