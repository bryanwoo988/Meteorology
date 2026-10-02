/* Language resolution and the interface string table.

   Every translatable value is a {zh, en, ms} object; pick() is the single
   place that turns one into a string. Knows nothing about the DOM. */

import { get as getPrefs } from './prefs.js';

const FALLBACK = ['en', 'zh', 'ms'];

// The header button shows the language currently in use.
export const LANG_GLYPH = { zh: '中', en: 'EN', ms: 'BM' };

// Each language named in itself: the first-run picker appears before any
// language has been chosen to label the others in.
export const LANG_NATIVE = { zh: '中文', en: 'English', ms: 'Bahasa Melayu' };

export function current() {
  return getPrefs().lang;
}

export function pick(value, lang = current()) {
  if (value == null) return '';
  if (typeof value === 'string' || typeof value === 'number') return String(value);
  if (value[lang]) return value[lang];
  for (const f of FALLBACK) {
    if (value[f]) {
      // The content linter stops this shipping; in development, make it findable.
      console.warn(`[i18n] missing "${lang}":`, String(value[f]).slice(0, 40));
      return value[f];
    }
  }
  return '';
}

export function t(key, vars, lang = current()) {
  let s = pick(UI[key], lang);
  if (!s) console.warn(`[i18n] no UI string "${key}"`);
  if (vars) for (const [k, v] of Object.entries(vars)) s = s.replaceAll(`{${k}}`, String(v));
  return s;
}

