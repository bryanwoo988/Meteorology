import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  cToF, fToC, satVapPres, dewPoint, relHum, wetBulbStull, lclHeight, stdAtmos,
  pressureToHeight, moistLapse, parcelProfile, cape, dayLength, noonElevation,
  geostrophicWind, dbzToRain, et0, lorenzEnsemble,
} from '../js/physics.js';

const eq = (a, b, tol) => assert.ok(Math.abs(a - b) <= tol, `${a} not within ${tol} of ${b}`);

test('°C/°F', () => { eq(cToF(100), 212, 1e-9); eq(fToC(-40), -40, 1e-9); });
test('saturation vapour pressure', () => eq(satVapPres(20), 23.37, 0.05));
test('dew point', () => eq(dewPoint(20, 50), 9.3, 0.1));
test('relHum inverts dewPoint', () => eq(relHum(30, dewPoint(30, 70)), 70, 0.01));
test('Stull wet bulb paper example', () => eq(wetBulbStull(20, 50), 13.7, 0.1));
test('returns null outside validity range', () => {
  assert.equal(wetBulbStull(20, 2), null);
  assert.equal(wetBulbStull(60, 50), null);
  assert.equal(dewPoint(20, 0), null);
  assert.equal(stdAtmos(-10), null);
  assert.equal(geostrophicWind(1, 2), null);
});
test('LCL', () => eq(lclHeight(30, 24), 750, 1));
test('standard atmosphere', () => { const s = stdAtmos(0); eq(s.tC, 15, 1e-6); eq(s.pHpa, 1013.25, 0.01); });
test('pressure levels', () => {
  eq(pressureToHeight(850), 1457, 15); eq(pressureToHeight(500), 5574, 20); eq(pressureToHeight(250), 10363, 30);
});
test('moist lapse rate', () => eq(moistLapse(20, 1000), 4.3, 0.4));
test('parcel is dry adiabatic below LCL', () => {
  const p = parcelProfile(30, 20, 1000, 900);
  eq(p[0].t - p[5].t, 9.8 * (pressureToHeight(950) - pressureToHeight(1000)) / 1000, 0.6);
});
test('CAPE zero when parcel equals environment', () => {
  const p = parcelProfile(30, 24, 1000, 200);
  assert.equal(cape(p, p), 0);
});
test('CAPE positive for warm moist parcel in standard env', () => {
  const p = parcelProfile(32, 26, 1000, 200);
  const env = p.map(({ p: pp }) => ({ p: pp, t: stdAtmos(pressureToHeight(pp)).tC }));
  assert.ok(cape(env, p) > 500);
});
test('day length', () => { eq(dayLength(0, 80), 12, 0.15); eq(dayLength(0, 172), 12.1, 0.15); eq(dayLength(60, 172), 18.8, 0.3); });
test('noon elevation at equinox on equator', () => eq(noonElevation(0, 80), 90, 1));
test('geostrophic wind', () => eq(geostrophicWind(1, 45), 8.1, 0.2));
test('Marshall-Palmer', () => eq(dbzToRain(40), 11.5, 0.3));
test('FAO-56 example 18', () => eq(et0(21.5, 12.3, 84, 63, 2.078, 9.25, 50.8, 100, 187), 3.9, 0.15));
test('Lorenz ensemble is deterministic and diverges', () => {
  const a = lorenzEnsemble(51, 1500, 1e-3, 7), b = lorenzEnsemble(51, 1500, 1e-3, 7);
  assert.deepEqual(a, b);
  const spread = k => Math.max(...a.map(m => m[k])) - Math.min(...a.map(m => m[k]));
  assert.ok(spread(10) < 0.1 && spread(1499) > 5);
});
