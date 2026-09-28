"""Français : langue source du site.

Chaque [[marqueur]] est remplacé par un nombre de resultats.json, écrit selon les
conventions de la langue. Les formules $$…$$ et \\(…\\) sont identiques dans toutes
les langues. Chaîne brute (r\"\"\"…\"\"\") obligatoire à cause des barres obliques inverses.
"""
NOM = 'Français'
HTML_LANG = 'fr'
HREFLANG = 'fr'
DIR = 'ltr'
LOCALE_OG = 'fr_FR'
DECIMALE = ','

UI = {
    'devise': 'Recherche sur la théorie de la simulation.',
    'description_site': 'aeternam — recherche sur la théorie de la simulation.',
    'travaux': 'Travaux',
    'langue': 'Langue',
    'surtitre': 'Recherche · Test n° 1',
    'meta': 'version 2 · analyse secondaire reproductible',
    'verdict': 'Verdict à ce jour\xa0: non. Nous n’avons pas de meilleures raisons de nous croire simulés que de penser le contraire\xa0; nos tests ne détectent aucune signature de simulation, sans pouvoir exclure une simulation indétectable.',
    'introuvable': 'Page introuvable.',
    'fichier_pdf': 'aeternam-test-1-fr.pdf',
}

ARTICLE = {
    'titre': 'Une grille cubique face à GRB 221009A',
    'description': 'Ce que les photons observés par LHAASO imposent à la maille d’un espace discret, '
                   'et où cette contrainte s’arrête.',
    'date': '28 septembre 2026',
    'corps': r"""
<section class="resume">
<h2>En bref</h2>
<ul>
<li><strong>Si l’espace était une grille cubique</strong> où la lumière se propage comme dans une simulation numérique des équations de Maxwell, les photons les plus énergétiques arriveraient en retard. Sur le sursaut GRB&nbsp;221009A, LHAASO n’observe aucun retard de ce type.</li>
<li><strong>La maille est donc inférieure à [[a_resume]]&nbsp;m</strong>, pour une grille cubique en temps continu, avec la méthode la plus prudente et l’orientation la plus défavorable, ou à [[a_ml_resume]]&nbsp;m avec la méthode de vraisemblance. L’échelle d’énergie de la grille dépasse [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>Ce n’est pas une frontière nouvelle.</strong> Beane, Davoudi et Savage obtenaient déjà le même ordre de grandeur en 2012 (environ [[b_beane]]&nbsp;m) à partir des rayons cosmiques. Nous obtenons un ordre de grandeur comparable, avec une autre observable et d’autres hypothèses&nbsp;; les deux bornes portent sur des modèles différents et ne sont pas interchangeables.</li>
<li><strong>Nouveau&nbsp;: le pas de temps compte.</strong> Si le temps est lui aussi découpé, comme dans toute simulation numérique, l’effet diminue. Au pas maximal stable, la lumière ne subit plus aucune dispersion le long des huit directions diagonales du cube&nbsp;: un seul sursaut ne permet alors aucune borne universelle. Pour 95&nbsp;% des orientations, la maille reste inférieure à [[a95_sigma1]]&nbsp;m.</li>
<li><strong>Une grille dont l’erreur dominante serait linéaire</strong> en <em>a</em> est exclue jusqu’à [[a_lineaire]]&nbsp;m, un dixième de la longueur de Planck.</li>
<li><strong>Une maille de la taille de Planck reste hors de portée</strong>&nbsp;: son effet serait environ [[facteur_planck]] fois trop faible pour ce test.</li>
<li><strong>En vérifiant la littérature</strong>, nous avons relevé une incohérence de conversion dans un article de 2025 (Xi et Shu)&nbsp;: leur borne quadratique paraît surestimée d’un facteur [[xs_facteur]].</li>
<li><strong>Aucune détection, aucune probabilité d’être simulés.</strong> Le test borne une architecture précise&nbsp;; il ne dit rien de l’existence d’un simulateur.</li>
</ul>
</section>

<h2 id="question">1. La question testée</h2>
<p>Une simulation numérique représente l’espace par un nombre fini de points. Une onde qui s’y propage ne se comporte pas exactement comme dans le continu&nbsp;: sa vitesse dépend légèrement de sa longueur d’onde. Pour la lumière, la vitesse dépendrait donc de l’énergie des photons. L’effet est minuscule, mais il s’accumule sur des distances cosmologiques.</p>
<p>GRB&nbsp;221009A est le sursaut gamma le plus brillant jamais enregistré. L’observatoire LHAASO en a détecté des photons au-delà de 10&nbsp;TeV, partis il y a environ deux milliards d’années (décalage vers le rouge <em>z</em>&nbsp;=&nbsp;[[z]]). Si la vitesse de la lumière dépendait de l’énergie, les photons de haute énergie arriveraient après ceux de basse énergie. La collaboration LHAASO a cherché ce retard et ne l’a pas trouvé.</p>
<p>La question est donc précise&nbsp;: <em>quelle maille ce retard nul autorise-t-il encore&nbsp;?</em> Elle ne suppose ni que toute simulation utiliserait une grille, ni qu’une grille prouverait une simulation.</p>

<h2 id="modele">2. Le modèle&nbsp;: Maxwell sur une grille</h2>
<p>On place les champs électromagnétiques sur un réseau cubique de maille <em>a</em>, exactement comme le schéma de Yee (1966) qu’utilisent les simulations numériques des équations de Maxwell, ou comme la formulation hamiltonienne de l’électrodynamique sur réseau (Kogut et Susskind, 1975). Le temps s’écoule soit continûment, soit par pas \(\Delta t\). Une onde plane de vecteur d’onde \(\mathbf k\) et de pulsation \(\omega\) obéit alors à la relation de dispersion&nbsp;:</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>Le schéma n’est stable que si \(c\,\Delta t\le a/\sqrt{3}\). On écrit donc \(c\,\Delta t=\sigma a/\sqrt{3}\), avec un nombre de Courant \(0\le\sigma\le1\)&nbsp;; \(\sigma=0\) correspond au temps continu. Pour des photons dont la longueur d’onde est très grande devant la maille, la vitesse de groupe devient, avec \(E=\hbar\omega\)&nbsp;:</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) dépend de la direction \(\mathbf n\) du photon par rapport aux axes de la grille&nbsp;: \(Q=1\) le long d’un axe, \(Q=1/3\) le long d’une grande diagonale. Trois propriétés comptent pour la suite&nbsp;:</p>
<ul>
<li>l’effet est <strong>quadratique</strong>&nbsp;: une maille dix fois plus fine produit un effet cent fois plus faible&nbsp;;</li>
<li>les photons sont <strong>ralentis</strong>, jamais accélérés, tant que le schéma est stable&nbsp;;</li>
<li>les deux polarisations se propagent de la même façon&nbsp;: <strong>pas de biréfringence</strong>, si bien que les contraintes de polarisation, très fortes, ne s’appliquent pas ici.</li>
</ul>

<h2 id="lhaaso">3. La confrontation avec LHAASO</h2>
<p>LHAASO décrit un retard quadratique par \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) et publie des intervalles sur \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\), avec \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV (équations 2, 3 et 5 de l’article). Par identification&nbsp;:</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>Le retard accumulé entre deux photons d’énergies \(E_h\) et \(E_l\) s’écrit</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>avec la cosmologie de LHAASO (<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc, Ω<sub>m</sub>&nbsp;=&nbsp;[[om]], Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]), qui donne <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s. La mesure ne contraint que la combinaison \(a\sqrt{Q_{\mathrm{eff}}}\). Le tableau I de LHAASO donne, à 95&nbsp;%&nbsp;:</p>
<div class="tableau"><table>
<thead><tr><th>Méthode</th><th>Limite basse</th><th>Meilleur ajustement</th><th>Limite haute</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML (calibrée)</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>Le zéro appartient aux trois intervalles&nbsp;: aucun retard n’est détecté. Les trois méthodes analysent le même sursaut&nbsp;; nous ne les combinons pas. Une limite haute \(U\) sur \(\eta_2\) donne</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>En temps continu, on obtient&nbsp;:</p>
<div class="tableau"><table>
<thead><tr><th>Méthode</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\), pire orientation (m)</th><th>\(a\), 95&nbsp;% des orientations (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML (calibrée)</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>Le résumé retient la valeur la plus prudente, [[a_resume]]&nbsp;m&nbsp;: c’est une enveloppe de présentation, pas un nouvel intervalle. À cette limite, un photon de 1&nbsp;TeV arriverait au plus [[retard_limite]]&nbsp;s après un photon de [[e_bas]]&nbsp;TeV.</p>
<p>Quelques prédictions, qui ne sont pas des mesures (photon de 1&nbsp;TeV comparé à un photon de [[e_bas]]&nbsp;TeV)&nbsp;:</p>
<div class="tableau"><table>
<thead><tr><th>Maille</th><th>\(\eta_2\) prédit</th><th>Retard prédit</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]] à [[p26_eta_max]]</td><td>[[p26_ret_min]] à [[p26_ret_max]]&nbsp;s</td><td>exclue pour toute orientation</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]] à [[p27_eta_max]]</td><td>[[p27_ret_min]] à [[p27_ret_max]]&nbsp;s</td><td>exclue près des axes (\(Q>\)&nbsp;[[q_cal_axe]]) par la seule méthode calibrée</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]] à [[p28_eta_max]]</td><td>[[p28_ret_min]] à [[p28_ret_max]]&nbsp;ms</td><td>non exclue</td></tr>
<tr><td>[[lpl]]&nbsp;m (Planck)</td><td>[[pl_eta_min]] à [[pl_eta_max]]</td><td>[[pl_ret_min]] à [[pl_ret_max]]&nbsp;s</td><td>hors de portée</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. Jusqu’où la borne résiste</h2>
<h3>L’orientation de la grille</h3>
<p>On ignore comment la grille serait orientée par rapport à la direction du sursaut. La borne principale prend le cas le moins favorable, \(Q=1/3\). Sur un million de directions réparties uniformément, \(Q\) vaut [[q_mediane]] en médiane et dépasse [[q_5]] dans 95&nbsp;% des cas&nbsp;: la borne bouge peu, avec [[ccf_95]]&nbsp;m pour 95&nbsp;% des orientations et [[ccf_mediane]]&nbsp;m pour l’orientation médiane. Ces fractions sont géométriques&nbsp;: ce ne sont pas des probabilités sur l’Univers.</p>
<h3>Le temps discret, point faible de la borne</h3>
<p>Une simulation avance par pas de temps. Discrétiser le temps produit une erreur de signe opposé, qui compense en partie celle de l’espace (le terme \(-\sigma^{2}/3\)). Pour la méthode prudente&nbsp;:</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>Pire orientation</th><th>95&nbsp;% des orientations</th><th>Orientation médiane</th></tr></thead>
<tbody>
<tr><td>0 (temps continu)</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1 (pas maximal)</td><td>[[s4_cdt]]</td><td>aucune borne</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>Au pas maximal stable, la compensation est exacte le long des grandes diagonales, et pas seulement au premier ordre&nbsp;: la relation de dispersion y redonne \(\omega=ck\) pour toute longueur d’onde. Une simulation réglée ainsi échapperait entièrement à ce test si le sursaut tombait sur l’une de ses huit directions diagonales. C’est la principale limite d’une borne tirée d’une seule source&nbsp;; plusieurs sources dans des directions différentes la lèveraient, car elles ne peuvent pas, sauf coïncidence, être toutes alignées sur des diagonales.</p>
<h3>Une maille fixe ou étirée par l’expansion</h3>
<p>Nous supposons une maille physique fixe. Si la grille s’étirait avec l’Univers (maille comobile), l’effet ne croîtrait plus avec le décalage vers le rouge et \(I_2\) serait remplacé par \(I_0\)&nbsp;: la borne s’affaiblit d’un facteur \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]], soit [[comobile_a]]&nbsp;m. À <em>z</em>&nbsp;=&nbsp;[[z]], ce choix compte peu.</p>
<h3>Des schémas plus précis</h3>
<p>Un simulateur peut employer un schéma d’ordre supérieur, dont l’erreur dominante varie comme \(a^{4}\). L’effet devient alors quartique en énergie, et la borne sur \(a\) beaucoup plus faible. LHAASO ne publie pas de contrainte de ce type pour ce sursaut&nbsp;; la chiffrer demanderait les données photon par photon. Des termes conçus pour compenser la dispersion échapperaient aussi à la borne. Ce sont d’autres modèles, à tester séparément.</p>
<h3>Et si l’erreur était linéaire&nbsp;?</h3>
<p>Un réseau symétrique ne produit aucun effet linéaire en \(a\). Une discrétisation qui en produirait, en brisant la symétrie entre les deux sens de propagation, tomberait sous la borne linéaire de LHAASO, \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\)&nbsp;: avec un coefficient d’ordre un, \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m, soit un dixième de la longueur de Planck. Toute grille de ce type plus grossière est exclue.</p>
<h3>La validité du calcul</h3>
<p>Le développement suppose \(aE/\hbar c\ll1\). À la borne, même pour des photons de 20&nbsp;TeV, \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]. Nous avons aussi comparé le développement à la relation de dispersion exacte&nbsp;: pour \(ak\)&nbsp;=&nbsp;[[ak_test]], l’écart relatif ne dépasse pas [[ecart_dispersion]], comme attendu.</p>

<h2 id="contexte">5. Ce que cela vaut, comparé à l’existant</h2>
<p>Beane, Davoudi et Savage (2012) ont étudié une simulation de la chromodynamique quantique sur réseau. Ils bornaient l’inverse de la maille à \(1/b\gtrsim10^{11}\)&nbsp;GeV, soit \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m, à partir de la coupure du spectre des rayons cosmiques. Notre borne prudente vaut [[beane_ratio]] fois la leur&nbsp;; les méthodes de vraisemblance de LHAASO donnent [[beane_ml_min]] à [[beane_ml_max]] fois la leur. Les deux bornes sont du même ordre de grandeur, mais elles reposent sur des observables, des particules et des modèles différents&nbsp;: elles ne se confirment pas l’une l’autre au sens strict et ne sont pas interchangeables.</p>
<p>La longueur de Planck, [[lpl]]&nbsp;m, reste huit ordres de grandeur plus bas. Pour une maille de cette taille, l’effet serait [[facteur_planck_exact]] fois plus faible que la limite. Comme il croît avec le carré de l’énergie, il faudrait des photons environ cent millions de fois plus énergétiques, bien au-delà de tout ce qui est observé&nbsp;: à cet ordre, aucun test de temps de vol ne peut atteindre une grille de Planck.</p>

<h2 id="xi-shu">6. Une vérification de la littérature&nbsp;: Xi et Shu (2025)</h2>
<p>Xi et Shu ont analysé le même sursaut avec une autre méthode et annoncent \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV (leur tableau III), environ [[xs_rapport_lhaaso]] fois la borne de LHAASO. En reprenant leurs propres définitions, nous ne retrouvons pas cette valeur.</p>
<ul>
<li>Leur équation (3) fixe le retard en \((E/E_{\mathrm{QG},n})^{n}\). Pour \(n=1\), leur conversion (6), \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\) avec \(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]], est cohérente&nbsp;: nous trouvons [[xs_c1]].</li>
<li>Pour \(n=2\), leur équation (7), \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\) avec \(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]], garde la forme en \(1/\theta\). Appliquée à leur limite \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV², elle redonne bien leur tableau ([[xs_eq7]]&nbsp;GeV). Mais le retard étant quadratique, leur équation (3) impose une dépendance en \(1/\sqrt{\theta_2}\)&nbsp;: \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\), soit \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV.</li>
<li>L’écart est d’un facteur [[xs_facteur]]. Explication plausible&nbsp;: \(\varepsilon^{2}\theta_2\) vaut [[xs_eps2]], et [[xs_c2_imprime]] ressemble à la racine de [[xs_eps2_imprime]] prise sur la seule puissance de dix.</li>
</ul>
<p>Statut&nbsp;: incohérence apparente dans la version 1 de l’article, à confirmer avec les auteurs. Nous ne réanalysons pas leurs données et ne jugeons pas leurs autres résultats. Corrigée, leur borne resterait [[xs_vs_lhaaso]] fois plus forte que celle de LHAASO. Nous ne l’utilisons pas.</p>

<h2 id="limites">7. Ce que ce test ne dit pas</h2>
<ul>
<li>Il ne détecte rien&nbsp;: un retard nul reste compatible avec toutes les mesures.</li>
<li>Il ne calcule aucune probabilité que nous soyons dans une simulation&nbsp;; le «&nbsp;95&nbsp;%&nbsp;» porte sur un paramètre physique.</li>
<li>Il borne une architecture précise&nbsp;: grille cubique, schéma de Yee, maille fixe, sans compensation.</li>
<li>Même un retard détecté ne désignerait pas un ordinateur&nbsp;: une physique fondamentalement discrète, ou d’autres effets de gravité quantique, produiraient le même signal.</li>
<li>Les intervalles de LHAASO reposent sur des hypothèses sur l’émission de la source&nbsp;; nous en héritons.</li>
</ul>

<h2 id="suite">8. Prochaines étapes</h2>
<ol>
<li>Combiner plusieurs sources vues dans des directions différentes, pour fermer l’angle mort des diagonales.</li>
<li>Chiffrer les schémas d’ordre supérieur (effet en \(a^{4}\)), ce qui demande les données photon par photon.</li>
<li>Demander à Xi et Shu de clarifier leur conversion.</li>
<li>Étendre le test à d’autres signatures d’une grille&nbsp;: anisotropie des rayons cosmiques, particules chargées.</li>
</ol>

<h2 id="reproduire">9. Reproduire</h2>
<p>Tout est recalculé par un script Python sans dépendance, qui vérifie d’abord ses propres formules&nbsp;: développement contre dispersion exacte, diagonale exacte, conversions aller-retour, intégrale cosmologique, moyenne de \(Q\) égale à 3/5.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>&nbsp;: le script (Python&nbsp;3.10 ou plus récent, bibliothèque standard)</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>&nbsp;: toutes les valeurs calculées</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>&nbsp;: cette note en PDF</li>
</ul>
<p>Une contre-vérification indépendante (numpy, scipy) retrouve l’intégrale cosmologique à 10<sup>−15</sup> près, les quantiles d’orientation sur dix millions de tirages aléatoires, et la vitesse de groupe par résolution numérique de la dispersion.</p>
<p>Cette note remplace une première version du 28 septembre 2026. Elle ajoute le temps discret, l’orientation, la maille comobile, l’effet linéaire et la comparaison avec Beane et al.</p>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a> (révision du 13 février 2026)&nbsp;: équations 2, 3 et 5, tableau I.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a> (2025)&nbsp;: équations 3, 6 et 7, tableaux I et III.</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302 (1966).</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395 (1975).</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House&nbsp;: dispersion numérique et stabilité du schéma de Yee.</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>&nbsp;: constantes fondamentales.</li>
</ol>
""",
}

