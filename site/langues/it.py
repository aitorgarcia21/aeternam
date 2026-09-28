"""Italien : traduction de fr.py (langue source).

Mêmes marqueurs, formules, balises et attributs que la source ; seul le texte change.
Chaîne brute (r\"\"\"…\"\"\") obligatoire pour le corps à cause des barres obliques inverses.
"""
NOM = 'Italiano'
HTML_LANG = 'it'
HREFLANG = 'it'
DIR = 'ltr'
LOCALE_OG = 'it_IT'
DECIMALE = ','

UI = {
    'devise': 'Ricerca sulla teoria della simulazione.',
    'description_site': 'aeternam — ricerca sulla teoria della simulazione',
    'travaux': 'Lavori',
    'langue': 'Lingua',
    'surtitre': 'Ricerca · Test n. 1',
    'meta': 'versione 2 · analisi secondaria riproducibile',
    'verdict': 'Verdetto a oggi: no. I test effettuati non rilevano alcuna firma di simulazione; vincolano alcuni modelli di spazio discreto, senza dire se l’Universo sia simulato.',
    'introuvable': 'Pagina non trovata.',
    'fichier_pdf': 'aeternam-test-1-it.pdf',
}

ARTICLE = {
    'titre': 'Un reticolo cubico alla prova di GRB 221009A',
    'description': 'Che cosa impongono i fotoni osservati da LHAASO al passo reticolare di uno spazio discreto, '
                   'e dove si ferma questo vincolo.',
    'date': '28 settembre 2026',
    'corps': r"""
<section class="resume">
<h2>In breve</h2>
<ul>
<li><strong>Se lo spazio fosse un reticolo cubico</strong> in cui la luce si propagasse come in una simulazione numerica delle equazioni di Maxwell, i fotoni più energetici arriverebbero in ritardo. Nel lampo di raggi gamma GRB&nbsp;221009A, LHAASO non osserva alcun ritardo di questo tipo.</li>
<li><strong>Il passo reticolare è quindi inferiore a [[a_resume]]&nbsp;m</strong>, per un reticolo cubico in tempo continuo, con il metodo più prudente e l’orientazione più sfavorevole, oppure a [[a_ml_resume]]&nbsp;m con il metodo di massima verosimiglianza. La scala di energia del reticolo supera [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>Non è una frontiera nuova.</strong> Beane, Davoudi e Savage avevano già ottenuto lo stesso ordine di grandezza nel 2012 (circa [[b_beane]]&nbsp;m) a partire dai raggi cosmici. Otteniamo un ordine di grandezza comparabile, con un’altra osservabile e altre ipotesi; i due limiti riguardano modelli diversi e non sono interscambiabili.</li>
<li><strong>Novità: il passo temporale conta.</strong> Se anche il tempo è suddiviso in passi, come in ogni simulazione numerica, l’effetto diminuisce. Con il passo massimo stabile, la luce non subisce più alcuna dispersione lungo le otto direzioni diagonali del cubo: un solo lampo non consente allora alcun limite universale. Per il 95&nbsp;% delle orientazioni, il passo reticolare resta inferiore a [[a95_sigma1]]&nbsp;m.</li>
<li><strong>Un reticolo il cui errore dominante fosse lineare</strong> in <em>a</em> è escluso fino a [[a_lineaire]]&nbsp;m, un decimo della lunghezza di Planck.</li>
<li><strong>Un passo reticolare pari alla lunghezza di Planck resta fuori portata</strong>: il suo effetto sarebbe circa [[facteur_planck]] volte troppo debole per questo test.</li>
<li><strong>Verificando la letteratura</strong>, abbiamo rilevato un’incoerenza di conversione in un articolo del 2025 (Xi e Shu): il loro limite quadratico sembra sovrastimato di un fattore [[xs_facteur]].</li>
<li><strong>Nessun rilevamento, nessuna stima della probabilità di essere simulati.</strong> Il test pone un limite a un’architettura precisa; non dice nulla sull’esistenza di un simulatore.</li>
</ul>
</section>

<h2 id="question">1. La domanda in esame</h2>
<p>Una simulazione numerica rappresenta lo spazio con un numero finito di punti. Un’onda che vi si propaga non si comporta esattamente come nel continuo: la sua velocità dipende leggermente dalla lunghezza d’onda. Per la luce, la velocità dipenderebbe quindi dall’energia dei fotoni. L’effetto è minuscolo, ma si accumula su distanze cosmologiche.</p>
<p>GRB&nbsp;221009A è il lampo di raggi gamma più brillante mai registrato. L’osservatorio LHAASO ne ha rilevato fotoni oltre i 10&nbsp;TeV, partiti circa due miliardi di anni fa (spostamento verso il rosso <em>z</em>&nbsp;=&nbsp;[[z]]). Se la velocità della luce dipendesse dall’energia, i fotoni di alta energia arriverebbero dopo quelli di bassa energia. La collaborazione LHAASO ha cercato questo ritardo e non l’ha trovato.</p>
<p>La domanda è quindi precisa: <em>quale passo reticolare è ancora compatibile con questo ritardo nullo?</em> Non presuppone né che ogni simulazione usi un reticolo, né che un reticolo costituisca la prova di una simulazione.</p>

<h2 id="modele">2. Il modello: Maxwell su un reticolo</h2>
<p>Si collocano i campi elettromagnetici su un reticolo cubico di passo <em>a</em>, esattamente come nello schema di Yee (1966) usato nelle simulazioni numeriche delle equazioni di Maxwell, o come nella formulazione hamiltoniana dell’elettrodinamica su reticolo (Kogut e Susskind, 1975). Il tempo scorre in modo continuo oppure a passi \(\Delta t\). Un’onda piana con vettore d’onda \(\mathbf k\) e pulsazione \(\omega\) obbedisce allora alla relazione di dispersione:</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>Lo schema è stabile solo se \(c\,\Delta t\le a/\sqrt{3}\). Si scrive quindi \(c\,\Delta t=\sigma a/\sqrt{3}\), con un numero di Courant \(0\le\sigma\le1\); \(\sigma=0\) corrisponde al tempo continuo. Per fotoni la cui lunghezza d’onda è molto maggiore del passo reticolare, la velocità di gruppo diventa, con \(E=\hbar\omega\):</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) dipende dalla direzione \(\mathbf n\) del fotone rispetto agli assi del reticolo: \(Q=1\) lungo un asse, \(Q=1/3\) lungo una diagonale del cubo. Per quanto segue contano tre proprietà:</p>
<ul>
<li>l’effetto è <strong>quadratico</strong>: un passo reticolare dieci volte più fine produce un effetto cento volte più debole;</li>
<li>i fotoni sono <strong>rallentati</strong>, mai accelerati, finché lo schema è stabile;</li>
<li>le due polarizzazioni si propagano allo stesso modo: <strong>nessuna birifrangenza</strong>, per cui i vincoli di polarizzazione, molto stringenti, qui non si applicano.</li>
</ul>

<h2 id="lhaaso">3. Il confronto con LHAASO</h2>
<p>LHAASO descrive un ritardo quadratico con \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) e pubblica intervalli su \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\), con \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV (equazioni 2, 3 e 5 dell’articolo). Identificando le due espressioni:</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>Il ritardo accumulato tra due fotoni di energie \(E_h\) e \(E_l\) si scrive</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>con la cosmologia di LHAASO (<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc, Ω<sub>m</sub>&nbsp;=&nbsp;[[om]], Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]), che dà <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s. La misura vincola soltanto la combinazione \(a\sqrt{Q_{\mathrm{eff}}}\). La tabella I di LHAASO riporta, al 95&nbsp;%:</p>
<div class="tableau"><table>
<thead><tr><th>Metodo</th><th>Limite inferiore</th><th>Miglior fit</th><th>Limite superiore</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML (calibrato)</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>Lo zero è compreso in tutti e tre gli intervalli: non viene rilevato alcun ritardo. I tre metodi analizzano lo stesso lampo; non li combiniamo. Un limite superiore \(U\) su \(\eta_2\) dà</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>In tempo continuo si ottiene:</p>
<div class="tableau"><table>
<thead><tr><th>Metodo</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\), orientazione più sfavorevole (m)</th><th>\(a\), 95&nbsp;% delle orientazioni (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML (calibrato)</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>Il riepilogo riporta il valore più prudente, [[a_resume]]&nbsp;m: è un inviluppo di presentazione, non un nuovo intervallo. A questo limite, un fotone da 1&nbsp;TeV arriverebbe al massimo [[retard_limite]]&nbsp;s dopo un fotone da [[e_bas]]&nbsp;TeV.</p>
<p>Alcune previsioni, che non sono misure (fotone da 1&nbsp;TeV confrontato con un fotone da [[e_bas]]&nbsp;TeV):</p>
<div class="tableau"><table>
<thead><tr><th>Passo reticolare</th><th>\(\eta_2\) previsto</th><th>Ritardo previsto</th><th>Verdetto</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>da [[p26_eta_min]] a [[p26_eta_max]]</td><td>da [[p26_ret_min]] a [[p26_ret_max]]&nbsp;s</td><td>escluso per qualsiasi orientazione</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>da [[p27_eta_min]] a [[p27_eta_max]]</td><td>da [[p27_ret_min]] a [[p27_ret_max]]&nbsp;s</td><td>escluso vicino agli assi (\(Q>\)&nbsp;[[q_cal_axe]]) dal solo metodo calibrato</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>da [[p28_eta_min]] a [[p28_eta_max]]</td><td>da [[p28_ret_min]] a [[p28_ret_max]]&nbsp;ms</td><td>non escluso</td></tr>
<tr><td>[[lpl]]&nbsp;m (Planck)</td><td>da [[pl_eta_min]] a [[pl_eta_max]]</td><td>da [[pl_ret_min]] a [[pl_ret_max]]&nbsp;s</td><td>fuori portata</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. Fin dove regge il limite</h2>
<h3>L’orientazione del reticolo</h3>
<p>Non sappiamo come sarebbe orientato il reticolo rispetto alla direzione del lampo. Il limite principale considera il caso meno favorevole, \(Q=1/3\). Su un milione di direzioni distribuite uniformemente, \(Q\) ha valore mediano [[q_mediane]] e supera [[q_5]] nel 95&nbsp;% dei casi: il limite cambia poco, con [[ccf_95]]&nbsp;m per il 95&nbsp;% delle orientazioni e [[ccf_mediane]]&nbsp;m per l’orientazione mediana. Queste frazioni sono geometriche: non sono probabilità riferite all’Universo.</p>
<h3>Il tempo discreto, punto debole del limite</h3>
<p>Una simulazione avanza per passi temporali. Discretizzare il tempo produce un errore di segno opposto, che compensa in parte quello della discretizzazione spaziale (il termine \(-\sigma^{2}/3\)). Per il metodo prudente:</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>Orientazione più sfavorevole</th><th>95&nbsp;% delle orientazioni</th><th>Orientazione mediana</th></tr></thead>
<tbody>
<tr><td>0 (tempo continuo)</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1 (passo massimo)</td><td>[[s4_cdt]]</td><td>nessun limite</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>Con il passo massimo stabile, la compensazione è esatta lungo le diagonali del cubo, e non solo al primo ordine: lungo di esse la relazione di dispersione restituisce \(\omega=ck\) per qualsiasi lunghezza d’onda. Una simulazione impostata così sfuggirebbe del tutto a questo test se il lampo cadesse lungo una delle sue otto direzioni diagonali. È la principale limitazione di un vincolo ricavato da una sola sorgente; più sorgenti in direzioni diverse la rimuoverebbero, perché, salvo coincidenze, non possono essere tutte allineate con delle diagonali.</p>
<h3>Un passo reticolare fisso o dilatato dall’espansione</h3>
<p>Assumiamo che il passo reticolare fisico sia fisso. Se il reticolo si dilatasse insieme all’Universo (passo comovente), l’effetto non crescerebbe più con lo spostamento verso il rosso e \(I_2\) sarebbe sostituito da \(I_0\): il limite si indebolisce di un fattore \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]], arrivando a [[comobile_a]]&nbsp;m. A <em>z</em>&nbsp;=&nbsp;[[z]], questa scelta conta poco.</p>
<h3>Schemi più precisi</h3>
<p>Un simulatore può impiegare uno schema di ordine superiore, il cui errore dominante varia come \(a^{4}\). L’effetto diventa allora quartico nell’energia, e il limite su \(a\) molto più debole. LHAASO non pubblica vincoli di questo tipo per questo lampo; ricavarne uno richiederebbe i dati fotone per fotone. Anche eventuali termini concepiti per compensare la dispersione sfuggirebbero al limite. Si tratta di altri modelli, da verificare separatamente.</p>
<h3>E se l’errore fosse lineare?</h3>
<p>Un reticolo simmetrico non produce alcun effetto lineare in \(a\). Una discretizzazione che lo producesse, rompendo la simmetria tra i due versi di propagazione, sarebbe soggetta al limite lineare di LHAASO, \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\): con un coefficiente di ordine uno, \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m, cioè un decimo della lunghezza di Planck. Qualsiasi reticolo di questo tipo con passo più grande è escluso.</p>
<h3>La validità del calcolo</h3>
<p>Lo sviluppo in serie presuppone \(aE/\hbar c\ll1\). In corrispondenza del limite, anche per fotoni da 20&nbsp;TeV, \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]. Abbiamo anche confrontato lo sviluppo con la relazione di dispersione esatta: per \(ak\)&nbsp;=&nbsp;[[ak_test]], lo scarto relativo non supera [[ecart_dispersion]], come previsto.</p>

<h2 id="contexte">5. Quanto vale, a confronto con i risultati esistenti</h2>
<p>Beane, Davoudi e Savage (2012) hanno studiato una simulazione di cromodinamica quantistica (QCD) su reticolo. Dal taglio nello spettro dei raggi cosmici ricavavano per l’inverso del passo reticolare il limite \(1/b\gtrsim10^{11}\)&nbsp;GeV, cioè \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m. Il nostro limite prudente vale [[beane_ratio]] volte il loro; i metodi di massima verosimiglianza di LHAASO danno da [[beane_ml_min]] a [[beane_ml_max]] volte il loro. I due limiti sono dello stesso ordine di grandezza, ma si basano su osservabili, particelle e modelli diversi: non si confermano a vicenda in senso stretto e non sono interscambiabili.</p>
<p>La lunghezza di Planck, [[lpl]]&nbsp;m, resta otto ordini di grandezza più in basso. Per un passo reticolare di queste dimensioni, l’effetto sarebbe [[facteur_planck_exact]] volte più debole del limite. Poiché cresce con il quadrato dell’energia, servirebbero fotoni circa cento milioni di volte più energetici, ben oltre tutto ciò che è stato osservato: a quest’ordine, nessun test sul tempo di volo può raggiungere un reticolo di Planck.</p>

<h2 id="xi-shu">6. Una verifica della letteratura: Xi e Shu (2025)</h2>
<p>Xi e Shu hanno analizzato lo stesso lampo con un altro metodo e riportano \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV (la loro tabella III), circa [[xs_rapport_lhaaso]] volte il limite di LHAASO. Ripartendo dalle loro stesse definizioni, non ritroviamo questo valore.</p>
<ul>
<li>Nella loro equazione (3) il ritardo va come \((E/E_{\mathrm{QG},n})^{n}\). Per \(n=1\), la loro conversione (6), \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\) con \(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]], è coerente: troviamo [[xs_c1]].</li>
<li>Per \(n=2\), la loro equazione (7), \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\) con \(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]], mantiene la forma in \(1/\theta\). Applicata al loro limite \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV², riproduce effettivamente la loro tabella ([[xs_eq7]]&nbsp;GeV). Ma, essendo il ritardo quadratico, la loro equazione (3) impone una dipendenza in \(1/\sqrt{\theta_2}\): \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\), cioè \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV.</li>
<li>Lo scarto è di un fattore [[xs_facteur]]. Spiegazione plausibile: \(\varepsilon^{2}\theta_2\) vale [[xs_eps2]], e [[xs_c2_imprime]] somiglia alla radice di [[xs_eps2_imprime]] estratta sulla sola potenza di dieci.</li>
</ul>
<p>Stato: incoerenza apparente nella versione 1 dell’articolo, da confermare con gli autori. Non rianalizziamo i loro dati e non giudichiamo i loro altri risultati. Una volta corretto, il loro limite resterebbe [[xs_vs_lhaaso]] volte più stringente di quello di LHAASO. Non lo utilizziamo.</p>

<h2 id="limites">7. Che cosa questo test non dice</h2>
<ul>
<li>Non rileva nulla: un ritardo nullo resta compatibile con tutte le misure.</li>
<li>Non calcola alcuna probabilità che ci troviamo in una simulazione; il «95&nbsp;%» riguarda un parametro fisico.</li>
<li>Pone un limite a un’architettura precisa: reticolo cubico, schema di Yee, passo fisso, senza compensazione.</li>
<li>Anche un ritardo rilevato non indicherebbe un computer: una fisica fondamentalmente discreta, o altri effetti di gravità quantistica, produrrebbero lo stesso segnale.</li>
<li>Gli intervalli di LHAASO si basano su ipotesi sull’emissione della sorgente; noi le ereditiamo.</li>
</ul>

<h2 id="suite">8. Prossimi passi</h2>
<ol>
<li>Combinare più sorgenti osservate in direzioni diverse, per eliminare l’angolo cieco delle diagonali.</li>
<li>Quantificare gli schemi di ordine superiore (effetto in \(a^{4}\)), il che richiede i dati fotone per fotone.</li>
<li>Chiedere a Xi e Shu di chiarire la loro conversione.</li>
<li>Estendere il test ad altre segnature di un reticolo: anisotropia dei raggi cosmici, particelle cariche.</li>
</ol>

<h2 id="reproduire">9. Riprodurre i risultati</h2>
<p>Tutto viene ricalcolato da uno script Python senza dipendenze, che verifica innanzitutto le proprie formule: sviluppo confrontato con la dispersione esatta, caso diagonale esatto, conversioni di andata e ritorno, integrale cosmologico, media di \(Q\) pari a 3/5.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>: lo script (Python&nbsp;3.10 o successivo, libreria standard; commenti del codice in francese)</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>: tutti i valori calcolati</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>: questa nota in PDF</li>
</ul>
<p>Una verifica incrociata indipendente (numpy, scipy) ritrova l’integrale cosmologico con una precisione di 10<sup>−15</sup>, i quantili di orientazione su dieci milioni di estrazioni casuali e la velocità di gruppo risolvendo numericamente la relazione di dispersione.</p>
<p>Questa nota sostituisce una prima versione del 28 settembre 2026. Aggiunge il tempo discreto, l’orientazione, il passo comovente, l’effetto lineare e il confronto con Beane et al.</p>

<h2 id="sources">Fonti</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a> (revisione del 13 febbraio 2026): equazioni 2, 3 e 5, tabella I.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a> (2025): equazioni 3, 6 e 7, tabelle I e III.</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302 (1966).</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395 (1975).</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House: dispersione numerica e stabilità dello schema di Yee.</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>: costanti fondamentali.</li>
</ol>
""",
}

