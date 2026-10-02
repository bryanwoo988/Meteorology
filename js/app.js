/* Boot, hash router, views. The only module that wires the others together.

   Routes (all in the fragment, so the service worker only ever serves the root):
     #/                     home: the nine stages
     #/stage/N              one stage
     #/ch/chNN[/sID]        a chapter, optionally scrolled to a section
     #/info  #/share  #/search  #/tools/<name>[/N] */

import * as prefs from './prefs.js';
import { t, pick, LANG_GLYPH } from './i18n.js';
import { loadIndex, loadChapter, loadData, renderSections, el } from './content.js';
import { loadTerms, openTermSheet, renderNewTerms } from './terms.js';
import { newerRevision, updateAction, mayAutoReload } from './updatelogic.js';
import { notesSince } from './releases.js';
import { APP_URL, AUTHOR } from './config.js';

const $ = sel => document.querySelector(sel);
const main = $('#main');

/* ---------- Icons (24px stroke, currentColor) ---------- */
const svg = d => `<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
const ICON = {
  search: svg('<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/>'),
  sun: svg('<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>'),
  moon: svg('<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z"/>'),
  auto: svg('<circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17A8.5 8.5 0 0 0 12 3.5Z" fill="currentColor"/>'),
  more: svg('<circle cx="5.5" cy="12" r="1.2" fill="currentColor"/><circle cx="12" cy="12" r="1.2" fill="currentColor"/><circle cx="18.5" cy="12" r="1.2" fill="currentColor"/>'),
  close: svg('<path d="M6 6l12 12M18 6 6 18"/>'),
  check: svg('<path d="m5 12.5 4.5 4.5L19 7.5"/>'),
  arrowL: svg('<path d="M15 5l-7 7 7 7"/>'),
  arrowR: svg('<path d="M9 5l7 7-7 7"/>'),
};
const SCALE_LABEL = { 1: 'A', 1.15: 'AA', 1.3: 'AAA', 1.5: 'AAA+' };

/* ---------- State ---------- */
let index = null, terms = null, sources = null, releases = [];
let current = { route: null, chapterNum: null };
let visibleSince = performance.now();
let asked = false;

const lang = () => prefs.get().lang;
const tr = (k, v) => t(k, v, lang());
const cid = n => `ch${String(n).padStart(2, '0')}`;
const readyChapters = () => index.chapters.filter(c => c.ready !== false);

/* ---------- Header ---------- */
function paintHeader() {
  const p = prefs.get();
  const set = (sel, html, label) => { const b = $(sel); b.innerHTML = html; b.setAttribute('aria-label', label); b.title = label; };
  set('[data-action="search"]', ICON.search, tr('search'));
  set('[data-action="lang"]', `<span class="glyph">${LANG_GLYPH[p.lang]}</span>`, tr('langButton'));
  set('[data-action="theme"]', ICON[p.theme === 'auto' ? 'auto' : p.theme === 'dark' ? 'moon' : 'sun'], tr('themeButton'));
  set('[data-action="scale"]', `<span class="glyph glyph-scale">${SCALE_LABEL[p.scale]}</span>`, tr('scaleButton'));
  set('[data-action="more"]', ICON.more, tr('more'));
  $('.sheet-close').innerHTML = ICON.close;
  $('.sheet-close').setAttribute('aria-label', tr('close'));
  for (const n of document.querySelectorAll('[data-ui]')) n.textContent = tr(n.dataset.ui);
}

/* ---------- Sheet ---------- */
function openSheet(content) {
  const body = $('.sheet-body');
  body.replaceChildren(content);
  $('#sheet').hidden = false;
  document.body.classList.add('sheet-open');
  $('.sheet-panel').focus?.();
}
function closeSheet() {
  $('#sheet').hidden = true;
  document.body.classList.remove('sheet-open');
}

/* ---------- Routing ---------- */
function parse(hash) {
  const parts = hash.replace(/^#\/?/, '').split('/').filter(Boolean);
  const [a, b, c] = parts;
  if (!a) return { view: 'home' };
  if (a === 'stage') return { view: 'stage', n: Number(b) };
  if (a === 'ch') return { view: 'chapter', id: b, section: c };
  if (a === 'tools') return { view: 'tools', name: b, arg: c };
  if (['info', 'share', 'search'].includes(a)) return { view: a };
  return { view: 'home' };
}

const ctxFor = () => ({
  lang: lang(),
  terms,
  onTerm: id => openTermSheet(id, { lang: lang(), openSheet, currentChapter: current.chapterNum }),
  sourceLabel: s => {
    const [id, pages] = s.split(':');
    const src = sources.find(x => x.id === id);
    return `${src?.short ?? id}${pages ? `, p. ${pages}` : ''}`;
  },
});

async function render({ keepAnchor = false } = {}) {
  const r = parse(location.hash);
  current = { route: r, chapterNum: null };
  closeSheet();
  const anchor = keepAnchor ? readingAnchor() : null;
  document.documentElement.dataset.view = r.view;
  try {
    const view = await VIEWS[r.view](r);
    main.replaceChildren(view);
  } catch (e) {
    console.error(e);
    main.replaceChildren(el('div', { class: 'page' }, el('p', { class: 'error' }, tr('loadError'))));
  }
  if (anchor) restoreAnchor(anchor);
  else if (r.section) scrollToSection(r.section);
  else window.scrollTo(0, 0);
  if (r.view === 'chapter') prefs.setLastRoute(location.hash);
}

function scrollToSection(id) {
  const target = document.getElementById(id);
  if (!target) return;
  if (target.tagName === 'DETAILS') target.open = true;
  target.scrollIntoView({ block: 'start' });
}

// The section the reader is looking at, and where it sits on screen, so a
// language switch can put it back in the same place.
function readingAnchor() {
  const top = $('.topbar').getBoundingClientRect().bottom;
  for (const s of document.querySelectorAll('.section')) {
    const r = s.getBoundingClientRect();
    if (r.bottom > top + 8) return { id: s.id, offset: r.top };
  }
  return null;
}
function restoreAnchor({ id, offset }) {
  const s = document.getElementById(id);
  if (!s) return;
  window.scrollBy(0, s.getBoundingClientRect().top - offset);
}

/* ---------- Views ---------- */
const VIEWS = {
  async home() {
    const p = prefs.get();
    const last = p.lastRoute && parse(p.lastRoute).view === 'chapter' ? p.lastRoute : null;
    const first = readyChapters()[0];
    const hero = el('section', { class: 'hero' },
      el('h1', {}, tr('appName')),
      el('p', { class: 'lede' }, tr('tagline')),
      last ? el('a', { class: 'button', href: last }, tr('continueReading'))
        : first ? el('a', { class: 'button', href: `#/ch/${first.id}` }, tr('startHere')) : null);
    const stages = el('ol', { class: 'stage-list' }, index.stages.map(s => stageCard(s, p)));
    return el('div', { class: 'page page-home' }, hero, stages);
  },

  async stage({ n }) {
    const s = index.stages.find(x => x.n === n);
    if (!s) return VIEWS.home();
    const p = prefs.get();
    const chs = s.chapters.map(id => index.chapters.find(c => c.id === id));
    return el('div', { class: 'page' },
      el('p', { class: 'kicker' }, tr('stageN', { n })),
      el('h1', {}, pick(s.title, lang())),
      el('p', { class: 'lede' }, pick(s.blurb, lang())),
      el('ol', { class: 'chapter-list' }, chs.map(c => {
        const ready = c.ready !== false;
        const inner = [el('span', { class: 'ch-num' }, String(c.num)), el('span', { class: 'ch-title' }, pick(c.title, lang())),
          p.read[c.id] ? el('span', { class: 'ch-read', 'aria-label': tr('isRead') }) : null];
        const li = el('li', { class: ready ? '' : 'is-soon' },
          ready ? el('a', { href: `#/ch/${c.id}` }, inner) : el('span', { class: 'ch-row' }, inner));
        const mark = li.querySelector('.ch-read');
        if (mark) mark.innerHTML = ICON.check;
        return li;
      })));
  },

  async chapter({ id }) {
    const meta = index.chapters.find(c => c.id === id && c.ready !== false);
    if (!meta) return VIEWS.home();
    const ch = await loadChapter(id);
    current.chapterNum = ch.num;
    const ctx = ctxFor();
    const ready = readyChapters();
    const i = ready.findIndex(c => c.id === id);
    const prev = ready[i - 1], next = ready[i + 1];
    const stage = index.stages.find(s => s.n === ch.stage);
    const isRead = !!prefs.get().read[id];

    const toc = el('nav', { class: 'toc', 'aria-label': 'Contents' },
      el('p', { class: 'toc-title' }, pick(stage.title, lang())),
      el('ol', {}, stage.chapters.map(cId => {
        const c = index.chapters.find(x => x.id === cId);
        const on = c.ready !== false;
        return el('li', { class: [cId === id ? 'is-current' : '', on ? '' : 'is-soon'].join(' ').trim() },
          on ? el('a', { href: `#/ch/${cId}` }, `${c.num}. ${pick(c.title, lang())}`) : `${c.num}. ${pick(c.title, lang())}`);
      })));

    const readBtn = el('button', { type: 'button', class: `button ${isRead ? 'is-on' : 'button-quiet'}`,
      onclick: () => { prefs.markRead(id, !prefs.get().read[id]); render({ keepAnchor: true }); } },
      isRead ? tr('isRead') : tr('markRead'));
    if (isRead) readBtn.insertAdjacentHTML('afterbegin', ICON.check);

    const article = el('article', { class: 'chapter' },
      el('p', { class: 'kicker' }, el('a', { href: `#/stage/${ch.stage}` }, tr('stageN', { n: ch.stage })), ` · ${tr('chapterN', { n: ch.num })}`),
      el('h1', {}, pick(ch.title, lang())),
      renderNewTerms(ch.newTerms, ctx),
      renderSections(ch, ctx),
      el('section', { class: 'chapter-sources' },
        el('h2', {}, tr('sources')),
        el('ul', {}, ch.sources.map(sid => {
          const s = sources.find(x => x.id === sid);
          if (!s) return null;
          return el('li', {}, s.url ? el('a', { href: s.url, target: '_blank', rel: 'noopener' }, s.title, ' ↗') : s.title, `. ${s.publisher}.`);
        }))),
      el('footer', { class: 'chapter-foot' },
        readBtn,
        el('div', { class: 'pager' },
          prev ? el('a', { class: 'pager-link', href: `#/ch/${prev.id}` }, el('span', { class: 'pager-dir' }, tr('prev')), pick(prev.title, lang())) : el('span'),
          next ? el('a', { class: 'pager-link is-next', href: `#/ch/${next.id}` }, el('span', { class: 'pager-dir' }, tr('next')), pick(next.title, lang())) : el('span'))));
    return el('div', { class: 'page page-chapter' }, toc, article);
  },

  async info() {
    const status = el('p', { class: 'status' }, '…');
    offlineStatus().then(ok => { status.textContent = tr(ok ? 'offlineReady' : 'offlineNotYet'); status.classList.add(ok ? 'is-ok' : 'is-pending'); });
    return el('div', { class: 'page page-info' },
      el('h1', {}, tr('info')),
      el('p', { class: 'lede' }, tr('tagline')),
      el('dl', { class: 'keyval' },
        el('dt', {}, tr('version')), el('dd', {}, releases[0]?.v ?? ''),
        el('dt', {}, 'Offline'), el('dd', {}, status)),
      el('p', { class: 'credit' }, tr('createdBy')),
      el('p', {}, el('a', { class: 'button button-quiet', href: '#/share' }, tr('share'))),
      el('h2', {}, tr('allSources')),
      el('ul', { class: 'source-list' }, sources.map(s => el('li', {},
        s.url ? el('a', { href: s.url, target: '_blank', rel: 'noopener' }, s.title, ' ↗') : el('strong', {}, s.title),
        el('span', { class: 'muted' }, ` — ${s.publisher}`)))));
  },

  async share() {
    return el('div', { class: 'page page-share' },
      el('h1', {}, tr('share')),
      el('p', { class: 'lede' }, tr('shareHint')),
      el('div', { id: 'share-host' }),
      el('p', { class: 'share-url' }, APP_URL));
  },

  async search() {
    return el('div', { class: 'page' }, el('h1', {}, tr('search')), el('p', { class: 'muted' }, tr('searchHint')));
  },

  async tools() {
    return el('div', { class: 'page' }, el('h1', {}, tr('tools')));
  },
};