ARTICLE_2 = {
    'titre': 'Les rayons cosmiques dessinent-ils une grille ?',
    'description': 'Les particules les plus énergétiques jamais enregistrées par l’observatoire Pierre Auger, '
                   'confrontées à la trace qu’une grille cubique devrait leur laisser.',
    'date': '28 septembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>Non.</strong> Le test ne détecte aucun écart significatif à l’isotropie dans les directions des [[n_evt]] rayons cosmiques les plus énergétiques mesurés par l’observatoire Pierre Auger&nbsp;: sous le modèle isotrope, [[p4_pct]]&nbsp;% des ciels simulés, soumis à la même recherche, présentent un motif cubique au moins aussi marqué que celui observé.</p>
<p>Ce «&nbsp;non&nbsp;» a une portée limitée. Ce nombre n’est ni la probabilité que le hasard explique les données, ni celle qu’une grille existe. Un motif plus faible n’est pas exclu, et l’absence de motif cubique observable ne prouve pas l’absence de grille.</p>
</section>

<h2 id="explication">Explication</h2>
<p>Si notre monde était calculé par un ordinateur, l’espace serait peut-être découpé en tout petits cubes, comme une image est faite de pixels. En 2012, trois physiciens ont remarqué qu’un tel découpage laisserait une trace&nbsp;: les particules les plus rapides de l’Univers n’arriveraient pas de la même façon de toutes les directions. Certaines directions seraient favorisées, disposées comme les faces ou les coins d’un cube.</p>
<p>Ces particules existent&nbsp;: ce sont les rayons cosmiques, des noyaux d’atomes venus de l’espace avec une énergie bien supérieure à tout ce que produisent nos accélérateurs. En Argentine, l’observatoire Pierre Auger les guette avec un immense réseau de détecteurs. Il a publié la liste de ses [[n_evt]] prises les plus énergétiques, captées entre 2004 et 2020, avec la direction d’où chacune est arrivée.</p>
<p>Nous avons pris ces [[n_evt]] directions et cherché si elles se rangent le long d’un cube. Comme personne ne sait comment ce cube serait tourné, nous en avons essayé [[n_orient]] positions. La meilleure colle un peu aux données. Mais quand on essaie autant de positions, on en trouve toujours une qui colle un peu, même dans un ciel dû au pur hasard.</p>
<p>Pour trancher, nous avons fabriqué [[n_ciels]] faux ciels tirés au hasard, vus par le même observatoire, et refait exactement la même recherche sur chacun. Dans [[p4_pct]]&nbsp;% d’entre eux, on trouve un cube qui colle au moins aussi bien. Le vrai ciel ne se distingue donc pas de ces faux ciels. Pour parler d’un indice, il aurait fallu qu’il fasse mieux que presque tous les faux ciels.</p>
<p>Conclusion&nbsp;: aucune trace de grille n’est détectée. Mais cette recherche ne pouvait voir qu’un motif fort&nbsp;: avec seulement [[n_evt]] particules, un motif discret passerait inaperçu. De plus, les champs magnétiques de notre galaxie dévient ces particules en chemin, ce qui brouillerait une partie du motif. Ce test ne prouve donc pas que l’espace est continu&nbsp;; il montre que, là où l’on pouvait regarder, il n’y a rien.</p>

<h2 id="analyse">Analyse détaillée</h2>

<h3>1. De la grille à une prédiction testable</h3>
<p>Sur un réseau cubique de maille \(a\), le laplacien discret remplace \(k^{2}\) par \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\). Pour un champ libre,</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>où \(\mathbf n\) est la direction de propagation dans les axes du réseau. C’est la même fonction \(Q\) que dans le test n°&nbsp;1. Plus généralement, tout effet de la grille sur les directions d’arrivée (propagation, coupure du spectre dépendant de la direction) est une fonction de \(\mathbf n\) invariante par le groupe du cube \(O_h\). Or les harmoniques sphériques invariantes par \(O_h\) n’existent que pour \(\ell=0,4,6,8,\dots\)&nbsp;: la première anisotropie permise est l’harmonique cubique \(\ell=4\), proportionnelle à \(Q-3/5\). C’est notre test principal, fixé avant d’ouvrir les données&nbsp;; \(\ell=6\) est testé en second. Beane, Davoudi et Savage écrivent que la simulation «&nbsp;pourrait se révéler dans les distributions des rayons cosmiques de plus haute énergie, par un degré de brisure de la symétrie de rotation qui reflète la structure du réseau sous-jacent&nbsp;».</p>

<h3>2. Les données</h3>
<p>Catalogue de l’observatoire Pierre Auger (ApJS 264, 50, 2023)&nbsp;: les [[n_evt]] gerbes de plus haute énergie enregistrées du 1<sup>er</sup> janvier 2004 au 31 décembre 2020, de [[e_min]] à [[e_max]]&nbsp;EeV, avec des angles zénithaux jusqu’à [[zmax]]°. Le fichier ouvert contient aussi [[n_calib]] événements hybrides d’étalonnage, hors des [[n_evt]]&nbsp;: nous les écartons. Nous utilisons l’ascension droite et la déclinaison reconstruites par le détecteur de surface. L’empreinte SHA-256 du fichier est vérifiée à chaque exécution. À ces énergies, l’efficacité de détection est totale jusqu’à [[zmax]]°, si bien que l’exposition est purement géométrique.</p>

<h3>3. L’exposition du détecteur</h3>
<p>Un détecteur au sol, à la latitude \(a_0\)&nbsp;=&nbsp;[[lat]]°, qui accepte les zéniths \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]°, a une exposition uniforme en ascension droite et, en déclinaison \(\delta\) (Sommers, 2001)&nbsp;:</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>Le ciel visible s’arrête à \(\delta\)&nbsp;=&nbsp;[[dec_max]]°, soit [[ciel_pct]]&nbsp;% de la sphère. Un ciel isotrope vu par Auger n’est donc pas uniforme&nbsp;: toute la suite compare les données à ce ciel-là, pas à une sphère uniforme.</p>

<h3>4. La statistique</h3>
<p>Soit \(R\) une orientation de la grille, de lignes \(\mathbf e_k\), et \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). Pour les \(N\) directions observées&nbsp;:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>où \(\langle\cdot\rangle_\omega\) est la moyenne sur un ciel isotrope pondéré par l’exposition. \(T>0\) signale un excès le long des axes du cube, \(T<0\) le long de ses diagonales&nbsp;; la valeur absolue couvre les deux. Comme \(f\) est un polynôme de degré 4, \(T(R)\) ne dépend des données que par les 15 moments \(\sum_i\mathbf n_i^{\alpha}\)&nbsp;; moyenne et variance sont calculées exactement par quadrature de Gauss-Legendre. Le maximum porte sur [[n_orient]] orientations tirées uniformément (mesure de Haar). Pour \(\ell=6\), on prend \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\), avec \(\alpha\)&nbsp;=&nbsp;[[alpha6]] (soit \(-15/11\)), qui la rend orthogonale à \(\ell=4\)&nbsp;; le test combiné maximise \(T_4^{2}+T_6^{2}\).</p>

<h3>5. Calibrer le hasard</h3>
<p>Chercher la meilleure orientation parmi [[n_orient]] gonfle mécaniquement \(Z_4\)&nbsp;: il ne suit pas une loi normale. Nous tirons donc [[n_ciels]] ciels isotropes de \(N\) événements selon l’exposition, et leur appliquons exactement la même maximisation. Sous l’hypothèse «&nbsp;pas de grille&nbsp;», \(Z_4\) a pour médiane [[z4_50]]&nbsp;; il dépasse [[z4_95]] dans 5&nbsp;% des cas, [[z4_99]] dans 1&nbsp;% et [[z4_999]] dans 0,1&nbsp;%. La p-valeur, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), inclut ainsi le coût du choix de l’orientation.</p>

<h3>6. Résultat</h3>
<div class="tableau"><table>
<thead><tr><th>Test</th><th>Statistique observée</th><th>p-valeur</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (principal)</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\) et \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>À la meilleure orientation, la moyenne de \(Q\) vaut [[q_obs]] contre [[q_iso]] attendu, soit un excès de [[q_ecart_pct]]&nbsp;% vers les axes. Ce n’est pas significatif&nbsp;: \(p\)&nbsp;=&nbsp;[[p4]] pour le test principal, et aucun test secondaire ne descend sous 0,05. Les données sont compatibles avec l’absence de toute symétrie cubique.</p>

<h3>7. Ce que le test pouvait voir</h3>
<p>Pour chiffrer la sensibilité, on injecte un motif cubique&nbsp;: densité proportionnelle à \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Le long d’un axe (\(Q=1\)), le flux vaut \(1+\varepsilon\) fois la moyenne&nbsp;; le long d’une diagonale (\(Q=1/3\)), il vaut \(1-2\varepsilon/3\) fois la moyenne. Avec \(\varepsilon>0\), l’excès porte donc sur les axes&nbsp;; avec \(\varepsilon<0\), il porte sur les diagonales et vaut \(2\lvert\varepsilon\rvert/3\).</p>
<p>La limite supérieure à 95&nbsp;% dépend de la convention sur l’orientation. Si l’orientation de la grille est tirée au hasard pour chaque ciel simulé ([[n_ciels_signal]] ciels par amplitude), on obtient une limite moyenne sur les orientations&nbsp;: \(\varepsilon\le\)&nbsp;[[eps_axes]] et \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]]. Une moyenne ne garantit pas la couverture pour chaque orientation&nbsp;: nous refaisons donc le calcul à orientation fixée, pour [[n_orient_fixes]] orientations dont la moins visible par Auger ([[n_ciels_fixes]] ciels par amplitude). La limite varie alors de [[eps_axes_fix_min]] à [[eps_axes_fix]] vers les axes et de [[eps_diag_fix_min]] à [[eps_diag_fix]] vers les diagonales&nbsp;; nous retenons la valeur la moins contraignante. Un excès de flux allant jusqu’à environ [[exces_axes_pct]]&nbsp;% le long des axes, ou [[exces_diag_pct]]&nbsp;% le long des diagonales, n’est donc pas exclu. C’est une contrainte faible, fixée par le petit nombre d’événements, établie sur les orientations testées et non démontrée pour toutes.</p>
<p>Le script vérifie d’abord sa propre chaîne&nbsp;: invariance de \(Q\) par le groupe du cube, développement polynomial exact, exposition nulle au-delà de [[dec_max]]°, \(T\) centré réduit sous isotropie, orthogonalité de \(\ell=6\) à \(\ell=4\), et détection d’un motif injecté franc, dont l’orientation est retrouvée à [[ecart_orient]]° près.</p>

<h3>8. Limites</h3>
<ul>
<li>Les rayons cosmiques sont chargés&nbsp;: les champs magnétiques galactiques et extragalactiques dévient leurs directions, d’autant plus que les noyaux sont lourds. Le motif cherché est large (un axe et une diagonale sont séparés de [[angle_diag]]°) et résiste à des déviations modestes, mais une empreinte fixée à la source ou pendant la propagation serait en partie effacée.</li>
<li>Nous supposons la grille fixe par rapport aux étoiles lointaines (coordonnées équatoriales). Une grille en mouvement ou en rotation par rapport à elles demanderait un autre test.</li>
<li>[[n_evt]] événements et [[ciel_pct]]&nbsp;% du ciel&nbsp;: la puissance statistique est faible, comme le montre la limite ci-dessus.</li>
<li>De vraies anisotropies astrophysiques peuvent contenir une composante \(\ell=4\). Un résultat positif aurait exigé de les exclure&nbsp;; un résultat nul n’en dépend pas.</li>
<li>Aucune probabilité d’être simulés n’est calculée&nbsp;: le test porte sur une signature précise, celle d’une grille cubique.</li>
</ul>

