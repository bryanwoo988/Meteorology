/* Browser tests: each case opens the real app in an iframe at a given size
   with given saved preferences, then inspects it. Same origin, so storage
   written here is what the app reads. */

const KEY = 'meteo.prefs.v1';
const results = document.getElementById('results');
let passed = 0, failed = 0;

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function until(fn, ms = 4000) {
  const t0 = performance.now();
  for (;;) {
    try { const v = fn(); if (v) return v; } catch { /* not yet */ }
    if (performance.now() - t0 > ms) throw new Error(`timed out waiting for ${fn}`);
    await sleep(50);
  }
}

async function openApp({ hash = '', width = 375, height = 740, prefs = null }) {
  localStorage.removeItem(KEY);
  if (prefs) localStorage.setItem(KEY, JSON.stringify({ lang: 'en', theme: 'light', scale: 1, chosen: true, read: {}, quiz: {}, lastRoute: '', seenVersion: '1.0.0', ...prefs }));
  const f = document.createElement('iframe');
  f.width = width; f.height = height;
  f.src = `../index.html${hash}`;
  document.getElementById('frames').append(f);
  await new Promise(r => f.addEventListener('load', r, { once: true }));
  const w = f.contentWindow;
  await until(() => w.document.documentElement.dataset.ready === 'true');
  return { f, w, d: w.document, close: () => f.remove() };
}

async function test(name, fn) {
  const li = document.createElement('li');
  try { await fn(); li.className = 'pass'; li.textContent = `✓ ${name}`; passed++; }
  catch (e) { li.className = 'fail'; li.innerHTML = `✗ ${name}<pre>${e.stack || e}</pre>`; failed++; }
  results.append(li);
}

const assert = (c, msg) => { if (!c) throw new Error(msg); };

await test('first visit shows the language picker with English as default', async () => {
  const a = await openApp({});
  const picker = await until(() => a.d.getElementById('picker'));
  assert(!picker.hidden, 'picker hidden');
  assert(a.d.querySelector('#picker [data-lang="en"]').classList.contains('is-default'), 'English not marked default');
  a.close();
});

await test('deep link survives the language picker', async () => {
  const a = await openApp({ hash: '#/ch/ch05/s4' });
  a.d.querySelector('#picker [data-lang="zh"]').click();
  await until(() => a.d.getElementById('s4'));
  assert(a.w.location.hash === '#/ch/ch05/s4', `hash is ${a.w.location.hash}`);
  assert(a.d.documentElement.lang.startsWith('zh'), 'language not applied');
  await sleep(200);
  const top = a.d.getElementById('s4').getBoundingClientRect().top;
  assert(top > -5 && top < 160, `section s4 at ${top}px`);
  a.close();
});

await test('language button cycles and keeps the reading position', async () => {
  const a = await openApp({ hash: '#/ch/ch05/s4', prefs: { lang: 'en' } });
  await until(() => a.d.getElementById('s4'));
  await sleep(200);
  a.d.querySelector('[data-action="lang"]').click();
  await until(() => a.d.documentElement.lang === 'ms');
  await sleep(200);
  const top = a.d.getElementById('s4').getBoundingClientRect().top;
  assert(top > -5 && top < 160, `section s4 moved to ${top}px`);
  a.close();
});

await test('theme is applied by an inline script before the stylesheet', async () => {
  const html = await (await fetch('../index.html', { cache: 'no-store' })).text();
  const pre = html.indexOf('id="prepaint"'), css = html.indexOf('css/app.css');
  assert(pre > 0 && pre < css, 'prepaint script missing or after the stylesheet');
  const a = await openApp({ prefs: { theme: 'dark' } });
  assert(a.d.documentElement.dataset.theme === 'dark', 'dark theme not applied');
  a.close();
});

await test('text size 1.3 switches the chapter to a single column', async () => {
  const cols = async scale => {
    const a = await openApp({ hash: '#/ch/ch05', width: 1200, prefs: { scale } });
    await until(() => a.d.getElementById('s1'));
    const n = a.w.getComputedStyle(a.d.querySelector('.page-chapter')).gridTemplateColumns.split(' ').length;
    const single = 'single' in a.d.documentElement.dataset;
    a.close();
    return [n, single];
  };
  const [normal] = await cols(1);
  const [big, single] = await cols(1.3);
  assert(normal === 2, `scale 1 has ${normal} columns`);
  assert(single && big === 1, `scale 1.3 has ${big} columns, data-single=${single}`);
});

for (const lang of ['ms', 'zh', 'en']) {
  await test(`no horizontal overflow at 375px × scale 1.5 in ${lang}`, async () => {
    for (const hash of ['#/', '#/ch/ch05', '#/stage/3', '#/info', '#/share']) {
      const a = await openApp({ hash, prefs: { lang, scale: 1.5 } });
      await sleep(250);
      const sw = a.d.scrollingElement.scrollWidth;
      a.close();
      assert(sw <= 375, `${hash}: scrollWidth ${sw}`);
    }
  });
}

await test('share page shows a QR code, a share button and copy link', async () => {
  const a = await openApp({ hash: '#/share', prefs: { lang: 'zh' } });
  const svg = await until(() => a.d.querySelector('#share-host svg'));
  assert(svg.querySelectorAll('rect, path').length > 0, 'QR svg is empty');
  assert(a.d.querySelector('[data-share="copy"]'), 'no copy button');
  assert(a.d.querySelector('[data-share="native"]'), 'no share button');
  assert(a.d.querySelector('.share-url').textContent.includes('bryanwoo988.github.io/Meteorology/'), 'URL not shown');
  a.close();
});

