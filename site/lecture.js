/* Les liens fonctionnent sans JavaScript ; celui-ci suit la section lue. */
(() => {
  const EN = document.documentElement.lang === 'en';
  const t = (fr, en) => (EN ? en : fr);
  const liens = [...document.querySelectorAll('.reperes-lecture a[href^="#"]')];
  const titres = [...document.querySelectorAll('.corps-article h2[id]')];
  if (!titres.length) return;
  let programme = false;
  function actualiser() {
    programme = false;
    let actif = titres[0].id;
    for (const titre of titres) {
      if (titre.getBoundingClientRect().top <= 150) actif = titre.id;
      else break;
    }
    for (const lien of liens) {
      if (lien.hash === '#' + actif) lien.setAttribute('aria-current', 'location');
      else lien.removeAttribute('aria-current');
    }
  }
  window.addEventListener('scroll', () => {
    if (!programme) { programme = true; requestAnimationFrame(actualiser); }
  }, { passive: true });
  window.addEventListener('resize', actualiser);
  for (const lien of liens) {
    lien.addEventListener('click', () => {
      const detail = lien.closest('details');
      if (detail) detail.open = false;
      const titre = document.getElementById(lien.hash.slice(1));
      if (titre) {
        titre.setAttribute('tabindex', '-1');
        titre.focus({ preventScroll: true });
      }
      requestAnimationFrame(actualiser);
    });
  }
  /* Les tableaux débordants se parcourent aussi au clavier. */
  for (const tableau of document.querySelectorAll('.tableau')) {
    tableau.tabIndex = 0;
    tableau.setAttribute('role', 'region');
    tableau.setAttribute('aria-label', t('Tableau, défilement horizontal si nécessaire', 'Table, scrolls horizontally if needed'));
  }
  actualiser();
})();
