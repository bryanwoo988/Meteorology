/* Meteorology as pure functions.

   Every interactive figure computes from here, so this is the one module
   where a wrong number would quietly teach something false. Each function
   names its source; tests/physics.test.js pins each against a published
   value. Functions return null outside the range their formula is valid
   for — the widgets show "—" rather than a confident wrong answer. */

const G = 9.80665;          // m s-2
const RD = 287.04;          // J kg-1 K-1, dry air
const CP = 1004;            // J kg-1 K-1
const LV = 2.501e6;         // J kg-1, latent heat of vaporisation
const EPS = 0.622;          // Rd / Rv
const K0 = 273.15;
const RAD = Math.PI / 180;

const finite = (...xs) => xs.every(Number.isFinite);

/* --- Units --- */

export const cToF = c => c * 9 / 5 + 32;
export const fToC = f => (f - 32) * 5 / 9;

/* --- Humidity --- */

// Magnus formula, coefficients of Alduchov & Eskridge (1996). hPa.
export function satVapPres(tC) {
  if (!finite(tC) || tC < -80 || tC > 60) return null;
  return 6.1094 * Math.exp(17.625 * tC / (tC + 243.04));
}

// Inverse of the Magnus formula for e = rh% of saturation.
export function dewPoint(tC, rh) {
  if (!finite(tC, rh) || rh <= 0 || rh > 100 || satVapPres(tC) === null) return null;
  const g = Math.log(rh / 100) + 17.625 * tC / (243.04 + tC);
  return 243.04 * g / (17.625 - g);
}

export function relHum(tC, tdC) {
  const es = satVapPres(tC), e = satVapPres(tdC);
  if (es === null || e === null || tdC > tC) return null;
  return 100 * e / es;
}

// Stull (2011), J. Appl. Meteor. Climatol. 50, 2267–2269. Valid for
// RH 5–99 % and T −20…50 °C at sea-level pressure.
export function wetBulbStull(tC, rh) {
  if (!finite(tC, rh) || rh < 5 || rh > 99 || tC < -20 || tC > 50) return null;
  return tC * Math.atan(0.151977 * Math.sqrt(rh + 8.313659))
    + Math.atan(tC + rh) - Math.atan(rh - 1.676331)
    + 0.00391838 * rh ** 1.5 * Math.atan(0.023101 * rh) - 4.686035;
}

// Espy's rule of thumb: the cloud base rises about 125 m per °C of
// temperature–dew point spread.
export function lclHeight(tC, tdC) {
  if (!finite(tC, tdC) || tdC > tC) return null;
  return 125 * (tC - tdC);
}

/* --- Standard atmosphere (ICAO), 0–20 km --- */

const P0 = 1013.25, T0 = 288.15, LAPSE = 0.0065, P11 = 226.32, T11 = 216.65;
const EXP = G / (RD * LAPSE);            // ≈ 5.256
const H11 = RD * T11 / G;                // scale height of the isothermal layer, m

export function stdAtmos(zM) {
  if (!finite(zM) || zM < 0 || zM > 20000) return null;
  if (zM <= 11000) {
    const tK = T0 - LAPSE * zM;
    return { tC: tK - K0, pHpa: P0 * (tK / T0) ** EXP };
  }
  return { tC: T11 - K0, pHpa: P11 * Math.exp(-(zM - 11000) / H11) };
}

export function pressureToHeight(pHpa) {
  if (!finite(pHpa) || pHpa <= 0 || pHpa > P0 + 60) return null;
  if (pHpa >= P11) return (T0 / LAPSE) * (1 - (pHpa / P0) ** (1 / EXP));
  return 11000 + H11 * Math.log(P11 / pHpa);
}

/* --- Parcel theory --- */

const mixingRatio = (eHpa, pHpa) => EPS * eHpa / (pHpa - eHpa);

