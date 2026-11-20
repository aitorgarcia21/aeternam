/* Commun à toutes les pages : la pastille de navigation, l'arrivée des blocs, le trait qui vit.
   Rien d'essentiel ne dépend de ce fichier : sans lui, tout est déjà affiché. */
(() => {
  'use strict';
  const racine = document.documentElement;
  const calme = matchMedia('(prefers-reduced-motion: reduce)');

  // La pastille s'efface quand on descend et revient dès qu'on remonte.
  let dernier = scrollY, attente = false;
  addEventListener('scroll', () => {
    if (attente) return;
    attente = true;
    requestAnimationFrame(() => {
      attente = false;
      const y = scrollY;
      if (Math.abs(y - dernier) < 8) return;
      racine.classList.toggle('barre-cachee', y > dernier && y > 320);
      dernier = y;
    });
  }, { passive: true });
  document.querySelector('.barre')?.addEventListener('focusin', () => racine.classList.remove('barre-cachee'));

  // Les blocs marqués data-vu reçoivent .vu à leur arrivée : les dessins se tracent.
  const blocs = document.querySelectorAll('[data-vu]');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entrees) => {
      for (const e of entrees) if (e.isIntersecting) { e.target.classList.add('vu'); io.unobserve(e.target); }
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.1 });
    blocs.forEach((b) => io.observe(b));
  } else {
    blocs.forEach((b) => b.classList.add('vu'));
  }

  // Mouvement réduit : les animations des dessins (SMIL) s'arrêtent aussi.
  const dessins = document.querySelectorAll('svg.dessin');
  let anime = true;
  function regler() {
    anime = !calme.matches;
    dessins.forEach((s) => {
      if (!s.pauseAnimations) return;
      if (anime) s.unpauseAnimations(); else s.pauseAnimations();
    });
  }
  regler();
  calme.addEventListener('change', regler);

  // Le trait vit : la graine du bruit change quelques fois par seconde, comme un dessin
  // animé à la main. Pas sur les écrans tactiles, pour ménager la batterie.
  const bruits = document.querySelectorAll('#trait feTurbulence, #trait2 feTurbulence');
  if (bruits.length && !matchMedia('(pointer: coarse)').matches) {
    const graines = [[4, 19], [11, 27], [23, 5]];
    let i = 0;
    setInterval(() => {
      if (!anime || document.hidden) return;
      i = (i + 1) % graines.length;
      bruits.forEach((b, k) => b.setAttribute('seed', graines[i][k % 2]));
    }, 180);
  }
})();
