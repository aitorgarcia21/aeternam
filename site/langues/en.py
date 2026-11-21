"""English: the translation of site/langues/fr.py, with the same structure.

Every [[marker]], HTML tag and formula is the same as in the French source; the build
(site/generer.py) checks it and stops on any difference. Raw strings (r\"\"\"…\"\"\") are
required because of the backslashes.
"""
NOM = 'English'
HTML_LANG = 'en'
HREFLANG = 'en'
DIR = 'ltr'
LOCALE_OG = 'en_US'
DECIMALE = '.'
MILLIERS = ','
PREFIXE = '/en'       # the English edition is served under /en/, with the same page addresses

MOIS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December')

UI = {
    'description_site': 'Can we live forever? What we measure of aging, what remains to be found, and a blog for the curious: '
                        'memory, the brain, vision, dreams, time and simulation.',
    'introuvable': 'Page not found.',
    'retour_accueil': 'Back to the home page',
    # Navigation: the pill at the top, repeated in the footer.
    'nav': (('/recherche/', 'Research'), ('/recherches/', 'Blog'), ('/ecrire/', 'Write'), ('/a-propos/', 'About')),
    'nav_principale': 'Main navigation',
    'nav_fin': 'Footer navigation',
    'accueil_label': 'ÆTERNAM, home',
    'aller_contenu': 'Skip to content',
    'en_haut': 'Back to top',
    'version': 'English version',
    'ecrit_en': {'fr': 'in French', 'en': 'in English'},
    'licence_pied': ('Texts, figures and results are licensed under <a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener">CC BY 4.0</a>. '
                     'Code is licensed under <a href="https://github.com/aitorgarcia21/aeternam/blob/main/LICENSE-CODE" rel="noopener">MIT</a>. '
                     '<a href="https://github.com/aitorgarcia21/aeternam" rel="noopener">Everything is public.</a>'),
    'adresse_licence': 'https://creativecommons.org/licenses/by/4.0/',
    # Articles
    'dans_article': 'In this article',
    'poursuivre': 'Keep reading',
    'lire_ensuite': 'Read next',
    'tous_articles': 'The whole blog',
    'toute_recherche': 'Where the research stands',
    'tous_themes': 'All topics',
    'ecrire_article': 'Write an article',
    # The blog
    'recherches_titre': 'The blog — ÆTERNAM',
    'recherches_h1': 'The blog',
    'recherches_intro': 'For the curious: memory, the brain, vision, dreams, time, black holes, simulation. Questions with no direct link to '
                        'our research on aging, treated with the same rigor: every number has a source, every calculation can be rerun. '
                        'The research itself has its own page: <a href="/recherche/">where we stand</a>.',
    'recherches_description': 'The ÆTERNAM blog, for the curious: memory, the brain, vision, dreams, time, black holes and simulation, with the community’s articles.',
    'aller_theme': 'Jump to a topic',
    'sujets_titre': 'Research topics — ÆTERNAM',
    'sujets_h1': 'Research topics',
    'sujets_intro': 'Seven topics, seven questions about a life that lasts. An article can touch more than one.',
    'sujet_source': 'Read the study',
    'sujet_questions': 'The questions',
    'sujet_commencer': 'Where to start',
    'sujet_articles': 'Articles on this topic',
    # Community articles
    'signes_titre': 'Community articles',
    'signes_description': 'Written by readers, signed with their name and reviewed in public before they appear. Anyone can submit one.',
    'signes_aucun': 'No community articles yet.',
    'signes_premier': 'The first one could be yours.',
    'signe_par': 'By {auteur}, {date}',
    'signe_defaut': 'An article by {auteur}, submitted to ÆTERNAM and reviewed in public.',
    'signature': ('<p>By <strong>{auteur}</strong>{orcid}, {date}.</p>'
                  '<p>Submitted to ÆTERNAM and reviewed in public before publication. The text is licensed under '
                  '<a href="{adresse_licence}" rel="noopener">{licence}</a>: anyone may reuse it with credit to its author.</p>'),
    'signature_liens': ('Version history', 'Suggest a correction'),
    # The line drawings (site/dessins.py): what each one shows, for those who cannot see it.
    'dessins': {
        'vieillir': 'Two lines: the risk of dying, rising faster and faster with age, and a line that stays flat.',
        'pente_age': 'age', 'pente_risque': 'risk of dying',
        'vieillir_risque': 'risk of dying', 'vieillir_sans': 'without aging',
        'scene': 'Diagram: the risk of dying rises faster and faster with age; without that rise, it would stay flat, as in hydra; a cell and what gets damaged in it; the biological age of cells going back down early in the embryo, and four factors that bring an adult cell back down; delaying pushes the curve back, slowing softens its slope; two drops of blood, one younger; two blood draws per mouse, at 16 and 28 months, the last still unknown in those that eat less; the same blood test in mice and in humans.',
        'humain_souris': 'mouse', 'humain_humain': 'human', 'humain_mesure': 'same blood test',
        'scene_dix': '10 years', 'scene_plat': 'without the rise',
        'cellule_adn': 'DNA', 'cellule_proteines': 'proteins', 'cellule_mito': 'mitochondrion',
        'embryon_age': 'biological age of cells', 'embryon_temps': 'time', 'embryon_zero': 'reset', 'embryon_facteurs': 'four factors',
        'scene_humain': 'human', 'scene_hydre': 'hydra', 'scene_retarder': 'delay', 'scene_ralentir': 'slow down',
        'sang_volonte': 'fed freely', 'sang_restriction': 'eats less', 'sang_naif': 'naive T', 'sang_memoire': 'memory T',
        'exp_mois': '{} months',
        'relativite': 'A black hole ringed by its disk, two bent rays of light and two clocks: the closer one ticks more slowly.',
        'vision': 'An eye whose pupil is a grid of dots; some light up and draw the letter E.',
        'memoire': 'A network of neurons; five of them, in gold, fire again together.',
        'reve': 'A crescent moon above the trace of one night: the REM phases, in gold, grow longer toward morning.',
        'bci': 'A head seen from above with eight electrodes over the motor cortex, and drawn EEG traces.',
        'simulation': 'A cubic grid; from the same point, one ray follows an edge and another a diagonal.',
        'eveil': 'Awake', 'paradoxal': 'REM',
    },
}

# ---------------------------------------------------------------- the home page
# One subject, immortality, then an open research blog. The subject is asked as a question,
# never stated as a description of the site, and no small label sits above a heading.
ACCUEIL = {
    'titre_page': 'ÆTERNAM — can we live forever?',
    'description': 'Can we live forever? Aging plays out in our cells. Our measurements, mouse by mouse: the known molecules delay aging, caloric restriction slows it. The experiment that remains to be funded: knowing whether it slows the aging of cells.',
    'question': 'Can we live forever?',
    'defiler': 'Scroll',
    # Five steps, one per screen, each with its diagram (scene in site/dessins.py): the risk curve
    # climbs, hydra stays flat, delaying pushes the curve back, slowing softens its slope, the
    # blood of restricted mice stays younger. One sentence, then what proves it.
    'recit_label': 'What is known',
    'temps': (
        {'phrase': 'Aging is a risk of dying that rises faster and faster.', 'texte': 'In adults, it doubles <a href="https://doi.org/10.1126/science.2392680" rel="noopener">about every 8 years</a>.'},
        {'phrase': 'Without that rise, we would live for millennia.', 'texte': 'At age 10, the risk of dying is about <a href="https://www.ssa.gov/oact/STATS/table4c6.html" rel="noopener">1 in 10,000 per year</a>. If it stayed at that level for life, one person in two would live more than 5,000 years.'},
        {'phrase': 'It is not a law of nature.', 'texte': 'Among 2,256 hydra followed for eight years in the laboratory, the risk of dying <a href="https://doi.org/10.1073/pnas.1521002112" rel="noopener">did not rise with age</a>.'},
        {'phrase': 'Aging plays out in our cells.', 'texte': 'Most of the <a href="https://doi.org/10.1016/j.cell.2022.11.001" rel="noopener">twelve hallmarks of aging</a> play out inside cells: DNA gets damaged there, and mitochondria, which provide energy, weaken.'},
        {'phrase': 'And a cell can grow young again.', 'texte': 'A baby is born young to parents who no longer are: early in every embryo, <a href="https://doi.org/10.1126/sciadv.abg6082" rel="noopener">the biological age of cells goes back down</a>.'},
        {'phrase': 'Four factors redo what the embryo does.', 'texte': 'They <a href="https://doi.org/10.1016/j.cell.2006.07.024" rel="noopener">take an adult cell back to the embryonic state</a>, and three of them have <a href="https://doi.org/10.1038/s41586-020-2975-4" rel="noopener">restored sight to old mice</a>; pushed too far, <a href="https://doi.org/10.1038/nature12586" rel="noopener">they cause tumors</a>.'},
        {'phrase': 'In mice, treatments that extend life delay aging without slowing it.', 'texte': 'Across [[rr_souris]] mice, the [[rr_efficaces]] treatments of this kind push the curve back, but <a href="/retarder-ou-ralentir/">none softens its slope</a> in an established way.'},
        {'phrase': 'Eating less slows aging.', 'texte': 'In [[rs_souris]] mice, eating 40% less <a href="/restriction/">multiplies by [[rs_l40]]</a> the time it takes the risk to double. In humans, two years of eating less slowed by 2 to 3% <a href="https://doi.org/10.1038/s43587-022-00357-y" rel="noopener">a pace of aging read in the blood</a>.'},
        {'phrase': 'In mice that eat less, the blood stays younger.', 'texte': 'With age, naive T lymphocytes, white blood cells that have never yet been used, give way to memory T lymphocytes. In these mice, <a href="/cellules-du-sang/">naive cells remain more numerous</a>.'},
        {'phrase': 'Two blood draws per mouse will tell whether their blood ages more slowly.', 'texte': 'About [[cs_r_cd8m_n90]] mice, measured at 16 and then 28 months: in those that eat less, will memory T lymphocytes take the place of naive ones more slowly? <a href="/cellules-du-sang/#rythme">The protocol</a> writes in advance what would prove us wrong.'},
        {'phrase': 'If their blood ages more slowly, we will know what to copy.', 'texte': 'It will remain to obtain this effect without dieting, and the same blood test will check it in humans. This is the experiment to fund.'},
    ),
    # The call, last step of the scene: the cry, then what we ask; the address follows.
    'cri': 'We will find a way.',
    'appel_texte': 'What we find will belong to everyone. To fund this experiment or challenge our calculations, write to us.',
    'appel_objet': 'Contact',
}

# ---------------------------------------------------------------- the research
# Where ÆTERNAM's research on immortality stands: the thesis, then each step with its status.
# Same structure as the French. Each step: (title, text, link, status).
RECHERCHE = {
    'titre': 'Where we stand — ÆTERNAM',
    'description': 'ÆTERNAM’s research on aging: what is measured, what is ready to be funded, what remains to be done.',
    'h1': 'Where we stand',
    'intro': (
        'We will find how to stop aging. Our thesis: aging plays out in the cells. We must first learn to slow it, then to repair it, rather than replace worn-out organs.',
        'The common criterion of our studies is the time the risk of dying takes to double. A treatment that lengthens it slows aging; a treatment that only shifts the curve delays it. Every number has a source, every calculation can be rerun.',
    ),
    'groupes': (
        ('mesure', 'What we have measured', 'On public data, mouse by mouse.', (
            ('Restriction keeps the blood young', 'Of [[cs_mesures]] blood measures, [[cs_cand_cal]] change under restriction and predict survival within each diet: more red cells and naive T cells, fewer myeloid cells. They explain the shift of the risk, not yet its slope.', '/cellules-du-sang/', 'Measured on November 21, 2026, plan recorded before the calculation'),
            ('Caloric restriction slows aging', 'In [[rs_souris]] mice, 40% restriction multiplies the doubling time of the risk by [[rs_l40]] ([[rs_l40_bas]] to [[rs_l40_haut]]); 20%, by [[rs_l20]]. Fasting one or two days a week does not change the slope.', '/restriction/', 'Measured on November 21, 2026'),
            ('The known molecules delay, without slowing', 'In [[rr_souris]] mice, [[rr_efficaces]] treatments extend life. Their doubling time averages [[rr_lambda]] times that of controls, [[rf_lambda]] when each mouse’s frailty is taken into account: no slowing established.', '/retarder-ou-ralentir/', 'Measured on November 20, 2026, checked on the 21st'),
        )),
        ('financer', 'What is ready and awaits funding', 'Hypothesis written beforehand, sample sizes calculated, the result that would refute it.', (
            ('Measure the slowing in humans', '[[rs_n_total]] people aged 40 to 65, three years of 20% restriction or of their usual diet. Criterion: the pace of aging read in the blood, which slowed by 2 to 3% over two years in the only published trial.', '/restriction/#essai', 'Protocol written on November 21, 2026'),
            ('Delay and slow at once', 'Restriction and rapamycin in mice, with the slope as the primary criterion: [[rs_n450]] mice per group to see it.', '/combinaisons/#revision', 'Protocol revised on November 21, 2026'),
            ('Read a memory from a preserved brain', 'The fallback, if the body gives out first: a pilot step, then [[lc_n80_90]] brains read blind.', '/lecture-cerveau/#pilote', 'Protocol written; pilot step added on November 21, 2026'),
        )),
        ('a-faire', 'What remains to be done', 'The next steps, in order.', (
            ('Follow T cells over time', 'In mice fed at will, naive T cells recede with age; restriction slows this decline, without proof at this size. About [[cs_r_cd8m_n90]] mice measured twice are needed, or more frequent measurements.', '/cellules-du-sang/#rythme', 'Protocol written on November 21, 2026'),
            ('Reset cells without tumors', 'Taking cells back toward the embryonic state rejuvenates mouse tissues, but pushed too far, it causes tumors. The lead remains to be written, with the same criterion: the slope.', '/vieillir/#zero', 'To be written'),
        )),
        ('comprendre', 'To understand', 'The thread of all the research.', (
            ('Why do we age?', 'What is known about aging, from the life table to cells that reset themselves.', '/vieillir/', 'Background article'),
        )),
    ),
}

# ---------------------------------------------------------------- the articles
ARTICLE = {
    'titre': 'A cubic grid confronted with GRB 221009A',
    'description': 'What the photons observed by LHAASO impose on the spacing of a discrete space, '
                   'and where this constraint stops.',
    'date': 'September 28, 2026',
    'corps': r"""
<section class="resume">
<h2>In brief</h2>
<ul>
<li><strong>If space were a cubic grid</strong> on which light propagates as in a numerical simulation of Maxwell’s equations, the most energetic photons would arrive late. In the burst GRB&nbsp;221009A, LHAASO observes no delay of this kind.</li>
<li><strong>The grid spacing is therefore below [[a_resume]]&nbsp;m</strong>, for a cubic grid in continuous time, with the most conservative method and the least favorable orientation, or below [[a_ml_resume]]&nbsp;m with the likelihood method. The energy scale of the grid exceeds [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>This is not a new frontier.</strong> Beane, Davoudi and Savage already obtained the same order of magnitude in 2012 (about [[b_beane]]&nbsp;m) from cosmic rays. We obtain a comparable order of magnitude, with another observable and other assumptions; the two bounds apply to different models and are not interchangeable.</li>
<li><strong>New: the time step matters.</strong> If time is also discretized, as in any numerical simulation, the effect decreases. At the maximum stable step, light no longer undergoes any dispersion along the eight diagonal directions of the cube: a single burst then allows no universal bound. For 95% of orientations, the spacing remains below [[a95_sigma1]]&nbsp;m.</li>
<li><strong>A grid whose dominant error is linear</strong> in <em>a</em> is excluded down to [[a_lineaire]]&nbsp;m, one tenth of the Planck length.</li>
<li><strong>A Planck-sized spacing remains out of reach</strong>: its effect would be about [[facteur_planck]] times too weak for this test.</li>
<li><strong>While checking the literature</strong>, we found a conversion inconsistency in a 2025 paper (Xi and Shu): their quadratic bound appears to be overestimated by a factor of [[xs_facteur]].</li>
<li><strong>No detection, no probability of being simulated.</strong> The test bounds a specific architecture; it says nothing about the existence of a simulator.</li>
</ul>
</section>

<h2 id="question">1. The question tested</h2>
<p>A numerical simulation represents space by a finite number of points. A wave propagating on it does not behave exactly as in the continuum: its speed depends slightly on its wavelength. For light, the speed would therefore depend on the energy of the photons. The effect is tiny, but it accumulates over cosmological distances.</p>
<p>GRB&nbsp;221009A is the brightest gamma-ray burst ever recorded. The LHAASO observatory detected photons from it above 10&nbsp;TeV, emitted about two billion years ago (redshift <em>z</em>&nbsp;=&nbsp;[[z]]). If the speed of light depended on energy, the high-energy photons would arrive after the low-energy ones. The LHAASO collaboration searched for this delay and did not find it.</p>
<p>The question is therefore precise: <em>what grid spacing does this null delay still allow?</em> It assumes neither that every simulation would use a grid, nor that a grid would prove a simulation.</p>

<h2 id="modele">2. The model: Maxwell on a grid</h2>
<p>The electromagnetic fields are placed on a cubic lattice of spacing <em>a</em>, exactly as in the Yee scheme (1966) used by numerical simulations of Maxwell’s equations, or as in the Hamiltonian formulation of lattice electrodynamics (Kogut and Susskind, 1975). Time flows either continuously or in steps \(\Delta t\). A plane wave with wave vector \(\mathbf k\) and angular frequency \(\omega\) then obeys the dispersion relation:</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>The scheme is stable only if \(c\,\Delta t\le a/\sqrt{3}\). We therefore write \(c\,\Delta t=\sigma a/\sqrt{3}\), with a Courant number \(0\le\sigma\le1\); \(\sigma=0\) corresponds to continuous time. For photons whose wavelength is very large compared with the spacing, the group velocity becomes, with \(E=\hbar\omega\):</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) depends on the direction \(\mathbf n\) of the photon relative to the grid axes: \(Q=1\) along an axis, \(Q=1/3\) along a main diagonal. Three properties matter for what follows:</p>
<ul>
<li>the effect is <strong>quadratic</strong>: a spacing ten times finer produces an effect a hundred times weaker;</li>
<li>photons are <strong>slowed down</strong>, never sped up, as long as the scheme is stable;</li>
<li>both polarisations propagate in the same way: <strong>no birefringence</strong>, so the polarization constraints, which are very strong, do not apply here.</li>
</ul>

<h2 id="lhaaso">3. Confrontation with LHAASO</h2>
<p>LHAASO describes a quadratic delay by \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) and publishes intervals on \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\), with \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV (equations 2, 3 and 5 of the paper). By identification:</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>The delay accumulated between two photons of energies \(E_h\) and \(E_l\) is</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>with the LHAASO cosmology (<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc, Ω<sub>m</sub>&nbsp;=&nbsp;[[om]], Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]), which gives <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s. The measurement constrains only the combination \(a\sqrt{Q_{\mathrm{eff}}}\). Table I of LHAASO gives, at 95%:</p>
<div class="tableau"><table>
<thead><tr><th>Method</th><th>Lower limit</th><th>Best fit</th><th>Upper limit</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML (calibrated)</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>Zero lies within all three intervals: no delay is detected. The three methods analyze the same burst; we do not combine them. An upper limit \(U\) on \(\eta_2\) gives</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>In continuous time, we obtain:</p>
<div class="tableau"><table>
<thead><tr><th>Method</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\), worst orientation (m)</th><th>\(a\), 95% of orientations (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML (calibrated)</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>The summary keeps the most conservative value, [[a_resume]]&nbsp;m: it is a presentation envelope, not a new interval. At this limit, a 1&nbsp;TeV photon would arrive at most [[retard_limite]]&nbsp;s after a [[e_bas]]&nbsp;TeV photon.</p>
<p>A few predictions, which are not measurements (1&nbsp;TeV photon compared with a [[e_bas]]&nbsp;TeV photon):</p>
<div class="tableau"><table>
<thead><tr><th>Spacing</th><th>Predicted \(\eta_2\)</th><th>Predicted delay</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]] to [[p26_eta_max]]</td><td>[[p26_ret_min]] to [[p26_ret_max]]&nbsp;s</td><td>excluded for every orientation</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]] to [[p27_eta_max]]</td><td>[[p27_ret_min]] to [[p27_ret_max]]&nbsp;s</td><td>excluded near the axes (\(Q>\)&nbsp;[[q_cal_axe]]) by the calibrated method only</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]] to [[p28_eta_max]]</td><td>[[p28_ret_min]] to [[p28_ret_max]]&nbsp;ms</td><td>not excluded</td></tr>
<tr><td>[[lpl]]&nbsp;m (Planck)</td><td>[[pl_eta_min]] to [[pl_eta_max]]</td><td>[[pl_ret_min]] to [[pl_ret_max]]&nbsp;s</td><td>out of reach</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. How far the bound holds</h2>
<h3>The orientation of the grid</h3>
<p>We do not know how the grid would be oriented relative to the direction of the burst. The main bound takes the least favorable case, \(Q=1/3\). Over one million uniformly distributed directions, \(Q\) has a median of [[q_mediane]] and exceeds [[q_5]] in 95% of cases: the bound moves little, with [[ccf_95]]&nbsp;m for 95% of orientations and [[ccf_mediane]]&nbsp;m for the median orientation. These fractions are geometric: they are not probabilities about the Universe.</p>
<h3>Discrete time, the weak point of the bound</h3>
<p>A simulation advances in time steps. Discretizing time produces an error of opposite sign, which partly compensates the spatial one (the term \(-\sigma^{2}/3\)). For the conservative method:</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>Worst orientation</th><th>95% of orientations</th><th>Median orientation</th></tr></thead>
<tbody>
<tr><td>0 (continuous time)</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1 (maximum step)</td><td>[[s4_cdt]]</td><td>no bound</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>At the maximum stable step, the compensation is exact along the main diagonals, and not only at first order: there the dispersion relation gives back \(\omega=ck\) for every wavelength. A simulation tuned this way would escape this test entirely if the burst fell on one of its eight diagonal directions. This is the main limitation of a bound drawn from a single source; several sources in different directions would remove it, because, barring coincidence, they cannot all be aligned with diagonals.</p>
<h3>A fixed spacing or one stretched by expansion</h3>
<p>We assume a fixed physical spacing. If the grid stretched with the Universe (comoving spacing), the effect would no longer grow with redshift and \(I_2\) would be replaced by \(I_0\): the bound weakens by a factor \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]], giving [[comobile_a]]&nbsp;m. At <em>z</em>&nbsp;=&nbsp;[[z]], this choice matters little.</p>
<h3>More accurate schemes</h3>
<p>A simulator can use a higher-order scheme, whose dominant error scales as \(a^{4}\). The effect then becomes quartic in energy, and the bound on \(a\) much weaker. LHAASO does not publish a constraint of this type for this burst; quantifying it would require the photon-by-photon data. Terms designed to compensate the dispersion would also escape the bound. These are other models, to be tested separately.</p>
<h3>What if the error were linear?</h3>
<p>A symmetric lattice produces no effect linear in \(a\). A discretization that did produce one, by breaking the symmetry between the two directions of propagation, would fall under the linear bound of LHAASO, \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\): with a coefficient of order one, \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m, that is one tenth of the Planck length. Any coarser grid of this type is excluded.</p>
<h3>The validity of the calculation</h3>
<p>The expansion assumes \(aE/\hbar c\ll1\). At the bound, even for 20&nbsp;TeV photons, \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]. We also compared the expansion with the exact dispersion relation: for \(ak\)&nbsp;=&nbsp;[[ak_test]], the relative difference does not exceed [[ecart_dispersion]], as expected.</p>

<h2 id="contexte">5. What it is worth, compared with existing work</h2>
<p>Beane, Davoudi and Savage (2012) studied a simulation of lattice quantum chromodynamics. They bounded the inverse lattice spacing at \(1/b\gtrsim10^{11}\)&nbsp;GeV, that is \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m, from the cutoff of the cosmic-ray spectrum. Our conservative bound is [[beane_ratio]] times theirs; the LHAASO likelihood methods give [[beane_ml_min]] to [[beane_ml_max]] times theirs. The two bounds are of the same order of magnitude, but they rest on different observables, particles and models: strictly speaking they do not confirm each other and are not interchangeable.</p>
<p>The Planck length, [[lpl]]&nbsp;m, remains eight orders of magnitude lower. For a spacing of this size, the effect would be [[facteur_planck_exact]] times weaker than the limit. Since it grows with the square of the energy, photons about a hundred million times more energetic would be needed, far beyond anything observed: at this order, no time-of-flight test can reach a Planck grid.</p>

<h2 id="xi-shu">6. A check of the literature: Xi and Shu (2025)</h2>
<p>Xi and Shu analyzed the same burst with another method and report \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV (their table III), about [[xs_rapport_lhaaso]] times the LHAASO bound. Using their own definitions, we do not recover this value.</p>
<ul>
<li>Their equation (3) sets the delay in \((E/E_{\mathrm{QG},n})^{n}\). For \(n=1\), their conversion (6), \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\) with \(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]], is consistent: we find [[xs_c1]].</li>
<li>For \(n=2\), their equation (7), \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\) with \(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]], keeps the \(1/\theta\) form. Applied to their limit \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV², it does reproduce their table ([[xs_eq7]]&nbsp;GeV). But since the delay is quadratic, their equation (3) imposes a \(1/\sqrt{\theta_2}\) dependence: \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\), that is \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV.</li>
<li>The discrepancy is a factor of [[xs_facteur]]. A plausible explanation: \(\varepsilon^{2}\theta_2\) equals [[xs_eps2]], and [[xs_c2_imprime]] looks like the square root of [[xs_eps2_imprime]] taken on the power of ten alone.</li>
</ul>
<p>Status: apparent inconsistency in version 1 of the paper, to be confirmed with the authors. We do not reanalyze their data and do not judge their other results. Once corrected, their bound would remain [[xs_vs_lhaaso]] times stronger than that of LHAASO. We do not use it.</p>

<h2 id="limites">7. What this test does not say</h2>
<ul>
<li>It detects nothing: a null delay remains compatible with all measurements.</li>
<li>It computes no probability that we are in a simulation; the “95%” refers to a physical parameter.</li>
<li>It bounds a specific architecture: cubic grid, Yee scheme, fixed spacing, no compensation.</li>
<li>Even a detected delay would not point to a computer: a fundamentally discrete physics, or other quantum gravity effects, would produce the same signal.</li>
<li>The LHAASO intervals rest on assumptions about the emission of the source; we inherit them.</li>
</ul>

<h2 id="suite">8. Next steps</h2>
<ol>
<li>Combine several sources seen in different directions, to close the blind spot of the diagonals.</li>
<li>Quantify higher-order schemes (effect in \(a^{4}\)), which requires the photon-by-photon data.</li>
<li>Ask Xi and Shu to clarify their conversion.</li>
<li>Extend the test to other signatures of a grid: cosmic-ray anisotropy, charged particles.</li>
</ol>

<h2 id="reproduire">9. Reproduce</h2>
<p>Everything is recomputed by a dependency-free Python script, which first checks its own formulas: expansion against exact dispersion, exact diagonal, round-trip conversions, cosmological integral, mean of \(Q\) equal to 3/5.</p>
<p>An independent cross-check (numpy, scipy) recovers the cosmological integral to within 10<sup>−15</sup>, the orientation quantiles over ten million random draws, and the group velocity by numerical solution of the dispersion relation.</p>
<p>This note replaces a first version of September 28, 2026. It adds discrete time, orientation, the comoving spacing, the linear effect and the comparison with Beane et al.</p>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a> (revision of February 13, 2026): equations 2, 3 and 5, table I.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a> (2025): equations 3, 6 and 7, tables I and III.</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302 (1966).</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395 (1975).</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House: numerical dispersion and stability of the Yee scheme.</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>: fundamental constants.</li>
</ol>
""",
}
ARTICLE_2 = {
    'titre': 'Do cosmic rays trace out a grid?',
    'description': 'The most energetic particles ever recorded by the Pierre Auger Observatory, '
                   'compared with the imprint a cubic grid should leave on them.',
    'date': 'September 28, 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No.</strong> The test detects no significant departure from isotropy in the directions of the [[n_evt]] most energetic cosmic rays measured by the Pierre Auger Observatory: under the isotropic model, [[p4_pct]]% of the simulated skies, put through the same search, show a cubic pattern at least as marked as the one observed.</p>
<p>This “no” has a limited scope. This number is neither the probability that chance explains the data, nor the probability that a grid exists. A weaker pattern is not excluded, and the absence of an observable cubic pattern does not prove the absence of a grid.</p>
</section>

<h2 id="explication">Explanation</h2>
<p>If our world were computed by a computer, space might be cut into tiny cubes, the way an image is made of pixels. In 2012, three physicists pointed out that such a division would leave a trace: the fastest particles in the Universe would not arrive in the same way from all directions. Some directions would be favored, arranged like the faces or the corners of a cube.</p>
<p>These particles exist: they are cosmic rays, atomic nuclei coming from space with an energy far above anything our accelerators produce. In Argentina, the Pierre Auger Observatory watches for them with a huge array of detectors. It has published the list of its [[n_evt]] most energetic catches, recorded between 2004 and 2020, with the direction from which each one arrived.</p>
<p>We took these [[n_evt]] directions and looked for whether they line up along a cube. Since nobody knows how this cube would be rotated, we tried [[n_orient]] positions. The best one fits the data a little. But when you try that many positions, you always find one that fits a little, even in a sky due to pure chance.</p>
<p>To decide, we built [[n_ciels]] fake skies drawn at random, seen by the same observatory, and ran exactly the same search on each one. In [[p4_pct]]% of them, a cube is found that fits at least as well. The real sky therefore does not stand out from these fake skies. To speak of a hint, it would have had to do better than almost all the fake skies.</p>
<p>Conclusion: no trace of a grid is detected. But this search could only see a strong pattern: with only [[n_evt]] particles, a subtle pattern would go unnoticed. Moreover, the magnetic fields of our galaxy deflect these particles on their way, which would blur part of the pattern. This test therefore does not prove that space is continuous; it shows that, where it was possible to look, there is nothing.</p>

<h2 id="analyse">Detailed analysis</h2>

<h3>1. From the grid to a testable prediction</h3>
<p>On a cubic lattice of spacing \(a\), the discrete Laplacian replaces \(k^{2}\) by \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\). For a free field,</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>where \(\mathbf n\) is the direction of propagation in the lattice axes. This is the same function \(Q\) as in test&nbsp;1. More generally, any effect of the grid on arrival directions (propagation, direction-dependent spectral cutoff) is a function of \(\mathbf n\) invariant under the cube group \(O_h\). Now, spherical harmonics invariant under \(O_h\) exist only for \(\ell=0,4,6,8,\dots\): the first allowed anisotropy is the cubic harmonic \(\ell=4\), proportional to \(Q-3/5\). This is our main test, fixed before opening the data; \(\ell=6\) is tested second. Beane, Davoudi and Savage write that the simulation “could reveal itself in the distributions of the highest energy cosmic rays exhibiting a degree of rotational symmetry breaking that reflects the structure of the underlying lattice”.</p>

<h3>2. The data</h3>
<p>Catalog of the Pierre Auger Observatory (ApJS 264, 50, 2023): the [[n_evt]] highest-energy air showers recorded from January 1<sup>st</sup>, 2004 to December 31, 2020, from [[e_min]] to [[e_max]]&nbsp;EeV, with zenith angles up to [[zmax]]°. The open file also contains [[n_calib]] hybrid calibration events, outside the [[n_evt]]: we discard them. We use the right ascension and declination reconstructed by the surface detector. The SHA-256 hash of the file is checked at each run. At these energies, the detection efficiency is full up to [[zmax]]°, so the exposure is purely geometric.</p>

<h3>3. The exposure of the detector</h3>
<p>A ground-based detector at latitude \(a_0\)&nbsp;=&nbsp;[[lat]]°, which accepts zenith angles \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]°, has an exposure that is uniform in right ascension and, in declination \(\delta\) (Sommers, 2001):</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>The visible sky stops at \(\delta\)&nbsp;=&nbsp;[[dec_max]]°, that is [[ciel_pct]]% of the sphere. An isotropic sky seen by Auger is therefore not uniform: everything that follows compares the data with that sky, not with a uniform sphere.</p>

<h3>4. The statistic</h3>
<p>Let \(R\) be an orientation of the grid, with rows \(\mathbf e_k\), and \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). For the \(N\) observed directions:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>where \(\langle\cdot\rangle_\omega\) is the mean over an isotropic sky weighted by the exposure. \(T>0\) signals an excess along the axes of the cube, \(T<0\) along its diagonals; the absolute value covers both. Since \(f\) is a polynomial of degree 4, \(T(R)\) depends on the data only through the 15 moments \(\sum_i\mathbf n_i^{\alpha}\); mean and variance are computed exactly by Gauss-Legendre quadrature. The maximum is taken over [[n_orient]] orientations drawn uniformly (Haar measure). For \(\ell=6\), we take \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\), with \(\alpha\)&nbsp;=&nbsp;[[alpha6]] (that is \(-15/11\)), which makes it orthogonal to \(\ell=4\); the combined test maximizes \(T_4^{2}+T_6^{2}\).</p>

<h3>5. Calibrating chance</h3>
<p>Searching for the best orientation among [[n_orient]] mechanically inflates \(Z_4\): it does not follow a normal distribution. We therefore draw [[n_ciels]] isotropic skies of \(N\) events according to the exposure, and apply exactly the same maximization to them. Under the “no grid” hypothesis, \(Z_4\) has a median of [[z4_50]]; it exceeds [[z4_95]] in 5% of cases, [[z4_99]] in 1% and [[z4_999]] in 0.1%. The p-value, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), thus includes the cost of choosing the orientation.</p>

<h3>6. Result</h3>
<div class="tableau"><table>
<thead><tr><th>Test</th><th>Observed statistic</th><th>p-value</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (main)</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\) and \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>At the best orientation, the mean of \(Q\) is [[q_obs]] against [[q_iso]] expected, an excess of [[q_ecart_pct]]% toward the axes. This is not significant: \(p\)&nbsp;=&nbsp;[[p4]] for the main test, and no secondary test goes below 0.05. The data are compatible with the absence of any cubic symmetry.</p>

<h3>7. What the test could see</h3>
<p>To quantify the sensitivity, a cubic pattern is injected: density proportional to \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Along an axis (\(Q=1\)), the flux is \(1+\varepsilon\) times the mean; along a diagonal (\(Q=1/3\)), it is \(1-2\varepsilon/3\) times the mean. With \(\varepsilon>0\), the excess is therefore along the axes; with \(\varepsilon<0\), it is along the diagonals and equals \(2\lvert\varepsilon\rvert/3\).</p>
<p>The 95% upper limit depends on the convention for the orientation. If the orientation of the grid is drawn at random for each simulated sky ([[n_ciels_signal]] skies per amplitude), we obtain a limit averaged over orientations: \(\varepsilon\le\)&nbsp;[[eps_axes]] and \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]]. An average does not guarantee coverage for each orientation: we therefore redo the calculation at fixed orientation, for [[n_orient_fixes]] orientations including the one least visible to Auger ([[n_ciels_fixes]] skies per amplitude). The limit then ranges from [[eps_axes_fix_min]] to [[eps_axes_fix]] toward the axes and from [[eps_diag_fix_min]] to [[eps_diag_fix]] toward the diagonals; we keep the least constraining value. A flux excess of up to about [[exces_axes_pct]]% along the axes, or [[exces_diag_pct]]% along the diagonals, is therefore not excluded. This is a weak constraint, set by the small number of events, established for the orientations tested and not demonstrated for all of them.</p>
<p>The script first checks its own chain: invariance of \(Q\) under the cube group, exact polynomial expansion, zero exposure beyond [[dec_max]]°, \(T\) standardized under isotropy, orthogonality of \(\ell=6\) to \(\ell=4\), and detection of a clear injected pattern, whose orientation is recovered to within [[ecart_orient]]°.</p>

<h3>8. Limitations</h3>
<ul>
<li>Cosmic rays are charged: Galactic and extragalactic magnetic fields deflect their directions, all the more so for heavier nuclei. The pattern sought is broad (an axis and a diagonal are [[angle_diag]]° apart) and withstands modest deflections, but an imprint set at the source or during propagation would be partly erased.</li>
<li>We assume the grid is fixed relative to the distant stars (equatorial coordinates). A grid moving or rotating relative to them would require another test.</li>
<li>[[n_evt]] events and [[ciel_pct]]% of the sky: the statistical power is low, as the limit above shows.</li>
<li>Real astrophysical anisotropies can contain an \(\ell=4\) component. A positive result would have required excluding them; a null result does not depend on them.</li>
<li>No probability of being simulated is computed: the test addresses one specific signature, that of a cubic grid.</li>
</ul>

