/* L'accueil. Premier écran : le nom et la question, seuls, sous un ciel d'étoiles. Au défilement,
   le nom s'efface et cinq temps se succèdent, un par écran, chacun avec son schéma : la courbe du
   risque de mourir se trace pendant que les étoiles filent ; chez l'hydre, une ligne plate ;
   retarder repousse la courbe ; ralentir adoucit sa pente, et le ciel s'arrête ; puis deux
   gouttes de sang, l'une plus jeune. Puis la feuille monte : l'expérience à financer, puis
   l'appel, dont les phrases s'éclairent mot à mot. Sans ce fichier, ou en mouvement réduit : le
   nom, la question, puis les temps, écrits dans la page. */
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
    function taille(py = 0.5) {            // le pôle, en fraction de la hauteur
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

  // ---------- Les étiquettes des schémas gardent la même taille à l'écran (--zoom, accueil.css).
  const schemas = [...document.querySelectorAll('.accueil .dessin')];
  const zoomer = () => schemas.forEach((s) => {
    const l = s.getBoundingClientRect().width;
    if (l && s.viewBox?.baseVal?.width) s.style.setProperty('--zoom', (s.viewBox.baseVal.width / l).toFixed(3));
  });
  zoomer();
  addEventListener('resize', zoomer);
  document.fonts?.ready.then(zoomer);

  // ---------- Les temps : un par écran. Les temps se comptent en hauteurs d'écran défilées ;
  // DEBUT et PAS servent aussi à la hauteur de .heros (accueil.css) : les deux vont ensemble.
  const DEBUT = 0.55, PAS = 1.25;
  function recitScene(recit) {
    const temps = [...recit.querySelectorAll('.temps')];
    // q vaut 0 au début du premier temps et avance de 1 par temps.
    return (q) => {
      const dernier = temps.length - 1;
      recit.style.visibility = q > -0.1 && q < dernier + 2.2 ? 'visible' : 'hidden';
      temps.forEach((c, k) => {
        const u = q - k, entre = lisse(0.04, 0.32, u), sort = k === dernier ? 0 : lisse(0.86, 1.02, u);
        c.style.setProperty('--n', entre.toFixed(3));
        c.style.setProperty('--o', lisse(0.16, 0.44, u).toFixed(3));
        c.style.setProperty('--s', sort.toFixed(3));
        c.classList.toggle('actif', entre > 0.004 && sort < 0.996);
      });
    };
  }

  // ---------- La scène.
  const heros = document.getElementById('heros');
  const dessin = heros?.querySelector('.d-scene');
  if (heros) {
    const plan = heros.querySelector('.heros-plan');
    const tete = heros.querySelector('.heros-tete');
    const voute = ciel(heros.querySelector('.ciel'));
    const recit = document.getElementById('recit');

    if (calme || !dessin) {
      // Sans mouvement : le nom et la question, sous un ciel immobile.
      const fixe = () => { voute.taille(); voute.dessiner(0.4, 0.006); };
      fixe();
      addEventListener('resize', fixe);
    } else {
      // Mêmes nombres que SCENE_* de site/dessins.py : y = (e^(k·u) − 1) / (e^K − 1).
      const X0 = 64, X1 = 530, BAS = 410, HAUT = 70, K = 4.2, K_FIN = 2.6, DECALE = 88;
      const $ = (id) => dessin.querySelector(`#${id}`);
      const courbe = $('scene-courbe'), sang = $('scene-sang');
      const humain = $('c-humain'), hydre = $('c-hydre'), fantome = $('c-fantome'), ralenti = $('c-ralentir');
      const noms = { humain: $('n-humain'), hydre: $('n-hydre'), retarder: $('n-retarder'), ralentir: $('n-ralentir') };
      const gouttes = [...sang.querySelectorAll('.goutte')];
      const cellules = [...sang.querySelectorAll('.goutte ~ .cellule')];
      const legende = sang.querySelector('.sang-legende');
      const raconter = recit && recit.querySelector('.temps') ? recitScene(recit) : null;
      const memoire = new Map();
      // N'écrit un attribut ou un style que s'il change : la scène tourne à chaque image.
      const poser = (el, cle, valeur) => {
        let m = memoire.get(el);
        if (!m) memoire.set(el, (m = {}));
        if (m[cle] === valeur) return;
        m[cle] = valeur;
        if (cle === 'd') el.setAttribute('d', valeur);
        else el.style[cle] = valeur;
      };
      const opacite = (el, x) => poser(el, 'opacity', x.toFixed(3));
      const trace = (el, x) => poser(el, 'strokeDashoffset', (1.02 * (1 - x)).toFixed(4));

      function tracer(k, decale) {
        const echelle = Math.exp(K) - 1, longueur = X1 - X0, fin = (longueur - decale) / longueur;
        let d = `M${X0} ${BAS}`;
        for (let i = 0; i <= 80; i++) {
          const u = fin * i / 80;
          d += ` L${(X0 + decale + longueur * u).toFixed(1)} ${(BAS - (BAS - HAUT) * (Math.exp(k * u) - 1) / echelle).toFixed(1)}`;
        }
        return d;
      }

      let avant = 0, angle = 0, visible = true, tourneEncore = false;
      function image(temps) {
        if (!innerHeight) return;            // fenêtre sans hauteur : rien à dessiner
        const dt = borne((temps - avant) / 1000, 0, 0.05);
        avant = temps;
        const P = (scrollY - heros.offsetTop) / innerHeight;
        const q = (P - DEBUT) / PAS, u = (k) => q - k;

        // Le nom s'efface et monte un peu ; le schéma arrive.
        const titre = 1 - lisse(0.06, 0.4, P);
        plan.style.setProperty('--titre', titre.toFixed(3));
        plan.style.setProperty('--monte', `${(-(1 - titre) * 0.06 * innerHeight).toFixed(1)}px`);
        plan.style.setProperty('--note', (1 - lisse(0.02, 0.1, P)).toFixed(3));
        tete.style.visibility = titre < 0.004 ? 'hidden' : '';
        plan.style.setProperty('--scene', lisse(-0.3, 0.02, q).toFixed(3));

        // 1. La courbe du risque se trace.
        trace(humain, lisse(0.04, 0.62, u(0)));
        opacite(noms.humain, lisse(0.5, 0.72, u(0)));
        // 2. Chez l'hydre, une ligne plate ; elle s'efface au temps suivant.
        const sansHydre = 1 - lisse(0.02, 0.24, u(2));
        trace(hydre, lisse(0.08, 0.56, u(1)));
        poser(hydre, 'opacity', sansHydre.toFixed(3));
        opacite(noms.hydre, lisse(0.4, 0.62, u(1)) * sansHydre);
        // 3. Retarder : la courbe glisse vers la droite ; sa place reste en pointillé.
        const glisse = lisse(0.08, 0.6, u(2));
        poser(humain, 'd', tracer(K, glisse * DECALE));
        opacite(fantome, lisse(0.04, 0.24, u(2)));
        opacite(noms.retarder, lisse(0.46, 0.68, u(2)));
        // 4. Ralentir : depuis la courbe d'origine, une pente plus douce, en or.
        const adoucit = lisse(0.08, 0.62, u(3));
        opacite(ralenti, lisse(0.02, 0.1, u(3)));
        poser(ralenti, 'd', tracer(melange(K, K_FIN, adoucit), 0));
        opacite(noms.ralentir, lisse(0.5, 0.72, u(3)));
        // 5. Le sang : la courbe s'efface, deux gouttes se dessinent, les cellules apparaissent.
        const versSang = lisse(0.02, 0.3, u(4));
        opacite(courbe, 1 - versSang);
        poser(courbe, 'transform', `scale(${(1 - 0.06 * versSang).toFixed(3)})`);
        opacite(sang, lisse(0.12, 0.36, u(4)));
        gouttes.forEach((g) => trace(g, lisse(0.12, 0.5, u(4))));
        opacite(legende, lisse(0.3, 0.5, u(4)));
        cellules.forEach((c, i) => {
          const a = 0.3 + 0.014 * (i % 14) + 0.05 * Math.floor(i / 14);
          opacite(c, lisse(a, a + 0.1, u(4)));
        });

        // Le ciel file tant que la courbe monte vite, et s'arrête quand on la ralentit.
        const cours = 1 - lisse(0.08, 0.7, u(3));
        const file = lisse(-0.4, 0.3, q) * cours;
        angle += dt * (0.014 + 0.1 * file) * cours;
        voute.dessiner(angle, 0.006 + 0.4 * file ** 1.3);
        raconter?.(q);
      }

      function boucleDessin(temps) {
        if (!visible || document.hidden) { tourneEncore = false; return; }
        image(temps);
        requestAnimationFrame(boucleDessin);
      }
      function relancer() { if (!tourneEncore) { tourneEncore = true; requestAnimationFrame(boucleDessin); } }

      voute.taille();
      image(0);
      addEventListener('resize', () => { voute.taille(); relancer(); });
      document.fonts?.ready.then(relancer);
      document.addEventListener('visibilitychange', relancer);
      addEventListener('scroll', relancer, { passive: true });   // la scène repart toujours avec le défilement
      new IntersectionObserver(([e]) => { visible = e.isIntersecting; relancer(); }).observe(heros);
      relancer();
    }
  }

  // ---------- Les volets : chacun s'arrête quand son bas touche le bas de l'écran, et le suivant
  // glisse par-dessus. Un volet plus haut que l'écran colle donc à une hauteur négative.
  const volets = [...document.querySelectorAll('.volet')].slice(0, -1);
  if (volets.length && !calme && CSS.supports('position', 'sticky')) {
    const coller = () => volets.forEach((v) => {
      v.style.setProperty('--colle', `${Math.min(0, innerHeight - v.offsetHeight)}px`);
      v.classList.add('colle');
    });
    coller();
    addEventListener('resize', coller);
    addEventListener('load', coller);
    document.fonts?.ready.then(coller);
  }

  // ---------- Les phrases de l'appel s'éclairent mot à mot ; lues, le cri arrive.
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
      phrase.parentElement.classList.toggle('eclate', n === mots.length);
    };
    addEventListener('scroll', () => { if (!attente) { attente = true; requestAnimationFrame(eclairer); } }, { passive: true });
    addEventListener('resize', eclairer);
    eclairer();
  }
})();
