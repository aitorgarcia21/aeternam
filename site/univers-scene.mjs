/** Illustrations procédurales, sans images ni données d'observation.
 * Les positions sont déterministes. Le mélange dépend du défilement, pas du temps.
 * WebGL dessine les nuages ; un rendu Canvas conserve les scènes sans accélération.
 * Scènes 0 à 12 : histoire cosmique. Scènes 13 à 19 : cerveau, frontières et trou noir,
 * schémas hors échelle. Chaque scène n'est construite qu'au moment où elle sert.
 */
const TAU = Math.PI * 2;
const mix = (a, b, t) => a + (b - a) * t;
const smooth = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
const GOLD = [1, .76, .42], BLUE = [.53, .73, 1], WHITE = [.93, .96, 1];
const PALE = WHITE.map((value, k) => mix(value, BLUE[k], .45));
const tint = (a, b, t) => a.map((value, k) => mix(value, b[k], t));
const COSMIC_SCENES = 13;

export const SCENES = {
  neurones: 13, vision: 14, memoire: 15, reve: 16, interface: 17, simulation: 18, 'trou-noir': 19,
};

function generator(seed) {
  let state = seed >>> 0;
  const random = () => ((state = (Math.imul(state, 1664525) + 1013904223) >>> 0) / 4294967296);
  const normal = () => Math.sqrt(-2 * Math.log(Math.max(random(), .000001))) * Math.cos(TAU * random());
  return {random, normal};
}

let filamentNodes = null;
function cosmicNodes() {
  if (!filamentNodes) {
    const {random} = generator(31973);
    filamentNodes = Array.from({length: 23}, () => [random() * 2.5 - 1.25, random() * 1.8 - .9, random() - .5]);
  }
  return filamentNodes;
}