<h3>9. Reproduce</h3>
<p>A Python script (numpy) redoes everything in a few minutes: reading and checking the data, self-tests, statistic, simulated skies, upper limits. The random number generator has a fixed seed: the results are identical from one run to the next.</p>
<p>Corrections of September 28, 2026, after review: the flux excess along the diagonals had been confused with the parameter \(\lvert\varepsilon\rvert\), whereas it equals \(2\lvert\varepsilon\rvert/3\); the fixed-orientation limit was added; the verdict was reworded so as not to present the p-value as a probability about the hypotheses.</p>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Pierre Auger Collaboration, <cite>A Catalog of the Highest-Energy Cosmic Rays Recorded During Phase I of Operation of the Pierre Auger Observatory</cite>, ApJS 264, 50 (2023), <a href="https://arxiv.org/abs/2211.16020">arXiv:2211.16020</a>.</li>
<li>Pierre Auger Collaboration, <cite>Auger Open Data</cite>, release 3, <a href="https://doi.org/10.5281/zenodo.10488964">DOI 10.5281/zenodo.10488964</a>; detection efficiency: <a href="https://opendata.auger.org/data.php">opendata.auger.org</a>.</li>
<li>P. Sommers, <cite>Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory</cite>, Astroparticle Physics 14, 271 (2001), <a href="https://arxiv.org/abs/astro-ph/0004016">arXiv:astro-ph/0004016</a>.</li>
</ol>
""",
}

ARTICLE_3 = {
    'titre': 'Does light travel more slowly in some directions?',
    'description': 'Eight gamma-ray sources spread across the sky, combined to close the blind spot '
                   'of test 1 and bound the spacing of a cubic grid whatever its orientation.',
    'date': 'September 28, 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No.</strong> None of the [[n_src]] sources studied shows the delay that a grid would produce. By combining their directions, a cubic grid with a spacing greater than or equal to [[a_exclue]]&nbsp;m is excluded, whatever its orientation and whatever its time step: the blind spot of test&nbsp;1 is closed.</p>
</section>

<h2 id="explication">Explanation</h2>
<p>If the Universe were computed on a grid, the way an image is made of pixels, light would not travel through it at quite the same speed in all directions. The most energetic light would pick up a very slight delay, larger along the edges of the grid than along its diagonals. Over billions of years of travel, this delay would become measurable.</p>
<p>Test&nbsp;1 looked for this delay in the brightest gamma-ray burst ever observed, and saw nothing. But a loophole remained: if the simulation advances in time by the largest possible step, light no longer picks up any delay along the diagonals of the grid. A single source located on a diagonal then allowed no conclusion.</p>
<p>Here, we look at [[n_src]] sources at once, in different directions of the sky: three explosions of distant stars, four galaxies with a very active black hole, and the pulsar of the Crab Nebula. For each one, a team of astronomers has already measured that no delay appears, down to a certain precision. We reread each paper, brought all the results to the same convention, then looked for the orientation of the grid most favorable to a hidden grid, the one that weakens the limit the most.</p>
<p>It is impossible to place all the sources on diagonals at the same time. Even in the most favorable orientation, three sources remain far enough from a diagonal that a delay should have appeared. A grid whose cells measure at least [[a_exclue]]&nbsp;m is therefore excluded in all orientations. This size remains about [[planck_x]] times larger than the Planck length: a much finer grid remains entirely possible.</p>

<h2 id="analyse">Detailed analysis</h2><p><strong>Corrected statistical scope.</strong> The eight nominal 95% bounds form a complete family. Bonferroni gives at least [[couverture]]% simultaneous coverage, under their respective assumptions. Counting only the [[n_actives]] constraints that are active after optimization would be an a posteriori selection. The orientation maximum is numerical, without a global certificate: the value [[pire1]]&nbsp;m is a compatibility envelope of the model, not a joint 95% exclusion.</p>

<h3>1. The model</h3>
<p>As in test&nbsp;1: Maxwell’s equations on a cubic lattice of spacing \(a\) (Yee scheme), time step \(c\,\Delta t=\sigma a/\sqrt{3}\) with \(0\le\sigma\le1\). At leading order,</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\,Q_{\mathrm{eff}}\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3},\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>Since \(1/3\le Q\le1\), \(Q_{\mathrm{eff}}\ge0\): the photon is always slowed down, and \(Q_{\mathrm{eff}}=0\) exactly on the main diagonals when \(\sigma=1\). At the final bound, \(aE/\hbar c\)&nbsp;=&nbsp;[[ae]] for a 20&nbsp;TeV photon: the expansion is valid.</p>

<h3>2. From published limits to a bound on the spacing</h3>
<p>The eight papers describe a quadratic delay by \(v/c\simeq1-\tfrac{3}{2}(E/E_{\mathrm{QG},2})^{2}\), with the Jacob and Piran distance \(K_2=\int_0^{z}(1+z')^{2}\,dz'/H(z')\). By identification,</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}}\quad\Longrightarrow\quad a\sqrt{Q_{\mathrm{eff}}(\mathbf n_i)}\le B_i=\frac{\sqrt{12}\,\hbar c}{E_i}.$$
<p>Rule fixed in advance: 95% limit, subluminal case, time of flight, least constraining method of each paper. Each limit is brought to the LHAASO cosmology by \(E_i\sqrt{K_2^{\mathrm{LHAASO}}(z_i)/K_2^{(i)}(z_i)}\); the factor does not exceed [[fc_max]]. Each published conversion is redone from the printed parameters and recovers the value in the paper (self-tests).</p>
<div class="tableau"><table>
<thead><tr><th>Source</th><th>Instrument</th><th>\(z\) or distance</th><th>Published \(E_{\mathrm{QG},2}\) (GeV)</th><th>Common cosmology (GeV)</th><th>\(B_i\) (m)</th></tr></thead>
<tbody>
<tr><td>GRB 221009A</td><td>LHAASO</td><td>[[s0_z]]</td><td>[[s0_pub]]</td><td>[[s0_com]]</td><td>[[s0_b]]</td></tr>
<tr><td>GRB 190114C</td><td>MAGIC</td><td>[[s1_z]]</td><td>[[s1_pub]]</td><td>[[s1_com]]</td><td>[[s1_b]]</td></tr>
<tr><td>GRB 090510</td><td>Fermi-LAT</td><td>[[s2_z]]</td><td>[[s2_pub]]</td><td>[[s2_com]]</td><td>[[s2_b]]</td></tr>
<tr><td>Mrk 501</td><td>H.E.S.S.</td><td>[[s3_z]]</td><td>[[s3_pub]]</td><td>[[s3_com]]</td><td>[[s3_b]]</td></tr>
<tr><td>Mrk 421</td><td>MAGIC</td><td>[[s4_z]]</td><td>[[s4_pub]]</td><td>[[s4_com]]</td><td>[[s4_b]]</td></tr>
<tr><td>PKS 2155-304</td><td>H.E.S.S.</td><td>[[s5_z]]</td><td>[[s5_pub]]</td><td>[[s5_com]]</td><td>[[s5_b]]</td></tr>
<tr><td>PG 1553+113</td><td>H.E.S.S.</td><td>[[s6_z]]</td><td>[[s6_pub]]</td><td>[[s6_com]]</td><td>[[s6_b]]</td></tr>
<tr><td>Crab (pulsar)</td><td>MAGIC</td><td>[[s7_z]]&nbsp;kpc</td><td>[[s7_pub]]</td><td>[[s7_com]]</td><td>[[s7_b]]</td></tr>
</tbody>
</table></div>

<h3>3. The worst orientation</h3>
<p>For an orientation \(R\) of the lattice, the sources jointly bound</p>
$$a\le A(R)=\min_i\frac{B_i}{\sqrt{Q_{\mathrm{eff}}(R\mathbf n_i)}},$$
<p>a source on a diagonal at \(\sigma=1\) bounding nothing. We look for \(\max_R A(R)\): [[n_orient]] uniformly drawn rotations, constructed orientations (each source placed on a diagonal then rotated about it), then a local refinement. A second, independent seed recovers the same maximum to within [[ecart_graines]]. The optimiser is validated on known cases: a single source bounds nothing at \(\sigma=1\), and two sources separated by the angle between two diagonals can be placed on diagonals together.</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>Worst orientation (m)</th><th>95% of orientations (m)</th></tr></thead>
<tbody>
<tr><td>0</td><td>[[pire0]]</td><td>[[q95_0]]</td></tr>
<tr><td>0.5</td><td>[[pire05]]</td><td>[[q95_05]]</td></tr>
<tr><td>0.9</td><td>[[pire09]]</td><td>[[q95_09]]</td></tr>
<tr><td>1</td><td>[[pire1]]</td><td>[[q95_1]]</td></tr>
</tbody>
</table></div>
<p>For \(\sigma<1\), nothing changes compared with test&nbsp;1: GRB&nbsp;221009A dominates, the other sources being [[x_min]] to [[x_max]] times less sensitive. Everything is decided at \(\sigma=1\): placing GRB&nbsp;221009A on a diagonal is no longer enough, because the other sources then see the grid at an angle. The worst compromise moves GRB&nbsp;221009A [[ang_grb]]° away from the nearest diagonal (\(Q_{\mathrm{eff}}\)&nbsp;=&nbsp;[[qeff_grb]]) and balances [[n_actives]] constraints: GRB&nbsp;221009A, GRB&nbsp;090510 and the Crab. The bound is then [[pire1]]&nbsp;m, that is a scale \(\hbar c/a\ge\)&nbsp;[[echelle]]&nbsp;GeV. Since \(A(R)\) increases with \(\sigma\) for every orientation, it holds for every \(\sigma\le1\). At \(\sigma=1\), the median of the orientations gives [[med1]]&nbsp;m.</p>
<p>Closing the blind spot was not a given: GRB&nbsp;190114C and GRB&nbsp;090510 are [[ang_190_090]]° apart, almost the angle between two diagonals ([[ang_diag]]°), and GRB&nbsp;090510 and PKS&nbsp;2155-304 are only [[ang_090_pks]]° from each other. It is the diversity of the rest of the sky that closes the blind spot.</p>

<h3>4. Robustness</h3>
<p>Worst orientation at \(\sigma=1\), depending on the choices:</p>
<ul>
<li>without GRB&nbsp;221009A: [[v_sans_lhaaso]]&nbsp;m, the blind spot stays closed;</li>
<li>published limits without cosmology conversion: [[v_sans_cosmo]]&nbsp;m;</li>
<li>Fermi with source-intrinsic effects (table V of the paper): [[v_fermi]]&nbsp;m;</li>
<li>gamma-ray bursts only: [[v_sursauts]]&nbsp;m;</li>
<li>blazars and pulsar only: [[v_blazars]]&nbsp;m.</li>
</ul>

<h3>5. Comparisons</h3>
<p>The bound valid for every orientation and every time step is [[x_test1]] times weaker than that of test&nbsp;1 in continuous time. Beane, Davoudi and Savage obtained \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m from the cutoff of the cosmic-ray spectrum; our continuous-time bound is [[x_beane0]] times theirs, and our universal bound [[x_beane]] times.</p>

<h3>6. Limitations</h3>
<ul>
<li>For each orientation, the combined bound takes the most constraining of 95% limits published one by one: it is not a combined likelihood, which the papers do not publish. With a Bonferroni correction over the eight sources (1 − 8 × 0.05), the guaranteed coverage is at least [[couverture]]%, not 95%.</li>
<li>Each paper assumes that no source-intrinsic lag compensates or mimics the delay.</li>
<li>The redshifts of Mrk&nbsp;421 and PG&nbsp;1553+113 are uncertain; these two sources are not active at the worst orientation. The distance of the Crab, which is active, is included in the MAGIC uncertainties.</li>
<li>A higher-order scheme (error in \(a^{4}\)), compensating terms, or a non-cubic grid or one stretched by expansion escape this bound.</li>
<li>Secondary analysis: no photon is reanalyzed. The fractions of orientations are geometric, not probabilities about the Universe.</li>
</ul>

<h3>7. Reproduce</h3>
<p>The script redoes everything in a few seconds and first checks its formulas and each published conversion. Every input figure is cited, with page and table, in <code>sources.md</code>.</p>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>LHAASO Collaboration, GRB 221009A, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>, table I.</li>
<li>MAGIC Collaboration, GRB 190114C, <a href="https://arxiv.org/abs/2001.09728v4">arXiv:2001.09728v4</a>, table I.</li>
<li>Fermi-LAT Collaboration, GRB 090510, <a href="https://arxiv.org/abs/1305.3463v1">arXiv:1305.3463v1</a>, tables IV and V.</li>
<li>H.E.S.S. Collaboration, Mrk 501, <a href="https://arxiv.org/abs/1901.05209v1">arXiv:1901.05209v1</a>.</li>
<li>MAGIC Collaboration, Mrk 421, <a href="https://arxiv.org/abs/2406.07140v1">arXiv:2406.07140v1</a>, table 2.</li>
<li>H.E.S.S. Collaboration, PKS 2155-304, <a href="https://arxiv.org/abs/1101.3650v2">arXiv:1101.3650v2</a>.</li>
<li>H.E.S.S. Collaboration, PG 1553+113, <a href="https://arxiv.org/abs/1501.05087v1">arXiv:1501.05087v1</a>, table 5.</li>
<li>MAGIC Collaboration, Crab pulsar, <a href="https://arxiv.org/abs/1709.00346v1">arXiv:1709.00346v1</a>, table 6.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>.</li>
<li>Coordinates: <a href="https://simbad.cds.unistra.fr/simbad/">SIMBAD</a> (CDS, Strasbourg).</li>
</ol>
""",
}

ARTICLE_4 = {
    'titre': 'Does quantum randomness betray a program?',
    'description': 'Millions of bits drawn from quantum experiments, screened with the tests that expose '
                   'the pseudorandom generators a simulation would use.',
    'date': 'September 28, 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No.</strong> In the raw quantum bits tested, no signature of a pseudorandom generator appears, while the same tests expose four simple generators used as controls. One point must be stated at the outset: the rule set before the analysis is triggered by the IBM data as published, but the cause is identified — one of the nine machines stayed stuck at 0 or at 1 for entire series — and this defect does not have the structure of a generator. Setting it aside was decided after seeing the data; we report it as such.</p>
<p>This “no” has a limited scope: it rules out a simulation that would draw its quantum measurements from a simple generator, not a simulation that would use a cryptographic-quality generator, which is indistinguishable in principle.</p>
</section>

<h2 id="explication">Explanation</h2>
<p>If the world were a simulation, the result of every quantum measurement, 0 or 1, would have to be produced. Physics says this result is unpredictable by nature. A computer cannot produce true randomness: it manufactures it with a computational recipe. A thrifty simulation would use a fast and simple recipe, and simple recipes leave fingerprints: repetitions, hidden regularities, a structure that can be recovered by computation.</p>
<p>So we took sequences of 0s and 1s produced by real quantum experiments and published by their authors, and we searched them for these fingerprints. First difficulty: most public sources of quantum randomness pass their results through a mathematical “mixer” before publishing them. This mixer is designed to erase all structure; testing its output says nothing about the source. We tested these data anyway, but they do not count in the verdict.</p>
<p>Two raw sources remain: an entangled-photon device at the University of Portland (Oregon), which publishes its bits as they are, and nine IBM quantum computers that were asked millions of times to flip a coin with a single qubit. The photons pass every test. The IBM machines give slightly too many 0s, a known defect explained by their authors; once this imbalance is corrected, they pass. One of them, Belem, stayed stuck for entire series of measurements: a fault, not a computational recipe.</p>
<p>The controls behave as expected: the simple recipes are exposed, including a very widespread generator that nonetheless passes the official NIST battery; the sophisticated recipes are not, and neither are the digits of the square root of 2, even though they are perfectly computable. This is the limit of this test: a carefully built simulation would leave no trace of this kind.</p>

<h2 id="analyse">Detailed analysis</h2>

<h3>1. What is testable</h3>
<p>A statistical test only informs about the last processing step applied to a sequence of bits: an output hashed by a cryptographic function looks like perfect randomness whatever the input. We tested [[bits_total]] bits, of which [[bits_bruts]] are raw:</p>
<div class="tableau"><table>
<thead><tr><th>Dataset</th><th>Origin</th><th>Processing</th><th>Bits</th></tr></thead>
<tbody>
<tr><td>parity</td><td>polarization-entangled photons (Kavulich et al., 2021)</td><td>none</td><td>[[n_parity]]</td></tr>
<tr><td>ibm</td><td>one qubit, Hadamard gate, measurement; nine machines (Root and Becker, 2024)</td><td>none</td><td>[[n_ibm]]</td></tr>
<tr><td>anu</td><td>vacuum fluctuations, ANU</td><td>AES-128</td><td>[[n_anu]]</td></tr>
<tr><td>beacon</td><td>NIST Beacon 2.0</td><td>SHA-512</td><td>[[n_beacon]]</td></tr>
</tbody>
</table></div>
<p>Only parity and ibm inform about the nature of quantum randomness. The raw data of the NIST loophole-free Bell test (2015) were not used: their measurement choices combine physical sources and a pseudorandom source, and their detection results are not uniform bits. For the Beacon, the published chain of commitments was checked on [[engagements]] consecutive pairs.</p>

<h3>2. Level 1: the NIST SP 800-22 battery</h3>
<p>The 15 tests of the official battery are reimplemented and reproduce the [[annexe_n]] p-values of Appendix B of the document to within [[annexe_ecart]] ([[annexe_ecart_chev]] for one test). The data are cut into [[n_seq]] sequences of 10<sup>6</sup> bits; the [[np1]] p-values form a single family corrected by the Holm method at an overall level of 1%.</p>
<ul>
<li>parity: [[par_np1]] p-values, no rejection (smallest adjusted p-value: [[par_p1]]); proportion of bits equal to 1: [[par_frac]].</li>
<li>anu and beacon: no rejection (smallest adjusted p-value for anu: [[anu_p1]]).</li>
<li>ibm: [[ibm_rej1]] rejections out of [[ibm_np1]]; proportion of bits equal to 1: [[ibm_frac]], a deviation of [[ibm_z]] standard deviations. Without the Belem machine, the von Neumann extractor, which removes a constant bias exactly, leaves [[vn_bits]] bits and no rejection out of [[vn_np]] p-values ([[vn_p]]): the failures come from the bias described by the authors.</li>
</ul>

<h3>3. Level 2: the signatures of a generator</h3>
<p>The NIST battery says whether a sequence departs from ideal randomness, not why. Three tests target the defects specific to algorithmic generators:</p>
<ul>
<li><strong>Linear complexity.</strong> The Berlekamp-Massey algorithm gives the length \(L\) of the shortest linear feedback shift register that reproduces a segment of \(n\) bits. For a random sequence, \(L\simeq n/2\); any linear generator over \(\mathrm{GF}(2)\) whose state has fewer than \(n/2\) bits gives \(L\lt n/2\). Segments of [[seg_bm]] bits, read continuously or one bit in 48 and one in 64: a state of up to [[etat_max]] bits is covered.</li>
<li><strong>Repetitions.</strong> Each 64-bit window is compared with all the others; the expected number of identical pairs is of the order of [[rep_attendu]]. A single repetition would signal a period or a reused seed.</li>
<li><strong>Long-range correlations.</strong> Autocorrelation at lags 17 to [[lag_max]], with Bonferroni correction.</li>
</ul>
<p>Main family, Holm at 1% on [[np2]] p-values: parity rejects nothing ([[par_p2]]); its maximum deviation of \(L\) from \(n/2\) is [[par_ecart_l]]; no repetition; long-range correlations: [[par_auto]]. anu and beacon reject nothing. ibm rejects [[ibm_rej2]] times.</p>

<h3>4. The IBM rejections: a stuck machine</h3>
<p>The IBM data consist of [[ibm_essais]] runs of 8,192 shots. [[ibm_const]] of them are constant ([[ibm_const0]] entirely 0, [[ibm_const1]] entirely 1) and [[ibm_quasi]] others are more than 99% constant; all come from the Belem machine. The [[ibm_paires]] pairs of identical windows are all sequences of equal bits: among windows of ordinary composition, there are [[ibm_paires_typ]]. A frozen output is not the output of a pseudorandom generator: it is the absence of output.</p>
<p>Setting Belem aside was decided after seeing the data: it is therefore a secondary analysis, with its own Holm correction, and the result of the initial rule remains published. On the other eight machines ([[sb_bits]] bits), level 2 rejects nothing ([[sb_np2]] p-values, smallest adjusted p-value [[sb_p2]]); the maximum deviation of \(L\) from \(n/2\) is [[sb_ecart_l]] and there is no repetition. A correlation at lag 1 exists ([[sb_r1]], or [[sb_z1]] standard deviations): a short-range measurement defect, unrelated to the structure of a generator. Level 1 rejects [[sb_rej1]] times out of [[sb_np1]] there, because of the bias.</p>

<h3>5. The controls</h3>
<p>The same pipeline is applied to [[bits_ctrl]] bits from each known generator; the script stops if a control does not behave as expected.</p>
<div class="tableau"><table>
<thead><tr><th>Generator</th><th>Expected</th><th>Result (smallest adjusted p-values, levels 1 and 2)</th></tr></thead>
<tbody>
<tr><td>LFSR of degree 20</td><td>detected</td><td>detected: \(L\)&nbsp;=&nbsp;[[l20_lmin]], repetitions</td></tr>
<tr><td>LFSR of degree 31</td><td>detected</td><td>detected: \(L\)&nbsp;=&nbsp;[[l31_lmin]], \(\log_{10}p\)&nbsp;=&nbsp;[[l31_log10p]]</td></tr>
<tr><td>32-bit LCG</td><td>detected</td><td>detected: spectral test, long-range correlations</td></tr>
<tr><td>Mersenne Twister</td><td>detected</td><td>detected by level 2 alone: \(L\)&nbsp;=&nbsp;[[mt_lmin]], \(\log_{10}p\)&nbsp;=&nbsp;[[mt_log10p]]; NIST battery silent ([[mt_p1]])</td></tr>
<tr><td>PCG64</td><td>not detected</td><td>nothing ([[pcg_p1]]; [[pcg_p2]])</td></tr>
<tr><td>SHA-256 in counter mode</td><td>not detected</td><td>nothing ([[sha_p1]]; [[sha_p2]])</td></tr>
<tr><td>Binary digits of \(\sqrt{2}\)</td><td>not detected</td><td>nothing ([[r2_p1]]; [[r2_p2]])</td></tr>
</tbody>
</table></div>
<p>The Mersenne Twister shows that level 2 adds real sensitivity to the official battery. PCG64, SHA-256 and \(\sqrt{2}\) show that an entirely deterministic sequence can have no detectable signature.</p>

<h3>6. Limitations</h3>
<ul>
<li>A cryptographic-quality generator is indistinguishable: this test rules out a simulation that would use a simple generator, not a carefully built simulation. The SP 800-22 document says so itself: no set of tests replaces cryptanalysis.</li>
<li>Coverage of level 2: a linear generator is detected only if its state has fewer than [[etat_max]] bits; a repetition, only if the period is shorter than the data.</li>
<li>Modest raw volume, and neither of the two raw sources is certified by a loophole-free Bell test.</li>
<li>Excluding the Belem machine is an a posteriori decision; its cause is documented and the raw result published.</li>
<li>The ANU and Beacon datasets measure only the quality of AES-128 and SHA-512.</li>
</ul>

<h3>7. Reproduce</h3>
<p>The data are rebuilt by <code>telecharger.py</code>, which checks their hashes; <code>analyse.py</code> then runs offline in under two minutes, self-tests included.</p>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>J. T. Kavulich, B. P. Van Deren, M. Schlosshauer, <cite>Searching for evidence of algorithmic randomness and incomputability in the output of quantum random number generators</cite>, Physics Letters A 388, 127032 (2021), <a href="https://arxiv.org/abs/2101.01238">arXiv:2101.01238</a>; data: <a href="https://zenodo.org/records/4440318">Zenodo 4440318</a>.</li>
<li>B. P. Van Deren, J. T. Kavulich, M. Schlosshauer, <cite>Parity-based, bias-free optical quantum random number generation with min-entropy estimation</cite>, <a href="https://arxiv.org/abs/2006.11425">arXiv:2006.11425</a>.</li>
<li>O. Root, M. Becker, <cite>Does True Randomness Exist? Efficacy Testing IBM Quantum Computers via Statistical Randomness</cite>, <a href="https://arxiv.org/abs/2401.12250">arXiv:2401.12250</a>; data: <a href="https://doi.org/10.5281/zenodo.10542216">DOI 10.5281/zenodo.10542216</a>.</li>
<li>J. Y. Haw et al., <cite>Maximization of Extractable Randomness in a Quantum Random-Number Generator</cite>, <a href="https://arxiv.org/abs/1411.4512">arXiv:1411.4512</a>.</li>
<li>NIST, <cite>A Reference for Randomness Beacons: Format and Protocol Version 2</cite>, <a href="https://csrc.nist.gov/pubs/ir/8213/ipd">NISTIR 8213</a>.</li>
<li>L. K. Shalm et al., <cite>A strong loophole-free test of local realism</cite>, <a href="https://arxiv.org/abs/1511.03189">arXiv:1511.03189</a>.</li>
<li>NIST, <cite>A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications</cite>, <a href="https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final">SP 800-22 Rev. 1a</a>.</li>
</ol>
""",
}

SYNTHESE = {
    'titre': 'What our research says about the simulation',
    'description': 'Conditional arguments, specific physical models and sensitivity calculations: no measured cosmic probability.',
    'date': 'September 29, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>Have we found proof that our Universe is simulated? No.</strong> We studied arguments and tested specific models. No result examined establishes this conclusion.</p>
<p>This research remains a fundamental branch of Aeternam. It asks about the nature of our world. The <a href="/sujets/reve-temps/">articles on dreaming</a> study the experiences of a human brain. The two can share a philosophical curiosity without sharing their evidence.</p>
<p>Three questions must remain distinct: is a computed world conceivable? Is there an observation that distinguishes it from another world? Can richer or longer dream experiences be built? An answer to one does not settle the others.</p>
<p>A computer need not use a naive cubic grid, a simple random generator or rendering triggered by a conscious observer. Our tests concern some of these architectures. Their failure or their exclusion does not decide the fate of all possible simulations.</p>
<p>We have also withdrawn the presentation of a “7% chance of being simulated” as an Aeternam estimate. This number came from chosen intervals and probabilities. It remains an example of sensitivity to assumptions, with no status as a measurement.</p>
<h2 id="analyse">Detailed analysis</h2>
<h3 id="bostrom">1. What Bostrom’s argument calculates</h3>
<p>The <a href="https://simulation-argument.com/simulation/">2003 argument</a> links the proportion of simulated observers to the number of simulations and to the fractions of civilizations that can and wish to produce them. Under its counting framework, with <em>x</em> the product of these factors, the simulated fraction is:</p>
$$f_{\mathrm{sim}}=\frac{x}{1+x},\qquad x=f_P f_I N_I.$$
<p>The calculation is conditional. Neither the existence of many conscious simulations, nor these parameters, nor our position as a typical observer are measured by the formula. If two hypotheses produce the same observations with the same probability, their likelihood ratio is 1: these observations alone do not decide between them.</p>
<h3>2. Sensitivity of the scenarios</h3>
<p>We integrate this formula over chosen log-uniform distributions, with a logarithmic grid, then compare the calculation with a Monte Carlo. The numerical agreement validates an integration, not the assumptions. The following values are conditional fractions between 0 and 1.</p>
<div class="tableau"><table class="phrases"><thead><tr><th>Illustrative choice</th><th>Model result</th></tr></thead><tbody>
<tr><td>Fractions between 0.1 and 1; number of simulations between a thousand and a billion</td><td>[[conf_genereux]]</td></tr>
<tr><td>Fractions between 10<sup>−10</sup> and 1; number of simulations between 1 and a billion</td><td>[[conf_ignorance]]</td></tr>
<tr><td>Same fractions, number of simulations up to 10<sup>30</sup></td><td>[[conf_n_astro]]</td></tr>
<tr><td>Second scenario, with fewer observers per simulation under another chosen distribution</td><td>[[conf_observateurs]]</td></tr>
<tr><td>Second scenario, weighted by an arbitrary choice of 1/2 on a model of consciousness</td><td>[[conf_aeternam]]</td></tr>
</tbody></table></div>
<p>No row is neutral. Choosing ten orders of magnitude, a billion worlds or a weight of 1/2 expresses a prior. Not knowing imposes none of these values.</p>
<p>Consciousness also requires the model to be specified. If <em>c</em> weights two global possibilities — all simulated beings conscious, or none — our example uses \(c\,x/(1+x)\). If <em>c</em> instead denotes the fraction of simulated individuals who are conscious, the counting would give \(cx/(1+cx)\). These expressions are not interchangeable.</p>
<h3>3. Kipping’s Bayesian result</h3>
<p>In the framework of <a href="https://doi.org/10.3390/universe6080109">Kipping (2020)</a>, two classes of worlds receive prior weights. For the conditioning used in his equation 22, an immense number of simulations is not enough to erase these weights. With our generalization to a weight \(\pi\), the term considered is \(\pi N/(N+1)\).</p>
<p>For the same very large number of simulations, changing \(\pi\) from 1/3 to 1/10 gives [[k_pi_tiers]] and [[k_pi_dixieme]] respectively. This variation comes from the structure of the model. It is not an astrophysical measurement.</p>
<h3>4. Scope of our physical tests</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Analysis</th><th>What is tested</th><th>Scope of the result</th></tr></thead><tbody>
<tr><td><a href="/test-1/">Dispersion of a gamma-ray burst</a></td><td>A specific scheme of propagation on a lattice</td><td>Constraint conditional on the parameters and on the chosen discretization</td></tr>
<tr><td><a href="/test-3/">Eight gamma-ray sources</a></td><td>Directional compatibility of eight published constraints</td><td>Numerically optimized envelope; corrected simultaneous coverage</td></tr>
<tr><td><a href="/test-2/">Cosmic rays</a> and <a href="/test-6/">full sky</a></td><td>A cubic pattern under an exposure model</td><td>No significant detection in the main test; conclusions tied to this pattern</td></tr>
<tr><td><a href="/test-4/">Quantum randomness</a></td><td>Repetitions and structures detectable by the chosen statistics</td><td>Neither a test of every family of generators nor a general certification of unpredictability</td></tr>
<tr><td><a href="/test-5/">Rendering on demand</a></td><td>A formalization of interference visibility</td><td>Disagreement with this formalization; significances conditional on the reconstructed errors</td></tr>
<tr><td><a href="/audit-infodynamique/">Infodynamics</a></td><td>Algebraic steps of proposed proofs</td><td>Counterexamples invalidate these steps, without settling the whole simulation hypothesis</td></tr>
</tbody></table></div>
<p>For the eight gamma-ray sources, the Bonferroni correction must cover the whole family: 1 − 8 × 0.05 = 0.60. Keeping only the three constraints active after optimization wrongly gave 0.85. This minimum coverage remains conditional on the validity of the nominal coverages of each source; it is not a joint analysis at 95%.</p>
<p>For the full sky, the amplitude values rest on a normal approximation and a finite set of orientations. For the interference, the data digitized from the figures and their assumed errors do not justify presenting a combined significance as a universal refutation.</p>
<h3>5. What a null test really changes</h3>
<p>Our simplified updating model assumes that a share <em>w</em> of the simulations considered would have given a signal with certainty, while the others give the same data as the no-simulation hypothesis. In this ideal case only, the Bayes factor of a null result is 1 − <em>w</em>.</p>
<p>A 95% frequentist bound does not say that the probability of an architecture is 5%. A real update would require a likelihood under each model, its sensitivity, its parameters and explicit weights. The tests in the repository do not provide these elements for all simulations.</p>
<h3>6. The program that follows</h3>
<p>A usable lead must state a model, an observable, a different prediction and a test that can fail. Future analyses will have to include the instrumental parameters, multiplicity and competing physical explanations. A reproducible anomaly would be an observation to explain; its existence alone would not attribute it to a simulator.</p>
<p>This research concerns physical models and philosophical arguments. The articles on the brain use their own measures: access, content, duration and memory. A conclusion on one of these subjects does not validate the hypotheses of another.</p>
""",
}

TEMPS_STIMULATION = {
    'titre': 'Changing felt time',
    'description': 'Estimated duration, attention, performance and recall: a reanalysis of the interventions studied.',
    'date': 'September 29, 2026',
    'corps': r"""

<h2 id="explication">Explanation</h2>
<p><strong>Do the interventions examined demonstrate an accelerated conscious life? No.</strong> They show changes in estimated duration and, for some tasks, in performance. These results raise distinct research questions.</p>
<p>A person can judge an event to be longer without better distinguishing rapid images. They can also report more letters after a stimulation without having lived a longer existence. Recall, attention and felt duration must be measured separately.</p>
<p>For Aeternam, the lines of work are time perception, access to dreaming and memory on waking. The <a href="/programme/">current program</a> proceeds by reanalysis and numerical simulation, with no new intervention on a person.</p>
<h2 id="analyse">Detailed analysis</h2>
<h3>A change in judgment</h3>
<p>In the study by <a href="https://doi.org/10.1371/journal.pone.0001295">Stetson et al. (2007)</a>, the ratio between the retrospective duration of one’s own fall and the duration imagined for someone else is [[chute_autrui]]. Relative to the actual duration, it is [[chute_reel]]. The chosen denominator therefore changes what the factor means. Temporal resolution performance does not establish a general acceleration.</p>
<h3>A change in performance</h3>
<p><a href="https://doi.org/10.1080/17470218.2010.502580">Jones, Allely and Wearden (2011)</a> report gains in correctly recalled letters of 3.25% and 5.85% in two conditions. Their arithmetic mean is [[jones_gain]]%. It describes these two gains, without constituting a speed of experience.</p>
<p>Our former calculation reconstructed a standard error of this mean from the <em>F</em> test of another contrast. This operation is not justified by the available summaries alone. The resulting interval is withdrawn.</p>
<h3>Hypnotic accounts, substances and brain stimulation</h3>
<p>Historical accounts can claim very long durations. Without external reference points or verifiable content, their relation to the clock remains a statement. The other studies reviewed concern the reproduction of intervals, attention or learning: we keep their results in their own units. An improvement in memory for learned items does not measure years of additional practice.</p>
<h3>A missing uncertainty stays missing</h3>
<p>The former synthesis sometimes replaced a missing statistical bound with the value 1. A non-significant difference then became proof of the absence of a gain. This treatment is withdrawn. Even complete intervals on different tasks would not make it possible to calculate a universal ceiling on conscious time.</p>
<p><strong>Correction.</strong> The bound “experience per second below 1.09 at 95%” is withdrawn from the results and from their presentation. Its value is now <code>null</code>. We derive from it no numerical gap to the goal of a lifetime in one night.</p>

""",
}

TEMPS_REVE = {
    'titre': 'The time of a dream',
    'description': 'Reported duration, timed tasks and DREAM data: what each measurement allows us to conclude.',
    'date': 'September 29, 2026',
    'corps': r"""

<h2 id="explication">Explanation</h2>
<p><strong>Is an accelerated life already demonstrated by these data? No.</strong> The experiments examined measure judgments of duration or the time needed for certain actions. They do not give a general speed of consciousness.</p>
<p>In the lucid dreams studied by <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3893623/">Erlacher and his colleagues</a>, agreed eye movements delimit a task during sleep. Walking and gymnastics take more time than when awake. This describes these tasks in these experiments.</p>
<p>Our reanalysis of the DREAM database counts [[dream_n]] duration reports. For [[dream_intervalles]] of them, an interval between awakenings could be reconstructed. No report has a duration bound greater than this interval. But a dream felt as two minutes could have occupied one minute inside a thirty-minute interval: our count would not detect it.</p>
<p>The question for Aeternam therefore becomes precise: how can what a person says they experienced be compared with reference points recorded during the dream? The <a href="/programme/#temps">computation program</a> studies this measurement.</p>
<h2 id="analyse">Detailed analysis</h2>
<h3>Three measurements that do not add up</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Experiment</th><th>Observed variable</th><th>Interpretation</th></tr></thead><tbody>
<tr><td>Dement–Kleitman, 1957</td><td>Choice between five and fifteen minutes</td><td>Discrimination of two durations, dependent on the response criterion</td></tr>
<tr><td>Erlacher et al., 2014</td><td>Duration of a task delimited by eye signals</td><td>Temporal performance on this task</td></tr>
<tr><td>DREAM, Tononi series</td><td>Class of duration reported on awakening</td><td>Retrospective estimate, dream onset unknown</td></tr>
</tbody></table></div>
<h3>Why forced choice does not identify an acceleration</h3>
<p>In the log-normal model used previously, a response depends on the ratio between the decision criterion <em>c</em> and the factor <em>F</em>. Multiplying both by ten changes no response probability. The script checks this invariance. Fixing <em>c</em> arbitrarily makes it possible to calculate a conditional <em>F</em>; this does not measure <em>F</em>. The historical sample sizes remain documented as coming from secondary sources, since the original article has not been reread.</p>
<h3>Task durations</h3>
<div class="tableau"><table><thead><tr><th>Task</th><th>Participants</th><th>Awake (s)</th><th>Dream (s)</th></tr></thead><tbody>
<tr><td>Counting</td><td>5</td><td>50.3</td><td>64.0</td></tr>
<tr><td>Walking</td><td>7</td><td>37.7</td><td>57.5</td></tr>
<tr><td>Gymnastics</td><td>8</td><td>6.6</td><td>8.1</td></tr>
</tbody></table></div>
<p>The counting and walking groups overlap. We keep the published means and tests, with no meta-analysis across tasks. A reconstruction of the difference intervals from the paired tests appears in the <a href="/programme/#temps">program</a>.</p>
<h3>DREAM reanalysis</h3>
<p>The script checks the archive’s hash, then links the two tables by recording name. The intervals between awakenings are reconstructed from the times; a gap of more than six hours is treated as a new night. This rule is heuristic. The reports are grouped into classes: they give neither the onset nor the objective duration of an experience. Awakenings of the same person are dependent.</p>
<p><strong>Methodological correction.</strong> The former “global factor” of 0.84 and its bound of 0.92 are withdrawn, as is the frequency bound drawn from the non-detections. They aggregated different measurements and gave them an unjustified scope. The corresponding fields are now <code>null</code>.</p>
<p>Sources: <a href="https://doi.org/10.1038/s41467-025-61945-1">DREAM database</a>, <a href="https://doi.org/10.26180/23306054.v3">Tononi series</a>, <a href="https://doi.org/10.3389/fpsyg.2013.01013">lucid tasks of Erlacher et al.</a></p>

""",
}

