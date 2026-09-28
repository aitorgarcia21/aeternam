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
    'verdict': 'Verdict à ce jour : non. Aucune signature de simulation n’est détectée par les tests effectués ; ils contraignent certains modèles d’espace discret, sans dire si l’Univers est simulé.',
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
