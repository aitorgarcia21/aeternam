// Le trou noir du site, un trou noir de Schwarzschild calculé pour de vrai. Chaque pixel suit à
// rebours un rayon de lumière dans l'espace-temps courbé (orbite de Binet, u'' + u = 3/2 u²)
// jusqu'au disque d'accrétion, au ciel ou à l'horizon ; le disque tourne à la vitesse
// képlérienne, avec décalages Doppler et gravitationnel.
// Accueil (.ciel) : la caméra tombe dedans, d'elle-même au bout de quelques secondes ou dès
// qu'on fait défiler, tape ou appuie sur une touche. Sous la sphère de photons, tout est noir
// devant soi : on est avalé, et le titre est à l'intérieur.
// Ouverture du chapitre Relativité (.univ-trou-noir) : le même trou noir, vu de loin, animé
// seulement quand on le voit et figé avec les autres animations du parcours.
// Thème Relativité (.scene-sujet de la scène 19) : une seule image, immobile, comme les autres
// scènes de thème ; sans WebGL, theme.js y dessine l'illustration en nuage de points.
(function () {
  var racine = document.documentElement;

  // Unités : rayon de Schwarzschild = 1 ; sphère de photons à 1,5 ; disque de 2 à 14.
  var R_DEPART = 26;                // distance de la caméra à l'arrivée
  var R_FIN = 1.45;                 // sous 1,5, tout est noir devant soi
  var ATTENTE = 5;                  // secondes avant que la chute commence d'elle-même
  var CHUTE = 6, CHUTE_VITE = 3.4;  // durée de la chute, seule ou provoquée
  var NOIR = 0.4;                   // un instant de noir complet avant d'entrer
  var calme = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var tactile = !!(window.matchMedia && window.matchMedia('(pointer: coarse)').matches);

  var PRECISION = '#ifdef GL_FRAGMENT_PRECISION_HIGH\nprecision highp float;\n#else\nprecision mediump float;\n#endif\n';
  var SOMMETS = 'attribute vec2 a; varying vec2 v_uv;\n' +
    'void main() { v_uv = a * 0.5 + 0.5; gl_Position = vec4(a, 0.0, 1.0); }';

  var TRACE = PRECISION + [
    'varying vec2 v_uv;',
    'uniform vec2 u_tan;',
    'uniform vec3 u_cam, u_av, u_dr, u_ha;',
    'uniform float u_temps, u_pas, u_pix, u_loin, u_expo;',

    'float h11(float p) { p = fract(p * 0.1031); p *= p + 33.33; p *= p + p; return fract(p); }',
    'float h13(vec3 p) { p = fract(p * 0.1031); p += dot(p, p.zyx + 31.32); return fract((p.x + p.y) * p.z); }',
    'vec3 h33(vec3 p) { p = fract(p * vec3(0.1031, 0.1030, 0.0973)); p += dot(p, p.yxz + 33.33); return fract((p.xxy + p.yxx) * p.zyx); }',
    'float bruit1(float x) { float i = floor(x); float f = fract(x); f = f * f * (3.0 - 2.0 * f); return mix(h11(i), h11(i + 1.0), f); }',
    'float bruit2(vec2 p) {',
    '  vec2 i = floor(p); vec2 f = fract(p); f = f * f * (3.0 - 2.0 * f);',
    '  return mix(mix(h13(vec3(i, 1.0)), h13(vec3(i + vec2(1.0, 0.0), 1.0)), f.x),',
    '             mix(h13(vec3(i + vec2(0.0, 1.0), 1.0)), h13(vec3(i + 1.0, 1.0)), f.x), f.y);',
    '}',
    'float bruit3(vec3 p) {',
    '  vec3 i = floor(p); vec3 f = fract(p); f = f * f * (3.0 - 2.0 * f); vec2 e = vec2(1.0, 0.0);',
    '  return mix(mix(mix(h13(i), h13(i + e.xyy), f.x), mix(h13(i + e.yxy), h13(i + e.xxy), f.x), f.y),',
    '             mix(mix(h13(i + e.yyx), h13(i + e.xyx), f.x), mix(h13(i + e.yxx), h13(i + e.xxx), f.x), f.y), f.z);',
    '}',

    // Couleur d'un corps noir (approximation), en valeurs linéaires.
    'vec3 corpsNoir(float T) {',
    '  float t = clamp(T, 1500.0, 40000.0) / 100.0;',
    '  vec3 c;',
    '  c.r = t <= 66.0 ? 1.0 : 1.292936 * pow(max(t - 60.0, 1.0), -0.1332048);',
    '  c.g = t <= 66.0 ? 0.3900816 * log(t) - 0.6318414 : 1.129891 * pow(max(t - 60.0, 1.0), -0.0755148);',
    '  c.b = t >= 66.0 ? 1.0 : (t <= 19.0 ? 0.0 : 0.5432068 * log(t - 10.0) - 1.1962541);',
    '  c = clamp(c, 0.0, 1.0);',
    '  return c * c;',
    '}',

    // Ciel de fond : étoiles et une traînée de nébuleuse, dans la direction n.
    'vec3 fond(vec3 n) {',
    '  vec3 c = vec3(0.002, 0.003, 0.007);',
    '  float z = dot(n, vec3(0.0, 0.6, 0.8)) / 0.3;',
    '  float bande = exp(-z * z);',
    '  float neb = 0.6 * bruit3(n * 3.0) + 0.4 * bruit3(n * 8.0);',
    '  c += vec3(0.010, 0.016, 0.040) * bande * neb * neb * 2.5;',
    '  vec3 p = n * 80.0;',
    '  vec3 id = floor(p);',
    '  vec3 s = normalize(id + 0.25 + 0.5 * h33(id)) * 80.0;',
    '  float taille = max(0.035, 0.6 * u_pix);',
    '  float eclat = pow(h13(id + 11.7), 8.0);',
    '  float etoile = step(0.9, h13(id)) * (0.1 + 6.0 * eclat) * exp(-dot(p - s, p - s) / (taille * taille));',
    '  return c + etoile * mix(vec3(0.7, 0.8, 1.0), vec3(1.0, 0.88, 0.75), h13(id + 5.3));',
    '}',

    // Disque d'accrétion mince, au point p du plan y = 0, traversé par un rayon de vitesse v.
    // Rend la lumière émise vers la caméra (rgb) et l'opacité (a).
    'vec4 disque(vec3 p, vec3 v, float vinf, float laps) {',
    '  float r = length(p.xz);',
    '  if (r < 2.0 || r > 14.0) return vec4(0.0);',
    '  float om = 0.70710678 / (r * sqrt(r));',                    // vitesse angulaire képlérienne
    '  float a = -om * u_temps * 1.6;',
    '  vec2 q = mat2(cos(a), sin(a), -sin(a), cos(a)) * vec2(p.x, -p.z);',
    '  float anneaux = 0.7 * bruit1(r * 5.0) + 0.3 * bruit1(r * 13.0 + 7.0);',
    '  anneaux = 3.2 * pow(anneaux, 4.0);',
    '  float grumeaux = 0.45 + 1.1 * bruit2(q * 1.6 + 3.0) * bruit2(q * 0.7 - 5.0);',
    '  float dens = anneaux * grumeaux * smoothstep(2.0, 3.2, r) * (1.0 - smoothstep(6.0, 12.0, r));',
    '  float x3 = 3.0 / r;',
    '  float prof = (r > 3.0 ? x3 * x3 * x3 * (1.0 - sqrt(x3)) / 0.0567 : 0.0)',
    '             + 0.35 * smoothstep(2.0, 3.0, r) * (1.0 - smoothstep(3.0, 4.5, r));',
    '  float bphi = (p.x * v.z - p.z * v.x) / vinf;',                // moment cinétique du photon / énergie
    '  float g = sqrt(max(1.0 - 1.5 / r, 0.02)) / max(1.0 - om * bphi, 0.1) / laps;',
    '  float T = 16000.0 * pow(max(prof, 0.02), 0.25);',
    '  vec3 c = corpsNoir(T * g) * (1.2 * dens * prof * g * g * g);',
    '  return vec4(c, clamp(0.7 * dens, 0.0, 0.9));',
    '}',

    'void main() {',
    '  vec2 s = v_uv * 2.0 - 1.0;',
    '  vec3 d = normalize(u_av + s.x * u_tan.x * u_dr + s.y * u_tan.y * u_ha);',
    // Direction vue par un observateur immobile : la composante radiale est contractée.
    '  float rc = length(u_cam);',
    '  vec3 nr = u_cam / rc;',
    '  float laps = sqrt(max(1.0 - 1.0 / rc, 0.0001));',
    '  vec3 v = d - (1.0 - laps) * dot(d, nr) * nr;',
    '  vec3 x = u_cam;',
    '  vec3 mom = cross(x, v);',
    '  float h2 = dot(mom, mom);',
    '  float vinf = sqrt(max(dot(v, v) - h2 / (rc * rc * rc), 0.000001));',
    '  float r = rc;',
    '  vec3 acc = -1.5 * h2 * x / (r * r * r * r * r);',
    '  vec3 col = vec3(0.0);',
    '  float T = 1.0;',
    '  float sorti = 0.0;',
    '  for (int i = 0; i < 240; i++) {',
    '    float dt = u_pas * r * mix(0.35, 1.0, smoothstep(1.5, 6.0, r)) / length(v);',
    '    vec3 xn = x + v * dt + 0.5 * acc * dt * dt;',
    '    float rn = length(xn);',
    '    vec3 accn = -1.5 * h2 * xn / (rn * rn * rn * rn * rn);',
    '    vec3 vn = v + 0.5 * (acc + accn) * dt;',
    '    if (x.y * xn.y < 0.0) {',
    '      float f = x.y / (x.y - xn.y);',
    '      vec4 e = disque(mix(x, xn, f), mix(v, vn, f), vinf, laps);',
    '      col += T * e.rgb;',
    '      T *= 1.0 - e.a;',
    '    }',
    '    x = xn; v = vn; acc = accn; r = rn;',
    '    if (r < 1.0 || T < 0.01) { T = 0.0; break; }',
    '    if (r > u_loin && dot(x, v) > 0.0) { sorti = 1.0; break; }',
    '  }',
    '  if (sorti < 0.5 && r > rc && dot(x, v) > 0.0) sorti = 1.0;',
    '  col += sorti * T * fond(normalize(v)) / (laps * laps);',
    '  col *= u_expo;',
    '  col = (col * (2.51 * col + 0.03)) / (col * (2.43 * col + 0.59) + 0.14);',
    '  gl_FragColor = vec4(sqrt(clamp(col, 0.0, 1.0)), 1.0);',
    '}'
  ].join('\n');

  // Halo : on garde ce qui brille, à un quart de la définition, puis on le floute.
  var SEUIL = PRECISION + [
    'varying vec2 v_uv;',
    'uniform sampler2D u_tex;',
    'uniform vec2 u_texel;',
    'void main() {',
    '  vec3 c = 0.25 * (texture2D(u_tex, v_uv + u_texel * vec2(-1.0, -1.0)).rgb',
    '                 + texture2D(u_tex, v_uv + u_texel * vec2(1.0, -1.0)).rgb',
    '                 + texture2D(u_tex, v_uv + u_texel * vec2(-1.0, 1.0)).rgb',
    '                 + texture2D(u_tex, v_uv + u_texel * vec2(1.0, 1.0)).rgb);',
    '  gl_FragColor = vec4(max(c - 0.4, 0.0) * 1.7, 1.0);',
    '}'
  ].join('\n');

  var FLOU = PRECISION + [
    'varying vec2 v_uv;',
    'uniform sampler2D u_tex;',
    'uniform vec2 u_dir;',
    'void main() {',
    '  vec3 c = 0.19648 * texture2D(u_tex, v_uv).rgb;',
    '  c += 0.29691 * (texture2D(u_tex, v_uv + u_dir * 1.41176).rgb + texture2D(u_tex, v_uv - u_dir * 1.41176).rgb);',
    '  c += 0.09447 * (texture2D(u_tex, v_uv + u_dir * 3.29412).rgb + texture2D(u_tex, v_uv - u_dir * 3.29412).rgb);',
    '  c += 0.01038 * (texture2D(u_tex, v_uv + u_dir * 5.17647).rgb + texture2D(u_tex, v_uv - u_dir * 5.17647).rgb);',
    '  gl_FragColor = vec4(c, 1.0);',
    '}'
  ].join('\n');

  var FINAL = PRECISION + [
    'varying vec2 v_uv;',
    'uniform sampler2D u_scene, u_halo;',
    'uniform float u_fondu;',
    'float h(vec2 p) { vec3 q = fract(vec3(p.xyx) * 0.1031); q += dot(q, q.yzx + 33.33); return fract((q.x + q.y) * q.z); }',
    'void main() {',
    '  vec3 c = texture2D(u_scene, v_uv).rgb + 0.9 * texture2D(u_halo, v_uv).rgb;',
    '  gl_FragColor = vec4(c * u_fondu + (h(gl_FragCoord.xy) - 0.5) / 255.0, 1.0);',
    '}'
  ].join('\n');

  // Un trou noir calculé dans le cadre donné ; mode : 'accueil', 'parcours' ou 'figure'.
  function lancer(cadre, mode) {
    var toile = cadre.querySelector('canvas'), accueil = mode === 'accueil';
    var gl = null, progs = null, cibles = null, ctx = null, rayon2d = 0;
    var temps = 0, tChute = null, duree = CHUTE, dernier = null;
    var azimut = 0, rCamera = R_DEPART;
    var fini = false, images = 0, cumul = 0, baisses = 0;
    var visible = false, fige = calme, enCours = false;  // ouverture du chapitre Relativité
    // Pixels calculés par image ; une image fixe peut l'être en pleine définition.
    var budget = accueil ? (tactile ? 4.5e5 : 1.5e6) : mode === 'parcours' ? (tactile ? 3.5e5 : 9e5) : 2.5e6;
    var vise = [0, 0], cible = [0, 0];

    function lisse(a, b, x) { var t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); }
    function croix(a, b) { return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]; }
    function normer(a) { var n = Math.hypot(a[0], a[1], a[2]); return [a[0] / n, a[1] / n, a[2] / n]; }

    // Rayon de l'ombre à l'écran au repos, comme sur l'image de référence.
    function rayon(L, H) {
      if (accueil) return Math.min(L * (L < 700 ? 0.2 : 0.13), H * 0.26);
      return mode === 'parcours' ? Math.min(H * 0.2, L * 0.16) : Math.min(L, H) * 0.14;
    }
    // Demi-angle de l'ombre pour un observateur immobile à la distance r (r > 1,5).
    function ombre(r) { return Math.asin(Math.min(1, 2.598 / r * Math.sqrt(1 - 1 / r))); }

    // Position et visée de la caméra ; e va de 0 (au repos) à 1 (avalé).
    function camera(L, H, e) {
      var repos = accueil ? R_DEPART - 2 * (1 - Math.exp(-temps / 10)) : R_DEPART;  // il nous attire déjà
      var r = repos * Math.pow(R_FIN / repos, e);
      var elev = (1.5 + 11 * lisse(12, 2.5, r)) * Math.PI / 180 + vise[1] * 0.03;
      var az = azimut + vise[0] * 0.06;
      var pos = [r * Math.cos(elev) * Math.cos(az), r * Math.sin(elev), r * Math.cos(elev) * Math.sin(az)];
      var av = [-pos[0] / r, -pos[1] / r, -pos[2] / r];
      var dr = normer(croix(av, [0, 1, 0]));
      // Le champ s'élargit pendant la chute, sans que l'ombre cesse de grandir à l'écran.
      var m = Math.min(L, H);
      var tm = Math.min(5, Math.tan(ombre(R_DEPART)) * m / 2 / rayon(L, H) * Math.pow(R_DEPART / r, 0.8));
      return { r: r, pos: pos, av: av, dr: dr, ha: croix(dr, av), tx: tm * L / m, ty: tm * H / m };
    }

    function compiler(type, source) {
      var s = gl.createShader(type);
      gl.shaderSource(s, source);
      gl.compileShader(s);
      if (gl.getShaderParameter(s, gl.COMPILE_STATUS)) return s;
      console.warn(gl.getShaderInfoLog(s));
      return null;
    }

    function programme(source, noms) {
      var vs = compiler(gl.VERTEX_SHADER, SOMMETS), fs = compiler(gl.FRAGMENT_SHADER, source);
      if (!vs || !fs) return null;
      var p = gl.createProgram();
      gl.attachShader(p, vs);
      gl.attachShader(p, fs);
      gl.bindAttribLocation(p, 0, 'a');
      gl.linkProgram(p);
      if (!gl.getProgramParameter(p, gl.LINK_STATUS)) { console.warn(gl.getProgramInfoLog(p)); return null; }
      var u = {};
      noms.forEach(function (nom) { u[nom] = gl.getUniformLocation(p, nom); });
      return { p: p, u: u };
    }

    function preparerGL() {
      var hp = gl.getShaderPrecisionFormat(gl.FRAGMENT_SHADER, gl.HIGH_FLOAT);
      if (!hp || hp.precision < 16) return false;
      progs = {
        trace: programme(TRACE, ['u_tan', 'u_cam', 'u_av', 'u_dr', 'u_ha', 'u_temps', 'u_pas', 'u_pix', 'u_loin', 'u_expo']),
        seuil: programme(SEUIL, ['u_texel']),
        flou: programme(FLOU, ['u_dir']),
        final: programme(FINAL, ['u_halo', 'u_fondu'])
      };
      if (!progs.trace || !progs.seuil || !progs.flou || !progs.final) return false;
      gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      gl.enableVertexAttribArray(0);
      gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
      gl.useProgram(progs.final.p);
      gl.uniform1i(progs.final.u.u_halo, 1);
      return true;
    }

    function cibleRendu(w, h) {
      var tex = gl.createTexture();
      gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, w, h, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      var fb = gl.createFramebuffer();
      gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
      gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tex, 0);
      return { tex: tex, fb: fb, w: w, h: h };
    }

    function liberer(c) { gl.deleteTexture(c.tex); gl.deleteFramebuffer(c.fb); }

    // Le calcul se fait à une définition bornée (budget de pixels), l'image est étirée à l'écran.
    function dimensionner(L, H) {
      var k = Math.min(window.devicePixelRatio || 1, 2);
      if (gl && L * H * k * k > budget) k = Math.sqrt(budget / (L * H));
      var w = Math.max(4, Math.round(L * k)), h = Math.max(4, Math.round(H * k));
      if (toile.width === w && toile.height === h && (cibles || !gl)) return false;
      toile.width = w;
      toile.height = h;
      if (gl) {
        if (cibles) [cibles.scene, cibles.a, cibles.b].forEach(liberer);
        var qw = Math.max(1, Math.round(w / 4)), qh = Math.max(1, Math.round(h / 4));
        cibles = { scene: cibleRendu(w, h), a: cibleRendu(qw, qh), b: cibleRendu(qw, qh) };
      }
      return true;
    }

    function passe(prog, cible, tex0, tex1) {
      gl.bindFramebuffer(gl.FRAMEBUFFER, cible ? cible.fb : null);
      gl.viewport(0, 0, cible ? cible.w : toile.width, cible ? cible.h : toile.height);
      gl.useProgram(prog.p);
      if (tex1) { gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, tex1); }
      if (tex0) { gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, tex0); }
    }

    function tracer() { gl.drawArrays(gl.TRIANGLES, 0, 3); }

    function dessinerGL(cam, e) {
      var c = cibles, u = progs.trace.u;
      passe(progs.trace, c.scene);
      gl.uniform2f(u.u_tan, cam.tx, cam.ty);
      gl.uniform3fv(u.u_cam, cam.pos);
      gl.uniform3fv(u.u_av, cam.av);
      gl.uniform3fv(u.u_dr, cam.dr);
      gl.uniform3fv(u.u_ha, cam.ha);
      gl.uniform1f(u.u_temps, temps);
      gl.uniform1f(u.u_pas, baisses ? 0.13 : 0.1);
      gl.uniform1f(u.u_pix, 160 * cam.ty / c.scene.h);
      gl.uniform1f(u.u_loin, Math.max(1.5 * cam.r, 30));
      gl.uniform1f(u.u_expo, 1 + 0.25 * e);
      tracer();
      passe(progs.seuil, c.a, c.scene.tex);
      gl.uniform2f(progs.seuil.u.u_texel, 1 / c.scene.w, 1 / c.scene.h);
      tracer();
      [[c.a, c.b, 1, 0], [c.b, c.a, 0, 1], [c.a, c.b, 2.5, 0], [c.b, c.a, 0, 2.5]].forEach(function (f) {
        passe(progs.flou, f[1], f[0].tex);
        gl.uniform2f(progs.flou.u.u_dir, f[2] / f[0].w, f[3] / f[0].h);
        tracer();
      });
      passe(progs.final, null, c.scene.tex, c.a.tex);
      gl.uniform1f(progs.final.u.u_fondu, accueil && !calme ? Math.min(1, temps / 1.5) : 1);
      tracer();
    }

    // Sans WebGL : une image fixe de l'ombre et de ses lignes de lumière, que la chute agrandit.
    function dessiner2d(L, H, R) {
      var k = toile.width / L;
      ctx.setTransform(k, 0, 0, k, 0, 0);
      var cx = L / 2, cy = H / 2;
      var fond = ctx.createRadialGradient(cx, cy, R, cx, cy, Math.max(L, H) * 0.75);
      fond.addColorStop(0, '#0f1a2e');
      fond.addColorStop(0.45, '#0a1120');
      fond.addColorStop(1, '#05070c');
      ctx.globalCompositeOperation = 'source-over';
      ctx.fillStyle = fond;
      ctx.fillRect(0, 0, L, H);
      ctx.globalCompositeOperation = 'lighter';
      var halo = ctx.createRadialGradient(cx, cy, R * 0.95, cx, cy, R * 2.1);
      halo.addColorStop(0, 'rgba(150,180,230,0.35)');
      halo.addColorStop(0.25, 'rgba(90,120,180,0.12)');
      halo.addColorStop(1, 'rgba(40,60,110,0)');
      ctx.fillStyle = halo;
      ctx.beginPath(); ctx.arc(cx, cy, R * 2.1, 0, Math.PI * 2); ctx.fill();
      [[1.075, 0.9, 1.6], [1.185, 0.57, 1.1], [1.31, 0.36, 0.9], [1.455, 0.22, 0.8], [1.61, 0.14, 0.7]].forEach(function (l) {
        var rk = R * l[0];
        var d = ctx.createLinearGradient(0, 0, L, 0);
        d.addColorStop(0, 'rgba(160,185,230,0)');
        d.addColorStop(0.5, 'rgba(210,225,255,' + l[1] + ')');
        d.addColorStop(1, 'rgba(160,185,230,0)');
        ctx.strokeStyle = d;
        ctx.lineWidth = l[2];
        [1, -1].forEach(function (sens) {
          ctx.beginPath();
          for (var x = 0; x <= L; x += 2) {
            var y = cy - sens * (0.6 + rk / Math.pow(Math.cosh(1.15 * (x - cx) / rk), 1.5));
            if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
          }
          ctx.stroke();
        });
      });
      var h = ctx.createLinearGradient(0, 0, L, 0);
      h.addColorStop(0, 'rgba(190,210,250,0.05)');
      h.addColorStop(0.5, 'rgba(255,255,255,1)');
      h.addColorStop(1, 'rgba(190,210,250,0.05)');
      ctx.fillStyle = h;
      ctx.fillRect(0, cy - 0.8, L, 1.6);
      ctx.shadowColor = 'rgba(190,215,255,0.9)';
      ctx.shadowBlur = R * 0.18;
      ctx.strokeStyle = 'rgba(235,242,255,0.95)';
      ctx.lineWidth = Math.max(2, R * 0.03);
      ctx.beginPath(); ctx.arc(cx, cy, R * 1.005, 0, Math.PI * 2); ctx.stroke();
      ctx.shadowBlur = 0;
      ctx.globalCompositeOperation = 'source-over';
      ctx.fillStyle = '#000';
      ctx.beginPath(); ctx.arc(cx, cy, R * 0.985, 0, Math.PI * 2); ctx.fill();
    }

    function rendre(e) {
      var L = toile.clientWidth, H = toile.clientHeight;
      if (!L || !H) return;
      var cam = camera(L, H, e);
      rCamera = cam.r;
      var change = dimensionner(L, H);
      if (gl) dessinerGL(cam, e);
      else {
        if (change || !rayon2d) { rayon2d = rayon(L, H); dessiner2d(L, H, rayon2d); }
        toile.style.transform = e ? 'scale(' + Math.pow(Math.hypot(L, H) / rayon2d, e) + ')' : '';
      }
    }

    // Machine lente : on calcule moins de pixels, jusqu'à trois fois.
    function adapter(brut) {
      if (!gl || baisses >= 3 || brut <= 0 || ++images <= 5) return;
      cumul += brut;
      if (images < 25) return;
      if (cumul / 20 > 0.026) { budget *= 0.55; baisses++; }
      images = 0;
      cumul = 0;
    }

    function image(maintenant) {
      if (fini) return;
      try {
        var brut = dernier === null ? 0 : (maintenant - dernier) / 1000;
        dernier = maintenant;
        var dt = Math.min(0.1, brut);
        temps += dt;
        adapter(brut);
        if (!accueil) {
          azimut += dt * 0.035;
          rendre(0);
          if (!visible || fige) { enCours = false; return; }
          return requestAnimationFrame(image);
        }
        if (tChute === null && temps > ATTENTE) avaler(false);
        var s = tChute === null ? 0 : Math.min(1, (temps - tChute) / duree);
        azimut += dt * 0.035 * Math.pow(R_DEPART / rCamera, 0.7);  // on spirale en tombant
        vise[0] += (cible[0] - vise[0]) * Math.min(1, dt * 2.5);
        vise[1] += (cible[1] - vise[1]) * Math.min(1, dt * 2.5);
        rendre(Math.pow(s, 1.5));
        if (s >= 1 && temps - tChute - duree > NOIR) return entrer();
        requestAnimationFrame(image);
      } catch (erreur) {
        if (accueil) entrer(); else eteindre();
        throw erreur;
      }
    }

    function boucler() {
      if (enCours || fini || !visible) return;
      enCours = true;
      dernier = null;
      requestAnimationFrame(image);
    }

    // Hors de l'accueil, une panne retire la figure (sa place se referme).
    function eteindre() {
      fini = true;
      delete cadre.dataset.rendu;
    }

    function avaler(vite) {
      if (fini || tChute !== null) return;
      if (calme) return entrer();
      tChute = temps;
      duree = vite ? CHUTE_VITE : CHUTE;
    }

    function entrer() {
      if (fini) return;
      fini = true;
      window.scrollTo(0, 0);
      racine.classList.add('dedans');
      setTimeout(function () {
        cadre.style.display = 'none';
        var perte = gl && gl.getExtension('WEBGL_lose_context');
        if (perte) perte.loseContext();
      }, 1600);
    }

    // Thème Relativité : le calcul remplace l'illustration et le dit dans la légende.
    function figer() {
      cadre.dataset.rendu = 'calcul';
      var legende = cadre.querySelector('figcaption');
      if (legende) legende.textContent = 'Trou noir · calculé en relativité générale, pas une observation';
      racine.classList.add('scene-js');
      new ResizeObserver(function () { rendre(0); }).observe(toile);
    }

    // Ouverture du chapitre Relativité : la place est prise dès le départ, le calcul est préparé
    // quand on approche, puis il tourne tant qu'on le voit, sauf si le parcours est figé.
    function ouvrir() {
      var pret = false;
      var gele = document.body.dataset.frozen;
      if (gele) fige = gele === 'true';
      cadre.dataset.rendu = 'calcul';
      toile.addEventListener('webglcontextlost', function (ev) { ev.preventDefault(); eteindre(); });
      document.addEventListener('aeternam-motion', function (ev) {
        fige = ev.detail.frozen;
        if (pret) { if (fige) rendre(0); else boucler(); }
      });
      new ResizeObserver(function () { if (pret && !enCours) rendre(0); }).observe(toile);
      new IntersectionObserver(function (entrees) {
        visible = entrees[0].isIntersecting;
        if (!visible || fini) return;
        if (!pret && !(pret = preparerGL())) return eteindre();
        if (fige) rendre(0); else boucler();
      }, { rootMargin: '200px' }).observe(cadre.closest('article') || cadre);
    }

    try {
      try {
        gl = toile.getContext('webgl', { alpha: false, antialias: false, depth: false, stencil: false });
      } catch (erreur) { gl = null; }
      if (mode === 'parcours') {
        if (gl) ouvrir();
        return;
      }
      if (gl && !preparerGL()) gl = null;
      if (!accueil) {
        if (gl) figer();
        return;
      }
      if (!gl) {
        // Sans WebGL : l'image fixe dessinée en 2D, qui n'est plus un calcul.
        var neuve = toile.cloneNode(false);
        toile.parentNode.replaceChild(neuve, toile);
        toile = neuve;
        ctx = toile.getContext('2d');
        if (!ctx) { racine.classList.remove('vivant'); return; }
        var legende = cadre.querySelector('.ciel-legende');
        if (legende) legende.textContent = 'Trou noir · illustration hors échelle';
      }
      toile.addEventListener('webglcontextlost', function (ev) { ev.preventDefault(); entrer(); });

      ['wheel', 'touchstart', 'keydown', 'pointerdown'].forEach(function (nom) {
        window.addEventListener(nom, function () { avaler(true); }, { passive: true });
      });
      document.addEventListener('focusin', function () { avaler(true); });
      window.addEventListener('pointermove', function (ev) {
        if (ev.pointerType !== 'mouse') return;
        cible = [ev.clientX / window.innerWidth - 0.5, ev.clientY / window.innerHeight - 0.5];
      }, { passive: true });

      if (calme) {
        rendre(0);
        window.addEventListener('resize', function () { if (!fini) rendre(0); });
        setTimeout(entrer, 3500);
      } else {
        requestAnimationFrame(image);
      }
    } catch (erreur) {
      if (accueil) racine.classList.remove('vivant');
      else eteindre();
      throw erreur;
    }
  }

  var ciel = document.querySelector('.ciel');
  if (ciel && racine.classList.contains('vivant')) lancer(ciel, 'accueil');  // revenu du site : déjà dedans
  var ouverture = document.querySelector('.univ-trou-noir figure');
  if (ouverture) lancer(ouverture, 'parcours');
  var theme = document.querySelector('.scene-sujet[data-scene="19"]');
  if (theme) lancer(theme, 'figure');
})();
