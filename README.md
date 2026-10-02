# 气象学 · Meteorology

An offline, trilingual (中文 / English / Bahasa Melayu) course in meteorology —
from how the atmosphere works to how ECMWF's ensemble forecasts are made — with
Malaysia as the running example. A static PWA: no build step, no npm
dependencies, no CDN.

Live: <https://bryanwoo988.github.io/Meteorology/>

## What is in it

- **42 chapters in 9 stages**, in a beginner order: each chapter uses only terms
  taught before it. Stage 6 is Malaysia's weather (monsoons, the afternoon-shower
  rhythm, MetMalaysia warnings, floods and drought, haze); stages 7–8 are
  observations, satellites, radar, Skew-T, numerical models, ECMWF, ensembles,
  AI models and reading forecast apps; stage 9 brings it back to the farm.
- **Interactive figures you drag with a finger** — parcel and Skew-T on a real
  KLIA sounding, the monsoon calendar (ERA5 1991–2020), a 51-member ECMWF ENS
  EPSgram for Kuala Lumpur, live Lorenz chaos, the geostationary-satellite
  family, radar dBZ, API bands, ET₀ (FAO-56) and more.
- **Maps** for anything about *where*: an Equal Earth world map, a detailed
  South-East Asia map and a globe you can turn, with real data (NOAA OISST,
  Köppen–Geiger, ASMC hotspots, NDBC buoys) or clearly labelled schematics.
- **Data cards** for the datasets behind the figures: what the data are, their
  parameters, a real sample of rows, the licence, and links graded from
  "view it" to "use it in code".
- **Tools**: glossary, abbreviations, concept map, flashcards, stage quizzes,
  °C ⇄ °F converter, Beaufort scale, search across all three languages.
- **House conventions**: first-run language picker (default English), 中 → EN →
  BM toggle that keeps your place, light / dark / auto theme, AAA reading
  scale, offline after the first visit, auto-updating service worker with a
  "what's new" sheet, QR-code / share / copy-link page, Info page.

## Sources

Main text: *Principles of Agricultural Meteorology* (Mote & Sahu), supported by
Ahrens' *Essentials of Meteorology*, *Fundamentals of Meteorology* and the
*Terminology on Agricultural Meteorology and Agronomy* — cited by printed page
number. The books themselves are **not** in this repository.

Everything Malaysian or current comes from official or peer-reviewed sources
(MetMalaysia, DOE, ASMC, ECMWF, NOAA, WMO, JMA, FAO, MPOB's Journal of Oil Palm
Research, Scientific Reports, …). Each such fact is logged with its URL and the
date it was checked in [`docs/sources-log.md`](docs/sources-log.md), and every
paragraph shows its sources in the app.

## Run it locally

```bash
python3 tools/serve.py
```

Open <http://127.0.0.1:4190/>. The service worker is skipped on localhost unless
you add `?sw=1`.

## Tests and checks

```bash
node --test 'tests/*.test.js'     # logic: physics, prefs, i18n, updates, SW, markup, lint, quiz…
node tools/lint-content.mjs       # content: three languages, term order, sources, widgets, quiz
node tools/check-links.mjs        # every outside link still answers
```

Browser tests run at <http://127.0.0.1:4190/tests/> (overflow at 375 px in all
three languages at scale 1.5, every widget at its slider extremes, maps, quiz,
share page…).

## Editing content

Chapters are written as Python in `tools/content/chNN.py` and compiled to
`data/chNN.json`, `terms.json`, `sources.json`, `quiz.json` and
`datasets.json`:

```bash
python3 tools/content/ch16.py && node tools/lint-content.mjs
node tools/build-sw.mjs           # refresh the precache list after any change
```

Inline markup: `{{t:dew-point}}` makes a tappable glossary term,
`{{ch:ch09|Chapter 9}}` a link to a chapter. Data fetchers for the maps and
series live in `tools/` (`fetch-sst.py`, `build-koppen.py`, `build-maps.py`).

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`: lint → build the service
worker → tests → publish to GitHub Pages. A weekly workflow re-checks links.

## Licences

App code and original text © Bryan Woo. The app icon is used under a paid
Flaticon licence. Coastlines and borders: Natural Earth (public domain).
Köppen–Geiger: Beck et al. 2023 (CC0). ECMWF open data and Open-Meteo: CC BY 4.0.
NOAA data: US Government work. Other data remain their providers'; see each
data card.