ARTICLE_6 = {
    'titre': 'Does the whole sky draw a grid?',
    'description': 'The most energetic cosmic rays seen by the Pierre Auger Observatory in the south and by '
                   'Telescope Array in the north, combined to cover the whole sky and compared with the imprint '
                   'that a cubic grid should leave on them.',
    'date': 'September 28, 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No: the whole sky shows no trace of a cubic grid.</strong> With [[t6_resultats_n_evenements]] cosmic rays covering the entire celestial sphere, [[t6_resultats_p_valeur_l4]]% of the simulated skies without a grid show, after the same search, a cubic pattern at least as pronounced as the real sky.</p>
<p>This “no” has a precise scope. It does not say that there is no grid: it says that a strong cubic pattern is excluded. A flux excess of more than about [[t6_ntations_borne_analytique_exces_axes_max]]% along the axes of the cube, or of more than about [[t6_ns_borne_analytique_exces_diagonales_max]]% along its diagonals, exceeds our approximate 95% bound in the orientations studied: this is about three times better than test No. 2. One control, which adds Auger’s lower-energy events, goes down to p = [[t6_variantes_n_maximal_p_valeur_l4]]; we followed it through to the end: it is mostly due to the two astrophysical excesses already known, is no longer significant after they are removed (p = [[t6_ntes_n_maximal_exces_masques_p_valeur_l4]]) and does not reproduce significantly on independent events (see the analysis, § 7).</p>
</section>

<h2 id="explication">Explanation</h2>
<p>If our world were computed by a computer, space might be divided into tiny cubes, the way an image is made of pixels. In 2012, three physicists noted that such a division would leave a trace: the most energetic particles in the Universe would not arrive in the same way from all directions. Some directions would be favored, arranged like the faces or like the corners of a cube.</p>
<p>Test No. 2 looked for this trace in the [[t6_test2_meme_methode_n_evenements]] most energetic particles captured by the Pierre Auger Observatory, in Argentina. It found nothing, but it had two weaknesses: an observatory in the southern hemisphere does not see the far northern sky, and 100 particles can only reveal a very strong pattern.</p>
<p>We therefore combined two observatories. Auger, in the south, has published the list of its [[t6_donnees_auger_n_liste]] most energetic particles, captured from 2004 to 2020. Telescope Array, in Utah, in the north, has published the list of its [[t6_donnees_telescope_array_n]] most energetic, captured from 2008 to 2013. The two observatories do not measure energy in quite the same way; their teams have jointly published the rule for converting from one scale to the other. Using this rule, we kept from the Auger list the particles with energies comparable to those of Telescope Array. [[t6_resultats_n_auger]] remain, giving [[t6_resultats_n_evenements]] in total, ten times more than in test No. 2, and this time over the whole sky.</p>
<p>The method is that of test No. 2. We try [[t6_methode_orientations]] positions of the cube and keep the one that best fits the data. Then we generate [[t6_methode_ciels_isotropes]] fake skies without a grid, seen by the same observatories, and repeat exactly the same search on each. In [[t6_resultats_p_valeur_l4]]% of them, the best cube fits at least as well as on the real sky. The real sky therefore cannot be told apart from the fake skies: no grid is detected.</p>
<p>We then checked that this result does not depend on our choices: a different energy conversion rule, only the most energetic particles, exposure computed differently, and so on. One control stands out: when all of Auger’s lower-energy particles are added, a cube seems to fit better than almost all the fake skies. We looked into why, without presuming anything.</p>
<p>Cosmic rays are known to arrive in excess from two regions of the sky: one around the galaxy Centaurus A, seen by Auger, the other in the northern sky, seen by Telescope Array. These are astronomical sources, not cubes. Yet already in the main sample, the best-fitting cube places precisely two of its corners about ten degrees from these two regions. When these two regions are removed from the sky, the pattern weakens markedly and is no longer significant. Above all, a real grid should show up, with the same orientation, in different batches of particles. We chose the best cube using only the low-energy particles, then checked whether it also fits the others, which played no part in that choice: it fits a little, but not enough to stand out from chance, and even less once the two regions are removed. Finally, the prediction concerns the most energetic particles, the least deflected along the way; the opposite is observed, with the pattern coming from the least energetic. This control therefore does not show a grid, but mainly these two clusters of particles, which the nearest cube was trying to catch.</p>
<p>What this test shows: where we could look, that is, over the whole sky and with ten times more particles, there is no strong cubic pattern. What it does not show: that there is no grid at all. A weak pattern would still go unnoticed, and the magnetic fields of our galaxy deflect these particles along the way, which would blur part of the trace.</p>
<h2 id="analyse">Detailed analysis</h2><p>The amplitudes reported rest on a normal approximation, a finite grid of amplitudes and a finite scan of orientations. The available Monte Carlo checks do not certify uniform coverage over the continuum of parameters.</p>
<h3>1. The prediction</h3>
<p>On a cubic lattice, any effect of the grid on the arrival directions is a function of the direction \(\mathbf n\) that is invariant under the cube group \(O_h\). Spherical harmonics invariant under \(O_h\) exist only for \(\ell=0,4,6,8,\dots\): the first allowed anisotropy is the cubic harmonic \(\ell=4\), proportional to \(Q-3/5\), with</p>
$$Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>Beane, Davoudi and Savage (arXiv:1210.1847) write that a lattice simulation could reveal itself in the highest-energy cosmic rays through a breaking of rotational symmetry that reflects the grid. Main test fixed in advance: \(\ell=4\); secondary tests: \(\ell=6\) and \(\ell=4+6\). Method, statistic, orientations and seed are those of test No. 2.</p>
<h3>2. The data</h3>
<p><strong>South.</strong> Pierre Auger Collaboration, ApJ 935, 170 (2022): complete public list of the [[t6_donnees_auger_n_liste]] events with energy greater than or equal to [[t6_donnees_auger_energie_min_liste_eev]]EeV (from January 1, 2004 to December 31, 2020, zenith up to 80°), of which [[t6_donnees_auger_n_verticaux_liste]] are “vertical” (zenith \(\lt\) 60°) and the others “inclined” (60° to 80°), figures identical to those of the paper (sources.md, § 2). Maximum energy: [[t6_donnees_auger_energie_max_eev]] EeV. The 100 events of test No. 2 are all in this list (checked, sources.md, § 2).</p>
<p><strong>North.</strong> Telescope Array Collaboration, ApJL 790, L21 (2014), table 1: the [[t6_donnees_telescope_array_n]] events with energy above [[t6_etalonnage_seuil_ta_eev]]EeV and zenith \(\lt\) 55°, from May 11, 2008 to May 4, 2013, from [[t6_donnees_telescope_array_energie_min_eev]] to [[t6_donnees_telescope_array_energie_max_eev]] EeV, declinations down to [[t6_nees_telescope_array_declinaison_min_deg]]° in the south. This is the only list of Telescope Array events published with their coordinates (sources.md, § 1); the more recent datasets used in the joint Auger-TA analyses are not public.</p>
<p>The SHA-256 hashes of all files are checked at every run. As the Telescope Array table is under the publisher’s copyright, it is not redistributed: the script downloads it and checks the hash of the file and that of the list as read (sources.md, § 3).</p>
<h3>3. Putting the two energies on the same scale</h3>
<p>The joint Auger-TA working group cross-calibrates the energies by comparing the fluxes in the band of sky seen by both observatories:</p>
$$\frac{E_{\mathrm{Auger}}}{10\ \mathrm{EeV}}=e^{\alpha}\left(\frac{E_{\mathrm{TA}}}{10\ \mathrm{EeV}}\right)^{\beta},$$
<p>with \(\alpha\) = [[t6_etalonnage_principal_alpha]] and \(\beta\) = [[t6_etalonnage_principal_beta]], values published precisely for this Telescope Array selection (arXiv:2507.10441, p. 3; sources.md, § 5). The 57 EeV threshold of Telescope Array is therefore equivalent to [[t6_etalonnage_seuil_auger_equivalent_eev]] EeV on the Auger scale. The main sample combines the Auger events of at least this energy and the 72 TA events:</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Batch</th><th>Latitude</th><th>Zenith</th><th>Events</th></tr></thead>
<tbody>
<tr><td>Auger vertical</td><td>[[t6_methode_lots_0_latitude_deg]]°</td><td>0-60°</td><td>[[t6_resultats_n_auger_verticaux]]</td></tr>
<tr><td>Auger inclined</td><td>[[t6_methode_lots_1_latitude_deg]]°</td><td>60-80°</td><td>[[t6_resultats_n_auger_inclines]]</td></tr>
<tr><td>Telescope Array</td><td>[[t6_methode_lots_2_latitude_deg]]°</td><td>0-55°</td><td>[[t6_resultats_n_ta]]</td></tr>
<tr><td>Total</td><td></td><td></td><td>[[t6_resultats_n_evenements]]</td></tr>
</tbody>
</table></div>
<h3>4. Exposure, batch by batch</h3>
<p>A ground-based detector at latitude \(a_0\), accepting zenith angles \(\theta\le\theta_m\), has an exposure that is uniform in right ascension and, in declination \(\delta\) (Sommers, 2001),</p>
$$\omega_{\theta_m}(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>For a zenith band \([\theta_1,\theta_2]\), \(\omega=\omega_{\theta_2}-\omega_{\theta_1}\). At these energies, the detection efficiency is full and the exposure purely geometric (arXiv:1404.5890 p. 6 for TA; Auger exposure code published with the data; sources.md, § 2 and 3).</p>
<p>Each batch \(d\) keeps its exposure \(\omega_d\), and its number of events \(N_d\) is held fixed in the simulations: we condition on it, as Auger does for its vertical and inclined batches. The test then depends neither on the absolute exposures of the two observatories nor on the energy-scale offset beyond the choice of thresholds. Auger sees up to declination +[[t6_methode_declinaison_max_auger_deg]]°, Telescope Array down to [[t6_methode_declinaison_min_ta_deg]]°: the whole sky is covered (visible fraction [[t6_methode_fraction_du_ciel_visible]], against [[t6_t2_meme_methode_fraction_du_ciel_visible]]% in test No. 2); [[t6_ethode_fraction_du_ciel_vue_par_les_deux]]% of the sphere is seen by both, [[t6_methode_fraction_du_ciel_vue_par_ta_seul]]% by Telescope Array alone.</p>
<h3>5. The statistic</h3>
<p>Let \(R\) be an orientation of the grid, with rows \(\mathbf e_k\), and \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). Extended to the batches:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-\sum_d N_d\,\langle f\rangle_{\omega_d}}{\sqrt{\sum_d N_d\,\mathrm{Var}_{\omega_d} f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>where \(\langle\cdot\rangle_{\omega_d}\) is the mean over an isotropic sky seen by batch \(d\), computed exactly by Gauss-Legendre quadrature on the 15 monomials of degree 4. \(T\gt0\) signals an excess along the axes of the cube, \(T\lt0\) along its diagonals. The maximum is taken over the [[t6_methode_orientations]] orientations of test No. 2 (same seed, [[t6_methode_graine]]). For \(\ell=6\): \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha_6\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\), with \(\alpha_6=-15/11\) ≈ [[t6_methode_fonction_l6_alpha]], orthogonal to \(\ell=4\); the combined test maximizes \(T_4^{2}+T_6^{2}\).</p>
<p>The p-value, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), comes from n = [[t6_methode_ciels_isotropes]] isotropic skies drawn batch by batch and put through the same maximization: it includes the cost of choosing the orientation. Under isotropy, \(Z_4\) has a median of [[t6_resultats_seuils_z4_isotrope_0_5]]; it exceeds [[t6_resultats_seuils_z4_isotrope_0_95]] in 5% of cases, [[t6_resultats_seuils_z4_isotrope_0_99]] in 1% and [[t6_resultats_seuils_z4_isotrope_0_999]] in 0.1%.</p>
<h3>6. Result</h3>
<div class="tableau"><table class="phrases">
<thead><tr><th>Test</th><th>Observed statistic</th><th>p-value</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (main)</td><td>\(Z_4\) = [[t6_resultats_z4_observe]]</td><td>[[t6_resultats_p_valeur_l4_41]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\) = [[t6_resultats_z6_observe]]</td><td>[[t6_resultats_p_valeur_l6]]</td></tr>
<tr><td>\(\ell=4\) and \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\) = [[t6_resultats_z46_observe]]</td><td>[[t6_resultats_p_valeur_l4_l6]]</td></tr>
</tbody>
</table></div>
<p>No test goes below 0.05. At the best orientation, \(T_4\) = [[t6_resultats_meilleure_orientation_t4]]: the deviation points toward the diagonals. The mean of \(Q\) there is [[t6_resultats_q_moyen_observe]] against [[t6_resultats_q_moyen_attendu_isotrope]] expected, i.e. [[t6_resultats_ecart_relatif_q]]%. This orientation is [[t6_meilleure_orientation_ecart_au_test2_deg]]° (up to the cube group) from the best orientation of test No. 2: the “best grid” is not stable from one sample to another, as expected from noise.</p>
<p>Batch by batch, at this same orientation: \(T_4\) = [[t6_lot_meilleure_orientation_auger_vertical]] for Auger vertical, [[t6_lot_meilleure_orientation_auger_inclin]] for Auger inclined, [[t6_ot_meilleure_orientation_telescope_array]] for Telescope Array. These values are taken at the orientation chosen on the full sample: they are not independent tests.</p>
<p><strong>Where does the deviation come from?</strong> In cones of [[t6_methode_rayon_cones_deg]]° around the eight diagonals of the best orientation, we observe [[t6_ure_orientation_diagonales_observe_total]] events against [[t6_ure_orientation_diagonales_attendu_total]] expected. The excess is concentrated in two cones: [[t6_e_orientation_diagonales_cones_5_observe]] observed against [[t6_e_orientation_diagonales_cones_5_attendu]] expected around the diagonal pointing toward ([[t6_re_orientation_diagonales_cones_5_ra_deg]]°; [[t6_e_orientation_diagonales_cones_5_dec_deg]]°), [[t6_gonales_cones_5_distance_centaurus_a_deg]]° from Centaurus A; [[t6_e_orientation_diagonales_cones_3_observe]] against [[t6_e_orientation_diagonales_cones_3_attendu]] around ([[t6_re_orientation_diagonales_cones_3_ra_deg]]°; [[t6_e_orientation_diagonales_cones_3_dec_deg]]°), [[t6_ales_cones_3_distance_point_chaud_ta_deg]]° from the Telescope Array hotspot. The other six diagonals show nothing of the kind. These are the two astrophysical excesses published by the collaborations themselves: around Centaurus A, 215 events observed against 152.0 expected in a 27° circle above 38 EeV (arXiv:2206.13492 p. 11); the TA hotspot, 19 observed against 4.49 expected in a 20° circle (arXiv:1404.5890 p. 7).</p>
<h3>7. Controls</h3>
<p>Nine variants fixed before the computation ([[t6_methode_ciels_par_variante]] isotropic skies each), then four added afterwards, and flagged as such, to understand the “maximal N” variant:</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Variant</th><th>N</th><th>\(Z_4\)</th><th>p (\(\ell=4\))</th></tr></thead>
<tbody>
<tr><td>Main</td><td>[[t6_resultats_n_evenements]]</td><td>[[t6_resultats_z4_observe]]</td><td>[[t6_resultats_p_valeur_l4_41]]</td></tr>
<tr><td>Auger alone, same threshold</td><td>[[t6_variantes_auger_seul_n_evenements]]</td><td>[[t6_variantes_auger_seul_z4_observe]]</td><td>[[t6_variantes_auger_seul_p_valeur_l4]]</td></tr>
<tr><td>Highest energies (Auger ≥ 78 EeV, TA ≥ [[t6_nnage_seuil_ta_equivalent_a_78_eev_auger]] EeV)</td><td>[[t6_variantes_hautes_energies_n_evenements]]</td><td>[[t6_variantes_hautes_energies_z4_observe]]</td><td>[[t6_variantes_hautes_energies_p_valeur_l4]]</td></tr>
<tr><td>ICRC 2021 calibration (Auger threshold [[t6_uils_auger_selon_etalonnage_eev_icrc2021]] EeV)</td><td>[[t6_riantes_etalonnage_icrc2021_n_evenements]]</td><td>[[t6_variantes_etalonnage_icrc2021_z4_observe]]</td><td>[[t6_ariantes_etalonnage_icrc2021_p_valeur_l4]]</td></tr>
<tr><td>Strict ICRC 2025 calibration (threshold [[t6_ger_selon_etalonnage_eev_icrc2025_strict]] EeV)</td><td>[[t6_etalonnage_icrc2025_strict_n_evenements]]</td><td>[[t6_es_etalonnage_icrc2025_strict_z4_observe]]</td><td>[[t6_s_etalonnage_icrc2025_strict_p_valeur_l4]]</td></tr>
<tr><td>Auger exposure as a single block</td><td>[[t6_variantes_auger_un_bloc_n_evenements]]</td><td>[[t6_variantes_auger_un_bloc_z4_observe]]</td><td>[[t6_variantes_auger_un_bloc_p_valeur_l4]]</td></tr>
<tr><td>With the Amaterasu event (244 EeV, 2021)</td><td>[[t6_variantes_avec_amaterasu_n_evenements]]</td><td>[[t6_variantes_avec_amaterasu_z4_observe]]</td><td>[[t6_variantes_avec_amaterasu_p_valeur_l4]]</td></tr>
<tr><td>Centaurus A and TA hotspot removed</td><td>[[t6_variantes_exces_masques_n_evenements]]</td><td>[[t6_variantes_exces_masques_z4_observe]]</td><td>[[t6_variantes_exces_masques_p_valeur_l4]]</td></tr>
<tr><td>Without scale correction (Auger ≥ 57 EeV)</td><td>[[t6_variantes_sans_correction_n_evenements]]</td><td>[[t6_variantes_sans_correction_z4_observe]]</td><td>[[t6_variantes_sans_correction_p_valeur_l4]]</td></tr>
<tr><td>Maximal N (Auger ≥ 32 EeV, TA > 57 EeV)</td><td>[[t6_variantes_n_maximal_n_evenements]]</td><td>[[t6_variantes_n_maximal_z4_observe]]</td><td>[[t6_variantes_n_maximal_p_valeur_l4]]</td></tr>
<tr><td><cite>Post hoc:</cite> maximal N, Auger alone</td><td>[[t6_iantes_n_maximal_auger_seul_n_evenements]]</td><td>[[t6_ariantes_n_maximal_auger_seul_z4_observe]]</td><td>[[t6_riantes_n_maximal_auger_seul_p_valeur_l4]]</td></tr>
<tr><td><cite>Post hoc:</cite> maximal N, excesses removed</td><td>[[t6_tes_n_maximal_exces_masques_n_evenements]]</td><td>[[t6_antes_n_maximal_exces_masques_z4_observe]]</td><td>[[t6_ntes_n_maximal_exces_masques_p_valeur_l4]]</td></tr>
<tr><td><cite>Post hoc:</cite> Auger 32 to 44.88 EeV alone</td><td>[[t6_variantes_auger_32_a_seuil_n_evenements]]</td><td>[[t6_variantes_auger_32_a_seuil_z4_observe]]</td><td>[[t6_variantes_auger_32_a_seuil_p_valeur_l4]]</td></tr>
<tr><td><cite>Post hoc:</cite> Auger 32 to 44.88 EeV, excesses removed</td><td>[[t6_er_32_a_seuil_exces_masques_n_evenements]]</td><td>[[t6_uger_32_a_seuil_exces_masques_z4_observe]]</td><td>[[t6_ger_32_a_seuil_exces_masques_p_valeur_l4]]</td></tr>
</tbody>
</table></div>
<p>Two planned variants go below 0.05: “without correction” ([[t6_variantes_sans_correction_p_valeur_l4]]) and above all “maximal N” ([[t6_variantes_n_maximal_p_valeur_l4]]). We dug into them; neither calls the verdict into question.</p>
<ol>
<li><strong>These are controls, not the test.</strong> The main test was fixed in advance. Over nine planned variants, the probability that at least one goes down to 0.008 by chance is bounded by \(9\times0{,}008\approx0{,}07\) (Bonferroni); since the variants are highly correlated with one another, this bound is conservative but not wrong.</li>
<li><strong>The signal comes from the lowest energies, and from the south.</strong> Auger alone, from 32 EeV, already gives p = [[t6_riantes_n_maximal_auger_seul_p_valeur_l4]]; the Auger events from 32 to 44.88 EeV alone, which are absent from the main sample, give p = [[t6_variantes_auger_32_a_seuil_p_valeur_l4]]. At the highest energies, where the prediction of Beane, Davoudi and Savage applies and where magnetic deflections are smallest, nothing: p = [[t6_variantes_hautes_energies_p_valeur_l4]]. A grid would give the opposite profile.</li>
<li><strong>It follows the known excesses.</strong> With Centaurus A and the TA hotspot removed, using the circles published by the collaborations: “maximal N” rises to p = [[t6_ntes_n_maximal_exces_masques_p_valeur_l4]], the 32-44.88 EeV slice to p = [[t6_ger_32_a_seuil_exces_masques_p_valeur_l4]], the main sample to p = [[t6_variantes_exces_masques_p_valeur_l4]].</li>
<li><strong>It does not reproduce significantly.</strong> Reproduction test: we choose the best orientation using only the Auger events from 32 to 44.88 EeV (\(T_4\) = [[t6_duction_par_energie_sans_masque_t4_choix]]), then compute \(T_4\) at this fixed orientation in the main sample, which shares no event with them. At fixed orientation, \(T_4\) follows a standard normal distribution under isotropy (self-test). We obtain \(T_4\) = [[t6_4_echantillon_principal_meme_orientation]], i.e. p = [[t6_energie_sans_masque_p_bilaterale_normale]] (two-sided): same sign, but not significant. Excesses removed: \(T_4\) = [[t6_4_echantillon_principal_meme_orientation_111]], p = [[t6_ergie_exces_masques_p_bilaterale_normale]]. The weak agreement that remains is compatible with the same astrophysical anisotropy seen at two neighboring energies.</li>
<li><strong>A dipole does not explain everything, and it does not need to.</strong> We also simulated skies carrying the dipole fitted to the data, rather than isotropic skies (amplitude [[t6_s_coup_nul_dipolaire_n_maximal_amplitude]] for “maximal N”): the p-value hardly changes, [[t6_olaire_n_maximal_p_valeur_l4_sous_dipole]] ([[t6_olaire_principal_p_valeur_l4_sous_dipole]] for the main test). The anisotropy that matters here is not the large-scale anisotropy, but the intermediate-scale excesses of Centaurus A and the hotspot, whose removal brings all the p-values back above 0.05.</li>
<li><strong>“Without correction”</strong> compares Auger above 57 EeV on its own scale with TA above 57 EeV on its own, whereas the joint calibration matches 57 EeV of TA to [[t6_etalonnage_seuil_auger_equivalent_eev]] EeV of Auger: the ratio of the fluxes between north and south is then distorted. With the three published calibrations we tested, p stays between [[t6_resultats_p_valeur_l4_41]] and [[t6_s_etalonnage_icrc2025_strict_p_valeur_l4]].</li>
</ol>
<p>Summary: the only notable deviation in the controls is carried by lower-energy events, is concentrated near the two known astrophysical excesses, vanishes when they are removed and does not reproduce significantly on an independent sample. This is not the signature of a grid.</p>
<h3>8. What the test could see</h3>
<p>We inject a cubic pattern: density proportional to \(\omega_d(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Along an axis (\(Q=1\)) the flux is \(1+\varepsilon\) times the mean; along a diagonal (\(Q=1/3\)), \(1-2\varepsilon/3\). With \(\varepsilon\gt0\), the excess lies on the axes; with \(\varepsilon\lt0\), on the diagonals, and it equals \(2\lvert\varepsilon\rvert/3\). Upper limits at 95%, three conventions:</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Convention</th><th>Axes: \(\varepsilon\le\)</th><th>Diagonals: \(\lvert\varepsilon\rvert\le\)</th><th>Test No. 2, same convention (axes / diagonals)</th></tr></thead>
<tbody>
<tr><td>Orientation drawn at random for each sky ([[t6_methode_ciels_par_amplitude]] skies per amplitude)</td><td>[[t6_95_moyenne_orientations_epsilon_axes_max]]</td><td>[[t6_enne_orientations_epsilon_diagonales_max]]</td><td>[[t6_test2_meme_methode_limite_moyenne_axes]] / [[t6_2_meme_methode_limite_moyenne_diagonales]]</td></tr>
<tr><td>Worst of 16 fixed orientations, including the least visible ([[t6_ode_ciels_par_amplitude_orientation_fixe]] skies per point)</td><td>[[t6_5_pire_orientation_fixe_epsilon_axes_max]]</td><td>[[t6_orientation_fixe_epsilon_diagonales_max]]</td><td>[[t6_2_meme_methode_pire_16_orientations_axes]] / [[t6_methode_pire_16_orientations_diagonales]]</td></tr>
<tr><td>Worst of the 20,000 orientations, analytical bound</td><td>[[t6_orientations_borne_analytique_axes_pire]]</td><td>[[t6_tations_borne_analytique_diagonales_pire]]</td><td>[[t6_hode_borne_toutes_orientations_axes_pire]] / [[t6_orne_toutes_orientations_diagonales_pire]]</td></tr>
</tbody>
</table></div>
<p>The analytical bound rests on \(Z_4\ge\lvert T(R_0)\rvert\): if the sky carries the pattern at orientation \(R_0\), it is enough for \(\lvert T(R_0)\rvert\) to exceed \(Z_4^{\mathrm{obs}}\) with a probability of at least 95%. \(T(R_0)\) is a sum of \(N\) independent terms, normally distributed to a very good approximation, whose mean and variance under the signal can be computed exactly:</p>
$$\mathbb E_\varepsilon[f]_d=\frac{\langle f\rangle_{\omega_d}+\varepsilon\,\langle f g\rangle_{\omega_d}}{1+\varepsilon\,\langle g\rangle_{\omega_d}},\qquad g=\frac{5Q(R_0\mathbf n)-3}{2},$$
<p>and likewise for \(\mathbb E_\varepsilon[f^{2}]_d\). The construction ignores the gain from the maximum, but its coverage relies on a normal approximation: for each of the 16 fixed orientations, it lies above the simulated limit. Self-test: at \(\varepsilon=0{,}3\) and at a given orientation, analytical mean [[t6_s_borne_contre_mc_0_3_moyenne_analytique]] against [[t6_autotests_borne_contre_mc_0_3_moyenne_mc]] simulated.</p>
<p>In terms of flux: <strong>an excess of more than about [[t6_ntations_borne_analytique_exces_axes_max]]% along the axes, or of more than about [[t6_ns_borne_analytique_exces_diagonales_max]]% along the diagonals, exceeds the approximate 95% bound over the scan of orientations.</strong> The gain over test No. 2 is a factor of [[t6_comparaison_gain_pire_orientation_axes]] toward the axes and [[t6_araison_gain_pire_orientation_diagonales]] toward the diagonals, for [[t6_comparaison_rapport_n]] times more events, close to the factor \(\sqrt{10{,}2}\approx3{,}2\) expected from a sensitivity scaling as \(1/\sqrt N\).</p>
<h3>9. Self-tests</h3>
<p>The script first checks its own pipeline: published counts and bounds of the two lists; energy correspondences printed in the four calibration papers; invariance of \(Q\) under the cube group and exact polynomial expansion; \(\ell=6\) orthogonal to \(\ell=4\); limits of the visible skies (Auger +44.8°, TA −15.7°) and sum of the vertical and inclined bands; agreement between quadrature and large random draws, masks included; \(T\) standardized under isotropy; analytical moments equal to the Monte Carlo ones; finally, a clear cubic pattern injected over the whole sky is detected and its orientation recovered to within [[t6_utotests_orientation_retrouvee_ecart_deg]]°.</p>
<h2 id="limites">Limitations</h2>
<ul>
<li>Cosmic rays are charged: magnetic fields deflect their directions, all the more so for heavier nuclei. The pattern sought is broad (an axis and a diagonal are separated by \(\arccos(1/\sqrt3)\approx54{,}7^\circ\)) and withstands modest deflections, but an imprint fixed at the source or along the way would be partly erased.</li>
<li>The north carries little weight: [[t6_resultats_n_ta]] TA events against [[t6_resultats_n_auger]] for Auger. The only Telescope Array list published with coordinates stops in 2013; the richer datasets of the joint analyses are not public.</li>
<li>The cross-calibration of energies has an uncertainty: each observatory states ±14% (Auger) and ±21% (TA) on its absolute scale (arXiv:2507.10441 p. 3). The published calibration variants do not change the result; the absence of any correction does change it (p = [[t6_variantes_sans_correction_p_valeur_l4]]), for the reason given in § 7.</li>
<li>Astrophysical anisotropies (the Centaurus A and TA hotspot excesses, and more generally any large-scale anisotropy) partly project onto \(\ell=4\) through non-uniform exposures. The test models none of them; it removes them only in the masked-excess variants, using the circles published by the collaborations, not fitted by us. A positive result would have required excluding them; the negative verdict does not depend on them.</li>
<li>Four variants, the reproduction test and the dipole skies were added after seeing the “maximal N” variant; they serve to explain it, not to build the verdict. The reproduction test remains weak: the main sample contains only [[t6_resultats_n_evenements]] events.</li>
<li>The deviation of the “maximal N” variant is not explained by a complete physical model: we show that it follows the known excesses and that it does not reproduce, without modeling these excesses themselves.</li>
<li>The grid is assumed to be fixed relative to the distant stars. A grid moving or rotating relative to them would require a different test.</li>
<li>No probability of being simulated is computed: the test concerns one precise signature, that of a cubic grid.</li>
</ul>
<h2>Sources</h2>
<ul>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, “Constraints on the Universe as a Numerical Simulation”, arXiv:1210.1847 (2012).</li>
<li>Pierre Auger Collaboration, “Arrival Directions of Cosmic Rays above 32 EeV from Phase One of the Pierre Auger Observatory”, ApJ 935, 170 (2022), arXiv:2206.13492; data DOI 10.5281/zenodo.6504276.</li>
<li>Telescope Array Collaboration, “Indications of Intermediate-Scale Anisotropy of Cosmic Rays with Energy Greater Than 57 EeV in the Northern Sky”, ApJL 790, L21 (2014), arXiv:1404.5890.</li>
<li>Telescope Array Collaboration, “An extremely energetic cosmic ray observed by a surface detector array”, Science 382, 903 (2023), arXiv:2311.14231; data DOI 10.5281/zenodo.8427755.</li>
<li>A. Gálvez Ureña for the Auger and TA collaborations, ICRC 2025, arXiv:2507.10441; A. di Matteo et al., ICRC 2021, arXiv:2111.12366; UHECR 2022 report, arXiv:2302.04502.</li>
<li>P. Sommers, “Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory”, Astropart. Phys. 14, 271 (2001), arXiv:astro-ph/0004016.</li>
</ul>
""",
}

ARTICLE_5 = {
    'titre': 'Does the world wait for us to look at it?',
    'description': 'An economical simulation would compute details only at the moment an observer can know them. '
                   'Six published interference experiments say otherwise: the fringes disappear as soon as the '
                   'information exists, whether or not anyone reads it.',
    'date': 'September 28, 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No: this reanalysis does not provide evidence of rendering controlled by a conscious observer.</strong> The experiments examined constrain the HR formalization chosen in our script. The figures in standard deviations below are conditional diagnostics: reconstructed errors, digitized points and assumed independence. They do not constitute a universal refutation of simulation.</p>
</section>

<h2 id="explication">Explanation</h2>
<p>A simulation is often credited with the video-game trick: draw only what the player is looking at. Nick Bostrom mentions it in his 2025 FAQ: some details would only be “filled in” when someone looks at them or does an experiment. Proponents of the hypothesis, Tom Campbell and three coauthors, derived from it a prediction that can be checked. In the double-slit experiment, a particle sent toward two slits produces fringes (alternating bright and dark bands on the screen), like a wave that passes through both at once. If we learn which slit it went through, the fringes disappear. According to them, what matters is not that a device has detected this passage, but that an observer can know it. As long as the information is neither read nor recorded anywhere, the simulation would not have had to compute it, and the fringes should remain.</p>
<p>Ordinary physics says something else: the fringes disappear as soon as a trace of the passage exists somewhere in nature, even if no one will ever look at it. The two ideas therefore give opposite predictions in one precise case: a trace that is present, but never read.</p>
<p>This case has been realized several times, although that was not the aim of the experiments, and the results are published. We extracted the digitized estimates from the figures of the papers and redid the calculations:</p>
<ul>
<li>at Los Alamos, in 1999, the visibility of the fringes was measured with the which-path information present in the light, but with no instrument to read it. The fringes fade exactly as ordinary physics predicts, down to only [[t5_schwindt1999_v_45deg]]% of their sharpness; on-demand rendering predicted about [[t5_schwindt1999_v0]]%. In a second series, the information was read: the amount read and the loss of the unread fringes fit together exactly;</li>
<li>in Brazil, in 2002, in a true double-slit experiment, the trace of the passage was written into the light and no one analyzed it: the fringes drop to [[t5_born2002_test_hr_fig3_sur_fig2_rapport_v]]% of their initial sharpness, as in an experiment where the information is read ([[t5_kim2000_rapport_v_r03_sur_r01]]%, non-significant difference);</li>
<li>in Vienna, in 2003 and 2004, large molecules lose their fringes because gas molecules collide with them, or because they emit thermal light. These gas molecules and this light are detected by no one and are lost in the apparatus. The fringes disappear anyway, in the proportion calculated in advance.</li>
</ul>
<p>The result is clear: nature behaves as if the information counts as soon as it exists, whether or not an observer can know it. One loophole remains: a simulation that computed everything as soon as information exists somewhere would produce exactly what we see. But it would then make no observer-related savings, and it would be in no way distinguishable from ordinary physics. This test therefore finds no trace of simulation.</p>
<h2 id="analyse">Detailed analysis</h2>
<h3>1. The hypothesis tested and its prediction</h3>
<p>Campbell, Owhadi, Sauvageau and Watkinson (arXiv:1703.00058, § 4) posit that the observed pattern is determined “by the existence and availability of the which-way data when the pattern is observed”, availability being defined by recording on an objective medium (§ 4.2). Their proposed experiment consists in detecting the which-path information without recording it: the screen “should display the wave pattern if the experiment is successful”. We call HR (on-demand rendering) the following prediction: if the which-path information is neither read nor recorded, the visibility remains that of the interferometer without marking, \(V = V_0\).</p>
<h3>2. The quantum prediction, without an observer</h3>
<p>For a particle whose two paths are correlated with states \(|M_1\rangle\), \(|M_2\rangle\) of a marker, quantum mechanics gives, for equiprobable paths and a pure marker,</p>
$$V = |\langle M_1|M_2\rangle|, \qquad D = \sqrt{1-|\langle M_1|M_2\rangle|^2},$$
<p>hence \(D^2 + V^2 = 1\), and in general (mixed marker) Englert’s inequality (Phys. Rev. Lett. 77, 2154, 1996)</p>
$$D^2 + V^2 \le 1,$$
<p>where \(D\) is the distinguishability, that is, the best knowledge of the path that a measurement of the marker <cite>could</cite> provide. Nothing in these formulas depends on what is done with the marker afterwards: \(V\) is set by the overlap of the marker states, read or not. <code>analyse.py</code> checks the inequality and the equality case on 900 random states, and the equality on 300 pure markers, in dimensions 2, 3 and 5 (self-test). The full text of Englert (1996) is paywalled and has not been read; the inequality is taken from Schwindt, Kwiat and Englert (1999), eq. (1), of which Englert is a coauthor.</p>
<h3>3. Data</h3>
<p>The data points are extracted by <code>extraire.py</code> from the vector drawings of the arXiv PDFs: each data marker there is an object whose coordinates are exact, calibrated on the tick marks (largest deviation of a tick mark from the calibration line: [[t5_residu_etalonnage_max_pt_toutes_figures]] pt). Checks: for Schwindt et al., the mean of the extracted \(V^2+K^2\) is [[t5_controle_extraction_moyenne_v2k2_relevee]] against 0.976 printed; for Walborn et al., the extracted error bars are on average, figure by figure, between [[t5_e_releve_erreur_sur_racine_n_moyenne_min]] and [[t5_e_releve_erreur_sur_racine_n_moyenne_max]] times \(\sqrt N\), the Poisson law expected for counts. The uncertainties on the fitted visibilities come from a parametric bootstrap (300 draws), multiplied by \(\sqrt{\chi^2/\text{dof}}\) when this ratio exceeds 1.</p>
<h3>4. Test (a): is the inequality respected?</h3>
<p><strong>Schwindt, Kwiat and Englert (1999), fig. 2.</strong> Single photon in a Mach-Zehnder interferometer; a half-wave plate rotated by an angle \(\theta\) marks the path through polarization. Over the seven angles, \(V^2+K^2\) (knowledge \(K\) measured in the optimal basis, hence \(K = D\) up to imperfections) never exceeds 1: maximum [[t5_schwindt1999_v2_plus_k2_max]], i.e. [[t5_schwindt1999_z_max_au_dessus_de_1]] standard deviation above 1 at worst. The quantum prediction without an observer, \(V = V_0|\cos 2\theta|\) and \(D = |\sin 2\theta|\) with \(V_0\) = [[t5_schwindt1999_v0_14]] (visibility at \(\theta = 0\)), describes K to within [[t5_schwindt1999_ecart_max_k_moins_d_mq]] and V to within [[t5_schwindt1999_ecart_max_v_moins_v_mq]]; the largest deviation is the residual visibility at 45°, which the authors attribute to slight polarization transformations in the mirrors.</p>
<p><strong>Ma et al. (2013).</strong> In the erasure case, \(I^2+V^2\) = [[t5_ma2013_complementarite_fig3_i2_plus_v2]] ± [[t5_ma2013_complementarite_fig3_err]], below 1; corrected for the imperfection factors stated by the authors (\(\eta_I \approx 0{,}97\), \(\eta_V \approx 0{,}95\)), it is [[t5_ma2013_complementarite_fig3_corrige_eta]] ± [[t5_013_complementarite_fig3_corrige_eta_err]], that is, the expected saturation.</p>
<p>Answer to point (a): yes, all the data respect \(D^2+V^2 \le 1\), and they follow the quantum prediction without an observer.</p>
<h3>5. Test (b): information read versus information never read, on the same apparatus</h3>
<p>In Schwindt et al., the visibility is measured with the analyzer removed (“the polarization analyzer was lowered out of the beam path”): during this measurement, the marker is read by nothing and no one. The knowledge \(K\) is measured in another series, with the analyzer in place: the marker is read. Let us define, for each angle \(\theta \gt 0\),</p>
$$Q = \left(\frac{V_{\text{unread}}}{V_0}\right)^2 + K_{\text{read}}^2 .$$
<p>Quantum mechanics (pure marker) predicts \(Q = 1\): the loss of visibility without reading is exactly the one imposed by the available information. HR predicts \(V_{\text{unread}} = V_0\), hence \(Q = 1 + K^2\), up to [[t5_schwindt1999_q_attendu_hr_5_21]] at 45°. Measured: mean \(Q\) = [[t5_lu_contre_non_lu_schwindt_q_moyen]] ± [[t5_lu_contre_non_lu_schwindt_q_err]]. Over the six angles, \(\chi^2_{\text{QM}}\) = [[t5_schwindt1999_chi2_mq]] for [[t5_schwindt1999_ddl]] degrees of freedom (\(p\) = [[t5_schwindt1999_p_mq]]), \(\chi^2_{\text{HR}}\) = [[t5_schwindt1999_chi2_hr]], i.e. a formal deviation from the HR model of [[t5_schwindt1999_sigma_rejet_hr]] σ. At 45° alone, the unread visibility is [[t5_schwindt1999_v_45deg_27]] instead of 0.98, a deviation of [[t5_schwindt1999_z_hr_45deg]] standard deviations.</p>
<p>Another reading of the same points: the fraction of the visibility loss predicted by quantum mechanics that occurs without any reading is [[t5_windt1999_fraction_perte_mq_sans_lecture]] ± [[t5_schwindt1999_fraction_err]] (1 for quantum mechanics, 0 for HR). The values per angle range from [[t5_schwindt1999_fraction_min_max_0]] to [[t5_schwindt1999_fraction_min_max_1]] and scatter more than their error bars (\(\chi^2\) = [[t5_schwindt1999_fraction_chi2]] for [[t5_schwindt1999_fraction_ddl]] degrees of freedom): the very small error bars on \(V\) do not cover the imperfections of the optics, at the level of a few percent. This does not affect the conclusion: the deviation from HR is counted in tens of percent.</p>
<p>Answer to point (b): no, there is no measurable difference between information read and information never read; the sensitivity of the test is of the order of one percent.</p>
<h3>6. Information never recorded: the Young’s slits of Walborn et al. (2002)</h3>
<p>A photon from an entangled pair is sent onto a real double slit (width 200 µm, spacing 200 µm, λ = 702.2 nm); two quarter-wave plates mark the path through polarization. In figs. 3 and 7, no polarizer is placed anywhere: the polarization is neither analyzed nor recorded, which realizes the experiment of § 4.2 of Campbell et al. We fit each figure with</p>
$$N(x) = \operatorname{sinc}^2\!\left(\frac{x-x_0}{w}\right)\left[a + b\cos\frac{2\pi x}{\Lambda} + c\sin\frac{2\pi x}{\Lambda}\right], \qquad V = \frac{\sqrt{b^2+c^2}}{a},$$
<p>the fringe spacing \(\Lambda\) being fitted on the figure without marking and then fixed. The fitted fringe spacing, [[t5_walborn2002_ajustements_fig2_periode_mm]] mm (direct setup) and [[t5_walborn2002_ajustements_fig6_periode_mm]] mm (delayed setup), is the one imposed by the published geometry, \(\lambda L/d\) = [[t5_walborn2002_periode_attendue_mm]] mm (automatic check).</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Figure</th><th>Situation</th><th>V</th></tr></thead>
<tbody>
<tr><td>2</td><td>no marking</td><td>[[t5_walborn2002_ajustements_fig2_v]] ± [[t5_walborn2002_ajustements_fig2_sv]]</td></tr>
<tr><td>3</td><td>path marked, never read</td><td>[[t5_walborn2002_ajustements_fig3_v]] ± [[t5_walborn2002_ajustements_fig3_sv]]</td></tr>
<tr><td>6</td><td>no marking, delayed detection</td><td>[[t5_walborn2002_ajustements_fig6_v]] ± [[t5_walborn2002_ajustements_fig6_sv]]</td></tr>
<tr><td>7</td><td>path marked, never read, delayed</td><td>[[t5_walborn2002_ajustements_fig7_v]] ± [[t5_walborn2002_ajustements_fig7_sv]]</td></tr>
</tbody>
</table></div>
<p>Ratios \(V_{\text{marked}}/V_{\text{no marking}}\): [[t5_born2002_test_hr_fig3_sur_fig2_rapport_v_47]] ± [[t5_rn2002_test_hr_fig3_sur_fig2_rapport_err]] and [[t5_born2002_test_hr_fig7_sur_fig6_rapport_v]] ± [[t5_rn2002_test_hr_fig7_sur_fig6_rapport_err]]. HR predicts 1: formal deviation of [[t5_walborn2002_test_hr_fig3_sur_fig2_z_hr]] σ and [[t5_walborn2002_test_hr_fig7_sur_fig6_z_hr]] σ. The authors attribute the remaining fringes in fig. 3 to a slight misalignment of the plates.</p>
<p>Comparison with a case where the information is read: in Kim et al. (2000), the coincidences with the path detector D3 (R03) keep a visibility ratio of [[t5_kim2000_rapport_v_r03_sur_r01_53]] ± [[t5_kim2000_rapport_err]] relative to the erased fringes R01. Mean of the two unread Walborn cases: [[t5_lu_contre_non_lu_non_lu_walborn]] ± [[t5_lu_contre_non_lu_non_lu_err]]; unread − read difference: [[t5_contre_non_lu_difference_non_lu_moins_lu]] ± [[t5_lu_contre_non_lu_difference_err]] ([[t5_lu_contre_non_lu_z_difference]] σ), where HR predicts 1 (formal deviation of [[t5_lu_contre_non_lu_z_hr]] σ). This comparison crosses two different experiments; it confirms § 5 without replacing it.</p>
<h3>7. Information lost in the environment</h3>
<p><strong>Collisions (Hornberger et al., 2003).</strong> C70 molecules pass through a Talbot-Lau interferometer filled with gas; each collision carries the which-path information away into a gas molecule that is never detected. Quantum mechanics predicts \(V(p) = V_0\,e^{-p/p_0}\), with \(p_0\) computed without any adjustable parameter. On the [[t5_hornberger2003_fig2_n_points]] methane points (fig. 2), the fit gives \(p_0\) = ([[t5_hornberger2003_fig2_p0_ajuste_1e_6_mbar]] ± [[t5_hornberger2003_fig2_p0_ajuste_err]]) × 10<sup>−6</sup> mbar, against [[t5_hornberger2003_fig2_p0_theorie_1e_6_mbar]] × 10<sup>−6</sup> mbar for the published theoretical line; this line, without any fitting, gives \(\chi^2\) = [[t5_rnberger2003_fig2_chi2_mq_sans_parametre]] for [[t5_hornberger2003_fig2_ddl_mq]] points (\(p\) = [[t5_hornberger2003_fig2_p_mq]]). HR (constant visibility, [[t5_hornberger2003_fig2_v0_hr_pct]]%) is rejected at [[t5_hornberger2003_fig2_sigma_rejet_hr]] σ; at the highest pressure, the visibility is only [[t5_hornberger2003_fig2_v_derniere_pct]]%. Over the ten gases of fig. 3, the measured \(p_0\) are on average [[t5_03_fig3_rapport_mesure_sur_theorie_moyen]] times the computed \(p_0\), with \(\chi^2\) = [[t5_hornberger2003_fig3_chi2_mq]] for [[t5_hornberger2003_fig3_ddl]] gases (\(p\) = [[t5_hornberger2003_fig3_p_mq]]): the agreement is good but not perfect. This common offset of about 10% stays within the 15% uncertainty on the pressure measurement, which is largely common to all the gases (we treated it as independent, which inflates the \(\chi^2\)). HR, which predicts no decoherence (\(1/p_0 = 0\)), is rejected at [[t5_hornberger2003_fig3_sigma_rejet_hr]] σ.</p>
<p><strong>Thermal emission (Hackermüller et al., 2004).</strong> Laser-heated molecules emit photons that the walls absorb; no one detects them. HR predicts a normalized visibility equal to 1; above 7.5 W, it is [[t5_ermuller2004_a_v_norm_moyenne_p_sup_7_5w]] (panel a) and [[t5_ermuller2004_b_v_norm_moyenne_p_sup_7_5w]] (panel b), against [[t5_2004_a_v_norm_theorie_moyenne_p_sup_7_5w]] and [[t5_2004_b_v_norm_theorie_moyenne_p_sup_7_5w]] for the theoretical curve. To be honest, the theoretical curve does not pass through the error bars: \(\chi^2/\text{dof}\) = [[t5_hackermuller2004_a_chi2_mq_par_ddl]] and [[t5_hackermuller2004_b_chi2_mq_par_ddl]], deviations up to [[t5_hackermuller2004_a_ecart_max_mq]] and [[t5_hackermuller2004_b_ecart_max_mq]]. The authors attribute this to the alignment of the heating lasers (“The difference between the theoretical and the experimental curve is of the order of this variation”). When the error bars are inflated until quantum theory has \(\chi^2/\text{dof} = 1\), HR remains rejected at [[t5_muller2004_a_sigma_rejet_hr_conservateur]] σ and [[t5_muller2004_b_sigma_rejet_hr_conservateur]] σ.</p>
<h3>8. Erasure, delayed choice and temporal order</h3>
<p>These experiments do not separate HR from quantum mechanics (all the data in them are recorded), but they check that no effect depends on the moment at which the information is processed, which a rendering triggered at detection might give away.</p>
<ul>
<li><strong>Walborn et al.</strong> By placing a polarizer on the other photon, fringes are recovered (fig. 4: [[t5_walborn2002_ajustements_fig4_v]]; fig. 5: [[t5_walborn2002_ajustements_fig5_v]]) phase-shifted by ([[t5_s_antifranges_fig4_fig5_dephasage_sur_pi]] ± [[t5_franges_antifranges_fig4_fig5_err_sur_pi]]) π; their sum no longer has fringes ([[t5_walborn2002_ajustements_fig4_fig5_v]] ± [[t5_walborn2002_ajustements_fig4_fig5_sv]]) and reproduces fig. 3 (deviation [[t5_ements_fig4_fig5_z_contre_figure_marquee]] σ): what is done later on the other photon does not change what was recorded on the first. In delayed detection, the same sum is [[t5_walborn2002_ajustements_fig8_fig9_v]] ± [[t5_walborn2002_ajustements_fig8_fig9_sv]] and reproduces fig. 7 ([[t5_ements_fig8_fig9_z_contre_figure_marquee]] σ). The visibilities recovered in direct and delayed detection differ by [[t5_detections_fig4_contre_fig8_z_difference]] σ (fringes) and [[t5_detections_fig5_contre_fig9_z_difference]] σ (anti-fringes, weaker in the delayed case).</li>
<li><strong>Kim et al.</strong> The erasure takes place at least 8 ns after the detection of the first photon. The R01 fringes (\(V\) = [[t5_kim2000_ajustements_r01_v]] ± [[t5_kim2000_ajustements_r01_sv]]) and R02 fringes ([[t5_kim2000_ajustements_r02_v]] ± [[t5_kim2000_ajustements_r02_sv]]) are phase-shifted by ([[t5_kim2000_dephasage_r01_r02_sur_pi]] ± [[t5_kim2000_dephasage_err_sur_pi]]) π; their sum is almost flat ([[t5_kim2000_ajustements_r01_r02_v]] ± [[t5_kim2000_ajustements_r01_r02_sv]]); R03 has no fringes ([[t5_kim2000_ajustements_r03_v]] ± [[t5_kim2000_ajustements_r03_sv]]).</li>
<li><strong>Ma et al.</strong>, table I (Vienna): whether the projection of the “environment” photon takes place before, outside the light cone of, or after the passage of the “system” photon, the visibility after erasure is the same: [[t5_ma2013_tableau_i_v_projection_avant]] before, [[t5_ma2013_tableau_i_v_projection_apres]] after, difference [[t5_3_tableau_i_difference_apres_moins_avant]] ± [[t5_ma2013_tableau_i_difference_err]]; the six scenarios are homogeneous (\(\chi^2\) = [[t5_ma2013_tableau_i_chi2_v]] for [[t5_ma2013_tableau_i_ddl]] degrees of freedom). Table II (Canary Islands, 144 km): the which-path information is homogeneous (\(p\) = [[t5_ma2013_tableau_ii_p_i_homogene]]), but the visibility is not (\(\chi^2\) = [[t5_ma2013_tableau_ii_chi2_v]] for [[t5_ma2013_tableau_ii_ddl]] degrees of freedom): scenario II’, choice simultaneous with the emission, gives 0.776 against 0.756 and 0.751, a deviation of [[t5_3_tableau_ii_z_ecarts_v_par_paire_ii_ii]] σ and [[t5_3_tableau_ii_z_ecarts_v_par_paire_ii_iii]] σ, whereas the two scenarios where the choice comes after (II) and before (III) differ by only [[t5_3_tableau_ii_z_ecarts_v_par_paire_ii_iii_118]] σ. The paper states that the results are “similar [...] up to statistical errors”; the figures in its own table do not confirm this. The deviation is not ordered by the timing of the choice and concerns background-subtracted data; we cannot explain it from the paper, and it corresponds to no prediction of HR.</li>
</ul>
<h3>9. Statistical summary and decision rule</h3>
<p>The fits are exploratory. The script keeps the diagnostics computed under its error assumptions, but summing the χ² of panels from the same experiment does not guarantee their independence. Without covariances or a model of the systematic digitization errors, we do not take the combined figures as a level of scientific evidence. The rule was modified after inspecting the results: it is not a preregistered confirmatory protocol.</p>
<h3>10. What the test cannot decide</h3>
<p>A simulation that computed interference from the information <cite>physically present</cite>, read or not, reproduces quantum mechanics identically: no experiment can distinguish it from the absence of simulation. This is in fact what Ma et al. say: “The presence of path information anywhere in the universe is sufficient to prohibit any possibility of interference. It is irrelevant whether a future observer might decide to acquire it.” Such a simulation would make no observer-related savings: it would have to track every gas molecule and every photon lost in the walls. The economical version, the one that motivates the idea, is refuted; the non-economical version is not testable.</p>
<h2 id="limites">Limitations</h2>
<ul>
<li><strong>No raw data.</strong> The points come from the published figures, extracted from the vector drawings; the imprecision of the extraction (at most [[t5_residu_etalonnage_max_pt_toutes_figures]] pt on the tick marks) is far smaller than the error bars, and several checks cross-check the values printed in the texts. The extracted Walborn et al. counts do not fall on integers (deviation up to [[t5_02_controle_releve_ecart_max_a_un_entier]] count), whereas their error bars do equal \(\sqrt N\): an offset of the order of half a count in the plot or in the calibration, with no effect on the visibilities.</li>
<li><strong>The decisive experiment of Campbell et al. has not been carried out as such.</strong> None of the experiments analyzed destroys a record before it is read (their § 4.3) or links a human choice to the moment of observation (§ 4.5). We test their § 4.2 (information detected or present but never recorded), which is the simplest version. Their more elaborate experiments remain to be done; quantum mechanics predicts their outcome unambiguously.</li>
<li><strong>What does “recorded” mean?</strong> A proponent of HR can argue that the polarization of a photon, a gas molecule or the walls of the apparatus “record” the information. But then the notion of observer disappears and the hypothesis merges with quantum mechanics (§ 10).</li>
<li><strong>Deviations from quantum mechanics itself.</strong> The published theory describes the shape of the Hackermüller et al. curve poorly (\(\chi^2/\text{dof}\) from 18 to 46); the \(p_0\) of Hornberger et al. are about 10% below theory; in the mixed state of Schwindt et al., the measured \(V^2+K^2\) (0.003 ± 0.001) deviates from theory (0.017 ± 0.003) by [[t5_99_melange_fig3a_z_mesure_contre_theorie]] σ, a deviation the authors attribute to the empty interferometer. None of these deviations goes in the direction of HR: everywhere, interference is <cite>more</cite> destroyed than HR allows.</li>
<li><strong>Table II of Ma et al.</strong> Unexplained visibility difference between scenarios (§ 8), reported as is.</li>
<li><strong>Sources not read in full.</strong> Englert (1996) and Dürr, Nonn and Rempe (Nature 1998) are paywalled; only their citation by Schwindt et al. and the abstract of Dürr et al. were read, and none of their figures is used.</li>
<li><strong>Independence.</strong> The datasets combined in § 9 come from different experiments; within a dataset, common systematic errors (pressure, alignment) are not modeled.</li>
</ul>
""",
}

AUDIT_1 = {
    'titre': 'Do the proofs of the “yes” hold up?',
    'description': 'We redid, step by step, the calculations published by Melvin Vopson and others to support '
                   'the idea that our Universe is simulated; none of them proves what it claims.',
    'date': 'September 28, 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No.</strong> None of the proofs examined establishes that we live in a simulation: the most recent rests on a verifiable mathematical error, the 2023 thermodynamic derivation on an equality that does not hold for real processes, and its 2025 repair on unproven assumptions.</p>
<p>This “no” concerns these proofs, not the hypothesis itself. That a line of reasoning fails does not prove that the simulation is impossible; it only shows that these papers do not make it more probable. The work of Campbell and of Wolpert, often cited in the same direction, does not in fact claim to establish it: the former propose experiments, the latter proves a logical possibility.</p>
</section>

<h2 id="explication">Explanation</h2>
<p>Melvin Vopson, a physicist at the University of Portsmouth, has been arguing since 2022 for a “second law of infodynamics”: in any system that carries information, the disorder of that information could only remain stable or decrease. He sees in it the mark of a universe that, like a computer, economizes its resources, and therefore a clue in favor of the simulation. We went back over three of his proofs.</p>
<p>The first, published in May 2026, sets out to prove that a system reaches its lowest disorder when all its pieces are repeated the same number of times. The reverse is true. Take six objects of two kinds. Three and three is the most mixed distribution possible, hence the most unpredictable; five and one is the most ordered, because one can guess almost for certain the kind of an object picked at random. The exact calculation confirms this in every case we reviewed, without exception. The paper itself acknowledges, a few lines earlier, that the equal distribution gives the maximum disorder. Its polygon examples (the square “more ordered” than an arbitrary quadrilateral) remain correct, but for another reason, which we prove, and which says nothing about a general law.</p>
<p>The second, published in 2023, starts from an accepted fact: the universe exchanges heat with nothing. Vopson inferred from this that its total disorder cannot change; since physical disorder increases, something else, information, had to compensate by decreasing. But the absence of heat exchange does not prevent disorder from growing. A gas enclosed in an insulated box, which suddenly escapes into an empty half, receives neither heat nor work, and yet its disorder increases by an amount that any textbook calculates. Vopson acknowledged this in 2025.</p>
<p>The third is his 2025 repair. It adds loss terms and again concludes that the disorder of information decreases. But the conclusion does not come out of the calculation: it comes from assumptions made along the way (the losses decrease with time, the temperature of the universe is constant), which the paper asserts without establishing them, and one of which contradicts a sentence in the same text, where the temperature “must decrease”. The calculation itself, done correctly, leaves the result undetermined.</p>
<p>Finally, one often reads that a universe that “compresses” information would betray a computer concerned with economy. Three different things are mixed up here. That a quantity decreases does not imply that there is compression. That a compression exists does not imply that a computer intended it: a perfect compression, moreover, changes nothing in the amount of information transmitted, it only writes it in a shorter form. And only a compression that loses information actually reduces it.</p>
<h2 id="analyse">Detailed analysis</h2>
<h3>1. Vopson’s lemma (2026): a maximum taken for a minimum</h3>
<p>Vopson (<cite>Entropy</cite> 28, 564, May 18, 2026, section 2) considers \(N\) elements distributed into \(n\) categories with multiplicities \(g_i \ge 1\), with \(\sum_i g_i = N\) (equation 3), and the entropy (equation 5)</p>
$$ I(g) = \log_2 N - \frac{1}{N}\sum_{i=1}^{n} g_i \log_2 g_i . $$
<p>This is exactly the Shannon entropy of the distribution \(p_i = g_i/N\): \(I = -\sum_i p_i \log_2 p_i\) (his equations 2 and 4). He looks for the minimum of \(I\) at fixed \(N\), sets \(f = \frac1N\sum g_i \log_2 g_i\) (equation 6), writes that the minimum of I is obtained when [f] is maximal, then sets the derivative of the Lagrangian \(L = f - \lambda(\sum g_i - N)\) to zero and obtains \(g_i = N/n\) (equation 14). He concludes that, when n ≠ 1, the minimum information entropy is non-zero and the condition is given by (14), and, in the abstract as in the conclusion, that the minimum-entropy configuration is that of equal multiplicities.</p>
<p><strong>The stationary point is a maximum.</strong> On the admissible set \(\{g \in \mathbb{R}_{>0}^n : \sum g_i = N\}\), with \(N\) constant,</p>
$$ \frac{\partial I}{\partial g_i} = -\frac{1}{N}\left(\log_2 g_i + \frac{1}{\ln 2}\right), \qquad \frac{\partial^2 I}{\partial g_i\,\partial g_j} = -\frac{\delta_{ij}}{N \ln 2 \; g_i}. $$
<p>The Hessian is diagonal with strictly negative entries, hence negative definite: for any admissible direction \(d \ne 0\) (\(\sum d_i = 0\)), \(d^{\mathsf T} \nabla^2 I \, d = -\sum_i d_i^2/(N\ln 2\, g_i) \lt 0\). \(I\) is strictly concave on a convex set; its unique stationary point, which is indeed \(g_i = N/n\) (the gradient there is proportional to \((1,\dots,1)\), hence orthogonal to the constraint), is its <strong>global maximum</strong>, equal to \(\log_2 n\). The Lagrange method does not distinguish a maximum from a minimum; the second-order condition decides, and it is not examined in the paper. The step “minimum of I ⇔ maximum of f” is correct; the error is to take the stationary point of \(f\), which is convex, for its maximum, whereas it is its minimum.</p>
<p>The paper itself recalls, in the same section, that the maximization of Shannon entropy for uniform probability distributions is a well-established result. Yet, at fixed \(N\) and \(n\), equal multiplicities and a uniform distribution are the same thing: the lemma contradicts the result the paper recalls.</p>
<p><strong>Counterexample.</strong> \(N = 6\), \(n = 2\):</p>
<ul><li>\((3,3)\): [[i33]] bit;</li><li>\((4,2)\): [[i42]] bit;</li><li>\((5,1)\): [[i51]] bit.</li></ul>
<p>The equal distribution gives the largest value, not the smallest.</p>
<p><strong>Exhaustive enumeration.</strong> For \(N\) from 2 to 15 and \(n\) from 2 to \(\min(5, N)\), i.e. [[nb_cas]] cases and [[nb_compo]] compositions examined one by one, the maximum of \(I\) is reached by the most equal distribution \((\lceil N/n\rceil, \dots, \lfloor N/n\rfloor)\) and the minimum by \((N-n+1, 1, \dots, 1)\). Among the [[nb_non_triv]] cases where not all compositions have the same entropy, the most equal distribution is the maximum in [[nb_max]] and the minimum in [[nb_min]]. The true minimum at fixed \(N\) and \(n\) is therefore the most unbalanced distribution; at fixed \(N\) alone, it is \(n = 1\), \(I = 0\), a case the paper mentions separately.</p>
<p><strong>Numerical check of concavity.</strong> At [[nb_points]] randomly drawn points (fixed seed), with random admissible directions, the second derivative by finite differences is always negative (the largest value is [[d2_max]]) and deviates from the analytical formula by at most [[ecart_hess]] in relative terms.</p>
<h3>2. The polygons: right conclusion, different reason</h3>
<p>Section 3 describes a polygon with \(m\) vertices by its \(m\) lengths and its \(m\) angles, i.e. \(N = 2m\) characters, lengths and angles remaining distinct characters (the regular polygon has “only two distinct characters, n = 2”). We recover its values: arbitrary triangle [[p_tri]] bits, arbitrary quadrilateral [[p_quad]] bits, arbitrary pentagon [[p_penta]] bits (the paper prints 3.321, a truncated value), regular polygons [[p_carre]] bit.</p>
<p>Let \(K\) be the kind of a character drawn at random (length or angle): it is “length” with probability exactly \(1/2\). By the chain rule,</p>
$$ I = H(K) + H(X \mid K) = 1 + \tfrac12 H_{\text{sides}} + \tfrac12 H_{\text{angles}} \;\ge\; 1 \text{ bit}, $$
<p>with equality if and only if all the lengths are equal and all the angles are equal, that is, for the regular polygon. The script checks the identity on nine shapes, including the isosceles triangle ([[p_iso]] bit), the rectangle and the rhombus ([[p_rect]] bit).</p>
<p>The geometric constraint therefore changes the scope of the objection. It saves the result of section 3: among polygons with \(m\) sides, the regular one does have the lowest entropy. But equation (14) has nothing to do with it. As soon as \(n = 2\), the only geometrically possible distribution is \((m, m)\); the agreement with “\(g_i = N/n\)” is automatic, and what lowers the entropy is the decrease of \(n\) (from 6 to 2 for the triangle), not the equality of the multiplicities. The general lemma of section 2 remains false, and the result on polygons, a property of the chosen measure, says nothing about a physical tendency toward the minimum.</p>
<h3>3. Vopson (2023): the equality \(dS = \delta Q/T\) holds only for a reversible process</h3>
<p>We could not read the 2023 paper (<cite>AIP Advances</cite> 13, 105308) itself: the publisher and the Portsmouth repository refuse automated access (see `sources.md`). Its derivation is known from the summary the author gives of it in 2025: the universe “exchanges heat with nothing”; the relation \(dQ = T\,dS\) was used; “it was concluded that dS = 0”; the missing entropy term would be that of information, hence \(\partial S_{\text{info}}/\partial t = -\partial S_{\text{phys}}/\partial t \le 0\).</p>
<p>The Clausius inequality only gives \(dS \ge \delta Q/T\), with equality for a reversible process. <strong>Counterexample</strong>: one mole of ideal gas in a rigid, insulated enclosure expands into vacuum until its volume doubles. \(Q = 0\), \(W = 0\), hence \(\Delta U = 0\) and the temperature does not change; since entropy is a state function, it is computed along the reversible isothermal path between the same end states:</p>
$$ \Delta S = n R \ln\frac{V_2}{V_1} = R \ln 2 \quad\text{whereas}\quad \int \frac{\delta Q}{T} = 0 . $$ <p>i.e. [[ds]]&nbsp;J/K,</p>
<p>with \(R = k_B N_A\) = [[r_gaz]]&nbsp;J·mol⁻¹·K⁻¹, the product of two exact SI constants. The MIT notes say so: the equality between ΔS and dQ/T holds only for a reversible process. An absence of heat exchange therefore does not impose a constant entropy, and there is nothing to compensate. Vopson admits this in 2025: without reversibility, one can no longer deduce that dS = 0, which would remove the need to introduce information entropy.</p>
<h3>4. The 2025 repair: a sign that does not follow from the equations</h3>
<p>Vopson (<cite>IPI Letters</cite> 3(1), N6-N9, January 10, 2025) splits the heat into two parts, \(dQ_{\text{phys}} + dQ_{\text{info}} = 0\) (equation 5), writes \(dQ_{\text{phys}} = T dS_{\text{phys}} - dU^{\text{loss}}_{\text{phys}}\) (equation 8), then assumes a similar relation for the informational process (equation 9). He obtains (equation 11)</p>
$$ dS_{\text{info}} = -\,dS_{\text{phys}} + \frac{dU^{\text{loss}}}{T}, \qquad dS_{\text{phys}} \ge 0,\quad dU^{\text{loss}} \ge 0 , $$
<p>the positivity of the losses being stated in the paper (“dULoss is a positive quantity”). Four points.</p>
<ol><li><strong>The sign is undetermined.</strong> The right-hand side is the difference of two positive terms. \(dS_{\text{info}} \le 0\) requires \(dU^{\text{loss}} \le T\,dS_{\text{phys}}\), which nothing establishes. The script tabulates the cases: for \(dS_{\text{phys}} = 1\) and \(dU^{\text{loss}}/T = 2\), \(dS_{\text{info}}\) = [[ds_info]], positive. Expressed per unit time, (11) gives \(\dot S_{\text{info}} = -\dot S_{\text{phys}} + \dot U^{\text{loss}}/T\), where the loss rate \(\dot U^{\text{loss}} \ge 0\) works against the conclusion.</li><li><strong>Equation (12) mixes two operations.</strong> The first two terms are divided by \(dt\), the third is differentiated with \(d/dt\) as if the infinitesimal loss \(dU^{\text{loss}}\) were a function of time. This is what makes the variation of the loss rate, instead of the loss rate itself, appear in (13).</li><li><strong>Even granting (13), the conclusion rests on assumptions.</strong> The second term is negative only if “the loss decreases with time”, which is posited, not proven. The third is positive (\(T\) decreases); the argument that it “cannot compensate” because it “varies as 1/T²” does not compare magnitudes: the ratio of the third term to the second is \(-\,dU^{\text{loss}}\,\dot T / (T\, \tfrac{d}{dt}dU^{\text{loss}})\), which depends on the rates and not on a power of \(T\). Finally, the assumption “T = constant” contradicts the preceding sentence of the same text (“T must decrease with time”) and is justified by no calculation.</li><li><strong>The informational term is postulated.</strong> Neither \(Q_{\text{info}}\), nor the \(S_{\text{info}}\) of the universe, nor \(U^{\text{loss}}_{\text{info}}\) is given an independent definition or a measurement; equation (9) is an assumption, announced as such.</li></ol>
<p>The final sentence, according to which the second law of infodynamics follows identically whether the process is reversible or irreversible, is therefore not proven by the paper.</p>
<h3>5. Compression: three claims not to be confused</h3>
<p>A source with four symbols of probabilities \(1/2, 1/4, 1/8, 1/8\): entropy \(H\) = [[h_src]] bit. The prefix code \(0, 10, 110, 111\) is injective and uniquely decodable; we compute the entropy <strong>on the distribution of the codewords actually emitted</strong> (the third-party script we started from copied the input entropy, which would have hidden a loss): [[h_code]] bit. Over the [[nb_msg]] three-symbol messages, the entropy is [[h_msg]] bits both before and after coding. An injective map preserves probabilities, hence the entropy of complete messages.</p>
<p>What changes is the length: [[l_pref]] bit per symbol instead of [[l_fixe]] for a fixed-length code. The entropy <strong>per bit emitted</strong> even increases, from [[hb_fixe]] to [[hb_pref]]: in the compressed stream, 0 and 1 are equiprobable (frequency of 1s: 1/2). Lossless compression therefore does not lower the entropy of the information; it makes it denser.</p>
<p>Only a non-injective coding reduces it. By merging the two rare symbols (\(c, d \mapsto 11\)), the entropy of the output drops to [[h_perte]] bit, and [[info_perdue]] bit of information is permanently lost: there is no longer any way to know which of the two was emitted.</p>
<p>Hence three distinct claims:</p>
<ol><li><strong>an informational quantity decreases</strong>: a measurable fact, which requires a definition of the quantity and a measurement;</li><li><strong>a compression exists</strong>: a property of a coding, which does not imply the previous claim (without loss, the entropy of the messages is conserved);</li><li><strong>a simulator optimizes its computation</strong>: a hypothesis about a cause, which is implied neither by 1 nor by 2. For an observation to favor it, one would have to show that the observation is more probable with a simulator than without; none of the papers examined computes this ratio.</li></ol>
<h3>6. Campbell et al., Wolpert: what they actually claim</h3>
<p>Campbell, Owhadi, Sauvageau and Watkinson (“On testing the simulation theory”, arXiv:1703.00058, 2017) “describe conceptual wave/particle duality experiments aimed at testing the simulation theory”, under the assumption that a simulator with finite resources would “render” reality only at the moment of observation. They state that they cannot predict the outcome of the proposed experiments. These are protocols, not results; we found no peer-reviewed published result of these experiments.</p>
<p>Wolpert (“Implications of computer science theory for the simulation hypothesis”, arXiv:2404.16050, version 5 of March 19, 2026) proves, using Kleene’s second recursion theorem, that it is “mathematically possible” that we are a simulation, including one run by ourselves. He specifies that he is concerned only with “the logical possibility” of such a system, without examining whether one exists “in our universe”. A possibility result is not evidence.</p>
<h2 id="limites">Limitations</h2>
<ul><li>The full text of Vopson (2023) has not been read: its derivation is known from the summary the author gives of it in 2025; the numbering “section V” has not been verified by us.</li><li>We examined only three of Vopson’s proofs; his other arguments (digital data, genomes, Hund’s rules, gravity) are not audited here, and the 2026 error does not by itself invalidate them.</li><li>The enumeration covers a finite domain; the general validity comes from the concavity proof, which the enumeration and the numerical check only illustrate.</li><li>Free expansion is an ideal-gas model, not a cosmological model: it is enough to refute the general implication “Q = 0 ⇒ ΔS = 0”, not to describe the entropy of the universe.</li><li>We did not check whether the work of Campbell et al. and of Wolpert, read as preprints, has been published in journals.</li><li>Refuting a proof does not establish the opposite of its conclusion: a simulation remains possible, as Wolpert shows, and none of these calculations can rule it out.</li></ul>
""",
}

REVE_RECIT = {
    'titre': 'Dreams and memory: comparing what is signaled with what is recounted',
    'description': 'An audit of eight sources, a recalculation of an individual-level table and an analysis plan for comparing duration judgements made during the dream and after awakening.',
    'date': 'October 8, 2026',
    'corps': r"""
<h2>Explanation</h2>
<p>When a person recounts a dream that felt very long, at what point did that impression form? To make progress, we looked for data that would let us compare what the person signals during sleep with what they report on awakening, about the same interval.</p>
<p>We examined [[rr_candidats]] candidate sources or datasets, inspected the open metadata of DREAM and recalculated an individual-level table published in 2026. <strong>No dataset directly usable for comparing two paired duration judgements was retrieved in this corpus.</strong> The effect we are looking for remains unknown. Our contribution is an access report, a check of the denominators and an executable method for a future reanalysis.</p>

<h3>A response during the dream can differ from the memory of it</h3>
<p><a href="https://doi.org/10.1016/j.cub.2021.01.026">Konkoly and colleagues (2021)</a> describe exchanges recorded during sleep, some details of which are forgotten or reported differently after awakening. This justifies comparing the two moments. These observations do not quantify a speeding-up of experience. A <a href="https://pubmed.ncbi.nlm.nih.gov/15336243/">study by Conduit and colleagues (2004)</a> had already compared an eye response to a sound with its later recall.</p>

<h3>Many signals can come from few people</h3>
<p>In the table of <a href="https://doi.org/10.1162/JOCN.a.107">Konkoly and colleagues (2026)</a>, [[rr_signaux]] signals come from [[rr_personnes_signaux]] of the [[rr_personnes]] people listed. The two largest contributors provide [[rr_top2]] of them, or [[rr_part_top2]]%. This descriptive recalculation explains why our future contrast will first be computed per person.</p>
<figure class="figure-scientifique">
<img src="/fichiers/reve-recit/signaux-par-personne.svg" width="640" height="580" loading="lazy" alt="Distribution of 150 signals across 13 rows of the published table: the two largest counts are 57 and 45; two people produced no signal.">
<figcaption>Counts from Table 1, page 367. The order of the source rows provides the identifiers P01 to P13. The numbers of sessions differ; this chart does not compare the abilities of the people.</figcaption>
</figure>

<h3>The proposed comparison</h3>
<p>It requires a bounded interval, then two comparable questions about that interval: a response given during sleep, and a response after awakening, before any feedback on the first response or on the measured duration. A duration recounted for a whole story will not be compared with the duration of a single task.</p>
<p>A discrepancy would indicate that the judgment changed between the two reports. It would not, on its own, determine when that change occurred, nor attribute its whole cause to memory. The act of responding, the change of state and communication difficulties may also play a part.</p>

<h2>Detailed analysis</h2>
<h3>1. What the sources actually allow us to analyze</h3>
<p>The search is targeted and makes no claim to be exhaustive. A dataset that was not retrieved is not declared non-existent. The access statements below were checked on October 8, 2026.</p>
<div class="tableau"><table>
<thead><tr><th>Source or dataset</th><th>Contribution and limitation for this question</th></tr></thead>
<tbody>
<tr><td>Conduit 2004; Erlacher 2014</td><td>Recall of events or task durations. No individual pair of during/after duration judgements retrieved.</td></tr>
<tr><td>Konkoly 2021 and 2026</td><td>Communication during the dream; individual data on request or under restriction. Table of counts accessible in 2026.</td></tr>
<tr><td>DREAM / Tononi</td><td>Open metadata: [[rr_dream_lignes]] awakenings from [[rr_dream_personnes]] people. Duration classes after awakening; no judgment during sleep in these tables.</td></tr>
<tr><td>Donders 2022</td><td>Repository announcing a publication in preparation; the necessary files are not available in the root examined.</td></tr>
<tr><td>DreamViews, 2026 preprint</td><td>Forum accounts; no paired physiological recording in the definition of the corpus.</td></tr>
<tr><td>MÖBIUS, 2026</td><td>Proposed model of dream/memory confusion; individual clinical data under restrictions.</td></tr>
</tbody></table></div>
<p>The <a href="https://doi.org/10.26180/23306054.v3">Tononi Serial Awakenings</a> archive was checked by its checksum and the shared keys of its tables. The interval between two awakenings does not give the start of the reported experience. The ordinal classes remain classes; we do not assign them an arbitrary number of seconds.</p>
<p>The <a href="https://github.com/Niloy333/Donders-2022">Donders repository</a>, the <a href="https://arxiv.org/abs/2603.26992">DreamViews corpus</a> and the <a href="https://www.nature.com/articles/s42003-026-09781-x">MÖBIUS model</a> answer other useful questions. Their existence does not fill the missing fields of our comparison. No contact, no new data collection and no EEG reanalysis were carried out in this study.</p>

<h3>2. A contrast between reports, with equal weight per person</h3>
<p>For an admissible episode, let \(P_{ij}\) denote the estimate during the dream and \(A_{ij}\) the estimate after awakening, expressed in the same unit. The plan proposes:</p>
$$d_{ij}=\log(A_{ij}/P_{ij}),\qquad d_i=\frac{1}{n_i}\sum_j d_{ij},\qquad D=\frac{1}{N}\sum_i d_i.$$
<p>The geometric ratio \(e^D\) expresses the mean change of judgment under this weighting. A person who produces many responses does not receive more weight. Uncertainty is estimated by resampling whole people; the episodes of one person stay grouped.</p>
<p>The software keeps every attempt and the reasons for its non-admissibility. It rejects duplicates, impossible chronologies and non-positive durations; it excludes from the main contrast different intervals or questions, unverified signals and responses collected after feedback. An absence of recall stays distinct from a judgment of zero duration.</p>
<p>The plan adopts a report on awakening within two minutes, an operational convention with no biological claim. It provides for a bootstrap of [[rr_bootstrap]] repetitions and produces no interval below [[rr_min_personnes]] admissible people. This threshold does not guarantee the quality of the inference. An analysis that removes each person in turn measures how much the result depends on a single participant.</p>
<p>This plan is proposed for a reanalysis of suitable data. It was recorded after reading the papers and before any pairs were acquired in this project; <strong>it is not preregistered with an independent registry</strong>. The published table, for its part, has undergone an exploratory reanalysis.</p>

<h3>3. Why even two reports do not give a speed of consciousness</h3>
<p>Consider a purely illustrative measurement model. For a physical duration \(T\), a hypothetical latent factor \(F\) and two report biases \(B_P\) and \(B_A\), we write:</p>
$$P=T F B_P,\qquad A=T F B_A,\qquad \frac{A}{P}=\frac{B_A}{B_P}.$$
<p>The calculation builds two scenarios that give exactly the same observations: for [[rr_ex_t]] physical seconds, a response of [[rr_ex_p]] seconds during the dream and of [[rr_ex_a]] seconds afterwards. In the first scenario, \(F=1\), \(B_P=1\), \(B_A=2\). In the second, \(F=2\), \(B_P=1/2\), \(B_A=1\). The observations cannot decide between the two values of \(F\).</p>
<p>This is an algebraic counterexample, with no participant and no validated neural model. It shows the additional assumptions needed before a report can be interpreted as an absolute conscious duration. Controls during wakefulness could study some response biases, without guaranteeing that they stay the same during sleep.</p>

<h3>4. Present result and the next evidence needed</h3>
<p>The check of the table confirms its totals; the concentration of [[rr_part_top2]]% is descriptive. The formulas and the handling of missing data were tested on artificial cases, with a separate numerical check. <strong>The number of human pairs analyzed is [[rr_paires]] and the main effect remains unestimated.</strong> This absence of data is not evidence of an absence of change.</p>
<p>The next empirical step requires a dataset documenting both reports of the same interval, the instructions, the timestamps and the attempts without a response. The result will then have to be checked against other people or sessions. A result compatible with zero would not demonstrate the equivalence of the two reports either, without a relevant margin defined in advance.</p>
<p>This study extends the <a href="/programme/">notebook on dreams, time and memory</a>. It specifies a measurement that is feasible in principle and the limits of its interpretation. No result here links felt duration to the <a href="/gravitation-horloges/">gravitational dilation of clocks</a> or to a hypothesis about the origin of the Universe.</p>
""",
}

EINSTEIN_RESTREINTE = {
    'titre': 'Einstein: why speeds and durations depend on the observer',
    'description': 'Special relativity, velocity addition, light and the twin paradox: explanation, calculations and limits.',
    'date': 'October 8, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>Two people who follow different paths can accumulate different durations before they meet again.</strong> Yet each sees their own watch running normally. This offset concerns local physical processes, not merely an illusion produced by light signals.</p>
<p>Here is an idealized scenario. One person stays in a frame of reference that we will call “terrestrial”. Another leaves and comes back at 80% of the speed of light; we neglect the manoeuvring phases and gravitation. Between the departure and the reunion, the first counts 50 years and the second [[voyage_80]] years. The same two events bound two different proper times. This calculation describes no available travel technology.</p>
<h3 id="vitesses">Why do two high speeds not exceed the speed of light?</h3>
<p>A spaceship moves at 90% of the speed of light relative to the Earth. It launches an object forward at 90% of that speed, <em>measured from the spaceship</em>. The Earth measures [[addition_90]]% of the speed of light for the object. Velocities do combine, but the ordinary rule “90 + 90” no longer applies.</p>
<p>This difference does involve space and time, as well as the <strong>relativity of simultaneity</strong>: observers do not assign the same time and space coordinates to distant events. What is simultaneous for one may not be for the other. Distances, durations and synchronization must be transformed together. It is not a matter of space physically stretching to slow the object down.</p>
<p>If the spaceship switches on a lamp, it measures light in vacuum at speed c, and so does the Earth. There is no rest frame of a photon in which the comparison could be repeated. These rules go back to <a href="https://doi.org/10.1002/andp.19053221004">Einstein’s special relativity, published in 1905</a>.</p>
<h3>Why this is not just an effect of perspective</h3>
<p>An object moving away can appear slowed down to us because its signals arrive later and later. This Doppler effect and the propagation time must be distinguished from the duration actually shown by its watch. In the reunion scenario, the two watches are brought together at the same place: the difference remains.</p>
<p>The phenomenon does not rest only on a thought experiment. <a href="https://doi.org/10.1126/science.1192720">Chou and colleagues, in 2010</a>, compared optical clocks and measured changes of rate due to motion at speeds below ten meters per second. The effect is then extremely small.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3>Proper time and the Lorentz transformations</h3>
<p>In flat spacetime, for a path with velocity v(t) in an inertial frame:</p>
$$\Delta\tau=\int\sqrt{1-\frac{v(t)^2}{c^2}}\,dt.$$
<p>At constant speed, this becomes \(\Delta\tau=\Delta t/\gamma\), with \(\gamma=(1-v^2/c^2)^{-1/2}\). Special relativity can also handle accelerated paths in flat spacetime: “special” does not mean that all acceleration is forbidden.</p>
<table class="phrases"><caption>Idealized round trip: 50 years in the terrestrial frame, manoeuvres neglected.</caption><thead><tr><th>Speed during the legs</th><th>Traveler’s duration</th></tr></thead><tbody>
<tr><td>80% of c</td><td>[[voyage_80]] years</td></tr>
<tr><td>90% of c</td><td>[[voyage_90]] years</td></tr>
<tr><td>99% of c</td><td>[[voyage_99]] years</td></tr>
<tr><td>99.9% of c</td><td>[[voyage_999]] years</td></tr>
</tbody></table>
<p>The values are calculated here, without any human measurement. The turnaround makes the two histories different; the roles cannot be swapped while keeping a single inertial frame for the traveler. The total gap is calculated along the paths. Acceleration is not a substance that would damage the clock and produce the whole offset by itself.</p>
<p>For two frames in relative motion v along x, the inverse transformation gives:</p>
$$dx=\gamma(dx'+v\,dt'),\qquad dt=\gamma\left(dt'+\frac{v\,dx'}{c^2}\right).$$
<p>Dividing the two expressions, with \(u'=dx'/dt'\), gives the collinear composition:</p>
$$u=\frac{u'+v}{1+u'v/c^2}.$$
<p>For \(u'=v=0{,}9c\), we obtain \(u/c=1{,}8/1{,}81\). For \(u'=c\) and \(|v|\lt c\), the result is exactly c. At low speeds, the denominator is very close to one: everyday addition is an excellent approximation.</p>
<h3>Two objects can nevertheless approach each other at 1.8 c</h3>
<p>If two objects each have a speed of 0.9 c in opposite directions <em>in the same terrestrial frame</em>, their separation decreases at 1.8 c in these coordinates. This closing rate is not the speed of any object in the frame of the other. That speed is obtained by the relativistic transformation and stays below c.</p>
<h3>Energy and the speed limit</h3>
<p>For an object with non-zero rest mass, \(E=\gamma mc^2\). Its energy increases without bound as its speed approaches c. The rest energy \(E_0=mc^2\) is a special case of the relation \(E^2=p^2c^2+m^2c^4\). Photons, whose rest mass is zero, are not massive objects accelerated up to c.</p>
<h3 id="limites">What this theory does not resolve</h3>
<p>Special relativity describes physics on a flat geometry. It does not provide the dynamics of a general gravitational field: that is the role of general relativity. Nor does it determine the subjective sensation of time. It is compatible with quantum field theory; the problem of quantum gravity should therefore not be presented as a general contradiction between “Einstein” and “the quantum”.</p>
<p>Its experimental confirmations do not mean that every extrapolation to every imaginable energy is proven. Any new theory will have to explain why the results already measured are recovered within their domain of validity.</p>
<p>Next: <a href="/gravitation-horloges/">gravitation, clocks one centimeter above the ground and time near black holes</a>.</p>
""",
}

GRAVITATION_HORLOGES = {
    'titre': 'Do we age more slowly near a black hole and at the center of the Earth?',
    'description': 'From a clock raised by one centimeter to the Earth’s center and black holes: potential, proper times, calculations and conditions.',
    'date': 'October 8, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>Yes, in well-defined comparisons, a clock located deeper in a gravitational well accumulates less time.</strong> Near the Earth, the gap is tiny. Near the event horizon of a black hole, it can become very large. The two positions and the paths being compared must always be specified.</p>
<ol>
<li>Two identical clocks are compared, taking into account how their signals are carried.</li>
<li>One is placed higher than the other and both are held at fixed positions.</li>
<li>In the ordinary terrestrial case, the higher clock gradually gets ahead.</li>
</ol>
<p>A person accompanying each clock would experience their own time normally. Under comparable biological conditions, less proper time means less time available for the body’s processes. This is neither rejuvenation nor a local sensation of slow motion. Biological aging also depends on the environment; the calculations below compare ideal clocks first.</p>
<h3 id="centimetre">A clock one centimeter above the ground</h3>
<p>Compared with an identical clock left at ground level, it gains about <strong>[[cm_an_ps]] picoseconds per year</strong>: a picosecond is a millionth of a millionth of a second. That is also [[cm_jour_fs]] femtoseconds per day. This is not a continuous acceleration of its rate: at a fixed height, the small difference in rate stays practically constant and the lead accumulates.</p>
<p>This number is our calculation for a local gravitational acceleration of 9.81 m/s². The gravitational effect is measured: <a href="https://doi.org/10.1038/s41586-021-04349-7">Bothwell and colleagues, in 2022</a>, resolved frequency differences across a millimeter-scale atomic sample. An optical clock is an atomic clock that uses a transition at an optical frequency; not every ordinary atomic clock reaches this precision.</p>
<h3 id="terre">At the center of the Earth: the zero-force trap</h3>
<p>At the center of an ideal spherical Earth, the attractions cancel out: the net gravitational acceleration is zero. Yet the gravitational potential there is lower than at the surface. <strong>A central clock therefore accumulates less time.</strong> The local force indicates the slope of the potential, not its depth. A valley can have a flat floor while lying far below its rims.</p>
<p>The core is an extended region: the number quoted for the exact center does not apply identically to the whole core. The further down one goes in the stationary spherical model, the more the clock lags behind the surface. The force of gravity, by contrast, does not increase continuously all the way to the center.</p>
<p>The study by <a href="https://arxiv.org/abs/1604.05507">Uggerhøj, Mikkelsen and Faye (2016)</a> gives a difference of [[prem_age]] years between center and surface by extrapolating a model of the Earth’s structure over 4.54 billion years. This is a theoretical estimate, not a measurement of two ancient clocks. The same extrapolation amounts to <strong>[[prem_80]] second over 80 years</strong>. It does not mean that the rocks of the core formed two and a half years after those of the crust.</p>
<h3 id="trou-noir">Near a black hole: a potentially much larger effect</h3>
<p>Consider a non-rotating black hole and a clock held at a fixed position outside it. At a distance from the center equal to four thirds of the horizon radius, it counts 30 minutes while a very distant clock counts 60. Locally, these 30 minutes are ordinary. This scenario, however, requires the clock to be held in place by thrust; it is not a stable free orbit.</p>
<p>As the fixed position gets closer to the horizon, the thrust required becomes unbounded in this model. A stationary clock cannot be placed on the horizon. A falling observer follows a different path and can cross the horizon in a finite proper time. The apparent freezing of their last signals for a distant observer does not mean that their personal time stops.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3>What general relativity adds</h3>
<p>General relativity, formulated by Einstein in 1915 and set out in his <a href="https://doi.org/10.1002/andp.19163540702">1916 review paper</a>, relates the geometry of spacetime to its content in energy, momentum and stress. In the form that includes the cosmological constant:</p>
$$G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}.$$
<p>The left-hand side describes the geometry, the right-hand side the physical content that contributes to it. Clocks measure the temporal length of their path in this geometry. Speaking only of a “force that slows everything down” hides this structure.</p>
<h3>Weak field and small heights</h3>
<p>In a weak, stationary field, at low speeds, with a Newtonian potential Φ equal to zero at infinity:</p>
$$\frac{d\tau}{dt}\simeq1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}.$$
<p>For two clocks held close to each other, a small difference in height Δh gives, to first order, \(\Delta\Phi\simeq g\Delta h\). Hence:</p>
$$\frac{\Delta f}{f}\simeq\frac{g\Delta h}{c^2}.$$
<p>For Δh = 0.01 m, this gives [[cm_fraction]]. Multiplied by the seconds in a year of 365.25 days, we recover [[cm_an_ps]] picoseconds. Over one meter, the lead is about [[metre_an_ns]] nanoseconds per year; over one kilometer, [[km_an_us]] microseconds per year in the constant-g approximation. Speeds, the Earth’s rotation and variations of the potential require corrections in a precise comparison.</p>
<h3>Why the exterior formula does not apply at the center of the Earth</h3>
<p>Inside, the matter lying further out than the clock still contributes to the potential, even when its net force cancels by symmetry. One must therefore not extend \(-GM/r\) down to r = 0 by putting the whole mass of the Earth at the center. For a homogeneous sphere of radius R:</p>
$$\Phi(r)=-\frac{GM}{2R}\left(3-\frac{r^2}{R^2}\right),\qquad 0\leq r\leq R.$$
$$\Phi(R)-\Phi(0)=\frac{GM}{2R},\qquad \frac{\tau_{\rm surface}-\tau_{\rm centre}}{\tau_{\rm surface}}\simeq\frac{GM}{2Rc^2}.$$
<p>With the Earth’s radius rounded to 6,371 km, our homogeneous calculation gives [[homogene_age]] years over the chosen geological time span, or [[homogene_80]] second over 80 years. The published result with the PREM density profile, [[prem_age]] years, takes a denser center into account. We quote this result and carry out its time conversion; we did not redo the PREM integration.</p>
<figure class="mc-resultats">
<img src="/fichiers/gravitation-horloges/terre-horloges.svg" width="480" height="490" loading="lazy" alt="A clock’s lag increases going from the surface to the centre. Curve calculated for a homogeneous Earth and a separate central point taken from the published PREM value.">
<figcaption>Homogeneous-sphere calculation; PREM point converted from Uggerhøj et al. (2016). The reference duration of 80 years belongs to the surface clock. Both estimates assume a stationary structure.</figcaption>
</figure>
<p>The geological result does not trace the whole accretion, differentiation and evolution of the planet. For an exact history, the potential and the motion would have to be integrated over time. No organism could stay at the center of the Earth: the comparison concerns the proper time of ideal clocks, independently of this physical impossibility.</p>
<h3>The Schwarzschild comparison</h3>
<p>The horizon radius of a spherical, uncharged, non-rotating black hole is \(r_s=2GM/c^2\). For ten nominal solar masses, our calculation gives [[bh_rs_10]] km. The radius r used here is defined by the area \(4\pi r^2\) of the spheres: its difference from r_s is not directly a radial distance measured with a ruler.</p>
<p>At a fixed position, for \(r>r_s\), the duration compared with the time of a static clock at infinity satisfies:</p>
$$\frac{d\tau}{dt}=\sqrt{1-\frac{r_s}{r}}.$$
<table class="phrases"><caption>Clock held at fixed radius: local duration during 60 minutes very far from the black hole.</caption><thead><tr><th>Radius from the center</th><th>Local minutes</th></tr></thead><tbody>
<tr><td>10 r_s</td><td>[[bh_10_min]]</td></tr>
<tr><td>3 r_s</td><td>[[bh_3_min]]</td></tr>
<tr><td>2 r_s</td><td>[[bh_2_min]]</td></tr>
<tr><td>4 r_s / 3</td><td>[[bh_43_min]]</td></tr>
<tr><td>1.01 r_s</td><td>[[bh_101_min]]</td></tr>
</tbody></table>
<p>These figures are predictions in an ideal model. They are not enough to propose a feasible stay: thrust, tidal forces, surrounding radiation and the round trip must also be considered.</p>
<h3>An orbit is not being held static</h3>
<p>For a circular geodesic orbit in the same spacetime:</p>
$$\frac{d\tau}{dt}=\sqrt{1-\frac{3r_s}{2r}}.$$
<p>Stable circular orbits begin at \(r=3r_s\), with marginal stability at that limit. The ratio is then [[bh_orbite_3]], instead of about 0.816 for a static clock at the same radius. Orbital motion therefore really contributes to the difference. Rotating black holes require a different geometry and a specification of the direction of the orbit.</p>
<figure class="mc-resultats">
<img src="/fichiers/gravitation-horloges/trou-noir-horloges.svg" width="480" height="490" loading="lazy" alt="Comparison of the rates of static clocks and clocks on stable circular orbits. The orbital curve begins at three horizon radii; no static clock is defined on the horizon.">
<figcaption>Calculations in the Schwarzschild solution. The point at 3 r_s marks the marginally stable circular orbit. The limit of the static curve toward the horizon does not represent a clock that could stay stationary there.</figcaption>
</figure>
<h3 id="preuves">What is tested, and what remains extrapolated</h3>
<p>Optical clocks directly test rate differences in the Earth’s field. Near the Galactic Center, <a href="https://arxiv.org/abs/1807.09409">GRAVITY observed in the light of the star S2</a> a signal combining gravitational redshift and transverse Doppler shift, consistent with general relativity. This is neither an isolated measurement of the gravitational component nor an observation at the horizon.</p>
<p>The <a href="https://arxiv.org/abs/1602.03837">GW150914 detection</a> tests another prediction: the gravitational waves from a black hole merger. These successes do not give us access to the interior singularity. The distinction is developed in <a href="/hawking-trous-noirs-limites/">the study on Hawking and the limits of theories</a>.</p>
""",
}

HAWKING_LIMITES = {
    'titre': 'Hawking: what black holes reveal, and what remains unknown',
    'description': 'Singularities, the area theorem, radiation, information and the no-boundary proposal: separating the evidence from the open questions.',
    'date': 'October 8, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>Hawking did not propose a single theory that would replace Einstein’s.</strong> His work made use of general relativity, then confronted it with quantum physics. It brings to light powerful results and places where our description remains incomplete.</p>
<p>Three steps must be followed: gravitation can form a horizon; quantum fields on this background predict an emission; the full evolution of the object, especially at the end, requires more than this first calculation. Each of these steps has its own level of evidence.</p>
<ol>
<li><strong>Singularities, with Penrose:</strong> certain classical assumptions lead to incomplete paths. The theorem does not describe any replacement physics.</li>
<li><strong>Area theorem:</strong> under its classical assumptions, the total area of horizons does not decrease. Its domain excludes quantum effects that are relevant to evaporation.</li>
<li><strong>Hawking radiation:</strong> a quasi-thermal emission is predicted on a gravitational background. Direct astronomical detection is lacking; the approximation does not explain the whole end.</li>
<li><strong>Hartle–Hawking proposal:</strong> a quantum prescription for the state of the Universe without a classical initial boundary. It depends on assumptions and is not confirmed as the actual origin of the Universe.</li>
</ol>
<h3 id="horizon">The horizon is not the singularity</h3>
<p>The horizon separates the events that can still send a signal to the distant outside from those that no longer can. It is not a material wall. In the classical model of a large black hole, the crossing can take place without any local encounter with a solid surface; tidal forces depend in particular on the mass and the path.</p>
<p>The singularity corresponds to a different difficulty: the classical description no longer allows certain paths to be continued. In the Schwarzschild solution, the curvature diverges toward r = 0. This does not entitle us to claim that an infinite density is a physically observed object. The calculation tells us where it reaches its limit.</p>
<h3 id="rayonnement">How can a black hole emit?</h3>
<p><a href="https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-43/issue-3/Particle-creation-by-black-holes/cmp/1103899181.pdf">Hawking’s 1975 calculation</a> deals with quantum fields in a collapse geometry. The state that resembles the vacuum before the black hole forms produces an emission for distant observers. The popular description of two small particles created at the edge is a limited picture, not the full mechanism of the calculation.</p>
<p>The radiated energy reduces the mass of the black hole if it loses more than it absorbs. For stellar masses, the predicted temperature is extraordinarily low. The bright gas around a black hole and its jets are not an observation of Hawking radiation.</p>
<p><a href="https://arxiv.org/abs/1510.00621">Analog experiments in atomic condensates</a> study horizons for excitations of the medium. They are relevant to emission mechanisms, but they do not create an astrophysical black hole and are not a direct detection of one.</p>
<h3 id="information">The information problem, in concrete terms</h3>
<p>Imagine two different quantum states that collapse. If, after complete evaporation, they ended up in exactly the same final state of radiation, the distinction between them would have disappeared. A unitary quantum evolution, by contrast, preserves the distinctions of the complete state. “Information” here refers to these states and their correlations; it is not necessarily a recoverable human memory.</p>
<p>The initial calculation produces radiation part of whose description is thermal and correlated with the interior. The decisive question concerns the correlations of the complete system during evaporation. Recent progress on entropy provides answers in specific models, while leaving open the full physical description of an astrophysical black hole.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3>Singularities: a theorem with assumptions</h3>
<p>The <a href="https://doi.org/10.1098/rspa.1970.0021">theorem of Hawking and Penrose (1970)</a> combines conditions of causality, convergence of paths, energy and focusing, with a suitable global assumption. It leads to the incompleteness of at least some timelike or null geodesics. It does not say that all observers meet the same point, nor that every indicator of curvature diverges in every case.</p>
<p>An incomplete timelike path can have a finite proper time with no continuation in the spacetime under consideration. For a light ray, the corresponding notion uses an affine parameter; it is not the time shown by a watch attached to the photon. Some classical assumptions can be violated by quantum effects. This theorem therefore proves neither a creation from nothing nor the impossibility of any earlier cosmological model.</p>
<p>In Schwarzschild, the Kretschmann curvature scalar is:</p>
$$K=R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta}=\frac{48G^2M^2}{c^4r^6}=\frac{12r_s^2}{r^6}.$$
<p>It is finite at the horizon, \(K(r_s)=12/r_s^4\), and diverges as r tends to zero. The divergence of certain coordinates at the horizon is therefore not this curvature singularity. This distinction explains why the <a href="/gravitation-horloges/">traveler’s proper time does not stop at the horizon</a>.</p>
<h3>Temperature and entropy</h3>
<p>For an uncharged, non-rotating black hole:</p>
$$T_H=\frac{\hbar c^3}{8\pi G M k_B},\qquad S_{BH}=\frac{k_B c^3 A}{4G\hbar}.$$
<p>The temperature varies as the inverse of the mass; the entropy as the area. Applying these expressions with the constants given in our analysis, we obtain:</p>
<table class="phrases"><caption>Theoretical Schwarzschild temperatures; masses expressed in nominal solar units.</caption><thead><tr><th>Mass</th><th>Temperature</th></tr></thead><tbody>
<tr><td>One solar mass</td><td>[[hawking_solaire_k]] K</td></tr>
<tr><td>Ten solar masses</td><td>[[hawking_10_k]] K</td></tr>
<tr><td>One million solar masses</td><td>[[hawking_million_k]] K</td></tr>
</tbody></table>
<p>For one solar mass, \(S_{BH}/k_B\) is [[hawking_solaire_s]]. These values are predictions, not measurements of temperature or entropy made by Aeternam. The received spectrum also includes transmission factors due to the propagation of the fields in the geometry.</p>
<h3>An area theorem put to the test, a radiation still distinct</h3>
<p>The <a href="https://arxiv.org/abs/2509.08054">GW250114 analysis, published by LIGO, Virgo and KAGRA in 2025</a>, compares the properties before and after a merger. In the analyses presented, the final area is greater than the sum of the initial areas with high credibility. This is an observational test of the classical law, under the assumptions used to infer the masses and spins.</p>
<p>The area can nevertheless decrease during quantum evaporation: the energy conditions of the classical theorem no longer apply there in the same way. The generalized thermodynamic law then concerns the entropy of the black hole <em>and</em> that of its surroundings. An increase in area during a merger therefore does not demonstrate the detection of the quantum emission.</p>
<h3>Evaporation: what a gigantic duration means</h3>
<p>A black-body estimate, without accretion and without detailing the emitted species, leads to:</p>
$$t_{\rm evap}\approx\frac{5120\pi G^2M^3}{\hbar c^4}.$$
<p>It gives [[hawking_solaire_ans]] years for one solar mass. The coefficient depends on how the emission is modeled; the transmission factors and the accessible particles matter. This figure is an order of magnitude under assumptions, not a certain date of disappearance. The mass, the spin and the environment evolve, and the approximation does not describe the final quantum phase in a controlled way.</p>
<h3>Page curve and entropy islands</h3>
<p>In an ideal scenario of unitary evaporation, the fine-grained entropy of the radiation first increases and then falls again as the correlations become accessible in a larger part of the radiation. <a href="https://arxiv.org/abs/1911.12333">Replica and island calculations</a> reproduce this structure in certain models, notably two-dimensional ones, with precise gravitational prescriptions.</p>
<p>The <a href="https://arxiv.org/abs/2006.06872">review by Almheiri and colleagues</a> explains why this is major progress. Calculating an entropy consistent with unitarity is not, however, the same as having a device that recovers the information from a real black hole, nor a universally accepted description of every stage of evaporation. None of these calculations is an astronomical measurement of the Page curve.</p>
<h3>Hartle–Hawking: a proposal about the Universe</h3>
<p>The <a href="https://doi.org/10.1103/PhysRevD.28.2960">no-boundary proposal of Hartle and Hawking (1983)</a> seeks to define a cosmological quantum state from regular geometries that lack the usual classical initial boundary. It does not demonstrate that our Universe never began, nor that it appeared from an experimentally defined physical nothingness.</p>
<p>The predictions depend in particular on the calculation prescription and on the probabilities drawn from it. <a href="https://arxiv.org/abs/2403.10510">Maldacena (2024)</a> discusses difficulties in inflationary models. A <a href="https://arxiv.org/abs/2602.02682">preprint by Abdalla and colleagues (2026)</a> re-examines the normalization and shows that it profoundly changes the probabilities obtained within its framework. This illustrates an active theoretical question, not an origin of the Universe that has now been measured.</p>
<h3 id="points-ouverts">The real open questions</h3>
<ul>
<li><strong>Quantum gravity:</strong> what description replaces classical geometry when its fluctuations become essential, and which observations will decide between the proposals?</li>
<li><strong>The interior of black holes:</strong> what becomes of a singularity in this description? The observed exterior does not provide a photograph of the center.</li>
<li><strong>Information:</strong> how do the entropy results translate into microscopic dynamics for a realistic collapse and evaporation?</li>
<li><strong>The end of evaporation:</strong> complete disappearance, a remnant state or some other evolution require physics beyond the semi-classical extrapolation.</li>
<li><strong>The cosmological origin:</strong> singular classical models, no-boundary proposals and other scenarios do not have the same status as an observation of the initial instant.</li>
</ul>
<p>These limits do not cancel the clock comparisons, orbits and gravitational waves already tested. A description can be remarkably reliable in one domain while remaining incomplete in another. The contribution of these three studies is to specify the domains, reproduce orders of magnitude and avoid turning a formula or an assumption into universal proof.</p>
<p>Go back to <a href="/einstein-relativite-restreinte/">Einstein’s speeds and durations</a>, or to the <a href="/gravitation-horloges/">clock comparisons from the Earth’s center to black holes</a>.</p>
""",
}

