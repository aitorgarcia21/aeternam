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
<li><strong>La maille est donc inférieure à [[a_resume]]&nbsp;m</strong> avec la méthode la plus prudente et l’orientation la plus défavorable, ou à [[a_ml_resume]]&nbsp;m avec la méthode de vraisemblance. L’échelle d’énergie de la grille dépasse [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>Ce n’est pas une frontière nouvelle.</strong> Beane, Davoudi et Savage obtenaient déjà le même ordre de grandeur en 2012 (environ [[b_beane]]&nbsp;m) à partir des rayons cosmiques. Ce résultat en est une confirmation indépendante, par une autre observable.</li>
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
<p>Beane, Davoudi et Savage (2012) ont étudié une simulation de la chromodynamique quantique sur réseau. Ils bornaient l’inverse de la maille à \(1/b\gtrsim10^{11}\)&nbsp;GeV, soit \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m, à partir de la coupure du spectre des rayons cosmiques. Notre borne prudente vaut [[beane_ratio]] fois la leur&nbsp;; les méthodes de vraisemblance de LHAASO donnent [[beane_ml_min]] à [[beane_ml_max]] fois la leur. Les deux approches se recoupent donc à l’ordre de grandeur, avec des observables, des particules et des hypothèses différentes&nbsp;: c’est une confirmation, pas un record.</p>
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
