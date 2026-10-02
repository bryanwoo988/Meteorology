/* M9 — Köppen–Geiger climate zones, 1991–2020 (Beck et al. 2023, CC0).
   Real data at 1° (world) and 0.5° (South-East Asia). Tap a spot. */

import { baseMap } from '../maps.js';
import { loadData } from '../content.js';
import { h, clamp, frame } from './kit.js';
import { pick } from '../i18n.js';

const T = (zh, en, ms) => ({ zh, en, ms });
const L = {
  title: T('Köppen 气候分区（1991–2020）：点一个地方', 'Köppen climate zones (1991–2020): tap a place', 'Zon iklim Köppen (1991–2020): ketik satu tempat'),
  world: T('世界', 'World', 'Dunia'), seasia: T('东南亚', 'South-East Asia', 'Asia Tenggara'),
  hint: T('点地图上的一个地方看它的气候类型。', 'Tap the map to see the climate type there.', 'Ketik peta untuk melihat jenis iklim di situ.'),
};
const GROUP = {
  A: [T('热带', 'Tropical', 'Tropika'), '#2f6fe0'], B: [T('干旱', 'Arid', 'Gersang'), '#e2833a'], C: [T('温带', 'Temperate', 'Sederhana'), '#5fbf5f'],
  D: [T('冷温带', 'Cold', 'Sejuk'), '#7f6fd6'], E: [T('极地', 'Polar', 'Kutub'), '#9aa3ad'],
};
const NAME = {
  Af: T('热带雨林气候：全年湿热、没有旱季', 'Tropical rainforest: hot and wet all year, no dry season', 'Hutan hujan tropika: panas dan basah sepanjang tahun, tiada musim kering'),
  Am: T('热带季风气候：有短暂的较干季节', 'Tropical monsoon: a short drier season', 'Monsun tropika: musim kering yang singkat'),
  Aw: T('热带草原气候：有明显的旱季', 'Tropical savanna: a distinct dry season', 'Savana tropika: musim kering yang jelas'),
};

export async function mount(el, { lang }) {
  const p = v => pick(v, lang);
  const W = Math.round(clamp((el.clientWidth || 640) - 30, 280, 680));
  const d = await loadData('maps/koppen');
  const tabs = h('div', { class: 'stage-chips' }), out = h('p', { class: 'w-explain', 'aria-live': 'polite' }, p(L.hint));
  const host = h('div');
  const legend = h('ul', { class: 'chart-legend' }, Object.values(GROUP).map(([n, c]) => h('li', {}, h('span', { class: 'swatch', style: `--c: ${c}` }), p(n))));
  async function show(kind) {
    const g = d[kind], cls = c => d.classes[c.charCodeAt(0) - 48];
    const m = await baseMap(kind, { width: W, label: p(L.title), ...(kind === 'seasia' ? { bbox: [g.lon0, g.lat0, g.lon0 + g.nx * g.dlon, g.lat0 + g.ny * g.dlat] } : {}) });
    const values = [...g.cells].map(c => (cls(c) ? cls(c) : null));
    m.setLayers([{ type: 'grid', lon0: g.lon0, lat0: g.lat0, dlon: g.dlon, dlat: g.dlat, nx: g.nx, ny: g.ny, values, colour: v => GROUP[v[0]][1] },
      { type: 'points', items: [{ at: [101.69, 3.14], label: 'KL', color: 'ink', r: 3 }] }]);
    m.svg.querySelectorAll('.map-grid path').forEach(n => { n.style.fillOpacity = '0.75'; });
    m.svg.style.cursor = 'pointer';
    m.svg.addEventListener('click', e => {
      // Find the grid cell under the tap by inverting the projection numerically over the cells.
      const r = m.svg.getBoundingClientRect(), vb = m.svg.viewBox.baseVal;
      const px = (e.clientX - r.left) * vb.width / r.width, py = (e.clientY - r.top) * vb.height / r.height;
      let best = null, bd = Infinity;
      for (let j = 0; j < g.ny; j++) for (let i = 0; i < g.nx; i++) {
        const c = cls(g.cells[j * g.nx + i]); if (!c) continue;
        const q = m.project([g.lon0 + (i + 0.5) * g.dlon, g.lat0 + (j + 0.5) * g.dlat]); if (!q) continue;
        const dd = (q[0] - px) ** 2 + (q[1] - py) ** 2; if (dd < bd) { bd = dd; best = c; }
      }
      if (best) out.textContent = `${best} · ${p(GROUP[best[0]][0])}${NAME[best] ? ` — ${p(NAME[best])}` : ''}`;
    });
    host.replaceChildren(m.el);
    tabs.replaceChildren(...['seasia', 'world'].map(k => { const b = h('button', { type: 'button', class: `chip${k === kind ? ' is-on' : ''}` }, p(L[k])); b.addEventListener('click', () => show(k)); return b; }));
  }
  await show('seasia');
  el.append(frame({ title: p(L.title), lang, source: d.source, children: [tabs, host, legend, out] }));
  return { destroy() { el.replaceChildren(); } };
}
