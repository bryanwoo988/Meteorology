/* Base maps and the layers drawn on them.

   Three kinds: 'world' (Equal Earth), 'seasia' (South-East Asia, plate
   carrée), 'globe' (orthographic, turned by dragging). Coastlines and
   borders come from Natural Earth (public domain) via tools/build-maps.py
   and are precached, so every map works offline.

   Layers are plain data in geographic coordinates and are re-projected on
   every redraw, which is what lets the globe turn:
     { type: 'regions', items: [{ ring: [[lon,lat]…], fill: 'sun', label, id }] }
     { type: 'arrows',  items: [{ from: [lon,lat], to: [lon,lat], color }] }
     { type: 'lines',   items: [{ pts: [[lon,lat]…], color, dash }] }
     { type: 'points',  items: [{ at: [lon,lat], label, id, color }] }
     { type: 'circles', items: [{ at: [lon,lat], km, color, id }] }
     { type: 'grid',    lon0, lat0, dlon, dlat, nx, ny, values, colour(v) → css }
   onPick(id) is called when a region, point or circle with an id is tapped. */

import { equalEarth, orthographic, equirect, clipRingToGlobe } from './projections.js';
import { loadData } from './content.js';
import { s, h, clamp } from './widgets/kit.js';

const EE_X = 2.7066, EE_Y = 1.3173;   // Equal Earth extent on the unit sphere

function projector(kind, W, state) {
  if (kind === 'world') {
    const k = W / (2 * EE_X), H = Math.round(2 * EE_Y * k);
    const f = ll => { const [x, y] = equalEarth(ll); return [W / 2 + x * k, H / 2 - y * k]; };
    return { H, fwd: f, ring: r => r.map(f) };
  }
  if (kind === 'seasia') {
    const [x0, y0, x1, y1] = state.bbox, mid = [(x0 + x1) / 2, (y0 + y1) / 2];
    const sx = W / ((x1 - x0) * Math.cos(mid[1] * Math.PI / 180));
    const H = Math.round((y1 - y0) * sx);
    const f = ll => { const [x, y] = equirect(ll, mid); return [W / 2 + x * sx, H / 2 - (y - mid[1]) * sx]; };
    return { H, fwd: f, ring: r => r.map(f) };
  }
  const r = W / 2 - 2, H = W;
  const place = p => (p ? [W / 2 + p[0] * r, H / 2 - p[1] * r] : null);
  return {
    H, r,
    fwd: ll => place(orthographic(ll, state.centre)),
    ring: ring => { const c = clipRingToGlobe(ring, state.centre); return c ? c.map(place) : null; },
  };
}

const path = (pts, close) => pts.map((p, i) => `${i ? 'L' : 'M'}${p[0].toFixed(1)},${p[1].toFixed(1)}`).join('') + (close ? 'Z' : '');

// Split a line wherever it goes behind the globe, so it is not drawn across the disc.
function visibleRuns(pts, fwd) {
  const runs = [];
  let cur = [];
  for (const ll of pts) {
    const p = fwd(ll);
    if (p) cur.push(p);
    else if (cur.length) { runs.push(cur); cur = []; }
  }
  if (cur.length) runs.push(cur);
  return runs.filter(r => r.length > 1);
}