ARTICLE_2 = {
    'titre': 'I raggi cosmici disegnano una griglia?',
    'description': 'Le particelle più energetiche mai registrate dall’Osservatorio Pierre Auger, '
                   'messe a confronto con l’impronta che una griglia cubica dovrebbe lasciare su di esse.',
    'date': '28 settembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdetto</h2>
<p><strong>No.</strong> Il test non rileva alcuno scostamento significativo dall’isotropia nelle direzioni dei [[n_evt]] raggi cosmici più energetici misurati dall’Osservatorio Pierre Auger: nel modello isotropo, il [[p4_pct]]&nbsp;% dei cieli simulati, sottoposti alla stessa ricerca, presenta un motivo cubico marcato almeno quanto quello osservato.</p>
<p>Questo «no» ha una portata limitata. Questo numero non è né la probabilità che il caso spieghi i dati, né quella che esista una griglia. Un motivo più debole non è escluso, e l’assenza di un motivo cubico osservabile non prova l’assenza di una griglia.</p>
</section>

<h2 id="explication">Spiegazione</h2>
<p>Se il nostro mondo fosse calcolato da un computer, lo spazio sarebbe forse suddiviso in cubetti minuscoli, come un’immagine è fatta di pixel. Nel 2012 tre fisici hanno osservato che una simile suddivisione lascerebbe un’impronta: le particelle più veloci dell’Universo non arriverebbero allo stesso modo da tutte le direzioni. Alcune direzioni sarebbero favorite, disposte come le facce o gli spigoli di un cubo.</p>
<p>Queste particelle esistono: sono i raggi cosmici, nuclei di atomi giunti dallo spazio con un’energia di gran lunga superiore a quella prodotta dai nostri acceleratori. In Argentina l’Osservatorio Pierre Auger li attende con un’immensa rete di rivelatori. Ha pubblicato l’elenco delle sue [[n_evt]] catture più energetiche, registrate tra il 2004 e il 2020, con la direzione da cui è arrivata ciascuna.</p>
<p>Abbiamo preso queste [[n_evt]] direzioni e cercato se si allineano lungo un cubo. Poiché nessuno sa come sarebbe ruotato questo cubo, ne abbiamo provate [[n_orient]] posizioni. La migliore si adatta un po’ ai dati. Ma quando si provano così tante posizioni, se ne trova sempre una che si adatta un po’, anche in un cielo dovuto al puro caso.</p>
<p>Per decidere, abbiamo costruito [[n_ciels]] cieli finti estratti a caso, visti dallo stesso osservatorio, e ripetuto esattamente la stessa ricerca su ciascuno. Nel [[p4_pct]]&nbsp;% di essi si trova un cubo che si adatta almeno altrettanto bene. Il cielo vero non si distingue quindi da questi cieli finti. Per parlare di un indizio, avrebbe dovuto fare meglio di quasi tutti i cieli finti.</p>
<p>Conclusione: non si rileva alcuna traccia di griglia. Ma questa ricerca poteva vedere solo un motivo forte: con appena [[n_evt]] particelle, uno tenue passerebbe inosservato. Inoltre i campi magnetici della nostra galassia deviano queste particelle lungo il percorso, il che confonderebbe parte del motivo. Questo test non dimostra dunque che lo spazio sia continuo; mostra che, là dove potevamo guardare, non c’è nulla.</p>

<h2 id="analyse">Analisi dettagliata</h2>

<h3>1. Dalla griglia a una previsione verificabile</h3>
<p>Su un reticolo cubico di passo \(a\), il laplaciano discreto sostituisce \(k^{2}\) con \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\). Per un campo libero,</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>dove \(\mathbf n\) è la direzione di propagazione negli assi del reticolo. È la stessa funzione \(Q\) del test n.&nbsp;1. Più in generale, qualsiasi effetto della griglia sulle direzioni di arrivo (propagazione, taglio dello spettro dipendente dalla direzione) è una funzione di \(\mathbf n\) invariante sotto il gruppo del cubo \(O_h\). Ora, le armoniche sferiche invarianti sotto \(O_h\) esistono solo per \(\ell=0,4,6,8,\dots\): la prima anisotropia permessa è l’armonica cubica \(\ell=4\), proporzionale a \(Q-3/5\). È il nostro test principale, fissato prima di aprire i dati; \(\ell=6\) è verificato in secondo luogo. Beane, Davoudi e Savage scrivono che la simulazione «potrebbe rivelarsi nelle distribuzioni dei raggi cosmici di più alta energia, con un grado di rottura della simmetria per rotazioni che riflette la struttura del reticolo sottostante».</p>

