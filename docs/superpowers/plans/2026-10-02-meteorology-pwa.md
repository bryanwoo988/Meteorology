# Meteorology PWA Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build 气象学 · Meteorology — an offline, trilingual (zh/en/ms), interactive meteorology course PWA with 42 chapters in 9 stages, deployed to GitHub Pages.

**Architecture:** Static PWA with no build step, no npm dependencies and no CDN. ES modules in `js/`, all content as trilingual JSON in `data/`, a generated precache service worker, and pure-function modules (physics, update logic, cache policy, inline markup, projections) covered by `node --test`. Proven pieces are ported from `~/Desktop/MyPWA/OilPalmWiki` (QR encoder, dev server, SW builder, icon script, CI) and `~/Desktop/MyPWA/CompareCast/CompareCast` (update detection, cache policy, release notes).

**Tech Stack:** HTML, CSS custom properties, vanilla ES2022 modules, SVG, Pointer Events; Node 22 (`node --test`, tooling); Python 3 venv (`pymupdf pillow segno zxing-cpp opencv-python-headless numpy pyshp`) for icons, maps and QR verification; GitHub Actions + GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-10-02-meteorology-design.md` and the content outline `docs/superpowers/specs/2026-10-02-meteorology-outline.md` (the outline is the single source of truth for chapters, terms, widgets, maps and dataset cards).

## Global Constraints

- No npm dependencies, no CDN, no framework. `package.json` exists only for `"type": "module"` and the `test` script.
- Every user-visible string is a `{zh, en, ms}` triple. Missing language = lint failure, never a silent fallback.
- Names: zh `气象学`, en `Meteorology`, ms `Meteorology`. Author line: `Apps created by Bryan Woo`.
- `APP_URL = 'https://bryanwoo988.github.io/Meteorology/'`. All in-app paths relative (`./`).
- First run shows a language picker, default **English**. Header language cycle `zh → en → ms → zh`, glyphs `中 / EN / BM`.
- Theme cycle `auto → light → dark → auto`, applied before first paint. Font scales `[1, 1.15, 1.3, 1.5]`; ≥ 1.3 switches to single column.
- No ambient animation except the splash screen; honour `prefers-reduced-motion`. Widgets move only on user input.
- Reference PDFs are never committed (`References/` and `*.pdf` are git-ignored). No book prose, figures or quiz questions are copied — rewritten text, redrawn SVG, original questions.
- Every non-book fact carries a source id from `data/sources.json` and an entry in `docs/sources-log.md` (claim, URL, date checked). Unverifiable claims are left out. Every Stage 6 (Malaysia) block must have a `src`.
- Illustrative figures are labelled "示意图 / Schematic / Ilustrasi"; they never show invented numbers. W21 is labelled as a Lorenz-63 demonstration, not a forecast.
- UI tone: professional and clean — restrained palette from `icon.png`, one sans-serif system font stack, generous whitespace, no decorative gradients or emoji in chrome, 375 px phone width first.
- Git identity for commits: `bryanwoo988 <94886394+bryanwoo988@users.noreply.github.com>`. Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Pushing / creating the GitHub repo requires Bryan's explicit go-ahead.

## Review Focus

1. **Storage unavailable** (private browsing, blocked site data): the app must still boot with defaults and the picker; `prefs` falls back to memory. → Task 4 test `prefs works when localStorage throws`.
2. **Deep link opened before a language is chosen, while offline-uninstalled**: picker appears, then the reader lands on `#/ch/14#s2`. → Task 7 browser test `deep link survives the language picker`.
3. **Extreme widget input** (RH 0 %, RH 100 %, T −40 °C / 55 °C, drag past the edge): physics returns `null` outside validity, widgets show "—" instead of `NaN`. → Task 3 tests `returns null outside validity range`; Task 9 test `widget clamps pointer outside the plot`.
4. **Update while reading**: a new deploy must show the banner, not reload, and must never reload-loop. → Task 5 tests on `updateAction` and `mayAutoReload`.
5. **Long Malay strings at 150 % on 375 px**: header, cards and tables must not overflow horizontally. → Task 7 browser test `no horizontal overflow at 375px × scale 1.5 in ms`, re-run in every content task.

---

## File Structure

