// ÆTERNAM CAP — maquette interactive. Tout est simulé : aucune donnée EEG réelle.
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduit = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const ACCENT = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#a9c2ff';

  // Règles de la boucle (docs/regles/boucle-qr.md du dépôt ae-cap)
  const SEUIL_FORT = 30, SEUIL_FAIBLE = 300, MAX_Q = 6;
  const RECOMPENSE = { oui: 1, autre: 0.3, rien: -1, ignoree: -0.5 };
  const NOMS = { A: 'Commande A', B: 'Commande B' };
  const IMAGINE = { A: 'main gauche', B: 'main droite' };
  const VOIES = ['FC3', 'FC4', 'C3', 'Cz', 'C4', 'CP3', 'CPz', 'CP4'];
  const virgule = (x) => String(x).replace('.', ',');

  // ---------- temps simulé ----------
  let facteur = 1, simAcc = 0, dernier = performance.now();
  const simNow = () => { const t = performance.now(); simAcc += ((t - dernier) / 1000) * facteur; dernier = t; return simAcc; };

  const etat = { pause: false, questions: [], forts: 0, faibles: 0, recompense: 0, attente: new Map(), id: 0 };

  // ---------- horloge ----------
  const majHeure = () => {
    const d = new Date();
    const h = d.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
    $('#heure').textContent = h;
    $('#heure-petite').textContent = h;
    $('#date').textContent = d.toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' });
  };
  majHeure(); setInterval(majHeure, 10000);

  // ---------- qualité ----------
  const qualites = VOIES.map(() => 'bon');
  const couleur = (q) => (q === 'bon' ? 'var(--accent)' : q === 'moyen' ? 'var(--warn)' : 'var(--bad)');
  const majQualite = () => {
    for (let i = 0; i < qualites.length; i++) { const r = Math.random(); qualites[i] = r < 0.05 ? 'moyen' : r < 0.065 ? 'mauvais' : 'bon'; }
    $('#signal-verrou').innerHTML = qualites.map(q => `<i class="${q === 'bon' ? '' : q}"></i>`).join('');
    $('#qualite').innerHTML = VOIES.map((v, i) => `<span><i style="background:${couleur(qualites[i])}"></i>${v}</span>`).join('');
  };
  majQualite(); setInterval(majQualite, 3000);

  // ---------- messages ----------
  let tMsg;
  const dire = (t) => { $('#message').textContent = t; clearTimeout(tMsg); tMsg = setTimeout(() => ($('#message').textContent = ''), 4500); };

  // ---------- journal ----------
  const fmt = (s) => (s == null ? '—' : s < 60 ? `${Math.round(s)} s` : `${Math.floor(s / 60)} min ${String(Math.round(s % 60)).padStart(2, '0')}`);
  const journal = ({ detecte, reponse, delai, label, poids }) => {
    const tb = $('#journal');
    tb.querySelector('.vide')?.remove();
    const tr = document.createElement('tr');
    tr.className = 'nouveau';
    const cls = poids === 1 ? 'fort' : poids > 0 ? 'faible' : 'aucun';
    const etiquette = poids ? `${label} · ${virgule(poids)}` : label;
    tr.innerHTML = `<td>${new Date().toLocaleTimeString('fr-FR')}</td><td>${detecte}</td><td>${reponse}</td><td>${fmt(delai)}</td><td><span class="lbl ${cls}">${etiquette}</span></td>`;
    tb.prepend(tr);
    while (tb.children.length > 10) tb.lastElementChild.remove();
  };

  const majModele = () => {
    const t = simNow();
    etat.questions = etat.questions.filter(q => t - q < 3600);
    $('#m-forts').textContent = etat.forts;
    $('#m-faibles').textContent = etat.faibles;
    $('#m-questions').textContent = `${etat.questions.length} / ${MAX_Q}`;
    $('#m-recompense').textContent = virgule(Math.round(etat.recompense * 10) / 10);
    const n = Math.floor(etat.forts / 5);
    $('#m-candidate').textContent = n ? `perso u01·${n}` : 'pas encore (5 exemples forts)';
  };
  majModele();

  // ---------- détection → question ----------
  const ICONE = '<span>Æ</span>';

  const detecter = () => {
    if (etat.pause) { dire('En pause : ni détection, ni question, ni action.'); return; }
    majModele();
    const cmd = Math.random() < 0.5 ? 'A' : 'B';
    if (qualites.includes('mauvais')) {
      journal({ detecte: NOMS[cmd], reponse: 'silence', delai: null, label: 'mauvais contact', poids: 0 });
      dire('Une électrode a un mauvais contact : le téléphone se tait.');
      return;
    }
    if (etat.questions.length >= MAX_Q) {
      journal({ detecte: NOMS[cmd], reponse: 'silence', delai: null, label: 'plafond horaire', poids: 0 });
      dire(`Déjà ${MAX_Q} questions cette heure : le téléphone ne vous dérange plus.`);
      return;
    }
    etat.questions.push(simNow());
    montrer('verrou');
    poser(cmd);
    majModele();
  };

  const poser = (cmd) => {
    const id = ++etat.id;
    $$('.notif-groupe', $('#notifs')).forEach(n => n.classList.add('vieille'));
    const g = document.createElement('div');
    g.className = 'notif-groupe';
    g.innerHTML = `
      <div class="notif">
        <div class="notif-icone">${ICONE}</div>
        <div class="notif-corps">
          <div class="notif-ligne"><span class="notif-titre">${NOMS[cmd]} ?</span><span class="notif-temps">maintenant</span></div>
          <div class="notif-texte">Vous avez imaginé « ${IMAGINE[cmd]} » ?</div>
          <div class="notif-delai"></div>
        </div>
      </div>
      <div class="notif-actions">
        <button data-r="oui">Oui</button>
        <button data-r="autre">Non, l’autre commande</button>
        <button data-r="rien">Non, rien</button>
      </div>`;
    $('#notifs').prepend(g);
    while ($('#notifs').children.length > 2) $('#notifs').lastElementChild.remove();
    etat.attente.set(id, { cmd, t0: simNow(), el: g });
    $$('button', g).forEach(b => b.addEventListener('click', () => repondre(id, b.dataset.r)));
  };

  const poidsPour = (d) => (d <= SEUIL_FORT ? 1 : d <= SEUIL_FAIBLE ? 0.3 : 0);

  const repondre = (id, r) => {
    const q = etat.attente.get(id);
    if (!q) return;
    etat.attente.delete(id);
    const d = simNow() - q.t0;
    const autre = q.cmd === 'A' ? 'B' : 'A';
    const label = r === 'oui' ? NOMS[q.cmd] : r === 'autre' ? NOMS[autre] : 'repos';
    const poids = poidsPour(d);
    if (poids === 1) etat.forts++; else if (poids > 0) etat.faibles++;
    etat.recompense += RECOMPENSE[r];
    journal({ detecte: NOMS[q.cmd], reponse: { oui: 'Oui', autre: 'Non, l’autre', rien: 'Non, rien' }[r], delai: d, label: poids ? label : 'trop tard', poids });
    q.el.querySelector('.notif-actions').remove();
    const del = q.el.querySelector('.notif-delai');
    del.classList.remove('faible');
    del.textContent = poids ? `Noté : « ${label} », poids ${virgule(poids)}` : 'Trop tard : statistiques seulement';
    setTimeout(() => { q.el.style.transition = 'opacity .4s'; q.el.style.opacity = '0'; setTimeout(() => q.el.remove(), 400); }, 2600);
    majModele();
  };

  setInterval(() => {
    const t = simNow();
    for (const [id, q] of etat.attente) {
      const d = t - q.t0, p = poidsPour(d);
      q.el.querySelector('.notif-temps').textContent = d < 5 ? 'maintenant' : d < 60 ? `il y a ${Math.round(d)} s` : `il y a ${Math.floor(d / 60)} min`;
      const del = q.el.querySelector('.notif-delai');
      del.classList.toggle('faible', p < 1);
      del.textContent = p === 1 ? `Exemple fort encore ${Math.ceil(SEUIL_FORT - d)} s` : 'Exemple faible (poids 0,3)';
      if (d > SEUIL_FAIBLE) {
        etat.attente.delete(id);
        etat.recompense += RECOMPENSE.ignoree;
        journal({ detecte: NOMS[q.cmd], reponse: 'ignorée', delai: d, label: 'aucun', poids: 0 });
        q.el.remove();
        majModele();
      }
    }
  }, 250);

  $('#detecter').addEventListener('click', detecter);
  $('#pause').addEventListener('click', (e) => {
    etat.pause = !etat.pause;
    e.currentTarget.setAttribute('aria-pressed', String(etat.pause));
    e.currentTarget.textContent = etat.pause ? 'Reprendre' : 'Pause';
    dire(etat.pause ? 'Pause : tout est coupé.' : 'Reprise.');
  });
  $('#accelerer').addEventListener('change', (e) => { simNow(); facteur = e.target.checked ? 10 : 1; });

  // ---------- onglets ----------
  let calibActive = false, debutCalib = 0, etapePrec = -1;
  const montrer = (nom) => {
    $$('.ecran').forEach(e => e.classList.toggle('actif', e.dataset.ecran === nom));
    $$('.onglets button').forEach(b => b.setAttribute('aria-selected', String(b.dataset.cible === nom)));
    calibActive = nom === 'calib';
    if (calibActive) { debutCalib = performance.now(); etapePrec = -1; requestAnimationFrame(calib); }
  };
  $$('.onglets button').forEach(b => b.addEventListener('click', () => montrer(b.dataset.cible)));

  // ---------- signal simulé ----------
  const phases = VOIES.map(() => Math.random() * Math.PI * 2);
  const tracer = (ctx, W, H, now, amp, x0, col) => {
    const rang = H / VOIES.length;
    for (let v = 0; v < VOIES.length; v++) {
      const y0 = rang * v + rang / 2;
      ctx.beginPath();
      ctx.strokeStyle = col(v);
      for (let x = x0; x <= W; x += 3) {
        const t = now / 1000 + x / 170;
        const y = y0
          + Math.sin(t * 2 * Math.PI * 10 + phases[v]) * rang * 0.26 * amp(v)
          + Math.sin(t * 2 * Math.PI * 2.7 + phases[v] * 1.7) * rang * 0.1
          + Math.sin(t * 2 * Math.PI * 21 + phases[v] * 3) * rang * 0.05
          + (Math.random() - 0.5) * rang * 0.1;
        x === x0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
      }
      ctx.stroke();
    }
  };

  // Calibration guidée
  const SEQ = [
    { c: 'Repos', s: 'Respirez, ne pensez à rien de précis.', t: null },
    { c: 'Imaginez : main gauche', s: 'Serrer le poing, sans bouger.', t: 'A' },
    { c: 'Repos', s: 'Relâchez.', t: null },
    { c: 'Imaginez : main droite', s: 'Serrer le poing, sans bouger.', t: 'B' },
  ];
  const DUREE = 4000;
  const cv = $('#traces'), ctx = cv.getContext('2d');
  const calib = (now) => {
    if (!calibActive) return;
    const e0 = now - debutCalib, etape = Math.floor(e0 / DUREE) % SEQ.length, e = SEQ[etape];
    if (etape !== etapePrec) {
      $('#consigne').textContent = e.c; $('#consigne').classList.toggle('tache', !!e.t);
      $('#sous-consigne').textContent = e.s; etapePrec = etape;
    }
    $('#progression').style.width = `${((e0 % (DUREE * SEQ.length)) / (DUREE * SEQ.length)) * 100}%`;
    ctx.clearRect(0, 0, cv.width, cv.height);
    ctx.lineWidth = 1.6;
    ctx.font = '15px -apple-system, sans-serif';
    const rang = cv.height / VOIES.length;
    // Baisse du rythme mu au-dessus de l'hémisphère opposé à la main imaginée
    const baisse = (v) => (e.t === 'A' && /4$/.test(VOIES[v])) || (e.t === 'B' && /3$/.test(VOIES[v]));
    VOIES.forEach((v, i) => { ctx.fillStyle = 'rgba(255,255,255,.4)'; ctx.fillText(v, 0, rang * i + rang / 2 + 5); });
    tracer(ctx, cv.width, cv.height, now, v => (baisse(v) ? 0.3 : 1), 48, v => (qualites[v] === 'mauvais' ? '#7c86a0' : baisse(v) ? ACCENT : 'rgba(255,255,255,.7)'));
    if (!reduit) requestAnimationFrame(calib);
  };

  // Bandeau du héros
  const bd = $('#bandeau');
  if (bd) {
    const bctx = bd.getContext('2d');
    const taille = () => { const r = bd.getBoundingClientRect(); bd.width = r.width * devicePixelRatio; bd.height = r.height * devicePixelRatio; };
    taille(); addEventListener('resize', taille);
    let visible = true;
    new IntersectionObserver(([en]) => { visible = en.isIntersecting; if (visible && !reduit) requestAnimationFrame(boucle); }).observe(bd);
    const boucle = (now) => {
      if (!visible) return;
      bctx.clearRect(0, 0, bd.width, bd.height);
      bctx.lineWidth = 1.1 * devicePixelRatio;
      tracer(bctx, bd.width, bd.height, now * 0.6, () => 0.8, 0, v => (v === 2 || v === 4 ? ACCENT : `rgba(255,255,255,${0.12 + v * 0.02})`));
      if (!reduit) requestAnimationFrame(boucle);
    };
    requestAnimationFrame(boucle);
  }

  // ---------- trois cerveaux, trois signatures ----------
  // Positions de dessus (nez en haut) ; valeur = baisse relative du rythme pendant « main gauche ».
  const POS = { FC3: [52, 62], FC4: [108, 62], C3: [40, 84], Cz: [80, 84], C4: [120, 84], CP3: [52, 106], CPz: [80, 110], CP4: [108, 106] };
  const MOTIFS = {
    a: { C4: 1, FC4: 0.45, CP4: 0.5, Cz: 0.15 },
    b: { CP4: 0.6, CPz: 0.45, C4: 0.35, CP3: 0.15 },
    c: { C4: 0.55, C3: 0.5, Cz: 0.35, FC4: 0.25, FC3: 0.2 },
  };
  $$('.topo').forEach((svg, k) => {
    const m = MOTIFS[svg.dataset.motif];
    let html = `<defs><radialGradient id="tg${k}"><stop offset="0" stop-color="${ACCENT}" stop-opacity=".9"/><stop offset="1" stop-color="${ACCENT}" stop-opacity="0"/></radialGradient></defs>`;
    html += '<path class="nez" d="M72 18 L80 6 L88 18"/><circle class="crane" cx="80" cy="84" r="66"/>';
    for (const [n, [x, y]] of Object.entries(POS)) {
      const v = m[n] || 0;
      if (v) html += `<circle cx="${x}" cy="${y}" r="${12 + v * 22}" fill="url(#tg${k})" opacity="${0.25 + v * 0.75}"/>`;
    }
    for (const [n, [x, y]] of Object.entries(POS)) html += `<circle class="pt" cx="${x}" cy="${y}" r="3.2"/><text x="${x}" y="${y + 12}">${n}</text>`;
    html += '<text x="80" y="158" style="font-size:7.5px;fill:var(--faint)">même consigne : main gauche</text>';
    svg.innerHTML = html;
  });
})();