function stageCard(s, p) {
  const chs = s.chapters.map(id => index.chapters.find(c => c.id === id));
  const ready = chs.filter(c => c.ready !== false);
  const done = ready.filter(c => p.read[c.id]).length;
  const pct = chs.length ? Math.round(100 * done / chs.length) : 0;
  const body = [
    el('span', { class: 'stage-num' }, String(s.n)),
    el('span', { class: 'stage-text' },
      el('span', { class: 'stage-title' }, pick(s.title, lang())),
      el('span', { class: 'stage-blurb' }, pick(s.blurb, lang())),
      el('span', { class: 'stage-meta' }, `${tr('chaptersCount', { n: chs.length })} · ${tr('progress', { done, total: chs.length })}`),
      el('span', { class: 'progress', role: 'progressbar', 'aria-valuenow': pct, 'aria-valuemin': 0, 'aria-valuemax': 100 }, el('span', { style: `width:${pct}%` }))),
  ];
  return el('li', { class: 'stage-card' }, el('a', { href: `#/stage/${s.n}` }, body));
}

/* ---------- More menu ---------- */
function openMore() {
  const item = (href, key) => el('li', {}, el('a', { href, onclick: closeSheet }, tr(key)));
  openSheet(el('nav', { class: 'more-menu' },
    el('ul', {},
      item('#/', 'home'), item('#/tools/glossary', 'glossary'), item('#/tools/abbr', 'abbr'),
      item('#/tools/map', 'conceptMap'), item('#/tools/cards', 'flashcards'), item('#/tools/quiz', 'quiz'),
      item('#/tools/convert', 'converter'), item('#/tools/beaufort', 'beaufort'), item('#/tools/data', 'dataCatalogue'),
      item('#/share', 'share'), item('#/info', 'info'))));
}