function cosmicScene(scene, count) {
  const {random, normal} = generator(31973 + 7919 * (scene + 1));
  const nodes = cosmicNodes();
  const data = new Float32Array(count * 8);
  for (let i = 0; i < count; i++) {
    const a = random(), b = random(), c = random(), d = random();
    let x, y, z, color = BLUE, opacity = .65, size = .65 + Math.pow(d, 6) * 3;
    if (scene === 9 || scene === 12) {
      const bulge = i % 6 === 0;
      const r = bulge ? Math.abs(normal()) * .19 : Math.pow(a, .75) * 1.5;
      const arm = i % 2;
      const angle = i % 7 < 2 ? b * TAU : arm * TAU / 2 + 4.1 * Math.log(r + .22) + normal() * (.21 + .13 / (r + .2));
      const px = Math.cos(angle) * r, py = Math.sin(angle) * r;
      x = px * .94 - py * .2; y = px * .24 + py * .65;
      z = normal() * (bulge ? .12 : .026) * (1.3 - Math.min(r, 1));
      const tone = Math.min(1, Math.max(0, (r - .1) / .8));
      color = i % 9 < 2 ? WHITE : [1,.86,.62].map((value,k)=>mix(value,BLUE[k],tone));
      opacity = bulge ? .62 : .18 + b * .7;
      size *= bulge ? .85 : 1;
      if (scene === 9) { x *= .86; y *= .86; }
    } else if (scene === 0) {
      const r = .16 + a * 1.7, angle = b * TAU;
      x = Math.cos(angle) * r; y = Math.sin(angle) * r * .73; z = (c - .5) * .8;
      opacity = .05 + Math.pow(a, 3) * .38;
      color = i % 4 ? BLUE : GOLD;
    } else if (scene === 1) {
      const n = 24, plane = i % 5;
      x = ((i % n) / (n - 1) - .5) * 2.4 + normal() * .007;
      y = ((Math.floor(i / n) % n) / (n - 1) - .5) * 1.5 + normal() * .007;
      z = (plane - 2) * .2; color = plane % 2 ? BLUE : GOLD;
      opacity = .38; size *= .8;
    } else if (scene === 2 || scene === 5) {
      x = normal() * .64; y = normal() * .45; z = (c - .5) * .8;
      color = scene === 2 ? (i % 5 ? GOLD : [1,.42,.2]) : (i % 4 ? BLUE : GOLD);
      opacity = .12 + b * .35; size = 1 + d * 2.1;
    } else if (scene === 3 || scene === 4) {
      const group = i % 5;
      const centers = [[0,0],[.88,.48],[-.75,-.53],[.85,-.63],[-.95,.53]];
      const nucleon = Math.floor(i / 5) % (scene === 3 ? 3 : 4);
      const angle = nucleon * TAU / (scene === 3 ? 3 : 4);
      const offset = scene === 3 ? .135 : .1;
      const rad = Math.cbrt(a) * (scene === 3 ? .078 : .105), az = b * TAU;
      const cosPolar = c * 2 - 1, sinPolar = Math.sqrt(1 - cosPolar * cosPolar);
      x = centers[group][0] + Math.cos(angle) * offset + rad * sinPolar * Math.cos(az);
      y = centers[group][1] + Math.sin(angle) * offset + rad * sinPolar * Math.sin(az);
      z = rad * cosPolar;
      color = nucleon % 2 ? BLUE : GOLD; opacity = .4; size *= .8;
    } else if (scene === 6) {
      const group = i % 7 < 5 ? 0 : i % 7 === 5 ? 1 : 2;
      const centers = [[.08,.04],[-.74,-.55],[.97,.6]];
      const scale = group === 0 ? 1 : .42;
      const nucleus = i % 14 === 0;
      // Nuage probabiliste, pas une orbite d'électron ; tailles schématiques.
      const r = nucleus ? Math.cbrt(a) * .035 : -Math.log(Math.max(.00001,a * b)) * .14;
      const angle = c * TAU, polar = random() * 2 - 1, s = Math.sqrt(1 - polar * polar);
      x = centers[group][0] + r * s * Math.cos(angle) * scale;
      y = centers[group][1] + r * s * Math.sin(angle) * scale;
      z = r * polar * scale;
      color = nucleus ? GOLD : BLUE; opacity = nucleus ? .24 : .15 + d * .4;
      size = nucleus ? 1 : .55 + d;
    } else if (scene === 7 || scene === 8 || scene === 11) {
      const n = i % nodes.length, start = nodes[n];
      const end = nodes[(n + 1 + n % 4) % nodes.length];
      const along = a;
      const diffuse = scene === 7 ? .12 : scene === 8 ? .055 : .027;
      const curl = Math.sin(along * Math.PI) * .13;
      x = mix(start[0], end[0], along) + normal() * diffuse;
      y = mix(start[1], end[1], along) + Math.sin(n * 2.3) * curl + normal() * diffuse;
      z = mix(start[2], end[2], along) + normal() * diffuse;
      color = scene === 11 ? (i % 3 ? GOLD : BLUE) : BLUE;
      opacity = scene === 7 ? .075 : scene === 8 ? .28 : .36;
      if (scene === 8 && i % 6 === 0) {
        x = start[0] + normal() * .014; y = start[1] + normal() * .014; z = start[2];
        color = GOLD; opacity = .8; size *= 1.7;
      }
    } else if (scene === 10) {
      const central = i % 5 < 2, r = central ? Math.cbrt(a) * .115 : .2 + Math.sqrt(a) * 1.12;
      const angle = b * TAU;
      x = Math.cos(angle) * r; y = Math.sin(angle) * r * (central ? 1 : .32); z = (c - .5) * (central ? .2 : .02);
      color = GOLD; opacity = central ? .055 : .12; size *= central ? .45 : .5;
    }
    // Étoiles d'arrière-plan seulement pour les époques où elles existent.
    if ((scene >= 8 || scene === 12) && i > count * .965) {
      x = (a - .5) * 5.8; y = (b - .5) * 3.4; z = (c - .5) * 1.5;
      color = i % 4 ? BLUE : GOLD; opacity = .2 + d * .7; size = .7 + Math.pow(d, 10) * 4;
    }
    data.set([x,y,z,...color,opacity,size],i * 8);
  }
  return data;
}

export function buildCosmicShapes(count) {
  return Array.from({length: COSMIC_SCENES}, (_, scene) => cosmicScene(scene, count));
}

/* Les scènes du cerveau sont faites de segments : un point tombe sur un segment au prorata
 * de son poids, puis s'écarte un peu de la ligne. Un segment de longueur nulle donne un amas. */
function fill(data, first, last, segments, {random, normal}) {
  if (!segments.length || last <= first) return;
  const cumulative = new Float64Array(segments.length);
  let total = 0;
  segments.forEach((s, i) => { total += s.weight; cumulative[i] = total; });
  for (let i = first; i < last; i++) {
    const target = random() * total;
    let lo = 0, hi = segments.length - 1;
    while (lo < hi) { const mid = (lo + hi) >> 1; if (cumulative[mid] < target) lo = mid + 1; else hi = mid; }
    const s = segments[lo], t = random(), o = i * 8;
    data[o] = mix(s.a[0], s.b[0], t) + normal() * s.spread;
    data[o + 1] = mix(s.a[1], s.b[1], t) + normal() * s.spread;
    data[o + 2] = mix(s.a[2], s.b[2], t) + normal() * s.spread * .6;
    data[o + 3] = s.color[0]; data[o + 4] = s.color[1]; data[o + 5] = s.color[2];
    data[o + 6] = s.opacity * (.55 + random() * .45);
    data[o + 7] = s.size * (.7 + random() * .6);
  }
}