await test('humidity widget never shows NaN at its extremes', async () => {
  const a = await openApp({ hash: '#/ch/ch05/s4', prefs: { lang: 'en' } });
  const fig = await until(() => a.d.querySelector('[data-widget="W5"] .w-frame'));
  const inputs = fig.querySelectorAll('input[type=range]');
  assert(inputs.length === 2, `expected 2 sliders, got ${inputs.length}`);
  for (const [t, rh] of [[0, 1], [45, 100], [45, 1], [0, 100], [33, 50]]) {
    inputs[0].value = t; inputs[0].dispatchEvent(new Event('input'));
    inputs[1].value = rh; inputs[1].dispatchEvent(new Event('input'));
    const text = fig.querySelector('.w-readout').textContent;
    assert(!/NaN|undefined|Infinity/.test(text), `T=${t} RH=${rh}: ${text}`);
  }
  inputs[0].value = 30; inputs[0].dispatchEvent(new Event('input'));
  inputs[1].value = 29; inputs[1].dispatchEvent(new Event('input'));
  assert(/10\.\d/.test(fig.querySelector('[data-k="td"]').textContent), 'dew point for 30 °C / 29 % should be about 10 °C');
  a.close();
});

await test('dragging past the plot edge clamps instead of breaking', async () => {
  const a = await openApp({ hash: '#/ch/ch05/s4', prefs: { lang: 'en' } });
  const svg = await until(() => a.d.querySelector('[data-widget="W5"] svg'));
  const r = svg.getBoundingClientRect();
  const fire = (type, x, y) => svg.dispatchEvent(new a.w.PointerEvent(type, { bubbles: true, clientX: x, clientY: y, pointerId: 1, pointerType: 'touch' }));
  fire('pointerdown', r.left + r.width / 2, r.top + r.height / 2);
  fire('pointermove', r.right + 400, r.top - 400);
  fire('pointerup', r.right + 400, r.top - 400);
  const text = svg.closest('.w-frame').querySelector('.w-readout').textContent;
  assert(!/NaN|undefined|Infinity/.test(text), text);
  a.close();
});

await test('line chart scrubs with the keyboard and updates its readout', async () => {
  const a = await openApp({ hash: '#/ch/ch05/s4', prefs: { lang: 'en' } });
  const svg = await until(() => a.d.querySelector('.chart svg'));
  const out = svg.closest('.chart').querySelector('.chart-readout');
  svg.focus();
  svg.dispatchEvent(new a.w.KeyboardEvent('keydown', { key: 'End', bubbles: true }));
  const last = out.textContent;
  svg.dispatchEvent(new a.w.KeyboardEvent('keydown', { key: 'ArrowLeft', bubbles: true }));
  assert(out.textContent && out.textContent !== last, `readout did not change: "${last}" → "${out.textContent}"`);
  assert(svg.closest('.chart').querySelector('table'), 'no data table for screen readers');
  a.close();
});

await test('base maps render: world, South-East Asia and a globe that turns', async () => {
  const { baseMap } = await import('../js/maps.js');
  const host = document.createElement('div'); host.style.width = '360px';
  document.getElementById('frames').append(host);
  for (const kind of ['world', 'seasia', 'globe']) {
    const m = await baseMap(kind, { lang: 'en', width: 340 });
    host.append(m.el);
    const land = m.el.querySelectorAll('.map-land path, path.map-land');
    assert(land.length > 0, `${kind}: no land drawn`);
    const kl = m.project([101.69, 3.14]);
    assert(kl && kl.every(Number.isFinite), `${kind}: Kuala Lumpur not projected`);
    if (kind === 'globe') {
      const before = m.centre().join(',');
      m.rotateTo([20, 10]);
      assert(m.centre().join(',') !== before, 'globe did not rotate');
      assert(m.project([101.69, 3.14]) === null || m.project([101.69, 3.14]).every(Number.isFinite), 'bad projection after rotate');
    }
  }
  host.remove();
});

await test('dataset card shows parameters, a data sample and graded outside links', async () => {
  const { renderDataset } = await import('../js/datasets.js');
  const T = en => ({ zh: `中${en}`, en, ms: `M${en}` });
  const card = renderDataset({
    id: 'sample', name: 'Sample', provider: 'Provider', what: T('what'), resolution: '9 km', update: T('daily'), format: 'GRIB2',
    licence: { text: 'CC BY 4.0', url: 'https://creativecommons.org/licenses/by/4.0/' },
    params: [{ raw: '2t', meaning: T('2 m temperature'), unit: 'K', chapter: 4 }],
    sample: { columns: ['time', '2t'], rows: [['00:00', '300.1']], source: 'src', fetched: '2026-10-02' },
    links: [{ level: 'view', label: T('Charts'), url: 'https://charts.ecmwf.int/' }, { level: 'try', label: T('Try it'), url: 'https://api.open-meteo.com/' }, { level: 'pro', label: T('Raw'), url: 'https://data.ecmwf.int/' }],
  }, { lang: 'en' });
  assert(card.querySelector('code').textContent === '2t', 'raw parameter name not shown');
  assert(card.querySelector('a[href="#/ch/ch04"]'), 'no link to the chapter that teaches it');
  assert(card.querySelectorAll('.ds-sample td').length === 2, 'sample table missing');
  const links = card.querySelectorAll('.ds-links a');
  assert(links.length === 3 && [...links].every(a => a.target === '_blank' && a.rel.includes('noopener')), 'outside links not safe');
  assert([...links].map(a => a.dataset.level).join() === 'view,try,pro', 'links not in order of difficulty');
});

document.getElementById('summary').textContent = `${passed} passed, ${failed} failed`;
document.documentElement.dataset.done = 'true';