export const UI = {
  appName: { zh: '气象学', en: 'Meteorology', ms: 'Meteorology' },
  tagline: {
    zh: '从大气原理到 ECMWF 集合预报，离线可读的三语气象课',
    en: 'From how the atmosphere works to ECMWF ensembles — an offline course in three languages',
    ms: 'Daripada cara atmosfera berfungsi hingga ramalan ensembel ECMWF — kursus luar talian dalam tiga bahasa',
  },
  pickTitle: { zh: '选择语言', en: 'Choose your language', ms: 'Pilih bahasa anda' },
  pickHint: { zh: '之后随时可以在右上角切换', en: 'You can change it any time from the top bar', ms: 'Anda boleh menukarnya bila-bila masa di bar atas' },

  home: { zh: '首页', en: 'Home', ms: 'Utama' },
  stageN: { zh: '阶段 {n}', en: 'Stage {n}', ms: 'Peringkat {n}' },
  chapterN: { zh: '第 {n} 章', en: 'Chapter {n}', ms: 'Bab {n}' },
  chaptersCount: { zh: '{n} 章', en: '{n} chapters', ms: '{n} bab' },
  progress: { zh: '已读 {done}/{total}', en: '{done} of {total} read', ms: '{done}/{total} dibaca' },
  continueReading: { zh: '继续上次阅读', en: 'Continue reading', ms: 'Sambung membaca' },
  startHere: { zh: '从第一章开始', en: 'Start with Chapter 1', ms: 'Mula dengan Bab 1' },
  newTerms: { zh: '本章新名词', en: 'New in this chapter', ms: 'Istilah baharu bab ini' },
  advanced: { zh: '进阶', en: 'Going deeper', ms: 'Lanjutan' },
  sources: { zh: '本章来源', en: 'Sources for this chapter', ms: 'Sumber bab ini' },
  prev: { zh: '上一章', en: 'Previous', ms: 'Sebelumnya' },
  next: { zh: '下一章', en: 'Next', ms: 'Seterusnya' },
  markRead: { zh: '标记为已读', en: 'Mark as read', ms: 'Tanda sudah dibaca' },
  isRead: { zh: '已读', en: 'Read', ms: 'Sudah dibaca' },
  detailIn: { zh: '详见第 {n} 章', en: 'Explained in Chapter {n}', ms: 'Diterangkan dalam Bab {n}' },
  openChapter: { zh: '打开这一章', en: 'Open the chapter', ms: 'Buka bab' },
  close: { zh: '关闭', en: 'Close', ms: 'Tutup' },
  schematic: { zh: '示意图', en: 'Schematic', ms: 'Ilustrasi' },
  source: { zh: '来源', en: 'Source', ms: 'Sumber' },
  needsNet: { zh: '需要网络', en: 'Needs internet', ms: 'Perlu internet' },

  noteTip: { zh: '小提示', en: 'Tip', ms: 'Tip' },
  noteWarn: { zh: '注意', en: 'Caution', ms: 'Awas' },
  noteKey: { zh: '重点', en: 'Key point', ms: 'Perkara utama' },
  noteMyth: { zh: '常见误解', en: 'Common misconception', ms: 'Salah faham biasa' },

  search: { zh: '搜索', en: 'Search', ms: 'Cari' },
  searchHint: { zh: '搜索章节和名词（三种语言都可以）', en: 'Search chapters and terms, in any of the three languages', ms: 'Cari bab dan istilah, dalam mana-mana tiga bahasa' },
  noResults: { zh: '找不到结果', en: 'No results', ms: 'Tiada hasil' },

  tools: { zh: '工具', en: 'Tools', ms: 'Alatan' },
  glossary: { zh: '名词词典', en: 'Glossary', ms: 'Glosari' },
  abbr: { zh: '缩写表', en: 'Abbreviations', ms: 'Singkatan' },
  conceptMap: { zh: '名词地图', en: 'Concept map', ms: 'Peta konsep' },
  flashcards: { zh: '名词闪卡', en: 'Flashcards', ms: 'Kad imbas' },
  quiz: { zh: '自测题', en: 'Self-test', ms: 'Uji diri' },
  converter: { zh: '°C ⇄ °F 换算', en: '°C ⇄ °F converter', ms: 'Penukar °C ⇄ °F' },
  beaufort: { zh: '蒲福风级', en: 'Beaufort scale', ms: 'Skala Beaufort' },
  dataCatalogue: { zh: '数据目录', en: 'Data catalogue', ms: 'Katalog data' },

  info: { zh: '关于', en: 'About', ms: 'Perihal' },
  share: { zh: '分享', en: 'Share', ms: 'Kongsi' },
  shareHint: { zh: '扫描二维码，用浏览器直接打开这个 App', en: 'Scan to open the app in a browser', ms: 'Imbas untuk membuka aplikasi dalam pelayar' },
  shareButton: { zh: '分享链接', en: 'Share link', ms: 'Kongsi pautan' },
  copyLink: { zh: '复制链接', en: 'Copy link', ms: 'Salin pautan' },
  copied: { zh: '已复制', en: 'Copied', ms: 'Disalin' },
  createdBy: { zh: 'Apps created by Bryan Woo', en: 'Apps created by Bryan Woo', ms: 'Apps created by Bryan Woo' },
  version: { zh: '版本', en: 'Version', ms: 'Versi' },
  offlineReady: { zh: '已可离线使用', en: 'Ready to use offline', ms: 'Sedia digunakan luar talian' },
  offlineNotYet: { zh: '尚未完成离线下载', en: 'Offline download not finished yet', ms: 'Muat turun luar talian belum selesai' },
  allSources: { zh: '资料来源', en: 'Sources', ms: 'Sumber' },

  updateReady: { zh: '有新版本', en: 'A new version is ready', ms: 'Versi baharu sedia' },
  updateNow: { zh: '立即更新', en: 'Update now', ms: 'Kemas kini sekarang' },
  updatedTo: { zh: '已更新到 v{v}', en: 'Updated to v{v}', ms: 'Dikemas kini ke v{v}' },
  ok: { zh: '好的', en: 'OK', ms: 'OK' },

  langButton: { zh: '切换语言', en: 'Change language', ms: 'Tukar bahasa' },
  themeButton: { zh: '切换深浅色', en: 'Change theme', ms: 'Tukar tema' },
  scaleButton: { zh: '字体大小', en: 'Text size', ms: 'Saiz teks' },
  more: { zh: '更多', en: 'More', ms: 'Lagi' },
  loading: { zh: '载入中…', en: 'Loading…', ms: 'Memuatkan…' },
  loadError: { zh: '内容载入失败', en: 'Could not load this page', ms: 'Gagal memuatkan halaman ini' },
};