<h3>2. I dati</h3>
<p>Catalogo dell’Osservatorio Pierre Auger (ApJS 264, 50, 2023): i [[n_evt]] sciami di più alta energia registrati dal 1º gennaio 2004 al 31 dicembre 2020, da [[e_min]] a [[e_max]]&nbsp;EeV, con angoli zenitali fino a [[zmax]]°. Il file aperto contiene anche [[n_calib]] eventi ibridi di calibrazione, esterni ai [[n_evt]]: li scartiamo. Usiamo l’ascensione retta e la declinazione ricostruite dal rivelatore di superficie. L’impronta SHA-256 del file è verificata a ogni esecuzione. A queste energie l’efficienza di rivelazione è piena fino a [[zmax]]°, quindi l’esposizione è puramente geometrica.</p>

<h3>3. L’esposizione del rivelatore</h3>
<p>Un rivelatore a terra, alla latitudine \(a_0\)&nbsp;=&nbsp;[[lat]]°, che accetta zenit \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]°, ha un’esposizione uniforme in ascensione retta e, in declinazione \(\delta\) (Sommers, 2001):</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>Il cielo visibile termina a \(\delta\)&nbsp;=&nbsp;[[dec_max]]°, cioè il [[ciel_pct]]&nbsp;% della sfera. Un cielo isotropo visto da Auger non è quindi uniforme: tutto ciò che segue confronta i dati con quel cielo, non con una sfera uniforme.</p>

