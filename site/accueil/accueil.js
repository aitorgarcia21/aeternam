/* L'accueil, sur la nuit unie. Premier écran : le nom et la question, seuls. Au défilement,
   le nom s'efface et huit temps se succèdent, un par écran, chacun avec son schéma : la courbe du
   risque de mourir se trace ; sans sa montée, une ligne plate ; chez l'hydre, cette ligne est
   réelle ; retarder repousse la courbe ; ralentir adoucit sa pente ; une cellule et ce qui s'y
   abîme ; l'âge biologique qui redescend au début de l'embryon ; deux gouttes de sang, l'une plus
   jeune. Puis la feuille monte : l'expérience à financer, en trois écrans, puis l'appel, dont les phrases
   s'éclairent mot à mot. Sans ce fichier, ou en mouvement réduit : le nom, la question, puis les
   temps, écrits dans la page. */
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
  // DEBUT et PAS servent aussi à la hauteur de .heros (accueil.css) : les deux vont ensemble.
  const DEBUT = 0.55, PAS = 1.15;
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
    const recit = document.getElementById('recit');

    if (!calme && dessin) {
      // Mêmes nombres que SCENE_* de site/dessins.py : y = (e^(k·u) − 1) / (e^K − 1).
      const X0 = 64, X1 = 530, BAS = 410, HAUT = 70, K = 4.2, K_FIN = 2.6, DECALE = 88;
      const $ = (id) => dessin.querySelector(`#${id}`);
      const tous = (sel) => [...dessin.querySelectorAll(sel)];
      const g = { courbe: $('scene-courbe'), cellule: $('scene-cellule'), embryon: $('scene-embryon'), sang: $('scene-sang') };
      const nombreDeTemps = recit ? recit.querySelectorAll('.temps').length : 0;
      const raconter = nombreDeTemps ? recitScene(recit) : null;

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

      function tracer(k, decale) {
        const echelle = Math.exp(K) - 1, longueur = X1 - X0, fin = (longueur - decale) / longueur;
        let d = `M${X0} ${BAS}`;
        for (let i = 0; i <= 80; i++) {
          const u = fin * i / 80;
          d += ` L${(X0 + decale + longueur * u).toFixed(1)} ${(BAS - (BAS - HAUT) * (Math.exp(k * u) - 1) / echelle).toFixed(1)}`;
        }
        return d;
      }

      // En hauteur, le schéma se place au milieu de ce que le plus long des temps laisse libre.
      const enHauteur = matchMedia('not all and (min-width: 900px) and (orientation: landscape)');
      function placer() {
        if (!recit) return;
        let bas = 0;
        if (enHauteur.matches) recit.querySelectorAll('.temps').forEach((t) => { bas = Math.max(bas, t.offsetTop + t.offsetHeight); });
        if (bas) plan.style.setProperty('--texte-bas', `${Math.round(bas)}px`);
        else plan.style.removeProperty('--texte-bas');
      }

      const el = {
        humain: $('c-humain'), plat: $('c-plat'), platRect: $('plat-rect'), hydre: $('c-hydre'), fantome: $('c-fantome'),
        ralenti: $('c-ralentir'), dix: $('p-dix'), membrane: $('k-membrane'), noyau: $('k-noyau'), adn: $('k-adn'),
        casse: $('k-casse'), eCourbe: $('e-courbe'), eSaut: $('e-saut'), eZero: $('e-zero'), eLigne: $('e-zero-ligne'), eAdulte: $('e-adulte'),
      };
      const nom = {
        humain: $('n-humain'), dix: $('n-dix'), plat: $('n-plat'), hydre: $('n-hydre'), retarder: $('n-retarder'),
        ralentir: $('n-ralentir'), zero: $('n-zero'), facteurs: $('n-facteurs'),
      };
      const mitos = tous('.k-mito'), amas = tous('.k-amas'), kNoms = tous('.k-nom');
      const gouttes = tous('.goutte'), cellules = tous('#scene-sang .cellule.a'), legende = $('scene-sang')?.querySelector('.sang-legende');

      function image() {
        if (!innerHeight) return;            // fenêtre sans hauteur : rien à dessiner
        const P = (scrollY - heros.offsetTop) / innerHeight;
        const q = (P - DEBUT) / PAS, u = (k) => q - k;

        // Le nom s'efface et monte un peu ; le schéma arrive.
        const titre = 1 - lisse(0.06, 0.4, P);
        plan.style.setProperty('--titre', titre.toFixed(3));
        plan.style.setProperty('--monte', `${(-(1 - titre) * 0.06 * innerHeight).toFixed(1)}px`);
        plan.style.setProperty('--note', (1 - lisse(0.02, 0.1, P)).toFixed(3));
        tete.style.visibility = titre < 0.004 ? 'hidden' : '';
        plan.style.setProperty('--scene', lisse(-0.3, 0.02, q).toFixed(3));

        // Les tableaux : chacun entre au début de son premier temps et sort au début du suivant.
        const sort = (k) => lisse(0, 0.22, u(k));
        opacite(g.courbe, 1 - sort(5));
        poser(g.courbe, 'transform', `scale(${(1 - 0.05 * sort(5)).toFixed(3)})`);
        opacite(g.cellule, lisse(0.06, 0.28, u(5)) * (1 - sort(6)));
        opacite(g.embryon, lisse(0.06, 0.28, u(6)) * (1 - sort(7)));
        opacite(g.sang, lisse(0.08, 0.3, u(7)));

        // 1. La courbe du risque se trace.
        trace(el.humain, lisse(0.04, 0.62, u(0)));
        opacite(nom.humain, lisse(0.5, 0.72, u(0)));
        // 2. À 10 ans, un point ; s'il ne montait plus, une ligne plate qui s'étend.
        const sansDix = 1 - lisse(0.02, 0.24, u(3));
        opacite(el.dix, lisse(0.04, 0.2, u(1)) * sansDix);
        opacite(nom.dix, lisse(0.08, 0.26, u(1)) * sansDix);
        poser(el.platRect, '@width', (8 + (X1 - X0 + 8) * lisse(0.12, 0.6, u(1))).toFixed(1));
        opacite(el.plat, lisse(0.1, 0.16, u(1)) * (1 - lisse(0.3, 0.6, u(2))));
        opacite(nom.plat, lisse(0.5, 0.7, u(1)) * (1 - lisse(0.04, 0.24, u(2))));
        // 3. Chez l'hydre, cette ligne est réelle ; elle s'efface au temps suivant.
        const sansHydre = 1 - lisse(0.02, 0.24, u(3));
        trace(el.hydre, lisse(0.08, 0.56, u(2)));
        poser(el.hydre, 'opacity', sansHydre.toFixed(3));
        opacite(nom.hydre, lisse(0.4, 0.62, u(2)) * sansHydre);
        // 4. Retarder : la courbe glisse vers la droite ; sa place reste en pointillé.
        poser(el.humain, '@d', tracer(K, lisse(0.08, 0.6, u(3)) * DECALE));
        opacite(el.fantome, lisse(0.04, 0.24, u(3)));
        opacite(nom.retarder, lisse(0.46, 0.68, u(3)));
        // 5. Ralentir : depuis la courbe d'origine, une pente plus douce, en or.
        opacite(el.ralenti, lisse(0.02, 0.1, u(4)));
        poser(el.ralenti, '@d', tracer(melange(K, K_FIN, lisse(0.08, 0.62, u(4))), 0));
        opacite(nom.ralentir, lisse(0.5, 0.72, u(4)));
        // 6. La cellule se dessine, puis ce qui s'y abîme : l'ADN se casse, les mitochondries,
        // les amas de protéines ; enfin leurs noms.
        trace(el.membrane, lisse(0.06, 0.42, u(5)));
        trace(el.noyau, lisse(0.14, 0.46, u(5)));
        opacite(el.adn, lisse(0.3, 0.42, u(5)));
        opacite(el.casse, lisse(0.42, 0.5, u(5)));
        apparaitre(mitos, u(5), 0.36, 0.04);
        apparaitre(amas, u(5), 0.46, 0.05);
        apparaitre(kNoms, u(5), 0.52, 0.05, 0.12);
        // 7. L'âge biologique redescend au début de l'embryon, puis remonte ; quatre facteurs
        // ramènent une cellule adulte en bas.
        trace(el.eCourbe, lisse(0.08, 0.46, u(6)));
        opacite(el.eZero, lisse(0.36, 0.46, u(6)));
        opacite(el.eLigne, lisse(0.4, 0.5, u(6)));
        opacite(nom.zero, lisse(0.4, 0.56, u(6)));
        opacite(el.eAdulte, lisse(0.5, 0.58, u(6)));
        trace(el.eSaut, lisse(0.56, 0.74, u(6)));
        opacite(nom.facteurs, lisse(0.66, 0.8, u(6)));
        // 8. Deux gouttes de sang se dessinent, puis leurs cellules.
        gouttes.forEach((c) => trace(c, lisse(0.12, 0.5, u(7))));
        opacite(legende, lisse(0.3, 0.5, u(7)));
        cellules.forEach((c, i) => {
          const a = 0.3 + 0.014 * (i % 14) + 0.05 * Math.floor(i / 14);
          opacite(c, lisse(a, a + 0.1, u(7)));
        });

        raconter?.(q);
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
