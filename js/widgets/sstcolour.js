/* Shared colour scales for the ocean maps. */
const mix = (a, b, t) => a.map((v, i) => Math.round(v + (b[i] - v) * t));
const rgb = c => `rgb(${c.join(',')})`;

// Sea-surface temperature 0–32 °C: deep blue → pale → orange-red.
export function sstColour(v) {
  v = Math.round(v * 2) / 2;   // 0.5 °C steps: few distinct colours, so few paths
  const stops = [[0, [40, 70, 160]], [15, [110, 170, 220]], [24, [245, 230, 170]], [28, [240, 150, 80]], [32, [190, 40, 40]]];
  for (let i = 1; i < stops.length; i++) if (v <= stops[i][0]) {
    const [a, ca] = stops[i - 1], [b, cb] = stops[i];
    return rgb(mix(ca, cb, Math.max(0, (v - a) / (b - a))));
  }
  return rgb(stops[stops.length - 1][1]);
}

// Anomaly −3…+3 °C: blue – white – red.
export function anomColour(v) {
  v = Math.round(v * 4) / 4;
  const t = Math.max(-1, Math.min(1, v / 3));
  return t < 0 ? rgb(mix([255, 255, 255], [40, 90, 200], -t)) : rgb(mix([255, 255, 255], [210, 45, 40], t));
}

export function legendBar(stops, label) {
  return `linear-gradient(to right, ${stops.join(',')})`;
}
