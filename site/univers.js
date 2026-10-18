import {movingClockRatio, stationaryClockRatio, traceLight} from './univers-physique.mjs?v=__PHYSIQUE_VERSION__';
import {createCosmos, SCENES} from './univers-scene.mjs?v=__SCENE_VERSION__';

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
  const menu = root.querySelector('.univ-sommaire');
  const menuScroller = menu.querySelector('.univ-chapitres');
  const menuLinks = [...menu.querySelectorAll('a')];
  const chapters = menuLinks.map(link => $(link.hash.slice(1)));
  let chapterIndex = -1;
  // Deux récits au défilement : l'Univers, puis le cerveau et les frontières. Chacun a sa scène fixe.
  const stories = [...root.querySelectorAll('.univ-histoire')].map(section => ({
    section,
    cosmos: createCosmos(section.querySelector('.cosmos-canvas')),
    overlay: section.querySelector('.cosmos-overlay'),
    container: section.querySelector('.univ-scenes'),
    artLayer: section.querySelector('.univ-art-layer'),
    artworks: [...section.querySelectorAll('.univ-illustration')],
    legend: section.querySelector('.cosmos-legende'),
    opening: section.querySelector('.univ-ouverture'),
    steps: [...section.querySelectorAll('.univ-etape')],
    introScene: Number(section.dataset.sceneIntro),
    epoch: -2, progress: 0, from: 0, to: 0, blend: 0, art: null,
  }));
  const surfaces = [...root.querySelectorAll('main canvas:not(.cosmos-canvas)')].map(canvas => ({
    canvas, ctx: canvas.getContext('2d'), w: 0, h: 0, visible: false,
    story: stories.find(story => story.overlay === canvas) || null,
  }));
  if (surfaces.some(surface => !surface.ctx)) return;
  const fields = Object.fromEntries(['coord-x', 'coord-y', 'coord-z', 'coord-t', 'echelle', 'vitesse', 'rayon', 'impact', 'electrodes']
    .filter(id => $(id)).map(id => [id, $(id)]));
  let ray = traceLight(Number(fields.impact.value));
  let electrodesPending = null;
  for (const story of stories) {
    story.artworks.forEach(figure => {
      figure.hidden = true; story.artLayer.append(figure);
      const img = figure.querySelector('img');
      const loaded = () => { figure.dataset.loaded = String(img.naturalWidth > 0); scrollDirty = true; dirty = true; };
      img.addEventListener('load', loaded);
      img.addEventListener('error', loaded);
      if (img.complete) loaded();
    });
  }

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
      const story = stories.find(item => item.cosmos.canvas === entry.target);
      if (story) story.cosmos.resize();
    }
    root.style.setProperty('--nav-height', menu.getBoundingClientRect().height + 'px');
    scrollDirty = true;
  });
  surfaces.forEach(surface => resizeObserver.observe(surface.canvas));
  resizeObserver.observe(menu);
  for (const story of stories) {
    resizeObserver.observe(story.cosmos.canvas);
    story.steps.forEach(step => resizeObserver.observe(step));
  }
  const visibility = new IntersectionObserver(entries => {
    for (const entry of entries) {
      const s = surfaces.find(surface => surface.canvas === entry.target);
      if (s) s.visible = entry.isIntersecting;
    }
    dirty = true;
  }, {rootMargin: '40px'});
  surfaces.forEach(surface => visibility.observe(surface.canvas));

  function syncStory(story) {
    const mobile = innerWidth <= 760;
    const readingLine = mobile ? menu.offsetHeight + story.container.offsetHeight + 72 : innerHeight * .58;
    let next = -1;
    story.steps.forEach((step, i) => { if (step.getBoundingClientRect().top <= readingLine) next = i; });
    const current = next < 0 ? story.opening : story.steps[next];
    const box = current.getBoundingClientRect();
    const sceneOf = i => i < 0 ? story.introScene : Number(story.steps[i].dataset.scene);
    story.progress = clamp((readingLine - box.top) / Math.max(1, box.height));
    story.from = sceneOf(Math.max(-1, next - 1));
    story.to = sceneOf(next);
    story.blend = next < 0 ? 0 : clamp(story.progress * 5);
    story.blend = story.blend * story.blend * (3 - 2 * story.blend);
    if (reduce.matches) { story.from = story.to; story.blend = 1; }
    if (next !== story.epoch) {
      story.epoch = next;
      story.art = story.artworks.find(figure => figure.dataset.art === current.id) || null;
      story.artworks.forEach(figure => { figure.hidden = figure !== story.art; });
      if (story.art) story.art.querySelector('img').loading = 'eager';
      // Une seule scène d'avance ; ne pas télécharger toute la galerie à l'ouverture.
      if (!navigator.connection?.saveData) {
        const upcoming = story.artworks.find(figure => figure.dataset.art === story.steps[next + 1]?.id);
        if (upcoming) upcoming.querySelector('img').loading = 'eager';
      }
      story.cosmos.canvas.dataset.epoch = current.id;
      story.section.dataset.intro = String(next < 0);
      if (story.legend) story.legend.textContent = current.dataset.legende || story.legend.dataset.defaut;
    }
    story.container.dataset.art = String(story.art?.dataset.loaded === 'true');
    story.container.dataset.scene = current.id;
  }

  function syncScroll() {
    stories.forEach(syncStory);
    let index = 0;
    chapters.forEach((chapter, i) => { if (chapter && chapter.getBoundingClientRect().top <= menu.offsetHeight + 140) index = i; });
    menuLinks.forEach((link, i) => i === index ? link.setAttribute('aria-current', 'location') : link.removeAttribute('aria-current'));
    if (index !== chapterIndex) {
      chapterIndex = index;
      // Sur un écran étroit, les chapitres défilent latéralement : garder le chapitre courant visible.
      const link = menuLinks[index];
      if (menuScroller.scrollWidth > menuScroller.clientWidth) {
        menuScroller.scrollTo({left: link.offsetLeft - (menuScroller.clientWidth - link.offsetWidth) / 2, behavior: frozen ? 'auto' : 'smooth'});
      }
    }
    root.dataset.chapter = String(index);
    dirty = true; scrollDirty = false;
  }

  function drawStory(story) {
    if (story.art?.dataset.loaded === 'true') {
      const scale = frozen ? 1 : 1.015 + story.progress * .045;
      const drift = frozen ? 0 : Math.sin(animationTime * .16) * 3 - story.progress * 8;
      story.art.querySelector('.univ-image-wrap').style.transform = `translateY(${drift}px) scale(${scale})`;
    } else {
      story.cosmos.draw({from: story.from, to: story.to, blend: story.blend, time: animationTime, phase: story.progress});
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
    const face = ctx.createRadialGradient(x - r * .3, y - r * .4, 0, x, y, r);
    face.addColorStop(0, `rgba(${rgb(color)},.13)`);
    face.addColorStop(.7, `rgba(${rgb(color)},.035)`);
    face.addColorStop(1, `rgba(${rgb(color)},.08)`);
    ctx.fillStyle = face; ctx.beginPath(); ctx.arc(x, y, r, 0, tau); ctx.fill();
    ctx.strokeStyle = color; ctx.globalAlpha = .7; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.arc(x, y, r, 0, tau); ctx.stroke(); ctx.globalAlpha = 1;
    for (let i = 0; i < 60; i++) {
      const a = i / 60 * tau - Math.PI / 2, length = i % 5 === 0 ? 9 : 3;
      line(ctx, [[x + Math.cos(a) * (r - length), y + Math.sin(a) * (r - length)], [x + Math.cos(a) * (r - 2), y + Math.sin(a) * (r - 2)]], color, i % 5 === 0 ? .8 : .35);
    }
    ctx.shadowColor = color; ctx.shadowBlur = 8;
    line(ctx, [[x, y], [x + Math.cos(angle - Math.PI / 2) * r * .78, y + Math.sin(angle - Math.PI / 2) * r * .78]], color, .9, 1.6);
    ctx.shadowBlur = 0;
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
  let gravityMesh = null;
  function drawGravity({ctx, w, h}) {
    const scale = Math.min(w / 22, h / 11);
    const p = (r, a) => [w * .5 + r * Math.cos(a) * scale, h * .88 + r * Math.sin(a) * scale * .36 - 2 * Math.sqrt(r - 1) * scale * .95];
    if (!gravityMesh || gravityMesh.w !== w || gravityMesh.h !== h) {
      const canvas = document.createElement('canvas'), dpr = Math.min(devicePixelRatio || 1, 2);
      canvas.width = w * dpr; canvas.height = h * dpr;
      const mesh = canvas.getContext('2d'); mesh.scale(dpr, dpr);
      const faces = [];
      for (let r = 1; r < 10; r += .25) for (let k = 0; k < 64; k++) {
        const a = k / 64 * tau, b = (k + 1) / 64 * tau;
        const pts = [p(r, a), p(r + .25, a), p(r + .25, b), p(r, b)];
        // Profondeur dans la direction du regard, indépendante de la hauteur à l'écran.
        const depth = (r + .125) * Math.sin(a + tau / 128) * .95 + 2 * Math.sqrt(r + .125 - 1) * .36;
        faces.push({pts, r, a, depth});
      }
      faces.sort((a, b) => a.depth - b.depth);
      for (const {pts, r, a} of faces) {
        const light = .5 + .5 * Math.cos(a + 1.2), rim = Math.pow(1 - r / 11, 1.4);
        mesh.beginPath(); mesh.moveTo(...pts[0]); pts.slice(1).forEach(pt => mesh.lineTo(...pt)); mesh.closePath();
        mesh.fillStyle = `rgb(${Math.round(20 + light * 60 + rim * 28)},${Math.round(28 + light * 47 + rim * 18)},${Math.round(34 + light * 32)})`;
        mesh.fill();
        mesh.strokeStyle = `rgba(207,196,156,${.11 + light * .16})`; mesh.lineWidth = .6; mesh.stroke();
      }
      gravityMesh = {canvas, w, h};
    }
    ctx.drawImage(gravityMesh.canvas, 0, 0, w, h);
    ctx.shadowColor = palette.gold; ctx.shadowBlur = 12;
    line(ctx, Array.from({length: 101}, (_, i) => p(1, i / 100 * tau)), palette.gold, .95, 2);
    ctx.shadowBlur = 0;
    const radius = +fields.rayon.value, pos = p(radius, -.7);
    glow(ctx, pos[0], pos[1], 20, true); dot(ctx, pos[0], pos[1], 4, palette.gold);
    label(ctx, 'Horloge à r = ' + fmt(radius) + ' rₛ', pos[0], pos[1] - 20, pos[0] > w * .65 ? 'right' : 'center', palette.text);
    label(ctx, 'Horizon · rₛ', w / 2, h * .88 + 27);
    const ratio = stationaryClockRatio(radius);
    clock(ctx, w * .83, h * .16, Math.min(34, w * .09), animationTime * .8 * ratio + .3, palette.gold);
  }
  function updateRay() {
    ray = traceLight(+fields.impact.value);

  }
  function drawLight({ctx, w, h}) {
    const impact = +fields.impact.value;
    const scale = Math.min((w - 50) / 20, (h - 70) / (impact + 4));
    const cx = w / 2, cy = h - 52 - scale * 1.8;
    const p = point => [cx + point[0] * scale, cy - point[1] * scale];
    ctx.setLineDash([3, 6]);
    ctx.beginPath(); ctx.arc(cx, cy, scale * 1.5, 0, tau); ctx.strokeStyle = palette.muted; ctx.globalAlpha = .4; ctx.stroke();
    line(ctx, [p([-20, +fields.impact.value]), p([20, +fields.impact.value])], palette.muted, .3);
    ctx.setLineDash([]); ctx.globalAlpha = 1;
    const halo = ctx.createRadialGradient(cx, cy, scale * .93, cx, cy, scale * 2.7);
    halo.addColorStop(0, 'rgba(159,187,216,.35)'); halo.addColorStop(.12, 'rgba(159,187,216,.08)'); halo.addColorStop(1, 'rgba(159,187,216,0)');
    ctx.fillStyle = halo; ctx.beginPath(); ctx.arc(cx, cy, scale * 2.7, 0, tau); ctx.fill();
    ctx.beginPath(); ctx.arc(cx, cy, scale, 0, tau); ctx.fillStyle = '#070a09'; ctx.fill();
    ctx.strokeStyle = palette.sage; ctx.lineWidth = 1.2; ctx.stroke();
    ctx.shadowColor = palette.gold; ctx.shadowBlur = 12;
    line(ctx, ray.points.map(p), palette.gold, .97, 1.8);
    ctx.shadowBlur = 0;
    const visible = ray.points.map(p).filter(point => point[0] > 0 && point[0] < w && point[1] > 0 && point[1] < h - 25);
    if (visible.length > 1) {
      const at = (animationTime * .12 + .32) % 1 * (visible.length - 1), index = Math.floor(at), fraction = at - index;
      const pos = [lerp(visible[index][0],visible[index+1][0],fraction),lerp(visible[index][1],visible[index+1][1],fraction)];
      glow(ctx,...pos,14,true);dot(ctx,...pos,3,palette.gold);
    }
    label(ctx, 'Horizon', cx, cy + scale + 24, 'center', palette.text);
    label(ctx, 'Sphère des photons : 1,5 rₛ', cx, h - 13);
    label(ctx, 'Rayon incident', 18, Math.max(20,cy-impact*scale-18), 'left', palette.text);
  }
  const drawingFunctions = {
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
    $('vitesse-observation').textContent = beta === 0 ? 'Au repos dans ce référentiel, les deux durées sont identiques.' : 'À cette vitesse, l’horloge mobile accumule ' + fmt((1-movingClockRatio(beta))*10) + ' ans de moins.';
    const radius = +fields.rayon.value;
    $('val-rayon').textContent = fmt(radius) + ' rₛ';
    fields.rayon.setAttribute('aria-valuetext', fmt(radius) + ' rayons d’horizon');
    $('temps-gravite').textContent = fmt(stationaryClockRatio(radius) * 10) + ' ans';
    $('position-horloge').firstChild.textContent = 'À ' + fmt(radius) + ' rayons d’horizon';
    $('val-impact').textContent = fmt(+fields.impact.value) + ' rₛ';
    fields.impact.setAttribute('aria-valuetext', fmt(+fields.impact.value) + ' rayons de Schwarzschild');
    if (!changed || changed === 'impact') updateRay();
    $('sort-lumiere').textContent = ray.captured ? 'Le rayon franchit l’horizon : il est capturé.' : ray.escaped ? 'Le rayon est dévié puis repart.' : 'Le rayon reste proche de l’orbite critique dans cette intégration.';
    if (fields.electrodes) {
      const side = +fields.electrodes.value, count = side * side;
      $('val-electrodes').textContent = count.toLocaleString('fr-FR');
      fields.electrodes.setAttribute('aria-valuetext', count.toLocaleString('fr-FR') + ' électrodes');
      if (!changed || changed === 'electrodes') electrodesPending = count;
    }
    Object.values(fields).forEach(field => field.style.setProperty('--range', ((+field.value - +field.min) / (+field.max - +field.min) * 100) + '%'));
    root.querySelectorAll('[data-field]').forEach(button => button.setAttribute('aria-pressed', String(+fields[button.dataset.field].value === +button.dataset.value)));
    dirty = true;
  }
  Object.entries(fields).forEach(([id, field]) => field.addEventListener('input', () => updateControls(id)));
  root.querySelectorAll('[data-field]').forEach(button => button.addEventListener('click',()=> { fields[button.dataset.field].value = button.dataset.value; updateControls(button.dataset.field); }));
  function setFrozen(value) {
    frozen = value;
    root.dataset.frozen = String(frozen);
    $('univ-motion').setAttribute('aria-pressed', String(frozen));
    $('univ-motion').title = frozen ? 'Reprendre les animations' : 'Figer les animations';
    $('univ-motion').setAttribute('aria-label',frozen ? 'Reprendre les animations' : 'Figer les animations');
    document.dispatchEvent(new CustomEvent('aeternam-motion', {detail: {frozen}}));
    dirty = true;
  }
  $('univ-motion').hidden = false;
  $('univ-motion').addEventListener('click', () => setFrozen(!frozen));
  reduce.addEventListener('change', event => setFrozen(event.matches));
  addEventListener('scroll', () => { scrollDirty = true; }, {passive: true});
  addEventListener('resize', () => { stories.forEach(story => story.cosmos.resize()); scrollDirty = true; dirty = true; }, {passive: true});
  document.addEventListener('visibilitychange', () => { lastTime = 0; dirty = true; });
  document.fonts.ready.then(() => {
    // Le passage des images dans la scène fixe change la hauteur du document.
    // Replacer un lien direct une fois cette disposition et les polices prêtes.
    const anchor = document.getElementById(location.hash.slice(1));
    if (anchor) anchor.scrollIntoView({behavior: 'instant'});
    scrollDirty = true; dirty = true;
  });
  function frame(now) {
    const dt = lastTime ? Math.min((now - lastTime) / 1000, .1) : 0; lastTime = now;
    if (!document.hidden) {
      if (!frozen) animationTime += dt;
      if (scrollDirty) syncScroll();
      if (electrodesPending !== null) {
        // Une seule reconstruction par image, même si le curseur envoie plusieurs valeurs.
        for (const library of new Set(stories.map(story => story.cosmos.library))) library.configure(SCENES.vision, {electrodes: electrodesPending});
        electrodesPending = null; dirty = true;
      }
      if ((dirty || !frozen) && now - lastPaint >= 32) {
        for (const s of surfaces) {
          if (!s.visible || !s.w || !s.h) continue;
          if (s.story) { drawStory(s.story); continue; }
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
  surfaces.forEach(resize);
  setFrozen(frozen); updateControls(); syncScroll();
  requestAnimationFrame(frame);
}
