/* L'accueil. Premier écran : le nom et la question, seuls, sous un ciel d'étoiles. Au défilement,
   le nom s'efface et le sablier arrive ; son sable tombe pendant que les étoiles filent, puis il
   ralentit et reste suspendu : le temps s'arrête. Le sable quitte alors le verre et vient écrire,
   chapitre après chapitre, les nombres de ce que l'on sait. Puis la feuille monte : les phrases
   du manifeste s'éclairent mot à mot. Sans ce fichier, ou en mouvement réduit : le nom, la
   question, puis les chapitres, écrits dans la page. */
(() => {
  'use strict';
  const calme = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const borne = (x, a, b) => Math.min(b, Math.max(a, x));
  const lisse = (a, b, x) => { const u = borne((x - a) / (b - a), 0, 1); return u * u * (3 - 2 * u); };
  const melange = (a, b, u) => a + (b - a) * u;

  // ---------- Le ciel : des étoiles autour d'un pôle. Plus la pose est longue, plus elles filent.
  function ciel(toile) {
    const ctx = toile.getContext('2d');
    let l = 0, h = 0, d = 1, etoiles = [], pole = { x: 0, y: 0 };
    function taille(py = 0.64) {            // le pôle est au centre du sablier
      d = Math.min(devicePixelRatio || 1, 2);
      l = toile.clientWidth; h = toile.clientHeight;
      toile.width = Math.round(l * d); toile.height = Math.round(h * d);
      pole = { x: l * 0.5, y: h * py };
      const portee = Math.hypot(Math.max(pole.x, l - pole.x), Math.max(pole.y, h - pole.y));
      let graine = 20261120;
      const alea = () => (graine = (graine * 1664525 + 1013904223) >>> 0) / 4294967296;
      etoiles = [];
      const nombre = Math.round(borne(l * h / 2100, 220, 820));
      for (let i = 0; i < nombre; i++) {
        etoiles.push({ r: Math.sqrt(alea()) * portee, a: alea() * Math.PI * 2, e: 0.2 + 0.8 * alea() ** 2, l: 0.6 + alea() * 1.1, or: alea() < 0.1 });
      }
    }
    function dessiner(angle, pose) {
      if (!l || !h) return;
      ctx.setTransform(d, 0, 0, d, 0, 0);
      ctx.clearRect(0, 0, l, h);
      ctx.lineCap = 'round';
      for (const s of etoiles) {
        const a0 = s.a + angle;
        ctx.beginPath();
        ctx.arc(pole.x, pole.y, s.r, a0, a0 + pose * (0.55 + 0.45 * s.e));
        ctx.strokeStyle = s.or ? `rgba(214,179,106,${(0.62 * s.e).toFixed(3)})` : `rgba(236,232,222,${(0.5 * s.e).toFixed(3)})`;
        ctx.lineWidth = s.l;
        ctx.stroke();
      }
    }
    return { taille, dessiner };
  }

  // ---------- Le récit : le sable quitte le sablier et écrit le nombre de chaque chapitre.
  // Les temps se comptent en hauteurs d'écran défilées ; DEBUT et PAS servent aussi à la hauteur
  // de .heros (site/accueil/accueil.css) : les deux calculs vont ensemble.
  const DEBUT = 1.35, PAS = 1.05;
  function ecriture(recit, hauteurSablier) {
    const toile = recit.querySelector('.grains');
    const ctx = toile.getContext('2d');
    const chapitres = [...recit.querySelectorAll('.chapitre')];
    let l = 0, h = 0, d = 1, grains = [], depart = null, formes = [];

    // Les points d'un nombre : le texte est dessiné hors écran, à la place exacte qu'il occupe
    // dans la page (même police, même ligne de base), puis ses pixels sont tirés au sort.
    function points(chapitre, n, alea) {
      const el = chapitre.querySelector('.n'), style = getComputedStyle(el);
      const o = toile.getBoundingClientRect(), r = el.getBoundingClientRect();
      const base = chapitre.querySelector('.base').getBoundingClientRect().bottom;
      const tampon = document.createElement('canvas');
      tampon.width = l; tampon.height = h;
      const t = tampon.getContext('2d', { willReadFrequently: true });
      t.font = `${style.fontStyle} ${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;
      if ('letterSpacing' in t) t.letterSpacing = style.letterSpacing;
      t.textBaseline = 'alphabetic';
      t.fillText(el.textContent, r.left - o.left, base - o.top);
      const image = t.getImageData(0, 0, l, h).data, pleins = [];
      for (let y = 0; y < h; y += 2) for (let x = 0; x < l; x += 2) if (image[(y * l + x) * 4 + 3] > 128) pleins.push(x, y);
      const combien = pleins.length / 2, forme = new Float32Array(2 * n);
      for (let i = 0; i < n; i++) {
        const j = combien ? Math.floor(alea() * combien) : -1;
        forme[2 * i] = (j < 0 ? l / 2 : pleins[2 * j]) + (alea() - 0.5) * 2;
        forme[2 * i + 1] = (j < 0 ? h / 2 : pleins[2 * j + 1]) + (alea() - 0.5) * 2;
      }
      return forme;
    }

    function mesurer() {
      d = Math.min(devicePixelRatio || 1, 2);
      l = toile.clientWidth; h = toile.clientHeight;
      if (!l || !h) return;
      toile.width = Math.round(l * d); toile.height = Math.round(h * d);
      let graine = 18750221;
      const alea = () => (graine = (graine * 1664525 + 1013904223) >>> 0) / 4294967296;
      const n = Math.round(borne(l * h / 420, 1800, 3000));
      // Le départ : le sable des deux ampoules, là où le sablier se tient, au centre de l'écran.
      const H = hauteurSablier(), W = H * 264 / 540, cx = l / 2, haut = h / 2 - H / 2;
      depart = new Float32Array(2 * n);
      for (let i = 0; i < n; i++) {
        const t = Math.sqrt(alea()), cote = (alea() * 2 - 1) * t * 0.3 * W;
        depart[2 * i] = cx + cote;
        depart[2 * i + 1] = i % 2 ? haut + (0.5 - 0.14 * t) * H : haut + (0.69 + 0.21 * t) * H;
      }
      formes = chapitres.map((c) => points(c, n, alea));
      grains = Array.from({ length: n }, () => ({
        retard: alea() * 0.4, courbe: (alea() * 2 - 1) * 0.22, rayon: 0.55 + alea() * 0.6, w: 0.6 + alea() * 0.8, phase: alea() * 6.283 }));
    }

    // q vaut 0 au début du premier chapitre et avance de 1 par chapitre.
    function image(P, temps) {
      const q = (P - DEBUT) / PAS, dernier = chapitres.length - 1;
      recit.style.visibility = q > -0.2 && q < dernier + 2.2 ? 'visible' : 'hidden';
      chapitres.forEach((c, k) => {
        const u = q - k, o = lisse(0.3, 0.56, u) * (k === dernier ? 1 : 1 - lisse(0.84, 1.02, u));
        c.style.setProperty('--o', o.toFixed(3));
        c.classList.toggle('actif', o > 0.01);
      });
      if (!l || !h) return;
      ctx.setTransform(d, 0, 0, d, 0, 0);
      ctx.clearRect(0, 0, l, h);
      if (q <= 0 || !grains.length) return;
      const k = Math.min(dernier, Math.floor(q)), e = borne((q - k) / 0.5, 0, 1);
      const de = k ? formes[k - 1] : depart, vers = formes[k];
      ctx.globalAlpha = k ? 1 : Math.min(1, e * 3);
      ctx.fillStyle = '#d6b36a';
      ctx.beginPath();
      grains.forEach((g, i) => {
        const u = borne(e * 1.4 - g.retard, 0, 1), s = u * u * (3 - 2 * u);
        const x0 = de[2 * i], y0 = de[2 * i + 1], dx = vers[2 * i] - x0, dy = vers[2 * i + 1] - y0;
        const arc = Math.sin(Math.PI * s) * g.courbe, flotte = Math.sin(temps * 0.001 * g.w + g.phase) * 0.5;
        const x = x0 + dx * s - dy * arc + flotte, y = y0 + dy * s + dx * arc + flotte * 0.6;
        ctx.moveTo(x + g.rayon, y);
        ctx.arc(x, y, g.rayon, 0, 6.283);
      });
      ctx.fill();
    }
    return { mesurer, image };
  }

  // ---------- La scène : le nom et la question, puis le sablier dont le sable s'arrête
  const heros = document.getElementById('heros');
  if (heros) {
    const plan = heros.querySelector('.heros-plan');
    const tete = heros.querySelector('.heros-tete');
    const dessin = heros.querySelector('.d-sablier');
    const tourne = document.getElementById('sablier-tourne');
    const voute = ciel(heros.querySelector('.ciel'));
    const recit = document.getElementById('recit');

    if (calme || !dessin) {
      // Sans mouvement : le nom et la question, sous un ciel immobile.
      const fixe = () => { voute.taille(0.5); voute.dessiner(0.4, 0.006); };
      fixe();
      addEventListener('resize', fixe);
    } else {
      // Le dessin fait 600 unités de côté ; le sablier en occupe 540 de haut pour 264 de large.
      const grille = () => tete.clientWidth - 2 * (parseFloat(getComputedStyle(tete).paddingLeft) || 0);
      const unite = () => (dessin.clientWidth || dessin.getBoundingClientRect().width || 1) / 600;
      const grains = [...dessin.querySelectorAll('.sablier-chute circle')].map((c) => ({
        c, x: +c.getAttribute('cx'), phase: +c.dataset.phase, dx: +c.dataset.dx, dy: +c.dataset.dy, w: +c.dataset.w }));
      const CHUTE = 1.9;                // secondes qu'un grain met à tomber du col au tas
      let echelle = 1, visible = true, tourneEncore = false, avant = 0, sable = 0, angle = 0;
      const hauteurSablier = () => Math.min(0.6 * (plan.clientHeight || innerHeight), 1.6 * grille());
      const ecrit = recit && recit.querySelector('.chapitre') ? ecriture(recit, hauteurSablier) : null;

      function mesurer() {
        echelle = hauteurSablier() / (540 * unite());
        voute.taille(0.5);
        ecrit?.mesurer();
      }

      // p va de 0 à 1 sur une fois et quart la hauteur de l'écran : le nom s'efface (0,08 à 0,26),
      // le sablier arrive (0,20 à 0,38), puis le temps ralentit et s'arrête (0,50 à 0,80).
      function image(temps) {
        if (!innerHeight) return;            // fenêtre sans hauteur : rien à dessiner
        const dt = borne((temps - avant) / 1000, 0, 0.05);
        avant = temps;
        const P = (scrollY - heros.offsetTop) / innerHeight;
        const p = borne(P / 1.25, 0, 1);
        const titre = 1 - lisse(0.08, 0.26, p);
        plan.style.setProperty('--titre', titre.toFixed(3));
        plan.style.setProperty('--monte', `${(-(1 - titre) * 0.06 * innerHeight).toFixed(1)}px`);
        plan.style.setProperty('--note', (1 - lisse(0.02, 0.1, p)).toFixed(3));
        tete.style.visibility = titre < 0.004 ? 'hidden' : '';
        // Le sablier arrive, puis s'efface quand son sable part écrire le premier chapitre.
        const entree = lisse(0.2, 0.38, p);
        plan.style.setProperty('--sablier', (entree * (1 - lisse(0, 0.3, (P - DEBUT) / PAS))).toFixed(3));
        tourne.setAttribute('transform', `scale(${(echelle * melange(0.94, 1, entree)).toFixed(3)})`);

        // Le cours du temps : à 1 il s'écoule, à 0 il est arrêté.
        const cours = 1 - lisse(0.5, 0.8, p);
        sable += dt * cours / CHUTE;
        const suspendu = (1 - cours) ** 2;
        for (const g of grains) {
          const u = (g.phase + sable) % 1;
          const y = 2 + 102 * u * (0.3 + 0.7 * u);                    // la chute s'accélère
          const large = Math.min(1, y / 14);                          // près du col, le verre est étroit
          const berce = Math.sin(temps * 0.0011 * g.w + g.phase * 40) * 1.4 * suspendu;
          g.c.setAttribute('cx', (g.x + (g.dx * suspendu + 0.6 * berce) * large).toFixed(2));
          g.c.setAttribute('cy', (y + (g.dy * suspendu + berce) * large).toFixed(2));
        }

        // Le ciel file tant que le sable tombe, et s'arrête avec lui.
        const file = lisse(0.2, 0.44, p) * cours;
        angle += dt * (0.014 + 0.1 * file) * cours;
        voute.dessiner(angle, 0.006 + 0.4 * file ** 1.3);
        ecrit?.image(P, temps);
      }

      function boucleDessin(temps) {
        if (!visible || document.hidden) { tourneEncore = false; return; }
        image(temps);
        requestAnimationFrame(boucleDessin);
      }
      function relancer() { if (!tourneEncore) { tourneEncore = true; requestAnimationFrame(boucleDessin); } }

      mesurer();
      image(0);
      addEventListener('resize', () => { mesurer(); relancer(); });
      document.fonts?.ready.then(() => { mesurer(); relancer(); });
      document.addEventListener('visibilitychange', relancer);
      addEventListener('scroll', relancer, { passive: true });   // la scène repart toujours avec le défilement
      new IntersectionObserver(([e]) => { visible = e.isIntersecting; relancer(); }).observe(heros);
      relancer();
    }
  }

  // ---------- Les phrases du manifeste s'éclairent mot à mot, au rythme du défilement.
  const phrase = document.querySelector('.manifeste-phrase');
  if (phrase && !calme) {
    const mots = [...phrase.querySelectorAll('.m')];
    phrase.classList.add('suivie');
    let attente = false;
    const eclairer = () => {
      attente = false;
      const r = phrase.getBoundingClientRect();
      const u = borne((innerHeight * 0.86 - r.top) / (r.height + innerHeight * 0.3), 0, 1);
      const n = Math.round(u * mots.length);
      mots.forEach((m, i) => m.classList.toggle('lu', i < n));
    };
    addEventListener('scroll', () => { if (!attente) { attente = true; requestAnimationFrame(eclairer); } }, { passive: true });
    addEventListener('resize', eclairer);
    eclairer();
  }

  // ---------- Les chiffres comptent jusqu'à leur valeur.
  const compteurs = document.querySelectorAll('[data-compte]');
  if (compteurs.length && !calme && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entrees) => {
      for (const e of entrees) {
        if (!e.isIntersecting) continue;
        io.unobserve(e.target);
        const cible = +e.target.dataset.compte, depart = performance.now();
        const pas = (t) => {
          const u = borne((t - depart) / 1100, 0, 1);
          e.target.textContent = Math.round(cible * (1 - (1 - u) ** 3));
          if (u < 1) requestAnimationFrame(pas);
        };
        requestAnimationFrame(pas);
      }
    }, { threshold: 0.6 });
    compteurs.forEach((c) => io.observe(c));
  }
})();