# The seven topics of the blog, from the closest to a person to the widest. For each one:
# the question, what is at stake (why it belongs on a site about immortality), the answer
# in plain words (its [[markers]] are filled with numbers from the articles in 'sources')
# and 'lien', the article where the evidence can be read.
CELLULES = {
    'titre': 'Does restriction keep the blood young?',
    'description': 'Of 75 blood measures in 937 mice, 25 change under caloric restriction and predict survival within each diet: a younger blood. They explain the shift of the risk, not yet its slope.',
    'date': 'November 21, 2026',
    'corps': r'''

<h2 id="explication">Explication</h2>
<p><strong>Does caloric restriction keep the blood young? Yes, and this younger blood predicts a longer life. But it does not yet explain why aging slows down.</strong></p>
<p>We took the blood measurements of the [[cs_souris]] mice of <a href="/restriction/">the restriction study</a>: the blood count, at about [[cs_age_cbc]] days, and the cells of the immune system, at about [[cs_age_flow]] days. Before looking at survival, we wrote and recorded the analysis plan: which measures, which tests, what would count as a result.</p>
<p>Of [[cs_mesures]] measures, [[cs_cand_cal]] change under restriction and predict each mouse’s survival within its diet. They sketch a younger blood: more red cells, more lymphocytes and fewer myeloid cells, more naive T cells and fewer memory T cells, fewer of the B cells that resemble those that age accumulates. And each of these traits, when more pronounced, goes with a longer life, whatever the diet.</p>
<p>Each of these measures carries up to [[cs_part_max]]% of the effect of restriction. Together, they explain the shift of the risk curve, not its slope: a snapshot of the blood at a given age tells where the risk stands, not how fast it rises. For the slope, the cells must be followed over time. In mice fed at will, naive T cells recede with age and memory T cells advance; restriction slows these changes in all four measures, without proof at this size. That is the next lead.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="plan">The plan, written beforehand</h3>
<p>The <a href="/fichiers/cellules-du-sang/plan.md">plan</a> was recorded in the repository history before any calculation linking a measure to survival. It sets the main family (the [[cs_mesures]] blood measures, at their first series after the diets began), two tests, the correction for the number of measures, the rule that designates a candidate measure, and what would refute the lead: no candidate. We knew the abstract of the original paper, which describes the health effects of restriction as uncoupled from longevity.</p>
<h3 id="tests">The two tests</h3>
<p>Test 1, the effect of the diet: in mice fed at will or restricted by 20% or 40%, the measure, transformed into normalized ranks, is regressed on the dose of restriction, the age on the day of measurement and the generation. Test 2, the link with survival: in all measured mice, a Cox model of the death that follows the measurement, at equal diet and generation. A measure is a candidate if it passes both tests after the Benjamini-Hochberg correction (q below 0.05), and if restriction moves it toward the side where the risk of dying is lower.</p>
<h3 id="temoin">The negative control, which did not pass</h3>
<p>The plan included a check: rerun test 1 on the [[cs_t_mesures]] measures taken before the diets began, which restriction cannot have changed. It should have found about 5% significant results and no discovery. It finds [[cs_t_part]]% and [[cs_t_dec]] discoveries: the mice destined for restriction already differed slightly before starting it (their weight at 3 months, for instance: z = [[cs_t_poids]]), and the measures of a same series are linked to one another. Test 1 was therefore too optimistic.</p>
<p>We corrected it after the fact, as the study of the molecules had done for its threshold: its z are divided by the square root of the inflation factor measured on this control, [[cs_t_infl]]. The measures changed by restriction go from [[cs_changees]] to [[cs_changees_cal]], the candidates from [[cs_cand]] to [[cs_cand_cal]]. The effects of restriction also hold when the weight at 3 months is taken into account and, for immune cells, the same measure taken before the diets.</p>
<h3 id="resultats">What we find</h3>
<p>[[cs_liees]] of the [[cs_mesures]] blood measures predict survival within each diet. Among the [[cs_s_mesures]] other measures (heart, body composition, metabolism, strength, activity), restriction changes many ([[cs_s_changees_cal]] after correction), but only [[cs_s_liees]] predict survival, and [[cs_s_cand]] are candidates. The blood says far more about these mice’s future than their metabolism does.</p>
<div class="tableau"><table>
<thead><tr><th>Measure</th><th>Under restriction</th><th>Risk per SD</th><th>Share of the effect</th></tr></thead>
<tbody>
<tr><td>Lymphocytes</td><td>more (z = [[cs_lymph_z1]])</td><td>[[cs_lymph_hr]]</td><td>[[cs_lymph_part]]%</td></tr>
<tr><td>Myeloid cells</td><td>fewer (z = [[cs_myelo_z1]])</td><td>[[cs_myelo_hr]]</td><td>[[cs_myelo_part]]%</td></tr>
<tr><td>Naive CD8 T cells</td><td>more (z = [[cs_cd8n_z1]])</td><td>[[cs_cd8n_hr]]</td><td>[[cs_cd8n_part]]%</td></tr>
<tr><td>Effector-memory CD8 T cells</td><td>fewer (z = [[cs_cd8m_z1]])</td><td>[[cs_cd8m_hr]]</td><td>[[cs_cd8m_part]]%</td></tr>
<tr><td>Naive CD4 T cells</td><td>more (z = [[cs_cd4n_z1]])</td><td>[[cs_cd4n_hr]]</td><td>[[cs_cd4n_part]]%</td></tr>
<tr><td>Effector-memory CD4 T cells</td><td>fewer (z = [[cs_cd4m_z1]])</td><td>[[cs_cd4m_hr]]</td><td>[[cs_cd4m_part]]%</td></tr>
<tr><td>CD11b+ B cells</td><td>fewer (z = [[cs_b11b_z1]])</td><td>[[cs_b11b_hr]]</td><td>[[cs_b11b_part]]%</td></tr>
<tr><td>CD11b− CD11c− NK cells</td><td>more (z = [[cs_nk_z1]])</td><td>[[cs_nk_hr]]</td><td>[[cs_nk_part]]%</td></tr>
<tr><td>CLL-like cells</td><td>fewer (z = [[cs_cll_z1]])</td><td>[[cs_cll_hr]]</td><td>[[cs_cll_part]]%</td></tr>
<tr><td>Red blood cells</td><td>more (z = [[cs_rbc_z1]])</td><td>[[cs_rbc_hr]]</td><td>[[cs_rbc_part]]%</td></tr>
<tr><td>Hemoglobin</td><td>more (z = [[cs_hgb_z1]])</td><td>[[cs_hgb_hr]]</td><td>[[cs_hgb_part]]%</td></tr>
<tr><td>Neutrophils to lymphocytes</td><td>lower (z = [[cs_nlr_z1]])</td><td>[[cs_nlr_hr]]</td><td>[[cs_nlr_part]]%</td></tr>
</tbody>
</table></div>
<p>The risk per standard deviation compares two mice on the same diet whose measure differs by one standard deviation: below 1, the higher measure goes with a longer life. In every row, restriction moves the measure toward the side of lower risk. Lymphocytes and myeloid cells are counted as a share of live cells; CLL: chronic lymphocytic leukemia. The table shows twelve of the [[cs_cand_cal]] candidates; all of them are in the <a href="/fichiers/cellules-du-sang/resultats.json">results file</a>.</p>
<p>The portrait is consistent. CD11b+ B cells resemble the <a href="https://doi.org/10.1182/blood-2011-01-330530">“age-associated” B cells</a> that accumulate in old mice, and age tilts blood production toward myeloid cells (<a href="https://doi.org/10.3389/fimmu.2019.00318">2019 review</a>). Under restriction, these mice’s blood goes the other way.</p>
<h3 id="pente">The shift, not the slope</h3>
<p>Each candidate, added to the Cox model, carries [[cs_part_min]] to [[cs_part_max]]% of the effect of 40% restriction. In the Gompertz model of <a href="/restriction/#modele">the restriction study</a>, the blood-count candidates move the shift factor θ from [[cs_p_cbc_t0]] to [[cs_p_cbc_t1]], the cytometry candidates from [[cs_p_flow_t0]] to [[cs_p_flow_t1]]: they explain the shift of the risk. But the slope does not move the right way: λ goes from [[cs_p_cbc_l0]] to [[cs_p_cbc_l1]], and from [[cs_p_flow_l0]] to [[cs_p_flow_l1]]. Summarized in a single score, the same conclusion (λ = [[cs_ps_cbc_l1]] and [[cs_ps_flow_l1]]).</p>
<p>This is no surprise: a measure taken only once can explain a lower risk at every age, not a risk that rises more slowly. For the slope, one needs a measure whose gap between diets grows with age.</p>
<h3 id="rythme">What changes with age</h3>
<p>The mice measured twice make it possible to look for one. Of the [[cs_r_suivies]] candidates, [[cs_r_changent]] change clearly with age in mice fed at will, between [[cs_age_flow]] days and a year later: naive T cells recede (z = [[cs_r_cd8n_al]] for CD8, [[cs_r_cd4n_al]] for CD4) and effector-memory T cells advance ([[cs_r_cd8m_al]] and [[cs_r_cd4m_al]]). For all [[cs_r_frein]], restriction goes in the direction of a brake, without proving it: the clearest, on effector-memory CD8 cells, gives z = [[cs_r_cd8m_dose]] (p = [[cs_r_p_cd8m]]), in [[cs_r_n]] mice. Only mice still alive at the second measurement count, which can bias the comparison.</p>
<p>To see an effect of this size with a 90% chance, about [[cs_r_cd8m_n90]] mice measured twice would be needed, or more frequent measurements of the same mice. That is the experiment that would link restriction, T cells and the slope of aging; its <a href="/fichiers/cellules-du-sang/protocole.md">protocol</a> says in advance what would refute it.</p>
<h3 id="limites">What this does not say</h3>
<p>An association within a diet is not a cause: a measure can predict death without having anything to do with it. Blood is not the cells of the organs. The negative control showed that the test of the diet’s effect was too optimistic; we corrected it, but the correction is itself an estimate. A single experiment, females, one laboratory. ÆTERNAM has run no experiment: this work comes from public data and calculations anyone can redo.</p>
''',
}