function groups(data, count, rng, parts) {
  let start = 0;
  parts.forEach(([segments, share], i) => {
    const end = i === parts.length - 1 ? count : Math.min(count, start + Math.round(count * share));
    fill(data, start, end, segments, rng);
    start = end;
  });
}

const amas = (p, spread, color, opacity, size, weight = 1) => ({a: p, b: p, weight, spread, color, opacity, size});

function branch(list, rng, x, y, z, angle, length, depth, width, style) {
  let a = angle;
  for (let k = 0; k < 3; k++) {
    a += rng.normal() * .2;
    const nx = x + Math.cos(a) * length / 3, ny = y + Math.sin(a) * length / 3, nz = z + rng.normal() * .015;
    list.push({a: [x, y, z], b: [nx, ny, nz], weight: length / 3 * (.35 + width), spread: .0025 + width * .004,
      color: style.color, opacity: style.opacity * (.55 + width * .45), size: style.size * (.75 + width * .35)});
    x = nx; y = ny; z = nz;
  }
  if (depth > 0) for (const turn of [-1, 1]) {
    branch(list, rng, x, y, z, a + turn * (.32 + rng.random() * .32), length * (.6 + rng.random() * .14), depth - 1, width * .7, style);
  }
}

function curve(list, rng, p, q, style, bend = (rng.random() - .5) * .5, pieces = 10) {
  const dx = q[0] - p[0], dy = q[1] - p[1];
  const control = [p[0] + dx * .5 - dy * bend, p[1] + dy * .5 + dx * bend, (p[2] + q[2]) / 2];
  let previous = p;
  for (let k = 1; k <= pieces; k++) {
    const t = k / pieces;
    const point = [0, 1, 2].map(j => (1 - t) * (1 - t) * p[j] + 2 * (1 - t) * t * control[j] + t * t * q[j]);
    list.push({a: previous, b: point, weight: Math.hypot(point[0] - previous[0], point[1] - previous[1]) * (style.weight || 1),
      spread: style.spread || .0025, color: style.color, opacity: style.opacity, size: style.size});
    previous = point;
  }
  return previous;
}

function neurones(data, count, rng) {
  const somas = [[-.5, -.38, 0], [.22, -.52, .05], [.5, .18, -.04], [-.18, .44, .03], [.02, -.04, -.02]];
  const dendrites = [], axons = [], corps = [], boutons = [], lointains = [];
  somas.forEach(([x, y, z], n) => {
    const primaires = 5 + (n % 2);
    for (let k = 0; k < primaires; k++) {
      branch(dendrites, rng, x, y, z, k / primaires * TAU + rng.random() * .5, .12 + rng.random() * .05, 3, 1, {color: PALE, opacity: .85, size: .85});
    }
    corps.push(amas([x, y, z], .022, GOLD, .85, 1.3));
    // L'axone s'arrête parmi les dendrites d'un autre neurone, où il se ramifie.
    const cible = somas[(n + 2) % somas.length];
    const fin = [mix(x, cible[0], .8), mix(y, cible[1], .8), mix(z, cible[2], .8)];
    curve(axons, rng, [x, y, z], fin, {color: PALE, opacity: .7, size: .7, spread: .0022}, (rng.random() - .5) * .6, 18);
    const direction = Math.atan2(cible[1] - y, cible[0] - x);
    for (let k = 0; k < 5; k++) {
      const angle = direction + (rng.random() - .5) * 1.7, r = .03 + rng.random() * .05;
      const bout = [fin[0] + Math.cos(angle) * r, fin[1] + Math.sin(angle) * r, fin[2]];
      axons.push({a: fin, b: bout, weight: r, spread: .002, color: PALE, opacity: .6, size: .65});
      boutons.push(amas(bout, .006, GOLD, .95, 1.05));
    }
  });
  for (let k = 0; k < 9; k++) {
    const x = (rng.random() - .5) * 2.8, y = (rng.random() - .5) * 1.9, z = .35 + rng.random() * .6;
    for (let j = 0; j < 4; j++) branch(lointains, rng, x, y, z, j / 4 * TAU + rng.random(), .09, 2, .6, {color: BLUE, opacity: .22, size: .7});
  }
  groups(data, count, rng, [[dendrites, .5], [axons, .17], [corps, .07], [boutons, .05], [lointains, .21]]);
}

