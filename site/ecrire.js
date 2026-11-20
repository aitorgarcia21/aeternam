// Écrire sur ÆTERNAM : prépare le fichier Markdown d'un article signé
// (contributions/AAAA-MM-JJ-titre-court.md) et l'ouvre sur GitHub, où il devient
// une proposition publique, relue avant publication. Rien n'est envoyé ailleurs ;
// le brouillon reste dans ce navigateur.
(() => {
  'use strict';
  const EN = document.documentElement.lang === 'en';
  const t = (fr, en) => (EN ? en : fr);
  const form = document.getElementById('proposer');
  if (!form) return;
  const depot = form.dataset.depot;
  const etat = document.getElementById('etat');
  const NOMS = ['titre', 'auteur', 'theme', 'resume', 'orcid', 'texte'];
  const CLE = 'aeternam-brouillon';
  const champ = (nom) => form.elements[nom];

  try {
    const brouillon = JSON.parse(localStorage.getItem(CLE) || '{}');
    NOMS.forEach((n) => { if (typeof brouillon[n] === 'string') champ(n).value = brouillon[n]; });
  } catch (e) { /* stockage indisponible : on écrit sans brouillon */ }
  form.addEventListener('input', () => {
    try { localStorage.setItem(CLE, JSON.stringify(Object.fromEntries(NOMS.map((n) => [n, champ(n).value])))); } catch (e) { /* idem */ }
  });

  const ligne = (v) => v.replace(/\s+/g, ' ').trim();
  const aujourdhui = () => {
    const d = new Date();
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  };
  const court = (titre) => titre.normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase()
    .replace(/œ/g, 'oe').replace(/æ/g, 'ae').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '')
    .split('-').slice(0, 8).join('-').slice(0, 60).replace(/-+$/, '') || 'article';

  // Mêmes règles que la construction du site (site/contributions.py).
  function fichier() {
    const titre = ligne(champ('titre').value), auteur = ligne(champ('auteur').value);
    const theme = champ('theme').value, resume = ligne(champ('resume').value), orcid = ligne(champ('orcid').value);
    const texte = champ('texte').value.replace(/\r\n?/g, '\n').trim();
    const problemes = [];
    if (titre.length < 3) problemes.push(t('Donnez un titre.', 'Give your article a title.'));
    if (auteur.length < 2) problemes.push(t('Signez de votre nom.', 'Sign with your name.'));
    else if (/https?:\/\/|[<>]/.test(auteur)) problemes.push(t('La signature est un nom, sans lien.', 'The signature is a name, without a link.'));
    if (orcid && !/^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$/.test(orcid)) problemes.push(t('ORCID attendu sous la forme 0000-0000-0000-0000.', 'ORCID expected in the form 0000-0000-0000-0000.'));
    if (texte.length < 200) problemes.push(t(`Le texte doit faire au moins 200 caractères (${texte.length} pour l’instant).`, `The text must be at least 200 characters long (${texte.length} so far).`));
    if (problemes.length) return { erreur: problemes.join(' ') };
    const date = aujourdhui();
    const tete = ['---', `titre: ${titre}`, `auteur: ${auteur}`, `date: ${date}`];
    if (EN) tete.push('langue: en');
    if (theme) tete.push(`theme: ${theme}`);
    if (resume) tete.push(`resume: ${resume}`);
    if (orcid) tete.push(`orcid: ${orcid}`);
    tete.push('licence: CC BY 4.0', '---');
    return { nom: `${date}-${court(titre)}.md`, contenu: `${tete.join('\n')}\n\n${texte}\n` };
  }

  function copier(texte) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(texte).then(() => true, () => false);
    return Promise.resolve(false);
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const f = fichier();
    if (f.erreur) { etat.textContent = f.erreur; return; }
    const base = `${depot}/new/main?filename=${encodeURIComponent('contributions/' + f.nom)}`;
    const complet = `${base}&value=${encodeURIComponent(f.contenu)}`;
    const long = complet.length > 7500;  // au-delà, l'adresse serait tronquée : le texte passe par le presse-papiers
    copier(f.contenu).then((ok) => {
      etat.textContent = long
        ? (ok ? t(`Texte long : il est copié. Collez-le sur la page GitHub qui vient de s’ouvrir (fichier contributions/${f.nom}).`, `Long text: it has been copied. Paste it into the GitHub page that has just opened (file contributions/${f.nom}).`)
              : t('Texte long : utilisez « Télécharger », puis déposez le fichier sur la page GitHub qui vient de s’ouvrir.', 'Long text: use “Download”, then drop the file onto the GitHub page that has just opened.'))
        : t(`GitHub s’ouvre avec contributions/${f.nom}${ok ? ', aussi copié' : ''}. Validez avec « Propose changes », puis ouvrez la demande de publication.`, `GitHub opens with contributions/${f.nom}${ok ? ', also copied' : ''}. Confirm with “Propose changes”, then open the publication request.`);
    });
    window.open(long ? base : complet, '_blank', 'noopener');
  });

  form.querySelectorAll('[data-action]').forEach((b) => b.addEventListener('click', () => {
    const f = fichier();
    if (f.erreur) { etat.textContent = f.erreur; return; }
    if (b.dataset.action === 'copier') {
      copier(f.contenu).then((ok) => {
        etat.textContent = ok ? t(`Fichier copié : contributions/${f.nom}`, `File copied: contributions/${f.nom}`) : t('Copie impossible ici : utilisez « Télécharger ».', 'Copying is not possible here: use “Download”.');
      });
      return;
    }
    const lien = document.createElement('a');
    lien.href = URL.createObjectURL(new Blob([f.contenu], { type: 'text/markdown;charset=utf-8' }));
    lien.download = f.nom;
    document.body.append(lien);
    lien.click();
    lien.remove();
    setTimeout(() => URL.revokeObjectURL(lien.href), 1000);
    etat.textContent = t(`Fichier ${f.nom} téléchargé : à déposer dans le dossier contributions/ du dépôt.`, `File ${f.nom} downloaded: drop it into the repository’s contributions/ folder.`);
  }));
})();
