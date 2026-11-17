// CAP : démonstration de la boucle de questions. Tout est simulé dans le navigateur ;
// l'exactitude du décodeur suit la courbe du Monte-Carlo publiée avec l'étude (data-courbe).
(() => {
  'use strict';
  const racine = document.getElementById('boucle');
  if (!racine) return;
  const $ = (id) => document.getElementById(id);
  const courbe = JSON.parse(racine.dataset.courbe);
  const MAINS = { gauche: 'main gauche', droite: 'main droite' };
  const FORT = 30, FAIBLE = 300;              // secondes
  const etat = { forts: 0, faibles: 0, question: null };

  const pct = (x) => (100 * x).toFixed(1).replace('.', ',') + ' %';
  const virgule = (x) => String(x).replace('.', ',');
  const autre = (m) => (m === 'gauche' ? 'droite' : 'gauche');
  const majuscule = (t) => t.charAt(0).toUpperCase() + t.slice(1);
  const delai = (s) => (s < 60 ? `${Math.round(s)} s` : `${Math.floor(s / 60)} min ${String(Math.round(s % 60)).padStart(2, '0')}`);
  const poids = (s) => (s <= FORT ? 1 : s <= FAIBLE ? 0.3 : 0);

  // Exactitude attendue pour n essais étiquetés : interpolation sur log2(1 + n).
  function exactitude(n) {
    const t = Math.log2(1 + n);
    for (let i = 1; i < courbe.length; i++) {
      const a = Math.log2(1 + courbe[i - 1][0]), b = Math.log2(1 + courbe[i][0]);
      if (t <= b) return courbe[i - 1][1] + (t - a) / (b - a) * (courbe[i][1] - courbe[i - 1][1]);
    }
    return courbe[courbe.length - 1][1];
  }
  const effectifs = () => etat.forts + 0.3 * etat.faibles;

  function horloge() {
    const d = new Date();
    $('tel-heure').textContent = d.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
    $('tel-date').textContent = d.toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' });
  }
  horloge();
  setInterval(horloge, 15000);

  function majEtat() {
    const total = etat.forts + etat.faibles;
    const fin = courbe[courbe.length - 1];
    $('boucle-etat').textContent = total
      ? `Couche personnelle : ${etat.forts} exemple${etat.forts > 1 ? 's' : ''} fort${etat.forts > 1 ? 's' : ''}, `
        + `${etat.faibles} faible${etat.faibles > 1 ? 's' : ''}. Exactitude attendue : ${pct(exactitude(effectifs()))}. `
        + `Il en faudrait ${fin[0]} pour approcher ${pct(fin[1])}.`
      : `Aucun exemple personnel : le décodeur ne s’appuie que sur le socle commun, ${pct(exactitude(0))} attendus.`;
  }

  function boutons(actifs) {
    racine.querySelectorAll('[data-imagine]').forEach((b) => { b.disabled = !actifs; });
  }

  function journal(cellules, classe) {
    const corps = $('boucle-journal');
    corps.querySelector('.vide')?.remove();
    const tr = document.createElement('tr');
    tr.innerHTML = cellules.map((c, i) => `<td${i === 4 && classe ? ` class="${classe}"` : ''}>${c}</td>`).join('');
    corps.prepend(tr);
    while (corps.children.length > 6) corps.lastElementChild.remove();
  }

  function imaginer(vrai) {
    if (etat.question) return;
    const p = exactitude(effectifs());
    const lu = Math.random() < p ? vrai : autre(vrai);
    $('boucle-lecture').innerHTML = `Vous imaginez la ${MAINS[vrai]}. Le décodeur lit <strong>la ${MAINS[lu]}</strong>`
      + (lu === vrai ? ' : c’est juste.' : ' : il se trompe.') + ' Répondez sur l’écran verrouillé.';
    const notif = document.createElement('div');
    notif.className = 'notif';
    notif.innerHTML = `<div class="notif-tete"><span class="notif-app" aria-hidden="true">Æ</span>CAP<span class="notif-temps">maintenant</span></div>
<p class="notif-titre">${majuscule(MAINS[lu])} ?</p><p class="notif-aide"></p>
<div class="notif-actions"><button type="button" data-r="oui">Oui</button><button type="button" data-r="autre">Non, l’autre</button><button type="button" data-r="rien">Non, rien</button></div>`;
    $('tel-notifs').replaceChildren(notif);
    etat.question = { vrai, lu, debut: performance.now(), notif };
    notif.querySelectorAll('[data-r]').forEach((b) => b.addEventListener('click', () => repondre(b.dataset.r)));
    boutons(false);
    suivre();
  }

  function repondre(r) {
    const q = etat.question;
    if (!q) return;
    etat.question = null;
    const s = (performance.now() - q.debut) / 1000;
    const w = poids(s);
    const etiquette = r === 'oui' ? q.lu : r === 'autre' ? autre(q.lu) : 'repos';
    const juste = etiquette === q.vrai;
    if (w === 1) etat.forts += 1; else if (w > 0) etat.faibles += 1;
    const appris = w ? `${etiquette} · ${virgule(w)}${juste ? '' : ' · faux'}` : 'rien, trop tard';
    journal([q.vrai, q.lu, { oui: 'Oui', autre: 'Non, l’autre', rien: 'Non, rien' }[r], delai(s), appris],
            !w ? 'aucun' : !juste ? 'faux' : w < 1 ? 'faible' : '');
    q.notif.querySelector('.notif-actions').remove();
    q.notif.querySelector('.notif-aide').textContent = w
      ? `Noté : exemple « ${etiquette === 'repos' ? 'repos' : MAINS[etiquette]} », poids ${virgule(w)}.`
      : 'Trop tard : gardé pour les statistiques seulement.';
    $('boucle-lecture').textContent = juste || !w
      ? 'Imaginez à nouveau une main pour continuer.'
      : 'Cette réponse enseigne une étiquette fausse : la couche personnelle n’apprend que ce que vous lui dites.';
    setTimeout(() => { if (!etat.question) $('tel-notifs').replaceChildren(); }, 2600);
    boutons(true);
    majEtat();
  }

  function suivre() {
    const q = etat.question;
    if (!q) return;
    const s = (performance.now() - q.debut) / 1000;
    if (s > FAIBLE) {
      etat.question = null;
      journal([q.vrai, q.lu, 'aucune', delai(s), 'rien'], 'aucun');
      $('tel-notifs').replaceChildren();
      $('boucle-lecture').textContent = 'Question restée sans réponse : rien à apprendre, et une gêne de plus.';
      boutons(true);
      majEtat();
      return;
    }
    q.notif.querySelector('.notif-temps').textContent = s < 5 ? 'maintenant' : `il y a ${delai(s)}`;
    q.notif.querySelector('.notif-aide').textContent = s <= FORT
      ? `Exemple fort si vous répondez dans ${Math.ceil(FORT - s)} s`
      : 'Exemple faible : poids 0,3';
    setTimeout(suivre, 250);
  }

  racine.querySelectorAll('[data-imagine]').forEach((b) => b.addEventListener('click', () => imaginer(b.dataset.imagine)));
  majEtat();
})();