RESTRICTION = {
    'titre': 'Does caloric restriction slow aging?',
    'description': 'In 937 genetically diverse mice, caloric restriction lengthens the time the risk of dying takes to double: it slows aging, where the known molecules delay it. What this would mean in humans, and the trial that would tell.',
    'date': 'November 21, 2026',
    'corps': r'''

<h2 id="explication">Explication</h2>
<p><strong>Does caloric restriction slow aging in mice? Yes.</strong> Eating 40% less, without lacking anything essential, does not just push back the curve of the risk of dying: the curve rises more slowly. The time this risk takes to double is multiplied by [[rs_l40]].</p>
<p>We took the [[rs_souris]] mice of a large study published in 2024: females, all genetically different, fed at will, fasted one or two days a week, or restricted by 20% or 40% from 6 months of age. We applied to them the calculation of <a href="/retarder-ou-ralentir/">our study of the molecules</a>. The contrast is sharp: the [[rs_itp_n]] treatments that extend life delay aging; restriction slows it. Intermittent fasting, for its part, does not change the slope.</p>
<p>In humans, a two-year trial measured a 2 to 3% slowing of the pace of aging, read in the blood. Converted on the American life table, it would add [[rs_h_c2_h]] to [[rs_h_c3_f]] years to the median age at death. If humans responded like mice, it would be [[rs_h_s20_h]] to [[rs_h_s40_f]] years. The trial that would tell which of the two is true is calculated: [[rs_n_total]] people, three years.</p>
<p>Restriction is not a remedy: at 40%, the mice lose lean mass and their immune system changes. It is the proof that the slope of aging can be set in a mammal. What remains is to find what it changes in cells, to obtain the same effect another way.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="donnees">The data</h3>
<p><a href="https://doi.org/10.1038/s41586-024-08026-3">Di Francesco and colleagues</a> followed 960 female Diversity Outbred mice until death, each with its own genome. At 6 months, [[rs_souris]] were alive: [[rs_al_n]] fed at will, [[rs_1d_n]] fasted one day a week, [[rs_2d_n]] two days, [[rs_20_n]] restricted by 20% and [[rs_40_n]] by 40%. Their individual lifespans are published under an open license; the [[rs_censurees]] mice removed for injuries are censored.</p>
<p>To check our reading, we redo their main result: with 40% restriction, median life is 36.3% longer according to the paper. We find [[rs_gain40]]% ([[rs_med_40]] days against [[rs_med_al]]).</p>
<h3 id="modele">The calculation</h3>
<p>It is the one of <a href="/retarder-ou-ralentir/#modele">the study of the molecules</a>. The risk of dying follows <code>h(t) = a·exp(b·t)</code>. A diet that delays divides it by the same factor θ at every age; a diet that slows makes time run λ times more slowly from 6 months on, which multiplies the doubling time by λ. The general model contains both. Each diet is compared with the mice fed at will, whose risk doubles in about [[rs_dbl]] days; mice enter the calculation at 365 days.</p>
<h3 id="resultat">What we find</h3>
<div class="tableau"><table>
<thead><tr><th>Diet</th><th>Median life</th><th>λ</th><th>95% interval</th></tr></thead>
<tbody>
<tr><td>40% restriction</td><td>+[[rs_gain40]]%</td><td>[[rs_l40]]</td><td>[[rs_l40_bas]] to [[rs_l40_haut]]</td></tr>
<tr><td>20% restriction</td><td>+[[rs_gain20]]%</td><td>[[rs_l20]]</td><td>[[rs_l20_bas]] to [[rs_l20_haut]]</td></tr>
<tr><td>Two fasting days a week</td><td>+[[rs_gain2d]]%</td><td>[[rs_l2d]]</td><td>[[rs_l2d_bas]] to [[rs_l2d_haut]]</td></tr>
<tr><td>One fasting day a week</td><td>+[[rs_gain1d]]%</td><td>[[rs_l1d]]</td><td>[[rs_l1d_bas]] to [[rs_l1d_haut]]</td></tr>
</tbody>
</table></div>
<p>With 40% restriction, slowing alone is enough to describe the data (gap to the general model: [[rs_x2ral_40]]), and delay alone is rejected (gap: [[rs_x2_40]], above the usual threshold of 3.84, below the corrected threshold of 6.99 from the study of the molecules; with the frailty below, [[rs_x2_40_f]], above both). With 20%, the effect goes the same way, weaker: its interval touches 1. Fasting lengthens median life without visibly changing the slope.</p>
<h3 id="fragilite">The frailty check</h3>
<p>Not all mice are equally frail. A treatment that first saves the frailest can change the shape of the curve without changing aging at all. Our simulations show it (these are not measurements): on heterogeneous mice generated with a pure delay, the calculation without frailty returns λ = [[rs_sim_het]] instead of 1; with an individual frailty (gamma-Gompertz model), it returns [[rs_sim_het_f]].</p>
<p>So we redid everything with this frailty. 40% restriction: λ = [[rs_l40_f]] ([[rs_l40_f_bas]] to [[rs_l40_f_haut]]). The [[rs_itp_n]] ITP treatments: mean λ [[rs_itp_lf]] ([[rs_itp_lf_bas]] to [[rs_itp_lf_haut]]) instead of [[rs_itp_l]]; rapamycin moves to [[rs_itp_rapa]] at the median. Part of the shortening seen with the molecules came from frailty, but no slowing appears: [[rs_itp_ral]] out of [[rs_itp_n]].</p>
<h3 id="sensibilite">How far the result holds</h3>
<p>If mice enter the calculation from 6 months instead of 365 days, λ is [[rs_l40_6m]] for 40% restriction. If ages beyond [[rs_c90_jours]] days, where the oldest 10% die, are cut off, λ falls to [[rs_l40_c90]] and is no longer distinct from 1: a good part of the signal comes from the restricted mice that live the longest. That is what a slowing should produce, since it yields more days the older one lives, but it is a reminder that the result rests on a single experiment, in females, in a single laboratory.</p>
<p>It is not a discovery: the authors themselves report a lower rate of aging under restriction, and not under fasting. Others had seen it on published curves of rats and mice (<a href="https://doi.org/10.1111/acel.12061">Simons and colleagues, 2013</a>). What we add: the same calculation for restriction and for every molecule in the ITP, the frailty check, and the conversion to humans.</p>
<h3 id="primate">In primates</h3>
<p>Two large studies of restriction in macaques long seemed to contradict each other: one saw better survival, the other did not. <a href="https://doi.org/10.1038/ncomms14063">Brought together in 2017</a>, they conclude that moderate restriction improves health and survival. We do not have their individual data: their slope is not calculated.</p>
<h3 id="humain">In humans</h3>
<p>In the randomized <a href="https://doi.org/10.1038/s43587-022-00357-y">CALERIE</a> trial, 220 adults aged 21 to 50 followed a prescribed 25% restriction for two years, or their usual diet. They achieved only 11.9% on average. The pace of aging read in the blood (DunedinPACE, derived from the change in 19 measures of the blood and organs) slowed by 2 to 3%; for 20% restriction actually achieved, the effect is about [[rs_rapport]] times larger. The other clocks did not move, and mortality was not measured.</p>
<p>We converted these effects into years on the 2023 American life table, by slowing from age 40 the part of the risk that rises with age. The background risk, that of a 10-year-old child, stays as it is. These are calculations on assumptions, not forecasts: DunedinPACE is not mortality, and nothing says that an effect measured over two years lasts a lifetime.</p>
<div class="tableau"><table>
<thead><tr><th>Assumed slowing</th><th>Where it comes from</th><th>Extra years, men</th><th>Extra years, women</th></tr></thead>
<tbody>
<tr><td>2%</td><td>CALERIE, low end of the range</td><td>[[rs_h_c2_h]]</td><td>[[rs_h_c2_f]]</td></tr>
<tr><td>3%</td><td>CALERIE, high end of the range</td><td>[[rs_h_c3_h]]</td><td>[[rs_h_c3_f]]</td></tr>
<tr><td>λ = [[rs_h_l20]]</td><td>CALERIE, 20% restriction achieved</td><td>[[rs_h_20_h]]</td><td>[[rs_h_20_f]]</td></tr>
<tr><td>λ = [[rs_l20]]</td><td>Mice, 20% restriction</td><td>[[rs_h_s20_h]]</td><td>[[rs_h_s20_f]]</td></tr>
<tr><td>λ = [[rs_l40]]</td><td>Mice, 40% restriction</td><td>[[rs_h_s40_h]]</td><td>[[rs_h_s40_f]]</td></tr>
</tbody>
</table></div>
<h3 id="jusqu-ou">Where this leads</h3>
<p>If aging ran twice as slowly after age 40, the median age at death would go from [[rs_h_med_h]] to [[rs_h_x2_h]] years in men, from [[rs_h_med_f]] to [[rs_h_x2_f]] years in women. Ten times more slowly: [[rs_h_x10_h]] and [[rs_h_x10_f]] years. A hundred times: [[rs_h_x100_h]] and [[rs_h_x100_f]] years. Beyond that, it is no longer aging that kills, but the background risk: accidents, infections, diseases of every age. Stopping aging is not enough to live forever; it is by far the biggest step.</p>
<h3 id="cellules">What restriction changes in cells</h3>
<p>Restriction proves that the slope can be set; it does not say how. In the blood measurements of the same mice, with a plan recorded before looking at survival, we looked for those that change under restriction and predict survival within each diet: [[cs_cand_cal]] out of [[cs_mesures]]. <a href="/cellules-du-sang/">The blood of restricted mice is younger</a>: more naive T cells, fewer myeloid cells. These measures explain the shift of the risk, not yet its slope: for the slope, T cells will have to be followed over time.</p>
<h3 id="essai">The trial that would settle it in humans</h3>
<p>Two randomized groups, aged 40 to 65, the age at which this risk, which doubles about every eight years, becomes large: a supervised 20% restriction, or the usual diet, for three years. Primary criterion: DunedinPACE at 36 months, with the 19 measures it is derived from, so as not to depend on a single clock. To see the CALERIE effect with a 90% chance, [[rs_n_itt]] people per group are needed, [[rs_n_recr]] to recruit if one in five drops out: [[rs_n_total]] in all. If the effect is that of 20% restriction achieved, [[rs_n_20]] per group would suffice. The result that would refute the hypothesis: a 95% interval that excludes a slowing of 1% or more.</p>
<p>In mice, a second experiment would check the slope in males and in another laboratory. Our simulations give, to see a slowing of 1.25 at the corrected threshold, a [[rs_p150]]% chance with 150 mice per group, [[rs_p300]]% with 300, [[rs_p450]]% with [[rs_n450]] and [[rs_p600]]% with 600. The <a href="/fichiers/restriction/protocole.md">protocol</a> details both experiments and the analysis of cells. ÆTERNAM has run no experiment: this work comes from public data and calculations anyone can redo.</p>
<h3 id="limites">What this does not say</h3>
<p>A single mouse experiment, females, one laboratory, an analysis done after seeing the data. The Gompertz model is an approximation. The conversion to humans assumes that the pace read in the blood follows the slope of mortality, which is not demonstrated. Severe restriction is not something to practice without medical supervision. Not demonstrated in humans does not mean impossible: that is what the trial would tell.</p>
''',
}