const LETTRE_E = [[-.6, -.75, .6, -.45], [-.6, -.75, -.25, .75], [-.6, -.15, .4, .15], [-.6, .45, .6, .75]];

/** Une électrode par case d'une grille carrée. Sa luminosité est la part de la case couverte
 * par la lettre : le modèle le plus simple d'une image réduite à N points lumineux. */
export function electrodeCoverage(electrodes) {
  const n = Math.max(2, Math.round(Math.sqrt(electrodes)));
  const cells = [];
  for (let j = 0; j < n; j++) for (let i = 0; i < n; i++) {
    let covered = 0;
    for (let sj = 0; sj < 5; sj++) for (let si = 0; si < 5; si++) {
      const x = -1 + (i + (si + .5) / 5) * 2 / n, y = -1 + (j + (sj + .5) / 5) * 2 / n;
      if (LETTRE_E.some(([x0, y0, x1, y1]) => x >= x0 && x <= x1 && y >= y0 && y <= y1)) covered++;
    }
    cells.push({x: -1 + (i + .5) * 2 / n, y: -1 + (j + .5) * 2 / n, intensity: covered / 25});
  }
  return {n, cells};
}

function vision(data, count, rng, electrodes) {
  const {n, cells} = electrodeCoverage(electrodes);
  const half = .62, spacing = 2 * half / n;
  const parCase = count / cells.length;
  const densite = Math.min(1, Math.sqrt(120 / parCase));  // Un amas de 3 000 points ne doit pas saturer.
  for (let i = 0; i < count; i++) {
    const cell = cells[i % cells.length], lit = cell.intensity, o = i * 8;
    const sigma = spacing * (.07 + .2 * lit);
    data[o] = cell.x * half + rng.normal() * sigma;
    data[o + 1] = cell.y * half + rng.normal() * sigma;
    data[o + 2] = rng.normal() * .01;
    const color = tint(BLUE, GOLD, lit);
    data[o + 3] = color[0]; data[o + 4] = color[1]; data[o + 5] = color[2];
    data[o + 6] = (.1 + .8 * lit * (.6 + rng.random() * .4)) * densite;
    data[o + 7] = .7 + 1.4 * lit * rng.random();
  }
}

function memoire(data, count, rng) {
  const nodes = [];
  for (let essai = 0; nodes.length < 44 && essai < 5000; essai++) {
    const p = [-.76 + rng.random() * 1.48, -.74 + rng.random() * 1.48, (rng.random() - .5) * .4];
    if (nodes.every(q => Math.hypot(p[0] - q[0], p[1] - q[1]) > .13)) nodes.push(p);
  }
  const proches = i => nodes.map((q, j) => [Math.hypot(nodes[i][0] - q[0], nodes[i][1] - q[1]), j]).sort((a, b) => a[0] - b[0]);
  const centre = nodes.map((p, i) => [Math.hypot(p[0] - .12, p[1] + .06), i]).sort((a, b) => a[0] - b[0])[0][1];
  const ensemble = new Set(proches(centre).slice(0, 7).map(([, j]) => j));
  const liens = new Map();
  nodes.forEach((p, i) => {
    const voisins = proches(i).slice(1, ensemble.has(i) ? 5 : 4);
    voisins.forEach(([, j]) => liens.set(`${Math.min(i, j)}-${Math.max(i, j)}`, [Math.min(i, j), Math.max(i, j)]));
  });
  const calmes = [], actifs = [], corps = [], coeurs = [], brume = [];
  for (const [i, j] of liens.values()) {
    const actif = ensemble.has(i) && ensemble.has(j);
    curve(actif ? actifs : calmes, rng, nodes[i], nodes[j], actif ? {color: GOLD, opacity: .85, size: .9, spread: .003} : {color: PALE, opacity: .42, size: .7}, (rng.random() - .5) * .35, 8);
  }
  nodes.forEach((p, i) => (ensemble.has(i) ? coeurs : corps).push(
    ensemble.has(i) ? amas(p, .02, GOLD, .95, 1.3) : amas(p, .012, BLUE, .6, .9)));
  for (let k = 0; k < 40; k++) brume.push(amas([(rng.random() - .5) * 2.8, (rng.random() - .5) * 1.9, (rng.random() - .5) * .8], .16, BLUE, .07, .6));
  groups(data, count, rng, [[calmes, .45], [actifs, .25], [corps, .12], [coeurs, .1], [brume, .08]]);
}

