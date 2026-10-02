import { test } from 'node:test';
import assert from 'node:assert/strict';
import { equalEarth, orthographic, limbPoint, equirect } from '../js/projections.js';

const near = (a, b, tol = 1e-9) => assert.ok(Math.abs(a - b) <= tol, `${a} vs ${b}`);

test('Equal Earth: origin maps to origin', () => {
  const [x, y] = equalEarth([0, 0]); near(x, 0); near(y, 0);
});
test('Equal Earth: symmetric in longitude and latitude', () => {
  const [x1, y1] = equalEarth([100, 30]), [x2, y2] = equalEarth([-100, -30]);
  near(x1, -x2); near(y1, -y2);
});
test('Equal Earth: the equator is wider than the 60th parallel', () => {
  assert.ok(equalEarth([180, 0])[0] > equalEarth([180, 60])[0]);
});
test('orthographic: centre maps to origin, far side is hidden', () => {
  const [x, y] = orthographic([0, 0], [0, 0]); near(x, 0); near(y, 0);
  assert.equal(orthographic([180, 0], [0, 0]), null);
});
test('orthographic: a point 90° east of centre lies on the limb', () => {
  const [x, y] = orthographic([90, 0], [0, 0]); near(Math.hypot(x, y), 1, 1e-9);
});
test('limbPoint pushes far-side points onto the horizon circle', () => {
  const [x, y] = limbPoint([150, 10], [0, 0]); near(Math.hypot(x, y), 1, 1e-9);
  const [a, b] = limbPoint([10, 5], [0, 0]); assert.ok(Math.hypot(a, b) < 1);
});
test('equirect scales longitude by cos(lat0)', () => {
  const [x, y] = equirect([110, 5], [100, 0]); near(x, 10); near(y, 5);
  near(equirect([110, 0], [100, 60])[0], 5, 1e-9);
});

import { clipRingToGlobe } from '../js/projections.js';

const square = (lon, lat, d) => [[lon - d, lat - d], [lon + d, lat - d], [lon + d, lat + d], [lon - d, lat + d], [lon - d, lat - d]];

test('globe clip: a ring on the near side is kept whole', () => {
  const out = clipRingToGlobe(square(100, 5, 5), [100, 5]);
  assert.equal(out.length, 5);
  for (const [x, y] of out) assert.ok(Math.hypot(x, y) < 1);
});
test('globe clip: a ring on the far side disappears', () => {
  assert.equal(clipRingToGlobe(square(-80, -5, 5), [100, 5]), null);
});
test('globe clip: a ring across the horizon is cut along the limb', () => {
  const out = clipRingToGlobe(square(190, 0, 20), [100, 0]);   // spans the limb at 190°
  assert.ok(out && out.length >= 4);
  for (const [x, y] of out) assert.ok(Math.hypot(x, y) <= 1 + 1e-9);
  assert.ok(out.some(([x, y]) => Math.abs(Math.hypot(x, y) - 1) < 1e-6), 'no point on the limb');
});
test('globe clip: the limb arc takes the short way round', () => {
  const out = clipRingToGlobe(square(190, 0, 20), [100, 0]);
  // Everything of this ring that is visible lies on the eastern edge (x > 0).
  for (const [x] of out) assert.ok(x > 0.3, `point at x=${x} is on the wrong side`);
});