export async function baseMap(kind, { width, bbox, centre = [105, 5], onPick, label } = {}) {
  const geo = await loadData(`maps/${kind === 'seasia' ? 'seasia' : 'world'}`);
  const state = { bbox: bbox ?? geo.bbox ?? [85, -15, 135, 28], centre: [...centre] };
  const layers = [];
  const W = Math.round(width ?? 640);
  const svg = s('svg', { class: `map map-${kind}`, role: 'img', 'aria-label': label ?? '' });
  const el = h('div', { class: 'map-wrap' }, svg);

  function draw() {
    const P = projector(kind, W, state);
    svg.setAttribute('viewBox', `0 0 ${W} ${P.H}`);
    svg.replaceChildren();
    if (kind === 'globe') svg.append(s('circle', { cx: W / 2, cy: P.H / 2, r: P.r, class: 'map-sea' }));
    else svg.append(s('rect', { x: 0, y: 0, width: W, height: P.H, class: 'map-sea' }));

    // Graticule: every 30° on world and globe, every 5° regionally.
    const g = s('g', { class: 'map-grat' });
    const step = kind === 'seasia' ? 5 : 30;
    const [lx0, ly0, lx1, ly1] = kind === 'seasia' ? state.bbox : [-180, -90, 180, 90];
    for (let lon = Math.ceil(lx0 / step) * step; lon <= lx1; lon += step) {
      const pts = []; for (let lat = ly0; lat <= ly1; lat += 2) pts.push([lon, lat]);
      for (const run of visibleRuns(pts, P.fwd)) g.append(s('path', { d: path(run) }));
    }
    for (let lat = Math.ceil(ly0 / step) * step; lat <= ly1; lat += step) {
      const pts = []; for (let lon = lx0; lon <= lx1; lon += 2) pts.push([lon, lat]);
      for (const run of visibleRuns(pts, P.fwd)) g.append(s('path', { d: path(run), class: lat === 0 ? 'equator' : null }));
    }
    svg.append(g);

    const land = s('g', { class: 'map-land' });
    for (const ring of geo.land) {
      const pts = P.ring(ring);
      if (pts) land.append(s('path', { d: path(pts, true) }));
    }
    svg.append(land);
    const borders = s('g', { class: 'map-borders' });
    for (const line of geo.borders) for (const run of visibleRuns(line, P.fwd)) borders.append(s('path', { d: path(run) }));
    svg.append(borders);

    for (const layer of layers) svg.append(drawLayer(layer, P));
    if (kind === 'globe') svg.append(s('circle', { cx: W / 2, cy: P.H / 2, r: P.r, class: 'map-limb' }));
  }

  function drawLayer(layer, P) {
    const g = s('g', { class: `map-layer map-${layer.type}` });
    const pick = (node, id) => { if (id && onPick) { node.classList.add('is-pickable'); node.addEventListener('click', () => onPick(id)); node.setAttribute('tabindex', '0'); node.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onPick(id); } }); } };
    for (const it of layer.items ?? []) {
      if (layer.type === 'regions') {
        const pts = P.ring(it.ring);
        if (!pts) continue;
        const n = s('path', { d: path(pts, true), style: `fill: var(--${it.fill ?? 'sun'}); fill-opacity: ${it.opacity ?? 0.35}; stroke: var(--${it.fill ?? 'sun'})`, 'data-id': it.id ?? null });
        pick(n, it.id); g.append(n);
      } else if (layer.type === 'lines') {
        for (const run of visibleRuns(it.pts, P.fwd)) g.append(s('path', { d: path(run), style: `stroke: var(--${it.color ?? 'ink-2'})`, 'stroke-dasharray': it.dash ?? null }));
      } else if (layer.type === 'arrows') {
        const a = P.fwd(it.from), b = P.fwd(it.to);
        if (!a || !b) continue;
        const ang = Math.atan2(b[1] - a[1], b[0] - a[0]), hl = 7;
        const head = [[b[0] - hl * Math.cos(ang - 0.45), b[1] - hl * Math.sin(ang - 0.45)], b, [b[0] - hl * Math.cos(ang + 0.45), b[1] - hl * Math.sin(ang + 0.45)]];
        g.append(s('path', { d: path([a, b]) + path(head), style: `stroke: var(--${it.color ?? 'sky'})` }));
      } else if (layer.type === 'points') {
        const p = P.fwd(it.at);
        if (!p) continue;
        const n = s('g', { 'data-id': it.id ?? null }, s('circle', { cx: p[0], cy: p[1], r: it.r ?? 4.5, style: `fill: var(--${it.color ?? 'mercury'})` }),
          it.label ? s('text', { x: p[0] + 7, y: p[1] + 4 }, it.label) : null);
        pick(n, it.id); g.append(n);
      } else if (layer.type === 'circles') {
        // A circle of `km` radius drawn as a ring of geographic points, so it bends correctly on every projection.
        const [lon, lat] = it.at, d = it.km / 111.2, pts = [];
        for (let a = 0; a <= 360; a += 6) pts.push([lon + d * Math.cos(a * Math.PI / 180) / Math.cos(lat * Math.PI / 180), lat + d * Math.sin(a * Math.PI / 180)]);
        const ring = P.ring(pts);
        if (!ring) continue;
        const n = s('path', { d: path(ring, true), style: `stroke: var(--${it.color ?? 'sky'}); fill: var(--${it.color ?? 'sky'}); fill-opacity: .12`, 'data-id': it.id ?? null });
        pick(n, it.id); g.append(n);
      }
    }
    if (layer.type === 'grid') {
      for (let j = 0; j < layer.ny; j++) for (let i = 0; i < layer.nx; i++) {
        const v = layer.values[j * layer.nx + i];
        if (v == null) continue;
        const lo = layer.lon0 + i * layer.dlon, la = layer.lat0 + j * layer.dlat;
        const ring = [[lo, la], [lo + layer.dlon, la], [lo + layer.dlon, la + layer.dlat], [lo, la + layer.dlat]];
        const pts = P.ring(ring);
        if (pts) g.append(s('path', { d: path(pts, true), style: `fill: ${layer.colour(v)}` }));
      }
    }
    if (layer.type === 'labels') for (const it of layer.items) {
      const p = P.fwd(it.at); if (p) g.append(s('text', { x: p[0], y: p[1], 'text-anchor': it.anchor ?? 'middle', class: it.cls ?? null }, it.text));
    }
    return g;
  }

  // Dragging the globe turns it; nothing moves on its own.
  if (kind === 'globe') {
    let start = null;
    svg.style.touchAction = 'none';
    svg.addEventListener('pointerdown', e => { start = { x: e.clientX, y: e.clientY, c: [...state.centre] }; svg.setPointerCapture(e.pointerId); });
    svg.addEventListener('pointermove', e => {
      if (!start) return;
      const k = 180 / (svg.getBoundingClientRect().width || W);
      state.centre = [start.c[0] - (e.clientX - start.x) * k, clamp(start.c[1] + (e.clientY - start.y) * k, -80, 80)];
      draw();
    });
    const end = () => { start = null; };
    svg.addEventListener('pointerup', end); svg.addEventListener('pointercancel', end);
  }

  draw();
  return {
    el, svg,
    project: ll => projector(kind, W, state).fwd(ll),
    addLayer(layer) { layers.push(layer); draw(); return layer; },
    setLayers(next) { layers.splice(0, layers.length, ...next); draw(); },
    centre: () => [...state.centre],
    rotateTo(c) { state.centre = [...c]; draw(); },
    redraw: draw,
    source: geo.source,
  };
}