/* ---------- Offline + updates ---------- */
async function offlineStatus() {
  try {
    if (!navigator.serviceWorker?.controller) return false;
    return (await caches.keys()).some(n => n.startsWith('meteo-'));
  } catch { return false; }
}

async function liveRevision() {
  try {
    const r = await fetch('index.html', { method: 'HEAD', cache: 'no-store' });
    return r.ok ? r.headers.get('Last-Modified') : null;
  } catch { return null; }
}

const TRIED = 'meteo.reload-tried';
async function checkForUpdate() {
  const live = await liveRevision();
  if (!newerRevision(document.lastModified, live)) return;
  const action = updateAction({
    hidden: document.hidden, asked,
    busy: !$('#sheet').hidden || window.scrollY > 200,
    sinceVisibleMs: performance.now() - visibleSince,
  });
  if (action === 'defer') return;
  let tried = null;
  try { tried = JSON.parse(sessionStorage.getItem(TRIED) || 'null'); } catch { /* ignore */ }
  if (action === 'apply' && (asked || mayAutoReload(tried, live, Date.now()))) return applyUpdate(live);
  $('#update-banner').hidden = false;
}

async function applyUpdate(live) {
  try { sessionStorage.setItem(TRIED, JSON.stringify({ v: live, at: Date.now() })); } catch { /* ignore */ }
  const reg = await navigator.serviceWorker?.getRegistration();
  if (reg) {
    await reg.update().catch(() => {});
    const waiting = reg.installing || reg.waiting;
    if (waiting) {
      await new Promise(r => {
        navigator.serviceWorker.addEventListener('controllerchange', r, { once: true });
        setTimeout(r, 8000);
      });
    }
  }
  location.reload();
}

