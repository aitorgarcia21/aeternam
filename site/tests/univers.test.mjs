import test from 'node:test';
import assert from 'node:assert/strict';
import {CRITICAL_IMPACT, movingClockRatio, stationaryClockRatio, traceLight} from '../univers-physique.mjs';

test('Horloges : cas analytiques indépendants et limites physiques', () => {
  assert.equal(movingClockRatio(0), 1);
  assert.ok(Math.abs(movingClockRatio(.8) - .6) < 1e-14);
  assert.equal(movingClockRatio(-.8), movingClockRatio(.8));
  assert.equal(stationaryClockRatio(4 / 3), .5);
  assert.ok(stationaryClockRatio(1e12) > .99999999999);
  for (const value of [1, -1, 2, NaN, Infinity]) assert.throws(() => movingClockRatio(value), RangeError);
  for (const value of [0, 1, -2, NaN, Infinity]) assert.throws(() => stationaryClockRatio(value), RangeError);
});

test('Capture et échappement de part et d’autre du seuil théorique', () => {
  assert.equal(traceLight(CRITICAL_IMPACT - .001).captured, true);
  assert.equal(traceLight(CRITICAL_IMPACT + .001).escaped, true);
  const capture = traceLight(2);
  const last = capture.points.at(-1);
  assert.ok(Math.abs(Math.hypot(...last) - 1) < 1e-12);
  assert.equal(capture.closest, 1);
});

test('La déviation rejoint la limite de champ faible 2 rₛ/b', () => {
  const weak = traceLight(100);
  assert.equal(weak.escaped, true);
  assert.ok(Math.abs(weak.deflection / .02 - 1) < .02);
});

test('La géodésique converge quand on raffine le pas', () => {
  for (const b of [2.61, 3, 4, 7]) {
    const coarse = traceLight(b, .008);
    const fine = traceLight(b, .002);
    assert.equal(coarse.captured, fine.captured);
    assert.ok(Math.abs(coarse.deflection - fine.deflection) < 1e-5);
    const radius = fine.closest;
    // Le point de rebroussement vérifie b² = r³/(r−1).
    assert.ok(Math.abs(radius ** 3 / (radius - 1) / b ** 2 - 1) < 1e-5);
  }
});

test('La plage du curseur ne produit ni NaN ni trajectoire vide', () => {
  for (let b = 1.8; b <= 7; b += .13) {
    const result = traceLight(b);
    assert.ok(result.points.length > 10);
    assert.ok(result.points.every(point => point.every(Number.isFinite)));
    assert.ok(result.captured || result.escaped);
  }
});
