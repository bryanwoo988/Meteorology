/* Map projections, pure. Input [lon, lat] in degrees.

   equalEarth   — world maps. Šavrič, Patterson & Jenny (2018): areas are
                  true, so the tropics are not shrunk the way Mercator
                  shrinks them. y grows northward.
   orthographic — the globe, seen from above [lon0, lat0]; null on the far side.
   limbPoint    — as orthographic, but far-side points are pushed onto the
                  horizon, so a filled coastline that wraps round the back
                  hugs the edge of the disc instead of tearing.
   equirect     — regional maps: degrees, with longitude shortened by cos(lat0). */

const R = Math.PI / 180;
const A1 = 1.340264, A2 = -0.081106, A3 = 0.000893, A4 = 0.003796, M = Math.sqrt(3) / 2;

export function equalEarth([lon, lat]) {
  const l = lon * R, th = Math.asin(M * Math.sin(lat * R));
  const t2 = th * th, t6 = t2 * t2 * t2;
  const x = (2 * Math.sqrt(3) * l * Math.cos(th)) / (3 * (9 * A4 * t6 * t2 + 7 * A3 * t6 + 3 * A2 * t2 + A1));
  const y = th * (A1 + A2 * t2 + t6 * (A3 + A4 * t2));
  return [x, y];
}

function ortho([lon, lat], [lon0, lat0]) {
  const l = (lon - lon0) * R, p = lat * R, p0 = lat0 * R;
  const cosc = Math.sin(p0) * Math.sin(p) + Math.cos(p0) * Math.cos(p) * Math.cos(l);
  return { x: Math.cos(p) * Math.sin(l), y: Math.cos(p0) * Math.sin(p) - Math.sin(p0) * Math.cos(p) * Math.cos(l), cosc };
}

export function orthographic(pt, centre) {
  const { x, y, cosc } = ortho(pt, centre);
  return cosc < 0 ? null : [x, y];
}

export function limbPoint(pt, centre) {
  const { x, y, cosc } = ortho(pt, centre);
  if (cosc >= 0) return [x, y];
  const r = Math.hypot(x, y) || 1;
  return [x / r, y / r];
}

export function equirect([lon, lat], [lon0, lat0]) {
  return [(lon - lon0) * Math.cos(lat0 * R), lat];
}

/* Clip a closed ring to the visible hemisphere of the globe and return it
   in orthographic unit coordinates, or null if none of it is visible.
   Sutherland–Hodgman against the horizon plane in 3-D; where the ring goes
   out of sight and comes back, the gap is closed along the limb (the
   shorter way round), so land that wraps behind the globe is drawn as a
   clean edge instead of a chord across the disc. */
const vec = ([lon, lat]) => {
  const l = lon * R, p = lat * R;
  return [Math.cos(p) * Math.cos(l), Math.cos(p) * Math.sin(l), Math.sin(p)];
};
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

export function clipRingToGlobe(ring, [lon0, lat0]) {
  const c = vec([lon0, lat0]);
  const l0 = lon0 * R, p0 = lat0 * R;
  const east = [-Math.sin(l0), Math.cos(l0), 0];
  const north = [-Math.sin(p0) * Math.cos(l0), -Math.sin(p0) * Math.sin(l0), Math.cos(p0)];
  const screen = v => [dot(v, east), dot(v, north)];
  const pts = ring.map(vec);
  if (pts.every(v => dot(v, c) < 0)) return null;
  if (pts.every(v => dot(v, c) >= 0)) return pts.map(screen);

  const out = [];          // { xy, edge: 'exit' | 'entry' | undefined }
  for (let i = 0; i < pts.length; i++) {
    const a = pts[i], b = pts[(i + 1) % pts.length];
    const da = dot(a, c), db = dot(b, c);
    const cross = () => {
      const t = da / (da - db);
      const v = a.map((x, k) => x + t * (b[k] - x));
      const n = Math.hypot(...v) || 1;
      const xy = screen(v.map(x => x / n));
      const r = Math.hypot(...xy) || 1;
      return [xy[0] / r, xy[1] / r];
    };
    if (da >= 0 && db >= 0) out.push({ xy: screen(b) });
    else if (da >= 0 && db < 0) out.push({ xy: cross(), edge: 'exit' });
    else if (da < 0 && db >= 0) { out.push({ xy: cross(), edge: 'entry' }); out.push({ xy: screen(b) }); }
  }

  const res = [];
  for (let i = 0; i < out.length; i++) {
    res.push(out[i].xy);
    if (out[i].edge !== 'exit') continue;
    const next = out.slice(i + 1).concat(out.slice(0, i + 1)).find(o => o.edge === 'entry');
    if (!next) continue;
    let a0 = Math.atan2(out[i].xy[1], out[i].xy[0]);
    let a1 = Math.atan2(next.xy[1], next.xy[0]);
    let d = a1 - a0;
    while (d > Math.PI) d -= 2 * Math.PI;
    while (d < -Math.PI) d += 2 * Math.PI;
    const steps = Math.max(1, Math.ceil(Math.abs(d) / (5 * R)));
    for (let k = 1; k < steps; k++) { const a = a0 + d * k / steps; res.push([Math.cos(a), Math.sin(a)]); }
  }
  return res.length >= 3 ? res : null;
}