function reve(data, count, rng) {
  const traces = 6, debut = -.76, fin = .72, fenetre = [-.02, .38];
  for (let i = 0; i < count; i++) {
    const k = i % traces, x = debut + rng.random() * (fin - debut), o = i * 8;
    const paradoxal = smooth(fenetre[0] - .05, fenetre[0] + .05, x) * (1 - smooth(fenetre[1] - .05, fenetre[1] + .05, x));
    const phase = k * 1.7;
    const lent = Math.sin(x * 13 + phase) * .062 + Math.sin(x * 5.3 + phase * 2) * .025;
    const rapide = Math.sin(x * 92 + phase) * .014 + Math.sin(x * 157 + phase * 3) * .008;
    data[o] = x;
    data[o + 1] = -.56 + k * .225 + mix(lent, rapide, paradoxal) + rng.normal() * .0035;
    data[o + 2] = rng.normal() * .01;
    const color = tint(PALE, GOLD, paradoxal);
    data[o + 3] = color[0]; data[o + 4] = color[1]; data[o + 5] = color[2];
    data[o + 6] = (.55 + .3 * paradoxal) * (.6 + rng.random() * .4);
    data[o + 7] = .7 + .35 * paradoxal;
  }
}

function interfaceCerveau(data, count, rng) {
  const cortex = [], grille = [], fils = [];
  for (let k = 0; k < 11; k++) {
    const profondeur = k / 10, y0 = -.12 + profondeur * .74, z = (profondeur - .5) * .9;
    let precedent = null;
    for (let s = 0; s <= 40; s++) {
      const x = -.78 + s / 40 * 1.52;
      const point = [x, y0 + Math.sin(x * 7 + k * 1.3) * .035 + Math.sin(x * 2.1 - k) * .03, z];
      if (precedent) cortex.push({a: precedent, b: point, weight: 1, spread: .006 + profondeur * .004, color: PALE, opacity: .32 + profondeur * .3, size: .7 + profondeur * .35});
      precedent = point;
    }
  }
  const electrode = (i, j) => { const u = (i - 4.5) * .07, v = (j - 4.5) * .07; return [.06 + u + v * .18, .04 + v * .5, v * .7]; };
  for (let j = 0; j < 10; j++) for (let i = 0; i < 10; i++) grille.push(amas(electrode(i, j), .008, GOLD, .95, 1.1));
  for (let k = 0; k < 6; k++) {
    curve(fils, rng, electrode(2 + k, 0), [.72 + k * .015, -.86 + k * .02, -.2], {color: GOLD, opacity: .5, size: .65, spread: .002}, .18, 16);
  }
  groups(data, count, rng, [[cortex, .55], [grille, .3], [fils, .15]]);
}