RETARDER = {
    'titre': 'Do the molecules that extend life slow aging?',
    'description': 'Across 36,975 mice from the American testing program, 27 treatments extend life and, for none, a lengthening of the doubling time of the risk of dying is established: they delay aging, they do not slow it.',
    'date': 'November 20, 2026',
    'corps': r'''

<h2 id="explication">Explication</h2>
<p><strong>Do the molecules that extend the life of mice slow their aging? No: they delay it.</strong> The difference matters. Slowing would mean lengthening the time the risk of dying takes to double. Delaying means pushing the same curve back by a few months: the risk still doubles just as fast, it only starts later.</p>
<p>We took the lifespans of [[rr_souris]] mice, published one by one by the American program that has tested these molecules since 2004. Out of [[rr_comparaisons]] comparisons between a treated group and its controls, [[rr_efficaces]] treatments clearly extend life: rapamycin, acarbose, 17‑α‑estradiol, canagliflozin and a few others.</p>
<p>For none of the [[rr_efficaces]] is a lengthening of the doubling time of the risk established. That time is even [[rr_racc]]% shorter on average in treated mice: deaths are pushed back, then they catch up. Part of this gap comes from the fact that not all mice are equally frail; corrected, it remains [[rf_racc]]%. At the median, these treatments gain [[rr_gain_med]] days; for the mice that live longest, [[rr_gain_90]].</p>
<p>This result says where the frontier is. The known molecules buy time; none touches the slope yet. Changing it is what every future experiment, ours included, will have to measure. None of this holds for humans, in whom none of these molecules has extended life in a trial.</p>
<h2 id="analyse">Detailed analysis</h2>
<h3 id="donnees">The data</h3>
<p>The National Institute on Aging’s <a href="https://phenome.jax.org/projects/ITP1">Interventions Testing Program</a> gives the same molecules, in food, to genetically heterogeneous mice (UM-HET3) raised in three laboratories. Its individual data are public. We took the [[rr_cohortes]] cohorts from 2004 to 2021: [[rr_groupes]] treated groups, [[rr_souris]] mice, of which [[rr_mortes]] were followed until death and [[rr_retirees]] were removed during the study.</p>
<p>To check that we read these data as their authors do, we redid a published result: rapamycin given at 600 days pushes back the age reached by the oldest 10% by <a href="https://doi.org/10.1038/nature08221">14% in females and 9% in males</a>. Our reading gives [[rr_h_f]]% and [[rr_h_m]]%.</p>
<h3 id="modele">Two ways to extend a life</h3>
<p>The risk of dying of an adult mouse grows roughly as an exponential of age: <code>h(t) = a·exp(b·t)</code>. The doubling time is <code>ln 2 / b</code>; in the controls of these cohorts, it is about [[rr_doublement]] days. A treatment that delays divides the risk by the same factor at every age: <code>h₁(t) = θ·h₀(t)</code>. The curve is shifted, its slope does not change. A treatment that slows makes time run λ times more slowly from its start, at age s: <code>h₁(t) = (1/λ)·h₀(s + (t − s)/λ)</code>. The doubling time is multiplied by λ.</p>
<p>A general model contains both: <code>h₁(t) = θ·a·exp(b·s)·exp((b/λ)(t − s))</code>. Delay is the case λ = 1, slowing the case θ = 1/λ. Each treated group is compared with the controls of its cohort and sex, with a baseline curve specific to each laboratory. Mice enter the calculation at the start of treatment, or at 365 days if it starts earlier. A treatment is retained if it lowers the risk and passes the threshold of 0.05 divided by the [[rr_comparaisons]] comparisons.</p>
<h3 id="resultat">What we find</h3>
<p>[[rr_efficaces]] treatments are retained: 11 of rapamycin alone, 4 of rapamycin with acarbose, 2 of rapamycin with metformin, 5 of acarbose, 2 of 17‑α‑estradiol, 1 of canagliflozin, 1 of nordihydroguaiaretic acid and 1 of 16‑α‑hydroxyestriol. For the last five molecules, only groups of males pass the threshold.</p>
<p>Slowing alone is rejected for [[rr_ral]] of them ([[rr_ral_theo]] at the usual threshold). Delay alone is rejected for [[rr_ret]] ([[rr_ret_theo]] at the usual threshold), and each time in the same direction: a shorter doubling time, not a longer one. The number of treatments for which a lengthened doubling is established is [[rr_allonge]].</p>
<p>Across the [[rr_grappes]] cohort and sex pairs concerned, the ratio of doubling times averages λ = [[rr_lambda]] (95% interval: [[rr_lambda_bas]] to [[rr_lambda_haut]]), that is a doubling [[rr_racc]]% shorter ([[rr_racc_bas]] to [[rr_racc_haut]]). If these treatments slowed aging, λ would have to lie between [[rr_lr_min]] and [[rr_lr_max]] to explain their effects.</p>
<h3 id="sans-modele">The same finding without a model</h3>
<p>Slowing gives all the more days the older one lives. That is not what we see. The age at which half the mice have died moves back by [[rr_gain_med]] days (median of the [[rr_efficaces]] treatments); the age at which 90% have died, by [[rr_gain_90]] days. For [[rr_gain_n]] treatments out of [[rr_efficaces]], the gain is smaller in the oldest than at the median.</p>
<h3 id="controles">Can the calculation be wrong?</h3>
<p>First check, on the data: among the [[rr_nuls]] comparisons where the treatment does nothing, the test should reject delay in 5% of cases. It does so in [[rr_etal]]%: the model is an approximation, and the test is too sensitive. We therefore raised its threshold from 3.84 to [[rr_seuil]], the value that 5% of these comparisons exceed. The counts above use this threshold.</p>
<p>Second check, by numerical simulation (these are not measurements): on mice generated with a pure delay, the calculation returns λ = [[rr_sim_ret]]; with a slowing of 1.22, it returns [[rr_sim_ral]]. It does not confuse the two. But a single comparison the size of those in the program is not always enough: it rules out the wrong model [[rr_sim_p_ral]]% of the time in the first case, [[rr_sim_p_ret]]% in the second. It is the whole set of [[rr_efficaces]] treatments that carries the conclusion.</p>
<p>Third check, added on November 21, 2026: not all mice are equally frail, and a treatment that first saves the frailest steepens the curve without changing aging at all. On mice simulated this way, with a pure delay, the calculation returns λ = [[rf_sim_het]]. Redone with an individual frailty, the mean λ of the [[rr_efficaces]] treatments is [[rf_lambda]] ([[rf_lambda_bas]] to [[rf_lambda_haut]]); rapamycin moves to [[rf_rapa]] at the median. The shortening shrinks, and no slowing appears: [[rf_ral]] treatment out of [[rr_efficaces]]. The details are in <a href="/restriction/#fragilite">the restriction study</a>.</p>
<h3 id="limites">What this does not say</h3>
<p>This is an exploratory analysis, done after seeing the data, with no plan filed in advance. It covers a single mouse stock and treatments started in adulthood. Groups in the same cohort share their controls. Not demonstrated does not mean impossible: a treatment that lengthens the doubling time is not ruled out, it is not in these data.</p>
<p>Others had seen it on published curves: in mice, reducing the pathway that rapamycin targets <a href="https://doi.org/10.1111/acel.12489">pushes back the onset of aging without changing the shape of the curve</a>. What we add: the individual data, every molecule in the program, and the finding that the slope lengthens for none. Conversely, dietary restriction in rodents <a href="https://doi.org/10.1111/acel.12061">reduces the rate of aging</a>, which <a href="/restriction/">we checked mouse by mouse</a>, and in worms, very different interventions <a href="https://doi.org/10.1038/nature16550">stretch time</a>. Slowing is therefore not out of reach for living things.</p>
<h3 id="suite">What this changes</h3>
<p>Extending life is not enough to say that aging has been slowed. The criterion is the doubling time of the risk, and it is measured with the same mice. <a href="/combinaisons/">The two-molecule experiment we calculated</a> will have to report it. Caloric restriction, for its part, lengthens it: <a href="/restriction/">λ = [[rf_r40]]</a>. And the strongest lead, <a href="/vieillir/#zero">the reset the embryo performs</a>, will be judged on it. ÆTERNAM has run no experiment: this result comes from public data and a calculation anyone can redo.</p>
''',
}

VIEILLIR = {
    'titre': 'Why do we age, and can it be stopped?',
    'description': 'The risk of dying doubles every eight years, but that is not a law of nature: what biology knows about aging, about its reset, and about the experiments that remain to be done.',
    'date': 'November 20, 2026',
    'corps': r'''

<h2 id="explication">Explanation</h2>
<p><strong>Why do we die? First of all because we age.</strong> At age ten, the risk of dying within the year is about one in ten thousand. If it stayed there for life, one person in two would live more than [[v_med_h]] years. What kills us is not time: it is that this risk doubles every eight to ten years.</p>
<p>That doubling is not a law of nature. Hydra followed for eight years in the laboratory do not show it. A shark lives at least 272 years. Aging is a trait of living things, set differently from one species to another: what is set can be set differently.</p>
<p>We also know it is not a one-way street. Every child is born young from cells that are as old as its parents: early in the embryo’s life, the biological age of cells goes back down. And four genes are enough to bring an adult cell back to that state. The reset exists, and we know one of its switches.</p>
<p>What we cannot do yet is trigger it in a whole body without putting it in danger. In the meantime, molecules already extend the life of mice: they delay their aging, without slowing it. In humans, nothing is demonstrated. That is where the work remains, and it is precise: experiments we know how to describe, and that need funding.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="risque">The risk that doubles</h3>
<p>The doubling time of the risk of dying in humans is <a href="https://doi.org/10.1126/science.2392680">about 8 years</a>. On the 2023 American life table, the line fitted between ages 30 and 90 gives [[v_doub_f]] years for women and [[v_doub_h]] years for men. If the risk at age ten stayed constant, half of a group would still be alive after [[v_med_h]] years (men) or [[v_med_f]] years (women). This is a calculation on an assumption, not a forecast: it measures how much of death is due to aging.</p>
<h3 id="loi">It is not a law</h3>
<p>In <a href="https://doi.org/10.1073/pnas.1521002112">2,256 hydra</a> followed in two laboratories, mortality stayed low and constant; the authors do not rule out aging beyond the period observed. The <a href="https://doi.org/10.1126/science.aaf1703">Greenland shark</a> lives at least 272 years. In the <a href="https://doi.org/10.7554/eLife.31157">naked mole-rat</a>, the risk does not rise with age across 3,299 animals, a contested result.</p>
<p>One result links these gaps to a mechanism. Across <a href="https://doi.org/10.1038/s41586-022-04618-z">sixteen mammalian species</a>, lifespan varies about 30-fold, but the number of mutations a cell has accumulated by the end of life varies only about 3-fold. Species that live long damage their DNA more slowly.</p>
<h3 id="marques">What ages</h3>
<p>Biology today describes <a href="https://doi.org/10.1016/j.cell.2022.11.001">twelve hallmarks of aging</a>: genomic instability, telomere attrition, epigenetic alterations, loss of proteostasis, disabled macroautophagy, deregulated nutrient-sensing, mitochondrial dysfunction, cellular senescence, stem cell exhaustion, altered intercellular communication, chronic inflammation, dysbiosis. It is a classification, not a single cause.</p>
<p>Two of these hallmarks have been tested directly. Normal human cells, placed in culture, <a href="https://doi.org/10.1016/0014-4827(65)90211-9">have only a limited lifetime</a>. And in mice modified so that their senescent cells can be eliminated, <a href="https://doi.org/10.1038/nature16932">median life increases by 24 to 27%</a>.</p>
<h3 id="zero">The reset</h3>
<p>Measured with epigenetic clocks, <a href="https://doi.org/10.1126/sciadv.abg6082">biological age decreases</a> early in the development of the embryo, in mice and in humans, then increases. Pluripotent stem cells, for their part, do not age, even after many passages in culture. The aging of a cell is therefore not irreversible by nature.</p>
<h3 id="interrupteur">A known switch</h3>
<p><a href="https://doi.org/10.1016/j.cell.2006.07.024">Four factors</a> are enough to bring an adult mouse cell back to the pluripotent state. Three of them, expressed in the retina of aged mice, <a href="https://doi.org/10.1038/s41586-020-2975-4">reversed a loss of vision</a>. In mice with accelerated aging, partial expression <a href="https://doi.org/10.1016/j.cell.2016.11.052">extended life</a>. But triggered without control in a whole animal, the same factors <a href="https://doi.org/10.1038/nature12586">produce tumors</a>. It is the strongest lead and the least mastered. Another sign that the state of an old cell depends on its environment: joined to the circulation of a young mouse, <a href="https://doi.org/10.1038/nature03260">the stem cells of an aged muscle</a> regain their capacity to regenerate.</p>
<h3 id="ralentir">Delaying, already</h3>
<p>A mutation in a single gene makes a worm live <a href="https://doi.org/10.1038/366461a0">more than twice as long</a>. In mice, rapamycin given from 600 days of age pushes back the age reached by the oldest 10% by <a href="https://doi.org/10.1038/nature08221">14% in females and 9% in males</a>. Two molecules together do better: that is the subject of <a href="/combinaisons/">our first lead</a>. But these molecules delay aging without slowing it: on the data of 36,975 mice, <a href="/retarder-ou-ralentir/">the doubling time of the risk lengthens in an established way for none of them</a>.</p>
<h3 id="humain">In humans</h3>
<p>No trial has shown that an intervention extends human life or reverses aging. Two years of calorie restriction <a href="https://doi.org/10.1038/s43587-022-00357-y">slowed a blood marker of the pace of aging</a>, with a small effect and no measure of mortality. Not demonstrated does not mean impossible: the decisive experiments have not been done.</p>
<h3 id="pistes">What remains to be done</h3>
<p>Three questions have a known experiment. Do two molecules do better than add up? <a href="/combinaisons/">Four groups of mice would tell.</a> Can the reset be triggered in a whole animal without tumors? That is the central question, and we have not yet worked it through. And if the body gives out first, can we keep what a brain holds? <a href="/lecture-cerveau/">A blind test would tell.</a> ÆTERNAM has run no experiment: this text gathers published results and one calculation.</p>
''',
}

LECTURE_CERVEAU = {
    'titre': 'Can a memory be read from a preserved brain?',
    'description': 'Learning survives vitrification in a worm; a memory shows in the structure in mice. The blind test that links the two is missing: here is its calculation.',
    'date': 'November 20, 2026',
    'corps': r'''

<h2 id="explication">Explanation</h2>
<p><strong>Does a memory leave a trace that can be read from a preserved brain? Nobody has shown it yet.</strong> Three results say the question can be settled.</p>
<p>First result: learning survives preservation by cold. Worms that had been taught an odor, then vitrified and revived, remembered it as adults. Second result: in mice, a memory changes the shape of the connections between neurons, and that change shows under the electron microscope. Third result: we know how to preserve a whole mammalian brain without damaging those connections, but the brain is then fixed, and therefore dead.</p>
<p>The experiment that links the three is missing: take preserved brains, without knowing which come from animals that learned, and find out by looking at their structure. The most advanced microscopy study covered five mice. With five brains, a reader who is right four times out of five has only a [[lc_p5]]% chance of proving it.</p>
<p>We calculated what is needed: [[lc_n80_90]] brains, of which [[lc_k80_90]] correctly recognized. If this test succeeds, we will know that a specific memory can be read from a preserved brain. If it fails, we will know that the visible structure is not enough.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="resultats">What is published</h3>
<p><a href="https://doi.org/10.1089/rej.2014.1636">Vita-More and Barranco</a> gave young <em>C. elegans</em> worms an olfactory imprint, vitrified them at the next stage, then revived them. As adults, their behavior kept the trace of the learned odor. This worm has 302 neurons, and an erratum was published in 2022.</p>
<p><a href="https://doi.org/10.1126/science.ado8316">Uytiepo and colleagues</a> reconstructed a pathway of the mouse hippocampus in three-dimensional electron microscopy, after labeling the neurons recruited during learning. About 26% of the multisynaptic terminals of those neurons contact more than two spines, against 11% for the others. The reconstructions cover three conditioned mice and two controls.</p>
<p><a href="https://doi.org/10.1016/j.cryobiol.2015.09.003">Aldehyde-stabilized cryopreservation</a> was applied to whole rabbit and pig brains, fixed and then vitrified at −135&nbsp;°C. After rewarming, the connections remain traceable under the microscope. Fixation kills the cells: this preserves structure, not life.</p>
<h3 id="manque">What is missing</h3>
<p>In the 2025 study, the neurons of the memory were labeled before the analysis: one knew where to look. No study has yet asked a reader who knows nothing about the animal to say, from structure alone, whether it had learned. A <a href="https://doi.org/10.3389/fmedt.2024.1400615">2024 review</a> notes it: memories cannot yet be reproducibly decoded from a static brain.</p>
<h3 id="experience">The blind test</h3>
<p>Mice assigned at random: half learn an association, the other half see the same place without learning anything. The brains are preserved, coded, imaged in the same region. The reader gives one answer per brain, then the codes are opened. By chance, the reader is right one time in two.</p>
<p>If the reader is right four times out of five, [[lc_n80_90]] brains are needed for a 90% chance of proving it, with at least [[lc_k80_90]] correct answers. If right nine times out of ten, [[lc_n90_90]] are enough. If only seven times out of ten, [[lc_n70_90]] are needed. The <a href="/fichiers/lecture-cerveau/protocole.md">protocol</a> (in French) fixes the measurements and the decision rule before the codes are opened.</p>
<h3 id="pilote">A pilot step first</h3>
<p>This calculation assumes a reader right four times out of five, and nothing guarantees it: in 2025, the trace was read on labeled neurons, and without labeling it is drowned among those that played no part. Before the [[lc_n80_90]] brains, a pilot step will measure the gap in six mice whose learning neurons are labeled, first on those neurons, then on all of them, ignoring the labeling. The expected accuracy without labeling will set the number of brains; if the gap disappears, the test will not be launched, and we will say so.</p>
<p>For humans, a brain would still have to be preserved at death without losing its structure, which has not been demonstrated for a reading, and imaged at the scale of synapses: <a href="https://doi.org/10.1126/science.adk4858">a single cubic millimeter of human cortex</a> required 1.4 petabytes of images. It is the fallback. ÆTERNAM’s main path is to <a href="/restriction/">slow</a>, then repair, the aging of cells, so as to have nothing to preserve.</p>
<h3 id="limites">Limits</h3>
<p>Recognizing that an animal learned is not reading what it learned: it is the first step. The worm result has not, to our knowledge, been reproduced by another team. A reader’s real accuracy is unknown: sample sizes are given for three assumptions. And none of this revives a brain: the question is about the information preserved. ÆTERNAM has run no experiment.</p>
''',
}

COMBINAISONS = {
    'titre': 'Are two molecules better than one?',
    'description': 'In mice, rapamycin and trametinib given together extend life more than either alone. Do their effects add up, or do better? The calculation of the experiment that would settle it.',
    'date': 'November 20, 2026',
    'corps': r'''

<h2 id="explication">Explanation</h2>
<p><strong>Can a mammal’s life be extended with molecules? In mice, yes.</strong> Rapamycin extends their life, and so does trametinib. In 2025, a team in Cologne gave both at once: the mice lived longer still.</p>
<p>The question that matters is this. If two molecules act on the same mechanism, the second adds almost nothing. If their effects add up, they can be stacked. If they do better than add up, there is a combination stronger than anything tried so far.</p>
<p>We redid the count from the published numbers. In males, the effects add up. In females, the combination extends median life by [[cb_f_obs]]%, whereas the sum of the two effects would give [[cb_f_att]]%. The gap is large. But the study did not have enough mice to say whether it is real or due to chance: it had a [[cb_f_puiss]]% chance of seeing it.</p>
<p>So we calculated the experiment that would settle it: four groups of [[cb_groupe_90]] female mice, followed until death. That is more than twice what the study used. None of this applies to humans, in whom no molecule has extended life in a trial.</p>
<p>Since then, we have learned that these molecules delay aging without slowing it, and that caloric restriction, for its part, slows it. The protocol has therefore changed: the slope becomes a primary criterion, and we propose crossing restriction with rapamycin.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="resultats">What is published</h3>
<p><a href="https://doi.org/10.1038/s43587-025-00876-4">Gkioni and colleagues</a> followed four groups of mice run at the same time: controls, rapamycin, trametinib, and both. In females (100 controls, 98 mice per treated group), median life increases by 7.2% with trametinib, by 17.4% with rapamycin and by 34.9% with both. In males (120 or 121 per group): 10.2%, 16.6% and 27.4%. The authors conclude that the effects are additive, with no interaction between the two molecules.</p>
<p>A second result points the same way, with a reservation. In the American program that tests these molecules at three sites, <a href="https://doi.org/10.1111/acel.13724">rapamycin combined with acarbose</a> extended median life by 34% in males and by 28% in females. But rapamycin alone came from older experiments, not from the same mice: the comparison does not prove an addition.</p>
<h3 id="addition">Counting the addition</h3>
<p>On medians, the sum of the two effects gives [[cb_f_att]]% in females, against [[cb_f_obs]]% observed, and [[cb_m_att]]% in males, against [[cb_m_obs]]% observed.</p>
<p>The correct measure concerns the risk of dying. The study gives the effect of trametinib alone, and its effect in mice already receiving rapamycin. The ratio of the two is 1 if the effects add up, less than 1 if the combination does better. It is [[cb_f_inter]] in females and [[cb_m_inter]] in males.</p>
<p>In females, this gap corresponds to p&nbsp;=&nbsp;[[cb_f_p]]: it is not established. Our uncertainty is rebuilt from the published intervals, treating the two estimates as independent, which is an approximation. With that uncertainty, the study had only a [[cb_f_puiss]]% chance of detecting an interaction of this size. The absence of a proven interaction therefore does not show the absence of an interaction.</p>
<h3 id="experience">The experiment that would settle it</h3>
<p>A design with four equal groups, run at the same time: controls, each molecule alone, both. To establish an interaction of [[cb_f_inter]], one must observe [[cb_morts_80]] deaths to have an 80% chance of seeing it, and [[cb_morts_90]] for 90%, that is [[cb_groupe_90]] mice per group followed until death. If the real interaction is weaker, 0.75 for example, [[cb_morts_075_90]] are needed.</p>
<p>The <a href="/fichiers/combinaisons/protocole.md">protocol</a> (in French) specifies the mice, both sexes, the criteria fixed before starting and what would refute the hypothesis. ÆTERNAM has run no experiment: this work is a calculation on published results, and a plan ready to be funded.</p>
<h3 id="revision">Revision of November 21, 2026: aiming at the slope</h3>
<p><a href="/retarder-ou-ralentir/">Our study of the molecules</a> shows that rapamycin, like the other treatments of the American program, delays aging without slowing it. <a href="/restriction/">Caloric restriction</a>, for its part, slows it. Two molecules that delay, given together, should delay more: that does not, in itself, aim at the slope. Trametinib is not in that program, and without the individual lifespans of the Cologne study, its slope remains unknown.</p>
<p>The protocol therefore changes on two points. The slope becomes a primary criterion, measured as in our study, with its corrected threshold. And more mice are needed to see it: according to our simulations, a slowing of 1.25 has a [[rs_p150]]% chance of being seen with 150 mice per group, [[rs_p300]]% with 300, and [[rs_p450]]% with [[rs_n450]].</p>
<p>We also propose another plan: crossing restriction and rapamycin, the only intervention that slows and the most tested molecule, which delays. If a delay and a slowing add up, the combination shifts the curve and changes its slope. <a href="https://doi.org/10.1093/gerona/glz060">A review predicted it</a>, and in the muscle of old mice, the effects of the two <a href="https://doi.org/10.1038/s41467-022-29714-6">add up</a>; we have found no published lifespan crossing the two. The <a href="/fichiers/combinaisons/protocole.md">revised protocol</a> gives both plans.</p>
<h3 id="limites">Limits</h3>
<p>The numbers come from a single study, on a single strain of mice, in a single laboratory. We do not have the data for each animal: the uncertainty of the interaction is approximate. An interaction in females only may be chance, since two sexes were examined. Trametinib is an anticancer drug, with known adverse effects in humans. Nothing here says that a person would live longer by taking these molecules.</p>
''',
}