<h3>4. La statistica</h3>
<p>Sia \(R\) un’orientazione della griglia, con righe \(\mathbf e_k\), e \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). Per le \(N\) direzioni osservate:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>dove \(\langle\cdot\rangle_\omega\) è la media su un cielo isotropo pesato con l’esposizione. \(T>0\) segnala un eccesso lungo gli assi del cubo, \(T<0\) lungo le sue diagonali; il valore assoluto copre entrambi. Poiché \(f\) è un polinomio di grado 4, \(T(R)\) dipende dai dati solo attraverso i 15 momenti \(\sum_i\mathbf n_i^{\alpha}\); media e varianza sono calcolate esattamente con la quadratura di Gauss-Legendre. Il massimo percorre [[n_orient]] orientazioni estratte uniformemente (misura di Haar). Per \(\ell=6\) prendiamo \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\), con \(\alpha\)&nbsp;=&nbsp;[[alpha6]] (cioè \(-15/11\)), che la rende ortogonale a \(\ell=4\); il test combinato massimizza \(T_4^{2}+T_6^{2}\).</p>

<h3>5. Calibrare il caso</h3>
<p>Cercare la migliore tra [[n_orient]] orientazioni gonfia meccanicamente \(Z_4\): non segue una legge normale. Estraiamo quindi [[n_ciels]] cieli isotropi di \(N\) eventi secondo l’esposizione e applichiamo loro esattamente la stessa massimizzazione. Nell’ipotesi «nessuna griglia», \(Z_4\) ha mediana [[z4_50]]; supera [[z4_95]] nel 5&nbsp;% dei casi, [[z4_99]] nell’1&nbsp;% e [[z4_999]] nello 0,1&nbsp;%. Il valore p, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), include così il costo della scelta dell’orientazione.</p>

<h3>6. Risultato</h3>
<div class="tableau"><table>
<thead><tr><th>Test</th><th>Statistica osservata</th><th>Valore p</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (principale)</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\) e \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>Nell’orientazione migliore, la media di \(Q\) vale [[q_obs]] contro [[q_iso]] atteso, un eccesso del [[q_ecart_pct]]&nbsp;% verso gli assi. Non è significativo: \(p\)&nbsp;=&nbsp;[[p4]] per il test principale, e nessun test secondario scende sotto 0,05. I dati sono compatibili con l’assenza di qualsiasi simmetria cubica.</p>

<h3>7. Che cosa poteva vedere il test</h3>
<p>Per quantificare la sensibilità, si inietta un motivo cubico: densità proporzionale a \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Lungo un asse (\(Q=1\)), il flusso vale \(1+\varepsilon\) volte la media; lungo una diagonale (\(Q=1/3\)), vale \(1-2\varepsilon/3\) volte la media. Con \(\varepsilon>0\), l’eccesso riguarda quindi gli assi; con \(\varepsilon<0\), riguarda le diagonali e vale \(2\lvert\varepsilon\rvert/3\).</p>
<p>Il limite superiore al 95&nbsp;% dipende dalla convenzione sull’orientazione. Se l’orientazione della griglia viene estratta a caso per ogni cielo simulato ([[n_ciels_signal]] cieli per ampiezza), si ottiene un limite medio sulle orientazioni: \(\varepsilon\le\)&nbsp;[[eps_axes]] e \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]]. Una media non garantisce la copertura per ogni orientazione: rifacciamo quindi il calcolo a orientazione fissata, per [[n_orient_fixes]] orientazioni, tra cui la meno visibile da Auger ([[n_ciels_fixes]] cieli per ampiezza). Il limite varia allora da [[eps_axes_fix_min]] a [[eps_axes_fix]] verso gli assi e da [[eps_diag_fix_min]] a [[eps_diag_fix]] verso le diagonali; adottiamo il valore meno vincolante. Un eccesso di flusso fino a circa il [[exces_axes_pct]]&nbsp;% lungo gli assi, o il [[exces_diag_pct]]&nbsp;% lungo le diagonali, non è quindi escluso. È un vincolo debole, dovuto al piccolo numero di eventi, stabilito sulle orientazioni testate e non dimostrato per tutte.</p>
<p>Lo script verifica innanzitutto la propria catena: invarianza di \(Q\) sotto il gruppo del cubo, sviluppo polinomiale esatto, esposizione nulla oltre [[dec_max]]°, \(T\) centrato e ridotto sotto isotropia, ortogonalità di \(\ell=6\) rispetto a \(\ell=4\), e rivelazione di un motivo iniettato netto, di cui l’orientazione è ritrovata entro [[ecart_orient]]°.</p>

<h3>8. Limiti</h3>
<ul>
<li>I raggi cosmici sono carichi: i campi magnetici galattici ed extragalattici ne deviano le direzioni, tanto più quanto più i nuclei sono pesanti. Il motivo cercato è ampio (un asse e una diagonale distano [[angle_diag]]°) e resiste a deviazioni modeste, ma un’impronta fissata alla sorgente o durante la propagazione sarebbe in parte cancellata.</li>
<li>Supponiamo la griglia fissa rispetto alle stelle lontane (coordinate equatoriali). Una griglia in moto o in rotazione rispetto a esse richiederebbe un altro test.</li>
<li>[[n_evt]] eventi e il [[ciel_pct]]&nbsp;% del cielo: la potenza statistica è bassa, come mostra il limite sopra.</li>
<li>Anisotropie astrofisiche reali possono contenere una componente \(\ell=4\). Un risultato positivo avrebbe richiesto di escluderle; un risultato nullo non ne dipende.</li>
<li>Non si calcola alcuna probabilità di essere simulati: il test riguarda una firma precisa, quella di una griglia cubica.</li>
</ul>

