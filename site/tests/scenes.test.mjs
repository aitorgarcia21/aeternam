import test from 'node:test';
import assert from 'node:assert/strict';
import {SCENES, buildBrainShape, buildCosmicShapes, electrodeCoverage, shapeLibrary} from '../univers-scene.mjs';

const finies = data => data.every(Number.isFinite);

test('Chaque scène du cerveau est finie, bornée et reproductible', () => {
  for (const scene of Object.values(SCENES)) {
    const data = buildBrainShape(scene, 6000);
    assert.equal(data.length, 6000 * 8);
    assert.ok(finies(data), `scène ${scene} : valeur non finie`);
    for (let i = 0; i < data.length; i += 8) {
      assert.ok(Math.abs(data[i]) < 2 && Math.abs(data[i + 1]) < 1.6 && Math.abs(data[i + 2]) < 1.5, `scène ${scene} : point hors cadre`);
      assert.ok(data[i + 6] >= 0 && data[i + 6] <= 1, `scène ${scene} : opacité hors de [0, 1]`);
      assert.ok(data[i + 7] > 0, `scène ${scene} : taille nulle`);
    }
    assert.deepEqual(buildBrainShape(scene, 6000), data);
  }
  assert.throws(() => buildBrainShape(12, 10), RangeError);
});

test('Les scènes cosmiques restent finies', () => {
  for (const data of buildCosmicShapes(4000)) assert.ok(finies(data));
});

test('La luminosité des électrodes est la part de lettre couverte', () => {
  for (const electrodes of [4, 16, 100, 378, 1600]) {
    const {n, cells} = electrodeCoverage(electrodes);
    assert.equal(cells.length, n * n);
    assert.ok(cells.every(cell => cell.intensity >= 0 && cell.intensity <= 1));
  }
  // Aire de la lettre E : 1,23 sur 4 ; la moyenne fine converge vers cette fraction.
  const fine = electrodeCoverage(1600).cells;
  const moyenne = fine.reduce((sum, cell) => sum + cell.intensity, 0) / fine.length;
  assert.ok(Math.abs(moyenne - 1.23 / 4) < .01, `moyenne ${moyenne}`);
  assert.equal(electrodeCoverage(100).n, 10);
});

test('Changer le nombre d’électrodes reconstruit seulement la scène de la vision', () => {
  const library = shapeLibrary(3000);
  const avant = library.get(SCENES.vision), memoire = library.get(SCENES.memoire);
  library.configure(SCENES.vision, {electrodes: 1600});
  assert.equal(library.version(SCENES.vision), 1);
  assert.notDeepEqual(library.get(SCENES.vision), avant);
  assert.equal(library.get(SCENES.memoire), memoire);
});
