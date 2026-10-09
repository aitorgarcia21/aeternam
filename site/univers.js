import {movingClockRatio, stationaryClockRatio, traceLight} from './univers-physique.mjs?v=__PHYSIQUE_VERSION__';
import {createCosmos} from './univers-scene.mjs?v=__SCENE_VERSION__';

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
  let epoch = -2, phaseProgress = 0, sceneFrom = 12, sceneTo = 12, sceneBlend = 0;
  const steps = [...root.querySelectorAll('.univ-etape')];
  const sceneContainer = root.querySelector('.univ-scenes');
  const schemaLayer = root.querySelector('.univ-schema-layer');
  const schemas = [...root.querySelectorAll('.univ-schema')];
  let activeSchema = null;
  const menu = root.querySelector('.univ-sommaire');
  const menuLinks = [...menu.querySelectorAll('a')];
  const chapters = ['histoire', 'espace-temps', 'avant-apres', 'sources-univers'].map($);
  const cosmos = createCosmos($('cosmos-canvas'));
  const stage = cosmos.canvas;
  const surfaces = [...root.querySelectorAll('main canvas:not(#cosmos-canvas)')].map(canvas => ({
    canvas, ctx: canvas.getContext('2d'), w: 0, h: 0, visible: false,
  }));
  if (surfaces.some(surface => !surface.ctx)) return;
  const fields = Object.fromEntries(['coord-x', 'coord-y', 'coord-z', 'coord-t', 'echelle', 'vitesse', 'rayon', 'impact'].map(id => [id, $(id)]));
  let ray = traceLight(Number(fields.impact.value));
  schemas.forEach(figure => { figure.hidden = true; schemaLayer.append(figure); });

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
      if (entry.target === cosmos.canvas) cosmos.resize();
    }
    root.style.setProperty('--nav-height', menu.getBoundingClientRect().height + 'px');
    scrollDirty = true;
  });
  surfaces.forEach(surface => resizeObserver.observe(surface.canvas));
  resizeObserver.observe(menu);
  resizeObserver.observe(cosmos.canvas);
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
    const readingLine = mobile ? menu.offsetHeight + innerHeight * .36 + 90 : innerHeight * .58;
    let next = -1;
    steps.forEach((step, i) => { if (step.getBoundingClientRect().top <= readingLine) next = i; });
    const box = (next < 0 ? $('apercu') : steps[next]).getBoundingClientRect();
    phaseProgress = clamp((readingLine - box.top) / Math.max(1, box.height));
    sceneFrom = next < 1 ? 12 : next - 1;
    sceneTo = next < 0 ? 12 : next;
    sceneBlend = next < 0 ? 0 : clamp(phaseProgress * 5);
    sceneBlend = sceneBlend * sceneBlend * (3 - 2 * sceneBlend);
    if (reduce.matches) { sceneFrom = sceneTo; sceneBlend = 1; }
    if (next !== epoch) {
      epoch = next;
      activeSchema = schemas.find(figure => figure.dataset.schema === steps[epoch]?.id) || null;
      schemas.forEach(figure => { figure.hidden = figure !== activeSchema; });
      sceneContainer.dataset.diagram = String(Boolean(activeSchema));
      cosmos.canvas.dataset.epoch = epoch < 0 ? 'apercu' : steps[epoch].id;
      $('histoire').dataset.intro = String(epoch < 0);
    }
    let chapterIndex = 0;
    chapters.forEach((chapter, i) => { if (chapter.getBoundingClientRect().top <= menu.offsetHeight + 140) chapterIndex = i; });
    menuLinks.forEach((link, i) => i === chapterIndex ? link.setAttribute('aria-current', 'location') : link.removeAttribute('aria-current'));
    root.dataset.chapter = String(chapterIndex);
    dirty = true; scrollDirty = false;
  }

  function drawStory() {
    if (!activeSchema) cosmos.draw({from:sceneFrom,to:sceneTo,blend:sceneBlend,time:animationTime,phase:phaseProgress});
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
    const scale = Math.min(w / 22, h / 11);
    const p = (r, a) => [w * .5 + r * Math.cos(a) * scale, h * .88 + r * Math.sin(a) * scale * .36 - 2 * Math.sqrt(r - 1) * scale * .95];
    for (let radius = 1; radius <= 10; radius += .25) {
      const pts = Array.from({length: 101}, (_, i) => p(radius, i / 100 * tau));
      line(ctx, pts, palette.gold, .29);
    }
    for (let k = 0; k < 48; k++) {
      const pts = Array.from({length: 91}, (_, i) => p(1 + i / 10, k / 48 * tau));
      line(ctx, pts, palette.gold, .29);
    }
    line(ctx, Array.from({length: 101}, (_, i) => p(1, i / 100 * tau)), palette.gold, .85, 1.6);
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
    glow(ctx,cx,cy,scale*2.1,true,.38);
    ctx.beginPath(); ctx.arc(cx, cy, scale, 0, tau); ctx.fillStyle = '#070a09'; ctx.fill();
    ctx.strokeStyle = palette.sage; ctx.lineWidth = 1.2; ctx.stroke();
    line(ctx, ray.points.map(p), palette.gold, .9, 1.7);
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
    'cosmos-overlay': drawStory,
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
    Object.values(fields).forEach(field => field.style.setProperty('--range', ((+field.value - +field.min) / (+field.max - +field.min) * 100) + '%'));
    root.querySelectorAll('[data-field]').forEach(button => button.setAttribute('aria-pressed', String(+fields[button.dataset.field].value === +button.dataset.value)));
    dirty = true;
  }
  Object.entries(fields).forEach(([id, field]) => field.addEventListener('input', () => updateControls(id)));
  root.querySelectorAll('[data-field]').forEach(button => button.addEventListener('click',()=> { fields[button.dataset.field].value = button.dataset.value; updateControls(button.dataset.field); }));
  function setFrozen(value) {
    frozen = value;
    $('univ-motion').setAttribute('aria-pressed', String(frozen));
    $('univ-motion').title = frozen ? 'Animer les schémas' : 'Figer les animations';
    $('univ-motion').setAttribute('aria-label',frozen ? 'Animer les schémas' : 'Figer les animations');
    document.dispatchEvent(new CustomEvent('aeternam-motion', {detail: {frozen}}));
    dirty = true;
  }
  $('univ-motion').hidden = false;
  $('univ-motion').addEventListener('click', () => setFrozen(!frozen));
  reduce.addEventListener('change', event => setFrozen(event.matches));
  addEventListener('scroll', () => { scrollDirty = true; }, {passive: true});
  addEventListener('resize', () => { cosmos.resize(); scrollDirty = true; dirty = true; }, {passive: true});
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
  stage.dataset.epoch = 'apercu';
  surfaces.forEach(resize);
  setFrozen(frozen); updateControls(); syncScroll();
  requestAnimationFrame(frame);
}