<h3>9. Riprodurre</h3>
<p>Uno script Python (numpy) rifà tutto in pochi minuti: lettura e controllo dei dati, autotest, statistica, cieli simulati, limiti superiori. Il generatore casuale ha un seme fisso: i risultati sono identici da un’esecuzione all’altra.</p>
<p>Correzioni del 28 settembre 2026, dopo una rilettura: l’eccesso di flusso lungo le diagonali era stato confuso con il parametro \(\lvert\varepsilon\rvert\), mentre vale \(2\lvert\varepsilon\rvert/3\); è stato aggiunto il limite a orientazione fissata; il verdetto è stato riformulato per non presentare il valore p come una probabilità sulle ipotesi.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-2/analyse.py" download>analyse.py</a>: lo script</li>
<li><a href="/fichiers/test-2/resultats.json" download>resultats.json</a>: tutti i valori calcolati</li>
<li><a href="/fichiers/test-2/donnees/auger_catalogSD.csv" download>auger_catalogSD.csv</a>: i dati dell’Osservatorio Pierre Auger (licenza CC BY-SA 4.0)</li>
</ul>

<h2 id="sources">Fonti</h2>
<ol class="sources">
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Pierre Auger Collaboration, <cite>A Catalog of the Highest-Energy Cosmic Rays Recorded During Phase I of Operation of the Pierre Auger Observatory</cite>, ApJS 264, 50 (2023), <a href="https://arxiv.org/abs/2211.16020">arXiv:2211.16020</a>.</li>
<li>Pierre Auger Collaboration, <cite>Auger Open Data</cite>, release 3, <a href="https://doi.org/10.5281/zenodo.10488964">DOI 10.5281/zenodo.10488964</a>; efficienza di rivelazione: <a href="https://opendata.auger.org/data.php">opendata.auger.org</a>.</li>
<li>P. Sommers, <cite>Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory</cite>, Astroparticle Physics 14, 271 (2001), <a href="https://arxiv.org/abs/astro-ph/0004016">arXiv:astro-ph/0004016</a>.</li>
</ol>
""",
}

ARTICLE_3 = {
    'titre': 'La luce viaggia più lentamente in certe direzioni?',
    'description': 'Otto sorgenti di raggi gamma distribuite nel cielo, combinate per chiudere l’angolo cieco '
                   'del test n. 1 e limitare il passo di una griglia cubica qualunque sia la sua orientazione.',
    'date': '28 settembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdetto</h2>
<p><strong>No.</strong> Nessuna delle [[n_src]] sorgenti studiate mostra il ritardo che produrrebbe una griglia. Combinando le loro direzioni, è esclusa una griglia cubica di passo pari o superiore a [[a_exclue]]&nbsp;m, qualunque sia la sua orientazione e qualunque sia il suo passo temporale: l’angolo cieco del test n.&nbsp;1 è chiuso.</p>
</section>

<h2 id="explication">Spiegazione</h2>
<p>Se l’Universo fosse calcolato su una griglia, come un’immagine è fatta di pixel, la luce non vi avanzerebbe esattamente alla stessa velocità in tutte le direzioni. La luce più energetica accumulerebbe un lievissimo ritardo, più forte lungo gli spigoli della griglia che lungo le sue diagonali. Su miliardi di anni di viaggio, questo ritardo diventerebbe misurabile.</p>
<p>Il test n.&nbsp;1 cercava questo ritardo nel lampo di raggi gamma più brillante mai osservato, e non ha visto nulla. Restava però una scappatoia: se la simulazione avanza nel tempo con il passo più grande possibile, la luce non accumula più alcun ritardo lungo le diagonali della griglia. Una sola sorgente situata su una diagonale non permetteva allora alcuna conclusione.</p>
<p>Qui osserviamo [[n_src]] sorgenti insieme, in direzioni diverse del cielo: tre esplosioni di stelle lontane, quattro galassie con un buco nero molto attivo e la pulsar della Nebulosa del Granchio. Per ciascuna, un gruppo di astronomi ha già misurato che non compare alcun ritardo, fino a una certa finezza. Abbiamo riletto ogni articolo, riportato tutti i risultati alla stessa convenzione e poi cercato l’orientazione in cui una griglia potrebbe nascondersi meglio, quella che indebolisce di più il limite.</p>
<p>È impossibile mettere tutte le sorgenti su delle diagonali allo stesso tempo. Anche nell’orientazione più favorevole, tre sorgenti restano abbastanza lontane da una diagonale perché un ritardo avrebbe dovuto comparire. Una griglia le cui caselle misurano almeno [[a_exclue]]&nbsp;m è quindi esclusa in tutte le orientazioni. Questa dimensione resta circa [[planck_x]] volte più grande della lunghezza di Planck: una griglia molto più fine resta del tutto possibile.</p>

<h2 id="analyse">Analisi dettagliata</h2>

<h3>1. Il modello</h3>
<p>Come nel test n.&nbsp;1: equazioni di Maxwell su un reticolo cubico di passo \(a\) (schema di Yee), passo temporale \(c\,\Delta t=\sigma a/\sqrt{3}\) con \(0\le\sigma\le1\). All’ordine dominante,</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\,Q_{\mathrm{eff}}\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3},\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>Poiché \(1/3\le Q\le1\), si ha \(Q_{\mathrm{eff}}\ge0\): il fotone è sempre rallentato, e \(Q_{\mathrm{eff}}=0\) esattamente lungo le diagonali del cubo quando \(\sigma=1\). In corrispondenza del limite finale, \(aE/\hbar c\)&nbsp;=&nbsp;[[ae]] per un fotone da 20&nbsp;TeV: lo sviluppo è valido.</p>

<h3>2. Dai limiti pubblicati a un limite sul passo reticolare</h3>
<p>Gli otto articoli descrivono un ritardo quadratico con \(v/c\simeq1-\tfrac{3}{2}(E/E_{\mathrm{QG},2})^{2}\), con la distanza di Jacob e Piran \(K_2=\int_0^{z}(1+z')^{2}\,dz'/H(z')\). Identificando le due espressioni,</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}}\quad\Longrightarrow\quad a\sqrt{Q_{\mathrm{eff}}(\mathbf n_i)}\le B_i=\frac{\sqrt{12}\,\hbar c}{E_i}.$$
<p>Regola fissata in anticipo: limite al 95&nbsp;%, caso subluminale, tempo di volo, metodo meno vincolante di ciascun articolo. Ogni limite è riportato alla cosmologia di LHAASO tramite \(E_i\sqrt{K_2^{\mathrm{LHAASO}}(z_i)/K_2^{(i)}(z_i)}\); il fattore non supera [[fc_max]]. Ogni conversione pubblicata è rifatta a partire dai parametri stampati e ritrova il valore dell’articolo (autotest).</p>
<div class="tableau"><table>
<thead><tr><th>Sorgente</th><th>Strumento</th><th>\(z\) o distanza</th><th>\(E_{\mathrm{QG},2}\) pubblicato (GeV)</th><th>Cosmologia comune (GeV)</th><th>\(B_i\) (m)</th></tr></thead>
<tbody>
<tr><td>GRB 221009A</td><td>LHAASO</td><td>[[s0_z]]</td><td>[[s0_pub]]</td><td>[[s0_com]]</td><td>[[s0_b]]</td></tr>
<tr><td>GRB 190114C</td><td>MAGIC</td><td>[[s1_z]]</td><td>[[s1_pub]]</td><td>[[s1_com]]</td><td>[[s1_b]]</td></tr>
<tr><td>GRB 090510</td><td>Fermi-LAT</td><td>[[s2_z]]</td><td>[[s2_pub]]</td><td>[[s2_com]]</td><td>[[s2_b]]</td></tr>
<tr><td>Mrk 501</td><td>H.E.S.S.</td><td>[[s3_z]]</td><td>[[s3_pub]]</td><td>[[s3_com]]</td><td>[[s3_b]]</td></tr>
<tr><td>Mrk 421</td><td>MAGIC</td><td>[[s4_z]]</td><td>[[s4_pub]]</td><td>[[s4_com]]</td><td>[[s4_b]]</td></tr>
<tr><td>PKS 2155-304</td><td>H.E.S.S.</td><td>[[s5_z]]</td><td>[[s5_pub]]</td><td>[[s5_com]]</td><td>[[s5_b]]</td></tr>
<tr><td>PG 1553+113</td><td>H.E.S.S.</td><td>[[s6_z]]</td><td>[[s6_pub]]</td><td>[[s6_com]]</td><td>[[s6_b]]</td></tr>
<tr><td>Granchio (pulsar)</td><td>MAGIC</td><td>[[s7_z]]&nbsp;kpc</td><td>[[s7_pub]]</td><td>[[s7_com]]</td><td>[[s7_b]]</td></tr>
</tbody>
</table></div>

<h3>3. L’orientazione più sfavorevole</h3>
<p>Per un’orientazione \(R\) del reticolo, le sorgenti impongono insieme</p>
$$a\le A(R)=\min_i\frac{B_i}{\sqrt{Q_{\mathrm{eff}}(R\mathbf n_i)}},$$
<p>dato che una sorgente su una diagonale a \(\sigma=1\) non limita nulla. Si cerca \(\max_R A(R)\): [[n_orient]] rotazioni estratte uniformemente, orientazioni costruite (ogni sorgente posta su una diagonale e poi ruotata attorno a essa), quindi un raffinamento locale. Un secondo seme indipendente ritrova lo stesso massimo entro [[ecart_graines]]. L’ottimizzatore è validato su casi noti: una sorgente da sola non limita nulla a \(\sigma=1\), e due sorgenti separate dall’angolo tra due diagonali possono essere poste insieme su delle diagonali.</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>Orientazione più sfavorevole (m)</th><th>95&nbsp;% delle orientazioni (m)</th></tr></thead>
<tbody>
<tr><td>0</td><td>[[pire0]]</td><td>[[q95_0]]</td></tr>
<tr><td>0,5</td><td>[[pire05]]</td><td>[[q95_05]]</td></tr>
<tr><td>0,9</td><td>[[pire09]]</td><td>[[q95_09]]</td></tr>
<tr><td>1</td><td>[[pire1]]</td><td>[[q95_1]]</td></tr>
</tbody>
</table></div>
<p>Per \(\sigma<1\) nulla cambia rispetto al test n.&nbsp;1: domina GRB&nbsp;221009A, mentre le altre sorgenti sono da [[x_min]] a [[x_max]] volte meno sensibili. Tutto si decide a \(\sigma=1\): porre GRB&nbsp;221009A su una diagonale non basta più, perché le altre sorgenti vedono allora il reticolo di sbieco. Il compromesso peggiore allontana GRB&nbsp;221009A di [[ang_grb]]° dalla diagonale più vicina (\(Q_{\mathrm{eff}}\)&nbsp;=&nbsp;[[qeff_grb]]) ed equilibra [[n_actives]] vincoli: GRB&nbsp;221009A, GRB&nbsp;090510 e il Granchio. Il limite vale allora [[pire1]]&nbsp;m, cioè una scala \(\hbar c/a\ge\)&nbsp;[[echelle]]&nbsp;GeV. Poiché \(A(R)\) cresce con \(\sigma\) per ogni orientazione, il limite vale per ogni \(\sigma\le1\). A \(\sigma=1\), l’orientazione mediana dà [[med1]]&nbsp;m.</p>
<p>La chiusura non era scontata: GRB&nbsp;190114C e GRB&nbsp;090510 distano [[ang_190_090]]°, quasi l’angolo tra due diagonali ([[ang_diag]]°), e GRB&nbsp;090510 e PKS&nbsp;2155-304 sono a soli [[ang_090_pks]]° l’uno dall’altro. È la varietà del resto del cielo a chiudere l’angolo cieco.</p>

<h3>4. Robustezza</h3>
<p>Orientazione più sfavorevole a \(\sigma=1\), secondo le scelte:</p>
<ul>
<li>senza GRB&nbsp;221009A: [[v_sans_lhaaso]]&nbsp;m, l’angolo cieco resta chiuso;</li>
<li>limiti pubblicati senza conversione della cosmologia: [[v_sans_cosmo]]&nbsp;m;</li>
<li>Fermi con effetti propri della sorgente (tabella V dell’articolo): [[v_fermi]]&nbsp;m;</li>
<li>solo lampi di raggi gamma: [[v_sursauts]]&nbsp;m;</li>
<li>solo blazar e pulsar: [[v_blazars]]&nbsp;m.</li>
</ul>

<h3>5. Confronti</h3>
<p>Il limite valido per ogni orientazione e ogni passo temporale è [[x_test1]] volte meno stringente di quello del test n.&nbsp;1 in tempo continuo. Beane, Davoudi e Savage ottenevano \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m dal taglio nello spettro dei raggi cosmici; il nostro limite in tempo continuo vale [[x_beane0]] volte il loro, e il nostro limite universale [[x_beane]] volte.</p>

<h3>6. Limiti</h3>
<ul>
<li>Il limite combinato prende, per ogni orientazione, il più stringente dei limiti pubblicati al 95&nbsp;%, uno per uno: non è una verosimiglianza combinata, che gli articoli non pubblicano. Poiché nell’orientazione più sfavorevole sono attivi tre limiti, la copertura garantita è pari ad almeno [[couverture]]&nbsp;%, non a 95&nbsp;%.</li>
<li>Ogni articolo presuppone che nessuno sfasamento proprio della sorgente compensi o imiti il ritardo.</li>
<li>Gli spostamenti verso il rosso di Mrk&nbsp;421 e di PG&nbsp;1553+113 sono incerti; nessuna delle due sorgenti è attiva nell’orientazione più sfavorevole. La distanza della pulsar del Granchio, sorgente attiva, è inclusa nelle incertezze di MAGIC.</li>
<li>Uno schema di ordine superiore (errore in \(a^{4}\)), termini compensatori, un reticolo non cubico o dilatato dall’espansione sfuggono a questo limite.</li>
<li>Analisi secondaria: nessun fotone viene rianalizzato. Le frazioni di orientazioni sono geometriche, non probabilità riferite all’Universo.</li>
</ul>

<h3>7. Riprodurre</h3>
<p>Lo script rifà tutto in pochi secondi e verifica innanzitutto le proprie formule e ogni conversione pubblicata. Ogni dato in ingresso è citato, con pagina e tabella, in <code>sources.md</code>.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-3/analyse.py" download>analyse.py</a>: lo script</li>
<li><a href="/fichiers/test-3/resultats.json" download>resultats.json</a>: tutti i valori calcolati</li>
<li><a href="/fichiers/test-3/sources.md" download>sources.md</a>: le citazioni di ogni dato in ingresso</li>
</ul>

<h2 id="sources">Fonti</h2>
<ol class="sources">
<li>LHAASO Collaboration, GRB 221009A, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>, tabella I.</li>
<li>MAGIC Collaboration, GRB 190114C, <a href="https://arxiv.org/abs/2001.09728v4">arXiv:2001.09728v4</a>, tabella I.</li>
<li>Fermi-LAT Collaboration, GRB 090510, <a href="https://arxiv.org/abs/1305.3463v1">arXiv:1305.3463v1</a>, tabelle IV e V.</li>
<li>H.E.S.S. Collaboration, Mrk 501, <a href="https://arxiv.org/abs/1901.05209v1">arXiv:1901.05209v1</a>.</li>
<li>MAGIC Collaboration, Mrk 421, <a href="https://arxiv.org/abs/2406.07140v1">arXiv:2406.07140v1</a>, tabella 2.</li>
<li>H.E.S.S. Collaboration, PKS 2155-304, <a href="https://arxiv.org/abs/1101.3650v2">arXiv:1101.3650v2</a>.</li>
<li>H.E.S.S. Collaboration, PG 1553+113, <a href="https://arxiv.org/abs/1501.05087v1">arXiv:1501.05087v1</a>, tabella 5.</li>
<li>MAGIC Collaboration, pulsar del Granchio, <a href="https://arxiv.org/abs/1709.00346v1">arXiv:1709.00346v1</a>, tabella 6.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>.</li>
<li>Coordinate: <a href="https://simbad.cds.unistra.fr/simbad/">SIMBAD</a> (CDS, Strasburgo).</li>
</ol>
""",
}