```
index.html                 shell markup, splash, picker, sheets
manifest.webmanifest
sw.js                      generated block (CACHE, ASSETS) + fetch/install/activate
package.json               {"type":"module","private":true,"scripts":{"test":"node --test tests/"}}
css/app.css                tokens (light/dark), type scale, layout, components
js/config.js               APP_URL, AUTHOR
js/prefs.js                lang/theme/scale/progress persistence (memory fallback)
js/i18n.js                 LANGS, pick(), t(), UI string table
js/markup.js               parseInline() for {{t:id}} / {{t:id|label}}  (pure)
js/content.js              loadIndex/loadChapter, renderBlocks()
js/terms.js                term sheet, "new terms" box, glossary data access
js/charts.js               declarative SVG charts with scrub readout
js/physics.js              pure meteorology functions
js/projections.js          equalEarth(), orthographic(), seAsia()  (pure)
js/maps.js                 base maps + layers → <svg>
js/widgets/index.js        registry: id → () => import('./wN.js')
js/widgets/w1.js … w27.js  one widget per file; m1.js … m13.js map figures
js/datasets.js             dataset card renderer
js/search.js               trilingual index over chapters + terms
js/quiz.js                 stage quizzes + flashcards
js/tools.js                glossary, abbreviations, concept map, °C⇄°F, Beaufort, data catalogue
js/share.js                share sheet (QR, navigator.share, copy)
js/qrcode.js               ported from OilPalmWiki unchanged
js/updatelogic.js          ported from CompareCast, ESM
js/swpolicy.js             cache rules (pure)
js/releases.js             notesSince() (pure)
js/app.js                  boot, hash router, views, wiring (only module touching the router)
data/index.json            stages, chapters, UI strings
data/ch01.json … ch42.json
data/terms.json  data/quiz.json  data/sources.json  data/releases.json  data/datasets.json
data/series/*.json         real data for widgets (source + fetched date)
data/maps/*.json           simplified coastlines/borders + gridded layers (source + date)
icons/                     generated
tools/serve.py  tools/make-icons.py  tools/build-maps.py  tools/build-sw.mjs
tools/lint-content.mjs  tools/fetch-series.mjs  tools/check-links.mjs  tools/verify-qr.py
tests/*.test.js            node tests;  tests/index.html  browser tests
.github/workflows/deploy.yml  .github/workflows/links.yml
docs/sources-log.md
```

---

## Task 1: Scaffold, dev server, config

**Files:**
- Create: `package.json`, `js/config.js`, `tools/serve.py`, `.claude/launch.json`, `README.md`, `docs/sources-log.md`, `tests/smoke.test.js`

**Interfaces:**
- Produces: `export const APP_URL`, `export const AUTHOR = 'Bryan Woo'` in `js/config.js`; dev server on port **4190**.

- [ ] **Step 1:** Write `tests/smoke.test.js`: imports `../js/config.js`, asserts `APP_URL === 'https://bryanwoo988.github.io/Meteorology/'` and `AUTHOR === 'Bryan Woo'`.
- [ ] **Step 2:** Run `node --test tests/` → FAIL (module not found).
- [ ] **Step 3:** Create `package.json` and `js/config.js`. Copy `~/Desktop/MyPWA/OilPalmWiki/tools/serve.py`, default port 4190. `.claude/launch.json` config named `meteorology` running `python3 tools/serve.py 4190`. `README.md`: one-paragraph description + "Run it" (serve.py, `npm test` equivalent `node --test tests/`). `docs/sources-log.md`: header table `| 章 | 说法 | 网址 | 查阅日期 |`.
- [ ] **Step 4:** `node --test tests/` → PASS; `python3 tools/serve.py 4190` serves `/` (404 is fine until Task 7).
- [ ] **Step 5:** Commit `Scaffold: config, dev server, test runner`.

## Task 2: Icons, splash, palette

**Files:**
- Create: `tools/make-icons.py`, `icons/*`, `favicon.ico`
- Modify: `css/app.css` (create with tokens only)

**Interfaces:**
- Produces: `icons/icon-192.png`, `icon-512.png`, `icon-192-maskable.png`, `icon-512-maskable.png`, `apple-touch-icon-180.png`, `favicon-32.png`, `favicon.ico`, `og-image.png` (1200×630), `og-image-square.png` (600×600), `splash-*.png` (iOS sizes as in OilPalmWiki); CSS tokens `--sky --cloud --sun --mercury --page --ink --bg --surface --muted --line` for light and dark.

- [ ] **Step 1:** Create venv in project (`python3 -m venv venv && venv/bin/pip install pillow segno zxing-cpp opencv-python-headless numpy pyshp`).
- [ ] **Step 2:** Port `OilPalmWiki/tools/make-icons.py` to read `icon.png` (512×512, transparent). Maskable icons: icon at 80 % on `--page` light background. Splash/og: icon centred on the background colour with app name in Latin + 中文 rendered by Pillow; never upscale `icon.png` beyond 512 px.
- [ ] **Step 3:** Script also prints the sampled hex of the five icon colours; write them into `css/app.css` `:root` tokens and derive dark-mode tokens (dark `--bg` near `#0f1720`, text contrast ≥ 4.5:1 checked by eye in Task 7).
- [ ] **Step 4:** Run `venv/bin/python tools/make-icons.py`; open `icons/og-image.png` and `icon-512-maskable.png` with Read to check them visually.
- [ ] **Step 5:** Commit `Icons, splash and palette from icon.png`.