function simulation(data, count, rng) {
  const noeuds = [], aretes = [], m = 5, demi = .4, lacet = .62, tangage = .42;
  const tourner = ([x, y, z]) => {
    const x1 = x * Math.cos(lacet) + z * Math.sin(lacet), z1 = -x * Math.sin(lacet) + z * Math.cos(lacet);
    return [x1, y * Math.cos(tangage) - z1 * Math.sin(tangage), y * Math.sin(tangage) + z1 * Math.cos(tangage)];
  };
  const site = (i, j, k) => tourner([(i / (m - 1) - .5) * 2 * demi, (j / (m - 1) - .5) * 2 * demi, (k / (m - 1) - .5) * 2 * demi]);
  for (let i = 0; i < m; i++) for (let j = 0; j < m; j++) for (let k = 0; k < m; k++) {
    noeuds.push(amas(site(i, j, k), .008, GOLD, .85, 1.05));
    for (const [di, dj, dk] of [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) {
      if (i + di < m && j + dj < m && k + dk < m) {
        aretes.push({a: site(i, j, k), b: site(i + di, j + dj, k + dk), weight: 1, spread: .003, color: PALE, opacity: .5, size: .65});
      }
    }
  }
  groups(data, count, rng, [[aretes, .7], [noeuds, .3]]);
}

function trouNoir(data, count, rng) {
  // Disque incliné, anneau lumineux et ombre centrale : une illustration, pas une image calculée.
  for (let i = 0; i < count; i++) {
    const o = i * 8, angle = rng.random() * TAU;
    let x, y, z, color, opacity, size;
    if (i % 9 === 0) {
      const r = .2 + rng.normal() * .006;
      x = Math.cos(angle) * r; y = Math.sin(angle) * r; z = 0;
      color = WHITE; opacity = .45; size = .7;
    } else {
      const u = Math.pow(rng.random(), 1.6), r = .26 + u * .7;
      x = Math.cos(angle) * r; y = Math.sin(angle) * r * .28 + rng.normal() * .006; z = Math.sin(angle) * r * .5;
      color = tint(GOLD, BLUE, u); opacity = .5 * (1 - u * .85); size = .6 + (1 - u) * .5;
    }
    data.set([x, y, z, ...color, opacity, size], o);
  }
}

const BRAIN_BUILDERS = {13: neurones, 14: vision, 15: memoire, 16: reve, 17: interfaceCerveau, 18: simulation, 19: trouNoir};

export function buildBrainShape(scene, count, {electrodes = 100} = {}) {
  const build = BRAIN_BUILDERS[scene];
  if (!build) throw new RangeError(`Scène inconnue : ${scene}`);
  const data = new Float32Array(count * 8);
  build(data, count, generator(104729 + 7919 * scene), electrodes);
  return data;
}

/** Une bibliothèque par nombre de points, partagée par toutes les scènes de la page. */
const libraries = new Map();
export function shapeLibrary(count) {
  if (!libraries.has(count)) {
    const built = new Map(), versions = new Map(), options = {};
    libraries.set(count, {
      get(scene) {
        if (!built.has(scene)) built.set(scene, scene < COSMIC_SCENES ? cosmicScene(scene, count) : buildBrainShape(scene, count, options));
        return built.get(scene);
      },
      version: scene => versions.get(scene) || 0,
      configure(scene, values) {
        Object.assign(options, values);
        built.delete(scene);
        versions.set(scene, (versions.get(scene) || 0) + 1);
      },
    });
  }
  return libraries.get(count);
}

const VERTEX = `
attribute vec3 aFrom; attribute vec3 aTo;
attribute vec4 cFrom; attribute vec4 cTo;
attribute float sFrom; attribute float sTo;
uniform vec2 uResolution; uniform vec2 uCenter;
uniform float uMix; uniform float uTime; uniform float uScale; uniform float uDpr; uniform float uCloud; uniform float uFade;
varying vec4 vColor;
void main(){
  vec3 p=mix(aFrom,aTo,uMix);
  float a=sin(uTime*.045)*.07;
  p.xz=mat2(cos(a),-sin(a),sin(a),cos(a))*p.xz;
  p.xy+=vec2(sin(p.y*5.+uTime*.14),cos(p.x*4.+uTime*.12))*.008*uCloud;
  float perspective=2.8/(2.8+p.z*.45);
  vec2 pos=uCenter+p.xy*uScale*perspective;
  gl_Position=vec4(pos/uResolution*2.-1.,0.,1.);
  gl_Position.y=-gl_Position.y;
  gl_PointSize=clamp(mix(sFrom,sTo,uMix)*3.6*uDpr*perspective,1.,34.);
  vColor=mix(cFrom,cTo,uMix);
  float leftFade=smoothstep(.24,.49,pos.x/uResolution.x);
  vColor.a*=mix(1.,mix(leftFade,1.,step(uResolution.x,760.)),uFade);
}
`;
const FRAGMENT = `
precision mediump float; varying vec4 vColor;
void main(){
  float r=length(gl_PointCoord-.5)*2.;
  if(r>1.) discard;
  float core=exp(-r*r*24.);
  float halo=exp(-r*r*5.)*.13;
  gl_FragColor=vec4(vColor.rgb, (core+halo)*vColor.a);
}
`;
const BACK_VERTEX = `attribute vec2 aPosition; varying vec2 vUV; void main(){vUV=aPosition*.5+.5;gl_Position=vec4(aPosition,0.,1.);}`;
const BACK_FRAGMENT = `
precision mediump float;
varying vec2 vUV; uniform vec2 uResolution; uniform vec2 uCenter;
uniform float uScale; uniform float uTime; uniform float uFrom; uniform float uTo; uniform float uMix; uniform float uFade;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p),f=fract(p); f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1.,0.)),f.x),mix(hash(i+vec2(0.,1.)),hash(i+1.),f.x),f.y);}
float fbm(vec2 p){float n=0.;float a=.5;for(int i=0;i<4;i++){n+=a*noise(p);p=p*2.04+3.8;a*=.5;}return n;}
vec3 field(float scene,vec2 p){
  vec3 gold=vec3(.94,.72,.44), blue=vec3(.27,.48,.76);
  float n=fbm(p*5.+uTime*.004);
  float r=length(p);
  if(scene>12.5){
    if(scene>18.5){float glow=exp(-abs(r-.2)*40.)*.35+exp(-r*3.)*.12;return gold*glow*step(.19,r)+blue*pow(n,3.)*exp(-r*r)*.08;}
    return blue*pow(n,3.)*exp(-r*r*.9)*.1+gold*pow(n,6.)*exp(-r*r*2.)*.05;
  }
  if(scene>11.5 || (scene>8.5 && scene<9.5)){
    vec2 q=vec2(p.x*.98+p.y*.3,(-p.x*.24+p.y*.94)/.64);
    float rr=length(q), a=atan(q.y,q.x);
    float arms=pow(.5+.5*cos(a*2.-8.2*log(rr+.22)+n*.8),5.);
    float disk=exp(-rr*1.8)*(1.-smoothstep(.8,1.7,rr));
    float cloud=pow(n,2.7)*arms*disk;
    return blue*cloud*3.6+gold*exp(-rr*10.)*1.3+gold*pow(n,3.)*disk*.18;
  }
  if(scene>1.5 && scene<2.5) return gold*pow(n,2.)*exp(-r*r*.9)*.55;
  if(scene>5.5 && scene<6.5){
    float atom=exp(-length(p-vec2(.08,.04))*5.);
    float farther=exp(-length(p-vec2(-.74,-.55))*13.)+exp(-length(p-vec2(.97,.6))*13.);
    return blue*(atom*.17+farther*.09)+gold*exp(-length(p-vec2(.08,.04))*45.)*.55;
  }
  if(scene>4.5 && scene<5.5) return blue*n*exp(-r*r)*.13;
  if(scene>9.5 && scene<10.5){
    if(r<.116){float z=sqrt(1.-(r/.116)*(r/.116));return vec3(1.,.68,.25)*(.55+.45*z)*(.7+.3*fbm(p*180.));}
    return gold*exp(-r*13.)*.7;
  }
  if(scene>6.5 && scene<8.5) return blue*pow(n,4.)*exp(-r*r*.3)*.24;
  if(scene>10.5 && scene<11.5) return gold*pow(n,5.)*exp(-r*r*.5)*.24;
  return vec3(0.);
}
void main(){
  vec2 pixel=vec2(vUV.x,1.-vUV.y)*uResolution;
  vec2 p=(pixel-uCenter)/uScale;
  vec3 light=mix(field(uFrom,p),field(uTo,p),uMix);
  float mask=mix(1.,mix(smoothstep(.25,.56,vUV.x),1.,step(uResolution.x,760.)),uFade);
  light*=mask;
  gl_FragColor=vec4(vec3(.051,.063,.059)+light,.92);
}
`;

function shader(gl,type,source){
  const s=gl.createShader(type); gl.shaderSource(s,source); gl.compileShader(s);
  if(!gl.getShaderParameter(s,gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
  return s;
}
function program(gl,vs,fs){
  const p=gl.createProgram(), v=shader(gl,gl.VERTEX_SHADER,vs), f=shader(gl,gl.FRAGMENT_SHADER,fs);
  gl.attachShader(p,v); gl.attachShader(p,f); gl.linkProgram(p);
  gl.deleteShader(v); gl.deleteShader(f);
  if(!gl.getProgramParameter(p,gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
  return p;
}
function attr(gl,p,name,size,stride,offset){
  const id=gl.getAttribLocation(p,name); if(id<0)return;
  gl.enableVertexAttribArray(id); gl.vertexAttribPointer(id,size,gl.FLOAT,false,stride,offset);
}
function uniforms(gl,p,values){
  for(const [key,value] of Object.entries(values)){
    const loc=gl.getUniformLocation(p,key);
    if(Array.isArray(value))gl.uniform2f(loc,...value); else gl.uniform1f(loc,value);
  }
}

/** cadrage 'scene' : grande scène fixe à droite du texte ; 'centre' : figure autonome, centrée. */
export function createCosmos(originalCanvas, {count = matchMedia('(max-width: 760px)').matches ? 16000 : 48000, cadrage = 'scene'} = {}) {
  let canvas=originalCanvas, ctx=null, gl=null, main=null, background=null, lost=false;
  const library=shapeLibrary(count);
  let buffers, quad, maxAttributes=0, previousFrom='', previousTo='';
  const fallback=()=>{
    if(gl){ const fresh=canvas.cloneNode(false); canvas.replaceWith(fresh); canvas=fresh; }
    gl=null; ctx=canvas.getContext('2d'); canvas.dataset.renderer='canvas';
  };
  try{
    gl=canvas.getContext('webgl',{alpha:true,antialias:false,depth:false,premultipliedAlpha:false});
    if(!gl) fallback();
    else {
      main=program(gl,VERTEX,FRAGMENT); background=program(gl,BACK_VERTEX,BACK_FRAGMENT);
      buffers=[gl.createBuffer(),gl.createBuffer()]; quad=gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER,quad); gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),gl.STATIC_DRAW);
      canvas.dataset.renderer='webgl';maxAttributes=gl.getParameter(gl.MAX_VERTEX_ATTRIBS);
      canvas.addEventListener('webglcontextlost',e=>{e.preventDefault(); lost=true;});
    }
  }catch(error){ console.warn('Rendu WebGL indisponible, passage au rendu Canvas.',error.message); fallback(); }
  let w=0,h=0,dpr=1;
  function resize(){
    const box=canvas.getBoundingClientRect(); w=box.width;h=box.height;dpr=Math.min(devicePixelRatio||1,1.75);
    canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);
    if(ctx)ctx.setTransform(dpr,0,0,dpr,0,0);
  }
  function draw({from=12,to=12,blend=0,time=0,phase=0}){
    if(lost){fallback();resize();lost=false;}
    if(!w||!h)return;
    const mobile=w<=760, centre=cadrage==='centre';
    const intro=from===12&&to===12;
    const center=centre?[w*.5,h*.5]:[w*(mobile?.52:.73),h*(intro&&!mobile?.3:.47)];
    let scale=centre?Math.min(w,h)*.56:Math.min(w*(mobile?.41:.38),h*.77);
    const inflationWeight=(from===1?1-blend:0)+(to===1?blend:0);
    scale*=1+inflationWeight*(phase-.3)*.6;
    const fade=centre?0:1;
    if(gl){
      gl.viewport(0,0,canvas.width,canvas.height);gl.disable(gl.DEPTH_TEST);gl.disable(gl.BLEND);
      gl.useProgram(background);gl.bindBuffer(gl.ARRAY_BUFFER,quad);attr(gl,background,'aPosition',2,0,0);
      const common={uResolution:[w,h],uCenter:center,uScale:scale,uTime:time,uFade:fade};
      uniforms(gl,background,{...common,uFrom:from,uTo:to,uMix:blend});
      gl.drawArrays(gl.TRIANGLES,0,6);
      // Le programme suivant réutilise les emplacements d'attributs : réinitialiser
      // les tableaux évite qu'un ancien buffer court borne un nouveau drawArrays.
      const max=maxAttributes;
      for(let i=0;i<max;i++)gl.disableVertexAttribArray(i);
      gl.useProgram(main);
      [from,to].forEach((scene,index)=>{
        const key=scene+':'+library.version(scene);
        gl.bindBuffer(gl.ARRAY_BUFFER,buffers[index]);
        if((index===0?previousFrom:previousTo)!==key)gl.bufferData(gl.ARRAY_BUFFER,library.get(scene),gl.STATIC_DRAW);
        if(index===0)previousFrom=key;else previousTo=key;
        attr(gl,main,index===0?'aFrom':'aTo',3,32,0);
        attr(gl,main,index===0?'cFrom':'cTo',4,32,12);
        attr(gl,main,index===0?'sFrom':'sTo',1,32,28);
      });
      uniforms(gl,main,{...common,uMix:blend,uDpr:dpr,uCloud:1});
      gl.enable(gl.BLEND);gl.blendFunc(gl.SRC_ALPHA,gl.ONE);
      gl.drawArrays(gl.POINTS,0,count);
      for(let i=0;i<max;i++)gl.disableVertexAttribArray(i);
    }else if(ctx){
      ctx.clearRect(0,0,w,h);
      const a=library.get(from), b=library.get(to), stride=Math.ceil(count/6500);
      for(let i=0;i<count;i+=stride){
        const o=i*8, x=center[0]+mix(a[o],b[o],blend)*scale, y=center[1]+mix(a[o+1],b[o+1],blend)*scale;
        const opacity=mix(a[o+6],b[o+6],blend)*(mobile||centre?1:Math.max(0,Math.min(1,(x/w-.27)/.25)));
        const c=[0,1,2].map(k=>Math.round(mix(a[o+3+k],b[o+3+k],blend)*255));
        ctx.fillStyle=`rgba(${c.join(',')},${opacity})`;
        const size=mix(a[o+7],b[o+7],blend);
        ctx.beginPath();ctx.arc(x,y,Math.max(.4,size*.7),0,TAU);ctx.fill();
      }
    }
    canvas.dataset.scene=String(blend>.5?to:from);
  }
  resize();
  return {draw,resize,library,get canvas(){return canvas;},get renderer(){return gl?'webgl':'canvas';}};
}