ARTICLE_4 = {
    'titre': 'La casualità quantistica tradisce un programma?',
    'description': 'Milioni di bit tratti da esperimenti quantistici, passati al vaglio dei test che smascherano '
                   'i generatori pseudocasuali che userebbe una simulazione.',
    'date': '28 settembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdetto</h2>
<p><strong>No.</strong> Nei bit quantistici grezzi esaminati non compare alcuna firma di generatore pseudocasuale, mentre gli stessi test smascherano quattro generatori semplici usati come controlli. Un punto va chiarito subito: la regola fissata prima dell’analisi scatta sui dati IBM così come sono stati pubblicati, ma la causa è stata individuata — una delle nove macchine è rimasta bloccata su 0 o su 1 per intere serie — e questo difetto non ha la struttura di un generatore. La decisione di escludere questa macchina è stata presa dopo aver visto i dati; lo segnaliamo esplicitamente.</p>
<p>Questo «no» ha una portata limitata: esclude una simulazione che traesse le sue misure quantistiche da un generatore semplice, non una simulazione che usasse un generatore di qualità crittografica, indistinguibile per costruzione.</p>
</section>

<h2 id="explication">Spiegazione</h2>
<p>Se il mondo fosse una simulazione, bisognerebbe produrre il risultato di ogni misura quantistica, 0 o 1. La fisica dice che questo risultato è imprevedibile per natura. Un computer, invece, non sa produrre vera casualità: la fabbrica con una ricetta di calcolo. Una simulazione parsimoniosa userebbe una ricetta rapida e semplice, e le ricette semplici lasciano impronte: ripetizioni, regolarità nascoste, una struttura che il calcolo può riportare alla luce.</p>
<p>Abbiamo quindi preso sequenze di 0 e di 1 prodotte da veri esperimenti quantistici e pubblicate dai loro autori, e vi abbiamo cercato queste impronte. Prima difficoltà: la maggior parte delle fonti pubbliche di casualità quantistica fa passare i propri risultati attraverso un «frullatore» matematico prima di pubblicarli. Questo frullatore è progettato per cancellare ogni struttura; testarne l’uscita non dice nulla sulla sorgente. Abbiamo comunque testato questi dati, ma non contano ai fini del verdetto.</p>
<p>Restano due fonti di dati grezzi: un apparato a fotoni entangled dell’Università di Portland (Oregon), che pubblica i suoi bit così come escono, e nove computer quantistici di IBM a cui è stato chiesto milioni di volte di fare a testa o croce con un solo qubit. I fotoni superano tutti i test. Le macchine di IBM danno un po’ troppi zeri, un difetto noto e spiegato dagli autori dei dati; una volta corretto questo squilibrio, superano i test. Una di esse, Belem, è rimasta bloccata per intere serie di misure: un guasto, non una ricetta di calcolo.</p>
<p>I controlli si comportano come previsto: le ricette semplici vengono smascherate, compreso un generatore molto diffuso che pure supera la batteria ufficiale del NIST; le ricette sofisticate no, e nemmeno le cifre della radice quadrata di 2, benché siano perfettamente calcolabili. È questo il limite del test: una simulazione curata non lascerebbe alcuna traccia di questo tipo.</p>

<h2 id="analyse">Analisi dettagliata</h2>

<h3>1. Che cosa si può testare</h3>
<p>Un test statistico informa solo sull’ultimo trattamento subito da una sequenza di bit: un’uscita passata attraverso una funzione di hash crittografica somiglia alla casualità perfetta qualunque sia l’ingresso. Abbiamo testato [[bits_total]] bit, di cui [[bits_bruts]] grezzi:</p>
<div class="tableau"><table>
<thead><tr><th>Dataset</th><th>Origine</th><th>Trattamento</th><th>Bit</th></tr></thead>
<tbody>
<tr><td>parity</td><td>fotoni entangled in polarizzazione (Kavulich et al., 2021)</td><td>nessuno</td><td>[[n_parity]]</td></tr>
<tr><td>ibm</td><td>un qubit, porta di Hadamard, misura; nove macchine (Root e Becker, 2024)</td><td>nessuno</td><td>[[n_ibm]]</td></tr>
<tr><td>anu</td><td>fluttuazioni del vuoto, ANU</td><td>AES-128</td><td>[[n_anu]]</td></tr>
<tr><td>beacon</td><td>NIST Beacon 2.0</td><td>SHA-512</td><td>[[n_beacon]]</td></tr>
</tbody>
</table></div>
<p>Solo parity e ibm informano sulla natura della casualità quantistica. I dati grezzi del test di Bell senza scappatoie del NIST (2015) non sono stati utilizzati: le loro scelte di misura combinano sorgenti fisiche e una sorgente pseudocasuale, e i loro esiti di rivelazione non sono bit uniformi. Per il Beacon, la catena di impegni pubblicata è stata verificata su [[engagements]] coppie consecutive.</p>

<h3>2. Livello 1: la batteria NIST SP 800-22</h3>
<p>I 15 test della batteria ufficiale sono stati reimplementati e riproducono i [[annexe_n]] valori p dell’appendice B del documento con uno scarto massimo di [[annexe_ecart]] ([[annexe_ecart_chev]] per un test). I dati sono suddivisi in [[n_seq]] sequenze di 10<sup>6</sup> bit; i [[np1]] valori p formano un’unica famiglia, corretta secondo il metodo di Holm con un rischio globale dell’1&nbsp;%.</p>
<ul>
<li>parity: [[par_np1]] valori p, nessun rifiuto (minimo valore p aggiustato: [[par_p1]]); proporzione di bit pari a 1: [[par_frac]].</li>
<li>anu e beacon: nessun rifiuto (minimo valore p aggiustato per anu: [[anu_p1]]).</li>
<li>ibm: [[ibm_rej1]] rifiuti su [[ibm_np1]]; proporzione di bit pari a 1: [[ibm_frac]], cioè uno scarto di [[ibm_z]] deviazioni standard. Senza la macchina Belem, l’estrattore di von Neumann, che elimina esattamente un bias costante, lascia [[vn_bits]] bit e nessun rifiuto su [[vn_np]] valori p ([[vn_p]]): i fallimenti derivano dal bias descritto dagli autori.</li>
</ul>

<h3>3. Livello 2: le firme di un generatore</h3>
<p>La batteria NIST dice se una sequenza si discosta dalla casualità ideale, non perché. Tre test mirano ai difetti propri dei generatori algoritmici:</p>
<ul>
<li><strong>Complessità lineare.</strong> L’algoritmo di Berlekamp-Massey fornisce la lunghezza \(L\) del più corto registro a scorrimento a retroazione lineare che riproduce un segmento di \(n\) bit. Per una sequenza casuale, \(L\simeq n/2\); ogni generatore lineare su \(\mathrm{GF}(2)\) il cui stato abbia meno di \(n/2\) bit dà \(L\lt n/2\). Segmenti di [[seg_bm]] bit, letti in modo continuo oppure prendendo un bit ogni 48 e uno ogni 64: è coperto uno stato fino a [[etat_max]] bit.</li>
<li><strong>Ripetizioni.</strong> Ogni finestra di 64 bit è confrontata con tutte le altre; il numero atteso di coppie identiche è dell’ordine di [[rep_attendu]]. Una sola ripetizione segnalerebbe un periodo o un seme riutilizzato.</li>
<li><strong>Correlazioni a lungo raggio.</strong> Autocorrelazione ai ritardi da 17 a [[lag_max]], con correzione di Bonferroni.</li>
</ul>
<p>Famiglia principale, Holm all’1&nbsp;% su [[np2]] valori p: parity non rifiuta nulla ([[par_p2]]); il suo scarto massimo di \(L\) da \(n/2\) è [[par_ecart_l]]; nessuna ripetizione; correlazioni a lungo raggio: [[par_auto]]. anu e beacon non rifiutano nulla. ibm rifiuta [[ibm_rej2]] volte.</p>

<h3>4. I rifiuti di IBM: una macchina bloccata</h3>
<p>I dati IBM sono costituiti da [[ibm_essais]] prove di 8&nbsp;192 lanci ciascuna. Di queste, [[ibm_const]] sono costanti ([[ibm_const0]] interamente a 0, [[ibm_const1]] interamente a 1) e altre [[ibm_quasi]] lo sono per oltre il 99&nbsp;%; tutte provengono dalla macchina Belem. Le [[ibm_paires]] coppie di finestre identiche sono tutte sequenze di bit uguali: tra le finestre di composizione ordinaria ce ne sono [[ibm_paires_typ]]. Un’uscita congelata non è l’uscita di un generatore pseudocasuale: è l’assenza di uscita.</p>
<p>La decisione di escludere Belem è stata presa dopo aver visto i dati: si tratta quindi di un’analisi secondaria, con una propria correzione di Holm, e il risultato della regola iniziale resta pubblicato. Sulle altre otto macchine ([[sb_bits]] bit) il livello 2 non rifiuta nulla ([[sb_np2]] valori p, minimo valore p aggiustato [[sb_p2]]); lo scarto massimo di \(L\) da \(n/2\) è [[sb_ecart_l]] e non c’è alcuna ripetizione. Esiste una correlazione al ritardo 1 ([[sb_r1]], cioè [[sb_z1]] deviazioni standard): un difetto di misura a corto raggio, senza rapporto con la struttura di un generatore. Su queste macchine il livello 1 dà [[sb_rej1]] rifiuti su [[sb_np1]], a causa del bias.</p>

<h3>5. I controlli</h3>
<p>La stessa catena è applicata a [[bits_ctrl]] bit di ciascun generatore noto; lo script si arresta se un controllo non si comporta come previsto.</p>
<div class="tableau"><table>
<thead><tr><th>Generatore</th><th>Atteso</th><th>Risultato (minimi valori p aggiustati, livelli 1 e 2)</th></tr></thead>
<tbody>
<tr><td>LFSR di grado 20</td><td>rilevato</td><td>rilevato: \(L\)&nbsp;=&nbsp;[[l20_lmin]], ripetizioni</td></tr>
<tr><td>LFSR di grado 31</td><td>rilevato</td><td>rilevato: \(L\)&nbsp;=&nbsp;[[l31_lmin]], \(\log_{10}p\)&nbsp;=&nbsp;[[l31_log10p]]</td></tr>
<tr><td>LCG a 32 bit</td><td>rilevato</td><td>rilevato: test spettrale, correlazioni a lungo raggio</td></tr>
<tr><td>Mersenne Twister</td><td>rilevato</td><td>rilevato solo dal livello 2: \(L\)&nbsp;=&nbsp;[[mt_lmin]], \(\log_{10}p\)&nbsp;=&nbsp;[[mt_log10p]]; batteria NIST muta ([[mt_p1]])</td></tr>
<tr><td>PCG64</td><td>non rilevato</td><td>nulla ([[pcg_p1]]; [[pcg_p2]])</td></tr>
<tr><td>SHA-256 in modalità contatore</td><td>non rilevato</td><td>nulla ([[sha_p1]]; [[sha_p2]])</td></tr>
<tr><td>Cifre binarie di \(\sqrt{2}\)</td><td>non rilevato</td><td>nulla ([[r2_p1]]; [[r2_p2]])</td></tr>
</tbody>
</table></div>
<p>Il Mersenne Twister mostra che il livello 2 aggiunge una sensibilità reale alla batteria ufficiale. PCG64, SHA-256 e \(\sqrt{2}\) mostrano che una sequenza interamente deterministica può non avere alcuna firma rilevabile.</p>

<h3>6. Limiti</h3>
<ul>
<li>Un generatore di qualità crittografica è indistinguibile: questo test esclude una simulazione che usasse un generatore semplice, non una simulazione curata. Lo dice lo stesso documento SP 800-22: nessun insieme di test sostituisce la crittoanalisi.</li>
<li>Copertura del livello 2: un generatore lineare è rilevato solo se il suo stato ha meno di [[etat_max]] bit; una ripetizione, solo se il periodo è più corto dei dati.</li>
<li>Volume modesto di dati grezzi, e nessuna delle due fonti grezze è certificata da un test di Bell senza scappatoie.</li>
<li>L’esclusione della macchina Belem è una decisione a posteriori; la sua causa è documentata e il risultato grezzo pubblicato.</li>
<li>I dataset ANU e Beacon misurano solo la qualità di AES-128 e di SHA-512.</li>
</ul>

<h3>7. Riprodurre</h3>
<p>I dati vengono ricostruiti da <code>telecharger.py</code>, che ne verifica le impronte; <code>analyse.py</code> gira poi senza rete in meno di due minuti, autotest compresi.</p>
<pre><code>python3 telecharger.py
python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-4/analyse.py" download>analyse.py</a>: l’analisi</li>
<li><a href="/fichiers/test-4/telecharger.py" download>telecharger.py</a>: il download verificato dei dati</li>
<li><a href="/fichiers/test-4/resultats.json" download>resultats.json</a>: tutti i valori calcolati</li>
<li><a href="/fichiers/test-4/sources.md" download>sources.md</a>: le citazioni di ogni affermazione</li>
</ul>

<h2 id="sources">Fonti</h2>
<ol class="sources">
<li>J. T. Kavulich, B. P. Van Deren, M. Schlosshauer, <cite>Searching for evidence of algorithmic randomness and incomputability in the output of quantum random number generators</cite>, Physics Letters A 388, 127032 (2021), <a href="https://arxiv.org/abs/2101.01238">arXiv:2101.01238</a>; dati: <a href="https://zenodo.org/records/4440318">Zenodo 4440318</a>.</li>
<li>B. P. Van Deren, J. T. Kavulich, M. Schlosshauer, <cite>Parity-based, bias-free optical quantum random number generation with min-entropy estimation</cite>, <a href="https://arxiv.org/abs/2006.11425">arXiv:2006.11425</a>.</li>
<li>O. Root, M. Becker, <cite>Does True Randomness Exist? Efficacy Testing IBM Quantum Computers via Statistical Randomness</cite>, <a href="https://arxiv.org/abs/2401.12250">arXiv:2401.12250</a>; dati: <a href="https://doi.org/10.5281/zenodo.10542216">DOI 10.5281/zenodo.10542216</a>.</li>
<li>J. Y. Haw et al., <cite>Maximization of Extractable Randomness in a Quantum Random-Number Generator</cite>, <a href="https://arxiv.org/abs/1411.4512">arXiv:1411.4512</a>.</li>
<li>NIST, <cite>A Reference for Randomness Beacons: Format and Protocol Version 2</cite>, <a href="https://csrc.nist.gov/pubs/ir/8213/ipd">NISTIR 8213</a>.</li>
<li>L. K. Shalm et al., <cite>A strong loophole-free test of local realism</cite>, <a href="https://arxiv.org/abs/1511.03189">arXiv:1511.03189</a>.</li>
<li>NIST, <cite>A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications</cite>, <a href="https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final">SP 800-22 Rev. 1a</a>.</li>
</ol>
""",
}