## Task 3: Physics

**Files:**
- Create: `js/physics.js`, `tests/physics.test.js`

**Interfaces (all pure, numbers in, number or `null` out; `null` = outside validity):**
- `cToF(c)`, `fToC(f)`
- `satVapPres(tC) → hPa` (Magnus, a=6.1094, b=17.625, c=243.04)
- `dewPoint(tC, rh) → °C`, `relHum(tC, tdC) → %`
- `wetBulbStull(tC, rh) → °C` (Stull 2011; valid RH 5–99 %, T −20…50 °C)
- `heatStressLevel(twC) → 'low'|'moderate'|'high'|'extreme'` (thresholds come from the source verified in Stage 3; until then the function is not exported)
- `lclHeight(tC, tdC) → m` (125 m per °C of spread)
- `stdAtmos(zM) → {tC, pHpa}` (troposphere to 11 km, isothermal to 20 km, `null` above 20 km or below 0)
- `pressureToHeight(pHpa) → m`
- `moistLapse(tC, pHpa) → K/km`
- `parcelProfile(tC, tdC, pSurf, pTop, dp=10) → [{p, t}]` (dry to LCL, then moist, integrated in dp steps)
- `cape(env, parcel) → J/kg` (both arrays of `{p, t}` on the same p levels; positive area only)
- `dayLength(latDeg, doy) → h` (sunrise/sunset at solar elevation −0.833°, i.e. including refraction, as almanacs do), `noonElevation(latDeg, doy) → °`
- `geostrophicWind(dpHpaPer100km, latDeg) → m/s` (ρ = 1.2; `null` for |lat| < 5°)
- `dbzToRain(dbz) → mm/h` (Z = 200 R^1.6)
- `et0(tmax, tmin, rhmax, rhmin, u2, sunH, latDeg, elevM, doy) → mm/day` (FAO-56 eq. 6 with Rs from Ångström a=0.25 b=0.5)
- `lorenzEnsemble(n, steps, eps, seed) → number[n][steps]` (x-component, dt 0.01, σ=10 ρ=28 β=8/3, seeded PRNG, deterministic)

- [ ] **Step 1: Write the failing tests** (`assert.ok(Math.abs(a - b) <= tol)`):

```js
test('°C/°F', () => { eq(cToF(100), 212, 1e-9); eq(fToC(-40), -40, 1e-9); });
test('saturation vapour pressure', () => eq(satVapPres(20), 23.37, 0.05));
test('dew point', () => eq(dewPoint(20, 50), 9.3, 0.1));
test('relHum inverts dewPoint', () => eq(relHum(30, dewPoint(30, 70)), 70, 0.01));
test('Stull wet bulb paper example', () => eq(wetBulbStull(20, 50), 13.7, 0.1));
test('returns null outside validity range', () => {
  assert.equal(wetBulbStull(20, 2), null); assert.equal(wetBulbStull(60, 50), null);
  assert.equal(dewPoint(20, 0), null); assert.equal(stdAtmos(-10), null);
  assert.equal(geostrophicWind(1, 2), null);
});
test('LCL', () => eq(lclHeight(30, 24), 750, 1));
test('standard atmosphere', () => { const s = stdAtmos(0); eq(s.tC, 15, 1e-6); eq(s.pHpa, 1013.25, 0.01); });
test('pressure levels', () => { eq(pressureToHeight(850), 1457, 15); eq(pressureToHeight(500), 5574, 20); eq(pressureToHeight(250), 10363, 30); });
test('moist lapse rate', () => eq(moistLapse(20, 1000), 4.3, 0.4));
test('parcel is dry adiabatic below LCL', () => { const p = parcelProfile(30, 20, 1000, 900); eq(p[0].t - p[5].t, 9.8 * (pressureToHeight(950) - pressureToHeight(1000)) / 1000, 0.6); });
test('CAPE zero when parcel equals environment', () => { const p = parcelProfile(30, 24, 1000, 200); assert.equal(cape(p, p), 0); });
test('CAPE positive for warm moist parcel in standard env', () => { const p = parcelProfile(32, 26, 1000, 200); const env = p.map(({p: pp}) => ({p: pp, t: stdAtmos(pressureToHeight(pp)).tC})); assert.ok(cape(env, p) > 500); });
test('day length', () => { eq(dayLength(0, 80), 12, 0.15); eq(dayLength(0, 172), 12.1, 0.15); eq(dayLength(60, 172), 18.8, 0.3); });
test('noon elevation at equinox on equator', () => eq(noonElevation(0, 80), 90, 1));
test('geostrophic wind', () => eq(geostrophicWind(1, 45), 8.1, 0.2));
test('Marshall-Palmer', () => eq(dbzToRain(40), 11.5, 0.3));
test('FAO-56 example 18', () => eq(et0(21.5, 12.3, 84, 63, 2.078, 9.25, 50.8, 100, 187), 3.9, 0.15));
test('Lorenz ensemble is deterministic and diverges', () => {
  const a = lorenzEnsemble(51, 1500, 1e-3, 7), b = lorenzEnsemble(51, 1500, 1e-3, 7);
  assert.deepEqual(a, b); const spread = k => Math.max(...a.map(m => m[k])) - Math.min(...a.map(m => m[k]));
  assert.ok(spread(10) < 0.1 && spread(1499) > 5);
});
```