// Saturated (pseudo-)adiabatic lapse rate, K/km (AMS Glossary form).
export function moistLapse(tC, pHpa) {
  const es = satVapPres(tC);
  if (es === null || !finite(pHpa) || pHpa <= es) return null;
  const tK = tC + K0, r = mixingRatio(es, pHpa);
  const num = G * (1 + LV * r / (RD * tK));
  const den = CP + LV * LV * r * EPS / (RD * tK * tK);
  return 1000 * num / den;
}

// A surface parcel lifted from pSurf to pTop: dry adiabatic (conserving
// potential temperature) until saturated, then moist adiabatic.
export function parcelProfile(tC, tdC, pSurf, pTop, dp = 10) {
  const e0 = satVapPres(tdC);
  if (e0 === null || !finite(tC, pSurf, pTop) || tdC > tC || pTop >= pSurf) return [];
  const r = mixingRatio(e0, pSurf);
  const theta = (tC + K0) * (1000 / pSurf) ** (RD / CP);
  const out = [{ p: pSurf, t: tC }];
  let t = tC, saturated = false;
  for (let p = pSurf - dp; p >= pTop - 1e-9; p -= dp) {
    const prev = out[out.length - 1];
    if (!saturated) {
      t = theta * (p / 1000) ** (RD / CP) - K0;
      const eParcel = r * p / (EPS + r);
      if (satVapPres(t) <= eParcel) saturated = true;
    } else {
      const dz = (RD * (prev.t + K0) / G) * Math.log(prev.p / p);
      t = prev.t - (moistLapse(prev.t, prev.p) ?? 9.8) * dz / 1000;
    }
    out.push({ p: Math.round(p * 1e6) / 1e6, t });
  }
  return out;
}

// Convective available potential energy, J/kg: the buoyant area where the
// parcel is warmer than its surroundings. Both profiles share p levels.
export function cape(env, parcel) {
  let sum = 0;
  for (let i = 1; i < Math.min(env.length, parcel.length); i++) {
    const b = (parcel[i].t - env[i].t) / (env[i].t + K0);
    if (b <= 0) continue;
    const dz = (RD * (env[i].t + K0) / G) * Math.log(env[i - 1].p / env[i].p);
    sum += G * b * dz;
  }
  return sum;
}

/* --- Sun --- */

const declination = doy => 23.44 * Math.sin(2 * Math.PI * (284 + doy) / 365);  // Cooper (1969), degrees

// Sunrise to sunset with the Sun's centre at −0.833° (refraction + radius),
// the convention almanacs use.
export function dayLength(latDeg, doy) {
  if (!finite(latDeg, doy) || Math.abs(latDeg) > 90) return null;
  const phi = latDeg * RAD, d = declination(doy) * RAD;
  const cosH = (Math.sin(-0.833 * RAD) - Math.sin(phi) * Math.sin(d)) / (Math.cos(phi) * Math.cos(d));
  if (cosH <= -1) return 24;
  if (cosH >= 1) return 0;
  return 2 * Math.acos(cosH) / RAD / 15;
}

export function noonElevation(latDeg, doy) {
  if (!finite(latDeg, doy) || Math.abs(latDeg) > 90) return null;
  return 90 - Math.abs(latDeg - declination(doy));
}

/* --- Wind --- */

// Geostrophic balance, V = (1/ρf) ∂p/∂n, ρ = 1.2 kg m-3. Undefined near the
// equator, where the Coriolis parameter vanishes.
export function geostrophicWind(dpHpaPer100km, latDeg) {
  if (!finite(dpHpaPer100km, latDeg) || Math.abs(latDeg) < 5 || Math.abs(latDeg) > 90) return null;
  const f = 2 * 7.2921e-5 * Math.sin(Math.abs(latDeg) * RAD);
  return (dpHpaPer100km * 100 / 1e5) / (1.2 * f);
}

/* --- Radar --- */

// Marshall & Palmer (1948): Z = 200 R^1.6, Z in mm6 m-3, R in mm/h.
export function dbzToRain(dbz) {
  if (!finite(dbz)) return null;
  return (10 ** (dbz / 10) / 200) ** (1 / 1.6);
}