SUJETS = {
    'vieillissement': {
        'chemin': '/sujets/vieillissement/',
        'titre': 'Aging',
        'question': 'Can we stop aging?',
        'enjeu': 'To age is to see your risk of dying double about every eight years. Everything else follows from that.',
        'reponse': 'In mice, we already know how to slow it: two molecules given together extended the median life of females by [[cb_f_obs]]%. In humans, nothing is demonstrated. We calculated the experiment that would say whether these effects do better than add up: [[cb_morts_90]] deaths to observe. It remains to be funded.',
        'sources': ('/combinaisons/',), 'lien': '/vieillir/',
        'description': 'What causes aging, what slows it in animals, and the experiments that remain to be run.',
        'intro': '<p>Some species do not age, or barely. In mice, molecules extend life. This topic gathers what is demonstrated, what is not, and the experiments ready to be funded.</p>',
        'questions': (
            'Why does the risk of dying rise with age?',
            'Do the effects of two molecules add up?',
            'What, in animals, also holds for humans?',
        ),
        'lectures': (
            ('/vieillir/#explication', 'Why do we age, and can it be stopped?'),
            ('/vieillir/#zero', 'The reset: what the embryo does'),
            ('/retarder-ou-ralentir/#explication', 'Delaying is not slowing: 36,975 mice'),
            ('/combinaisons/#explication', 'Are two molecules better than one?'),
            ('/combinaisons/#experience', 'The experiment that would settle it, and its sample sizes'),
        ),
    },
    'memoire': {
        'chemin': '/sujets/memoire/',
        'titre': 'Memory',
        'question': 'Can we keep a memory forever?',
        'enjeu': 'A person is, first of all, their memories. Keeping them is already a way to last.',
        'reponse': 'Not in the brain, not yet. Trials sometimes help it retain what it is shown, and sometimes get in the way. Nobody knows how to copy a memory, or how to write one.',
        'sources': ('/interfaces-cerveau/',), 'lien': '/interfaces-cerveau/#memoire',
        'description': 'Forming, strengthening or altering a memory; understanding what links recall, narrative and lived experience.',
        'intro': '<p>A memory can be a piece of learned information, a personal event or a feeling of familiarity. This thread looks at interventions on memory, artificial memories and the link between memory, dreaming and identity.</p>',
        'questions': (
            'What have memory-modification experiments actually shown?',
            'Does remembering a long story mean having lived it?',
            'How can recall and continuity be assessed without confusing their measures?',
        ),
        'lectures': (
            ('/interfaces-cerveau/#memoire', 'What memory interventions allow us to conclude'),
            ('/interfaces-cerveau/#vingt-ans', 'The twenty-year question: memory, belief and lived duration'),
            ('/programme/#memoire', 'Studying dream recall and the missing data'),
        ),
    },
    'bci': {
        'chemin': '/sujets/interfaces-cerveau-machine/',
        'titre': 'Brain-computer interfaces',
        'question': 'Can we read a brain?',
        'enjeu': 'To keep, one day, what a brain holds, we first have to know how to read it.',
        'reponse': 'A simple intention, yes: a movement you imagine. But every brain is different. Our program, trained on other people, is right [[bci_nouvelle]]% of the time on someone new. A coin toss gets 50%.',
        'sources': ('/bci-generalisation/',), 'lien': '/bci-generalisation/',
        'description': 'Reading brain activity, communicating with a machine and understanding what an interface can actually decode.',
        'intro': '<p>BCIs connect the brain to a computer system. This thread gathers research on decoding, EEG and MEG sensors, implants and interfaces that combine measurement and intervention.</p>',
        'questions': (
            'What information can be extracted from the brain signal, and under what conditions?',
            'What difference do sensors, training data and AI models make?',
            'How can one contribute with open data and reproducible results?',
        ),
        'lectures': (
            ('/interfaces-cerveau/#lire-ecrire', 'The difference between reading activity and causing an effect'),
            ('/meg-eeg-reves/#brain2qwerty', 'What EEG and MEG decoders have demonstrated'),
            ('/bci-monte-carlo/#resultats', 'Our simulation of calibration and noise'),
        ),
    },
    'vision': {
        'chemin': '/sujets/vision/',
        'titre': 'Vision and perception',
        'question': 'Can we restore sight?',
        'enjeu': 'Lasting also means repairing what wears out.',
        'reponse': 'In part. In people who had lost their central vision, an implant placed under the retina clearly improved the acuity of [[prima_reponses]] out of [[prima_suivis]] after one year. Sending a complete image straight to the brain is something nobody knows how to do.',
        'sources': ('/interfaces-cerveau/',), 'lien': '/interfaces-cerveau/#prima',
        'description': 'Producing a percept, restoring a visual function and studying the idea of adding an image to what one sees.',
        'intro': '<p>How does a signal become something we see? This section explores retinal and cortical prostheses, perceived shapes and models of artificial vision. The central question is the visual experience actually obtained.</p>',
        'questions': (
            'What exactly does “injecting an image” into vision mean?',
            'How do we tell apart a neural response, a recognized shape and a useful percept?',
            'Which open models make it possible to study these questions?',
        ),
        'lectures': (
            ('/interfaces-cerveau/#vision', 'From flashes of light to the idea of a visual scene'),
            ('/interfaces-cerveau/#prima', 'The results and limits of the PRIMAvera trial'),
            ('/interfaces-cerveau/#contribuer', 'Proposed projects for studying visual prostheses'),
        ),
    },
    'reve-temps': {
        'chemin': '/sujets/reve-temps/',
        'titre': 'Dreams and lived time',
        'question': 'Can we live a whole life in one night?',
        'enjeu': 'If a life cannot be made longer, can more be lived in the same time?',
        'reponse': 'Nobody has shown it. Out of [[dream_intervalles]] dream reports for which the elapsed sleep time is known, none describes a duration longer than that time. What remains is to measure the time lived, not just the time told.',
        'sources': ('/temps-reve/',), 'lien': '/temps-reve/',
        'description': 'Lucid dreaming, dream content, felt duration and the possibility of living an experience that seems longer.',
        'intro': '<p>Dreams raise questions about consciousness, the content of experience and the passing of time. The articles look at exchanges during sleep, the influence of a theme and the different ways of measuring a duration.</p>',
        'questions': (
            'Can content be recognized or steered during a dream?',
            'How can lived time be measured, rather than just the reported duration?',
            'What would have to be established before we could speak of a life in one night?',
        ),
        'lectures': (
            ('/temps-reve/', 'How time is measured in dreams'),
            ('/meg-eeg-reves/', 'Reading and steering dreams: evidence and open questions'),
            ('/projet/', 'Examining the hypothesis of a life in one night'),
        ),
    },
    'relativite': {
        'chemin': '/sujets/relativite-trous-noirs/',
        'titre': 'Relativity and black holes',
        'question': 'Can we slow down time?',
        'enjeu': 'Slowing time down is the most direct way to gain some.',
        'reponse': 'Yes. The closer you are to a mass, the more slowly time passes. This has been measured, down to the millimeter. On Earth, a clock placed one centimeter lower falls behind by about [[cm_an_ps]] picoseconds a year. Near a black hole, the gap becomes enormous.',
        'sources': ('/gravitation-horloges/',), 'lien': '/gravitation-horloges/',
        'description': 'Understanding Einstein and Hawking, comparing clocks and examining the limits of our descriptions of time and gravitation.',
        'intro': '<p>From clocks one centimeter apart to the horizons of black holes, relativity ties measured time to trajectory and gravitation. This section separates experiments, theoretical calculations and open questions.</p>',
        'questions': (
            'Why do speeds not add up the way they do in everyday life?',
            'How much time passes near a black hole or at the center of the Earth?',
            'What does Hawking’s work teach us, and where do our theories reach their limits?',
        ),
        'lectures': (
            ('/einstein-relativite-restreinte/', 'Start with speeds, light and durations'),
            ('/gravitation-horloges/', 'Compare clocks from the ground to the center of the Earth and to black holes'),
            ('/hawking-trous-noirs-limites/', 'Tell apart horizon, singularity, evaporation and information'),
        ),
    },
    'simulation': {
        'chemin': '/sujets/simulation/',
        'titre': 'Simulation theory',
        'question': 'Is our world a simulation?',
        'enjeu': 'Before trying to last in this world, we might as well know what it is made of.',
        'reponse': 'We looked for the traces a computed world would leave: a grid in space, manufactured randomness. In the light from [[n_src]] distant sources and in [[bits_bruts]] bits drawn from quantum experiments, we found none. That does not settle the question. It rules out the simplest simulations.',
        'sources': ('/test-3/', '/test-4/'), 'lien': '/synthese/',
        'description': 'Examining the hypothesis of a simulated world, its philosophical arguments and the signatures of specific physical models.',
        'intro': '<p>What could we observe if our world were simulated? This section gathers the arguments, their assumptions and the tests of particular architectures. Each conclusion stays tied to the model and the observations that support it.</p>',
        'questions': (
            'Which assumptions make the idea of a simulation testable?',
            'What traces would a grid, a random number generator or on-demand computation leave?',
            'How far does a result about one model tell us anything about the nature of our world?',
        ),
        'lectures': (
            ('/synthese/', 'Start with the summary of the results and their limits'),
            ('/test-1/', 'A cubic grid against the propagation of light'),
            ('/audit-infodynamique/', 'Checking the proofs put forward for a simulation'),
        ),
    },
}

A_PROPOS = {
    'titre': 'About ÆTERNAM',
    'description': 'Nobody knows yet how not to die. We will find a way. ÆTERNAM publishes what is known: every number has a source, every calculation can be rerun.',
    'corps': r"""
<p><strong>Nobody knows yet how not to die. We will find a way.</strong> Death spares no one, so this work is done for everyone and in full view: ÆTERNAM publishes what is known today, with the sources and the calculations, and anyone can write here.</p>
<h2>Seven topics, seven questions</h2>
<p>Each topic touches on one way of lasting. <a href="/sujets/vieillissement/">Aging</a>: what makes us die, and what slows it. <a href="/sujets/memoire/">Memory</a>: what remains of a life. <a href="/sujets/interfaces-cerveau-machine/">Brain-computer interfaces</a>: reading what a brain holds. <a href="/sujets/vision/">Vision</a>: repairing a lost sense. <a href="/sujets/reve-temps/">Dreams and lived time</a>: living more in the same time. <a href="/sujets/relativite-trous-noirs/">Relativity and black holes</a>: time does not pass at the same rate everywhere. <a href="/sujets/simulation/">Simulation theory</a>: what the world is made of.</p>
<p>These topics meet in one question; each keeps its own methods and its own evidence.</p>
<h2>How the articles are built</h2>
<p>The work starts from published studies, primary sources and open data. Depending on the article, it is a critical reading, a reanalysis of data or a calculation based on explicit assumptions. ÆTERNAM has run no experiments on people: the brain research gathered here relies on existing work and on calculations.</p>
<p>Each article opens with an accessible explanation, then gives the detailed analysis. Sources are linked in the text. A research proposal is presented as one; a simulation states what it assumes. Limits are part of the results.</p>
<h2>Open to everyone</h2>
<p>Anyone can <a href="/ecrire/">publish an article</a> under their name. A correction, a reproduction or a well-defined comparison are useful contributions. The <a href="https://github.com/aitorgarcia21/aeternam">public repository</a> keeps the analyses, the results, the history of changes and <a href="https://github.com/aitorgarcia21/aeternam/blob/main/AUDIT-SCIENTIFIQUE.md">the corrected mistakes</a>. Texts, figures and results are licensed under <a href="https://creativecommons.org/licenses/by/4.0/deed.fr">CC BY 4.0</a>: anyone may reuse them with credit to their author. Code is licensed under <a href="https://github.com/aitorgarcia21/aeternam/blob/main/LICENSE-CODE">MIT</a>.</p>
<p><a href="/recherches/">Read the blog</a> · <a href="/sujets/">Explore the topics</a></p>
""",
}

# The /ecrire/ page: [[options]], [[modele]], [[depot]], [[fleche]], [[licence]], [[adresse_licence]]
# and [[liste_signes]] are filled in by site/generer.py.
ECRIRE = {
    'titre': 'Write for ÆTERNAM',
    'description': 'Anyone can publish a signed article on ÆTERNAM: reviewed in public, published under the CC BY 4.0 license.',
    'modele': ('## Explanation\n\nWhat the article shows, in plain words.\n\n'
               '## Detailed analysis\n\nThe data, the method, the calculations and their limits.\n\n'
               '## Sources\n\n- [Title of the source](https://…)'),
    'corps': r"""
<p>The ÆTERNAM blog is open. Anyone can publish an article here under their name: a critical reading, a reanalysis of data, a calculation, a well-posed question. Each submission is reviewed in public before it appears, and the text stays free to reuse.</p>
<h2>Submit an article</h2>
<form class="proposer" id="proposer" data-depot="[[depot]]" novalidate>
<p class="champ"><label for="p-titre">Title</label><input id="p-titre" name="titre" maxlength="140" required autocomplete="off"></p>
<p class="champ"><label for="p-auteur">Byline</label><input id="p-auteur" name="auteur" maxlength="80" required autocomplete="name" placeholder="First name Last name"></p>
<p class="champ"><label for="p-theme">Topic</label><select id="p-theme" name="theme"><option value="">None in particular</option>[[options]]</select></p>
<p class="champ"><label for="p-resume">Summary <span>optional, one or two sentences</span></label><textarea id="p-resume" name="resume" maxlength="300" rows="2"></textarea></p>
<p class="champ"><label for="p-orcid">ORCID <span>optional</span></label><input id="p-orcid" name="orcid" maxlength="19" autocomplete="off" spellcheck="false" placeholder="0000-0000-0000-0000"></p>
<p class="champ"><label for="p-texte">Text <span>in Markdown, help below</span></label><textarea id="p-texte" name="texte" rows="18" required placeholder="[[modele]]"></textarea></p>
<p class="actions"><button type="submit" class="envoyer">Submit on GitHub [[fleche]]</button>
<button type="button" class="secondaire" data-action="copier">Copy the file</button>
<button type="button" class="secondaire" data-action="telecharger">Download</button></p>
<p class="etat" id="etat" aria-live="polite"></p>
</form>
<p>The button opens GitHub with your file already filled in; you need a GitHub account, which is free. GitHub creates your copy of the repository, then offers to open a publication request, a <i>pull request</i>. The file is also copied: if GitHub first makes you create that copy, paste it in afterwards. The draft stays in this browser and nowhere else.</p>
<h2>The rules</h2>
<ul>
<li><strong>Sign with your name.</strong> The article commits its author; the byline, the date and the version history stay public.</li>
<li><strong>Separate what is measured, calculated and assumed.</strong> Every number points to its primary source or to a calculation others can rerun; a simulation is presented as a simulation.</li>
<li><strong>Cite where you use it.</strong> The link to the paper, the data or the code goes in the sentence that relies on it.</li>
<li><strong>Explain, then detail.</strong> First what the article shows, in plain words; then the analysis, its calculations and its limits.</li>
<li><strong>Accept review.</strong> Comments are made in public, on the submission; the article appears once they are resolved. Review is about evidence and clarity, not opinions.</li>
<li><strong>Publish under the <a href="[[adresse_licence]]" rel="noopener">[[licence]]</a> license.</strong> Anyone may reuse the text with credit to its author. By submitting an article, you confirm that you wrote it.</li>
</ul>
<h2>Writing in Markdown</h2>
<div class="tableau"><table class="phrases">
<thead><tr><th>Write</th><th>To get</th></tr></thead>
<tbody>
<tr><td><code>## Explanation</code></td><td>a section heading, listed in the table of contents</td></tr>
<tr><td><code>### The data</code></td><td>a subheading</td></tr>
<tr><td><code>**bold**</code> · <code>*italic*</code></td><td><strong>bold</strong> · <em>italic</em></td></tr>
<tr><td><code>[text](https://…)</code></td><td>a link</td></tr>
<tr><td><code>- item</code> · <code>1. item</code></td><td>a list</td></tr>
<tr><td><code>&gt; quote</code></td><td>a quotation</td></tr>
<tr><td><code>$$E = mc^2$$</code> · <code>\(x^2\)</code></td><td>a formula, on its own line or within a sentence</td></tr>
<tr><td><code>![caption](medias/figure.png)</code></td><td>an image, added to the <code>contributions/medias/</code> folder</td></tr>
<tr><td><code>```</code></td><td>a code block, between two lines of three backticks</td></tr>
</tbody></table></div>
<p>HTML is not interpreted: it is displayed as written. SVG images and scripts are refused, to keep readers safe. If something is wrong, the automatic check on the submission says what to fix.</p>
<h2 id="signes">Community articles</h2>
[[liste_signes]]
""",
}

PROJET = {
    'titre': 'A life in one night: a hypothesis to examine',
    'description': 'What would it mean to live a life in one night? Continuous duration, narrative and memory raise three different questions.',
    'date': 'September 29, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>Living an entire life during one night is an open research question.</strong> To examine it, we have to specify what “living a life” means: a long conscious experience, a story that represents its moments, or the memory of such a story.</p>
<p>Dreams can produce scenes, encounters and emotions without a corresponding external environment. Studying their content and duration gives footholds on the question. This requires separate measures of the experience, of the report on waking and of memory.</p>
<p>The articles on <a href="/temps-reve/">the time of a dream</a>, <a href="/meg-eeg-reves/">reading and steering dreams</a> and <a href="/interfaces-cerveau/#memoire">interventions on memory</a> address these different components.</p>
<h2 id="analyse">Detailed analysis</h2>
<h3>Defining the duration to be explained</h3>
<p>Read literally, living [[vie_ans]] continuous years in [[nuit_h]] hours requires a ratio of [[facteur]] between lived duration and elapsed duration. This number comes from the definition of the hypothesis. It is neither a measurement of the brain nor a forecast of success.</p>
<p>A story covering eighty years with ellipses and eighty years lived continuously are two different objects. Narrative continuity is a useful research topic, whose results must be kept separate from those on acceleration.</p>
<h3>First footholds on the problem</h3>
<p><a href="https://doi.org/10.1016/j.cub.2021.01.026">Dialogue during dreaming</a> provides observable markers. <a href="https://doi.org/10.1016/j.concog.2020.102938">Thematic incubation</a> offers a way to influence certain contents. <a href="https://doi.org/10.1016/j.concog.2024.103759">Work on lucidity at home</a> studies software approaches. The notebook on <a href="/programme/">dreams, time and memory</a> examines their measures, their denominators and the available data.</p>
<p>Fast neural replay concerns memory. It does not measure a consciously accelerated life. A result on recall or on the speed of a task must therefore keep its own unit and its own scope.</p>
<h3>Questions to keep separate</h3>
<ul>
<li>Can content be identified or steered during sleep?</li>
<li>Which markers make it possible to measure the duration of the ongoing experience?</li>
<li>What remains on waking, and how are episodes linked in memory?</li>
<li>How can a real effect be separated from a selection, recall or measurement bias?</li>
</ul>
<p>These questions belong to the topics <a href="/sujets/reve-temps/">Dreams and lived time</a> and <a href="/sujets/memoire/">Memory</a>. <a href="/sujets/simulation/">Simulation theory</a> questions the nature of our world with other evidence; cosmological results do not establish the feasibility of a dream experience.</p>
""",
}

BCI_MONTE_CARLO = {
    'titre': 'BCI: simulating calibration and noise',
    'description': 'A Monte Carlo simulation fitted to human EEG explores the number of personal trials, noise correction and the limits of its predictions.',
    'date': 'October 3, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>We ran our own Monte Carlo experiment to study how much personal data improves a BCI decoder.</strong> Its generator is fitted to [[mc_essais_reels]] EEG trials from [[mc_reels]] people, actually processed in our <a href="/bci-generalisation/">previous analysis</a>. The new campaigns are simulated: they predict the behavior of a model of human measurement, and they are not new measurements in humans.</p>
<p>Each virtual person produces calibration observations, then an independent test. We vary the number of personal trials, the noise and the stability of the signal. Our criterion, chosen for this experiment, is a <strong>mean gain of at least five points</strong> over the same system without any labeled personal trial. It is not a clinical threshold.</p>
<p>In the scenario that keeps the contrasts fitted to the EEG, this criterion is reached at <strong>[[mc_budget_ref]] labeled trials with reference correction, against [[mc_budget_brut]] with uncorrected added noise</strong>. The correction also requires [[mc_reference_n]] unlabeled personal observations. The result therefore concerns the reduction of guided trials; the total cost of data collection must include this reference.</p>
<p><strong>The number required depends strongly on the assumptions.</strong> If we halve the contrast between the tasks, or triple the amplitude of the drift between blocks, the criterion is no longer reached up to [[mc_max]] trials. Here a simulation gives a conditional answer and situations to test, not a universal number valid for everyone.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="mesure">1. What we simulate of a human measurement</h3>
<p>Our starting point is the <a href="https://physionet.org/content/eegmmidb/1.0.0/">PhysioNet EEG Motor Movement/Imagery dataset</a>, attributed to Gerwin Schalk and the BCI2000 contributors. We keep six values per trial: the log powers of C3, Cz and C4 in two bands, from 8 to under 13 Hz and from 13 to under 30 Hz. They come from the three-second human segments already extracted.</p>
<p>For each person, we fit a mean level, a difference between the left/right cues, the joint fluctuations of the six values and a shift between recording blocks. The Monte Carlo draws new observations from these distributions. It produces the values our decoder receives; it reconstructs neither an anatomy nor a complete EEG waveform.</p>
<p>Each campaign picks one of the twelve fitted profiles. The other eleven profiles each generate [[mc_source_n]] trials for the starting model. The target profile separately generates the calibration and [[mc_test]] test trials. The decoder receives neither the hidden parameters of the virtual person nor the test answers. Repeated campaigns do not create additional biological diversity.</p>
<p>The original data contain 45 trials per person. Higher budgets extrapolate the fitted distributions. Differences between classes may also contain effects of the visual cue or artifacts: our simulation does not prove that all the information is a motor intention.</p>

<h3 id="experience">2. A repeated experiment, with its assumptions written down</h3>
<p>We ran [[mc_repetitions]] campaigns per assumption, with budgets of 0, 4, 8, 16, 32, 64, 128 and 256 labeled trials. The classes are balanced. A budget consists of the first trials of the budgets that follow it; the test is entirely separate. The conditions share their random draws to allow a paired comparison.</p>
<p>The starting model is a linear discriminant analysis. Personal calibration adapts its means and its covariance: the weight of the personal trials is \(n/(n+16)\), for \(n\) trials. The rest comes from the source model. The decoder’s regularization is fixed at 0.1 toward the covariance diagonal. We also computed a comparator that uses only the personal trials. The parameters were fixed before the curves, without external preregistration.</p>
<p>The four assumptions keep the empirical contrasts, halve them, triple the drift, or remove all contrast between classes. The two modifications are chosen sensitivity tests, with no claim to represent a particular clinical population. The no-contrast case serves as a negative control.</p>

<h3 id="bruit">3. Added noise and ways to reduce it</h3>
<p>The initial level already contains the variability that comes from human EEG. We add two perturbations, correlated across channels, in feature space. They represent a common nuisance, with a fixed intensity. This model is not an electromagnetic simulation: its units are neither volts nor teslas, and it does not reproduce 50 Hz interference in the time domain.</p>
<ul>
<li><strong>No added noise.</strong> Keep the variability of the generator fitted to human data.</li>
<li><strong>Added noise, no correction.</strong> Perturb the target person’s measurement during calibration and test.</li>
<li><strong>Reference correction.</strong> Also measure the interference with imperfect virtual sensors, learn its contribution from [[mc_reference_n]] independent unlabeled observations, then subtract it.</li>
<li><strong>Assumed attenuation.</strong> Reduce the amplitude of the added interference to 20%. This is an assumption of the simulator, not a demonstrated hardware performance.</li>
<li><strong>Contaminated reference.</strong> Let part of the useful activity reach the reference sensor, to test the risk of removing it along with the noise.</li>
</ul>
<p>The reference observations are an additional personal cost. The source model also uses the synthetic observations of the other profiles. “Zero labeled trials” therefore means no guided calibration; in the corrected condition, personal reference data remain.</p>

<h3 id="resultats">4. How many trials improve the decoder in this model?</h3>
<p>The criterion requires a mean gain of at least five points, a positive Monte Carlo lower bound, and the criterion holding at every higher budget tested. We keep the first budget on the grid that satisfies it. The accuracy is balanced, since the test contains as many trials of each class.</p>
[[figure_mc_seuils]]
<p>With the reference, the score goes from [[mc_score_ref0]]% to [[mc_score_ref64]]% between zero and 64 labels: <strong>a gain of [[mc_gain_ref64]] points</strong>, with a Monte Carlo interval from [[mc_ref64_bas]] to [[mc_ref64_haut]] points. At the same budget of 64, uncorrected noise gives [[mc_score_brut64]]%. The score remains modest, even when the exploratory criterion is reached.</p>
<p>The minimum of 128 under uncorrected noise is more fragile: its mean gain is [[mc_brut128_gain]] points, with an interval from [[mc_brut128_bas]] to [[mc_brut128_haut]] points that crosses the five-point boundary. The grid and the numerical precision do not allow us to claim that one trial fewer would make the method fail.</p>
<figure class="mc-resultats">
<h4>Gain by simulated calibration</h4>
<p>[[mc_repetitions]] campaigns per condition, empirical scenario.</p>
<img src="/fichiers/bci-monte-carlo/calibration-bruit.svg" width="390" height="450" loading="lazy" alt="Curves of the mean gain by number of trials. Reference correction reaches the criterion at 64 trials, uncorrected noise at 128, in the empirical scenario.">
<figcaption>The horizontal axis doubles at each tick. Each curve measures the gain over its own zero-label point. The bands show the 95% Monte Carlo precision under the fixed model; they do not include the human uncertainty about its parameters.</figcaption>
</figure>
[[figure_mc_scores]]
<p>The corrected budget includes 64 guided trials and 256 reference observations, that is, 320 personal observations in our construction. The uncorrected budget of 128 does not carry this reference cost. We have therefore shown a conditional reduction in the labels required, while making the extra measurement visible. No human session duration is inferred from these numbers.</p>

<h3 id="sensibilite">5. When more data is not enough</h3>
<p>After reference correction, the gain at 256 trials falls to [[mc_faible_gain]] points when the contrast is halved, and to [[mc_derive_gain]] points when the drift amplitude triples. The criterion is reached in neither scenario on the grid studied. This does not show that it would be impossible at every higher budget; we did not simulate those budgets.</p>
<figure class="mc-resultats">
<h4>Sensitivity to the measurement assumptions</h4>
<p>Reference correction, same paired campaigns.</p>
<img src="/fichiers/bci-monte-carlo/sensibilite-modele.svg" width="390" height="450" loading="lazy" alt="The empirical curve crosses five points. The halved-contrast and tripled-drift curves stay below five points up to 256 trials.">
<figcaption>The sensitivity parameters are chosen to test the conclusion. They are not measured patient categories. The intervals remain conditional on each model.</figcaption>
</figure>
<p>The contaminated reference gives [[mc_fuite_score]]% at 64 trials, against [[mc_score_ref64]]% with the reference independent of the useful signal. Denoising can remove the information being sought. A smoother trace or a lower reconstruction error therefore does not remove the need to check the final task.</p>
<p>The empirical contrasts were estimated from few trials and may be overestimated. The reduced-contrast scenario shows the possible consequence of this uncertainty; it does not provide an exact correction for it. The observed drift comes from three runs of a single session, with no measurement of change between days, of fatigue or of human learning.</p>

<h3 id="laboratoires-chinois">6. What we take from the Chinese laboratories</h3>
<p><strong>Beihang and its Ningbo institute act on the field before the MEG measurement.</strong> <a href="https://doi.org/10.1016/j.isatra.2025.07.050">Dou et al., 2025</a>, combine a shielded enclosure, low-noise coils and active compensation control. The sensor measures the residual field and the controller corrects it. Our hypothetical attenuation reproduces neither this setup nor its performance.</p>
<p><strong>In Shenzhen, the NCCLab at SUSTech builds controlled comparisons.</strong> In <a href="https://doi.org/10.1088/1741-2552/ac2bf8">EEGdenoiseNet</a>, the authors contaminate reference EEG with ocular or muscle artifacts and evaluate the reconstruction. We adopt this principle of a known perturbation. Our experiment uses its own statistical model, without reusing their networks or their results.</p>
<p>Three problems remain separate: external interference measured by the sensors, artifacts from the body, and the change in features between people or between sessions. For EEG, <a href="https://mne.tools/stable/auto_tutorials/preprocessing/40_artifact_correction_ica.html">component separation</a> and <a href="https://mne.tools/stable/auto_tutorials/preprocessing/25_background_filtering.html">frequency filtering</a> are other tools. Their effect on the useful information must be checked. A magnetic compensation result does not directly give a number of EEG calibration trials.</p>

<h3 id="verification">7. What the checks establish</h3>
<p>The 48,000 decisions of one checked campaign match an independent computation of Gaussian densities in SciPy. The reference correction is checked against scikit-learn, and the twenty thresholds are recomputed separately. An analytical example confirms the generator. In the scenario with no difference between classes, the largest deviation of the mean score from 50% is [[mc_nul_ecart]] points.</p>
<p>We also fitted a model on two human runs and examined the third: [[mc_couverture]]% of the observations fall inside an indicative 95% Gaussian ellipse. This diagnostic checks one aspect of the dispersion. Since the ellipse parameters are estimated, it is neither an exact test nor a validation of the number of trials that will be needed in the future.</p>
<p>The useful results of this experiment are the conditional curves, their calibration costs and their sensitivity. A future human study will have to confront these predictions with new sessions, measure the real noise, hold out trials chronologically and also count involuntary commands at rest. The Monte Carlo helps us define this study and identify the assumptions on which its success depends.</p>
""",
}