- [ ] **Step 2:** `node --test tests/physics.test.js` → FAIL.
- [ ] **Step 3:** Implement `js/physics.js` with the signatures above. Each function carries a one-line comment naming its source (Magnus/Alduchov–Eskridge 1996, Stull 2011, FAO-56, Marshall–Palmer 1948, ICAO standard atmosphere, Lorenz 1963).
- [ ] **Step 4:** `node --test tests/physics.test.js` → PASS.
- [ ] **Step 5:** Commit `Physics: humidity, parcel, CAPE, sun, wind, radar, ET0, Lorenz`.

## Task 4: Preferences and i18n

**Files:**
- Create: `js/prefs.js`, `js/i18n.js`, `tests/prefs.test.js`, `tests/i18n.test.js`

**Interfaces:**
- `prefs.js`: `LANGS = ['zh','en','ms']`, `THEMES = ['auto','light','dark']`, `SCALES = [1,1.15,1.3,1.5]`, `init(storage = globalThis.localStorage)`, `get() → {lang, theme, scale, chosen, read: {chNN: true}, quiz: {stageN: best}, lastRoute, seenVersion}`, `subscribe(fn) → unsubscribe`, `chooseLang(l)`, `cycleLang()`, `cycleTheme()`, `cycleFontScale()`, `markRead(chId, bool)`, `setQuizBest(stage, score)`, `setLastRoute(r)`, `setSeenVersion(v)`. Key `meteo.prefs.v1`. Applying to the DOM (`data-theme`, `--font-scale`, `lang`) is done by `applyToDocument(doc)`, separate so tests stay DOM-free.
- `i18n.js`: `LANG_GLYPH = {zh:'中', en:'EN', ms:'BM'}`, `LANG_NATIVE = {zh:'中文', en:'English', ms:'Bahasa Melayu'}`, `current()`, `pick(obj, lang) → string` (missing → `''` and `console.warn` in dev; lint prevents it shipping), `t(key, vars)`, `UI` table.

- [ ] **Step 1:** Tests: default `lang === 'en'` and `chosen === false`; `cycleLang` from `zh` → `en` → `ms` → `zh`; `cycleTheme` order; `cycleFontScale` wraps 1.5 → 1; **`prefs works when localStorage throws`** (pass a storage whose `getItem/setItem` throw — `init` succeeds, `chooseLang('ms')` updates `get().lang`); persisted state round-trips through a fake storage; `pick({zh:'甲',en:'A',ms:'B'}, 'ms') === 'B'`; `t('share.copy', {})` returns non-empty for all three languages.
- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3:** Implement. Port shape from `OilPalmWiki/js/prefs.js` and `i18n.js`; add progress/quiz/seenVersion fields.
- [ ] **Step 4:** Run → PASS.
- [ ] **Step 5:** Commit `Preferences and i18n with memory fallback`.

## Task 5: Offline and updates

**Files:**
- Create: `js/updatelogic.js`, `js/swpolicy.js`, `js/releases.js`, `sw.js`, `tools/build-sw.mjs`, `data/releases.json`, `tests/updatelogic.test.js`, `tests/swpolicy.test.js`, `tests/releases.test.js`, `tests/sw.test.js`

**Interfaces:**
- `updatelogic.js` (ESM port of CompareCast, same semantics): `newerRevision(running, live) → bool`, `updateAction({hidden, asked, busy, sinceVisibleMs}) → 'apply'|'banner'|'defer'`, `mayAutoReload(tried, v, now) → bool`, `JUST_MS = 3000`, `RETRY_MS = 600000`.
- `swpolicy.js`: `cacheStrategy(url, selfOrigin) → 'precache'|'never'` (own origin → precache-first; every other origin → never, because all external links are user navigations), `cacheKey(url) → url without query`.
- `releases.js`: `notesSince(list, seenVersion) → entries newer than seen, newest first`; `compareVersions(a, b)`.
- `data/releases.json`: `[{ "v": "1.0.0", "date": "…", "notes": [{zh,en,ms}] }]`.
- `tools/build-sw.mjs`: rewrites the `/* --- generated:begin --- */ … end` block in `sw.js` with `CACHE = 'meteo-<10 hex of sha256 over all assets>'` and `ASSETS` from `index.html manifest.webmanifest favicon.ico css js data icons`. Exits 0.