/* --- Evapotranspiration --- */

// FAO Irrigation and Drainage Paper 56, daily reference ET0 (eq. 6), with
// solar radiation from sunshine hours by the Ångström formula (a=0.25, b=0.50).
export function et0(tmax, tmin, rhmax, rhmin, u2, sunH, latDeg, elevM, doy) {
  if (!finite(tmax, tmin, rhmax, rhmin, u2, sunH, latDeg, elevM, doy)) return null;
  if (tmin > tmax || rhmin > rhmax || rhmin < 0 || rhmax > 100 || u2 < 0 || sunH < 0 || Math.abs(latDeg) > 66) return null;
  const e0 = t => 0.6108 * Math.exp(17.27 * t / (t + 237.3));
  const t = (tmax + tmin) / 2;
  const P = 101.3 * ((293 - 0.0065 * elevM) / 293) ** 5.26;
  const gamma = 0.665e-3 * P;
  const delta = 4098 * e0(t) / (t + 237.3) ** 2;
  const es = (e0(tmax) + e0(tmin)) / 2;
  const ea = (e0(tmin) * rhmax / 100 + e0(tmax) * rhmin / 100) / 2;
  const phi = latDeg * RAD;
  const dr = 1 + 0.033 * Math.cos(2 * Math.PI * doy / 365);
  const dec = 0.409 * Math.sin(2 * Math.PI * doy / 365 - 1.39);
  const ws = Math.acos(-Math.tan(phi) * Math.tan(dec));
  const Ra = 24 * 60 / Math.PI * 0.0820 * dr * (ws * Math.sin(phi) * Math.sin(dec) + Math.cos(phi) * Math.cos(dec) * Math.sin(ws));
  const N = 24 * ws / Math.PI;
  const Rs = (0.25 + 0.5 * Math.min(sunH, N) / N) * Ra;
  const Rso = (0.75 + 2e-5 * elevM) * Ra;
  const Rnl = 4.903e-9 * ((tmax + 273.16) ** 4 + (tmin + 273.16) ** 4) / 2
    * (0.34 - 0.14 * Math.sqrt(ea)) * (1.35 * Math.min(Rs / Rso, 1) - 0.35);
  const Rn = 0.77 * Rs - Rnl;
  return (0.408 * delta * Rn + gamma * 900 / (t + 273) * u2 * (es - ea)) / (delta + gamma * (1 + 0.34 * u2));
}

/* --- Chaos demonstration --- */

// Lorenz (1963) system, σ=10 ρ=28 β=8/3, RK4 with dt=0.01. Member 0 is the
// control; the others start within ±eps of it. Returns each member's x.
export function lorenzEnsemble(n, steps, eps, seed) {
  let s = seed >>> 0;
  const rand = () => {                      // mulberry32
    s = (s + 0x6D2B79F5) >>> 0;
    let x = Math.imul(s ^ (s >>> 15), 1 | s);
    x = (x + Math.imul(x ^ (x >>> 7), 61 | x)) ^ x;
    return ((x ^ (x >>> 14)) >>> 0) / 4294967296;
  };
  const f = ([x, y, z]) => [10 * (y - x), x * (28 - z) - y, x * y - (8 / 3) * z];
  const add = (a, b, k) => a.map((v, i) => v + b[i] * k);
  const dt = 0.01;
  const out = [];
  for (let m = 0; m < n; m++) {
    let v = m === 0 ? [1, 1, 20] : [1 + eps * (2 * rand() - 1), 1 + eps * (2 * rand() - 1), 20 + eps * (2 * rand() - 1)];
    const xs = new Array(steps);
    for (let k = 0; k < steps; k++) {
      xs[k] = v[0];
      const k1 = f(v), k2 = f(add(v, k1, dt / 2)), k3 = f(add(v, k2, dt / 2)), k4 = f(add(v, k3, dt));
      v = v.map((val, i) => val + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]));
    }
    out.push(xs);
  }
  return out;
}
