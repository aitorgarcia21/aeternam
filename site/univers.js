import {movingClockRatio, stationaryClockRatio, traceLight} from './univers-physique.mjs?v=__PHYSIQUE_VERSION__';

const root = document.querySelector('body.univers');
if (root) initializeUniverse();

function initializeUniverse() {
  const $ = id => document.getElementById(id);
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const lerp = (a, b, t) => a + (b - a) * t;
  const fmt = (x, digits = 2) => x.toLocaleString('fr-FR', {minimumFractionDigits: digits, maximumFractionDigits: digits});
  const tau = Math.PI * 2;
  const style = getComputedStyle(root);
  const palette = {
    text: style.getPropertyValue('--fg').trim(),
    muted: style.getPropertyValue('--muted').trim(),
    sage: style.getPropertyValue('--accent').trim(),
    gold: style.getPropertyValue('--or').trim(),
    background: style.getPropertyValue('--bg').trim(),
  };
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let frozen = reduce.matches;
  let animationTime = 0, lastTime = 0, lastPaint = 0, dirty = true, scrollDirty = true;
  let epoch = 0, previousEpoch = 0, sceneChangedAt = -1000, phaseProgress = 0;
  const steps = [...root.querySelectorAll('.univ-etape')];
  const chronology = root.querySelector('.univ-chronologie');
  const epochLinks = [...chronology.querySelectorAll('a')];
  const menu = root.querySelector('.univ-sommaire');
  const menuLinks = [...menu.querySelectorAll('a')];
  const chapters = ['histoire', 'espace-temps', 'avant-apres', 'sources-univers'].map($);
  const stage = $('cosmos-canvas');
  const surfaces = [...root.querySelectorAll('main canvas')].map(canvas => ({
    canvas, ctx: canvas.getContext('2d'), w: 0, h: 0, visible: false,
  }));
  if (surfaces.some(surface => !surface.ctx)) return;
  const fields = Object.fromEntries(['coord-x', 'coord-y', 'coord-z', 'coord-t', 'echelle', 'vitesse', 'rayon', 'impact'].map(id => [id, $(id)]));
  let ray = traceLight(Number(fields.impact.value));
  let rayLengths = [];
  let rayLength = 0;
  let seed = 193817;
  const random = () => { seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0; return seed / 4294967296; };
  const count = matchMedia('(max-width: 760px)').matches ? 850 : 1750;
  const seeds = Array.from({length: count}, () => Array.from({length: 8}, random));
  const centers = Array.from({length: 16}, () => [random() * 1.8 - .9, random() * 1.5 - .75, random() - .5]);

  // Ce nuage est une illustration déterministe : aucune donnée d'observation n'est simulée.
  const arrangements = Array.from({length: 12}, (_, scene) => seeds.map((r, i) => {
    let x = r[0] * 2 - 1, y = r[1] * 1.6 - .8, z = r[2] - .5;
    let size = .55 + r[3] * 1.15, opacity = .24 + r[4] * .7, gold = r[5] > .64;
    if (scene === 0) {
      x = r[0] < .68 ? -.18 + Math.cos(r[1] * tau) * r[2] * .55 : .2 + r[1];
      y = (r[3] - .5) * 1.5;
      z = (r[4] - .5) * .85;
      opacity *= .95; size *= .95;
    } else if (scene === 1) {
      x = (i % 13) / 6 - 1; y = (Math.floor(i / 13) % 11) / 6 - .8; z = (Math.floor(i / 143) % 9) / 8 - .5;
      size *= .7;
    } else if (scene === 2 || scene === 5) {
      gold = scene === 2 ? r[5] > .2 : r[5] > .8;
      size *= scene === 2 ? 1.3 : .7;
    } else if (scene === 3 || scene === 4) {
      const groups = scene === 3 ? 18 : 10;
      const group = i % groups;
      const cx = Math.sin(group * 9.71) * .85;
      const cy = Math.cos(group * 4.12) * .65;
      const a = Math.floor(i / groups) % (scene === 3 ? 3 : 4) * tau / (scene === 3 ? 3 : 4);
      x = cx + Math.cos(a) * .055 + (r[2] - .5) * .026;
      y = cy + Math.sin(a) * .055 + (r[3] - .5) * .026;
      z = Math.sin(group * 3.7) * .3 + (r[4] - .5) * .06;
      opacity = .25 + r[6] * .5; size *= .6; gold = i % 3 === 0;
    } else if (scene === 6) {
      const g = i % 9;
      const angle = r[1] * tau, radial = Math.sqrt(-2 * Math.log(Math.max(.0001, r[2]))) * .045;
      x = (g % 3 - 1) * .62 + Math.cos(angle) * radial;
      y = (Math.floor(g / 3) - 1) * .45 + Math.sin(angle) * radial;
      z = (r[3] - .5) * .13;
      size *= .65; opacity *= .6; gold = i % 12 === 0;
    } else if (scene === 7 || scene === 8) {
      const c = centers[i % 8];
      x = c[0] * .85 + (r[1] - .5) * .4;
      y = c[1] * .9 + (r[2] - .5) * .37;
      z = c[2] + (r[3] - .5) * .2;
      opacity = scene === 7 ? .13 + r[4] * .25 : .4 + r[4] * .6;
      size *= scene === 7 ? .65 : 1; gold = r[4] > .5;
    } else if (scene === 9) {
      const g = i % 5, radial = Math.pow(r[1], .65) * .33;
      const angle = radial * 13 + (i % 3) * tau / 3 + (r[2] - .5) * .7;
      const c = centers[g];
      x = c[0] * .8 + radial * Math.cos(angle);
      y = c[1] * .85 + radial * Math.sin(angle) * .55;
      z = c[2] + (r[3] - .5) * .035;
      size *= .65; gold = radial < .12 || r[5] > .8;
    } else if (scene === 10) {
      const a = r[0] * tau, radial = .14 + Math.pow(r[1], .7) * .78;
      x = Math.cos(a) * radial; y = Math.sin(a) * radial * .32; z = Math.sin(a) * radial * .14;
      size *= .55; opacity *= .32; gold = true;
    } else if (scene === 11) {
      const a = centers[i % 16], b = centers[(i % 16 + 3) % 16], t = r[1];
      const spread = Math.sin(t * Math.PI) * .025 + .012;
      x = lerp(a[0], b[0], t) + (r[2] - .5) * spread * 4;
      y = lerp(a[1], b[1], t) + (r[3] - .5) * spread * 4;
      z = lerp(a[2], b[2], t) + (r[4] - .5) * spread * 4;
      size *= .65; gold = r[5] > .5;
    }
    return {x, y, z, size, opacity, gold};
  }));

  function rgb(hex) {
    const n = parseInt(hex.replace('#', ''), 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255].join(',');
  }
  function glowSprite(color) {
    const c = document.createElement('canvas'); c.width = 64; c.height = 64;
    const ctx = c.getContext('2d');
    const gradient = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
    gradient.addColorStop(0, 'rgba(' + rgb(color) + ',1)');
    gradient.addColorStop(.1, 'rgba(' + rgb(color) + ',.9)');
    gradient.addColorStop(.3, 'rgba(' + rgb(color) + ',.16)');
    gradient.addColorStop(1, 'rgba(' + rgb(color) + ',0)');
    ctx.fillStyle = gradient; ctx.fillRect(0, 0, 64, 64); return c;
  }
  const sprites = {sage: glowSprite(palette.sage), gold: glowSprite(palette.gold)};
  function dot(ctx, x, y, r, color = palette.sage, alpha = 1) {
    ctx.globalAlpha = clamp(alpha);
    ctx.fillStyle = color; ctx.beginPath(); ctx.arc(x, y, Math.max(.3, r), 0, tau); ctx.fill();
    ctx.globalAlpha = 1;
  }
  function glow(ctx, x, y, radius, gold = false, alpha = 1) {
    ctx.globalAlpha = clamp(alpha); ctx.drawImage(gold ? sprites.gold : sprites.sage, x - radius, y - radius, radius * 2, radius * 2); ctx.globalAlpha = 1;
  }
  function line(ctx, points, color = palette.muted, alpha = .35, width = 1) {
    if (points.length < 2) return;
    ctx.beginPath(); ctx.moveTo(points[0][0], points[0][1]);
    for (const p of points.slice(1)) ctx.lineTo(p[0], p[1]);
    ctx.strokeStyle = color; ctx.lineWidth = width; ctx.globalAlpha = alpha; ctx.stroke(); ctx.globalAlpha = 1;
  }
  function label(ctx, text, x, y, align = 'center', color = palette.muted) {
    ctx.font = '13px "DM Sans", sans-serif'; ctx.textAlign = align; ctx.fillStyle = color; ctx.fillText(text, x, y);
  }
  function project(x, y, z, w, h, rotation = .18, scale = 1) {
    const xx = x * Math.cos(rotation) + z * Math.sin(rotation);
    const zz = -x * Math.sin(rotation) + z * Math.cos(rotation);
    const yy = y * .96 - zz * .22;
    const p = 2.8 / (2.8 + zz * .5);
    const s = Math.min(w * .43, h * .51) * scale;
    return [w * .5 + xx * s * p, h * .49 + yy * s * p, p];
  }
  function resize(surface) {
    const box = surface.canvas.getBoundingClientRect();
    const ratio = Math.min(devicePixelRatio || 1, 2);
    surface.w = box.width; surface.h = box.height;
    surface.canvas.width = Math.round(box.width * ratio); surface.canvas.height = Math.round(box.height * ratio);
    surface.ctx.setTransform(ratio, 0, 0, ratio, 0, 0); dirty = true;
  }
  const resizeObserver = new ResizeObserver(entries => {
    for (const entry of entries) {
      const s = surfaces.find(surface => surface.canvas === entry.target);
      if (s) resize(s);
    }
    root.style.setProperty('--nav-height', menu.getBoundingClientRect().height + 'px');
    scrollDirty = true;
  });
  surfaces.forEach(surface => resizeObserver.observe(surface.canvas));
  resizeObserver.observe(menu);
  steps.forEach(step => resizeObserver.observe(step));
  const visibility = new IntersectionObserver(entries => {
    for (const entry of entries) {
      const s = surfaces.find(surface => surface.canvas === entry.target);
      if (s) s.visible = entry.isIntersecting;
    }
    dirty = true;
  }, {rootMargin: '40px'});
  surfaces.forEach(surface => visibility.observe(surface.canvas));

  function syncScroll() {
    const mobile = innerWidth <= 760;
    const readingLine = mobile ? menu.offsetHeight + innerHeight * .33 + 65 : innerHeight * .45;
    let next = 0;
    steps.forEach((step, i) => { if (step.getBoundingClientRect().top <= readingLine) next = i; });
    const box = steps[next].getBoundingClientRect();
    phaseProgress = clamp((readingLine - box.top) / Math.max(1, box.height));
    if (next !== epoch) {
      previousEpoch = epoch; epoch = next; sceneChangedAt = performance.now();
      epochLinks.forEach((link, i) => i === epoch ? link.setAttribute('aria-current', 'step') : link.removeAttribute('aria-current'));
      $('cosmos-legende').textContent = steps[epoch].dataset.legende;
      stage.dataset.epoch = steps[epoch].id;
      if ($('univ-choix')) $('univ-choix').value = String(epoch);
    }
    const storyBox = $('histoire').getBoundingClientRect();
    chronology.dataset.visible = String(storyBox.top < innerHeight * .55 && storyBox.bottom > innerHeight * .7);
    let chapterIndex = 0;
    chapters.forEach((chapter, i) => { if (chapter.getBoundingClientRect().top <= menu.offsetHeight + 140) chapterIndex = i; });
    menuLinks.forEach((link, i) => i === chapterIndex ? link.setAttribute('aria-current', 'location') : link.removeAttribute('aria-current'));
    dirty = true; scrollDirty = false;
  }

  function drawStory(surface, now) {
    const {ctx, w, h} = surface;
    let blend = frozen ? 1 : clamp((now - sceneChangedAt) / 580);
    blend = blend * blend * (3 - 2 * blend);
    const rotation = .16 + (frozen ? 0 : Math.sin(animationTime * .07) * .06) + (phaseProgress - .5) * .1;
    const scale = epoch === 1 ? .75 + phaseProgress * .75 : 1;
    const pr = (x, y, z) => project(x, y, z, w, h, rotation, scale);
    if (epoch <= 1) {
      for (let j = 0; j <= 12; j++) {
        const a = j / 6 - 1;
        line(ctx, Array.from({length: 21}, (_, k) => pr(k / 10 - 1, a * .8, .45)), palette.sage, epoch === 0 ? .07 + j * .008 : .17);
        line(ctx, [pr(a, -.8, .45), pr(a, .8, .45)], palette.sage, .18);
      }
      for (let j = 0; j < 7; j++) line(ctx, [pr(1, j / 4 - .75, -.5), pr(1, j / 4 - .75, .45)], palette.sage, .2);
    }
    const from = arrangements[previousEpoch], to = arrangements[epoch];
    for (let i = 0; i < count; i++) {
      const a = from[i], b = to[i], r = seeds[i];
      let x = lerp(a.x, b.x, blend), y = lerp(a.y, b.y, blend), z = lerp(a.z, b.z, blend);
      if (epoch === 2 || epoch === 5) {
        x += Math.sin(animationTime * .25 + r[2] * tau) * .038;
        y += Math.cos(animationTime * .3 + r[1] * tau) * .025;
      }
      if (epoch === 10) {
        const a1 = animationTime * .025;
        const xx = x * Math.cos(a1) - y * Math.sin(a1);
        y = x * Math.sin(a1) * .3 + y * Math.cos(a1); x = xx;
      }
      const p = pr(x, y, z);
      const size = lerp(a.size, b.size, blend) * p[2];
      const alpha = lerp(a.opacity, b.opacity, blend);
      if (i % 53 === 0 && epoch !== 7) glow(ctx, p[0], p[1], 11 * p[2], b.gold, alpha * .65);
      dot(ctx, p[0], p[1], size, b.gold ? palette.gold : palette.sage, alpha);
    }
    if (epoch === 5) {
      for (let k = 0; k < 6; k++) {
        const pts = Array.from({length: 15}, (_, j) => [
          w * (.1 + ((j * .061 + k * .157) % .8)),
          h * (.22 + Math.sin(j * 13.13 + k * 5.17) * .11 + k * .085),
        ]);
        line(ctx, pts, palette.gold, .45, 1);
        const t = (animationTime * .6 + k * 2.13) % 14, j = Math.floor(t), q = t - j;
        const p = [lerp(pts[j][0], pts[j + 1][0], q), lerp(pts[j][1], pts[j + 1][1], q)];
        glow(ctx, p[0], p[1], 14, true); dot(ctx, p[0], p[1], 2, palette.gold);
      }
    }
    if (epoch === 6) {
      for (let k = 0; k < 9; k++) {
        const p = pr((k % 3 - 1) * .62, (Math.floor(k / 3) - 1) * .45, 0);
        glow(ctx, p[0], p[1], 25, false, .7); dot(ctx, p[0], p[1], 3, palette.sage);
      }
      for (let k = 0; k < 3; k++) {
        const pts = Array.from({length: 100}, (_, j) => {
          const x = j / 99;
          return [w * (.03 + .94 * x), h * (.24 + .23 * k) + Math.sin(x * tau * 2.5 - animationTime * .6) * 13];
        });
        line(ctx, pts, palette.gold, .6, 1.4);
        const q = (animationTime * .09 + k * .3) % 1;
        const p = pts[Math.floor(q * 99)];
        glow(ctx, p[0], p[1], 12, true); dot(ctx, p[0], p[1], 2, palette.gold);
      }
    }
    if (epoch === 8) {
      for (let k = 0; k < 8; k++) {
        const c = centers[k], p = pr(c[0] * .85, c[1] * .9, c[2]);
        glow(ctx, p[0], p[1], 32 + k * 2, true, .7); dot(ctx, p[0], p[1], 2.5, palette.gold);
      }
    }
    if (epoch === 10) {
      const center = pr(0, 0, 0);
      glow(ctx, center[0], center[1], 52, true); dot(ctx, center[0], center[1], 10, palette.gold);
      for (let k = 0; k < 8; k++) {
        const radius = .17 + k * .107;
        const orbit = Array.from({length: 97}, (_, j) => pr(Math.cos(j / 96 * tau) * radius, Math.sin(j / 96 * tau) * radius * .35, 0));
        line(ctx, orbit, palette.sage, .16);
        const a = k * 2.37 + animationTime * .15 / (1 + k * .3);
        const p = pr(Math.cos(a) * radius, Math.sin(a) * radius * .35, 0);
        dot(ctx, p[0], p[1], k > 3 ? 4 : 2.5, k % 2 ? palette.gold : palette.sage);
      }
    }
    if (epoch === 11) {
      for (const c of centers) {
        const p = pr(...c); glow(ctx, p[0], p[1], 23, true, .45);
      }
    }
  }

  function drawCoordinates({ctx, w, h}) {
    const p = (x, y, z) => project(x / 5, -y / 5, z / 5, w, h * .9, .52);
    for (let i = -4; i <= 4; i++) {
      line(ctx, [p(i, -4, -4), p(i, -4, 4)], palette.sage, .18);
      line(ctx, [p(-4, -4, i), p(4, -4, i)], palette.sage, .18);
      line(ctx, [p(i, -4, -4), p(i, 4, -4)], palette.sage, .12);
      line(ctx, [p(-4, i, -4), p(4, i, -4)], palette.sage, .12);
    }
    const zero = p(0, 0, 0);
    [[5, 0, 0, 'x'], [0, 5, 0, 'y'], [0, 0, 5, 'z']].forEach(([x, y, z, name]) => {
      const end = p(x, y, z);
      line(ctx, [zero, end], palette.sage, .7); label(ctx, name, end[0] + 10, end[1] - 7);
    });
    const x = +fields['coord-x'].value, y = +fields['coord-y'].value, z = +fields['coord-z'].value;
    const pos = p(x, y, z), foot = p(x, -4, z);
    ctx.setLineDash([3, 5]); line(ctx, [foot, pos], palette.gold, .7); ctx.setLineDash([]);
    glow(ctx, ...pos.slice(0, 2), 22, true); dot(ctx, pos[0], pos[1], 4, palette.gold);
    label(ctx, 'Événement', clamp(pos[0], 42, w - 42), Math.max(16, pos[1] - 18), 'center', palette.text);
    const t = +fields['coord-t'].value / 10;
    line(ctx, [[24, h - 28], [w - 24, h - 28]], palette.sage, .4);
    dot(ctx, lerp(24, w - 24, t), h - 28, 4, palette.gold);
    label(ctx, '0 s', 24, h - 7, 'left'); label(ctx, 'Temps', w / 2, h - 7); label(ctx, '10 s', w - 24, h - 7, 'right');
  }

  function drawExpansion({ctx, w, h}) {
    const a = +fields.echelle.value, unit = Math.min(w / 7.5, h / 5.5), cx = w * .42, cy = h * .5;
    const spacing = unit * a;
    for (let k = -7; k <= 7; k++) {
      line(ctx, [[cx + k * spacing, 18], [cx + k * spacing, h - 20]], palette.sage, .18);
      line(ctx, [[18, cy + k * spacing], [w - 18, cy + k * spacing]], palette.sage, .18);
    }
    for (let i = -5; i <= 5; i++) for (let j = -5; j <= 5; j++) {
      const x = cx + i * spacing, y = cy + j * spacing;
      if (x < 8 || x > w - 8 || y < 8 || y > h - 8) continue;
      ctx.save(); ctx.translate(x, y); ctx.rotate(.4 + i);
      ctx.scale(1, .45); glow(ctx, 0, 0, 18, i === 0 && j === 0, .8); ctx.restore();
      dot(ctx, x, y, 2, i === 0 && j === 0 ? palette.gold : palette.sage);
    }
    label(ctx, 'A', cx, cy - 20, 'center', palette.text);
    label(ctx, 'B', cx + spacing, cy - 20, 'center', palette.text);
    line(ctx, [[cx, cy + 32], [cx + spacing, cy + 32]], palette.gold, .8);
    line(ctx, [[cx, cy + 28], [cx, cy + 36]], palette.gold, .8);
    line(ctx, [[cx + spacing, cy + 28], [cx + spacing, cy + 36]], palette.gold, .8);
    label(ctx, fmt(a) + ' unité' + (a > 1 ? 's' : ''), cx + spacing / 2, cy + 55, 'center', palette.text);
  }

  function clock(ctx, x, y, r, angle, color) {
    ctx.strokeStyle = color; ctx.globalAlpha = .7; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.arc(x, y, r, 0, tau); ctx.stroke(); ctx.globalAlpha = 1;
    for (let i = 0; i < 60; i++) {
      const a = i / 60 * tau - Math.PI / 2, length = i % 5 === 0 ? 9 : 3;
      line(ctx, [[x + Math.cos(a) * (r - length), y + Math.sin(a) * (r - length)], [x + Math.cos(a) * (r - 2), y + Math.sin(a) * (r - 2)]], color, i % 5 === 0 ? .8 : .35);
    }
    line(ctx, [[x, y], [x + Math.cos(angle - Math.PI / 2) * r * .78, y + Math.sin(angle - Math.PI / 2) * r * .78]], color, .9, 1.6);
    dot(ctx, x, y, 3, palette.gold);
  }
  function drawVelocity({ctx, w, h}) {
    const ratio = movingClockRatio(+fields.vitesse.value / 100);
    const radius = Math.min(w * .195, h * .29);
    const y = h * .44, angle = animationTime * .8 + .5;
    label(ctx, 'Au repos', w * .25, y - radius - 24, 'center', palette.text);
    label(ctx, 'En mouvement', w * .75, y - radius - 24, 'center', palette.text);
    clock(ctx, w * .25, y, radius, angle, palette.sage);
    clock(ctx, w * .75, y, radius, angle * ratio, palette.gold);
    for (let i = 0; i < 2; i++) {
      const yy = h * .83 + i * 25, a = w * .08, b = w * .92;
      line(ctx, [[a, yy], [b, yy]], palette.muted, .15, 2);
      const end = lerp(a, b, i === 0 ? 1 : ratio);
      line(ctx, [[a, yy], [end, yy]], i ? palette.gold : palette.sage, .85, 2);
      dot(ctx, end, yy, 3, i ? palette.gold : palette.sage);
    }
  }
  function drawGravity({ctx, w, h}) {
    const scale = Math.min(w / 23, h / 8);
    const p = (r, a) => [w * .5 + r * Math.cos(a) * scale, h * .85 + r * Math.sin(a) * scale * .3 - 2 * Math.sqrt(r - 1) * scale * .8];
    for (let radius = 1; radius <= 10; radius += .42) {
      const pts = Array.from({length: 101}, (_, i) => p(radius, i / 100 * tau));
      line(ctx, pts, palette.sage, .2);
    }
    for (let k = 0; k < 28; k++) {
      const pts = Array.from({length: 91}, (_, i) => p(1 + i / 10, k / 28 * tau));
      line(ctx, pts, palette.sage, .2);
    }
    line(ctx, Array.from({length: 101}, (_, i) => p(1, i / 100 * tau)), palette.gold, .85, 1.6);
    const radius = +fields.rayon.value, pos = p(radius, -.7);
    glow(ctx, pos[0], pos[1], 20, true); dot(ctx, pos[0], pos[1], 4, palette.gold);
    label(ctx, 'Horloge à r = ' + fmt(radius) + ' rₛ', pos[0], pos[1] - 20, pos[0] > w * .65 ? 'right' : 'center', palette.text);
    label(ctx, 'Horizon · rₛ', w / 2, h * .85 + 34);
    const ratio = stationaryClockRatio(radius);
    clock(ctx, w * .83, h * .16, Math.min(34, w * .09), animationTime * .8 * ratio + .3, palette.gold);
  }
  function updateRay() {
    ray = traceLight(+fields.impact.value);
    rayLength = 0; rayLengths = [0];
    for (let i = 1; i < ray.points.length; i++) {
      rayLength += Math.hypot(ray.points[i][0] - ray.points[i - 1][0], ray.points[i][1] - ray.points[i - 1][1]);
      rayLengths.push(rayLength);
    }
  }
  function drawLight({ctx, w, h}) {
    const scale = Math.min(w / 20, h / 12), cx = w / 2, cy = h * .7;
    const p = point => [cx + point[0] * scale, cy - point[1] * scale];
    ctx.setLineDash([3, 6]);
    ctx.beginPath(); ctx.arc(cx, cy, scale * 1.5, 0, tau); ctx.strokeStyle = palette.muted; ctx.globalAlpha = .4; ctx.stroke();
    line(ctx, [p([-20, +fields.impact.value]), p([20, +fields.impact.value])], palette.muted, .3);
    ctx.setLineDash([]); ctx.globalAlpha = 1;
    ctx.beginPath(); ctx.arc(cx, cy, scale, 0, tau); ctx.fillStyle = palette.background; ctx.fill();
    ctx.strokeStyle = palette.sage; ctx.lineWidth = 1.2; ctx.stroke();
    line(ctx, ray.points.map(p), palette.gold, .9, 1.7);
    const distance = (animationTime * 5 + rayLength * .32) % rayLength;
    let j = 1;
    while (j < rayLengths.length - 1 && rayLengths[j] < distance) j++;
    if (ray.points[j]) {
      const part = (distance - rayLengths[j - 1]) / Math.max(1e-12, rayLengths[j] - rayLengths[j - 1]);
      const pos = p([lerp(ray.points[j - 1][0], ray.points[j][0], part), lerp(ray.points[j - 1][1], ray.points[j][1], part)]);
      glow(ctx, pos[0], pos[1], 14, true); dot(ctx, pos[0], pos[1], 3, palette.gold);
    }
    label(ctx, 'Horizon', cx, cy + scale + 24, 'center', palette.text);
    label(ctx, 'Sphère des photons : 1,5 rₛ', cx, h - 13);
    label(ctx, 'Rayon incident', 18, 25, 'left', palette.text);
  }
  const drawingFunctions = {
    'cosmos-canvas': drawStory,
    'espace-canvas': drawCoordinates,
    'expansion-canvas': drawExpansion,
    'vitesse-canvas': drawVelocity,
    'gravite-canvas': drawGravity,
    'lumiere-canvas': drawLight,
  };

  function updateControls(changed) {
    for (const name of ['x', 'y', 'z', 't']) {
      const val = +fields['coord-' + name].value;
      $('val-' + name).textContent = fmt(val, 1) + (name === 't' ? ' s' : '');
      fields['coord-' + name].setAttribute('aria-valuetext', fmt(val, 1) + (name === 't' ? ' secondes' : ''));
    }
    $('evenement-valeur').textContent = 'Événement : (' + ['x', 'y', 'z'].map(k => fmt(+fields['coord-' + k].value, 1)).join(' ; ') + '), à ' + fmt(+fields['coord-t'].value, 1) + ' s';
    const scale = +fields.echelle.value;
    $('val-echelle').textContent = fmt(scale);
    $('expansion-resultat').textContent = 'Distance entre A et B : ' + fmt(scale) + ' unité' + (scale > 1 ? 's' : '');
    const beta = +fields.vitesse.value / 100;
    $('val-vitesse').textContent = fmt(beta * 100, 1) + ' % de c';
    fields.vitesse.setAttribute('aria-valuetext', fmt(beta * 100, 1) + ' pour cent de la vitesse de la lumière');
    $('temps-mobile').textContent = fmt(movingClockRatio(beta) * 10) + ' ans';
    const radius = +fields.rayon.value;
    $('val-rayon').textContent = fmt(radius) + ' rₛ';
    fields.rayon.setAttribute('aria-valuetext', fmt(radius) + ' rayons d’horizon');
    $('temps-gravite').textContent = fmt(stationaryClockRatio(radius) * 10) + ' ans';
    $('val-impact').textContent = fmt(+fields.impact.value) + ' rₛ';
    fields.impact.setAttribute('aria-valuetext', fmt(+fields.impact.value) + ' rayons de Schwarzschild');
    if (!changed || changed === 'impact') updateRay();
    $('sort-lumiere').textContent = ray.captured ? 'Le rayon franchit l’horizon : il est capturé.' : ray.escaped ? 'Le rayon est dévié puis repart.' : 'Le rayon reste proche de l’orbite critique dans cette intégration.';
    dirty = true;
  }
  Object.entries(fields).forEach(([id, field]) => field.addEventListener('input', () => updateControls(id)));
  $('univ-choix').addEventListener('change', event => {
    steps[Number(event.target.value)].scrollIntoView({behavior: frozen ? 'instant' : 'smooth', block: 'start'});
  });
  function setFrozen(value) {
    frozen = value;
    $('univ-motion').setAttribute('aria-pressed', String(frozen));
    $('univ-motion').textContent = frozen ? 'Animer les schémas' : 'Figer les animations';
    document.dispatchEvent(new CustomEvent('aeternam-motion', {detail: {frozen}}));
    dirty = true;
  }
  $('univ-motion').hidden = false;
  $('univ-motion').addEventListener('click', () => setFrozen(!frozen));
  reduce.addEventListener('change', event => setFrozen(event.matches));
  addEventListener('scroll', () => { scrollDirty = true; }, {passive: true});
  addEventListener('resize', () => { scrollDirty = true; dirty = true; }, {passive: true});
  document.addEventListener('visibilitychange', () => { lastTime = 0; dirty = true; });
  document.fonts.ready.then(() => { scrollDirty = true; dirty = true; });
  function frame(now) {
    const dt = lastTime ? Math.min((now - lastTime) / 1000, .1) : 0; lastTime = now;
    if (!document.hidden) {
      if (!frozen) animationTime += dt;
      if (scrollDirty) syncScroll();
      if ((dirty || !frozen) && now - lastPaint >= 32) {
        for (const s of surfaces) {
          if (!s.visible || !s.w || !s.h) continue;
          s.ctx.clearRect(0, 0, s.w, s.h);
          s.ctx.save(); s.ctx.beginPath(); s.ctx.rect(0, 0, s.w, s.h); s.ctx.clip();
          drawingFunctions[s.canvas.id](s, now);
          s.ctx.restore();
        }
        lastPaint = now; dirty = false;
      }
    }
    requestAnimationFrame(frame);
  }
  document.documentElement.classList.add('univers-js');
  stage.dataset.epoch = steps[0].id;
  surfaces.forEach(resize);
  setFrozen(frozen); updateControls(); syncScroll();
  requestAnimationFrame(frame);
}
