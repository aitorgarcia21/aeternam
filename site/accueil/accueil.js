/* L'accueil, sur la nuit unie. Premier écran : le nom et la question, seuls. Au défilement, le nom
   s'efface et les temps se succèdent, un par écran, chacun avec son schéma. D'abord décortiquer le
   vieillissement : la courbe du risque de mourir se trace ; sans sa montée, une ligne plate ; chez
   l'hydre, cette ligne est réelle ; une cellule et ce qui s'y abîme. Puis le principe : l'âge
   biologique redescend au début de l'embryon. Puis copier ce qui marche : quatre facteurs ramènent
   une cellule adulte en bas ; la courbe revient, que retarder repousse et que ralentir adoucit ;
   deux gouttes de sang, l'une plus jeune ; les deux prises de sang de l'expérience ; la même chez
   l'humain. Le dernier temps est l'appel. Sans ce fichier, ou en mouvement réduit : le nom, la
   question, puis les temps, écrits dans la page. */
(() => {
  'use strict';
  const calme = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const borne = (x, a, b) => Math.min(b, Math.max(a, x));
  const lisse = (a, b, x) => { const u = borne((x - a) / (b - a), 0, 1); return u * u * (3 - 2 * u); };
  const melange = (a, b, u) => a + (b - a) * u;

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
  // DEBUT et PAS servent aussi à la hauteur de .heros et aux crans (accueil.css) : ils vont ensemble.
  const DEBUT = 0.55, PAS = 1.15;
  // L'ordre des temps (ACCUEIL de site/langues/) ; l'appel est le dernier.
  const T = { courbe: 0, plat: 1, hydre: 2, cellule: 3, embryon: 4, facteurs: 5, retarder: 6, ralentir: 7, sang: 8, mesure: 9, humain: 10, appel: 11 };
  function recitScene(recit) {
    const temps = [...recit.querySelectorAll('.temps')];
    // q vaut 0 au début du premier temps et avance de 1 par temps.
    return (q) => {
      const dernier = temps.length - 1;
      recit.style.visibility = q > -0.1 ? 'visible' : 'hidden';
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
  if (heros && !calme && dessin) {
    const plan = heros.querySelector('.heros-plan');
    const tete = heros.querySelector('.heros-tete');
    const recit = document.getElementById('recit');
    // La hauteur d'un écran : celle du plan épinglé (--ecran, accueil.css), qui ne change pas
    // quand la barre d'adresse d'un téléphone se cache ou revient. Les crans sont comptés avec elle.
    const ecran = () => plan.offsetHeight || innerHeight;

    // Mêmes nombres que SCENE_* de site/dessins.py : y = (e^(k·u) − 1) / (e^K − 1).
    const X0 = 64, X1 = 530, BAS = 410, HAUT = 70, K = 4.2, K_FIN = 2.6, DECALE = 88;
    const $ = (id) => dessin.querySelector(`#${id}`);
    const tous = (sel, dans = dessin) => [...dans.querySelectorAll(sel)];
    const g = {
      courbe: $('scene-courbe'), cellule: $('scene-cellule'), embryon: $('scene-embryon'),
      sang: $('scene-sang'), mesure: $('scene-mesure'), humain: $('scene-humain'),
    };
    const raconter = recit?.querySelector('.temps') ? recitScene(recit) : null;

    // N'écrit un attribut ou un style que s'il change : la scène tourne à chaque image.
    // Une clé qui commence par @ est un attribut, les autres sont des styles.
    const memoire = new Map();
    const poser = (el, cle, valeur) => {
      if (!el) return;
      let m = memoire.get(el);
      if (!m) memoire.set(el, (m = {}));
      if (m[cle] === valeur) return;
      m[cle] = valeur;
      if (cle[0] === '@') el.setAttribute(cle.slice(1), valeur);
      else el.style[cle] = valeur;
    };
    const opacite = (el, x) => poser(el, 'opacity', x.toFixed(3));
    const trace = (el, x) => poser(el, 'strokeDashoffset', (1.02 * (1 - x)).toFixed(4));
    // Une suite d'éléments qui apparaissent l'un après l'autre, à partir de a, tous les pas.
    const apparaitre = (els, u, a, pas, duree = 0.1) => els.forEach((el, i) => opacite(el, lisse(a + pas * i, a + pas * i + duree, u)));
    // Une goutte : son contour se dessine à partir de a, puis ses cellules apparaissent.
    const goutte = (grp, u, a) => {
      trace(grp.querySelector('.goutte'), lisse(a, a + 0.24, u));
      apparaitre(tous('.cellule.a', grp), u, a + 0.14, 0.008, 0.08);
    };

    function tracer(k, decale) {
      const echelle = Math.exp(K) - 1, longueur = X1 - X0, fin = (longueur - decale) / longueur;
      let d = `M${X0} ${BAS}`;
      for (let i = 0; i <= 80; i++) {
        const u = fin * i / 80;
        d += ` L${(X0 + decale + longueur * u).toFixed(1)} ${(BAS - (BAS - HAUT) * (Math.exp(k * u) - 1) / echelle).toFixed(1)}`;
      }
      return d;
    }

    // En hauteur, le schéma se place au milieu de ce que le plus long des temps laisse libre
    // (l'appel, seul au milieu de l'écran, ne compte pas).
    const enHauteur = matchMedia('not all and (min-width: 900px) and (orientation: landscape)');
    function placer() {
      if (!recit) return;
      let bas = 0;
      if (enHauteur.matches) recit.querySelectorAll('.temps:not(.final)').forEach((t) => { bas = Math.max(bas, t.offsetTop + t.offsetHeight); });
      if (bas) plan.style.setProperty('--texte-bas', `${Math.round(bas)}px`);
      else plan.style.removeProperty('--texte-bas');
    }

    const el = {
      humain: $('c-humain'), plat: $('c-plat'), platRect: $('plat-rect'), hydre: $('c-hydre'), fantome: $('c-fantome'),
      ralenti: $('c-ralentir'), dix: $('p-dix'), membrane: $('k-membrane'), noyau: $('k-noyau'), adn: $('k-adn'),
      casse: $('k-casse'), eCourbe: $('e-courbe'), eSaut: $('e-saut'), eZero: $('e-zero'), eLigne: $('e-zero-ligne'), eAdulte: $('e-adulte'),
      inconnue: $('m-inconnue'), question: $('m-question'), arc: $('h-arc'),
    };
    const nom = {
      humain: $('n-humain'), dix: $('n-dix'), plat: $('n-plat'), hydre: $('n-hydre'), retarder: $('n-retarder'),
      ralentir: $('n-ralentir'), zero: $('n-zero'), facteurs: $('n-facteurs'), mesure: $('n-mesure'),
    };
    const mitos = tous('.k-mito'), amas = tous('.k-amas'), kNoms = tous('.k-nom');
    const gouttes = tous('.goutte', g.sang), cellules = tous('.cellule.a', g.sang), legende = g.sang?.querySelector('.sang-legende');
    const mGouttes = tous('.m-goutte'), mFleches = tous('.m-fleche'), mLegende = g.mesure?.querySelector('.sang-legende');
    const hGouttes = tous('.h-goutte'), hNoms = tous('.h-nom');

    function image() {
      const H = ecran();
      if (!H) return;                       // fenêtre sans hauteur : rien à dessiner
      const P = (scrollY - heros.offsetTop) / H;
      const q = (P - DEBUT) / PAS, u = (k) => q - k;

      // Le nom s'efface et monte un peu ; le schéma arrive.
      const titre = 1 - lisse(0.06, 0.4, P);
      plan.style.setProperty('--titre', titre.toFixed(3));
      plan.style.setProperty('--monte', `${(-(1 - titre) * 0.06 * H).toFixed(1)}px`);
      plan.style.setProperty('--note', (1 - lisse(0.02, 0.1, P)).toFixed(3));
      tete.style.visibility = titre < 0.004 ? 'hidden' : '';
      plan.style.setProperty('--scene', lisse(-0.3, 0.02, q).toFixed(3));

      // Les tableaux : chacun entre au début de son premier temps et sort au début du suivant ;
      // la courbe revient pour retarder et ralentir.
      const entre = (k) => lisse(0.06, 0.28, u(k)), sort = (k) => lisse(0, 0.22, u(k));
      const courbe = (1 - sort(T.cellule)) + entre(T.retarder) * (1 - sort(T.sang));
      opacite(g.courbe, courbe);
      poser(g.courbe, 'transform', `scale(${(0.95 + 0.05 * courbe).toFixed(3)})`);
      opacite(g.cellule, entre(T.cellule) * (1 - sort(T.embryon)));
      opacite(g.embryon, entre(T.embryon) * (1 - sort(T.retarder)));
      opacite(g.sang, lisse(0.08, 0.3, u(T.sang)) * (1 - sort(T.mesure)));
      opacite(g.mesure, entre(T.mesure) * (1 - sort(T.humain)));
      opacite(g.humain, entre(T.humain) * (1 - sort(T.appel)));

      // La courbe du risque se trace.
      trace(el.humain, lisse(0.04, 0.62, u(T.courbe)));
      opacite(nom.humain, lisse(0.5, 0.72, u(T.courbe)));
      // À 10 ans, un point ; s'il ne montait plus, une ligne plate qui s'étend. Ces tracés partent
      // avec la courbe, au temps de la cellule, et ne reviennent pas avec elle.
      const sansPlat = 1 - lisse(0.02, 0.24, u(T.cellule));
      opacite(el.dix, lisse(0.04, 0.2, u(T.plat)) * sansPlat);
      opacite(nom.dix, lisse(0.08, 0.26, u(T.plat)) * sansPlat);
      poser(el.platRect, '@width', (8 + (X1 - X0 + 8) * lisse(0.12, 0.6, u(T.plat))).toFixed(1));
      opacite(el.plat, lisse(0.1, 0.16, u(T.plat)) * (1 - lisse(0.3, 0.6, u(T.hydre))));
      opacite(nom.plat, lisse(0.5, 0.7, u(T.plat)) * (1 - lisse(0.04, 0.24, u(T.hydre))));
      // Chez l'hydre, cette ligne est réelle.
      trace(el.hydre, lisse(0.08, 0.56, u(T.hydre)));
      poser(el.hydre, 'opacity', sansPlat.toFixed(3));
      opacite(nom.hydre, lisse(0.4, 0.62, u(T.hydre)) * sansPlat);
      // La cellule se dessine, puis ce qui s'y abîme : l'ADN se casse, les mitochondries, les
      // amas de protéines ; enfin leurs noms.
      trace(el.membrane, lisse(0.06, 0.42, u(T.cellule)));
      trace(el.noyau, lisse(0.14, 0.46, u(T.cellule)));
      opacite(el.adn, lisse(0.3, 0.42, u(T.cellule)));
      opacite(el.casse, lisse(0.42, 0.5, u(T.cellule)));
      apparaitre(mitos, u(T.cellule), 0.36, 0.04);
      apparaitre(amas, u(T.cellule), 0.46, 0.05);
      apparaitre(kNoms, u(T.cellule), 0.52, 0.05, 0.12);
      // L'âge biologique redescend au début de l'embryon, puis remonte.
      trace(el.eCourbe, lisse(0.08, 0.46, u(T.embryon)));
      opacite(el.eZero, lisse(0.36, 0.46, u(T.embryon)));
      opacite(el.eLigne, lisse(0.4, 0.5, u(T.embryon)));
      opacite(nom.zero, lisse(0.4, 0.56, u(T.embryon)));
      // Quatre facteurs ramènent une cellule adulte en bas.
      opacite(el.eAdulte, lisse(0.06, 0.16, u(T.facteurs)));
      trace(el.eSaut, lisse(0.14, 0.46, u(T.facteurs)));
      opacite(nom.facteurs, lisse(0.36, 0.56, u(T.facteurs)));
      // Retarder : la courbe glisse vers la droite ; sa place reste en pointillé.
      poser(el.humain, '@d', tracer(K, lisse(0.08, 0.6, u(T.retarder)) * DECALE));
      opacite(el.fantome, lisse(0.04, 0.24, u(T.retarder)));
      opacite(nom.retarder, lisse(0.46, 0.68, u(T.retarder)));
      // Ralentir : depuis la courbe d'origine, une pente plus douce, en or.
      opacite(el.ralenti, lisse(0.02, 0.1, u(T.ralentir)));
      poser(el.ralenti, '@d', tracer(melange(K, K_FIN, lisse(0.08, 0.62, u(T.ralentir))), 0));
      opacite(nom.ralentir, lisse(0.5, 0.72, u(T.ralentir)));
      // Deux gouttes de sang se dessinent, puis leurs cellules.
      gouttes.forEach((c) => trace(c, lisse(0.12, 0.5, u(T.sang))));
      opacite(legende, lisse(0.3, 0.5, u(T.sang)));
      cellules.forEach((c, i) => {
        const a = 0.3 + 0.014 * (i % 14) + 0.05 * Math.floor(i / 14);
        opacite(c, lisse(a, a + 0.1, u(T.sang)));
      });
      // L'expérience : les deux gouttes de 16 mois, les flèches, celle de 28 mois à volonté, puis
      // celle que l'on ne connaît pas encore, avec son point d'interrogation.
      opacite(mLegende, 1);
      [0.06, 0.14, 0.4].forEach((a, i) => mGouttes[i] && goutte(mGouttes[i], u(T.mesure), a));
      mFleches.forEach((f) => trace(f, lisse(0.32, 0.46, u(T.mesure))));
      opacite(el.inconnue, lisse(0.56, 0.66, u(T.mesure)));
      opacite(el.question, lisse(0.62, 0.74, u(T.mesure)));
      // La même prise de sang chez l'humain : la goutte de la souris, l'arc, celle de l'humain.
      if (hGouttes[0]) goutte(hGouttes[0], u(T.humain), 0.06);
      opacite(hNoms[0], lisse(0.24, 0.36, u(T.humain)));
      trace(el.arc, lisse(0.3, 0.5, u(T.humain)));
      opacite(nom.mesure, lisse(0.42, 0.54, u(T.humain)));
      if (hGouttes[1]) goutte(hGouttes[1], u(T.humain), 0.46);
      opacite(hNoms[1], lisse(0.62, 0.74, u(T.humain)));

      raconter?.(q);
      // Après le dernier cran, le plan se décroche et monte avec le pied de page : l'appel suit.
      const depasse = Math.max(0, scrollY - (heros.offsetTop + heros.offsetHeight - H));
      if (recit) poser(recit, 'transform', depasse ? `translateY(${(-depasse).toFixed(1)}px)` : '');
    }

    // La scène ne dépend que du défilement : elle se redessine une fois par image quand il change.
    let attente = false;
    const demander = () => { if (!attente) { attente = true; requestAnimationFrame(() => { attente = false; image(); }); } };
    placer();
    image();
    addEventListener('scroll', demander, { passive: true });
    addEventListener('resize', () => { placer(); demander(); });
    document.fonts?.ready.then(() => { placer(); demander(); });
  }
})();