function showReleaseNotes() {
  const latest = releases[0]?.v;
  if (!latest) return;
  const seen = prefs.get().seenVersion;
  prefs.setSeenVersion(latest);
  const list = notesSince(releases, seen).slice(0, 4);
  if (!list.length) return;
  openSheet(el('div', { class: 'release-notes' },
    el('h2', {}, tr('updatedTo', { v: latest })),
    list.map(r => el('section', {}, el('p', { class: 'kicker' }, `v${r.v} · ${r.date}`),
      el('ul', {}, r.notes.map(n => el('li', {}, pick(n, lang())))))),
    el('button', { type: 'button', class: 'button', onclick: closeSheet }, tr('ok'))));
}

/* ---------- Boot ---------- */
function wire() {
  document.addEventListener('click', e => {
    const a = e.target.closest('[data-action]');
    if (!a) return;
    switch (a.dataset.action) {
      case 'lang': prefs.cycleLang(); break;
      case 'theme': prefs.cycleTheme(); break;
      case 'scale': prefs.cycleFontScale(); break;
      case 'more': openMore(); break;
      case 'search': location.hash = '#/search'; break;
      case 'close-sheet': closeSheet(); break;
      case 'update': asked = true; checkForUpdate(); break;
      default: return;
    }
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !$('#sheet').hidden) closeSheet(); });
  window.addEventListener('hashchange', () => render());
  prefs.subscribe(what => {
    prefs.applyToDocument();
    paintHeader();
    if (what === 'lang' || what === 'scale') render({ keepAnchor: true });
  });
  matchMedia('(prefers-color-scheme: dark)').addEventListener?.('change', () => prefs.applyToDocument());
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) { visibleSince = performance.now(); checkForUpdate(); }
  });
  setInterval(checkForUpdate, 15 * 60e3);
}