<h3>9. Reproduire</h3>
<p>Un script Python (numpy) refait tout en quelques minutes&nbsp;: lecture et contrôle des données, autotests, statistique, ciels simulés, limites supérieures. Le générateur aléatoire a une graine fixe&nbsp;: les résultats sont identiques d’une exécution à l’autre.</p>
<p>Corrections du 28 septembre 2026, après relecture&nbsp;: l’excès de flux le long des diagonales avait été confondu avec le paramètre \(\lvert\varepsilon\rvert\), alors qu’il vaut \(2\lvert\varepsilon\rvert/3\)&nbsp;; la limite à orientation fixée a été ajoutée&nbsp;; le verdict a été reformulé pour ne pas présenter la p-valeur comme une probabilité sur les hypothèses.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-2/analyse.py" download>analyse.py</a>&nbsp;: le script</li>
<li><a href="/fichiers/test-2/resultats.json" download>resultats.json</a>&nbsp;: toutes les valeurs calculées</li>
<li><a href="/fichiers/test-2/donnees/auger_catalogSD.csv" download>auger_catalogSD.csv</a>&nbsp;: les données de l’observatoire Pierre Auger (licence CC BY-SA 4.0)</li>
</ul>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Pierre Auger Collaboration, <cite>A Catalog of the Highest-Energy Cosmic Rays Recorded During Phase I of Operation of the Pierre Auger Observatory</cite>, ApJS 264, 50 (2023), <a href="https://arxiv.org/abs/2211.16020">arXiv:2211.16020</a>.</li>
<li>Pierre Auger Collaboration, <cite>Auger Open Data</cite>, release 3, <a href="https://doi.org/10.5281/zenodo.10488964">DOI 10.5281/zenodo.10488964</a>&nbsp;; efficacité de détection&nbsp;: <a href="https://opendata.auger.org/data.php">opendata.auger.org</a>.</li>
<li>P. Sommers, <cite>Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory</cite>, Astroparticle Physics 14, 271 (2001), <a href="https://arxiv.org/abs/astro-ph/0004016">arXiv:astro-ph/0004016</a>.</li>
</ol>
""",
}

ARTICLE_3 = {
    'titre': 'La lumière va-t-elle moins vite dans certaines directions ?',
    'description': 'Huit sources de rayons gamma réparties sur le ciel, combinées pour fermer l’angle mort '
                   'du test n° 1 et borner la maille d’une grille cubique quelle que soit son orientation.',
    'date': '28 septembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>Non.</strong> Aucune des [[n_src]] sources étudiées ne montre le retard que produirait une grille. En combinant leurs directions, une grille cubique de maille supérieure ou égale à [[a_exclue]]&nbsp;m est exclue, quelle que soit son orientation et quel que soit son pas de temps&nbsp;: l’angle mort du test n°&nbsp;1 est fermé.</p>
</section>

<h2 id="explication">Explication</h2>
<p>Si l’Univers était calculé sur une grille, comme une image est faite de pixels, la lumière n’y avancerait pas tout à fait à la même vitesse dans toutes les directions. La lumière la plus énergétique prendrait un très léger retard, plus fort le long des arêtes du quadrillage que le long de ses diagonales. Sur des milliards d’années de voyage, ce retard deviendrait mesurable.</p>
<p>Le test n°&nbsp;1 cherchait ce retard dans le sursaut gamma le plus brillant jamais observé, et n’a rien vu. Mais il restait une faille&nbsp;: si la simulation avance dans le temps par le plus grand pas possible, la lumière ne prend plus aucun retard le long des diagonales du quadrillage. Une source unique située sur une diagonale ne permettait alors aucune conclusion.</p>
<p>Ici, on regarde [[n_src]] sources à la fois, dans des directions différentes du ciel&nbsp;: trois explosions d’étoiles lointaines, quatre galaxies à trou noir très actif et le pulsar de la nébuleuse du Crabe. Pour chacune, une équipe d’astronomes a déjà mesuré qu’aucun retard n’apparaît, jusqu’à une certaine finesse. Nous avons relu chaque article, ramené tous les résultats à la même convention, puis cherché l’orientation du quadrillage la plus favorable à une grille cachée, celle qui affaiblit le plus la limite.</p>
<p>Il est impossible de placer toutes les sources sur des diagonales en même temps. Même dans l’orientation la plus favorable, trois sources restent assez loin d’une diagonale pour qu’un retard ait dû apparaître. Une grille dont les cases mesurent au moins [[a_exclue]]&nbsp;m est donc exclue dans toutes les orientations. Cette taille reste environ [[planck_x]] fois plus grande que la longueur de Planck&nbsp;: une grille beaucoup plus fine reste entièrement possible.</p>

<h2 id="analyse">Analyse détaillée</h2>

<h3>1. Le modèle</h3>
<p>Comme au test n°&nbsp;1&nbsp;: équations de Maxwell sur un réseau cubique de maille \(a\) (schéma de Yee), pas de temps \(c\,\Delta t=\sigma a/\sqrt{3}\) avec \(0\le\sigma\le1\). À l’ordre dominant,</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\,Q_{\mathrm{eff}}\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3},\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>Comme \(1/3\le Q\le1\), \(Q_{\mathrm{eff}}\ge0\)&nbsp;: le photon est toujours ralenti, et \(Q_{\mathrm{eff}}=0\) exactement sur les grandes diagonales lorsque \(\sigma=1\). À la borne finale, \(aE/\hbar c\)&nbsp;=&nbsp;[[ae]] pour un photon de 20&nbsp;TeV&nbsp;: le développement est valide.</p>

<h3>2. Des limites publiées à une borne sur la maille</h3>
<p>Les huit articles décrivent un retard quadratique par \(v/c\simeq1-\tfrac{3}{2}(E/E_{\mathrm{QG},2})^{2}\), avec la distance de Jacob et Piran \(K_2=\int_0^{z}(1+z')^{2}\,dz'/H(z')\). Par identification,</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}}\quad\Longrightarrow\quad a\sqrt{Q_{\mathrm{eff}}(\mathbf n_i)}\le B_i=\frac{\sqrt{12}\,\hbar c}{E_i}.$$
<p>Règle fixée d’avance&nbsp;: limite à 95&nbsp;%, cas sous-luminal, temps de vol, méthode la moins contraignante de chaque article. Chaque limite est ramenée à la cosmologie de LHAASO par \(E_i\sqrt{K_2^{\mathrm{LHAASO}}(z_i)/K_2^{(i)}(z_i)}\)&nbsp;; le facteur ne dépasse pas [[fc_max]]. Chaque conversion publiée est refaite à partir des paramètres imprimés et retrouve la valeur de l’article (autotests).</p>
<div class="tableau"><table>
<thead><tr><th>Source</th><th>Instrument</th><th>\(z\) ou distance</th><th>\(E_{\mathrm{QG},2}\) publiée (GeV)</th><th>Cosmologie commune (GeV)</th><th>\(B_i\) (m)</th></tr></thead>
<tbody>
<tr><td>GRB 221009A</td><td>LHAASO</td><td>[[s0_z]]</td><td>[[s0_pub]]</td><td>[[s0_com]]</td><td>[[s0_b]]</td></tr>
<tr><td>GRB 190114C</td><td>MAGIC</td><td>[[s1_z]]</td><td>[[s1_pub]]</td><td>[[s1_com]]</td><td>[[s1_b]]</td></tr>
<tr><td>GRB 090510</td><td>Fermi-LAT</td><td>[[s2_z]]</td><td>[[s2_pub]]</td><td>[[s2_com]]</td><td>[[s2_b]]</td></tr>
<tr><td>Mrk 501</td><td>H.E.S.S.</td><td>[[s3_z]]</td><td>[[s3_pub]]</td><td>[[s3_com]]</td><td>[[s3_b]]</td></tr>
<tr><td>Mrk 421</td><td>MAGIC</td><td>[[s4_z]]</td><td>[[s4_pub]]</td><td>[[s4_com]]</td><td>[[s4_b]]</td></tr>
<tr><td>PKS 2155-304</td><td>H.E.S.S.</td><td>[[s5_z]]</td><td>[[s5_pub]]</td><td>[[s5_com]]</td><td>[[s5_b]]</td></tr>
<tr><td>PG 1553+113</td><td>H.E.S.S.</td><td>[[s6_z]]</td><td>[[s6_pub]]</td><td>[[s6_com]]</td><td>[[s6_b]]</td></tr>
<tr><td>Crabe (pulsar)</td><td>MAGIC</td><td>[[s7_z]]&nbsp;kpc</td><td>[[s7_pub]]</td><td>[[s7_com]]</td><td>[[s7_b]]</td></tr>
</tbody>
</table></div>

<h3>3. La pire orientation</h3>
<p>Pour une orientation \(R\) du réseau, les sources bornent ensemble</p>
$$a\le A(R)=\min_i\frac{B_i}{\sqrt{Q_{\mathrm{eff}}(R\mathbf n_i)}},$$
<p>une source sur une diagonale à \(\sigma=1\) ne bornant rien. On cherche \(\max_R A(R)\)&nbsp;: [[n_orient]] rotations tirées uniformément, des orientations construites (chaque source posée sur une diagonale puis tournée autour d’elle), puis un raffinement local. Une seconde graine indépendante retrouve le même maximum à [[ecart_graines]] près. L’optimiseur est validé sur des cas connus&nbsp;: une source seule ne borne rien à \(\sigma=1\), et deux sources séparées de l’angle entre deux diagonales peuvent être placées ensemble sur des diagonales.</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>Pire orientation (m)</th><th>95&nbsp;% des orientations (m)</th></tr></thead>
<tbody>
<tr><td>0</td><td>[[pire0]]</td><td>[[q95_0]]</td></tr>
<tr><td>0,5</td><td>[[pire05]]</td><td>[[q95_05]]</td></tr>
<tr><td>0,9</td><td>[[pire09]]</td><td>[[q95_09]]</td></tr>
<tr><td>1</td><td>[[pire1]]</td><td>[[q95_1]]</td></tr>
</tbody>
</table></div>
<p>Pour \(\sigma<1\), rien ne change par rapport au test n°&nbsp;1&nbsp;: GRB&nbsp;221009A domine, les autres sources étant de [[x_min]] à [[x_max]] fois moins sensibles. Tout se joue à \(\sigma=1\)&nbsp;: poser GRB&nbsp;221009A sur une diagonale ne suffit plus, car les autres sources voient alors la grille de biais. Le pire compromis écarte GRB&nbsp;221009A de [[ang_grb]]° de la diagonale la plus proche (\(Q_{\mathrm{eff}}\)&nbsp;=&nbsp;[[qeff_grb]]) et équilibre [[n_actives]] contraintes&nbsp;: GRB&nbsp;221009A, GRB&nbsp;090510 et le Crabe. La borne vaut alors [[pire1]]&nbsp;m, soit une échelle \(\hbar c/a\ge\)&nbsp;[[echelle]]&nbsp;GeV. Comme \(A(R)\) croît avec \(\sigma\) pour toute orientation, elle vaut pour tout \(\sigma\le1\). À \(\sigma=1\), la médiane des orientations donne [[med1]]&nbsp;m.</p>
<p>La fermeture n’allait pas de soi&nbsp;: GRB&nbsp;190114C et GRB&nbsp;090510 sont séparés de [[ang_190_090]]°, presque l’angle entre deux diagonales ([[ang_diag]]°), et GRB&nbsp;090510 et PKS&nbsp;2155-304 ne sont qu’à [[ang_090_pks]]° l’un de l’autre. C’est la diversité du reste du ciel qui ferme l’angle mort.</p>

<h3>4. Robustesse</h3>
<p>Pire orientation à \(\sigma=1\), selon les choix&nbsp;:</p>
<ul>
<li>sans GRB&nbsp;221009A&nbsp;: [[v_sans_lhaaso]]&nbsp;m, l’angle mort reste fermé&nbsp;;</li>
<li>limites publiées sans conversion de cosmologie&nbsp;: [[v_sans_cosmo]]&nbsp;m&nbsp;;</li>
<li>Fermi avec effets propres à la source (tableau V de l’article)&nbsp;: [[v_fermi]]&nbsp;m&nbsp;;</li>
<li>sursauts gamma seuls&nbsp;: [[v_sursauts]]&nbsp;m&nbsp;;</li>
<li>blazars et pulsar seuls&nbsp;: [[v_blazars]]&nbsp;m.</li>
</ul>

<h3>5. Comparaisons</h3>
<p>La borne valable pour toute orientation et tout pas de temps est [[x_test1]] fois moins forte que celle du test n°&nbsp;1 en temps continu. Beane, Davoudi et Savage obtenaient \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m à partir de la coupure du spectre des rayons cosmiques&nbsp;; notre borne en temps continu vaut [[x_beane0]] fois la leur, et notre borne universelle [[x_beane]] fois.</p>

<h3>6. Limites</h3>
<ul>
<li>La borne combinée prend, pour chaque orientation, la plus contraignante de limites publiées à 95&nbsp;% une à une&nbsp;: ce n’est pas une vraisemblance combinée, que les articles ne publient pas. Trois limites étant actives à la pire orientation, la couverture garantie est d’au moins [[couverture]]&nbsp;%, pas 95&nbsp;%.</li>
<li>Chaque article suppose qu’aucun décalage propre à la source ne compense ou n’imite le retard.</li>
<li>Les redshifts de Mrk&nbsp;421 et de PG&nbsp;1553+113 sont incertains&nbsp;; ces deux sources ne sont pas actives à la pire orientation. La distance du Crabe, active, est incluse dans les incertitudes de MAGIC.</li>
<li>Un schéma d’ordre supérieur (erreur en \(a^{4}\)), des termes compensateurs, une grille non cubique ou étirée par l’expansion échappent à cette borne.</li>
<li>Analyse secondaire&nbsp;: aucun photon n’est réanalysé. Les fractions d’orientations sont géométriques, pas des probabilités sur l’Univers.</li>
</ul>

<h3>7. Reproduire</h3>
<p>Le script refait tout en quelques secondes et vérifie d’abord ses formules et chaque conversion publiée. Chaque chiffre d’entrée est cité, page et tableau, dans <code>sources.md</code>.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-3/analyse.py" download>analyse.py</a>&nbsp;: le script</li>
<li><a href="/fichiers/test-3/resultats.json" download>resultats.json</a>&nbsp;: toutes les valeurs calculées</li>
<li><a href="/fichiers/test-3/sources.md" download>sources.md</a>&nbsp;: les citations de chaque chiffre d’entrée</li>
</ul>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>LHAASO Collaboration, GRB 221009A, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>, tableau I.</li>
<li>MAGIC Collaboration, GRB 190114C, <a href="https://arxiv.org/abs/2001.09728v4">arXiv:2001.09728v4</a>, tableau I.</li>
<li>Fermi-LAT Collaboration, GRB 090510, <a href="https://arxiv.org/abs/1305.3463v1">arXiv:1305.3463v1</a>, tableaux IV et V.</li>
<li>H.E.S.S. Collaboration, Mrk 501, <a href="https://arxiv.org/abs/1901.05209v1">arXiv:1901.05209v1</a>.</li>
<li>MAGIC Collaboration, Mrk 421, <a href="https://arxiv.org/abs/2406.07140v1">arXiv:2406.07140v1</a>, tableau 2.</li>
<li>H.E.S.S. Collaboration, PKS 2155-304, <a href="https://arxiv.org/abs/1101.3650v2">arXiv:1101.3650v2</a>.</li>
<li>H.E.S.S. Collaboration, PG 1553+113, <a href="https://arxiv.org/abs/1501.05087v1">arXiv:1501.05087v1</a>, tableau 5.</li>
<li>MAGIC Collaboration, pulsar du Crabe, <a href="https://arxiv.org/abs/1709.00346v1">arXiv:1709.00346v1</a>, tableau 6.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>.</li>
<li>Coordonnées&nbsp;: <a href="https://simbad.cds.unistra.fr/simbad/">SIMBAD</a> (CDS, Strasbourg).</li>
</ol>
""",
}