- [ ] **Step 1:** Port CompareCast's `tests/updatelogic.test.js` and `swpolicy.test.js` (adjust to ESM imports). Add: `newerRevision('10/02/2026 09:00:00', 'Fri, 02 Oct 2026 01:00:01 GMT')` true only when live is ≥ 1 s newer in absolute time; `updateAction({busy:true, sinceVisibleMs:100})` → `'banner'`; `mayAutoReload({v:'x', at:0}, 'x', 5*60e3)` → false. `notesSince` returns `[]` for unknown/garbage seen version and at most the entries newer than seen. `tests/sw.test.js`: port `OilPalmWiki/tools/test-sw.mjs` harness to `node:test` — install precaches every ASSET, activate deletes other `meteo-*` caches, fetch serves precache offline, navigation to a nested hash path offline returns `./`.
- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3:** Implement the modules; `sw.js` uses `swpolicy` logic inlined (SW is a classic script; keep a copy check in `tests/sw.test.js` that the inlined function source equals `swpolicy.js`'s).
- [ ] **Step 4:** `node tools/build-sw.mjs && node --test tests/` → PASS.
- [ ] **Step 5:** Commit `Offline service worker, update detection, release notes`.

## Task 6: Content model, terms, linter

**Files:**
- Create: `js/markup.js`, `js/content.js`, `js/terms.js`, `tools/lint-content.mjs`, `data/index.json`, `data/terms.json`, `data/sources.json`, `data/quiz.json`, `data/datasets.json`, `tests/markup.test.js`, `tests/lint.test.js`, `tests/fixtures/*`

**Interfaces:**
- `markup.js`: `parseInline(str) → Array<{text}|{term, label?}>`; `termIds(str) → string[]`.
- Chapter schema exactly as spec §6.2 plus: `{ id:'ch05', num:5, stage:3, title, newTerms:[ids], sections:[{id, heading, level:'basic'|'advanced', blocks}], sources:[ids] }`. Block types: `p list keyval table chart figure note(kind tip|warn|key|myth) widget dataset map`. Optional `src:[ids]` on any block.
- `index.json`: `{ app:{zh,en,ms}, stages:[{n, title, blurb, chapters:[ids]}], chapters:[{id,num,stage,title,blurb}], ui:{…} }`.
- `terms.json`: `[{id, name, short, chapter, abbr?, see?:[ids]}]`; `abbr` marks entries for the abbreviation list.
- `content.js`: `loadIndex()`, `loadChapter(id)`, `renderChapter(chapter, {lang, onTerm}) → DocumentFragment`.
- `terms.js`: `loadTerms()`, `termById(id)`, `openTermSheet(id)`, `renderNewTerms(ids) → Element`.
- `lint-content.mjs`: exports `lint(rootDir) → {errors:[string], stats}`; CLI prints and exits 1 on errors. Checks spec §6.3 items 1–6 plus: every `map` id and `dataset` id exists; Stage 6 blocks all have `src`; `newTerms` are exactly the terms whose `chapter` equals this chapter.

- [ ] **Step 1:** Tests: `parseInline('A {{t:dew-point}} and {{t:lcl|cloud base}}.')` → `[{text:'A '},{term:'dew-point'},{text:' and '},{term:'lcl',label:'cloud base'},{text:'.'}]`; unclosed `{{t:x` stays text. Lint fixtures: `missing-ms` → error mentions `ms`; `term-before-definition` (ch02 uses a term whose chapter is 5) → error `ch02 uses "dew-point" defined in ch05`; `term-before-defining-paragraph` (same chapter, used in section 1, defined in section 2) → error; `unknown-source`; `stage6-no-src`; `valid` → zero errors.
- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3:** Implement. "Defined" position = the first block in the defining chapter whose text contains `{{t:id}}` inside a block flagged `"defines": ["id"]`; the linter requires that flag exactly once per term.
- [ ] **Step 4:** Run → PASS; `node tools/lint-content.mjs` on the empty real data → PASS.
- [ ] **Step 5:** Commit `Content model, inline term markup, content linter`.

## Task 7: Shell, design system, first real chapter

**Files:**
- Create: `index.html`, `js/app.js`, `manifest.webmanifest`, `tests/index.html`, `tests/browser.js`, `data/ch05.json` (Chapter 5 Humidity, real content following the Content Procedure below, without its widget)
- Modify: `css/app.css`, `data/index.json`, `data/terms.json`, `data/sources.json`

**Interfaces:**
- Routes (hash): `#/` home, `#/stage/N`, `#/ch/chNN` (+ `#sID` section anchor), `#/tools/glossary|abbr|map|cards|quiz/N|convert|beaufort|data`, `#/info`, `#/share`, `#/search?q=`.
- `app.js` consumes everything above; exposes nothing.

- [ ] **Step 1:** Browser tests in `tests/browser.js` (run at `/tests/` in the preview browser): picker shows when `chosen` false and defaults to English; **`deep link survives the language picker`** (`#/ch/ch05#s2` → choose 中文 → lands on ch05 section s2); language button cycles and keeps scroll position; theme applied before first paint (no `data-theme` flash: inline head script); AAA scale 1.3 makes layout single-column; **`no horizontal overflow at 375px × scale 1.5 in ms`** (`document.documentElement.scrollWidth <= 375` on home and ch05).
- [ ] **Step 2:** Run in preview at 375 px → FAIL.
- [ ] **Step 3:** Build `index.html` (head: meta viewport, theme-color, og tags with absolute `APP_URL` URLs, manifest, iOS splash links, inline pre-paint theme/scale script; body: splash, picker, header, main, bottom sheet, update banner). `css/app.css`: type scale on `--font-scale`, system font stack, 8-px spacing grid, 1-px `--line` dividers, cards with no shadow in light / subtle border in dark, max content width 720 px, sticky stage/chapter TOC at ≥ 960 px. Views: home (9 stage cards with progress), stage, chapter (new-terms box → sections with basic/advanced disclosure → sources → prev/next/mark read), info (author, sources, version, offline status). Release-notes sheet after an update (`notesSince`), update banner (`updateAction`), SW registration.
- [ ] **Step 4:** Tests pass in preview at 375 px and at desktop width; screenshot both themes and send to Bryan.
- [ ] **Step 5:** Commit `App shell, design system, Chapter 5`.

## Task 8: Share and QR

**Files:**
- Create: `js/share.js`, `tools/verify-qr.py`, `tools/make-qr.mjs`
- Copy: `js/qrcode.js` from OilPalmWiki unchanged

**Interfaces:**
- `share.js`: `renderShare(el, {url, lang})` — QR SVG (`qrcode.toSVG(url, {quiet:4})`), "Share" button using `navigator.share({title, url})` when available, "Copy link" via `navigator.clipboard.writeText` with fallback text selection, plain URL text.

- [ ] **Step 1:** `tools/make-qr.mjs` writes the QR the app would render to `tests/out/qr.svg`; `verify-qr.py` (port) decodes it with zxing-cpp and asserts it equals `APP_URL`.
- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3:** Implement `share.js`; wire `#/share` and an entry in the header "more" menu and Info.
- [ ] **Step 4:** `node tools/make-qr.mjs && venv/bin/python tools/verify-qr.py` → PASS; check share sheet at 375 px.
- [ ] **Step 5:** Commit `Share sheet with offline QR code`.

## Task 9: Charts and the widget framework (W5)

**Files:**
- Create: `js/charts.js`, `js/widgets/index.js`, `js/widgets/kit.js`, `js/widgets/w5.js`, `tests/kit.test.js`

**Interfaces:**
- `charts.js`: `render(spec, {lang}) → SVGElement` for kinds `bar line`, with a readout element below; scrubbing via Pointer Events and arrow keys updates the readout. Includes `<title>`, `<desc>`, hidden data table.
- `widgets/kit.js` (shared helpers): `scale(d0, d1, r0, r1)`, `clamp(v, lo, hi)`, `dragValue(el, axis, {min, max, step, onChange})` (pointer capture, clamps outside the plot, arrow keys), `readout(el)`, `schematicBadge(lang)`, `sourceLine(text)`.
- Widget module contract: `export function mount(el, {lang, opts, data}) → {setLang(lang), destroy()}`.
- `widgets/index.js`: `mountWidget(el, id, ctx)` lazy-imports `./${id.toLowerCase()}.js`.

- [ ] **Step 1:** Tests for pure kit helpers: `scale`, `clamp`, and **`widget clamps pointer outside the plot`** (the value mapper used by `dragValue` returns `max` for x beyond the right edge and `min` beyond the left).
- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3:** Implement charts, kit, registry, and W5 (temperature slider 0–45 °C, RH slider 1–100 %; readouts: saturation vapour, dew point, wet bulb, "—" when physics returns `null`). Wire `widget` blocks in `content.js`; add W5 to ch05.
- [ ] **Step 4:** Tests pass; in preview drag both sliders to their extremes at 375 px — no `NaN`, no page scroll while dragging (`touch-action: none` on the plot).
- [ ] **Step 5:** Commit `Scrubbable charts, widget kit, humidity widget`.

## Task 10: Maps

**Files:**
- Create: `tools/build-maps.py`, `js/projections.js`, `js/maps.js`, `data/maps/world-110m.json`, `data/maps/seasia-50m.json`, `tests/projections.test.js`

**Interfaces:**
- `projections.js`: `equalEarth([lon, lat]) → [x, y]` (Šavrič et al. 2018 coefficients), `orthographic([lon, lat], [lon0, lat0]) → [x, y] | null` (null on the far side), `equirect` for the SE Asia view.
- `maps.js`: `baseMap(kind:'world'|'seasia'|'globe', {lang, rotate}) → {svg, project, addLayer(layer)}`; layer types `grid` (value grid + colour scale + legend), `arrows`, `points`, `regions`, `labels`; every layer has `source` and `schematic: bool`.
- `build-maps.py`: downloads Natural Earth `ne_110m_land`, `ne_110m_admin_0_countries`, `ne_50m_land`, `ne_50m_admin_0_countries` (public domain), simplifies, writes `[ [lon,lat], … ]` rings with 2-decimal precision; world file < 120 KB, SE Asia file (lon 90–130, lat −12–25) < 120 KB.

- [ ] **Step 1:** Tests: `equalEarth([0,0])` → `[0,0]`; symmetric in lon and lat; `orthographic([180,0],[0,0])` → `null`; `orthographic([0,0],[0,0])` → `[0,0]`.
- [ ] **Step 2:** Run → FAIL.
- [ ] **Step 3:** Implement; run `venv/bin/python tools/build-maps.py`. Globe rotates by drag (pointer), no inertia animation.
- [ ] **Step 4:** Tests pass; render world, SE Asia and globe on a scratch route in preview, both themes.
- [ ] **Step 5:** Commit `Offline base maps and projections`.

## Task 11: Dataset cards, catalogue, link checker

**Files:**
- Create: `js/datasets.js`, `tools/check-links.mjs`, `.github/workflows/links.yml`

**Interfaces:**
- `data/datasets.json` entries: `{id, name, provider, what:{zh,en,ms}, resolution, update:{…}, format, licence:{text, url}, params:[{raw, meaning:{…}, unit, chapter}], sample:{columns:[…], rows:[[…]], source, fetched}, links:[{level:'view'|'try'|'pro', label:{…}, url}]}`.
- `datasets.js`: `renderDataset(entry, {lang}) → Element`; external links get `↗`, `rel="noopener"`, and show "需要网络 / Needs internet / Perlu internet" when `navigator.onLine` is false.
- `check-links.mjs`: collects every `https://` URL in `data/**/*.json`, HEAD (fallback GET) with 15 s timeout, prints failures, exit 1 only with `--strict`. `links.yml` runs it weekly (Mon 01:00 UTC) and on manual dispatch.

- [ ] **Step 1:** Test (`tests/links.test.js`): `collectUrls(fixtureDir)` finds URLs nested in arrays/objects and de-duplicates.
- [ ] **Step 2:** Run → FAIL. **Step 3:** Implement. **Step 4:** PASS; render one placeholder card on the scratch route (removed before commit).
- [ ] **Step 5:** Commit `Dataset cards and weekly link check`.

## Task 12: Study tools

**Files:**
- Create: `js/search.js`, `js/quiz.js`, `js/tools.js`, `tests/search.test.js`, `tests/quiz.test.js`

**Interfaces:**
- `search.js`: `buildIndex(chapters, terms)`, `search(index, query, lang, limit=40) → [{route, title, snippet}]` — matches across all three languages, returns titles/snippets in `lang`.
- `quiz.js`: `quiz.json` = `[{stage, chapter, q:{…}, options:[{…}×4], answer:0-3, why:{…}}]`; `scoreQuiz(answers, questions) → {correct, total}`; flashcards from terms of a stage.
- `tools.js`: glossary (A–Z per language, chapter link), abbreviations (`abbr` terms), concept map (SVG graph: nodes = terms, edges = `see` links, laid out by chapter column; tap a node → highlight its prerequisites), °C⇄°F (two linked inputs using `cToF/fToC`), Beaufort table 0–12 (km/h, m/s, knots, description), data catalogue (all `datasets.json` cards).

- [ ] **Step 1:** Tests: searching `露点` while `lang='ms'` returns the ch05 hit with Malay title; search is case- and diacritic-insensitive for Latin; `scoreQuiz` counts correctly; every question has exactly 4 options and `answer` in 0–3 (validated by linter too).
- [ ] **Step 2–4:** FAIL → implement → PASS; check each tool page at 375 px.
- [ ] **Step 5:** Commit `Search, quizzes, flashcards, glossary and tools`.

## Task 13: CI and deploy pipeline

**Files:**
- Create: `.github/workflows/deploy.yml`

- [ ] **Step 1:** Port OilPalmWiki's workflow: `node tools/lint-content.mjs` → `node tools/build-sw.mjs` → `node --test tests/` → assemble `_site` from `index.html manifest.webmanifest favicon.ico sw.js css js data icons` → deploy Pages.
- [ ] **Step 2:** Run the same three commands locally → all exit 0.
- [ ] **Step 3:** Commit `CI: lint, rebuild worker, test, deploy`. (Repository creation and first push happen in Task 23 with Bryan's go-ahead.)

---

## Content Procedure (used by Tasks 14–22)

For each chapter in the stage, in outline order:

1. **Read the sources.** Extract the cited PDF pages with PyMuPDF from `References/` (scratch only, never committed). For every ⚠️ item, open the official page (WebFetch) and record `| 章 | 说法 | 网址 | 查阅日期 |` in `docs/sources-log.md`; add the source to `data/sources.json` (`{id, title, publisher, url, accessed}`). Drop any claim that cannot be verified.
2. **Write English first**, original wording, basic sections then advanced; mark each term's defining block with `"defines"`. Add the chapter's terms to `terms.json` (with `abbr` where applicable).
3. **Write 中文 and Bahasa Melayu.** Malay terms follow MetMalaysia / DBP usage where one exists (check MetMalaysia's Malay pages). Keep sentences short; no machine-translation tone.
4. **Widgets, maps, datasets** listed for the chapter in the outline: implement `wN.js`/`mN.js` against the kit/maps contracts; real data via `tools/fetch-series.mjs` (writes `data/series/<id>.json` with `source`, `url`, `fetched`); dataset cards with a real `sample` excerpt.
5. **Quiz:** 1–2 original questions per chapter in `quiz.json`; stage total 8–12.
6. **Verify:** `node tools/lint-content.mjs` and `node --test tests/` pass; open each chapter in preview at 375 px in all three languages and at scale 1.5; drag every widget to its extremes; check dark mode.
7. **Commit** per chapter: `Chapter N: <English title>`.

Running threads to honour (from the outline): 🌦️ afternoon showers in ch 4, 5, 7, 9, 12, 17, 23, 24, 25, 35; "what counts as rain" in ch 6, 7, 15, 35.

## Task 14: Stage 1 — ch01–ch02 (W1)
## Task 15: Stage 2 — ch03–ch04 (W2, W3, W4)
## Task 16: Stage 3 — ch05 (finish), ch06–ch08 (W6, W7)
## Task 17: Stage 4 — ch09–ch12 (W8, W9; maps M1 jet streams, M2 global circulation/ITCZ replacing W10, M3 cyclone basins)
## Task 18: Stage 5 — ch13–ch15 (W11, W12; maps M4 currents, M5 SST, M6 ENSO anomaly, M7 MJO phases, M8 IOD, M9 Köppen; datasets OISST, ONI, MJO)
## Task 19: Stage 6 — ch16–ch20 (W13 as SE Asia map, W24, W14; maps M10 Sumatra squall + sea breeze, M11 flood-prone states, M12 haze; datasets DOE API, ASMC hotspots)
## Task 20: Stage 7 — ch21–ch25 (W15 as globe, W16, W17, W18; maps M13 radar network, buoy array; datasets Himawari, NASA Worldview, MetMalaysia radar)
## Task 21: Stage 8 — ch26–ch37 (W19, W20, W21, W25, W26, W27, W22; model-domain map; datasets ECMWF Open Data, ERA5, GFS/GEFS, ICON, Open-Meteo)
## Task 22: Stage 9 — ch38–ch42 (W23; ch39 only if MPOB/academic sources are found — otherwise remove it from `index.json` and the outline, and tell Bryan)

Each of Tasks 14–22 follows the Content Procedure, ends with the stage quiz and flashcards working, and finishes with a commit `Stage N complete`.

## Task 23: Final review and launch

- [ ] **Step 1:** Whole-app pass: every chapter in three languages at 375 px and desktop, both themes, scale 1.5; offline (DevTools offline after first load) opens every chapter; update flow (change `index.html`, reload → banner / release sheet); `node tools/check-links.mjs` all reachable.
- [ ] **Step 2:** Write `data/releases.json` 1.0.0 notes (三语) and README (features, run, tools, deploy, content sources, licensing, the process).
- [ ] **Step 3:** Ask Bryan before creating `bryanwoo988/Meteorology` on GitHub and pushing; enable Pages (GitHub Actions source).
- [ ] **Step 4:** On the live URL: SW registers, precache complete, QR decodes to the live URL, WhatsApp preview (`og:image`) loads.
- [ ] **Step 5:** Commit any fixes; tell Bryan "已经好了" with the link.