BCI_GENERALISATION = {
    'titre': 'BCI: a decoder facing a new person',
    'description': '540 EEG trials from 12 people reanalyzed, two separate evaluations, and four recent BCI studies examined for their actual scope.',
    'date': 'October 3, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>We processed [[bci_essais]] EEG trials from [[bci_personnes]] people to ask a precise question: does a decoder trained on some brains work on a person it has never seen?</strong> The recordings come from existing open data. The participants had to imagine a movement of the left hand or the right hand, following a visual cue.</p>
<p>Our simple model reaches [[bci_meme]]% when it learns from other recordings of the same person, and [[bci_nouvelle]]% when the person tested is entirely absent from training. The measure gives the same weight to both classes; always answering “left” scores [[bci_reference]]%. The first result indicates a weak association in this exploratory setting. The second is not enough to establish decoding beyond our label-shuffling control.</p>
<p>This result concerns an elementary method and a small subset. It sets no limit on BCIs. It shows why “the software recognizes a task” and “the software works for a new user” must be checked separately. We also publish the individual scores, so that the mean does not hide the differences.</p>
<p>Recent implanted interfaces achieve other capabilities, notably for communication. Below we examine four studies from 2026, then our own analysis. The tasks, the sensors and the populations differ: their percentages cannot be compared directly with those of our EEG.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="recherche-recente">1. Four recent results, four concrete difficulties</h3>
<p><strong>Using a BCI at home.</strong> <a href="https://doi.org/10.1038/s41591-026-04414-6">Card et al., June 2026</a>, document more than [[card_heures]] hours with one implanted person, with an average of [[card_debit]] words per minute in personal use. The [[card_copie]]% word accuracy concerns a copy task; in personal use, [[card_personnel]]% of sentences are judged entirely correct straight away. The units differ. Setup remains assisted and the system recalibrates in the background.</p>
<p><strong>Speaking and gesturing at the same time.</strong> <a href="https://doi.org/10.1038/s41593-026-02446-2">Brosler et al., September 2026</a>, study isolated movements in [[brosler_isoles]] people, and simultaneous data in [[brosler_simultanes]]. The simultaneous copy quantified in real time concerns one person. Training on several contexts helps limit unwanted activations of one modality when only the other is intended. The conversation demonstrations remain limited; they do not validate general free interaction.</p>
<p><strong>Measuring a perceptual benefit.</strong> <a href="https://doi.org/10.1038/s41593-026-02281-5">Choudhari et al., May 2026</a>, decode auditory attention to enhance one voice among competing voices. They then evaluate comprehension and preference. The [[choudhari_n]] participants are recorded with intracranial electrodes during an epilepsy workup and report normal hearing. This result therefore does not validate a consumer EEG device intended for hearing loss.</p>
<p><strong>Transferring between people.</strong> <a href="https://doi.org/10.1038/s41467-026-75455-1">Spalding et al., July 2026</a>, align signals of actually produced speech in [[spalding_n]] people. The alignment uses training data from the target patient, keeping that patient’s test data apart. “Between people” therefore does not mean “without calibration”. Transfer to a paralyzed person remains a separate question.</p>
<p>These studies guide our research question: measuring what remains valid when conditions change. We have to examine the data needed to get started, the adaptations during use, unwanted activations and the functional benefit. A score obtained in a guided task does not answer all these questions.</p>

<h3 id="donnees">2. The signals we actually analyzed</h3>
<p>We downloaded [[bci_runs]] EDF files from the <a href="https://physionet.org/content/eegmmidb/1.0.0/">PhysioNet EEG Motor Movement/Imagery dataset</a>, attributed to Gerwin Schalk and the BCI2000 contributors, under the Open Data Commons Attribution License 1.0. The subset comprises identifiers S001 to S012 and recordings 04, 08 and 12. These recordings correspond to left-hand/right-hand imagery, as the <a href="https://mne.tools/stable/generated/mne.datasets.eegbci.load_data.html">MNE documentation</a> also states.</p>
<p>The annotations give [[bci_gauche]] “left” trials and [[bci_droite]] “right” trials. No trial of these two classes was excluded on the basis of its amplitude or its result. The rest periods are outside the chosen task. The subset and the parameters were written down before the first computation of scores, with no external preregistration and no selection based on performance.</p>
<p>The URLs, sizes and SHA-256 hashes of the raw files are kept. The derived features, labels, predictions and protocol are versioned. This is a reanalysis of existing measurements, with no new human data collection by Aeternam.</p>

<h3 id="protocole">3. A deliberately simple model, two ways of splitting the data</h3>
<p>Each trial provides a three-second window, from 0.5 to 3.5 seconds after the cue. We use three electrodes, C3, Cz and C4, and two frequency bands: from 8 to under 13 Hz, then from 13 to under 30 Hz. This gives [[bci_features]] features, the logarithms of the powers per channel and per band. The computation removes the segment mean, applies a Hann window and integrates the one-sided periodogram. The recorded reference is kept.</p>
<p>The classifier is a linear discriminant analysis, with equal prior probabilities and regularization fixed at 0.1 toward an identity matrix of the same trace. Standardization and the model are fitted on the training data only. No parameter is optimized on the results presented.</p>
<ol>
<li><strong>Entire person held out, main evaluation.</strong> Train on eleven people and predict the trials of the twelfth, then repeat for each person. No signal from the person tested is used to fit their decoder.</li>
<li><strong>Recording held out, secondary evaluation.</strong> For each person, train on two of their recordings and predict the third, then rotate the roles. Here the model already knows data from this person.</li>
</ol>
<p>A recording, or <em>run</em>, is a block of tasks in the dataset. Holding one out is not the same as testing another day. The two training runs may come before or after it: this is not a prospective validation after calibration. The two evaluations also change the amount and the origin of the training data. Their difference is not a causal estimate of the effect of calibration.</p>
<p>There are [[bci_plis_personnes]] training/test splits for the first evaluation, and [[bci_plis_runs]] for the second. In each, every trial is predicted exactly once outside training. We compute the balanced accuracy on each person’s predictions, then the mean across people. No window from a given trial ends up on both sides.</p>

<h3 id="resultats">4. Results and controls</h3>
<div class="tableau"><table class="phrases"><thead><tr><th scope="col">Data held out for testing</th><th scope="col">Mean balanced accuracy</th><th scope="col">Permutation p, Holm-corrected</th></tr></thead><tbody>
<tr><th scope="row">Entire person</th><td>[[bci_nouvelle]]%</td><td>[[bci_nouvelle_p]]</td></tr>
<tr><th scope="row">Run, same person</th><td>[[bci_meme]]%</td><td>[[bci_meme_p]]</td></tr>
</tbody></table></div>
<p>Balanced accuracy is the mean of the rate of correct answers in each class. Its constant baseline is [[bci_reference]]%, even if the left/right counts differ. Between people, the observed scores range from [[bci_nouvelle_min]] to [[bci_nouvelle_max]]%. For held-out runs, they range from [[bci_meme_min]] to [[bci_meme_max]]%. These ranges describe our sample, not the uncertainty in the population.</p>
<figure class="bci-resultats">
<img src="/fichiers/bci-generalisation/resultats-individuels.svg" width="380" height="540" loading="lazy" alt="Scores of the twelve people. Circles represent the person absent from training, squares a held-out run from the same person. The following table gives the exact rounded values.">
<figcaption>Each row corresponds to one person. The vertical line marks 50%. The individual differences are large; no individual score is presented here as statistically confirmed.</figcaption>
</figure>
[[figure_bci_tableau]]
<p>The control shuffles the left/right labels within each person/run block, then fully retrains both evaluations. We ran [[bci_permutations]] permutations, with a fixed seed. The test is one-sided: count the shuffled scores at least as high as the observed score, adding one to the numerator and to the denominator. Holm’s method corrects the two tests.</p>
<p><strong>The result on an unknown person does not allow us to conclude that decoding is established beyond this control.</strong> This does not prove the absence of information. The result on a held-out run indicates a weak association, under the assumptions of the test. A p-value is neither the probability that the model is true nor the probability that a particular prediction is correct. The limited number of permutations makes their estimate coarse.</p>
<p>We checked the spectral computation for one trial against <em>SciPy</em>, then the predictions of both evaluations against an independent implementation of discriminant analysis in <em>scikit-learn</em>, with the same choices of standardization, covariance and priors. No prediction differs. This check verifies the computations; it is not enough to validate the biological interpretation.</p>

<h3 id="limites">5. What this analysis leaves open</h3>
<p><strong>The cue is not a pure measure of intention.</strong> The classes are associated with a visual presentation. Sensory responses, residual movements or other artifacts may contribute to the signal. The central channels and the post-cue window are not enough to rule them out. A successful classification would therefore not, on its own, demonstrate the reading of an isolated motor intention.</p>
<p>The permutations assume that the trials are exchangeable within each block. A temporal dependence could weaken this assumption. The models of the different folds also share training data: we do not treat these folds as independent experiments, and we do not construct a binomial interval over the full set of predictions.</p>
<p>The dataset is small and chosen for convenience, and the model uses only three channels and six powers. It evaluates neither a high-performing, carefully tuned architecture nor all the available participants. This analysis does not reproduce a published MOABB result and does not claim a new decoding method.</p>
<p>Finally, we use a full three-second window in a guided task. We measured neither real-time control, nor throughput in free use, nor false commands during rest. Nor do these data answer the questions of <a href="/interfaces-cerveau/#vision">intervention on vision</a> or <a href="/interfaces-cerveau/#memoire">intervention on memory</a>.</p>

<h3 id="suite">6. The next useful contribution</h3>
<p>We have now run a <a href="/bci-monte-carlo/">Monte Carlo simulation of calibration and noise</a>, fitted to the EEG features of this study. It explores the effect of the number of personal trials in an explicit model. Comparison on new, held-out human measurements remains a separate step: our simple model could serve as a baseline against spatial filters or covariance models, with tuning kept entirely separate from the test.</p>
<p>A second question would concern adaptation: how many trials from a new person are needed to improve their score? Calibration and evaluation would have to be separated chronologically, with a comparable amount of training data. A true cross-day study would require a dataset that documents those days. To move toward free use, rest would also have to be included and commands triggered without intention counted.</p>
<p>The work done here provides a verifiable starting point: signals actually processed, explicit splits and a modest result kept as it is. The next comparisons will have to maintain this separation between choosing the method and evaluating it.</p>
""",
}

INTERFACES_CERVEAU = {
    'titre': 'Brain-computer interfaces: vision and memory',
    'description': 'The state of the evidence on BCIs, artificial vision and memory modification, with concrete avenues for contributing to research.',
    'date': 'October 3, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>We already know how to extract certain intentions from the brain and how to evoke certain perceptions. We do not know how to download a life into a memory.</strong> Brain-computer interfaces, or BCIs, link brain activity to a computer system. Some are used to control devices or to communicate. Other interfaces stimulate the nervous system to produce an effect. A bidirectional loop combines the two.</p>
<p>Artificial vision offers a concrete foothold: blind people can perceive shapes evoked by stimulation, and retinal implants have improved visual acuity in clinical trials. A great distance remains between these capabilities and the voluntary appearance of a realistic scene in the visual field.</p>
<p>Interventions on memory modify, in some protocols, the retention of information that was presented. They do not demonstrate the on-demand creation of a complete personal history. Remembering twenty years, believing they took place and living them consciously are three different goals.</p>
<p>To contribute now, our route is software: comparing decoding methods on open data and studying artificial vision models. A <a href="/bci-generalisation/">first reanalysis of EEG signals</a> has now been carried out. These questions also connect with <a href="/meg-eeg-reves/">reading and steering dreams</a>. The study below separates established results, open questions and the work we can undertake.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="lire-ecrire">1. Reading and writing are not two versions of the same problem</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Direction</th><th>Question</th><th>Example result</th></tr></thead><tbody>
<tr><td>Brain to machine</td><td>Which variable can be predicted from the signal?</td><td>Attempted speech, a voluntary command or a sleep state in a defined task.</td></tr>
<tr><td>Machine to brain</td><td>What effect does an intervention cause?</td><td>A light perception, a sensory modification or an effect on a memory task.</td></tr>
<tr><td>Bidirectional loop</td><td>Does the measurement help choose a better intervention?</td><td>Adapting a system according to its response, then checking for a perceptual or functional benefit.</td></tr>
</tbody></table></div>
<p>A decoder learns a statistical relationship between signal and label. An intervention device must establish a causal relationship between what it does and what the person perceives or accomplishes. Inverting a reading network is not enough to obtain a writing device: several states can produce similar signals, and the effects of a stimulation depend on the state of the brain.</p>
<p>EEG and MEG are means of measurement. A retinal prosthesis acts on the visual pathway before the brain; a cortical prosthesis intervenes directly in the brain. They have neither the same indications nor the same constraints. The existence of one does not automatically validate the other.</p>

<h3 id="decodage">2. Communication BCIs have already passed important milestones</h3>
<p>In <a href="https://doi.org/10.1038/s41586-023-06377-x">the study by Willett et al. published in 2023</a>, an intracortical interface decodes the attempted speech of a paralyzed participant. The results depend in particular on the vocabulary and the speaking mode evaluated. This is a capability for voluntary communication in a specific protocol, not indiscriminate access to her thoughts.</p>
<p>The work of <a href="https://doi.org/10.1038/s41593-025-01905-6">Littlejohn et al. in 2025</a> moves toward continuous speech synthesis from an implanted interface. This progress highlights the importance of response delay. Processing in small increments should not, however, be confused with the total delay of the whole chain, which includes acquisition, decoding and output.</p>
<p>Invasive and non-invasive studies are not a competition with a single score. The task, the number of people, the training data, the test conditions and the reliance on a language model change the meaning of a performance figure. For a scientific contribution, an honest comparison on the same task is worth more than a ranking that puts together incompatible percentages.</p>

<h3 id="vision">3. “Injecting an image” covers several capabilities</h3>
<p>The simplest case is an evoked light perception, called a phosphene. A more demanding capability consists of placing several perceptions in space and time so that a shape is recognized. Then come object recognition, navigation, and then a rich and stable scene. Succeeding at one stage does not establish the next ones.</p>
<p><a href="https://doi.org/10.1016/j.cell.2020.04.033">Beauchamp et al.</a> showed in sighted and blind participants that sequences of cortical stimulation could enable the recognition of letter shapes. The result gives a role to the timing and organization of the signals. It does not validate the hypothesis that one electrode would correspond to an independent pixel on a screen.</p>
<p>A <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12632539/">2025 study on controlling evoked activity</a> uses a model learned in a blind implanted participant. It shows the value of predicting the neural response and adapting the control. But succeeding in bringing activity closer to a chosen target does not, on its own, demonstrate that the person sees exactly the intended image. Validation must address perception and function, not only the recorded response.</p>
<p>A true visual overlay would also require placement consistent with gaze, stability across days, controlled interaction with remaining vision and a measurement of distortions. An object recognizable in a prepared task and an object that appears present in the real world are different results.</p>

<h3 id="prima">4. The retinal prosthesis provides clinical evidence in a specific setting</h3>
<p>In <a href="https://doi.org/10.1056/NEJMoa2501396">PRIMAvera, published online in 2025</a>, [[prima_n]] people with geographic atrophy received a subretinal implant. Of the [[prima_suivis]] assessed at twelve months, [[prima_reponses]] met the criterion for improvement in acuity, i.e. [[prima_taux]]%. The trial is open-label, with comparison to baseline and no randomized control group. It also reports [[prima_eig]] serious adverse events in [[prima_patients_eig]] participants. These elements are part of the result.</p>
<p>We checked the denominators: depending on the unknown outcome of the six people not assessed, the proportion over all implantations would arithmetically lie between [[prima_bas]] and [[prima_haut]]%. This range is not a confidence interval. The article separately provides an estimate by multiple imputation. The observed benefit does not transfer directly to a sighted person who wishes to add an image to their vision.</p>

<h3 id="memoire">5. Modifying memory does not mean writing a chosen memory</h3>
<p>We have to distinguish the encoding of a piece of information, its consolidation, its recall, the feeling that it is familiar and the conviction that an event was lived. A person may recognize an image better without having a new autobiographical episode. They may also recount more without having lived longer.</p>
<p>Human studies on a <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6576290/">hippocampal prosthesis in 2018</a>, then on <a href="https://doi.org/10.3389/fncom.2024.1263311">features and categories in 2024</a>, study the retention of information actually presented in memory tasks. The 2024 results include improvements and impairments depending on the people and the conditions. They do not establish that an arbitrary memory can be transferred from a computer.</p>
<p>The work of <a href="https://doi.org/10.1126/science.1239073">Ramirez et al. in mice</a> shows that an artificial memory association can be produced in an experimental paradigm. This is evidence about a context association in an animal. It demonstrates neither the narrative, nor the sensory richness, nor the continuity of identity of a human autobiography created from scratch.</p>
<p>To claim “memory writing”, one would have to specify what information was absent before the intervention, what the person retrieves afterwards, its fidelity, how long it is retained and the effects on the person’s existing memories. None of the studies checked here demonstrates the injection of a complete life.</p>

<h3 id="vingt-ans">6. Twenty years of memories, or twenty years actually lived?</h3>
<p>The idea of replacing twenty years of detention with twenty years “injected into memory” combines at least three different propositions:</p>
<ol>
<li><strong>A retrospective belief.</strong> The person believes they have gone through a long period. This conviction demonstrates neither detailed memories nor an equivalent lived duration.</li>
<li><strong>An artificial autobiographical history.</strong> The person has a coherent set of scenes, relationships and events that they attribute to themselves. This capability is not demonstrated by the memory intervention studies presented here.</li>
<li><strong>A prolonged conscious experience.</strong> The person actually lives every moment of the period during a short physical duration. This is a hypothesis of accelerated experience, distinct from memory.</li>
</ol>
<p>By definition, twenty continuous years in one hour would require a ratio of [[vingt_ans_une_heure]]; in eight hours, a ratio of [[vingt_ans_huit_heures]], using the convention of 365.25 days per year. These numbers are a division of durations. They describe no measured brain performance. A narrative that covers twenty years, like a film that tells them, does not demonstrate this ratio.</p>
<p>An artificial memory would not automatically reproduce the learning, the change in behavior or the other consequences of a real experience. Their equivalence would have to be demonstrated separately. The <a href="/programme/#temps">program on lived time</a> keeps this distinction between duration, narration and memory.</p>
<p>An imposed punitive application also raises a major problem of mental integrity and consent: modifying the history that a person attributes to themselves can constitute harm, even without long physical detention. The <a href="https://www.unesco.org/en/node/86248">UNESCO framework on neurotechnologies</a> places the rights and protection of people at the center of their development. Aeternam adopts voluntary experience and the restoration of capabilities as research directions, with no protocol of punitive suffering or imposed memories.</p>

<h3 id="contribuer">7. How to contribute usefully now</h3>
<p>Progress does not depend only on new implants. It also depends on reliable measurements, reproducible comparisons, models that fail in understandable ways and accessible software. Three workstreams make it possible to start with current resources.</p>
<div class="tableau"><table class="phrases"><thead><tr><th>Proposed workstream</th><th>First contribution</th><th>Expected evidence</th></tr></thead><tbody>
<tr><td>Artificial vision</td><td>Reproduce a published model with <a href="https://pulse2percept.readthedocs.io/en/stable/">pulse2percept</a>, then compare scene representations.</td><td>A stable result on new scenes and under several perception assumptions; visible limits.</td></tr>
<tr><td>EEG decoding</td><td>Reproduce a <a href="https://moabb.neurotechx.com/docs/paper_results.html">MOABB</a> benchmark on a restricted dataset.</td><td>Evaluation across sessions or people, uncertainty, computational cost and no data leakage.</td></tr>
<tr><td>Dream content</td><td>Audit the annotations and reproduce an EEG analysis of the reactivation of experiences.</td><td>Correspondence between data, labels and reports, then robustness on held-out data.</td></tr>
</tbody></table></div>
<p><strong>EEG decoding is the first workstream actually under way.</strong> Our <a href="/bci-generalisation/#resultats">reanalysis of open data</a> compares a simple model according to whether the person is known or absent from training. Reproducing a MOABB benchmark remains separate work still to be done. In artificial vision, another avenue would be to compare a raw representation, contours and a selection of elements relevant to a task, with criteria fixed before the comparison and held-out scenes.</p>
<p>We must, however, avoid taking the simulator’s image for what a person would see. The <a href="https://pulse2percept.readthedocs.io/en/stable/users/faq.html">pulse2percept documentation</a> stresses this limit. A method can exploit the peculiarities of a simulator and lose its advantage with other parameters or another model. A useful contribution measures precisely this fragility.</p>
<p>For decoding, <a href="https://moabb.neurotechx.com/">MOABB</a> offers a common framework for comparison. The question can be deliberately narrow: does a method remain better on a new session, at a comparable computational budget? Observations from the same person must stay grouped according to the evaluation plan. A difference obtained after many attempts must be confirmed on a dataset that is still untouched.</p>

<h3 id="programme">8. A research program with verifiable stages</h3>
<ol>
<li><strong>Establish the evidence and its limits.</strong> This review and the <a href="/meg-eeg-reves/">MEG/EEG</a> study are complemented by <a href="/bci-generalisation/">recent BCI studies and a first analysis of EEG signals</a>: sources checked, data processed and computations verified.</li>
<li><strong>Reproduce an open benchmark.</strong> Select a task, a small dataset and a software version. Check the license, the annotations and the result before modifying the method. This reproduction remains to be done.</li>
<li><strong>Test a narrowly defined improvement.</strong> Change one element, keep a credible comparator, evaluate outside the tuning data and also publish the failures. A new curve alone does not constitute progress.</li>
<li><strong>Prepare a scientific dossier useful to a team.</strong> Question, reproducible result, uncertainties, resources needed and missing experiment. Clinical access and collaborations must be established before claiming human validation.</li>
</ol>
<p>This review and the EEG reanalysis turn an intuition into measurable questions: what information to read, what perception to produce, what memory to improve, and how to recognize real success. The analysis of open signals is our first practical application in decoding; the other interventions described here remain work from the literature or research questions.</p>
""",
}

MEG_EEG_REVES = {
    'titre': 'Reading and steering dreams',
    'description': 'MEG, EEG, AI and sleep: verified sources, limits of decoding, transfer between sensors and a testable research program.',
    'date': 'October 3, 2026',
    'corps': r"""
<h2 id="explication">Explanation</h2>
<p><strong>MEG can help study the content of brain activity. It does not yet provide a dream reader.</strong> It measures very weak magnetic fields linked to brain activity. EEG measures differences in electrical potential at the surface of the skull. Their signals make it possible to study the brain, but a precise measurement does not automatically indicate what a person experiences.</p>
<p>The first useful goal would be to recognize a trace of an experience learned before sleep, then to check whether a sensory signal makes its presence in a reported dream more likely. Recognizing a beach among a few known themes would already be interesting. It would restore neither the people met, nor the events, nor the time lived.</p>
<p>Our analysis separates three results: detecting activity linked to a content, changing the probability of a reported content, and preserving sleep. Each must be demonstrated separately. The work we reviewed does not yet establish all three together in a single experiment.</p>
<p>We checked the articles, located the open repositories and ran calculations that show how an experiment could lead to a misleading conclusion. The section on <a href="/interfaces-cerveau/">brain-computer interfaces, vision and memory</a> extends this research to the possibilities of intervening on the brain.</p>

<h2 id="analyse">Detailed analysis</h2>
<h3 id="preuves">1. What the results allow us to conclude</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Work</th><th>Useful result</th><th>What remains to be established</th></tr></thead><tbody>
<tr><td><a href="https://doi.org/10.1038/s41593-026-02303-2">Brain2Qwerty v1</a></td><td>Decoding of sentences actually typed: mean character error of [[bq1_meg]]% with MEG and [[bq1_eeg]]% with EEG.</td><td>Decoding of a spontaneous experience, with no keyboard and no keystroke timestamps.</td></tr>
<tr><td><a href="https://facebookresearch.github.io/brain2qwerty/assets/brain2qwerty_v2.pdf">Brain2Qwerty v2</a></td><td>Preprint: [[bq2_wer]]% word error, with about [[bq2_phrases]] sentences typed by [[bq2_n]] people, each recorded for about [[bq2_h]] hours.</td><td>A continuous output with low delay, then generalization to sleep.</td></tr>
<tr><td><a href="https://doi.org/10.1111/jsr.70000">Vocabulary memory at home</a></td><td>Improved recall of some pseudowords reactivated during sleep.</td><td>A change in the dream, distinct from a memory consolidation effect.</td></tr>
<tr><td><a href="https://doi.org/10.1016/j.isci.2025.113032">Audiobooks and sleep</a></td><td>EEG profiles in REM are more similar between people exposed to the same book.</td><td>An individual decoder indicating at what moment a content is dreamed.</td></tr>
<tr><td><a href="https://doi.org/10.3389/frsle.2026.1812535">Incubation and REM dreams</a></td><td>A theme appears in reports after sleep onset.</td><td>A controlled causal effect, a directed story and preserved sleep.</td></tr>
</tbody></table></div>

<h3 id="brain2qwerty">2. Brain2Qwerty: an advance whose task must be kept in view</h3>
<p>v1 relies in particular on the motor representations of typing. Its confusions follow the proximity of keys. It therefore does not prove that the same information would be available during silent thought or a dream. The EEG and MEG come from separate sessions: this dataset does not directly provide the synchronized pairs needed to learn instantaneous transfer. These limits are described in <a href="https://doi.org/10.1038/s41593-026-02303-2">the article</a>.</p>
<p>v2 reduces the dependence on keystroke events supplied at inference, but its discussion states that the architecture is not causal: it processes the whole sentence before outputting it. The announced “real time” is therefore not a word-by-word readout with low delay. This is decisive for a loop that must choose when to intervene. The <a href="https://facebookresearch.github.io/brain2qwerty/assets/brain2qwerty_v2.pdf">preprint</a> reports a word error rate; its complement measures neither the fidelity of a thought nor a proportion of fully correct sentences.</p>
<p><strong>Consequence for Aeternam.</strong> Reusing an architecture can help in learning to process the signals. Validating a dream requires a new task, its own annotations and an independent evaluation. A language model can make an output more fluent; that fluency does not guarantee it originates in the brain signal. It must be compared with a model deprived of the signal, with desynchronized signals and with shuffled pairings.</p>

<h3 id="materiel">3. Wearable MEG keeps its physical constraints</h3>
<p>OPMs bring the sensors closer to the head and avoid cryogenics. That does not mean all of them operate internally at room temperature: alkali and helium technologies differ. The <a href="https://www.cea.fr/cea-tech/leti/english/Pages/What%27s-On/News/magnetoencephalography-towards-high-resolution-at-room-temperature.aspx">CEA describes this distinction</a>. A mobile helmet in a specialized room does not, through this progress alone, become usable in an ordinary bedroom.</p>
<p><a href="https://doi.org/10.1109/TBME.2024.3465654">Holmes et al.</a> show that spatial and temporal processing can help in a less shielded room. Control of the magnetic environment is still required. <a href="https://doi.org/10.1038/s41378-026-01226-z">Cho et al.</a> miniaturize an optical detector integrated into an OPM: the reported sensitivity of 33.5 fT/√Hz at 10 Hz is neither a measure of dream resolution nor the demonstration of a complete helmet on a chip.</p>
<p>The <a href="https://quspin.com/products-qzfm/">QuSpin price consulted on October 3, 2026</a> is 10,000 dollars per QZFM for an order of one to three sensors, with a surcharge for triaxial. The cost of a sensor does not include installation. The figure of 830,000 euros cited in the initial text has not been corroborated by an identifiable market reference; it is not accepted as evidence of cost.</p>
<p>For sleep research, one must also establish comfort, stability over a night, environmental noise, movements and compatibility with sensory stimulation. Multiplying measurement channels does not multiply independent information to the same extent. The choice of hardware must come after measuring what it adds to the task.</p>

<h3 id="transfert">4. Transfer from MEG to EEG is a hypothesis to be tested</h3>
<p>The idea is to train a model with a rich instrument, then teach an EEG model to reproduce some of its predictions. This can improve learning when the EEG signal contains usable information. It does not automatically recreate information that is absent at test time.</p>
<p>In a simplified physical model, the two instruments observe different projections of the brain currents: \(X_E=L_EJ+\varepsilon_E\) and \(X_M=L_MJ+\varepsilon_M\). The projections, the noise and the sensitivity to sources differ. MEG is therefore not a complete ground truth of which EEG would simply be a blurred copy. The truth to look for concerns the task and the experience, which both instruments measure indirectly.</p>
<p>We computed an exact counterexample. Four states are defined by two independent features. The teacher sees both; the student sees only one. Even with a perfect teacher and ideal learning, the student still has to choose between two indistinguishable states.</p>
<div class="tableau"><table class="phrases"><thead><tr><th>Abstract channel</th><th>Best possible accuracy</th></tr></thead><tbody>
<tr><td>Both features</td><td>[[info_professeur]]%</td></tr>
<tr><td>A single feature</td><td>[[info_eleve]]%</td></tr>
<tr><td>The same one, flipped with probability 0.2</td><td>[[info_bruite]]%</td></tr>
<tr><td>No information</td><td>[[info_hasard]]%</td></tr>
</tbody></table></div>
<p><strong>This table sets no real ceiling for EEG.</strong> It only shows why the quality of the teacher is not enough. We checked the values by enumerating every possible classifier in this small model.</p>
<p>A useful test would compare, on the same held-out data, EEG alone, MEG alone and EEG trained with the help of MEG. The next step would be to reduce the EEG channels, then to test transfer between nights. The alignment must be real, preprocessing must be learned on the training data only, and the data of the person evaluated must be held out according to the question asked. A benefit during wakefulness would not establish that it holds in REM.</p>

<h3 id="sommeil">5. From signal to dream: the link that remains uncertain</h3>
<p>In the <a href="https://doi.org/10.1016/j.isci.2025.113032">audiobook</a> study, the measure compares EEG power profiles between participants. It does not directly track the shift from one scene to another in a sleeper. The report is obtained on waking: it does not allow each recalled element to be dated within the recorded segment. The announced repository excludes roughly the last 30 to 60 seconds before waking. That absence must remain an absence.</p>
<p>The work of <a href="https://doi.org/10.1111/jsr.70000">Salfi et al.</a> analyzes 24 of the 31 people recruited. The reported +8.6% concerns the change in translation of the cued words between evening and morning, against −4.6% for the others. The result does not measure an “increase in dreams” and does not carry over to a chosen narrative.</p>
<p>The <a href="https://doi.org/10.3389/frsle.2026.1812535">incubation pilot</a> counts four people out of eight with incorporation in the first REM dream, that is [[pilote_premier]]%. The cumulative count reaches seven out of eight, that is [[pilote_cumul]]%, or [[pilote_total]]% relative to the eleven people recruited. The reminders of the instruction after some awakenings and the absence of a control prevent attributing this cumulative count to spontaneous persistence. Both denominators are kept.</p>

<h3 id="confusion">6. The central trap: decoding the sound that was played</h3>
<p>Suppose a forest is always paired with a birdsong. After this sound, the model announces “forest”. It could have recognized the auditory response, the file played or its time of presentation, without detecting a dreamed forest. The error becomes invisible if the theme of the sound is used as the label of the dream.</p>
<p>Our demonstration pairs four sounds with four contents independently. A model that identifies the sound perfectly scores [[cue_score]]% if the evaluation compares it with the sound, but only [[cue_contenu]]% if it compares it with the independent content. No progress in decoding the dream has taken place.</p>
<p>The proposed controls are therefore silent windows, unpaired sounds, several sounds per world, counterbalancing of the pairings and evaluation on sound cues absent from training. The immediate auditory response must be distinguished from later activity. The <a href="https://doi.org/10.1016/j.neuropsychologia.2025.109229">work on sounds in REM</a> motivates the study of incorporation; it does not exempt a new decoder from these controls.</p>

<h3 id="experience">7. An experiment that separates reading from intervention</h3>
<p><strong>First step: observation.</strong> Experiences learned before sleep serve as candidate themes. The model makes predictions on silent segments; the predictions are recorded before the report is collected. Raters blind to the prediction and the condition code the reports using a grid defined in advance. They may conclude “none”, “several” or “undetermined”. Forcing each dream into one of the four worlds would turn an open problem into an artificially easy exercise.</p>
<p><strong>Second step: randomized intervention.</strong> Once reading has been validated, compare the paired cue, a sound control and no signal. The reported content is an independent measure; the shift in the model’s score is a secondary measure. A system that optimizes its own score could learn to produce artefacts that it itself recognizes.</p>
<p><strong>Third step: value of the loop.</strong> Compare stimulation that depends on the brain state with a comparable presentation whose timing does not depend on that state. Without this contrast, one could observe an effect of the sounds while wrongly attributing the benefit to the decoder.</p>
<p>The design must hold out entire nights, then people if the goal is generalization. Neighboring windows from the same night must not end up on both sides of the evaluation. Permutations, intervals and analyses must respect this grouping. Eye and muscle movements are necessary controls, especially for high frequencies; their predictive power must be measured separately.</p>
<p>Missing reports remain missing. The incorporation rate among the reports collected and the yield among all planned opportunities answer different questions. Sleep must be assessed by its fragmentation, its architecture and its daytime impact. The absence of a statistically significant difference does not demonstrate that sleep is preserved: one must define what would count as an unacceptable degradation and estimate the uncertainty.</p>

<h3 id="mesures">8. A good average score can hide a bad detector</h3>
<p>In a purely hypothetical scenario, the target content appears in [[rare_prevalence]]% of segments. Even with a sensitivity of [[rare_sensibilite]]% and a specificity of [[rare_specificite]]%, only [[rare_precision]]% of alerts are correct. Bayes’ formula gives \(P(C\mid +)=sp/[sp+(1-c)(1-p)]\), where \(p\) is the frequency of the content, \(s\) the sensitivity and \(c\) the specificity. This calculation requires publishing false alerts and abstentions, not only an overall accuracy.</p>
<p>Another methodological example: four balanced classes, a one-sided test set at 5%, independent episodes and an assumed true accuracy of 40%. The exact binomial calculation gives:</p>
<div class="tableau"><table class="phrases"><thead><tr><th>Independent episodes</th><th>Successes needed</th><th>Probability of detecting the assumed effect</th></tr></thead><tbody>
<tr><td>[[d0_n]]</td><td>[[d0_k]]</td><td>[[d0_puissance]]%</td></tr>
<tr><td>[[d1_n]]</td><td>[[d1_k]]</td><td>[[d1_puissance]]%</td></tr>
<tr><td>[[d2_n]]</td><td>[[d2_k]]</td><td>[[d2_puissance]]%</td></tr>
</tbody></table></div>
<p>These are not recommended human sample sizes. Repeated episodes in the same person, the selection of many models and failures of recall change the calculation. These scenarios show why an uninformative first trial does not clearly separate success from failure.</p>

<h3 id="donnees">9. What is accessible to start with</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Resource</th><th>Verified access</th><th>Relevant work</th></tr></thead><tbody>
<tr><td><a href="https://doi.org/10.60493/31mg4-mfq53">Kumral EEG and reports</a></td><td>Record page and metadata accessible; announced archive of about 46.6 GB. Not downloaded here.</td><td>Check the correspondences between books, people, segments and reports before any reanalysis.</td></tr>
<tr><td><a href="https://osf.io/2bkus/">Code of the audiobook study</a></td><td>List of scripts and README read through the public API.</td><td>Reproduce the published similarity, then test its robustness. No rerun carried out in this study.</td></tr>
<tr><td><a href="https://huggingface.co/datasets/bcbl190626/SpanishBCBL">Brain2Qwerty v1</a></td><td>Dataset card and file tree accessible. About 262 GB announced.</td><td>Study a subset of awake typing. Group the identifiers of the same person and respect the stated license.</td></tr>
<tr><td><a href="https://mne.tools/stable/documentation/datasets.html#sample">MNE Sample</a></td><td>Simultaneous EEG and MEG, documented.</td><td>Learn software alignment. The documentation rules out its use as an evaluation of the hardware.</td></tr>
<tr><td><a href="https://github.com/facebookresearch/brain2qwerty">Brain2Qwerty v2</a></td><td>Code published, data announced as under embargo.</td><td>Read the architecture; do not claim a full reproduction without the data.</td></tr>
</tbody></table></div>
<p>The proposed priority is the audiobook study, because it already deals with sleep and content. Brain2Qwerty is a useful school of decoding, but its task is further from the result sought. The step that can be carried out immediately remains the inventory of annotations and usage rights, followed by a limited reanalysis compatible with the resources available.</p>

<h3 id="decision">10. The result to seek before building a helmet</h3>
<p>The next credible result would be a prediction of content on new data, better than the controls, with its errors and its uncertainty. Next would come a randomized effect on the reports, then the specific benefit of a closed loop and its compatibility with sleep. None of these milestones on its own measures an acceleration of lived time.</p>
<p>French teams have the relevant expertise: <a href="https://www.cea.fr/drf/joliot/Pages/Plateformes_et_infrastructures/plateformes_imagerie/plateforme-neurospin.aspx">NeuroSpin</a>, <a href="https://www.cea.fr/cea-tech/leti/Pages/recherche-appliquee/infrastructures-de-recherche/plateforme-CLINATEC.aspx">Clinatec</a> and the research on sleep onset presented by <a href="https://www.inserm.fr/actualite/portrait/comprendre-et-controler-lendormissement-le-reve-de-delphine-oudiette/">Inserm</a>. Their existence establishes neither the availability of time slots nor a partnership with Aeternam. The CEA-Leti page cited earlier combines a recent page date with a position start in 2020; it does not prove a current opening.</p>
<p><strong>Our research decision:</strong> start with open data, the quality of the annotations and the controls. MEG becomes relevant when a precise protocol makes it possible to measure what it adds to EEG. Observation and intervention will come together on evidence, step by step.</p>
""",
}

PROGRAMME = {
    'titre': 'Dreams, time and memory: a notebook of calculations',
    'description': 'Access to dreams, content, duration and memory: reanalyses of open data and simulations to test the methods.',
    'date': 'September 29, 2026',
    'corps': r"""

<h2 id="explication">Explanation</h2>
<p><strong>Can this research begin without a laboratory or funding? Yes.</strong> We ran a reanalysis of individual-level data, recomputed published results and built a digital laboratory. It lets us test our methods before trusting them with a conclusion about the brain.</p>
<p>This notebook gathers calculations on access to dreams, their content, their duration and how they are remembered. The question of continuity links these themes. The hypothesis of a life in one night would in addition require establishing a lengthening of experience; each question below has its own measure.</p>
[[figure_parcours]]
<h2 id="analyse">Detailed analysis</h2>
<h3 id="acces">1. Accessing the dream and establishing an exchange</h3>
<p>The table in <a href="https://doi.org/10.1016/j.cub.2021.01.026">Konkoly et al. (2021)</a> makes it possible to recompute two rates: [[dialogue_tous]]% correct responses across all trials, against [[dialogue_interpretes]]% among the responses classified as correct or incorrect. Silences and ambiguous responses account for [[dialogue_absents]]% of trials. These denominators answer different questions.</p>
<p>Our design conclusion: an exchange must not be evaluated only when it succeeds. One must count the attempts, the non-responses, the ambiguities and the number of people involved. The rate calculated per trial does not predict the success of a night for a new user.</p>
<p>A <a href="https://doi.org/10.1016/j.concog.2024.103759">2024 smartphone study</a> reports more lucid dreams with signals paired with prior training. Its individual-level data are available on request, not for download with the article. We use its published result, without claiming to have redone the individual-level analysis.</p>
<p><strong>Result for this strand.</strong> Exchanges during dreams are an existing experimental foothold. Our current contribution is the explicit calculation of the units and denominators needed to evaluate them.</p>
<h3 id="contenu">2. Steering a content and studying its persistence</h3>
<p>From the counts of <a href="https://doi.org/10.1016/j.concog.2020.102938">Dormio (2020)</a>, we recover a difference of [[incubation_difference]] points between the proportions of reports containing the theme with and without instruction. These are repeated reports, not independent people. We therefore do not calculate a binomial interval as if each report came from a new person.</p>
<p>The <a href="https://doi.org/10.3389/frsle.2026.1812535">June 2026 pilot</a> offers a lead on continuity between early sleep and REM sleep. The theme appears in REM in 7 of the 8 people who reached that stage: [[rem_conditionnel]]%. Relative to the 11 initial participants, this represents [[rem_total]]%. The first REM dream contains the theme in four people out of eight; the cumulative count includes later episodes and reminders of the instruction. These descriptive calculations do not give a causal effect: the study has no control group.</p>
<p>The hypothesis to work on is the persistence of stable elements — theme, place, character — across episodes. The model will have to count immediate incorporation, reappearance and coherence separately. Repeating the word for a theme does not demonstrate a continuous story.</p>
<p><strong>Result for this strand.</strong> There is a published lead for linking episodes through their content. Since the pilot’s raw data are announced as available on request, we recomputed its denominators, without inventing missing reports.</p>
<p>We are now taking the measurement of content further with the study <a href="/meg-eeg-reves/">Reading and steering dreams</a>: an audit of MEG decoders, open EEG data, transfer between sensors and the controls needed to distinguish a recognized sound from a dreamed content. <a href="/interfaces-cerveau/">BCIs, computer vision and interventions on memory</a> form a complementary strand. The new calculations are demonstrations of method, with no Aeternam human experiment.</p>
<h3 id="temps">3. Measuring time without confusing its dimensions</h3>
[[figure_dream]]
<p>We took the individual-level data of the Tononi series in <a href="https://doi.org/10.1038/s41467-025-61945-1">DREAM</a>: [[reveils]] awakenings, [[sujets]] people, all in stage N2. [[durees]] awakenings include a duration report; [[manquantes]] do not. The durations concern only recalled experiences.</p>
<p>[[longs]] reports fall in a class of at least one minute, that is [[part_longue]]% of the available reports. Giving each person the same weight, the mean becomes [[moyenne_sujets]]%, with a subject-level bootstrap interval of [[bootstrap_bas]] to [[bootstrap_haut]]%. This interval concerns a frequency of <em>reporting</em> in this corpus. It does not measure a speed of consciousness.</p>
<p>We also reconstructed the mean dream-minus-wake differences in the three published lucid tasks, from the difference and the paired test:</p>
<div class="tableau"><table><thead><tr><th>Task</th><th>Difference (s)</th><th>95% interval (s)</th></tr></thead><tbody>
<tr><td>Counting</td><td>[[compter_delta]]</td><td>[[compter_bas]] to [[compter_haut]]</td></tr>
<tr><td>Walking</td><td>[[marcher_delta]]</td><td>[[marcher_bas]] to [[marcher_haut]]</td></tr>
<tr><td>Gymnastics</td><td>[[gym_delta]]</td><td>[[gym_bas]] to [[gym_haut]]</td></tr>
</tbody></table></div>
<p>These intervals use the rounded published values and are not corrected for the three comparisons. They concern differences in task duration. We do not convert them into a ceiling on lived time.</p>
<p>The script checks two counterexamples. A choice between two durations does not separate the felt scale from the response criterion. And an experience of two minutes felt in one minute can remain invisible within a thirty-minute interval between awakenings. That is why the earlier global bounds were withdrawn.</p>
<p><strong>Result for this strand.</strong> The corpus gives descriptive measures and timed tasks. It does not demonstrate a general acceleration, nor does it allow one to be ruled out by a universal bound. To study the goal, one needs markers during the experience and a measure distinct from the final report.</p>
<h3 id="memoire">4. Distinguishing experience, memory and story</h3>
<p>In our reanalysis, a duration value exists for [[durees]] of the [[reveils]] awakenings. Replacing the others with a zero duration would equate “no duration reported” with “no experience”. We keep them as missing data.</p>
<p>An exploratory analysis compares, in the [[perception_n]] people who have both types of response, the frequency of durations of at least one minute when the experience is described as perceptual or not. The mean difference is [[perception_delta]] points, with a bootstrap interval of [[perception_bas]] to [[perception_haut]] points. It includes zero: this exploration does not allow us to conclude that there is a stable association. No causal link is established.</p>
<p>A scenario model illustrates the other distinction: a hundred scenes of three minutes take five hours. They could represent the moments of an eighty-year story, but they do not amount to eighty years lived continuously. This model makes a narrative hypothesis precise; it does not simulate the brain.</p>
<p>The program will therefore have to track separately the experienced duration, the amount of content recalled, the coherence between episodes and the feeling of personal continuity. The memory gains after sleep studied in the literature are not enough to establish these four results.</p>
<h3 id="calcul">5. Building a reliable digital laboratory</h3>
[[figure_erreurs]]
<p>We simulated [[simulations]] datasets per scenario, with 20, 40 or 80 people, three measurements per person and several levels of dependence between these measurements. These are artificial data: a target gain of 20% and a spread of 0.35 on the logarithms are chosen parameters.</p>
<p>In the scenario with 40 people and a correlation of 0.6, while no gain exists in the model, treating each measurement as independent produces [[faux_naif]]% false positives. The per-person analysis produces [[faux_sujet]]%, for an intended threshold of 2.5%. With a simulated gain of 20%, per-person detection reaches [[puissance]]% in the same scenario.</p>
<p>The simulation therefore checks a concrete risk: multiplying awakenings does not multiply independent observations to the same extent. These power results depend entirely on the chosen parameters; they do not predict the performance of a real device.</p>
<p>The bootstrap resamples whole people. The paired tests are reconstructed in their original unit. The scripts check the joins, the preservation of sample sizes, the missing data and the error rate under a known null hypothesis.</p>
<h3>What we produced</h3>
<p>A reproducible calculation base on reported time, a corrected reading of the results on interactive dreaming and incubation, a separation between duration and narrative, and a simulation bench for statistical errors. No participant was recruited and no experimental expense was incurred.</p>
<p>The next useful step is to add truly open individual-level datasets that make it possible to measure an action, a content or a memory. An accessible article whose data are only “on request” remains a documentary source: we do not invent its observations.</p>
<p>The <a href="/recherches/#simulation">simulation theory</a> remains a separate line of fundamental research. It plays no part in any of these calculations about the brain.</p>

""",
}