ARTICLE_4 = {
    'titre': 'Le hasard quantique trahit-il un programme ?',
    'description': 'Des millions de bits tirés d’expériences quantiques, passés au crible des tests qui démasquent '
                   'les générateurs pseudo-aléatoires qu’utiliserait une simulation.',
    'date': '28 septembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>Non.</strong> Dans les bits quantiques bruts testés, aucune signature de générateur pseudo-aléatoire n’apparaît, alors que les mêmes tests démasquent quatre générateurs simples utilisés comme témoins. Un point doit être dit d’emblée&nbsp;: la règle fixée avant l’analyse réagit sur les données IBM telles que publiées, mais la cause est identifiée — une des neuf machines est restée bloquée à 0 ou à 1 pendant des séries entières — et ce défaut n’a pas la structure d’un générateur. L’écarter a été décidé après avoir vu les données&nbsp;; nous le signalons comme tel.</p>
<p>Ce «&nbsp;non&nbsp;» a une portée limitée&nbsp;: il exclut une simulation qui tirerait ses mesures quantiques d’un générateur simple, pas une simulation qui utiliserait un générateur de qualité cryptographique, indiscernable par principe.</p>
</section>

<h2 id="explication">Explication</h2>
<p>Si le monde était une simulation, il faudrait produire le résultat de chaque mesure quantique, 0 ou 1. La physique dit que ce résultat est imprévisible par nature. Un ordinateur, lui, ne sait pas faire de vrai hasard&nbsp;: il le fabrique avec une recette de calcul. Une simulation économe utiliserait une recette rapide et simple, et les recettes simples laissent des empreintes&nbsp;: des répétitions, des régularités cachées, une structure que l’on peut retrouver par le calcul.</p>
<p>Nous avons donc pris des suites de 0 et de 1 produites par de vraies expériences quantiques et publiées par leurs auteurs, et nous y avons cherché ces empreintes. Première difficulté&nbsp;: la plupart des sources publiques de hasard quantique passent leurs résultats dans un «&nbsp;mixeur&nbsp;» mathématique avant de les publier. Ce mixeur est conçu pour effacer toute structure&nbsp;; tester sa sortie ne dit rien de la source. Nous avons testé ces données quand même, mais elles ne comptent pas dans le verdict.</p>
<p>Il reste deux sources brutes&nbsp;: un appareil à photons intriqués de l’université de Portland (Oregon), qui publie ses bits tels quels, et neuf ordinateurs quantiques d’IBM à qui l’on a demandé des millions de fois de tirer à pile ou face avec un seul qubit. Les photons passent tous les tests. Les machines d’IBM donnent un peu trop de 0, un défaut connu et expliqué par leurs auteurs&nbsp;; une fois ce déséquilibre corrigé, elles passent. L’une d’elles, Belem, est restée bloquée pendant des séries entières de mesures&nbsp;: une panne, pas une recette de calcul.</p>
<p>Les témoins se comportent comme prévu&nbsp;: les recettes simples sont démasquées, y compris un générateur très répandu qui passe pourtant la batterie officielle du NIST&nbsp;; les recettes sophistiquées ne le sont pas, pas plus que les chiffres de la racine carrée de 2, pourtant parfaitement calculables. C’est la limite de ce test&nbsp;: une simulation soignée ne laisserait aucune trace de ce genre.</p>

<h2 id="analyse">Analyse détaillée</h2>

<h3>1. Ce qui est testable</h3>
<p>Un test statistique ne renseigne que sur le dernier traitement subi par une suite de bits&nbsp;: une sortie hachée par une fonction cryptographique ressemble au hasard parfait quelle que soit l’entrée. Nous avons testé [[bits_total]] bits, dont [[bits_bruts]] bruts&nbsp;:</p>
<div class="tableau"><table>
<thead><tr><th>Jeu</th><th>Origine</th><th>Traitement</th><th>Bits</th></tr></thead>
<tbody>
<tr><td>parity</td><td>photons intriqués en polarisation (Kavulich et al., 2021)</td><td>aucun</td><td>[[n_parity]]</td></tr>
<tr><td>ibm</td><td>un qubit, porte de Hadamard, mesure&nbsp;; neuf machines (Root et Becker, 2024)</td><td>aucun</td><td>[[n_ibm]]</td></tr>
<tr><td>anu</td><td>fluctuations du vide, ANU</td><td>AES-128</td><td>[[n_anu]]</td></tr>
<tr><td>beacon</td><td>NIST Beacon 2.0</td><td>SHA-512</td><td>[[n_beacon]]</td></tr>
</tbody>
</table></div>
<p>Seuls parity et ibm renseignent sur la nature du hasard quantique. Les données brutes du test de Bell sans échappatoire du NIST (2015) n’ont pas été retenues&nbsp;: leurs choix de mesure combinent sources physiques et source pseudo-aléatoire, et leurs résultats de détection ne sont pas des bits uniformes. Pour le Beacon, la chaîne d’engagements publiée a été vérifiée sur [[engagements]] couples consécutifs.</p>

<h3>2. Niveau 1&nbsp;: la batterie NIST SP 800-22</h3>
<p>Les 15 tests de la batterie officielle sont réimplémentés et reproduisent les [[annexe_n]] p-valeurs de l’annexe B du document à [[annexe_ecart]] près ([[annexe_ecart_chev]] pour un test). Les données sont coupées en [[n_seq]] séquences de 10<sup>6</sup> bits&nbsp;; les [[np1]] p-valeurs forment une seule famille corrigée par la méthode de Holm au risque global de 1&nbsp;%.</p>
<ul>
<li>parity&nbsp;: [[par_np1]] p-valeurs, aucun rejet (plus petite p-valeur ajustée&nbsp;: [[par_p1]])&nbsp;; proportion de bits à 1&nbsp;: [[par_frac]].</li>
<li>anu et beacon&nbsp;: aucun rejet (plus petite p-valeur ajustée pour anu&nbsp;: [[anu_p1]]).</li>
<li>ibm&nbsp;: [[ibm_rej1]] rejets sur [[ibm_np1]]&nbsp;; proportion de bits à 1&nbsp;: [[ibm_frac]], soit un écart de [[ibm_z]] écarts-types. Sans la machine Belem, l’extracteur de von Neumann, qui supprime exactement un biais constant, laisse [[vn_bits]] bits et aucun rejet sur [[vn_np]] p-valeurs ([[vn_p]])&nbsp;: les échecs viennent du biais décrit par les auteurs.</li>
</ul>

<h3>3. Niveau 2&nbsp;: les signatures d’un générateur</h3>
<p>La batterie NIST dit si une suite s’écarte du hasard idéal, pas pourquoi. Trois tests visent les défauts propres aux générateurs algorithmiques&nbsp;:</p>
<ul>
<li><strong>Complexité linéaire.</strong> L’algorithme de Berlekamp-Massey donne la longueur \(L\) du plus court registre à décalage linéaire qui reproduit un segment de \(n\) bits. Pour une suite aléatoire, \(L\simeq n/2\)&nbsp;; tout générateur linéaire sur \(\mathrm{GF}(2)\) dont l’état compte moins de \(n/2\) bits donne \(L\lt n/2\). Segments de [[seg_bm]] bits, lus en continu ou un bit sur 48 et sur 64&nbsp;: un état jusqu’à [[etat_max]] bits est couvert.</li>
<li><strong>Répétitions.</strong> Chaque fenêtre de 64 bits est comparée à toutes les autres&nbsp;; le nombre attendu de paires identiques est de l’ordre de [[rep_attendu]]. Une seule répétition signalerait une période ou une graine réutilisée.</li>
<li><strong>Corrélations à longue portée.</strong> Autocorrélation aux décalages 17 à [[lag_max]], avec correction de Bonferroni.</li>
</ul>
<p>Famille principale, Holm à 1&nbsp;% sur [[np2]] p-valeurs&nbsp;: parity ne rejette rien ([[par_p2]])&nbsp;; son écart maximal de \(L\) à \(n/2\) est de [[par_ecart_l]]&nbsp;; aucune répétition&nbsp;; corrélations à longue portée&nbsp;: [[par_auto]]. anu et beacon ne rejettent rien. ibm rejette [[ibm_rej2]] fois.</p>

<h3>4. Les rejets d’IBM&nbsp;: une machine bloquée</h3>
<p>Les données IBM sont faites de [[ibm_essais]] essais de 8&nbsp;192 tirs. [[ibm_const]] d’entre eux sont constants ([[ibm_const0]] entièrement à 0, [[ibm_const1]] entièrement à 1) et [[ibm_quasi]] autres le sont à plus de 99&nbsp;%&nbsp;; tous viennent de la machine Belem. Les [[ibm_paires]] paires de fenêtres identiques sont toutes des suites de bits égaux&nbsp;: parmi les fenêtres de composition ordinaire, il y en a [[ibm_paires_typ]]. Une sortie figée n’est pas une sortie de générateur pseudo-aléatoire&nbsp;: c’est l’absence de sortie.</p>
<p>Écarter Belem a été décidé après avoir vu les données&nbsp;: c’est donc une analyse secondaire, avec sa propre correction de Holm, et le résultat de la règle initiale reste publié. Sur les huit autres machines ([[sb_bits]] bits), le niveau 2 ne rejette rien ([[sb_np2]] p-valeurs, plus petite p-valeur ajustée [[sb_p2]])&nbsp;; l’écart maximal de \(L\) à \(n/2\) est de [[sb_ecart_l]] et il n’y a aucune répétition. Une corrélation au décalage 1 existe ([[sb_r1]], soit [[sb_z1]] écarts-types)&nbsp;: un défaut de mesure à courte portée, sans rapport avec la structure d’un générateur. Le niveau 1 y rejette [[sb_rej1]] fois sur [[sb_np1]], à cause du biais.</p>

<h3>5. Les témoins</h3>
<p>La même chaîne est appliquée à [[bits_ctrl]] bits de chaque générateur connu&nbsp;; le script s’arrête si un témoin ne se comporte pas comme prévu.</p>
<div class="tableau"><table>
<thead><tr><th>Générateur</th><th>Attendu</th><th>Résultat (plus petites p-valeurs ajustées, niveaux 1 et 2)</th></tr></thead>
<tbody>
<tr><td>LFSR de degré 20</td><td>détecté</td><td>détecté&nbsp;: \(L\)&nbsp;=&nbsp;[[l20_lmin]], répétitions</td></tr>
<tr><td>LFSR de degré 31</td><td>détecté</td><td>détecté&nbsp;: \(L\)&nbsp;=&nbsp;[[l31_lmin]], \(\log_{10}p\)&nbsp;=&nbsp;[[l31_log10p]]</td></tr>
<tr><td>LCG 32 bits</td><td>détecté</td><td>détecté&nbsp;: test spectral, corrélations à longue portée</td></tr>
<tr><td>Mersenne Twister</td><td>détecté</td><td>détecté par le niveau 2 seul&nbsp;: \(L\)&nbsp;=&nbsp;[[mt_lmin]], \(\log_{10}p\)&nbsp;=&nbsp;[[mt_log10p]]&nbsp;; batterie NIST muette ([[mt_p1]])</td></tr>
<tr><td>PCG64</td><td>non détecté</td><td>rien ([[pcg_p1]]&nbsp;; [[pcg_p2]])</td></tr>
<tr><td>SHA-256 en mode compteur</td><td>non détecté</td><td>rien ([[sha_p1]]&nbsp;; [[sha_p2]])</td></tr>
<tr><td>Décimales binaires de \(\sqrt{2}\)</td><td>non détecté</td><td>rien ([[r2_p1]]&nbsp;; [[r2_p2]])</td></tr>
</tbody>
</table></div>
<p>Le Mersenne Twister montre que le niveau 2 ajoute une vraie sensibilité à la batterie officielle. PCG64, SHA-256 et \(\sqrt{2}\) montrent qu’une suite entièrement déterministe peut n’avoir aucune signature détectable.</p>

<h3>6. Limites</h3>
<ul>
<li>Un générateur de qualité cryptographique est indiscernable&nbsp;: ce test exclut une simulation qui utiliserait un générateur simple, pas une simulation soignée. Le document SP 800-22 le dit lui-même&nbsp;: aucun ensemble de tests ne remplace la cryptanalyse.</li>
<li>Couverture du niveau 2&nbsp;: un générateur linéaire n’est détecté que si son état compte moins de [[etat_max]] bits&nbsp;; une répétition, que si la période est plus courte que les données.</li>
<li>Volume brut modeste, et aucune des deux sources brutes n’est certifiée par un test de Bell sans échappatoire.</li>
<li>L’exclusion de la machine Belem est une décision a posteriori&nbsp;; sa cause est documentée et le résultat brut publié.</li>
<li>Les jeux ANU et Beacon ne mesurent que la qualité de l’AES-128 et du SHA-512.</li>
</ul>

<h3>7. Reproduire</h3>
<p>Les données sont refaites par <code>telecharger.py</code>, qui vérifie leurs empreintes&nbsp;; <code>analyse.py</code> tourne ensuite sans réseau en moins de deux minutes, autotests compris.</p>
<pre><code>python3 telecharger.py
python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-4/analyse.py" download>analyse.py</a>&nbsp;: l’analyse</li>
<li><a href="/fichiers/test-4/telecharger.py" download>telecharger.py</a>&nbsp;: le téléchargement vérifié des données</li>
<li><a href="/fichiers/test-4/resultats.json" download>resultats.json</a>&nbsp;: toutes les valeurs calculées</li>
<li><a href="/fichiers/test-4/sources.md" download>sources.md</a>&nbsp;: les citations de chaque affirmation</li>
</ul>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>J. T. Kavulich, B. P. Van Deren, M. Schlosshauer, <cite>Searching for evidence of algorithmic randomness and incomputability in the output of quantum random number generators</cite>, Physics Letters A 388, 127032 (2021), <a href="https://arxiv.org/abs/2101.01238">arXiv:2101.01238</a>&nbsp;; données&nbsp;: <a href="https://zenodo.org/records/4440318">Zenodo 4440318</a>.</li>
<li>B. P. Van Deren, J. T. Kavulich, M. Schlosshauer, <cite>Parity-based, bias-free optical quantum random number generation with min-entropy estimation</cite>, <a href="https://arxiv.org/abs/2006.11425">arXiv:2006.11425</a>.</li>
<li>O. Root, M. Becker, <cite>Does True Randomness Exist? Efficacy Testing IBM Quantum Computers via Statistical Randomness</cite>, <a href="https://arxiv.org/abs/2401.12250">arXiv:2401.12250</a>&nbsp;; données&nbsp;: <a href="https://doi.org/10.5281/zenodo.10542216">DOI 10.5281/zenodo.10542216</a>.</li>
<li>J. Y. Haw et al., <cite>Maximization of Extractable Randomness in a Quantum Random-Number Generator</cite>, <a href="https://arxiv.org/abs/1411.4512">arXiv:1411.4512</a>.</li>
<li>NIST, <cite>A Reference for Randomness Beacons: Format and Protocol Version 2</cite>, <a href="https://csrc.nist.gov/pubs/ir/8213/ipd">NISTIR 8213</a>.</li>
<li>L. K. Shalm et al., <cite>A strong loophole-free test of local realism</cite>, <a href="https://arxiv.org/abs/1511.03189">arXiv:1511.03189</a>.</li>
<li>NIST, <cite>A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications</cite>, <a href="https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final">SP 800-22 Rev. 1a</a>.</li>
</ol>
""",
}

# Synthèse centrale. Liens vers les tests relatifs à la langue (../test-1/) : identiques dans
# toutes les langues. Les nombres cités de la littérature sans marqueur s’adaptent à la langue.
SYNTHESE = {
    'titre': 'Avons-nous de meilleures raisons de nous croire simulés ?',
    'description': 'Perception, conscience, faisabilité, argument de Bostrom, physique, métaphysique ; '
                   'ce que valent, une fois vérifiées à la source, les raisons de penser que notre monde '
                   'est produit par un autre système.',
    'date': '28 septembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>Non.</strong> En l’état, nous n’avons pas de meilleures raisons de penser que notre monde et nos expériences sont produits par un autre système que de penser le contraire. La simulation n’est pas une explication étayée de notre situation&nbsp;: aucune observation ne la favorise, et le seul argument qui lui donne du poids, celui de Nick Bostrom, conclut à une alternative dont l’issue dépend de grandeurs que personne ne connaît. Bostrom l’écrit lui-même&nbsp;: son argument «&nbsp;ne cherche pas à établir que nous vivons probablement dans une simulation&nbsp;».</p>
<p>Ce «&nbsp;non&nbsp;» ne démontre pas le contraire. Nos quatre tests, comme ceux de la littérature, excluent des architectures précises, par exemple une grille cubique naïve de maille égale ou supérieure à [[t3_maille]]&nbsp;m, ou un hasard quantique tiré d’un générateur pseudo-aléatoire simple&nbsp;; aucun ne peut exclure une simulation conçue pour ne laisser aucune trace, et les «&nbsp;preuves&nbsp;» d’impossibilité publiées reposent sur des prémisses qui ne sont pas établies. Deux choses changeraient la réponse&nbsp;: une anomalie physique reproductible dont aucune autre explication ne rende compte, ou le jour où nous saurions nous-mêmes créer des êtres simulés conscients.</p>
</section>

<h2 id="explication">Explication</h2>
<p>Dire que nous vivons «&nbsp;dans une simulation&nbsp;» peut vouloir dire trois choses. Soit nos esprits sont ailleurs et reçoivent les images d’un monde artificiel, comme dans le film <cite>Matrix</cite>. Soit nous sommes nous-mêmes des personnages calculés par un ordinateur, en même temps que le monde qui nous entoure. Soit, enfin, les lois de la nature fonctionnent comme un programme, sans que personne ne l’ait écrit. Seules les deux premières répondent vraiment à la question posée, car seules elles supposent un autre système qui nous produit. Et même dans ces cas, notre monde ne deviendrait pas irréel&nbsp;: les tables, les personnes et leurs souffrances resteraient ce qu’elles sont. Ce qui changerait, c’est ce qui les fait exister.</p>
<p>Le premier argument est le plus intuitif&nbsp;: nos rêves paraissent réels, donc une vie entière pourrait être une illusion bien faite. C’est vrai, et cela suffit à montrer qu’on ne peut pas écarter l’idée d’un revers de main. Mais cela ne donne aucune raison de la croire. Si un monde simulé et un monde qui ne l’est pas nous paraissent exactement pareils, ce que nous percevons ne favorise ni l’un ni l’autre.</p>
<p>Deuxième point&nbsp;: pour que nous soyons des personnages calculés, il faudrait qu’un calcul puisse ressentir quelque chose. Des philosophes le pensent, avec de bons arguments&nbsp;; d’autres le contestent, avec de bons arguments aussi. La question n’est pas tranchée, et aucune expérience ne sait aujourd’hui la trancher.</p>
<p>Troisième point&nbsp;: pourrait-on seulement fabriquer un tel monde&nbsp;? Calculer tout l’Univers dans ses moindres détails est hors de portée de toute machine soumise à nos lois physiques&nbsp;: il y faudrait bien plus d’énergie que l’Univers n’en contient. Les partisans de l’idée répondent qu’il suffirait de calculer ce que les habitants voient, au moment où ils le regardent. C’est concevable, mais une telle simulation est faite pour ne laisser aucune trace. Elle échappe alors aux mesures, et les mesures ne peuvent plus rien dire en sa faveur.</p>
<p>Le raisonnement qui a rendu l’idée célèbre, celui du philosophe Nick Bostrom en 2003, est plus subtil. Si des civilisations avancées fabriquaient beaucoup de mondes simulés peuplés d’êtres conscients, les êtres simulés seraient bien plus nombreux que les autres, et nous serions probablement parmi eux. Mais le raisonnement contient un «&nbsp;si&nbsp;». Il ne dit pas si de telles civilisations existent, ni si elles le voudraient. Bostrom conclut seulement que l’une de trois possibilités est vraie&nbsp;: presque aucune civilisation n’atteint ce stade, ou presque aucune ne simule ses ancêtres, ou nous sommes presque sûrement simulés. Il ne dit pas laquelle. Nos calculs montrent que la réponse chiffrée dépend entièrement de ce qu’on suppose sur ces inconnues&nbsp;: selon des choix qui paraissent tous raisonnables, on obtient presque une certitude ([[conf_genereux]]), environ une chance sur [[un_sur_ignorance]] ([[conf_ignorance]]) ou environ [[pct_observateurs]] chances sur cent ([[conf_observateurs]]). Un astronome qui avait trouvé «&nbsp;un peu moins d’une chance sur deux&nbsp;» avait en réalité retrouvé le pari à égalité qu’il avait posé au départ.</p>
<p>Quatrième point&nbsp;: la physique a-t-elle trouvé un indice&nbsp;? Non. Les étrangetés de la physique quantique, souvent citées, s’expliquent sans ordinateur caché&nbsp;: elles ne dépendent pas de la présence d’un observateur conscient et ne réécrivent pas le passé. Le fait que les lois de la nature semblent réglées pour permettre la vie ne distingue pas un monde simulé d’un monde qui ne l’est pas. Les tests qui cherchent la trace d’un quadrillage de l’espace, dont trois des nôtres, n’ont rien trouvé&nbsp;: ils excluent un quadrillage grossier, pas une simulation en général. Notre quatrième test a cherché, dans les résultats de vraies mesures quantiques, les empreintes que laisserait un hasard fabriqué par une recette de calcul simple&nbsp;: il n’en a trouvé aucune, mais une recette soignée n’en laisserait pas.</p>
<p>Au bout du compte, aucune observation ne penche pour la simulation, et l’argument qui la soutient dépend de paris invérifiables. Nous n’avons donc pas de meilleures raisons de nous croire simulés que de penser le contraire. Cela ne prouve pas que nous ne le sommes pas&nbsp;: une simulation parfaite serait, par définition, indiscernable. La réponse changerait si l’on découvrait une anomalie physique qu’aucune autre explication ne rende, ou si nous savions un jour créer nous-mêmes des êtres simulés conscients.</p>

<h2 id="analyse">Analyse détaillée</h2>

<h3>1. De quelle simulation parle-t-on&nbsp;?</h3>
<p>Chalmers (<cite>The Matrix as Metaphysics</cite>, 2005) ramène l’hypothèse de <cite>Matrix</cite> à la conjonction de trois thèses distinctes, complétée par l’idée que le calcul a été conçu comme la simulation d’un monde. L’hypothèse computationnelle&nbsp;: «&nbsp;les processus microphysiques, partout dans l’espace-temps, sont constitués par des processus computationnels sous-jacents&nbsp;». L’hypothèse de création&nbsp;: «&nbsp;l’espace-temps physique et son contenu ont été créés par des êtres extérieurs à l’espace-temps physique&nbsp;». L’hypothèse corps-esprit&nbsp;: «&nbsp;mon esprit est constitué par des processus extérieurs à l’espace-temps physique et reçoit ses entrées perceptives de processus situés dans l’espace-temps physique&nbsp;». Ces trois briques séparent les trois sens du mot.</p>
<ul>
<li><strong>(a) Un environnement artificiel perçu par une conscience extérieure</strong>&nbsp;: création, calcul et esprit extérieur. C’est <cite>Matrix</cite>, ou le cerveau dans une cuve. La conscience n’y est pas simulée&nbsp;; elle est ailleurs. Chalmers juge l’hypothèse corps-esprit cohérente, «&nbsp;même si la science contemporaine tend à suggérer qu’elle est fausse&nbsp;».</li>
<li><strong>(b) Un monde calculé qui contient ses propres êtres conscients</strong>&nbsp;: création et calcul, les esprits étant eux-mêmes calculés. C’est le cas de Bostrom (2003), qui pose la prémisse d’indépendance du substrat&nbsp;: «&nbsp;pourvu qu’un système implémente le bon type de structures et de processus computationnels, il peut être associé à des expériences conscientes&nbsp;». Il la prend «&nbsp;comme donnée&nbsp;», en reconnaissant qu’elle «&nbsp;n’est pas entièrement incontestée&nbsp;».</li>
<li><strong>(c) Un univers dont les lois sont computationnelles, sans concepteur</strong>&nbsp;: le calcul seul. Chalmers cite Fredkin et Wolfram&nbsp;; Lloyd (2002) en donne une version chiffrée («&nbsp;si l’on choisit de regarder l’Univers comme effectuant un calcul&nbsp;», ce calcul compte environ [[lloyd_univers_ops]] opérations élémentaires sur [[lloyd_univers_bits]] bits)&nbsp;; ’t&nbsp;Hooft (2016) défend l’idée qu’un système classique, de type automate cellulaire, pourrait se cacher sous la mécanique quantique.</li>
</ul>
<p>La question posée, «&nbsp;notre monde et nos expériences sont-ils produits par un autre système&nbsp;?&nbsp;», porte sur (a) et (b). Dans (c), rien d’extérieur ne produit le monde&nbsp;: le calcul est la physique elle-même, et (c) peut être vraie sans que la réponse soit oui. Une grille détectée ne départagerait d’ailleurs pas (b) de (c)&nbsp;: une physique fondamentalement discrète produirait le même signal (<a href="../test-1/#limites">test n°&nbsp;1, section&nbsp;7</a>).</p>
<p>Deuxième précision&nbsp;: même vraie, (a) ou (b) ne rendrait pas le monde irréel. Selon Chalmers, l’hypothèse de <cite>Matrix</cite> «&nbsp;n’est pas une hypothèse sceptique&nbsp;»&nbsp;: «&nbsp;même si je suis dans une matrice, mon monde est parfaitement réel&nbsp;»&nbsp;; si l’hypothèse computationnelle est vraie, «&nbsp;il y a toujours des électrons et des protons&nbsp;», faits de quelque chose de plus fondamental, comme les molécules sont faites d’atomes. <cite>Reality+</cite> (2022) généralise&nbsp;: «&nbsp;la réalité virtuelle est une réalité authentique&nbsp;». Bostrom va dans le même sens&nbsp;: «&nbsp;on ne gagne aucune clarté à affirmer que le monde n’est pas “vraiment réel” si nous sommes dans une simulation&nbsp;»&nbsp;; il ne serait qu’une partie de la réalité. La question ne porte donc pas sur l’existence des choses mais sur leur constitution et leur origine causale. Elle peut recevoir deux sortes de raisons&nbsp;: des arguments a priori, qui portent sur le nombre d’observateurs simulés (section&nbsp;5), et des traces observables (section&nbsp;6). Les deux supposent d’abord qu’on sache ce que vaut la perception (section&nbsp;2), qu’un calcul puisse être conscient (section&nbsp;3) et qu’un tel monde puisse être construit (section&nbsp;4).</p>

<h3>2. L’argument par la perception</h3>
<p>Il enchaîne trois propositions qu’il faut séparer.</p>
<p><strong>(P1) Une expérience peut paraître réelle sans être véridique.</strong> C’est établi&nbsp;: le rêve et l’illusion en sont des exemples quotidiens. Bostrom le rappelle&nbsp;: nos cerveaux, sans aide technique, nous empêchent «&nbsp;d’ordinaire&nbsp;» de remarquer que nous rêvons, alors que le rêve typique «&nbsp;fourmille des anomalies les plus fantastiques&nbsp;».</p>
<p><strong>(P2) Une expérience équivalente à la nôtre pourrait être produite artificiellement.</strong> «&nbsp;Équivalente&nbsp;» veut dire&nbsp;: aussi riche, cohérente sur toute une vie, partagée par des milliards de personnes qui se la confirment les unes aux autres, et compatible avec toutes les mesures accumulées par les sciences. (P1) n’en fournit qu’un cas très partiel, puisque le rêve est bref, privé et incohérent. (P2) est une conjecture, qui dépend de la faisabilité (section&nbsp;4) et, pour la version (b), de la conscience des êtres calculés (section&nbsp;3).</p>
<p><strong>(P3) La nôtre l’est.</strong> (P3) ne suit pas de (P2)&nbsp;: qu’une chose soit possible ne dit pas qu’elle est le cas.</p>
<p>En probabilités, notons \(S\) l’hypothèse d’une simulation et \(\neg S\) sa négation. Si une version simulée reproduit exactement notre expérience \(E\), alors \(P(E\mid S)=P(E\mid\neg S)\), et le rapport de vraisemblance vaut 1. L’expérience ne déplace pas la balance, ni dans un sens ni dans l’autre. L’argument par la perception est un argument sceptique, qui interdit la certitude, et non un indice. Sa place légitime est de bloquer le rejet d’office&nbsp;: on ne peut pas écarter l’hypothèse en invoquant la vivacité de nos perceptions. Sa limite est sa symétrie&nbsp;: il soutiendrait aussi bien n’importe quelle hypothèse indécelable, le malin génie de Descartes ou le «&nbsp;cerveau de Boltzmann&nbsp;», rapprochement que fait Vazza (2025). Il ne distingue donc pas la simulation parmi les scénarios sceptiques, et s’il existe de meilleures raisons de la croire, elles doivent venir d’ailleurs.</p>

<h3>3. Un calcul peut-il être conscient&nbsp;?</h3>
<p>Pour la version (b), c’est la prémisse décisive. L’argument «&nbsp;peut-être le plus fort&nbsp;» en sa faveur, selon son critique le plus récent lui-même, est celui de Chalmers (1995&nbsp;; <cite>The Conscious Mind</cite>, 1996, chapitre&nbsp;7). Le principe d’invariance organisationnelle affirme qu’«&nbsp;étant donné un système qui a des expériences conscientes, tout système qui a la même organisation fonctionnelle, à un grain suffisamment fin, aura des expériences conscientes qualitativement identiques&nbsp;». L’argument des qualia évanescents le soutient&nbsp;: on remplace un à un les neurones d’un cerveau par des puces qui ont exactement la même fonction entrée-sortie&nbsp;; le comportement et les jugements restent identiques à chaque étape. Si l’expérience s’éteignait graduellement, un être parfaitement rationnel se tromperait massivement sur sa propre expérience, ou ses croyances flotteraient au-dessus de ses états physiques selon des règles arbitraires. Chalmers juge ces deux options bien moins plausibles que la conservation de l’expérience. C’est un argument de plausibilité, non une démonstration&nbsp;: les qualia évanescents sont «&nbsp;peut-être logiquement possibles&nbsp;», écrit-il&nbsp;; il les tient pour empiriquement invraisemblables.</p>
<p>Contre, Searle (1980) et la chambre chinoise&nbsp;: «&nbsp;instancier un programme d’ordinateur n’est jamais, par soi-même, une condition suffisante de l’intentionnalité&nbsp;»&nbsp;; un homme peut exécuter le programme sans rien comprendre, et seule une machine dotée de pouvoirs causaux équivalents à ceux du cerveau pourrait penser. Chalmers relève que Searle admet d’ailleurs la possibilité des qualia évanescents.</p>
<p>L’objection la plus récente est celle de Mogensen (<cite>Synthese</cite>, en ligne le 5&nbsp;novembre 2025). Il montre comment résister à l’argument des qualia évanescents en admettant deux hypothèses&nbsp;: la conscience a des frontières vagues, et l’activité neuronale consciente a une structure holistique. Il juge ces hypothèses «&nbsp;plausibles&nbsp;», quoique «&nbsp;évidemment controversées&nbsp;», et estime avoir mis au jour «&nbsp;d’importantes faiblesses&nbsp;» de l’argument.</p>
<p>La conscience d’un être calculé n’est donc ni démontrée ni réfutée, et aucune expérience ne sait aujourd’hui la tester. Dans la suite, sa probabilité est un paramètre libre, noté \(c\). Il pèse directement. Si les êtres calculés ne sont pas conscients, aucun être conscient n’est simulé, et comme nous nous savons conscients, nous ne le serions pas&nbsp;: la confiance d’être simulé est au plus \(c\). La version (a) échappe à ce paramètre, mais au prix de l’hypothèse corps-esprit, que Chalmers lui-même présente comme contraire à la tendance de la science contemporaine.</p>

<h3>4. Un tel monde peut-il être construit&nbsp;?</h3>
<p>Les limites physiques du calcul sont connues. Selon Lloyd (2000), un «&nbsp;ordinateur portable ultime&nbsp;» d’un kilogramme dans un litre effectuerait au plus [[lloyd_ops_s]] opérations par seconde sur environ [[lloyd_bits]] bits. Selon Lloyd (2002), l’Univers n’a pu effectuer depuis son origine plus de [[lloyd_univers_ops]] opérations sur [[lloyd_univers_bits]] bits ([[lloyd_univers_bits_grav]] bits si l’on compte la gravitation)&nbsp;; ces nombres sont aussi, écrit-il, des bornes inférieures du nombre d’opérations et de bits nécessaires pour simuler l’Univers entier sur un ordinateur quantique.</p>
<p>À l’autre extrême, Bostrom estime le coût d’une simulation de toute l’histoire mentale de l’humanité&nbsp;: [[b_humains]] personnes × [[b_annees]] ans × [[b_secondes]] secondes par an × [[b_cerveau_min]] à [[b_cerveau_max]] opérations par seconde et par cerveau. Il imprime «&nbsp;≈&nbsp;[[b_imprime_min]] à [[b_imprime_max]] opérations&nbsp;»&nbsp;; le produit de ses propres facteurs donne [[b_produit_min]] à [[b_produit_max]], soit [[b_facteur]] fois plus. L’écart ne change rien à son argument, qui tolère selon lui plusieurs ordres de grandeur d’erreur. Le nombre de Lloyd étant une borne inférieure, l’écart entre simuler les cerveaux et simuler l’Univers est d’au moins [[decades_min]] à [[decades_max]] ordres de grandeur, selon l’estimation retenue pour les cerveaux. Tout le débat sur la faisabilité tient dans cet écart&nbsp;: que faut-il calculer&nbsp;?</p>
<p>Vazza (2025) traite trois cas, en prenant la borne holographique pour la mémoire nécessaire et le coût thermodynamique minimal de l’effacement d’un bit pour l’énergie. L’Univers observable à la résolution de Planck demanderait 3,5&#8239;×&#8239;10<sup>124</sup> bits et 8,9&#8239;×&#8239;10<sup>108</sup>&nbsp;erg, quand l’Univers observable ne contient qu’environ 2,7&#8239;×&#8239;10<sup>78</sup>&nbsp;erg. La Terre à la résolution de Planck demanderait, rien que pour initialiser le calcul, l’énergie de masse de toutes les étoiles d’un amas globulaire. La Terre à la résolution la plus grossière compatible avec les neutrinos de haute énergie qui la traversent (1,2&#8239;×&#8239;10<sup>−21</sup>&nbsp;cm) tiendrait en 1,65&#8239;×&#8239;10<sup>51</sup> bits, mais une seconde simulée demanderait, même avec un trou noir pour calculateur, 4,2&#8239;×&#8239;10<sup>13</sup>&nbsp;s de calcul&nbsp;: des durées «&nbsp;géologiques&nbsp;», selon l’auteur. Sa conclusion&nbsp;: il est «&nbsp;tout simplement impossible que cet Univers soit simulé par un univers partageant les mêmes propriétés&nbsp;»&nbsp;; seuls des univers aux propriétés physiques «&nbsp;très différentes&nbsp;» le pourraient, et savoir si des univers aux lois entièrement différentes le pourraient lui paraît «&nbsp;entièrement hors de ce qui est scientifiquement testable&nbsp;». Deux réserves figurent dans l’article même. La borne holographique est un maximum d’information, et Vazza discute (section&nbsp;4.4) le cas où l’évolution se décrirait avec moins de bits, qu’il juge peu plausible à plusieurs ordres de grandeur près. Et un scénario solipsiste, qui ne simulerait que le cerveau d’un seul observateur, «&nbsp;ne pose pas de contrainte évidente&nbsp;» au calcul.</p>
<p>La réponse est venue de deux côtés. Edge et Brown (2026), dans un commentaire publié par la même revue, notent que Vazza vise la simulation d’un monde partagé, à l’échelle d’une planète et cohérent avec les expériences, alors que Bostrom ne s’engage que sur le rendu d’une expérience subjective sans anomalie décelable. Bostrom lui-même, dans la version 2025 de sa FAQ&nbsp;: «&nbsp;les critiques qui supposent qu’une simulation devrait être entièrement complète (par exemple Vazza (2025)) manquent donc leur cible&nbsp;»&nbsp;; les détails seraient produits à la demande, et les simulateurs pourraient «&nbsp;facilement nous empêcher de le découvrir&nbsp;».</p>
<p>Le débat aboutit à un dilemme. Une simulation complète, qui calcule le monde à partir de ses lois, est exclue, sous les hypothèses de Vazza, pour un simulateur soumis à notre physique. C’est le cas des «&nbsp;simulations d’ancêtres&nbsp;» de Bostrom si leurs auteurs vivent sous la même physique que leurs ancêtres. Une simulation minimale n’est pas exclue, mais personne n’en a chiffré le coût réel. L’estimation de Bostrom ne compte que les cerveaux, pas le maintien d’un monde partagé et cohérent avec les collisionneurs, les neutrinos qui traversent la Terre, les tests de Bell ou les ordinateurs, que Bostrom admet devoir simuler «&nbsp;jusqu’au niveau des éléments logiques individuels&nbsp;». Surtout, elle est conçue pour ne laisser aucune trace&nbsp;: sa faisabilité, même accordée, ne fournit donc aucune raison de croire qu’elle existe (section&nbsp;8).</p>
<p>Deux travaux resserrent encore la prémisse technique. Bibeau-Delisle et Brassard (2021) réécrivent l’argument sous la forme d’une équation «&nbsp;à la Drake&nbsp;» et montrent que, si chaque niveau simulé consacre à son tour sa puissance de calcul à des simulations, la fraction d’êtres simulés est bornée par l’efficacité du calcul, «&nbsp;très probablement sous 50&nbsp;%&nbsp;»&nbsp;; ils rappellent que la fraction de Bostrom n’est qu’une «&nbsp;probabilité de base&nbsp;» à corriger par des facteurs «&nbsp;pratiquement impossibles à évaluer&nbsp;». Birch (2013) relève une tension logique&nbsp;: l’argument suppose que nous avons de bonnes raisons de croire ce que notre physique dit des limites du calcul, et en même temps de mauvaises raisons de croire ce qu’elle dit de notre propre constitution. Ce «&nbsp;scepticisme sélectif&nbsp;» n’étant pas justifié, il n’y a pas, conclut-il, de bonne raison de croire la conclusion.</p>
<p>À l’inverse, les «&nbsp;preuves&nbsp;» d’impossibilité ne sont pas plus solides que leurs prémisses. Celle de Vazza vaut pour un simulateur soumis à notre physique. Celle de Faizal, Krauss, Shabir et Marino (2025) s’appuie sur les théorèmes d’incomplétude pour conclure que l’hypothèse de la simulation est «&nbsp;logiquement impossible&nbsp;». Elle suppose que la réalité contient des vérités accessibles seulement par une «&nbsp;compréhension non algorithmique&nbsp;», et qu’une simulation devrait reproduire la théorie complète du monde. Or un simulateur n’a pas à démontrer les vérités de son monde, seulement à en calculer l’évolution&nbsp;; et l’indécidabilité apparaît déjà pour des programmes ordinaires, dont on ne peut pas décider en général s’ils s’arrêteront. L’argument établit au mieux qu’aucune théorie algorithmique complète ne décrit tout, pas qu’aucun calcul ne peut produire un monde tel que le nôtre.</p>
<p>La faisabilité n’apporte donc pas de raison positive&nbsp;: elle élimine la version complète sous notre physique et laisse ouverte une version minimale que rien ne peut détecter. S’il y a une raison de croire à la simulation, elle doit venir du dénombrement des observateurs.</p>

<h3>5. L’argument de Bostrom</h3>
<p>Notations de Bostrom&nbsp;: \(f_P\), fraction des civilisations de niveau humain qui atteignent un stade «&nbsp;posthumain&nbsp;»&nbsp;; \(f_I\), fraction des civilisations posthumaines intéressées par les simulations d’ancêtres&nbsp;; \(N_I\), nombre moyen de simulations d’ancêtres qu’elles exécutent. Si chaque simulation contient autant d’observateurs que l’histoire réelle qu’elle reproduit, la fraction des observateurs à expérience humaine qui sont simulés vaut (sa formule (*))</p>
$$f_{\mathrm{sim}}=\frac{f_P\,f_I\,N_I}{f_P\,f_I\,N_I+1}.$$
<p>Comme \(N_I\) peut être astronomique, au moins une de trois propositions est vraie&nbsp;: (1)&nbsp;\(f_P\approx0\), (2)&nbsp;\(f_I\approx0\), (3)&nbsp;\(f_{\mathrm{sim}}\approx1\). Un principe d’indifférence «&nbsp;faible&nbsp;» fait le reste&nbsp;: si une fraction \(x\) des observateurs comme nous sont simulés et que rien ne nous indique lesquels, notre confiance d’être simulés doit valoir \(x\) (sa formule (#)).</p>
<p><strong>Sa force.</strong> Le trilemme ne demande pas que beaucoup de civilisations simulent. Comme \(N_I\) est immense, la rareté des civilisations intéressées «&nbsp;doit être extrême en proportion&nbsp;» pour que (3) soit fausse&nbsp;: quelques producteurs suffisent. C’est ce qui rend l’argument difficile à écarter.</p>
<p><strong>Sa sensibilité.</strong> \(f_{\mathrm{sim}}\) ne dépend que du produit \(x=f_P\,f_I\,N_I\), et presque en tout ou rien&nbsp;: elle passe de 1&nbsp;% à 99&nbsp;% quand \(x\) varie de [[x_1pct]] à [[x_99pct]], soit sur [[largeur_transition]] ordres de grandeur. Hors de cette bande, elle vaut presque 0 ou presque 1. Or chacun des facteurs est inconnu sur bien plus d’ordres de grandeur que cela. Trois difficultés s’y ajoutent.</p>
<p><strong>Les populations réelles.</strong> Bostrom et Kulczycki (2011) ont signalé une faille de la formule&nbsp;: elle suppose que les civilisations qui simulent et celles qui ne simulent pas ont eu, avant le stade posthumain, la même population moyenne. Si les secondes étaient bien plus peuplées, les trois propositions pourraient être fausses ensemble. Leur réparation ajoute une hypothèse&nbsp;: l’écart de population n’est pas «&nbsp;astronomiquement grand&nbsp;», par exemple pas plus d’un facteur un million. De même, une simulation ne contient pas forcément autant d’observateurs que l’histoire réelle. Bostrom envisage des «&nbsp;simulations de moi&nbsp;», qui ne simulent pleinement qu’une personne, et calcule qu’il en faudrait environ [[b_facteur_moi]] fois plus que de simulations d’ancêtres pour qu’elles l’emportent. Nous notons \(r\) le rapport entre le nombre d’observateurs d’une simulation et la population réelle moyenne&nbsp;: \(r=1\) chez Bostrom, \(r\approx\)&nbsp;[[r_moi]] pour une simulation d’une seule personne.</p>
<p><strong>Les observateurs conscients.</strong> C’est le paramètre \(c\) de la section&nbsp;3. Avec cette extension, qui est la nôtre, \(x=f_P\,f_I\,N_I\,r\) et la confiance d’être simulé vaut \(c\,x/(1+x)\).</p>
<p><strong>La règle de sélection.</strong> Le principe (#) suppose que nous sommes un échantillon quelconque des observateurs «&nbsp;comme nous&nbsp;». Weatherson (2003) en distingue quatre lectures&nbsp;: deux sont fausses, la troisième n’entraîne pas la conclusion, et la quatrième ne l’entraîne qu’avec une hypothèse auxiliaire «&nbsp;que nous n’avons aucune raison de croire&nbsp;». Bostrom (2005) maintient le principe. Hartle et Srednicki (2007) montrent, à propos de cosmologie, que se supposer «&nbsp;typique&nbsp;» n’est pas un résultat de la physique mais un choix de probabilités a priori, qu’il faut rendre explicite.</p>
<p><strong>Ce que donnent les chiffres.</strong> Notre script tire \(f_P\), \(f_I\), \(N_I\) et \(r\) selon des lois log-uniformes (chaque ordre de grandeur également probable dans l’intervalle choisi) et calcule exactement la loi de \(x\)&nbsp;; un tirage Monte-Carlo à graine fixe la contrôle. Ces lois ne sont pas des estimations&nbsp;: elles montrent comment la réponse suit le choix.</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Hypothèses a priori</th><th>Confiance d’être simulé</th></tr></thead>
<tbody>
<tr><td>\(f_P\) et \(f_I\) entre 10<sup>−1</sup> et 1&nbsp;; \(N_I\) entre 10<sup>3</sup> et 10<sup>9</sup>&nbsp;; \(r=1\)&nbsp;; \(c=1\)</td><td>[[conf_genereux]]</td></tr>
<tr><td>idem, mais une chance sur deux que les êtres simulés soient conscients (\(c=1/2\))</td><td>[[conf_genereux_c]]</td></tr>
<tr><td>\(f_P\) et \(f_I\) inconnus sur dix ordres de grandeur chacun (entre 10<sup>−10</sup> et 1)&nbsp;; \(N_I\) entre 1 et 10<sup>9</sup></td><td>[[conf_ignorance]]</td></tr>
<tr><td>idem, avec \(N_I\) jusqu’à 10<sup>30</sup></td><td>[[conf_n_astro]]</td></tr>
<tr><td>comme la troisième ligne, avec \(r\) entre 10<sup>−11</sup> et 1</td><td>[[conf_observateurs]]</td></tr>
</tbody>
</table></div>
<p>Le point de bascule est net&nbsp;: avec \(N_I\) entre 1 et 10<sup>9</sup>, la confiance passe sous 1/2 dès qu’on admet ignorer \(f_P\) et \(f_I\) sur plus de [[largeur_critique]] ordres de grandeur chacun. Le résultat lit la largeur des intervalles d’ignorance que l’on se donne, pas une propriété du monde, et aucune donnée ne fixe ces intervalles.</p>
<p><strong>Kipping (2020).</strong> Kipping traite l’argument par moyenne bayésienne de modèles. Il regroupe (1) et (2) en une hypothèse «&nbsp;physique&nbsp;» \(H_P\) et leur oppose (3), \(H_S\)&nbsp;: une réalité de base engendre \(\lambda\) simulations, dont une fraction \(p\) en engendre à son tour, sur \(G\) générations&nbsp;; le nombre total de simulations vaut alors (son équation&nbsp;1)</p>
$$N_{\mathrm{sim}}=\frac{p\lambda-(p\lambda)^{G}}{p-p^{2}\lambda}.$$
<p>Notons \(g\) la génération de notre réalité, \(g=1\) étant la réalité de base, et CES la seule donnée «&nbsp;je pense, donc je suis&nbsp;» (<i lang="la">cogito, ergo sum</i>). Avec des probabilités a priori égales pour les deux hypothèses, Kipping obtient (équation&nbsp;22)</p>
$$\Pr(g=1\mid\mathrm{CES})=\frac{1}{2}+\frac{1}{2\,(N_{\mathrm{sim}}+1)}.$$
<p>La probabilité d’être simulé est donc inférieure à 1/2 et tend vers 1/2 quand \(N_{\mathrm{sim}}\) croît. Nous avons reproduit ses équations et vérifié leur cohérence interne (autotests). Pour \(p\)&nbsp;=&nbsp;[[k_p]], \(\lambda\)&nbsp;=&nbsp;[[k_lambda]] et \(G\)&nbsp;=&nbsp;[[k_g]], par exemple, \(N_{\mathrm{sim}}\)&nbsp;=&nbsp;[[k_nsim]] et la probabilité d’être simulé vaut [[k_p_simule]]&nbsp;; elle vaut [[k_p_nullipare]] si l’on tient compte de ce que nous n’avons encore créé aucune simulation (équation&nbsp;27).</p>
<p>La lecture de ce résultat est simple. La seule donnée de Kipping, «&nbsp;je pense&nbsp;», a la même probabilité sous les deux hypothèses&nbsp;: son facteur de Bayes vaut 1. La probabilité a posteriori de \(H_S\) est donc égale à sa probabilité a priori \(\pi\), et la probabilité d’être simulé vaut \(\pi\,N_{\mathrm{sim}}/(N_{\mathrm{sim}}+1)\), soit \(\pi\) à très peu près. Le «&nbsp;presque 50&nbsp;%&nbsp;» est le pari à égalité posé au départ. Pour \(N_{\mathrm{sim}}\)&nbsp;=&nbsp;[[k_nsim_ref]], on obtient [[k_pi_tiers]] avec \(\pi=1/3\) et [[k_pi_dixieme]] avec \(\pi=1/10\). Le simple découpage des hypothèses décide&nbsp;: à parts égales entre les deux hypothèses de Kipping, on obtient [[part_deux]]&nbsp;; à parts égales entre les trois propositions de Bostrom, comme celui-ci le suggérait en 2003, [[part_trois]]. Kipping le reconnaît&nbsp;: l’a priori égal «&nbsp;pourrait être contesté comme trop généreux&nbsp;» envers \(H_S\), «&nbsp;modèle intrinsèquement bien plus complexe&nbsp;». Deux phrases de son article (sections&nbsp;2.9 et 3 de la version arXiv) intervertissent «&nbsp;réalité de base&nbsp;» et «&nbsp;simulation&nbsp;»&nbsp;; ses équations et son résumé, eux, sont cohérents.</p>
<p>Une conséquence de Kipping mérite d’être retenue. Si nous créions un jour des simulations peuplées d’êtres conscients, la probabilité d’être dans la réalité de base tomberait à \(\lambda/N_{\mathrm{sim}}\) (équation&nbsp;32), soit [[k_p_base_parous]] dans l’exemple ci-dessus. Bostrom le disait aussi&nbsp;: ce serait «&nbsp;un fort indice contre (1) et (2)&nbsp;». C’est la seule voie connue par laquelle l’argument deviendrait probant.</p>
<p>Enfin, Bostrom ne tire pas lui-même de probabilité de son argument. En 2005&nbsp;: «&nbsp;la disjonction est tout ce que l’argument de la simulation prétend montrer&nbsp;; il ne cherche pas à établir que nous vivons probablement dans une simulation&nbsp;». En 2025, il accorde une «&nbsp;probabilité substantielle&nbsp;» à l’hypothèse mais refuse d’avancer un nombre, qui donnerait «&nbsp;une fausse impression de précision&nbsp;».</p>
<p>L’argument donne donc à l’hypothèse un poids non nul, mais pas une valeur&nbsp;: cette valeur est celle des probabilités a priori qu’on y injecte. Pour la déplacer, il faudrait des données.</p>

<h3>6. Ce que dit la physique</h3>
<p>Plusieurs phénomènes sont souvent invoqués en faveur de la simulation. Voici ce qu’ils montrent, et ce qu’ils ne montrent pas.</p>
<p><strong>Les inégalités de Bell.</strong> En 2015, trois expériences les ont violées en fermant en même temps les principales échappatoires&nbsp;: Hensen et al. (spins d’électrons distants de 1,3&nbsp;km&nbsp;; 245 essais, \(S_{\mathrm{CHSH}}\)&nbsp;=&nbsp;2,42&nbsp;±&nbsp;0,20 alors que toute théorie réaliste locale impose \(S_{\mathrm{CHSH}}\le2\)&nbsp;; \(p\)&nbsp;=&nbsp;0,039), Giustina et al. (photons&nbsp;; probabilité sous le réalisme local au plus 3,74&#8239;×&#8239;10<sup>−31</sup>) et Shalm et al. (photons&nbsp;; \(p\) jusqu’à 5,9&#8239;×&#8239;10<sup>−9</sup>, ou 2,3&#8239;×&#8239;10<sup>−7</sup> en tenant compte de la prévisibilité des choix). Elles montrent qu’aucune théorie à la fois locale et réaliste ne rend compte des corrélations observées, pourvu que les réglages soient choisis indépendamment du système mesuré. Elles ne montrent pas que le monde est calculé&nbsp;: un programme qui calcule l’état quantique global, comme n’importe quel simulateur quantique, reproduit ces corrélations sans difficulté de principe, car la localité en cause est celle de l’espace simulé, pas celle du calculateur. Elles ne l’excluent pas non plus. L’échappatoire qui reste, et que Hensen et al. reconnaissent («&nbsp;aucune expérience de Bell ne peut exclure l’infinité des théories réalistes locales concevables&nbsp;»), porte sur l’indépendance des réglages&nbsp;; ’t&nbsp;Hooft l’assume sous le nom de superdéterminisme, pour un monde qui serait au fond un automate classique, c’est-à-dire la version (c), sans concepteur.</p>
<p><strong>La décohérence.</strong> Selon Zurek (2003), elle «&nbsp;est causée par l’interaction avec l’environnement&nbsp;», qui «&nbsp;surveille&nbsp;» certaines grandeurs du système et détruit les interférences. Aucune conscience n’est requise&nbsp;: Zurek rappelle que von Neumann, London et Bauer, puis Wigner, avaient donné un rôle spécial à l’observateur conscient, et que le formalisme quantique a conduit à une autre vue. L’image d’un monde «&nbsp;rendu seulement quand on le regarde&nbsp;» ne correspond donc pas à la physique quantique&nbsp;: les interférences disparaissent dès que l’information fuit dans l’environnement, qu’un être conscient la recueille ou non. Zurek écrit que la décohérence «&nbsp;aide à résoudre&nbsp;» le problème de la mesure, pas qu’elle le résout entièrement.</p>
<p><strong>Le choix retardé.</strong> Jacques et al. (2007) ont réalisé l’expérience imaginée par Wheeler avec des photons uniques&nbsp;: la configuration de l’interféromètre, ouverte ou fermée, est tirée au sort par un générateur quantique, séparé au sens de la relativité de l’entrée du photon. Les interférences apparaissent avec une visibilité de 94&nbsp;% en configuration fermée, et le chemin est déterminé avec moins de 1&nbsp;% d’erreur en configuration ouverte&nbsp;; la nature s’y comporte «&nbsp;en accord avec les prédictions de la mécanique quantique&nbsp;». Ma, Kofler et Zeilinger (2016) en tirent la leçon générale&nbsp;: ces effets peuvent «&nbsp;imiter une influence d’actions futures sur des événements passés&nbsp;», mais «&nbsp;aucune interaction ni aucun signal physique, a fortiori vers le passé, n’est nécessaire pour expliquer les résultats&nbsp;». Il n’y a pas de passé réécrit, donc pas d’indice d’un calcul fait après coup.</p>
<p><strong>L’ajustement fin.</strong> Barnes (2012) passe en revue les cas où l’ensemble des lois, des constantes et des conditions initiales compatibles avec la vie paraît très petit, en précisant qu’il ne défend «&nbsp;aucune conclusion fondée sur l’ajustement fin&nbsp;». Pour la simulation, ce fait ne discrimine pas. Il serait attendu d’un simulateur qui veut des observateurs, mais aussi d’un grand ensemble d’univers filtré par le fait même que nous sommes là pour l’observer, ou d’une loi plus profonde encore inconnue. Et dans le cas de Bostrom, où l’on simule ses ancêtres, la physique simulée recopie celle des simulateurs&nbsp;: l’ajustement fin serait hérité, non expliqué (section&nbsp;7).</p>
<p><strong>Les revendications d’indices positifs.</strong> Vopson (2023) présente comme des indices qui «&nbsp;semblent étayer&nbsp;» l’hypothèse d’un univers simulé une «&nbsp;seconde loi de l’infodynamique&nbsp;», que l’entropie de l’information ne peut que rester constante ou décroître, et un principe d’équivalence masse-énergie-information. Il note lui-même, en tête de son résumé, le «&nbsp;manque de preuves&nbsp;» de l’hypothèse. En 2025, il dérive la gravitation newtonienne comme une force entropique d’origine informationnelle, «&nbsp;en accord&nbsp;» avec les travaux de Verlinde, et y voit un exemple de «&nbsp;compression de données et d’optimisation computationnelle&nbsp;». Ces deux lois sont ses propres propositions&nbsp;: la seconde loi de l’infodynamique date de 2022, et le principe d’équivalence de 2019, pour lequel il publiait en 2022 un protocole expérimental de test. Surtout, montrer qu’une loi admet une formulation informationnelle ne dit pas qu’elle est plus probable dans un monde simulé que dans un monde qui ne l’est pas&nbsp;: ce rapport n’est calculé dans aucun des deux articles, et une physique informationnelle relève au mieux de la version (c), sans autre système.</p>
<p><strong>Les grilles.</strong> C’est la première des deux pistes qui visent une signature propre au calcul. Beane, Davoudi et Savage (2012, publié en 2014) supposent une simulation sur une grille cubique avec le schéma le plus simple (Wilson, sans amélioration)&nbsp;; la coupure du spectre des rayons cosmiques leur donne une échelle inverse de maille d’au moins 10<sup>11</sup>&nbsp;GeV, et ils proposent de chercher une anisotropie cubique des rayons cosmiques les plus énergétiques. Ils notent eux-mêmes qu’il «&nbsp;semble peu probable&nbsp;» que des simulations autres que «&nbsp;les toutes premières&nbsp;» se passent de schémas améliorés, et que l’amélioration «&nbsp;masque une grande partie&nbsp;» de notre capacité à tester l’hypothèse. Nos trois tests de grille&nbsp;:</p>
<ul>
<li><a href="../test-1/">Test n°&nbsp;1</a>&nbsp;: aucun retard des photons de GRB&nbsp;221009A&nbsp;; une grille cubique (schéma de Yee, temps continu) de maille supérieure à [[t1_maille]]&nbsp;m est exclue dans la pire orientation, mais un pas de temps maximal laisse un angle mort le long des diagonales de la grille.</li>
<li><a href="../test-2/">Test n°&nbsp;2</a>&nbsp;: les [[t2_n]] rayons cosmiques les plus énergétiques de l’observatoire Pierre Auger ne montrent aucune symétrie de cube (\(p\)&nbsp;=&nbsp;[[t2_p]])&nbsp;; mais un excès de flux allant jusqu’à environ [[t2_exces_pct]]&nbsp;% le long des axes n’est pas exclu&nbsp;: le test ne voit que les motifs très marqués.</li>
<li><a href="../test-3/">Test n°&nbsp;3</a>&nbsp;: [[t3_n]] sources de rayons gamma combinées ferment l’angle mort&nbsp;; une grille cubique de maille égale ou supérieure à [[t3_maille]]&nbsp;m est exclue pour toute orientation et tout pas de temps. C’est encore [[t3_planck]] fois la longueur de Planck.</li>
</ul>
<p>Leur portée exacte&nbsp;: ils excluent une famille précise, celle des grilles cubiques à schéma naïf, à maille fixe et sans terme de compensation, au-dessus de ces tailles. Ils ne disent rien des grilles plus fines, des schémas d’ordre supérieur, des maillages non cubiques ou adaptatifs, ni d’une simulation qui calcule à la demande. La FAQ de Bostrom est explicite&nbsp;: il y a «&nbsp;peu de raisons de supposer&nbsp;» que des simulateurs superintelligents utiliseraient «&nbsp;la technique de simulation grossière qu’un tel test détecterait&nbsp;». Même un signal positif ne désignerait pas un ordinateur&nbsp;: une physique fondamentalement discrète, la version (c), produirait le même.</p>
<p><strong>Le hasard.</strong> C’est la seconde piste. Un calcul déterministe ne produit pas de hasard&nbsp;: il l’imite avec un générateur pseudo-aléatoire, et un générateur simple laisse des traces, comme une complexité linéaire trop faible, des répétitions ou des corrélations à longue portée. Notre <a href="../test-4/">test n°&nbsp;4</a> les a cherchées dans [[t4_bits_bruts]] bits quantiques bruts, jamais passés par un algorithme de brassage&nbsp;: photons intriqués et qubits de neuf ordinateurs quantiques d’IBM. Aucune signature n’apparaît, alors que les mêmes tests démasquent quatre générateurs simples utilisés comme témoins, dont le Mersenne Twister, que la batterie officielle du NIST ne voit pas. La règle fixée avant l’analyse réagit sur les données d’IBM telles que publiées, mais la cause est identifiée&nbsp;: une des neuf machines est restée bloquée à 0 ou à 1 pendant des séries entières, un défaut qui n’a pas la structure d’un générateur. L’écarter a été décidé après avoir vu les données, et le test le signale comme tel. Surtout, PCG64, SHA-256 en mode compteur et les décimales binaires de \(\sqrt{2}\), des suites entièrement déterministes, passent tous les tests&nbsp;: un générateur de qualité cryptographique est indiscernable par principe. Le test exclut une simulation qui tirerait ses mesures quantiques d’un générateur simple, pas une simulation soignée.</p>
<p>La physique n’a donc trouvé aucune trace positive, et ses résultats négatifs ne portent que sur des architectures particulières. Leur poids dépend du poids qu’on donne a priori à ces architectures, ce qui ramène à la section&nbsp;8.</p>

<h3>7. Arguments métaphysiques</h3>
<p><strong>La souffrance et le choix.</strong> Bostrom envisage qu’une interdiction éthique, «&nbsp;à cause de la souffrance infligée aux habitants de la simulation&nbsp;», détourne les civilisations avancées des simulations d’ancêtres&nbsp;; il évoque aussi, en la qualifiant de «&nbsp;tirée par les cheveux&nbsp;», une solution au problème du mal&nbsp;: les souvenirs de souffrance seraient des illusions. La souffrance n’est un argument contre la simulation que si l’on suppose des simulateurs bienveillants et maîtres de leur œuvre&nbsp;; contre des simulateurs indifférents ou curieux, sur lesquels l’argument de Bostrom ne suppose rien, elle ne pèse rien. Elle ne devient pertinente que dans les modèles où les participants choisissent d’entrer dans la simulation, c’est-à-dire la version (a) avec une conscience extérieure qui aurait consenti. Mais on peut alors ajuster les motifs supposés pour rendre compte de n’importe quelle souffrance, ce qui retire à l’hypothèse tout pouvoir de test&nbsp;: une hypothèse qui s’accommode de tout ne prédit rien.</p>
<p><strong>La régression.</strong> La simulation n’explique pas l’existence d’un monde&nbsp;: elle la reporte sur un monde de base, ses simulateurs et leurs machines. Si notre monde réclame une explication, pour ses lois ou son ajustement fin, le monde de base la réclame tout autant. Bostrom reconnaît que le statut de la thèse selon laquelle la hiérarchie des simulations doit s’arrêter quelque part est «&nbsp;quelque peu obscur&nbsp;», et Vazza juge la physique d’un univers simulateur très différent du nôtre hors de ce qui est testable. On peut accepter qu’un niveau soit un fait brut, sans explication&nbsp;; mais alors rien n’oblige à placer ce niveau ailleurs que dans notre propre monde.</p>
<p><strong>La simplicité, traitée symétriquement.</strong> Si l’on compte la simplicité, elle compte contre l’hypothèse qui ajoute un monde, des agents, des machines et des motifs, à moins que cet ajout ne réduise d’autant les faits inexpliqués, ce qu’il ne fait pas puisqu’il les reporte. Si l’on invoque le caractère mathématique ou «&nbsp;compressible&nbsp;» de nos lois comme indice de programme, il faut appliquer la même mesure à un monde non simulé dont les lois seraient simples&nbsp;: il présenterait exactement le même caractère, et le rapport de vraisemblance vaut 1. Quant à la neutralité, l’indifférence n’en est pas une&nbsp;: on l’a vu à la section&nbsp;5, parts égales entre deux hypothèses ou entre trois propositions donnent une moitié ou un tiers.</p>
<p><strong>La valeur d’un monde simulé.</strong> Chalmers soutient que la vie dans un monde virtuel peut être «&nbsp;aussi bonne, en principe&nbsp;», et «&nbsp;pleinement signifiante&nbsp;»&nbsp;; Bostrom, que les implications d’une simulation ne seraient «&nbsp;pas si radicales&nbsp;», notre meilleur guide restant «&nbsp;l’étude empirique ordinaire de l’univers que nous voyons&nbsp;». Même si la réponse était oui, les personnes, leurs souffrances et leurs choix resteraient réels. L’enjeu pratique de la question est moindre qu’il n’y paraît&nbsp;; raison de plus pour ne pas lui donner une réponse plus assurée que ne le permettent les raisons.</p>

<h3>8. Ce qu’il faudrait calculer</h3>
<p>Notons \(S\) l’hypothèse «&nbsp;notre monde et nos expériences sont produits par un autre système&nbsp;», \(\neg S\) sa négation, \(D\) l’ensemble des données, \(\theta\) les caractéristiques d’une simulation (architecture, résolution, schéma, stratégie de rendu, motifs des simulateurs) et \(\pi(\theta\mid S)\) leur loi a priori. Alors</p>
$$P(S\mid D)=\frac{P(D\mid S)\,P(S)}{P(D\mid S)\,P(S)+P(D\mid\neg S)\,\bigl(1-P(S)\bigr)},\qquad P(D\mid S)=\int P(D\mid S,\theta)\,\pi(\theta\mid S)\,d\theta.$$
<p><strong>Ce que renseignent les tests.</strong> Ils donnent \(P(D\mid S,\theta)\) pour certains \(\theta\). Pour une grille cubique naïve plus grossière que les bornes, un résultat nul est exclu&nbsp;: \(P(D\mid S,\theta)\approx0\). Pour les autres \(\theta\), la simulation reproduit nos observations&nbsp;: \(P(D\mid S,\theta)=P(D\mid\neg S)\). Si \(w\) est le poids a priori des architectures exclues, le facteur de Bayes vaut \(1-w\). Les tests ne donnent pas \(w\)&nbsp;: ce poids n’est pas une mesure, c’est un jugement sur ce que feraient des simulateurs. Avec \(w\)&nbsp;=&nbsp;[[w_ex]], une confiance de 1/2 passe à [[w_apres]]. Pour la faire tomber à 1/10, il faudrait \(w\)&nbsp;=&nbsp;[[w_dixieme]], c’est-à-dire tenir les grilles naïves pour presque la seule manière de simuler un monde, ce que ni Beane et al. ni Bostrom ne soutiennent.</p>
<p><strong>Les arguments dépendants.</strong> «&nbsp;Nos perceptions pourraient être fabriquées&nbsp;», «&nbsp;la simulation serait indiscernable&nbsp;» et «&nbsp;la physique quantique ressemble à un rendu à la demande&nbsp;» reposent sur la même hypothèse d’indiscernabilité&nbsp;; «&nbsp;l’Univers est réglé pour la vie&nbsp;» et «&nbsp;un concepteur l’a voulu&nbsp;» reposent sur la même hypothèse sur les motifs des simulateurs. Formellement, \(P(D_1,D_2\mid S)=P(D_1\mid S)\,P(D_2\mid S,D_1)\), et non \(P(D_1\mid S)\,P(D_2\mid S)\)&nbsp;: multiplier les rapports de vraisemblance d’arguments qui partagent une prémisse compte cette prémisse autant de fois qu’il y a d’arguments.</p>
<p><strong>L’équivalence observationnelle.</strong> Pour la famille de simulations que décrivent Bostrom et, à sa suite, Edge et Brown, qui produisent les apparences à la demande et corrigent les incohérences, \(P(D\mid S,\theta)=P(D\mid\neg S)\) pour toute donnée \(D\) que nous pouvons recueillir&nbsp;: aucune expérience ne peut augmenter \(P(S)\). La confiance dans cette version est alors exactement sa probabilité a priori, et la section&nbsp;5 a montré que cette probabilité n’est fixée par rien d’objectif. Les versions qui laissent des traces sont, elles, soit contraintes par nos tests et par ceux de la littérature, soit exclues sous notre physique par les bornes de Vazza. C’est la structure de la réponse&nbsp;: les versions testables de l’hypothèse perdent du terrain, les versions intestables n’en gagnent pas.</p>
<p><strong>Ce qui changerait la réponse.</strong> Une anomalie reproductible, vue par plusieurs messagers indépendants, avec une signature propre au calcul (par exemple une anisotropie cubique de même orientation dans la lumière et dans les rayons cosmiques), qu’aucune physique ordinaire, discrète ou continue, n’expliquerait. Ou notre propre capacité à créer des simulations peuplées d’êtres dont nous aurions des raisons de croire qu’ils sont conscients&nbsp;: c’est l’équation&nbsp;32 de Kipping et le «&nbsp;fort indice&nbsp;» de Bostrom.</p>

<h3>9. Reproduire</h3>
<p>Le script refait en quelques secondes tous les calculs de cette synthèse et vérifie d’abord ses formules par [[n_autotests]] autotests&nbsp;: formule de Bostrom, produit de sa note&nbsp;10, lois a priori calculées exactement puis contrôlées par Monte-Carlo, équations de Kipping, cas limites de la mise à jour par les tests. Il relit les résultats des tests n°&nbsp;1 à 3 et en enregistre l’empreinte SHA-256. Les citations sont traduites par nous&nbsp;; l’original anglais et sa page figurent dans <code>sources.md</code>.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/synthese/analyse.py" download>analyse.py</a>&nbsp;: le script (Python&nbsp;3, numpy)</li>
<li><a href="/fichiers/synthese/resultats.json" download>resultats.json</a>&nbsp;: toutes les valeurs calculées</li>
<li><a href="/fichiers/synthese/sources.md" download>sources.md</a>&nbsp;: le passage vérifié de chaque référence</li>
</ul>

<h2 id="bilan">Bilan</h2>
<div class="tableau"><table class="phrases">
<thead><tr><th>Question</th><th>Conclusion</th></tr></thead>
<tbody>
<tr><td>De quelle simulation parle-t-on&nbsp;?</td><td>Seules (a), une conscience extérieure branchée sur un monde artificiel, et (b), un monde calculé avec ses propres êtres conscients, supposent un autre système&nbsp;; (c), des lois computationnelles sans concepteur, n’en suppose pas. Dans tous les cas, le monde resterait réel.</td></tr>
<tr><td>La perception suggère-t-elle la simulation&nbsp;?</td><td>Non. Elle interdit de l’exclure par introspection&nbsp;; pour une simulation indiscernable, le rapport de vraisemblance vaut 1.</td></tr>
<tr><td>Un calcul peut-il être conscient&nbsp;?</td><td>Question ouverte&nbsp;: Chalmers pour, Searle contre, et Mogensen (2025) affaiblit l’argument des qualia évanescents. Pour la version (b), la confiance d’être simulé est au plus \(c\).</td></tr>
<tr><td>Est-ce faisable&nbsp;?</td><td>Une simulation complète sous notre physique est exclue (Vazza, 2025)&nbsp;; une simulation minimale ne l’est pas, mais son coût n’a jamais été chiffré et elle ne laisse, par construction, aucune trace.</td></tr>
<tr><td>L’argument de Bostrom établit-il la simulation&nbsp;?</td><td>Non. Il établit une disjonction&nbsp;; la probabilité qu’on en tire reflète les hypothèses a priori, de [[conf_observateurs]] à [[conf_genereux]] dans nos scénarios&nbsp;; le «&nbsp;presque 50&nbsp;%&nbsp;» de Kipping est son a priori&nbsp;; Bostrom refuse lui-même d’avancer un nombre.</td></tr>
<tr><td>La physique en montre-t-elle une trace&nbsp;?</td><td>Non. Bell, la décohérence et le choix retardé s’expliquent sans calcul caché&nbsp;; l’ajustement fin ne discrimine pas&nbsp;; les indices revendiqués par Vopson ne calculent pas de rapport de vraisemblance&nbsp;; les tests de grille, dont trois des nôtres, ne trouvent rien, et notre test du hasard quantique ne trouve la signature d’aucun générateur simple.</td></tr>
<tr><td>La métaphysique la favorise-t-elle&nbsp;?</td><td>Non. L’hypothèse reporte l’explication sans la réduire&nbsp;; la simplicité, appliquée symétriquement, ne la favorise pas&nbsp;; la souffrance ne pèse que dans les modèles où les participants choisissent.</td></tr>
<tr><td>Les tests ou les «&nbsp;preuves&nbsp;» démontrent-ils son impossibilité&nbsp;?</td><td>Non. Les tests renseignent \(P(D\mid S,\theta)\) pour certains \(\theta\) seulement, dont le poids n’est pas mesurable&nbsp;; les preuves d’impossibilité valent sous leurs prémisses (notre physique pour Vazza, une réalité non algorithmique pour Faizal et al.).</td></tr>
</tbody>
</table></div>
<p><strong>Réponse à la question posée&nbsp;: non.</strong> Nous n’avons pas, en l’état, de meilleures raisons de penser que notre monde et nos expériences sont produits par un autre système que de penser le contraire. Aucune donnée ne favorise la simulation&nbsp;; l’argument qui la rend concevable ne fixe pas sa probabilité&nbsp;; les seules données pertinentes retirent des versions de l’hypothèse sans jamais en ajouter. Elles ne démontrent pas pour autant son impossibilité.</p>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>D. J. Chalmers, <cite>The Matrix as Metaphysics</cite>, dans C. Grau (dir.), <cite>Philosophers Explore The Matrix</cite>, Oxford University Press, 2005, p.&nbsp;132-176, <a href="https://doi.org/10.1093/oso/9780195181067.003.0009">DOI 10.1093/oso/9780195181067.003.0009</a>&nbsp;; texte de l’auteur&nbsp;: <a href="https://consc.net/papers/matrix.html">consc.net/papers/matrix.html</a>.</li>
<li>D. J. Chalmers, <cite>Reality+: Virtual Worlds and the Problems of Philosophy</cite>, W. W. Norton et Allen Lane, 2022 (ISBN 9780393635805)&nbsp;; présentation de l’auteur&nbsp;: <a href="https://consc.net/reality/">consc.net/reality</a>.</li>
<li>N. Bostrom, <cite>Are We Living in a Computer Simulation?</cite>, The Philosophical Quarterly 53 (211), 243-255 (2003), <a href="https://doi.org/10.1111/1467-9213.00309">DOI 10.1111/1467-9213.00309</a>&nbsp;; version de l’auteur, intitulée <cite>Are You Living in a Computer Simulation?</cite>&nbsp;: <a href="https://simulation-argument.com/simulation.pdf">simulation-argument.com/simulation.pdf</a>.</li>
<li>N. Bostrom, <cite>The Simulation Argument: Reply to Weatherson</cite>, The Philosophical Quarterly 55 (218), 90-97 (2005), <a href="https://doi.org/10.1111/j.0031-8094.2005.00387.x">DOI 10.1111/j.0031-8094.2005.00387.x</a>.</li>
<li>N. Bostrom, M. Kulczycki, <cite>A Patch for the Simulation Argument</cite>, Analysis 71 (1), 54-61 (2011), <a href="https://doi.org/10.1093/analys/anq107">DOI 10.1093/analys/anq107</a>.</li>
<li>N. Bostrom, <cite>The Simulation Argument FAQ</cite>, version 2.0 (2025), <a href="https://simulation-argument.com/faq.html">simulation-argument.com/faq.html</a>, consultée le 28&nbsp;septembre 2026.</li>
<li>B. Weatherson, <cite>Are You a Sim?</cite>, The Philosophical Quarterly 53 (212), 425-431 (2003), <a href="https://doi.org/10.1111/1467-9213.00323">DOI 10.1111/1467-9213.00323</a>.</li>
<li>J. B. Hartle, M. Srednicki, <cite>Are we typical?</cite>, Physical Review D 75, 123523 (2007), <a href="https://doi.org/10.1103/PhysRevD.75.123523">DOI 10.1103/PhysRevD.75.123523</a>, <a href="https://arxiv.org/abs/0704.2630">arXiv:0704.2630</a>.</li>
<li>D. Kipping, <cite>A Bayesian Approach to the Simulation Argument</cite>, Universe 6 (8), 109 (2020), <a href="https://doi.org/10.3390/universe6080109">DOI 10.3390/universe6080109</a>, <a href="https://arxiv.org/abs/2008.12254">arXiv:2008.12254</a>.</li>
<li>A. Bibeau-Delisle, G. Brassard, <cite>Probability and consequences of living inside a computer simulation</cite>, Proceedings of the Royal Society A 477 (2247), 20200658 (2021), <a href="https://doi.org/10.1098/rspa.2020.0658">DOI 10.1098/rspa.2020.0658</a>, <a href="https://arxiv.org/abs/2008.09275">arXiv:2008.09275</a>.</li>
<li>J. Birch, <cite>On the ‘Simulation Argument’ and Selective Scepticism</cite>, Erkenntnis 78 (1), 95-107 (2013), <a href="https://doi.org/10.1007/s10670-012-9400-9">DOI 10.1007/s10670-012-9400-9</a>.</li>
<li>D. J. Chalmers, <cite>Absent Qualia, Fading Qualia, Dancing Qualia</cite>, dans T. Metzinger (dir.), <cite>Conscious Experience</cite>, Imprint Academic, 1995, <a href="https://consc.net/papers/qualia.html">consc.net/papers/qualia.html</a>&nbsp;; repris dans <cite>The Conscious Mind</cite>, Oxford University Press, 1996, chapitre&nbsp;7.</li>
<li>J. R. Searle, <cite>Minds, brains, and programs</cite>, Behavioral and Brain Sciences 3 (3), 417-424 (1980), <a href="https://doi.org/10.1017/S0140525X00005756">DOI 10.1017/S0140525X00005756</a>.</li>
<li>A. L. Mogensen, <cite>How to resist the Fading Qualia Argument</cite>, Synthese 206, 252 (2025), <a href="https://doi.org/10.1007/s11229-025-05338-3">DOI 10.1007/s11229-025-05338-3</a>.</li>
<li>S. Lloyd, <cite>Ultimate physical limits to computation</cite>, Nature 406, 1047-1054 (2000), <a href="https://doi.org/10.1038/35023282">DOI 10.1038/35023282</a>, <a href="https://arxiv.org/abs/quant-ph/9908043">arXiv:quant-ph/9908043</a>.</li>
<li>S. Lloyd, <cite>Computational Capacity of the Universe</cite>, Physical Review Letters 88, 237901 (2002), <a href="https://doi.org/10.1103/PhysRevLett.88.237901">DOI 10.1103/PhysRevLett.88.237901</a>, <a href="https://arxiv.org/abs/quant-ph/0110141">arXiv:quant-ph/0110141</a>.</li>
<li>F. Vazza, <cite>Astrophysical constraints on the simulation hypothesis for this Universe: why it is (nearly) impossible that we live in a simulation</cite>, Frontiers in Physics 13, 1561873 (2025), <a href="https://doi.org/10.3389/fphy.2025.1561873">DOI 10.3389/fphy.2025.1561873</a>, <a href="https://arxiv.org/abs/2504.08461">arXiv:2504.08461</a>.</li>
<li>E. Edge, C. A. Brown, <cite>Commentary: Astrophysical constraints on the simulation hypothesis for this Universe: why it is (nearly) impossible that we live in a simulation</cite>, Frontiers in Physics 14, 1808725 (2026), <a href="https://doi.org/10.3389/fphy.2026.1808725">DOI 10.3389/fphy.2026.1808725</a>.</li>
<li>M. Faizal, L. M. Krauss, A. Shabir, F. Marino, <cite>Consequences of Undecidability in Physics on the Theory of Everything</cite>, Journal of Holography Applications in Physics 5 (2), 10-21 (2025), <a href="https://arxiv.org/abs/2507.22950">arXiv:2507.22950</a>.</li>
<li>G. ’t&nbsp;Hooft, <cite>The Cellular Automaton Interpretation of Quantum Mechanics</cite>, Springer, collection Fundamental Theories of Physics, 2016, <a href="https://doi.org/10.1007/978-3-319-41285-6">DOI 10.1007/978-3-319-41285-6</a>, <a href="https://arxiv.org/abs/1405.1548">arXiv:1405.1548</a>.</li>
<li>B. Hensen et al., <cite>Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres</cite>, Nature 526, 682-686 (2015), <a href="https://doi.org/10.1038/nature15759">DOI 10.1038/nature15759</a>, <a href="https://arxiv.org/abs/1508.05949">arXiv:1508.05949</a>.</li>
<li>M. Giustina et al., <cite>Significant-Loophole-Free Test of Bell’s Theorem with Entangled Photons</cite>, Physical Review Letters 115, 250401 (2015), <a href="https://doi.org/10.1103/PhysRevLett.115.250401">DOI 10.1103/PhysRevLett.115.250401</a>, <a href="https://arxiv.org/abs/1511.03190">arXiv:1511.03190</a>.</li>
<li>L. K. Shalm et al., <cite>Strong Loophole-Free Test of Local Realism</cite>, Physical Review Letters 115, 250402 (2015), <a href="https://doi.org/10.1103/PhysRevLett.115.250402">DOI 10.1103/PhysRevLett.115.250402</a>, <a href="https://arxiv.org/abs/1511.03189">arXiv:1511.03189</a>.</li>
<li>W. H. Zurek, <cite>Decoherence, einselection, and the quantum origins of the classical</cite>, Reviews of Modern Physics 75, 715-775 (2003), <a href="https://doi.org/10.1103/RevModPhys.75.715">DOI 10.1103/RevModPhys.75.715</a>, <a href="https://arxiv.org/abs/quant-ph/0105127">arXiv:quant-ph/0105127</a>.</li>
<li>V. Jacques et al., <cite>Experimental Realization of Wheeler’s Delayed-Choice Gedanken Experiment</cite>, Science 315, 966-968 (2007), <a href="https://doi.org/10.1126/science.1136303">DOI 10.1126/science.1136303</a>, <a href="https://arxiv.org/abs/quant-ph/0610241">arXiv:quant-ph/0610241</a>.</li>
<li>X.-S. Ma, J. Kofler, A. Zeilinger, <cite>Delayed-choice gedanken experiments and their realizations</cite>, Reviews of Modern Physics 88, 015005 (2016), <a href="https://doi.org/10.1103/RevModPhys.88.015005">DOI 10.1103/RevModPhys.88.015005</a>, <a href="https://arxiv.org/abs/1407.2930">arXiv:1407.2930</a>.</li>
<li>L. A. Barnes, <cite>The Fine-Tuning of the Universe for Intelligent Life</cite>, Publications of the Astronomical Society of Australia 29 (4), 529-564 (2012), <a href="https://doi.org/10.1071/AS12015">DOI 10.1071/AS12015</a>, <a href="https://arxiv.org/abs/1112.4647">arXiv:1112.4647</a>.</li>
<li>M. M. Vopson, <cite>The second law of infodynamics and its implications for the simulated universe hypothesis</cite>, AIP Advances 13, 105308 (2023), <a href="https://doi.org/10.1063/5.0173278">DOI 10.1063/5.0173278</a>.</li>
<li>M. M. Vopson, <cite>Is gravity evidence of a computational universe?</cite>, AIP Advances 15, 045035 (2025), <a href="https://doi.org/10.1063/5.0264945">DOI 10.1063/5.0264945</a>.</li>
<li>M. M. Vopson, <cite>The mass-energy-information equivalence principle</cite>, AIP Advances 9, 095206 (2019), <a href="https://doi.org/10.1063/1.5123794">DOI 10.1063/1.5123794</a>&nbsp;; <cite>Experimental protocol for testing the mass–energy–information equivalence principle</cite>, AIP Advances 12, 035311 (2022), <a href="https://doi.org/10.1063/5.0087175">DOI 10.1063/5.0087175</a>&nbsp;; M. M. Vopson, S. Lepadatu, <cite>Second law of information dynamics</cite>, AIP Advances 12, 075310 (2022), <a href="https://doi.org/10.1063/5.0100358">DOI 10.1063/5.0100358</a>.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, European Physical Journal A 50, 148 (2014), <a href="https://doi.org/10.1140/epja/i2014-14148-0">DOI 10.1140/epja/i2014-14148-0</a>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>aeternam, <a href="../test-1/">test n°&nbsp;1</a>, <a href="../test-2/">test n°&nbsp;2</a>, <a href="../test-3/">test n°&nbsp;3</a> et <a href="../test-4/">test n°&nbsp;4</a>&nbsp;: scripts et résultats téléchargeables sur chaque page.</li>
</ol>
""",
}