function showPicker() {
  return new Promise(resolve => {
    const picker = $('#picker');
    picker.hidden = false;
    picker.querySelector('.is-default').focus();
    picker.addEventListener('click', e => {
      const b = e.target.closest('[data-lang]');
      if (!b) return;
      picker.hidden = true;
      resolve(b.dataset.lang);
    });
  });
}

async function boot() {
  prefs.init();
  prefs.applyToDocument();
  [index, terms, sources, releases] = await Promise.all([
    loadIndex(), loadTerms(), loadData('sources'), loadData('releases').catch(() => []),
  ]);
  paintHeader();
  wire();
  $('#splash').classList.add('is-done');
  document.documentElement.dataset.ready = 'true';
  if (!prefs.get().chosen) {
    const chosen = await showPicker();
    prefs.chooseLang(chosen);   // subscribe() re-renders and repaints
    prefs.setSeenVersion(releases[0]?.v ?? '');
  } else {
    await render();
    showReleaseNotes();
  }
  // On the dev server a cache-first worker would pin stale files; ?sw=1 opts in.
  const dev = ['localhost', '127.0.0.1'].includes(location.hostname) && !/[?&]sw=1/.test(location.search);
  if ('serviceWorker' in navigator && location.protocol !== 'file:' && !dev) {
    navigator.serviceWorker.register('sw.js').catch(e => console.warn('[sw]', e));
  }
  checkForUpdate();
}

boot();

export { openSheet, closeSheet, AUTHOR };
