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
    'description_site': 'Aeternam, un blog de recherche sur les interfaces cerveau-machine, la vision, '
                        'la mémoire, le rêve, le temps vécu, la relativité, les trous noirs et la théorie de la simulation.',
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

<h2 id="analyse">Analyse détaillée</h2><p><strong>Portée statistique corrigée.</strong> Les huit bornes nominales à 95&nbsp;% forment une famille complète. Bonferroni donne au moins [[couverture]]&nbsp;% de couverture simultanée, sous leurs hypothèses respectives. Compter seulement les [[n_actives]] contraintes actives après optimisation serait une sélection a posteriori. Le maximum d’orientation est numérique, sans certificat global&nbsp;: la valeur [[pire1]]&nbsp;m est une enveloppe de compatibilité du modèle, pas une exclusion jointe à 95&nbsp;%.</p>

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
    'titre': 'Ce que nos recherches disent de la simulation',
    'description': 'Arguments conditionnels, modèles physiques précis et calculs de sensibilité : aucune probabilité cosmique mesurée.',
    'date': '29 septembre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>Avons-nous trouvé une preuve que notre Univers est simulé&nbsp;? Non.</strong> Nous avons étudié des arguments et testé des modèles précis. Aucun résultat examiné n’établit cette conclusion.</p>
<p>Cette recherche reste une branche fondamentale d’Aeternam. Elle pose la question de la nature de notre monde. Les <a href="/sujets/reve-temps/">articles sur le rêve</a> étudient les expériences d’un cerveau humain. Les deux peuvent partager une curiosité philosophique sans partager leurs preuves.</p>
<p>Trois questions doivent rester distinctes&nbsp;: un monde calculé est-il concevable&nbsp;? Existe-t-il une observation qui le distingue d’un autre monde&nbsp;? Peut-on construire des expériences oniriques plus riches ou plus longues&nbsp;? Une réponse à l’une ne résout pas les autres.</p>
<p>Un ordinateur ne doit pas nécessairement utiliser une grille cubique naïve, un générateur aléatoire simple ou un rendu déclenché par un observateur conscient. Nos tests portent sur certaines de ces architectures. Leur échec ou leur exclusion ne décide pas du sort de toutes les simulations possibles.</p>
<p>Nous avons également retiré la présentation de «&nbsp;7&nbsp;% de chances d’être simulés&nbsp;» comme estimation d’Aeternam. Ce nombre provenait d’intervalles et de probabilités choisis. Il reste un exemple de sensibilité aux hypothèses, sans statut de mesure.</p>
<h2 id="analyse">Analyse détaillée</h2>
<h3 id="bostrom">1. Ce que calcule l’argument de Bostrom</h3>
<p>L’<a href="https://simulation-argument.com/simulation/">argument de 2003</a> relie la proportion d’observateurs simulés au nombre de simulations et aux fractions de civilisations qui peuvent et souhaitent les produire. Sous son cadre de comptage, avec <em>x</em> le produit de ces facteurs, la fraction simulée vaut&nbsp;:</p>
$$f_{\mathrm{sim}}=\frac{x}{1+x},\qquad x=f_P f_I N_I.$$
<p>Le calcul est conditionnel. Ni l’existence de nombreuses simulations conscientes, ni ces paramètres, ni notre position d’observateur typique ne sont mesurés par la formule. Si deux hypothèses produisent les mêmes observations avec la même probabilité, leur rapport de vraisemblance vaut 1&nbsp;: ces observations seules ne les départagent pas.</p>
<h3>2. Sensibilité des scénarios</h3>
<p>Nous intégrons cette formule sur des lois log-uniformes choisies, avec une grille en logarithme, puis comparons le calcul à un Monte-Carlo. L’accord numérique valide une intégration, pas les hypothèses. Les valeurs suivantes sont des fractions conditionnelles entre 0 et 1.</p>
<div class="tableau"><table class="phrases"><thead><tr><th>Choix illustratif</th><th>Résultat du modèle</th></tr></thead><tbody>
<tr><td>Fractions entre 0,1 et 1&nbsp;; nombre de simulations entre mille et un milliard</td><td>[[conf_genereux]]</td></tr>
<tr><td>Fractions entre 10<sup>−10</sup> et 1&nbsp;; nombre de simulations entre 1 et un milliard</td><td>[[conf_ignorance]]</td></tr>
<tr><td>Mêmes fractions, nombre de simulations allant jusqu’à 10<sup>30</sup></td><td>[[conf_n_astro]]</td></tr>
<tr><td>Deuxième scénario, avec moins d’observateurs par simulation selon une autre loi choisie</td><td>[[conf_observateurs]]</td></tr>
<tr><td>Deuxième scénario, pondéré par un choix arbitraire de 1/2 sur un modèle de conscience</td><td>[[conf_aeternam]]</td></tr>
</tbody></table></div>
<p>Aucune ligne n’est neutre. Choisir dix ordres de grandeur, un milliard de mondes ou une pondération de 1/2 exprime un a priori. Le fait de ne pas savoir n’impose aucune de ces valeurs.</p>
<p>La conscience demande aussi de préciser le modèle. Si <em>c</em> pondère deux possibilités globales — tous les simulés conscients, ou aucun — notre exemple emploie \(c\,x/(1+x)\). Si <em>c</em> désigne plutôt la fraction d’individus simulés conscients, le comptage donnerait \(cx/(1+cx)\). Ces expressions ne sont pas interchangeables.</p>
<h3>3. Le résultat bayésien de Kipping</h3>
<p>Dans le cadre de <a href="https://doi.org/10.3390/universe6080109">Kipping (2020)</a>, deux classes de mondes reçoivent des poids a priori. Pour le conditionnement utilisé dans son équation 22, un nombre immense de simulations ne suffit pas à effacer ces poids. Avec notre généralisation à un poids \(\pi\), le terme considéré est \(\pi N/(N+1)\).</p>
<p>Pour un même nombre très élevé de simulations, changer \(\pi\) de 1/3 à 1/10 donne respectivement [[k_pi_tiers]] et [[k_pi_dixieme]]. Cette variation relève de la structure du modèle. Elle n’est pas une mesure astrophysique.</p>
<h3>4. Portée de nos tests physiques</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Analyse</th><th>Ce qui est testé</th><th>Portée du résultat</th></tr></thead><tbody>
<tr><td><a href="/test-1/">Dispersion d’un sursaut gamma</a></td><td>Un schéma précis de propagation sur réseau</td><td>Contrainte conditionnelle aux paramètres et à la discrétisation choisie</td></tr>
<tr><td><a href="/test-3/">Huit sources gamma</a></td><td>Compatibilité directionnelle de huit contraintes publiées</td><td>Enveloppe optimisée numériquement&nbsp;; couverture simultanée corrigée</td></tr>
<tr><td><a href="/test-2/">Rayons cosmiques</a> et <a href="/test-6/">ciel complet</a></td><td>Un motif cubique sous un modèle d’exposition</td><td>Pas de détection significative dans le test principal&nbsp;; conclusions liées à ce motif</td></tr>
<tr><td><a href="/test-4/">Hasard quantique</a></td><td>Répétitions et structures détectables par les statistiques choisies</td><td>Ni test de toute famille de générateurs, ni certification générale d’imprévisibilité</td></tr>
<tr><td><a href="/test-5/">Rendu à la demande</a></td><td>Une formalisation de visibilité des interférences</td><td>Désaccord avec cette formalisation&nbsp;; significativités conditionnelles aux erreurs reconstruites</td></tr>
<tr><td><a href="/audit-infodynamique/">Infodynamique</a></td><td>Étapes algébriques de démonstrations proposées</td><td>Des contre-exemples invalident ces étapes, sans trancher toute l’hypothèse de simulation</td></tr>
</tbody></table></div>
<p>Pour les huit sources gamma, la correction de Bonferroni doit porter sur toute la famille&nbsp;: 1 − 8 × 0,05 = 0,60. Retenir seulement les trois contraintes actives après optimisation donnait à tort 0,85. Cette couverture minimale reste conditionnelle à la validité des couvertures nominales de chaque source&nbsp;; elle n’est pas une analyse jointe à 95&nbsp;%.</p>
<p>Pour le ciel complet, les valeurs d’amplitude reposent sur une approximation normale et un ensemble fini d’orientations. Pour les interférences, les données numérisées dans les figures et leurs erreurs supposées ne justifient pas de présenter une significativité combinée comme une réfutation universelle.</p>
<h3>5. Ce qu’un test nul change réellement</h3>
<p>Notre modèle simplifié d’actualisation suppose qu’une part <em>w</em> des simulations envisagées aurait donné un signal avec certitude, tandis que les autres donnent les mêmes données que l’hypothèse sans simulation. Dans ce cas idéal seulement, le facteur de Bayes d’un résultat nul vaut 1 − <em>w</em>.</p>
<p>Une borne fréquentiste à 95&nbsp;% ne dit pas que la probabilité d’une architecture est de 5&nbsp;%. Pour une actualisation réelle, il faudrait une vraisemblance sous chaque modèle, sa sensibilité, ses paramètres et des poids explicites. Les tests du dépôt ne fournissent pas ces éléments pour toutes les simulations.</p>
<h3>6. Le programme qui en découle</h3>
<p>Une piste exploitable doit annoncer un modèle, une observable, une prédiction différente et un test pouvant échouer. Les analyses futures devront intégrer les paramètres instrumentaux, la multiplicité et les explications physiques concurrentes. Une anomalie reproductible serait une observation à expliquer&nbsp;; sa seule existence ne l’attribuerait pas à un simulateur.</p>
<p>Ces recherches portent sur des modèles physiques et des arguments philosophiques. Les articles sur le cerveau emploient leurs propres mesures : accès, contenu, durée et mémoire. Une conclusion sur l’un de ces sujets ne valide pas les hypothèses d’un autre.</p>
""",
}

TEMPS_STIMULATION = {
    'titre': 'Modifier le temps ressenti',
    'description': 'Durée estimée, attention, performance et souvenir : réanalyse des interventions étudiées.',
    'date': '29 septembre 2026',
    'corps': r"""

<h2 id="explication">Explication</h2>
<p><strong>Les interventions examinées démontrent-elles une vie consciente accélérée&nbsp;? Non.</strong> Elles montrent des changements de durée estimée et, pour certaines tâches, de performance. Ces résultats donnent des questions de recherche distinctes.</p>
<p>Une personne peut juger un événement plus long sans mieux distinguer des images rapides. Elle peut aussi rapporter davantage de lettres après une stimulation sans avoir vécu une existence plus longue. Le souvenir, l’attention et la durée ressentie doivent être mesurés séparément.</p>
<p>Pour Aeternam, les voies de travail sont la perception temporelle, l’accès au rêve et la mémoire au réveil. Le <a href="/programme/">programme actuel</a> avance par réanalyse et simulation numérique, sans nouvelle intervention sur une personne.</p>
<h2 id="analyse">Analyse détaillée</h2>
<h3>Un changement de jugement</h3>
<p>Dans l’étude de <a href="https://doi.org/10.1371/journal.pone.0001295">Stetson et al. (2007)</a>, le rapport entre la durée rétrospective de sa propre chute et celle imaginée pour autrui vaut [[chute_autrui]]. Par rapport à la durée réelle, il vaut [[chute_reel]]. Le dénominateur choisi change donc ce que signifie le facteur. La performance de résolution temporelle n’établit pas une accélération générale.</p>
<h3>Un changement de performance</h3>
<p><a href="https://doi.org/10.1080/17470218.2010.502580">Jones, Allely et Wearden (2011)</a> rapportent des gains de lettres correctement restituées de 3,25&nbsp;% et 5,85&nbsp;% dans deux conditions. Leur moyenne arithmétique vaut [[jones_gain]]&nbsp;%. Elle décrit ces deux gains, sans constituer une vitesse du vécu.</p>
<p>Notre ancien calcul reconstruisait une erreur type de cette moyenne à partir du test <em>F</em> d’un autre contraste. Cette opération n’est pas justifiée par les seuls résumés disponibles. L’intervalle qui en résultait est retiré.</p>
<h3>Récits hypnotiques, substances et stimulation cérébrale</h3>
<p>Les récits historiques peuvent annoncer des durées très longues. Sans repères externes ni contenu vérifiable, leur rapport à l’horloge reste une déclaration. Les autres études recensées portent sur la reproduction d’intervalles, l’attention ou l’apprentissage&nbsp;: nous conservons leurs résultats dans leur unité propre. Une amélioration de mémoire d’éléments appris ne mesure pas des années de pratique supplémentaires.</p>
<h3>Une incertitude absente reste absente</h3>
<p>L’ancienne synthèse remplaçait parfois une borne statistique manquante par la valeur 1. Une différence non significative devenait alors une preuve d’absence de gain. Ce traitement est retiré. Même des intervalles complets sur des tâches différentes ne permettraient pas de calculer un plafond universel du temps conscient.</p>
<p><strong>Correction.</strong> La borne «&nbsp;vécu par seconde inférieur à 1,09 à 95&nbsp;%&nbsp;» est retirée des résultats et de leur présentation. Sa valeur est désormais <code>null</code>. Nous n’en déduisons aucun écart chiffré à l’objectif d’une vie en une nuit.</p>

""",
}

TEMPS_REVE = {
    'titre': 'Le temps d’un rêve',
    'description': 'Durée déclarée, tâches chronométrées et données DREAM : ce que chaque mesure permet de conclure.',
    'date': '29 septembre 2026',
    'corps': r"""

<h2 id="explication">Explication</h2>
<p><strong>Une vie accélérée est-elle déjà démontrée par ces données&nbsp;? Non.</strong> Les expériences examinées mesurent des jugements de durée ou le temps nécessaire à certaines actions. Elles ne donnent pas une vitesse générale de la conscience.</p>
<p>Dans les rêves lucides étudiés par <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3893623/">Erlacher et ses collègues</a>, des mouvements convenus des yeux délimitent une tâche pendant le sommeil. La marche et la gymnastique prennent davantage de temps qu’à l’éveil. Cela décrit ces tâches dans ces expériences.</p>
<p>Notre réanalyse de la base DREAM compte [[dream_n]] déclarations de durée. Pour [[dream_intervalles]] d’entre elles, un intervalle entre réveils a pu être reconstruit. Aucun récit n’a une borne de durée supérieure à cet intervalle. Mais un rêve ressenti comme deux minutes pourrait avoir occupé une minute à l’intérieur d’un intervalle de trente minutes&nbsp;: notre décompte ne le détecterait pas.</p>
<p>La question d’Aeternam devient donc précise&nbsp;: comment confronter ce qu’une personne dit avoir vécu à des repères enregistrés pendant le rêve&nbsp;? Le <a href="/programme/#temps">programme de calcul</a> étudie cette mesure.</p>
<h2 id="analyse">Analyse détaillée</h2>
<h3>Trois mesures qui ne s’additionnent pas</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Expérience</th><th>Variable observée</th><th>Interprétation</th></tr></thead><tbody>
<tr><td>Dement–Kleitman, 1957</td><td>Choix entre cinq et quinze minutes</td><td>Discrimination de deux durées, dépendante du critère de réponse</td></tr>
<tr><td>Erlacher et al., 2014</td><td>Durée d’une tâche délimitée par signaux oculaires</td><td>Performance temporelle de cette tâche</td></tr>
<tr><td>DREAM, série Tononi</td><td>Classe de durée déclarée au réveil</td><td>Estimation rétrospective, début du rêve inconnu</td></tr>
</tbody></table></div>
<h3>Pourquoi le choix forcé n’identifie pas une accélération</h3>
<p>Dans le modèle log-normal utilisé auparavant, une réponse dépend du rapport entre le critère de décision <em>c</em> et le facteur <em>F</em>. Multiplier les deux par dix ne change aucune probabilité de réponse. Le script vérifie cette invariance. Fixer arbitrairement <em>c</em> permet de calculer un <em>F</em> conditionnel&nbsp;; cela ne mesure pas <em>F</em>. Les effectifs historiques restent documentés comme provenant de sources secondaires, l’article original n’ayant pas été relu.</p>
<h3>Durées des tâches</h3>
<div class="tableau"><table><thead><tr><th>Tâche</th><th>Personnes</th><th>Éveil (s)</th><th>Rêve (s)</th></tr></thead><tbody>
<tr><td>Compter</td><td>5</td><td>50,3</td><td>64,0</td></tr>
<tr><td>Marcher</td><td>7</td><td>37,7</td><td>57,5</td></tr>
<tr><td>Gymnastique</td><td>8</td><td>6,6</td><td>8,1</td></tr>
</tbody></table></div>
<p>Les groupes de comptage et de marche se recouvrent. Nous conservons les moyennes et les tests publiés, sans méta-analyse entre tâches. Une reconstruction des intervalles de différence à partir des tests appariés figure dans le <a href="/programme/#temps">programme</a>.</p>
<h3>Réanalyse DREAM</h3>
<p>Le script vérifie l’empreinte de l’archive puis relie les deux tables par nom d’enregistrement. Les intervalles entre réveils sont reconstruits à partir des heures&nbsp;; un écart supérieur à six heures est traité comme une nouvelle nuit. Cette règle est heuristique. Les déclarations sont groupées en classes&nbsp;: elles ne donnent ni le début ni la durée objective d’une expérience. Les réveils d’une même personne sont dépendants.</p>
<p><strong>Correction méthodologique.</strong> L’ancien «&nbsp;facteur global&nbsp;» de 0,84 et sa borne de 0,92 sont retirés, ainsi que la borne de fréquence tirée des non-détections. Ils agrégeaient des mesures différentes et leur donnaient une portée injustifiée. Les champs correspondants valent désormais <code>null</code>.</p>
<p>Sources&nbsp;: <a href="https://doi.org/10.1038/s41467-025-61945-1">base DREAM</a>, <a href="https://doi.org/10.26180/23306054.v3">série Tononi</a>, <a href="https://doi.org/10.3389/fpsyg.2013.01013">tâches lucides d’Erlacher et al.</a></p>

""",
}

ARTICLE_6 = {
    'titre': 'Le ciel entier dessine-t-il une grille\xa0?',
    'description': 'Les rayons cosmiques les plus énergétiques vus par l’observatoire Pierre Auger au sud et par '
                   'Telescope Array au nord, réunis pour couvrir tout le ciel et confrontés à la trace qu’une '
                   'grille cubique devrait leur laisser.',
    'date': '28 septembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>Non&nbsp;: le ciel entier ne montre aucune trace de grille cubique.</strong> Avec [[t6_resultats_n_evenements]] rayons cosmiques couvrant toute la sphère céleste, [[t6_resultats_p_valeur_l4]]% des ciels simulés sans grille présentent, après la même recherche, un motif cubique au moins aussi marqué que le vrai ciel.</p>
<p>Ce «&nbsp;non&nbsp;» a une portée précise. Il ne dit pas qu’il n’y a pas de grille&nbsp;: il dit qu’un motif cubique fort est exclu. Un excès de flux de plus d’environ [[t6_ntations_borne_analytique_exces_axes_max]]% le long des axes du cube, ou de plus d’environ [[t6_ns_borne_analytique_exces_diagonales_max]]% le long de ses diagonales, dépasse notre borne approximative à 95&nbsp;% dans les orientations étudiées&nbsp;: c’est environ trois fois mieux que le test n° 2. Un contrôle, qui ajoute les événements d’Auger d’énergie plus basse, descend à p = [[t6_variantes_n_maximal_p_valeur_l4]]&nbsp;; nous l’avons suivi jusqu’au bout&nbsp;: il tient pour l’essentiel aux deux excès astrophysiques déjà connus, n’est plus significatif après leur retrait (p = [[t6_ntes_n_maximal_exces_masques_p_valeur_l4]]) et ne se reproduit pas de façon significative sur des événements indépendants (voir l’analyse, § 7).</p>
</section>

<h2 id="explication">Explication</h2>
<p>Si notre monde était calculé par un ordinateur, l’espace serait peut-être découpé en tout petits cubes, comme une image est faite de pixels. Trois physiciens ont remarqué en 2012 qu’un tel découpage laisserait une trace&nbsp;: les particules les plus énergétiques de l’Univers n’arriveraient pas de la même façon de toutes les directions. Certaines directions seraient favorisées, disposées comme les faces ou comme les coins d’un cube.</p>
<p>Le test n° 2 cherchait cette trace dans les [[t6_test2_meme_methode_n_evenements]] particules les plus énergétiques captées par l’observatoire Pierre Auger, en Argentine. Il n’a rien trouvé, mais il avait deux faiblesses&nbsp;: un observatoire de l’hémisphère sud ne voit pas le ciel du grand Nord, et 100 particules ne permettent de voir qu’un motif très fort.</p>
<p>Nous avons donc réuni deux observatoires. Auger, au sud, a publié la liste de ses [[t6_donnees_auger_n_liste]] particules les plus énergétiques, captées de 2004 à 2020. Telescope Array, dans l’Utah, au nord, a publié la liste de ses [[t6_donnees_telescope_array_n]] plus énergétiques, captées de 2008 à 2013. Les deux observatoires ne mesurent pas l’énergie tout à fait de la même façon&nbsp;; leurs équipes ont publié ensemble la règle qui permet de passer d’une échelle à l’autre. Avec cette règle, nous avons retenu dans la liste d’Auger les particules d’énergie comparable à celles de Telescope Array. Il en reste [[t6_resultats_n_auger]], soit [[t6_resultats_n_evenements]] au total, dix fois plus qu’au test n° 2, et cette fois sur tout le ciel.</p>
<p>La méthode est celle du test n° 2. On essaie [[t6_methode_orientations]] positions du cube et l’on garde celle qui colle le mieux aux données. Puis on fabrique [[t6_methode_ciels_isotropes]] faux ciels sans grille, vus par les mêmes observatoires, et l’on refait exactement la même recherche sur chacun. Dans [[t6_resultats_p_valeur_l4]]% d’entre eux, le meilleur cube colle au moins aussi bien que sur le vrai ciel. Le vrai ciel ne se distingue donc pas des faux ciels&nbsp;: aucune grille n’est détectée.</p>
<p>Nous avons ensuite vérifié que ce résultat ne dépend pas de nos choix&nbsp;: autre règle de conversion des énergies, seulement les particules les plus énergétiques, exposition calculée autrement, et ainsi de suite. Un contrôle sort du lot&nbsp;: quand on ajoute toutes les particules d’Auger d’énergie plus basse, un cube semble coller mieux que presque tous les faux ciels. Nous avons cherché pourquoi, sans rien présumer.</p>
<p>On sait que les rayons cosmiques arrivent en surnombre de deux régions du ciel&nbsp;: l’une autour de la galaxie Centaurus A, vue par Auger, l’autre dans le ciel du nord, vue par Telescope Array. Ce sont des sources astronomiques, pas des cubes. Or, déjà dans l’échantillon principal, le cube qui colle le mieux place justement deux de ses coins à une dizaine de degrés de ces deux régions. Quand on retire ces deux régions du ciel, le motif s’affaiblit nettement et n’est plus significatif. Surtout, une vraie grille devrait se retrouver, avec la même orientation, dans des lots de particules différents. Nous avons choisi le meilleur cube sur les seules particules de basse énergie, puis regardé s’il colle aussi aux autres, qui n’ont servi à rien dans ce choix&nbsp;: il colle un peu, mais pas assez pour sortir du hasard, et encore moins une fois les deux régions retirées. Enfin, la prédiction porte sur les particules les plus énergétiques, les moins déviées en chemin&nbsp;; c’est l’inverse qu’on observe, le motif venant des moins énergétiques. Ce contrôle ne montre donc pas une grille, mais surtout ces deux amas de particules, que le cube le plus proche essayait d’attraper.</p>
<p>Ce que ce test montre&nbsp;: là où l’on pouvait regarder, c’est-à-dire sur tout le ciel et avec dix fois plus de particules, il n’y a pas de motif cubique fort. Ce qu’il ne montre pas&nbsp;: qu’il n’y a aucune grille. Un motif faible passerait encore inaperçu, et les champs magnétiques de notre galaxie dévient ces particules en chemin, ce qui brouillerait une partie de la trace.</p>
<h2 id="analyse">Analyse détaillée</h2><p>Les amplitudes annoncées reposent sur une approximation normale, une grille finie d’amplitudes et un balayage fini d’orientations. Les contrôles Monte-Carlo disponibles ne certifient pas une couverture uniforme sur le continuum des paramètres.</p>
<h3>1. La prédiction</h3>
<p>Sur un réseau cubique, tout effet de la grille sur les directions d’arrivée est une fonction de la direction \(\mathbf n\) invariante par le groupe du cube \(O_h\). Les harmoniques sphériques invariantes par \(O_h\) n’existent que pour \(\ell=0,4,6,8,\dots\)&nbsp;: la première anisotropie permise est l’harmonique cubique \(\ell=4\), proportionnelle à \(Q-3/5\), avec</p>
$$Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>Beane, Davoudi et Savage (arXiv:1210.1847) écrivent qu’une simulation sur réseau pourrait se révéler dans les rayons cosmiques de plus haute énergie par une brisure de la symétrie de rotation reflétant la grille. Test principal fixé d’avance&nbsp;: \(\ell=4\)&nbsp;; tests secondaires&nbsp;: \(\ell=6\) et \(\ell=4+6\). Méthode, statistique, orientations et graine sont celles du test n° 2.</p>
<h3>2. Les données</h3>
<p><strong>Sud.</strong> Pierre Auger Collaboration, ApJ 935, 170 (2022)&nbsp;: liste publique complète des [[t6_donnees_auger_n_liste]] événements d’énergie supérieure ou égale à [[t6_donnees_auger_energie_min_liste_eev]]EeV (du 1er janvier 2004 au 31 décembre 2020, zénith jusqu’à 80°), dont [[t6_donnees_auger_n_verticaux_liste]] «&nbsp;verticaux&nbsp;» (zénith \(\lt\) 60°) et les autres «&nbsp;inclinés&nbsp;» (60° à 80°), chiffres identiques à ceux de l’article (sources.md, § 2). Énergie maximale&nbsp;: [[t6_donnees_auger_energie_max_eev]] EeV. Les 100 événements du test n° 2 sont tous dans cette liste (vérifié, sources.md, § 2).</p>
<p><strong>Nord.</strong> Telescope Array Collaboration, ApJL 790, L21 (2014), tableau 1&nbsp;: les [[t6_donnees_telescope_array_n]] événements d’énergie supérieure à [[t6_etalonnage_seuil_ta_eev]]EeV et de zénith \(\lt\) 55°, du 11 mai 2008 au 4 mai 2013, de [[t6_donnees_telescope_array_energie_min_eev]] à [[t6_donnees_telescope_array_energie_max_eev]] EeV, déclinaisons jusqu’à [[t6_nees_telescope_array_declinaison_min_deg]]° vers le sud. C’est la seule liste d’événements de Telescope Array publiée avec leurs coordonnées (sources.md, § 1)&nbsp;; les jeux plus récents utilisés dans les analyses communes Auger-TA ne sont pas publics.</p>
<p>Les empreintes SHA-256 de tous les fichiers sont vérifiées à chaque exécution. La table de Telescope Array étant sous droits de l’éditeur, elle n’est pas redistribuée&nbsp;: le script la télécharge et contrôle l’empreinte du fichier et celle de la liste lue (sources.md, § 3).</p>
<h3>3. Mettre les deux énergies sur la même échelle</h3>
<p>Le groupe de travail commun Auger-TA recale les énergies en comparant les flux dans la bande de ciel vue par les deux observatoires&nbsp;:</p>
$$\frac{E_{\mathrm{Auger}}}{10\ \mathrm{EeV}}=e^{\alpha}\left(\frac{E_{\mathrm{TA}}}{10\ \mathrm{EeV}}\right)^{\beta},$$
<p>avec \(\alpha\) = [[t6_etalonnage_principal_alpha]] et \(\beta\) = [[t6_etalonnage_principal_beta]], valeurs publiées précisément pour cette sélection de Telescope Array (arXiv:2507.10441, p. 3&nbsp;; sources.md, § 5). Le seuil de 57 EeV de Telescope Array équivaut donc à [[t6_etalonnage_seuil_auger_equivalent_eev]] EeV sur l’échelle d’Auger. L’échantillon principal réunit les événements Auger d’au moins cette énergie et les 72 événements TA&nbsp;:</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Lot</th><th>Latitude</th><th>Zénith</th><th>Événements</th></tr></thead>
<tbody>
<tr><td>Auger vertical</td><td>[[t6_methode_lots_0_latitude_deg]]°</td><td>0-60°</td><td>[[t6_resultats_n_auger_verticaux]]</td></tr>
<tr><td>Auger incliné</td><td>[[t6_methode_lots_1_latitude_deg]]°</td><td>60-80°</td><td>[[t6_resultats_n_auger_inclines]]</td></tr>
<tr><td>Telescope Array</td><td>[[t6_methode_lots_2_latitude_deg]]°</td><td>0-55°</td><td>[[t6_resultats_n_ta]]</td></tr>
<tr><td>Total</td><td></td><td></td><td>[[t6_resultats_n_evenements]]</td></tr>
</tbody>
</table></div>
<h3>4. L’exposition, lot par lot</h3>
<p>Un détecteur au sol à la latitude \(a_0\), acceptant les zéniths \(\theta\le\theta_m\), a une exposition uniforme en ascension droite et, en déclinaison \(\delta\) (Sommers, 2001),</p>
$$\omega_{\theta_m}(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>Pour une bande de zénith \([\theta_1,\theta_2]\), \(\omega=\omega_{\theta_2}-\omega_{\theta_1}\). À ces énergies, l’efficacité de détection est totale et l’exposition purement géométrique (arXiv:1404.5890 p. 6 pour TA&nbsp;; code d’exposition d’Auger publié avec les données&nbsp;; sources.md, § 2 et 3).</p>
<p>Chaque lot \(d\) garde son exposition \(\omega_d\) et son nombre d’événements \(N_d\) est tenu fixe dans les simulations&nbsp;: on conditionne sur lui, comme Auger le fait pour ses lots vertical et incliné. Le test ne dépend alors ni des expositions absolues des deux observatoires, ni de l’écart d’échelle d’énergie au-delà du choix des seuils. Auger voit jusqu’à la déclinaison +[[t6_methode_declinaison_max_auger_deg]]°, Telescope Array jusqu’à [[t6_methode_declinaison_min_ta_deg]]°&nbsp;: le ciel entier est couvert (fraction visible [[t6_methode_fraction_du_ciel_visible]], contre [[t6_t2_meme_methode_fraction_du_ciel_visible]]% au test n° 2)&nbsp;; [[t6_ethode_fraction_du_ciel_vue_par_les_deux]]% de la sphère est vue par les deux, [[t6_methode_fraction_du_ciel_vue_par_ta_seul]]% par Telescope Array seul.</p>
<h3>5. La statistique</h3>
<p>Soit \(R\) une orientation de la grille, de lignes \(\mathbf e_k\), et \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). Étendue aux lots&nbsp;:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-\sum_d N_d\,\langle f\rangle_{\omega_d}}{\sqrt{\sum_d N_d\,\mathrm{Var}_{\omega_d} f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>où \(\langle\cdot\rangle_{\omega_d}\) est la moyenne sur un ciel isotrope vu par le lot \(d\), calculée exactement par quadrature de Gauss-Legendre sur les 15 monômes de degré 4. \(T\gt0\) signale un excès le long des axes du cube, \(T\lt0\) le long de ses diagonales. Le maximum porte sur les [[t6_methode_orientations]] orientations du test n° 2 (même graine, [[t6_methode_graine]]). Pour \(\ell=6\)&nbsp;: \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha_6\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\), avec \(\alpha_6=-15/11\) ≈ [[t6_methode_fonction_l6_alpha]], orthogonale à \(\ell=4\)&nbsp;; le test combiné maximise \(T_4^{2}+T_6^{2}\).</p>
<p>La p-valeur, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), vient de n = [[t6_methode_ciels_isotropes]] ciels isotropes tirés lot par lot, soumis à la même maximisation&nbsp;: elle inclut le coût du choix de l’orientation. Sous isotropie, \(Z_4\) a pour médiane [[t6_resultats_seuils_z4_isotrope_0_5]]&nbsp;; il dépasse [[t6_resultats_seuils_z4_isotrope_0_95]] dans 5 % des cas, [[t6_resultats_seuils_z4_isotrope_0_99]] dans 1 % et [[t6_resultats_seuils_z4_isotrope_0_999]] dans 0,1 %.</p>
<h3>6. Résultat</h3>
<div class="tableau"><table class="phrases">
<thead><tr><th>Test</th><th>Statistique observée</th><th>p-valeur</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (principal)</td><td>\(Z_4\) = [[t6_resultats_z4_observe]]</td><td>[[t6_resultats_p_valeur_l4_41]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\) = [[t6_resultats_z6_observe]]</td><td>[[t6_resultats_p_valeur_l6]]</td></tr>
<tr><td>\(\ell=4\) et \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\) = [[t6_resultats_z46_observe]]</td><td>[[t6_resultats_p_valeur_l4_l6]]</td></tr>
</tbody>
</table></div>
<p>Aucun test ne descend sous 0,05. À la meilleure orientation, \(T_4\) = [[t6_resultats_meilleure_orientation_t4]]&nbsp;: l’écart va vers les diagonales. La moyenne de \(Q\) y vaut [[t6_resultats_q_moyen_observe]] contre [[t6_resultats_q_moyen_attendu_isotrope]] attendu, soit [[t6_resultats_ecart_relatif_q]] %. Cette orientation est à [[t6_meilleure_orientation_ecart_au_test2_deg]]° (au groupe du cube près) de la meilleure orientation du test n° 2&nbsp;: la «&nbsp;meilleure grille&nbsp;» n’est pas stable d’un échantillon à l’autre, ce qu’on attend du bruit.</p>
<p>Lot par lot, à cette même orientation&nbsp;: \(T_4\) = [[t6_lot_meilleure_orientation_auger_vertical]] pour Auger vertical, [[t6_lot_meilleure_orientation_auger_inclin]] pour Auger incliné, [[t6_ot_meilleure_orientation_telescope_array]] pour Telescope Array. Ces valeurs sont prises à l’orientation choisie sur l’ensemble&nbsp;: elles ne sont pas des tests indépendants.</p>
<p><strong>D’où vient l’écart&nbsp;?</strong> Dans des cônes de [[t6_methode_rayon_cones_deg]]° autour des huit diagonales de la meilleure orientation, on observe [[t6_ure_orientation_diagonales_observe_total]] événements pour [[t6_ure_orientation_diagonales_attendu_total]] attendus. L’excès se concentre dans deux cônes&nbsp;: [[t6_e_orientation_diagonales_cones_5_observe]] observés pour [[t6_e_orientation_diagonales_cones_5_attendu]] attendus autour de la diagonale pointant vers ([[t6_re_orientation_diagonales_cones_5_ra_deg]]°&nbsp;; [[t6_e_orientation_diagonales_cones_5_dec_deg]]°), à [[t6_gonales_cones_5_distance_centaurus_a_deg]]° de Centaurus A&nbsp;; [[t6_e_orientation_diagonales_cones_3_observe]] pour [[t6_e_orientation_diagonales_cones_3_attendu]] autour de ([[t6_re_orientation_diagonales_cones_3_ra_deg]]°&nbsp;; [[t6_e_orientation_diagonales_cones_3_dec_deg]]°), à [[t6_ales_cones_3_distance_point_chaud_ta_deg]]° du point chaud de Telescope Array. Les six autres diagonales ne montrent rien de tel. Ce sont les deux excès astrophysiques publiés par les collaborations elles-mêmes&nbsp;: autour de Centaurus A, 215 événements observés pour 152,0 attendus dans un cercle de 27° au-dessus de 38 EeV (arXiv:2206.13492 p. 11)&nbsp;; le point chaud de TA, 19 observés pour 4,49 attendus dans un cercle de 20° (arXiv:1404.5890 p. 7).</p>
<h3>7. Contrôles</h3>
<p>Neuf variantes fixées avant le calcul ([[t6_methode_ciels_par_variante]] ciels isotropes chacune), puis quatre ajoutées après coup, et signalées comme telles, pour comprendre la variante «&nbsp;N maximal&nbsp;»&nbsp;:</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Variante</th><th>N</th><th>\(Z_4\)</th><th>p (\(\ell=4\))</th></tr></thead>
<tbody>
<tr><td>Principale</td><td>[[t6_resultats_n_evenements]]</td><td>[[t6_resultats_z4_observe]]</td><td>[[t6_resultats_p_valeur_l4_41]]</td></tr>
<tr><td>Auger seul, même seuil</td><td>[[t6_variantes_auger_seul_n_evenements]]</td><td>[[t6_variantes_auger_seul_z4_observe]]</td><td>[[t6_variantes_auger_seul_p_valeur_l4]]</td></tr>
<tr><td>Plus hautes énergies (Auger ≥ 78 EeV, TA ≥ [[t6_nnage_seuil_ta_equivalent_a_78_eev_auger]] EeV)</td><td>[[t6_variantes_hautes_energies_n_evenements]]</td><td>[[t6_variantes_hautes_energies_z4_observe]]</td><td>[[t6_variantes_hautes_energies_p_valeur_l4]]</td></tr>
<tr><td>Étalonnage ICRC 2021 (seuil Auger [[t6_uils_auger_selon_etalonnage_eev_icrc2021]] EeV)</td><td>[[t6_riantes_etalonnage_icrc2021_n_evenements]]</td><td>[[t6_variantes_etalonnage_icrc2021_z4_observe]]</td><td>[[t6_ariantes_etalonnage_icrc2021_p_valeur_l4]]</td></tr>
<tr><td>Étalonnage ICRC 2025 strict (seuil [[t6_ger_selon_etalonnage_eev_icrc2025_strict]] EeV)</td><td>[[t6_etalonnage_icrc2025_strict_n_evenements]]</td><td>[[t6_es_etalonnage_icrc2025_strict_z4_observe]]</td><td>[[t6_s_etalonnage_icrc2025_strict_p_valeur_l4]]</td></tr>
<tr><td>Exposition Auger d’un seul bloc</td><td>[[t6_variantes_auger_un_bloc_n_evenements]]</td><td>[[t6_variantes_auger_un_bloc_z4_observe]]</td><td>[[t6_variantes_auger_un_bloc_p_valeur_l4]]</td></tr>
<tr><td>Avec l’événement Amaterasu (244 EeV, 2021)</td><td>[[t6_variantes_avec_amaterasu_n_evenements]]</td><td>[[t6_variantes_avec_amaterasu_z4_observe]]</td><td>[[t6_variantes_avec_amaterasu_p_valeur_l4]]</td></tr>
<tr><td>Centaurus A et point chaud TA retirés</td><td>[[t6_variantes_exces_masques_n_evenements]]</td><td>[[t6_variantes_exces_masques_z4_observe]]</td><td>[[t6_variantes_exces_masques_p_valeur_l4]]</td></tr>
<tr><td>Sans correction d’échelle (Auger ≥ 57 EeV)</td><td>[[t6_variantes_sans_correction_n_evenements]]</td><td>[[t6_variantes_sans_correction_z4_observe]]</td><td>[[t6_variantes_sans_correction_p_valeur_l4]]</td></tr>
<tr><td>N maximal (Auger ≥ 32 EeV, TA > 57 EeV)</td><td>[[t6_variantes_n_maximal_n_evenements]]</td><td>[[t6_variantes_n_maximal_z4_observe]]</td><td>[[t6_variantes_n_maximal_p_valeur_l4]]</td></tr>
<tr><td><cite>Après coup&nbsp;:</cite> N maximal, Auger seul</td><td>[[t6_iantes_n_maximal_auger_seul_n_evenements]]</td><td>[[t6_ariantes_n_maximal_auger_seul_z4_observe]]</td><td>[[t6_riantes_n_maximal_auger_seul_p_valeur_l4]]</td></tr>
<tr><td><cite>Après coup&nbsp;:</cite> N maximal, excès retirés</td><td>[[t6_tes_n_maximal_exces_masques_n_evenements]]</td><td>[[t6_antes_n_maximal_exces_masques_z4_observe]]</td><td>[[t6_ntes_n_maximal_exces_masques_p_valeur_l4]]</td></tr>
<tr><td><cite>Après coup&nbsp;:</cite> Auger 32 à 44,88 EeV seul</td><td>[[t6_variantes_auger_32_a_seuil_n_evenements]]</td><td>[[t6_variantes_auger_32_a_seuil_z4_observe]]</td><td>[[t6_variantes_auger_32_a_seuil_p_valeur_l4]]</td></tr>
<tr><td><cite>Après coup&nbsp;:</cite> Auger 32 à 44,88 EeV, excès retirés</td><td>[[t6_er_32_a_seuil_exces_masques_n_evenements]]</td><td>[[t6_uger_32_a_seuil_exces_masques_z4_observe]]</td><td>[[t6_ger_32_a_seuil_exces_masques_p_valeur_l4]]</td></tr>
</tbody>
</table></div>
<p>Deux variantes prévues descendent sous 0,05&nbsp;: «&nbsp;sans correction&nbsp;» ([[t6_variantes_sans_correction_p_valeur_l4]]) et surtout «&nbsp;N maximal&nbsp;» ([[t6_variantes_n_maximal_p_valeur_l4]]). Nous les avons creusées&nbsp;; aucune ne met en cause le verdict.</p>
<ol>
<li><strong>Ce sont des contrôles, pas le test.</strong> Le test principal a été fixé d’avance. Sur neuf variantes prévues, la probabilité qu’au moins une descende à 0,008 par hasard est bornée par \(9\times0{,}008\approx0{,}07\) (Bonferroni)&nbsp;; les variantes, très corrélées entre elles, rendent cette borne prudente sans la rendre fausse.</li>
<li><strong>Le signal vient des énergies les plus basses, et du sud.</strong> Auger seul, dès 32 EeV, donne déjà p = [[t6_riantes_n_maximal_auger_seul_p_valeur_l4]]&nbsp;; les seuls événements Auger de 32 à 44,88 EeV, absents de l’échantillon principal, donnent p = [[t6_variantes_auger_32_a_seuil_p_valeur_l4]]. Aux plus hautes énergies, là où la prédiction de Beane, Davoudi et Savage porte et où les déviations magnétiques sont les plus faibles, rien&nbsp;: p = [[t6_variantes_hautes_energies_p_valeur_l4]]. Une grille donnerait le profil inverse.</li>
<li><strong>Il suit les excès connus.</strong> Centaurus A et le point chaud TA retirés, avec les cercles publiés par les collaborations&nbsp;: «&nbsp;N maximal&nbsp;» remonte à p = [[t6_ntes_n_maximal_exces_masques_p_valeur_l4]], la tranche 32-44,88 EeV à p = [[t6_ger_32_a_seuil_exces_masques_p_valeur_l4]], l’échantillon principal à p = [[t6_variantes_exces_masques_p_valeur_l4]].</li>
<li><strong>Il ne se reproduit pas de façon significative.</strong> Test de reproduction&nbsp;: on choisit la meilleure orientation sur les seuls événements Auger de 32 à 44,88 EeV (\(T_4\) = [[t6_duction_par_energie_sans_masque_t4_choix]]), puis on calcule \(T_4\) à cette orientation fixée dans l’échantillon principal, qui ne partage aucun événement avec eux. À orientation fixée, \(T_4\) suit une loi normale centrée réduite sous isotropie (autotest). On obtient \(T_4\) = [[t6_4_echantillon_principal_meme_orientation]], soit p = [[t6_energie_sans_masque_p_bilaterale_normale]] (bilatéral)&nbsp;: même signe, mais pas significatif. Excès retirés&nbsp;: \(T_4\) = [[t6_4_echantillon_principal_meme_orientation_111]], p = [[t6_ergie_exces_masques_p_bilaterale_normale]]. La faible concordance qui subsiste est compatible avec une même anisotropie astrophysique vue à deux énergies voisines.</li>
<li><strong>Un dipôle n’explique pas tout, et ce n’est pas nécessaire.</strong> Nous avons aussi simulé des ciels portant le dipôle ajusté aux données, plutôt que des ciels isotropes (amplitude [[t6_s_coup_nul_dipolaire_n_maximal_amplitude]] pour «&nbsp;N maximal&nbsp;»)&nbsp;: la p-valeur ne change presque pas, [[t6_olaire_n_maximal_p_valeur_l4_sous_dipole]] ([[t6_olaire_principal_p_valeur_l4_sous_dipole]] pour le test principal). L’anisotropie qui compte ici n’est pas l’anisotropie à grande échelle, mais les excès à échelle intermédiaire de Centaurus A et du point chaud, dont le retrait fait remonter toutes les p-valeurs au-dessus de 0,05.</li>
<li><strong>«&nbsp;Sans correction&nbsp;»</strong> compare Auger au-dessus de 57 EeV de son échelle à TA au-dessus de 57 EeV de la sienne, alors que l’étalonnage commun fait correspondre 57 EeV de TA à [[t6_etalonnage_seuil_auger_equivalent_eev]] EeV d’Auger&nbsp;: le rapport des flux entre le nord et le sud est alors faussé. Avec les trois étalonnages publiés que nous avons testés, p reste entre [[t6_resultats_p_valeur_l4_41]] et [[t6_s_etalonnage_icrc2025_strict_p_valeur_l4]].</li>
</ol>
<p>Bilan&nbsp;: le seul écart notable des contrôles est porté par des événements de plus basse énergie, se concentre près des deux excès astrophysiques connus, s’efface quand on les retire et ne se reproduit pas de façon significative sur un échantillon indépendant. Ce n’est pas la signature d’une grille.</p>
<h3>8. Ce que le test pouvait voir</h3>
<p>On injecte un motif cubique&nbsp;: densité proportionnelle à \(\omega_d(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Le long d’un axe (\(Q=1\)) le flux vaut \(1+\varepsilon\) fois la moyenne&nbsp;; le long d’une diagonale (\(Q=1/3\)), \(1-2\varepsilon/3\). Avec \(\varepsilon\gt0\), l’excès porte sur les axes&nbsp;; avec \(\varepsilon\lt0\), sur les diagonales, et il vaut \(2\lvert\varepsilon\rvert/3\). Limites supérieures à 95 %, trois conventions&nbsp;:</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Convention</th><th>Axes&nbsp;: \(\varepsilon\le\)</th><th>Diagonales&nbsp;: \(\lvert\varepsilon\rvert\le\)</th><th>Test n° 2, même convention (axes / diagonales)</th></tr></thead>
<tbody>
<tr><td>Orientation tirée au hasard pour chaque ciel ([[t6_methode_ciels_par_amplitude]] ciels par amplitude)</td><td>[[t6_95_moyenne_orientations_epsilon_axes_max]]</td><td>[[t6_enne_orientations_epsilon_diagonales_max]]</td><td>[[t6_test2_meme_methode_limite_moyenne_axes]] / [[t6_2_meme_methode_limite_moyenne_diagonales]]</td></tr>
<tr><td>Pire de 16 orientations fixes, dont la moins visible ([[t6_ode_ciels_par_amplitude_orientation_fixe]] ciels par point)</td><td>[[t6_5_pire_orientation_fixe_epsilon_axes_max]]</td><td>[[t6_orientation_fixe_epsilon_diagonales_max]]</td><td>[[t6_2_meme_methode_pire_16_orientations_axes]] / [[t6_methode_pire_16_orientations_diagonales]]</td></tr>
<tr><td>Pire des 20 000 orientations, borne analytique</td><td>[[t6_orientations_borne_analytique_axes_pire]]</td><td>[[t6_tations_borne_analytique_diagonales_pire]]</td><td>[[t6_hode_borne_toutes_orientations_axes_pire]] / [[t6_orne_toutes_orientations_diagonales_pire]]</td></tr>
</tbody>
</table></div>
<p>La borne analytique repose sur \(Z_4\ge\lvert T(R_0)\rvert\)&nbsp;: si le ciel porte le motif à l’orientation \(R_0\), il suffit que \(\lvert T(R_0)\rvert\) dépasse \(Z_4^{\mathrm{obs}}\) avec une probabilité d’au moins 95 %. \(T(R_0)\) est une somme de \(N\) termes indépendants, de loi normale à très bonne approximation, dont la moyenne et la variance sous le signal se calculent exactement&nbsp;:</p>
$$\mathbb E_\varepsilon[f]_d=\frac{\langle f\rangle_{\omega_d}+\varepsilon\,\langle f g\rangle_{\omega_d}}{1+\varepsilon\,\langle g\rangle_{\omega_d}},\qquad g=\frac{5Q(R_0\mathbf n)-3}{2},$$
<p>et de même pour \(\mathbb E_\varepsilon[f^{2}]_d\). La construction ignore le gain du maximum, mais sa couverture utilise une approximation normale&nbsp;: pour chacune des 16 orientations fixes, elle est au-dessus de la limite simulée. Autotest&nbsp;: à \(\varepsilon=0{,}3\) et à une orientation donnée, moyenne analytique [[t6_s_borne_contre_mc_0_3_moyenne_analytique]] contre [[t6_autotests_borne_contre_mc_0_3_moyenne_mc]] simulée.</p>
<p>En flux&nbsp;: <strong>un excès de plus d’environ [[t6_ntations_borne_analytique_exces_axes_max]]% le long des axes, ou de plus d’environ [[t6_ns_borne_analytique_exces_diagonales_max]]% le long des diagonales, dépasse la borne approximative à 95&nbsp;% sur le balayage d’orientations.</strong> Le gain sur le test n° 2 est d’un facteur [[t6_comparaison_gain_pire_orientation_axes]] vers les axes et [[t6_araison_gain_pire_orientation_diagonales]] vers les diagonales, pour [[t6_comparaison_rapport_n]] fois plus d’événements, proche du facteur \(\sqrt{10{,}2}\approx3{,}2\) attendu d’une sensibilité en \(1/\sqrt N\).</p>
<h3>9. Autotests</h3>
<p>Le script vérifie d’abord sa propre chaîne&nbsp;: effectifs et bornes publiés des deux listes&nbsp;; correspondances d’énergie imprimées dans les quatre articles d’étalonnage&nbsp;; invariance de \(Q\) par le groupe du cube et développement polynomial exact&nbsp;; \(\ell=6\) orthogonal à \(\ell=4\)&nbsp;; limites des ciels visibles (Auger +44,8°, TA −15,7°) et somme des bandes vertical et incliné&nbsp;; accord entre quadrature et grands tirages, masques compris&nbsp;; \(T\) centré réduit sous isotropie&nbsp;; moments analytiques égaux au Monte-Carlo&nbsp;; enfin un motif cubique franc injecté sur tout le ciel est détecté et son orientation retrouvée à [[t6_utotests_orientation_retrouvee_ecart_deg]]° près.</p>
<h2 id="limites">Limites</h2>
<ul>
<li>Les rayons cosmiques sont chargés&nbsp;: les champs magnétiques dévient leurs directions, d’autant plus que les noyaux sont lourds. Le motif cherché est large (un axe et une diagonale sont séparés de \(\arccos(1/\sqrt3)\approx54{,}7^\circ\)) et résiste à des déviations modestes, mais une empreinte fixée à la source ou en chemin serait en partie effacée.</li>
<li>Le nord pèse peu&nbsp;: [[t6_resultats_n_ta]] événements TA contre [[t6_resultats_n_auger]] pour Auger. La seule liste de Telescope Array publiée avec coordonnées s’arrête en 2013&nbsp;; les jeux plus riches des analyses communes ne sont pas publics.</li>
<li>L’étalonnage croisé des énergies a une incertitude&nbsp;: chaque observatoire annonce ±14 % (Auger) et ±21 % (TA) sur son échelle absolue (arXiv:2507.10441 p. 3). Les variantes d’étalonnage publiées ne changent pas le résultat&nbsp;; l’absence de toute correction le change (p = [[t6_variantes_sans_correction_p_valeur_l4]]), pour la raison donnée au § 7.</li>
<li>Les anisotropies astrophysiques (excès de Centaurus A et du point chaud TA, et plus généralement toute anisotropie à grande échelle) projettent en partie sur \(\ell=4\) à travers des expositions non uniformes. Le test n’en modélise aucune&nbsp;; il ne les retire que dans les variantes à excès masqués, avec les cercles publiés par les collaborations, non ajustés par nous. Un résultat positif aurait exigé de les exclure&nbsp;; le verdict négatif n’en dépend pas.</li>
<li>Quatre variantes, le test de reproduction et les ciels à dipôle ont été ajoutés après avoir vu la variante «&nbsp;N maximal&nbsp;»&nbsp;; ils servent à l’expliquer, pas à construire le verdict. Le test de reproduction reste faible&nbsp;: l’échantillon principal ne compte que [[t6_resultats_n_evenements]] événements.</li>
<li>L’écart de la variante «&nbsp;N maximal&nbsp;» n’est pas expliqué par un modèle physique complet&nbsp;: nous montrons qu’il suit les excès connus et qu’il ne se reproduit pas, sans modéliser ces excès eux-mêmes.</li>
<li>La grille est supposée fixe par rapport aux étoiles lointaines. Une grille en mouvement ou en rotation par rapport à elles demanderait un autre test.</li>
<li>Aucune probabilité d’être simulés n’est calculée&nbsp;: le test porte sur une signature précise, celle d’une grille cubique.</li>
</ul>
<h2>Sources</h2>
<ul>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, «&nbsp;Constraints on the Universe as a Numerical Simulation&nbsp;», arXiv:1210.1847 (2012).</li>
<li>Pierre Auger Collaboration, «&nbsp;Arrival Directions of Cosmic Rays above 32 EeV from Phase One of the Pierre Auger Observatory&nbsp;», ApJ 935, 170 (2022), arXiv:2206.13492&nbsp;; données DOI 10.5281/zenodo.6504276.</li>
<li>Telescope Array Collaboration, «&nbsp;Indications of Intermediate-Scale Anisotropy of Cosmic Rays with Energy Greater Than 57 EeV in the Northern Sky&nbsp;», ApJL 790, L21 (2014), arXiv:1404.5890.</li>
<li>Telescope Array Collaboration, «&nbsp;An extremely energetic cosmic ray observed by a surface detector array&nbsp;», Science 382, 903 (2023), arXiv:2311.14231&nbsp;; données DOI 10.5281/zenodo.8427755.</li>
<li>A. Gálvez Ureña pour les collaborations Auger et TA, ICRC 2025, arXiv:2507.10441&nbsp;; A. di Matteo et al., ICRC 2021, arXiv:2111.12366&nbsp;; rapport UHECR 2022, arXiv:2302.04502.</li>
<li>P. Sommers, «&nbsp;Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory&nbsp;», Astropart. Phys. 14, 271 (2001), arXiv:astro-ph/0004016.</li>
</ul>
""",
}

# Test n° 5 : le rendu à la demande de l'observateur, face aux expériences d'interférence publiées.
ARTICLE_5 = {
    'titre': 'Le monde attend-il qu’on le regarde\xa0?',
    'description': 'Une simulation économe ne calculerait les détails qu’au moment où un observateur peut les '
                   'connaître. Six expériences d’interférence publiées disent le contraire\xa0: les franges '
                   'disparaissent dès que l’information existe, qu’on la lise ou non.',
    'date': '28 septembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>Non&nbsp;: cette réanalyse ne fournit pas de preuve d’un rendu commandé par un observateur conscient.</strong> Les expériences examinées contraignent la formalisation HR choisie dans notre script. Les chiffres en écarts-types ci-dessous sont des diagnostics conditionnels&nbsp;: erreurs reconstruites, points numérisés et indépendance supposée. Ils ne constituent pas une réfutation universelle de la simulation.</p>
</section>

<h2 id="explication">Explication</h2>
<p>On prête souvent à une simulation l’astuce des jeux vidéo&nbsp;: ne dessiner que ce que le joueur regarde. Nick Bostrom l’évoque dans sa foire aux questions de 2025&nbsp;: certains détails ne seraient «&nbsp;remplis&nbsp;» que lorsque quelqu’un les regarde ou fait une expérience. Des partisans de l’hypothèse, Tom Campbell et trois coauteurs, en ont tiré une prédiction qu’on peut vérifier. Dans l’expérience des deux fentes, une particule envoyée vers deux fentes produit des franges (une alternance de bandes claires et sombres sur l’écran), comme une vague qui passerait par les deux à la fois. Si l’on apprend par quelle fente elle est passée, les franges disparaissent. Selon eux, ce qui compte n’est pas qu’un appareil ait détecté ce passage, mais qu’un observateur puisse le connaître. Tant que l’information n’est ni lue ni enregistrée nulle part, la simulation n’aurait pas eu à la calculer, et les franges devraient rester.</p>
<p>La physique ordinaire dit autre chose&nbsp;: les franges disparaissent dès que la trace du passage existe quelque part dans la nature, même si personne ne la regardera jamais. Les deux idées donnent donc des prédictions opposées dans un cas précis&nbsp;: une trace présente, mais jamais lue.</p>
<p>Ce cas a été réalisé plusieurs fois, sans que ce soit le but des expériences, et les résultats sont publiés. Nous avons relevé les estimations numérisées dans les figures des articles et refait les calculs&nbsp;:</p>
<ul>
<li>à Los Alamos, en 1999, la visibilité des franges a été mesurée avec l’information de passage présente dans la lumière, mais sans aucun instrument pour la lire. Les franges s’effacent exactement comme la physique ordinaire le prévoit, jusqu’à ne garder que [[t5_schwindt1999_v_45deg]] % de leur netteté&nbsp;; le rendu à la demande prévoyait environ [[t5_schwindt1999_v0]]%. Dans une seconde série, l’information a été lue&nbsp;: la quantité lue et la perte des franges non lues s’emboîtent exactement&nbsp;;</li>
<li>au Brésil, en 2002, dans une vraie expérience à deux fentes, la trace du passage était inscrite dans la lumière et personne ne l’analysait&nbsp;: les franges tombent à [[t5_born2002_test_hr_fig3_sur_fig2_rapport_v]]% de leur netteté initiale, comme dans une expérience où l’information est lue ([[t5_kim2000_rapport_v_r03_sur_r01]]%, écart non significatif)&nbsp;;</li>
<li>à Vienne, en 2003 et 2004, de grosses molécules perdent leurs franges parce que des molécules de gaz les heurtent, ou parce qu’elles émettent de la lumière de chaleur. Ces molécules de gaz et cette lumière ne sont détectées par personne et se perdent dans l’appareil. Les franges disparaissent quand même, dans la proportion calculée d’avance.</li>
</ul>
<p>Le résultat est net&nbsp;: la nature se comporte comme si l’information comptait dès qu’elle existe, qu’un observateur puisse la connaître ou non. Il reste une échappatoire&nbsp;: une simulation qui calculerait tout dès qu’une information existe quelque part produirait exactement ce que nous voyons. Mais elle ne ferait alors aucune économie liée à l’observateur, et elle ne se distinguerait en rien de la physique ordinaire. Ce test ne trouve donc aucune trace de simulation.</p>
<h2 id="analyse">Analyse détaillée</h2>
<h3>1. L’hypothèse testée et sa prédiction</h3>
<p>Campbell, Owhadi, Sauvageau et Watkinson (arXiv:1703.00058, § 4) posent que la figure observée est déterminée «&nbsp;by the existence and availability of the which-way data when the pattern is observed&nbsp;», la disponibilité étant définie par l’enregistrement sur un support objectif (§ 4.2). Leur expérience proposée consiste à détecter l’information de chemin sans l’enregistrer&nbsp;: l’écran «&nbsp;should display the wave pattern if the experiment is successful&nbsp;». Nous appelons HR (rendu à la demande) la prédiction suivante&nbsp;: si l’information de chemin n’est ni lue ni enregistrée, la visibilité reste celle de l’interféromètre sans marquage, \(V = V_0\).</p>
<h3>2. La prédiction quantique, sans observateur</h3>
<p>Pour une particule dont les deux chemins sont corrélés à des états \(|M_1\rangle\), \(|M_2\rangle\) d’un marqueur, la mécanique quantique donne, pour des chemins équiprobables et un marqueur pur,</p>
$$V = |\langle M_1|M_2\rangle|, \qquad D = \sqrt{1-|\langle M_1|M_2\rangle|^2},$$
<p>donc \(D^2 + V^2 = 1\), et en général (marqueur mélangé) l’inégalité d’Englert (Phys. Rev. Lett. 77, 2154, 1996)</p>
$$D^2 + V^2 \le 1,$$
<p>où \(D\) est la distinguabilité, c’est-à-dire la meilleure connaissance du chemin qu’une mesure du marqueur <cite>pourrait</cite> fournir. Rien dans ces formules ne dépend de ce qu’on fait du marqueur ensuite&nbsp;: \(V\) est fixée par le recouvrement des états du marqueur, lu ou non. <code>analyse.py</code> vérifie l’inégalité et le cas d’égalité sur 900 états aléatoires, et l’égalité sur 300 marqueurs purs, en dimensions 2, 3 et 5 (autotest). Le texte intégral d’Englert (1996) est payant et n’a pas été lu&nbsp;; l’inégalité est reprise de Schwindt, Kwiat et Englert (1999), éq. (1), où Englert est coauteur.</p>
<h3>3. Données</h3>
<p>Les points de mesure sont relevés par <code>extraire.py</code> dans les dessins vectoriels des PDF arXiv&nbsp;: chaque marqueur y est un objet dont les coordonnées sont exactes, étalonnées sur les graduations (écart maximal d’une graduation à la droite d’étalonnage&nbsp;: [[t5_residu_etalonnage_max_pt_toutes_figures]] pt). Contrôles&nbsp;: pour Schwindt et al., la moyenne des \(V^2+K^2\) relevés vaut [[t5_controle_extraction_moyenne_v2k2_relevee]] contre 0,976 imprimé&nbsp;; pour Walborn et al., les barres d’erreur relevées valent en moyenne, figure par figure, entre [[t5_e_releve_erreur_sur_racine_n_moyenne_min]] et [[t5_e_releve_erreur_sur_racine_n_moyenne_max]] fois \(\sqrt N\), la loi de Poisson attendue pour des comptages. Les incertitudes sur les visibilités ajustées viennent d’un bootstrap paramétrique (300 tirages), multipliées par \(\sqrt{\chi^2/\text{ddl}}\) quand ce rapport dépasse 1.</p>
<h3>4. Test (a)&nbsp;: l’inégalité est-elle respectée&nbsp;?</h3>
<p><strong>Schwindt, Kwiat et Englert (1999), fig. 2.</strong> Photon unique dans un interféromètre de Mach-Zehnder&nbsp;; une lame demi-onde tournée d’un angle \(\theta\) marque le chemin par la polarisation. Sur les sept angles, \(V^2+K^2\) (connaissance \(K\) mesurée dans la base optimale, donc \(K = D\) aux imperfections près) ne dépasse jamais 1&nbsp;: maximum [[t5_schwindt1999_v2_plus_k2_max]], soit [[t5_schwindt1999_z_max_au_dessus_de_1]] écart-type au-dessus de 1 au pire. La prédiction quantique sans observateur, \(V = V_0|\cos 2\theta|\) et \(D = |\sin 2\theta|\) avec \(V_0\) = [[t5_schwindt1999_v0_14]] (visibilité à \(\theta = 0\)), décrit K à [[t5_schwindt1999_ecart_max_k_moins_d_mq]] près et V à [[t5_schwindt1999_ecart_max_v_moins_v_mq]] près&nbsp;; le plus grand écart est la visibilité résiduelle à 45°, que les auteurs attribuent à de légères transformations de polarisation dans les miroirs.</p>
<p><strong>Ma et al. (2013).</strong> Dans le cas d’effacement, \(I^2+V^2\) = [[t5_ma2013_complementarite_fig3_i2_plus_v2]] ± [[t5_ma2013_complementarite_fig3_err]], sous 1&nbsp;; corrigé des facteurs d’imperfection annoncés par les auteurs (\(\eta_I \approx 0{,}97\), \(\eta_V \approx 0{,}95\)), il vaut [[t5_ma2013_complementarite_fig3_corrige_eta]] ± [[t5_013_complementarite_fig3_corrige_eta_err]], c’est-à-dire la saturation prévue.</p>
<p>Réponse au point (a)&nbsp;: oui, toutes les données respectent \(D^2+V^2 \le 1\), et elles suivent la prédiction quantique sans observateur.</p>
<h3>5. Test (b)&nbsp;: information lue contre information jamais lue, sur le même appareil</h3>
<p>Chez Schwindt et al., la visibilité est mesurée analyseur retiré («&nbsp;the polarization analyzer was lowered out of the beam path&nbsp;»)&nbsp;: pendant cette mesure, le marqueur n’est lu par rien ni personne. La connaissance \(K\) est mesurée dans une autre série, analyseur en place&nbsp;: le marqueur est lu. Posons, pour chaque angle \(\theta \gt 0\),</p>
$$Q = \left(\frac{V_{\text{non lu}}}{V_0}\right)^2 + K_{\text{lu}}^2 .$$
<p>La mécanique quantique (marqueur pur) prédit \(Q = 1\)&nbsp;: la perte de visibilité sans lecture est exactement celle qu’impose l’information disponible. HR prédit \(V_{\text{non lu}} = V_0\), donc \(Q = 1 + K^2\), jusqu’à [[t5_schwindt1999_q_attendu_hr_5_21]] à 45°. Mesuré&nbsp;: \(Q\) moyen = [[t5_lu_contre_non_lu_schwindt_q_moyen]] ± [[t5_lu_contre_non_lu_schwindt_q_err]]. Sur les six angles, \(\chi^2_{\text{MQ}}\) = [[t5_schwindt1999_chi2_mq]] pour [[t5_schwindt1999_ddl]] degrés de liberté (\(p\) = [[t5_schwindt1999_p_mq]]), \(\chi^2_{\text{HR}}\) = [[t5_schwindt1999_chi2_hr]], soit un écart formel au modèle HR de [[t5_schwindt1999_sigma_rejet_hr]] σ. À 45° seul, la visibilité non lue vaut [[t5_schwindt1999_v_45deg_27]] au lieu de 0,98, un écart de [[t5_schwindt1999_z_hr_45deg]] écarts-types.</p>
<p>Autre lecture des mêmes points&nbsp;: la fraction de la perte de visibilité prévue par la mécanique quantique qui a lieu sans aucune lecture vaut [[t5_windt1999_fraction_perte_mq_sans_lecture]] ± [[t5_schwindt1999_fraction_err]] (1 pour la mécanique quantique, 0 pour HR). Les valeurs par angle vont de [[t5_schwindt1999_fraction_min_max_0]] à [[t5_schwindt1999_fraction_min_max_1]] et dispersent plus que leurs barres (\(\chi^2\) = [[t5_schwindt1999_fraction_chi2]] pour [[t5_schwindt1999_fraction_ddl]] degrés de liberté)&nbsp;: les très petites barres de \(V\) ne couvrent pas les imperfections de l’optique, à quelques pour cent. Cela ne touche pas la conclusion&nbsp;: l’écart à HR se compte en dizaines de pour cent.</p>
<p>Réponse au point (b)&nbsp;: non, il n’existe aucun écart mesurable entre information lue et information jamais lue&nbsp;; la sensibilité du test est de l’ordre du pour cent.</p>
<h3>6. Information jamais enregistrée&nbsp;: les fentes d’Young de Walborn et al. (2002)</h3>
<p>Photon d’une paire intriquée envoyé sur une vraie double fente (largeur 200 µm, espacement 200 µm, λ = 702,2 nm)&nbsp;; deux lames quart d’onde marquent le chemin par la polarisation. Aux fig. 3 et 7, aucun polariseur n’est placé nulle part&nbsp;: la polarisation n’est ni analysée ni enregistrée, ce qui réalise l’expérience du § 4.2 de Campbell et al. Nous ajustons chaque figure par</p>
$$N(x) = \operatorname{sinc}^2\!\left(\frac{x-x_0}{w}\right)\left[a + b\cos\frac{2\pi x}{\Lambda} + c\sin\frac{2\pi x}{\Lambda}\right], \qquad V = \frac{\sqrt{b^2+c^2}}{a},$$
<p>l’interfrange \(\Lambda\) étant ajusté sur la figure sans marquage puis fixé. L’interfrange ajusté, [[t5_walborn2002_ajustements_fig2_periode_mm]] mm (montage direct) et [[t5_walborn2002_ajustements_fig6_periode_mm]] mm (montage retardé), est celui qu’impose la géométrie publiée, \(\lambda L/d\) = [[t5_walborn2002_periode_attendue_mm]] mm (contrôle automatique).</p>
<div class="tableau"><table class="phrases">
<thead><tr><th>Figure</th><th>Situation</th><th>V</th></tr></thead>
<tbody>
<tr><td>2</td><td>sans marquage</td><td>[[t5_walborn2002_ajustements_fig2_v]] ± [[t5_walborn2002_ajustements_fig2_sv]]</td></tr>
<tr><td>3</td><td>chemin marqué, jamais lu</td><td>[[t5_walborn2002_ajustements_fig3_v]] ± [[t5_walborn2002_ajustements_fig3_sv]]</td></tr>
<tr><td>6</td><td>sans marquage, détection retardée</td><td>[[t5_walborn2002_ajustements_fig6_v]] ± [[t5_walborn2002_ajustements_fig6_sv]]</td></tr>
<tr><td>7</td><td>chemin marqué, jamais lu, retardée</td><td>[[t5_walborn2002_ajustements_fig7_v]] ± [[t5_walborn2002_ajustements_fig7_sv]]</td></tr>
</tbody>
</table></div>
<p>Rapports \(V_{\text{marqué}}/V_{\text{sans marquage}}\)&nbsp;: [[t5_born2002_test_hr_fig3_sur_fig2_rapport_v_47]] ± [[t5_rn2002_test_hr_fig3_sur_fig2_rapport_err]] et [[t5_born2002_test_hr_fig7_sur_fig6_rapport_v]] ± [[t5_rn2002_test_hr_fig7_sur_fig6_rapport_err]]. HR prédit 1&nbsp;: écart formel de [[t5_walborn2002_test_hr_fig3_sur_fig2_z_hr]] σ et [[t5_walborn2002_test_hr_fig7_sur_fig6_z_hr]] σ. Le reste de franges de la fig. 3 est attribué par les auteurs à un léger défaut d’alignement des lames.</p>
<p>Comparaison avec un cas où l’information est lue&nbsp;: chez Kim et al. (2000), les coïncidences avec le détecteur de chemin D3 (R03) gardent un rapport de visibilité de [[t5_kim2000_rapport_v_r03_sur_r01_53]] ± [[t5_kim2000_rapport_err]] par rapport aux franges effacées R01. Moyenne des deux cas non lus de Walborn&nbsp;: [[t5_lu_contre_non_lu_non_lu_walborn]] ± [[t5_lu_contre_non_lu_non_lu_err]]&nbsp;; différence non lu − lu&nbsp;: [[t5_contre_non_lu_difference_non_lu_moins_lu]] ± [[t5_lu_contre_non_lu_difference_err]] ([[t5_lu_contre_non_lu_z_difference]] σ), là où HR prédit 1 (écart formel de [[t5_lu_contre_non_lu_z_hr]] σ). Cette comparaison croise deux expériences différentes&nbsp;; elle confirme le § 5 sans le remplacer.</p>
<h3>7. Information perdue dans l’environnement</h3>
<p><strong>Collisions (Hornberger et al., 2003).</strong> Les molécules de C70 traversent un interféromètre de Talbot-Lau rempli de gaz&nbsp;; chaque collision emporte l’information de chemin dans une molécule de gaz jamais détectée. La mécanique quantique prédit \(V(p) = V_0\,e^{-p/p_0}\), avec \(p_0\) calculé sans paramètre ajustable. Sur les [[t5_hornberger2003_fig2_n_points]] points du méthane (fig. 2), l’ajustement donne \(p_0\) = ([[t5_hornberger2003_fig2_p0_ajuste_1e_6_mbar]] ± [[t5_hornberger2003_fig2_p0_ajuste_err]]) × 10<sup>−6</sup> mbar, contre [[t5_hornberger2003_fig2_p0_theorie_1e_6_mbar]] × 10<sup>−6</sup> mbar pour la droite théorique publiée&nbsp;; cette droite, sans aucun ajustement, donne \(\chi^2\) = [[t5_rnberger2003_fig2_chi2_mq_sans_parametre]] pour [[t5_hornberger2003_fig2_ddl_mq]] points (\(p\) = [[t5_hornberger2003_fig2_p_mq]]). HR (visibilité constante, [[t5_hornberger2003_fig2_v0_hr_pct]] %) est rejetée à [[t5_hornberger2003_fig2_sigma_rejet_hr]] σ&nbsp;; à la plus forte pression, la visibilité n’est plus que [[t5_hornberger2003_fig2_v_derniere_pct]] %. Sur les dix gaz de la fig. 3, les \(p_0\) mesurés valent en moyenne [[t5_03_fig3_rapport_mesure_sur_theorie_moyen]] fois les \(p_0\) calculés, avec \(\chi^2\) = [[t5_hornberger2003_fig3_chi2_mq]] pour [[t5_hornberger2003_fig3_ddl]] gaz (\(p\) = [[t5_hornberger2003_fig3_p_mq]])&nbsp;: l’accord est bon mais pas parfait. Cet écart commun d’environ 10 % reste dans l’incertitude de 15 % sur la mesure de pression, qui est pour l’essentiel commune à tous les gaz (nous l’avons traitée comme indépendante, ce qui gonfle le \(\chi^2\)). HR, qui prédit l’absence de décohérence (\(1/p_0 = 0\)), est rejetée à [[t5_hornberger2003_fig3_sigma_rejet_hr]] σ.</p>
<p><strong>Émission thermique (Hackermüller et al., 2004).</strong> Des molécules chauffées par laser émettent des photons que les parois absorbent&nbsp;; personne ne les détecte. HR prédit une visibilité normalisée égale à 1&nbsp;; au-delà de 7,5 W, elle vaut [[t5_ermuller2004_a_v_norm_moyenne_p_sup_7_5w]] (panneau a) et [[t5_ermuller2004_b_v_norm_moyenne_p_sup_7_5w]] (panneau b), contre [[t5_2004_a_v_norm_theorie_moyenne_p_sup_7_5w]] et [[t5_2004_b_v_norm_theorie_moyenne_p_sup_7_5w]] pour la courbe théorique. Honnêtement, la courbe théorique ne passe pas dans les barres d’erreur&nbsp;: \(\chi^2/\text{ddl}\) = [[t5_hackermuller2004_a_chi2_mq_par_ddl]] et [[t5_hackermuller2004_b_chi2_mq_par_ddl]], écarts jusqu’à [[t5_hackermuller2004_a_ecart_max_mq]] et [[t5_hackermuller2004_b_ecart_max_mq]]. Les auteurs l’attribuent à l’alignement des lasers de chauffage («&nbsp;The difference between the theoretical and the experimental curve is of the order of this variation&nbsp;»). En gonflant les barres jusqu’à ce que la théorie quantique ait \(\chi^2/\text{ddl} = 1\), HR reste rejetée à [[t5_muller2004_a_sigma_rejet_hr_conservateur]] σ et [[t5_muller2004_b_sigma_rejet_hr_conservateur]] σ.</p>
<h3>8. Effacement, choix retardé et ordre temporel</h3>
<p>Ces expériences ne séparent pas HR de la mécanique quantique (toutes les données y sont enregistrées), mais elles vérifient qu’aucun effet ne dépend du moment où l’information est traitée, ce qu’un rendu déclenché à la détection pourrait trahir.</p>
<ul>
<li><strong>Walborn et al.</strong> En plaçant un polariseur sur l’autre photon, on retrouve des franges (fig. 4&nbsp;: [[t5_walborn2002_ajustements_fig4_v]]&nbsp;; fig. 5&nbsp;: [[t5_walborn2002_ajustements_fig5_v]]) déphasées de ([[t5_s_antifranges_fig4_fig5_dephasage_sur_pi]] ± [[t5_franges_antifranges_fig4_fig5_err_sur_pi]]) π&nbsp;; leur somme n’a plus de franges ([[t5_walborn2002_ajustements_fig4_fig5_v]] ± [[t5_walborn2002_ajustements_fig4_fig5_sv]]) et reproduit la fig. 3 (écart [[t5_ements_fig4_fig5_z_contre_figure_marquee]] σ)&nbsp;: ce qu’on fait plus tard sur l’autre photon ne change pas ce qui a été enregistré sur le premier. En détection retardée, la même somme vaut [[t5_walborn2002_ajustements_fig8_fig9_v]] ± [[t5_walborn2002_ajustements_fig8_fig9_sv]] et reproduit la fig. 7 ([[t5_ements_fig8_fig9_z_contre_figure_marquee]] σ). Les visibilités retrouvées en détection directe et retardée diffèrent de [[t5_detections_fig4_contre_fig8_z_difference]] σ (franges) et [[t5_detections_fig5_contre_fig9_z_difference]] σ (anti-franges, plus faibles en retardé).</li>
<li><strong>Kim et al.</strong> L’effacement a lieu au moins 8 ns après la détection du premier photon. Les franges R01 (\(V\) = [[t5_kim2000_ajustements_r01_v]] ± [[t5_kim2000_ajustements_r01_sv]]) et R02 ([[t5_kim2000_ajustements_r02_v]] ± [[t5_kim2000_ajustements_r02_sv]]) sont déphasées de ([[t5_kim2000_dephasage_r01_r02_sur_pi]] ± [[t5_kim2000_dephasage_err_sur_pi]]) π&nbsp;; leur somme est presque plate ([[t5_kim2000_ajustements_r01_r02_v]] ± [[t5_kim2000_ajustements_r01_r02_sv]])&nbsp;; R03 n’a pas de franges ([[t5_kim2000_ajustements_r03_v]] ± [[t5_kim2000_ajustements_r03_sv]]).</li>
<li><strong>Ma et al.</strong>, tableau I (Vienne)&nbsp;: que la projection du photon «&nbsp;environnement&nbsp;» ait lieu avant, en dehors du cône de lumière, ou après le passage du photon «&nbsp;système&nbsp;», la visibilité après effacement est la même&nbsp;: [[t5_ma2013_tableau_i_v_projection_avant]] avant, [[t5_ma2013_tableau_i_v_projection_apres]] après, différence [[t5_3_tableau_i_difference_apres_moins_avant]] ± [[t5_ma2013_tableau_i_difference_err]]&nbsp;; les six scénarios sont homogènes (\(\chi^2\) = [[t5_ma2013_tableau_i_chi2_v]] pour [[t5_ma2013_tableau_i_ddl]] degrés de liberté). Tableau II (Canaries, 144 km)&nbsp;: l’information de chemin est homogène (\(p\) = [[t5_ma2013_tableau_ii_p_i_homogene]]), mais pas la visibilité (\(\chi^2\) = [[t5_ma2013_tableau_ii_chi2_v]] pour [[t5_ma2013_tableau_ii_ddl]] degrés de liberté)&nbsp;: le scénario II’, choix simultané de l’émission, donne 0,776 contre 0,756 et 0,751, un écart de [[t5_3_tableau_ii_z_ecarts_v_par_paire_ii_ii]] σ et [[t5_3_tableau_ii_z_ecarts_v_par_paire_ii_iii]] σ, alors que les deux scénarios où le choix est après (II) et avant (III) ne diffèrent que de [[t5_3_tableau_ii_z_ecarts_v_par_paire_ii_iii_118]] σ. L’article affirme des résultats «&nbsp;similar [...] up to statistical errors&nbsp;»&nbsp;; les chiffres de son propre tableau ne le confirment pas. L’écart n’est pas ordonné selon le moment du choix et porte sur des données dont le bruit de fond a été soustrait&nbsp;; nous ne savons pas l’expliquer à partir de l’article, et il ne correspond à aucune prédiction de HR.</li>
</ul>
<h3>9. Bilan statistique et règle de décision</h3>
<p>Les ajustements sont exploratoires. Le script conserve les diagnostics calculés sous ses hypothèses d’erreur, mais la somme des χ² de panneaux d’une même expérience ne garantit pas leur indépendance. Sans covariances ni modèle des erreurs systématiques de numérisation, nous ne retenons pas les chiffres combinés comme niveau de preuve scientifique. La règle a été modifiée après inspection des résultats&nbsp;: elle n’est pas un protocole confirmatoire préenregistré.</p>
<h3>10. Ce que le test ne peut pas trancher</h3>
<p>Une simulation qui calculerait l’interférence à partir de l’information <cite>physiquement présente</cite>, lue ou non, reproduit la mécanique quantique à l’identique&nbsp;: aucune expérience ne peut la distinguer de l’absence de simulation. C’est d’ailleurs ce que disent Ma et al.&nbsp;: «&nbsp;The presence of path information anywhere in the universe is sufficient to prohibit any possibility of interference. It is irrelevant whether a future observer might decide to acquire it.&nbsp;» Une telle simulation ne réaliserait aucune économie liée à un observateur&nbsp;: elle devrait suivre chaque molécule de gaz et chaque photon perdu dans les parois. La version économe, celle qui justifie l’idée, est réfutée&nbsp;; la version non économe n’est pas testable.</p>
<h2 id="limites">Limites</h2>
<ul>
<li><strong>Pas de données brutes.</strong> Les points viennent des figures publiées, relevées dans les dessins vectoriels&nbsp;; l’imprécision du relevé (au plus [[t5_residu_etalonnage_max_pt_toutes_figures]] pt sur les graduations) est très inférieure aux barres d’erreur, et plusieurs contrôles recoupent les valeurs imprimées dans les textes. Les comptages de Walborn et al. relevés ne tombent pas sur des entiers (écart jusqu’à [[t5_02_controle_releve_ecart_max_a_un_entier]] coup), alors que leurs barres valent bien \(\sqrt N\)&nbsp;: un décalage de l’ordre d’un demi-coup dans le tracé ou l’étalonnage, sans effet sur les visibilités.</li>
<li><strong>L’expérience décisive de Campbell et al. n’est pas réalisée telle quelle.</strong> Aucune des expériences analysées ne détruit un enregistrement avant sa lecture (leur § 4.3) ni ne relie un choix humain au moment de l’observation (§ 4.5). Nous testons leur § 4.2 (information détectée ou présente mais jamais enregistrée), qui en est la version la plus simple. Leurs expériences plus élaborées restent à faire&nbsp;; la mécanique quantique en prédit l’issue sans ambiguïté.</li>
<li><strong>Qu’est-ce qu’«&nbsp;enregistré&nbsp;»&nbsp;?</strong> Un partisan de HR peut soutenir que la polarisation d’un photon, une molécule de gaz ou les parois de l’appareil «&nbsp;enregistrent&nbsp;» l’information. Mais alors la notion d’observateur disparaît et l’hypothèse se confond avec la mécanique quantique (§ 10).</li>
<li><strong>Écarts à la mécanique quantique elle-même.</strong> La théorie publiée décrit mal la forme de la courbe de Hackermüller et al. (\(\chi^2/\text{ddl}\) de 18 à 46)&nbsp;; les \(p_0\) de Hornberger et al. sont environ 10 % sous la théorie&nbsp;; dans l’état mélangé de Schwindt et al., \(V^2+K^2\) mesuré (0,003 ± 0,001) s’écarte de la théorie (0,017 ± 0,003) de [[t5_99_melange_fig3a_z_mesure_contre_theorie]] σ, écart attribué par les auteurs à l’interféromètre vide. Aucun de ces écarts ne va dans le sens de HR&nbsp;: partout, l’interférence est <cite>plus</cite> détruite que HR ne le permet.</li>
<li><strong>Tableau II de Ma et al.</strong> Écart de visibilité inexpliqué entre scénarios (§ 8), rapporté tel quel.</li>
<li><strong>Sources non lues en entier.</strong> Englert (1996) et Dürr, Nonn et Rempe (Nature 1998) sont payants&nbsp;; seuls leur citation par Schwindt et al. et le résumé de Dürr et al. ont été lus, et aucun de leurs chiffres n’est utilisé.</li>
<li><strong>Indépendance.</strong> Les jeux combinés au § 9 viennent d’expériences différentes&nbsp;; à l’intérieur d’un jeu, des erreurs systématiques communes (pression, alignement) ne sont pas modélisées.</li>
</ul>
""",
}

# Audit : les démonstrations publiées du « oui » (Vopson surtout), refaites pas à pas.
AUDIT_1 = {
    'titre': 'Les démonstrations du «\xa0oui\xa0» tiennent-elles\xa0?',
    'description': 'Nous avons refait, pas à pas, les calculs publiés par Melvin Vopson et d’autres pour appuyer '
                   'l’idée que notre Univers est simulé\xa0; aucun ne démontre ce qu’il annonce.',
    'date': '28 septembre 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>Non.</strong> Aucune des démonstrations examinées n’établit que nous vivons dans une simulation&nbsp;: la plus récente repose sur une erreur mathématique vérifiable, la dérivation thermodynamique de 2023 sur une égalité qui ne vaut pas pour les transformations réelles, et sa réparation de 2025 sur des hypothèses non démontrées.</p>
<p>Ce «&nbsp;non&nbsp;» porte sur ces démonstrations, pas sur l’hypothèse elle-même. Qu’un raisonnement échoue ne prouve pas que la simulation est impossible&nbsp;; cela montre seulement que ces articles ne la rendent pas plus probable. Les travaux de Campbell et de Wolpert, souvent cités dans le même sens, ne prétendent d’ailleurs pas l’établir&nbsp;: les premiers proposent des expériences, le second démontre une possibilité logique.</p>
</section>

<h2 id="explication">Explication</h2>
<p>Melvin Vopson, physicien à l’université de Portsmouth, défend depuis 2022 une «&nbsp;seconde loi de l’infodynamique&nbsp;»&nbsp;: dans tout système qui porte de l’information, le désordre de cette information ne pourrait que rester stable ou diminuer. Il y voit la marque d’un univers qui, comme un ordinateur, économise ses ressources, donc un indice en faveur de la simulation. Nous avons repris trois de ses démonstrations.</p>
<p>La première, publiée en mai 2026, veut prouver qu’un système atteint son désordre le plus faible quand toutes ses pièces se répètent le même nombre de fois. C’est l’inverse qui est vrai. Prenons six objets de deux sortes. Trois et trois, c’est la répartition la plus mélangée possible, donc la plus imprévisible&nbsp;; cinq et un, c’est la plus ordonnée, car on devine presque à coup sûr la sorte d’un objet pris au hasard. Le calcul exact le confirme dans chacun des cas que nous avons passés en revue, sans exception. L’article reconnaît d’ailleurs, quelques lignes plus haut, que la répartition égale donne le désordre maximal. Ses exemples de polygones (le carré «&nbsp;plus ordonné&nbsp;» que le quadrilatère quelconque) restent justes, mais pour une autre raison, que nous démontrons, et qui ne dit rien d’une loi générale.</p>
<p>La deuxième, publiée en 2023, part d’un fait admis&nbsp;: l’univers n’échange de chaleur avec rien. Vopson en tirait que son désordre total ne peut pas changer&nbsp;; comme le désordre physique augmente, il fallait qu’autre chose, l’information, compense en diminuant. Or l’absence d’échange de chaleur n’empêche pas le désordre de croître. Un gaz enfermé dans une boîte isolée, qui s’échappe d’un coup dans une moitié vide, ne reçoit ni chaleur ni travail, et pourtant son désordre augmente d’une quantité que tout manuel calcule. Vopson l’a reconnu en 2025.</p>
<p>La troisième est sa réparation de 2025. Elle ajoute des termes de pertes et conclut de nouveau que le désordre de l’information diminue. Mais la conclusion ne sort pas du calcul&nbsp;: elle vient d’hypothèses posées en chemin (les pertes diminuent avec le temps, la température de l’univers est constante), que l’article affirme sans les établir, et dont l’une contredit une phrase du même texte, où la température «&nbsp;doit décroître&nbsp;». Le calcul lui-même, fait correctement, laisse le résultat indéterminé.</p>
<p>Enfin, on lit souvent qu’un univers qui «&nbsp;compresse&nbsp;» l’information trahirait un ordinateur soucieux d’économie. Trois choses différentes se mélangent là. Qu’une quantité diminue n’implique pas qu’il y ait compression. Qu’il existe une compression n’implique pas qu’un calculateur l’ait voulue&nbsp;: une compression parfaite ne change d’ailleurs rien à la quantité d’information transmise, elle l’écrit seulement plus court. Et seule une compression qui perd de l’information la réduit vraiment.</p>
<h2 id="analyse">Analyse détaillée</h2>
<h3>1. Le lemme de Vopson (2026)&nbsp;: un maximum pris pour un minimum</h3>
<p>Vopson (<cite>Entropy</cite> 28, 564, 18 mai 2026, section 2) considère \(N\) éléments répartis en \(n\) catégories de multiplicités \(g_i \ge 1\), avec \(\sum_i g_i = N\) (équation 3), et l’entropie (équation 5)</p>
$$ I(g) = \log_2 N - \frac{1}{N}\sum_{i=1}^{n} g_i \log_2 g_i . $$
<p>C’est exactement l’entropie de Shannon de la loi \(p_i = g_i/N\)&nbsp;: \(I = -\sum_i p_i \log_2 p_i\) (ses équations 2 et 4). Il cherche le minimum de \(I\) à \(N\) fixé, pose \(f = \frac1N\sum g_i \log_2 g_i\) (équation 6), écrit que «&nbsp;le minimum de I est obtenu quand [f] est maximal&nbsp;», puis annule la dérivée du lagrangien \(L = f - \lambda(\sum g_i - N)\) et obtient \(g_i = N/n\) (équation 14). Il conclut&nbsp;: «&nbsp;quand n ≠ 1, l’entropie informationnelle minimale est non nulle et la condition est donnée par (14)&nbsp;», et, dans le résumé comme dans la conclusion, que la configuration d’entropie minimale est celle des multiplicités égales.</p>
<p><strong>Le point stationnaire est un maximum.</strong> Sur l’ensemble admissible \(\{g \in \mathbb{R}_{>0}^n : \sum g_i = N\}\), avec \(N\) constant,</p>
$$ \frac{\partial I}{\partial g_i} = -\frac{1}{N}\left(\log_2 g_i + \frac{1}{\ln 2}\right), \qquad \frac{\partial^2 I}{\partial g_i\,\partial g_j} = -\frac{\delta_{ij}}{N \ln 2 \; g_i}. $$
<p>La hessienne est diagonale à termes strictement négatifs, donc définie négative&nbsp;: pour toute direction admissible \(d \ne 0\) (\(\sum d_i = 0\)), \(d^{\mathsf T} \nabla^2 I \, d = -\sum_i d_i^2/(N\ln 2\, g_i) \lt 0\). \(I\) est strictement concave sur un ensemble convexe&nbsp;; son unique point stationnaire, qui est bien \(g_i = N/n\) (le gradient y est proportionnel à \((1,\dots,1)\), donc orthogonal à la contrainte), est son <strong>maximum global</strong>, qui vaut \(\log_2 n\). La méthode de Lagrange ne distingue pas un maximum d’un minimum&nbsp;; c’est la condition du second ordre qui tranche, et elle n’est pas examinée dans l’article. L’étape «&nbsp;minimum de I ⇔ maximum de f&nbsp;» est juste&nbsp;; l’erreur est de prendre le point stationnaire de \(f\), qui est convexe, pour son maximum, alors que c’est son minimum.</p>
<p>L’article écrit lui-même, dans la même section, que «&nbsp;la maximisation de l’entropie de Shannon pour des lois de probabilité uniformes est un résultat bien établi&nbsp;». Or, à \(N\) et \(n\) fixés, multiplicités égales et loi uniforme sont la même chose&nbsp;: le lemme contredit le résultat que l’article rappelle.</p>
<p><strong>Contre-exemple.</strong> \(N = 6\), \(n = 2\)&nbsp;:</p>
<ul><li>\((3,3)\)&nbsp;: [[i33]] bit&nbsp;;</li><li>\((4,2)\)&nbsp;: [[i42]] bit&nbsp;;</li><li>\((5,1)\)&nbsp;: [[i51]] bit.</li></ul>
<p>La répartition égale donne la plus grande valeur, pas la plus petite.</p>
<p><strong>Énumération exhaustive.</strong> Pour \(N\) de 2 à 15 et \(n\) de 2 à \(\min(5, N)\), soit [[nb_cas]] cas et [[nb_compo]] compositions examinées une à une, le maximum de \(I\) est atteint par la répartition la plus égale \((\lceil N/n\rceil, \dots, \lfloor N/n\rfloor)\) et le minimum par \((N-n+1, 1, \dots, 1)\). Sur les [[nb_non_triv]] cas où toutes les compositions n’ont pas la même entropie, la répartition la plus égale est le maximum dans [[nb_max]] et le minimum dans [[nb_min]]. Le vrai minimum à \(N\) et \(n\) fixés est donc la répartition la plus déséquilibrée&nbsp;; à \(N\) seul fixé, c’est \(n = 1\), \(I = 0\), cas que l’article mentionne à part.</p>
<p><strong>Contrôle numérique de la concavité.</strong> En [[nb_points]] points tirés au hasard (graine fixe), avec des directions admissibles aléatoires, la dérivée seconde par différences finies est toujours négative (la plus grande vaut [[d2_max]]) et s’écarte de la formule analytique d’au plus [[ecart_hess]] en valeur relative.</p>
<h3>2. Les polygones&nbsp;: conclusion juste, raison différente</h3>
<p>La section 3 décrit un polygone à \(m\) sommets par ses \(m\) longueurs et ses \(m\) angles, soit \(N = 2m\) caractères, longueurs et angles restant des caractères distincts (le polygone régulier a «&nbsp;seulement deux caractères distincts, n = 2&nbsp;»). Nous retrouvons ses valeurs&nbsp;: triangle quelconque [[p_tri]] bits, quadrilatère quelconque [[p_quad]] bits, pentagone quelconque [[p_penta]] bits (l’article imprime 3.321, valeur tronquée), polygones réguliers [[p_carre]] bit.</p>
<p>Soit \(K\) l’espèce d’un caractère tiré au hasard (longueur ou angle)&nbsp;: elle vaut «&nbsp;longueur&nbsp;» avec probabilité exactement \(1/2\). Par la règle de chaîne,</p>
$$ I = H(K) + H(X \mid K) = 1 + \tfrac12 H_{\text{côtés}} + \tfrac12 H_{\text{angles}} \;\ge\; 1 \text{ bit}, $$
<p>avec égalité si et seulement si toutes les longueurs sont égales et tous les angles égaux, c’est-à-dire pour le polygone régulier. Le script vérifie l’identité sur neuf formes, dont le triangle isocèle ([[p_iso]] bit), le rectangle et le losange ([[p_rect]] bit).</p>
<p>La contrainte géométrique change donc la portée de l’objection. Elle sauve le résultat de la section 3&nbsp;: parmi les polygones à \(m\) côtés, le régulier a bien l’entropie la plus basse. Mais l’équation (14) n’y est pour rien. Dès que \(n = 2\), la seule répartition géométriquement possible est \((m, m)\)&nbsp;; l’accord avec «&nbsp;\(g_i = N/n\)&nbsp;» est automatique, et ce qui fait baisser l’entropie est la diminution de \(n\) (de 6 à 2 pour le triangle), non l’égalité des multiplicités. Le lemme général de la section 2 reste faux, et le résultat sur les polygones, une propriété de la mesure choisie, ne dit rien d’une tendance physique vers le minimum.</p>
<h3>3. Vopson (2023)&nbsp;: l’égalité \(dS = \delta Q/T\) ne vaut que pour une transformation réversible</h3>
<p>Nous n’avons pas pu lire l’article de 2023 (<cite>AIP Advances</cite> 13, 105308) lui-même&nbsp;: l’éditeur et le dépôt de Portsmouth refusent l’accès automatisé (voir `sources.md`). Sa dérivation est connue par le résumé qu’en donne l’auteur en 2025&nbsp;: l’univers «&nbsp;n’échange de chaleur avec rien&nbsp;»&nbsp;; la relation \(dQ = T\,dS\) a été utilisée&nbsp;; «&nbsp;on en a conclu que dS = 0&nbsp;»&nbsp;; le terme d’entropie manquant serait celui de l’information, d’où \(\partial S_{\text{info}}/\partial t = -\partial S_{\text{phys}}/\partial t \le 0\).</p>
<p>L’inégalité de Clausius donne seulement \(dS \ge \delta Q/T\), avec égalité pour une transformation réversible. <strong>Contre-exemple</strong>&nbsp;: une mole de gaz parfait dans une enceinte rigide et isolée se détend dans le vide jusqu’à doubler son volume. \(Q = 0\), \(W = 0\), donc \(\Delta U = 0\) et la température ne change pas&nbsp;; l’entropie étant une fonction d’état, on la calcule sur le chemin réversible isotherme de mêmes états extrêmes&nbsp;:</p>
$$ \Delta S = n R \ln\frac{V_2}{V_1} = R \ln 2 \quad\text{alors que}\quad \int \frac{\delta Q}{T} = 0 . $$ <p>soit [[ds]]&nbsp;J/K,</p>
<p>avec \(R = k_B N_A\) = [[r_gaz]]&nbsp;J·mol⁻¹·K⁻¹, produit de deux constantes exactes du SI. Les notes du MIT le disent&nbsp;: «&nbsp;l’égalité entre ΔS et dQ/T ne vaut que pour une transformation réversible&nbsp;». Une absence d’échange de chaleur n’impose donc pas une entropie constante, et il n’y a rien à compenser. Vopson l’admet en 2025&nbsp;: sans réversibilité, «&nbsp;on ne peut plus en déduire que dS = 0, ce qui annulerait la nécessité d’introduire l’entropie informationnelle&nbsp;».</p>
<h3>4. La réparation de 2025&nbsp;: un signe qui ne suit pas des équations</h3>
<p>Vopson (<cite>IPI Letters</cite> 3(1), N6-N9, 10 janvier 2025) sépare la chaleur en deux parts, \(dQ_{\text{phys}} + dQ_{\text{info}} = 0\) (équation 5), écrit \(dQ_{\text{phys}} = T dS_{\text{phys}} - dU^{\text{loss}}_{\text{phys}}\) (équation 8), puis «&nbsp;suppose une relation semblable pour le processus informationnel&nbsp;» (équation 9). Il obtient (équation 11)</p>
$$ dS_{\text{info}} = -\,dS_{\text{phys}} + \frac{dU^{\text{loss}}}{T}, \qquad dS_{\text{phys}} \ge 0,\quad dU^{\text{loss}} \ge 0 , $$
<p>la positivité des pertes étant écrite dans l’article («&nbsp;dULoss est une quantité positive&nbsp;»). Quatre points.</p>
<ol><li><strong>Le signe est indéterminé.</strong> Le membre de droite est la différence de deux termes positifs. \(dS_{\text{info}} \le 0\) exige \(dU^{\text{loss}} \le T\,dS_{\text{phys}}\), que rien n’établit. Le script tabule les cas&nbsp;: pour \(dS_{\text{phys}} = 1\) et \(dU^{\text{loss}}/T = 2\), \(dS_{\text{info}}\) = [[ds_info]], positif. Rapportée au temps, (11) donne \(\dot S_{\text{info}} = -\dot S_{\text{phys}} + \dot U^{\text{loss}}/T\), où le taux de pertes \(\dot U^{\text{loss}} \ge 0\) s’oppose à la conclusion.</li><li><strong>L’équation (12) mélange deux opérations.</strong> Les deux premiers termes y sont divisés par \(dt\), le troisième dérivé par \(d/dt\) comme si la perte infinitésimale \(dU^{\text{loss}}\) était une fonction du temps. C’est ce qui fait apparaître, en (13), la variation du taux de pertes au lieu du taux de pertes lui-même.</li><li><strong>Même en admettant (13), la conclusion repose sur des hypothèses.</strong> Le deuxième terme n’est négatif que si «&nbsp;la perte diminue avec le temps&nbsp;», ce qui est posé, pas démontré. Le troisième est positif (\(T\) décroît)&nbsp;; l’argument selon lequel il «&nbsp;ne peut compenser&nbsp;» car il «&nbsp;varie en 1/T²&nbsp;» ne compare pas des grandeurs&nbsp;: le rapport du troisième au deuxième terme vaut \(-\,dU^{\text{loss}}\,\dot T / (T\, \tfrac{d}{dt}dU^{\text{loss}})\), qui dépend des taux et non d’une puissance de \(T\). Enfin, l’hypothèse «&nbsp;T = constante&nbsp;» contredit la phrase précédente du même texte («&nbsp;T doit décroître avec le temps&nbsp;») et n’est justifiée par aucun calcul.</li><li><strong>Le terme informationnel est postulé.</strong> Ni \(Q_{\text{info}}\), ni \(S_{\text{info}}\) de l’univers, ni \(U^{\text{loss}}_{\text{info}}\) ne reçoivent de définition indépendante ou de mesure&nbsp;; l’équation (9) est une hypothèse, annoncée comme telle.</li></ol>
<p>La phrase finale, «&nbsp;la seconde loi de l’infodynamique se déduit à l’identique, que le processus soit réversible ou irréversible&nbsp;», n’est donc pas démontrée par l’article.</p>
<h3>5. Compression&nbsp;: trois affirmations à ne pas confondre</h3>
<p>Source à quatre symboles de probabilités \(1/2, 1/4, 1/8, 1/8\)&nbsp;: entropie \(H\) = [[h_src]] bit. Le code préfixe \(0, 10, 110, 111\) est injectif et décodable sans ambiguïté&nbsp;; nous calculons l’entropie <strong>sur la loi des mots de code réellement émis</strong> (le script du tiers dont nous sommes partis recopiait l’entropie d’entrée, ce qui aurait masqué une perte)&nbsp;: [[h_code]] bit. Sur les [[nb_msg]] messages de trois symboles, l’entropie est de [[h_msg]] bits avant comme après codage. Une application injective conserve les probabilités, donc l’entropie des messages complets.</p>
<p>Ce qui change, c’est la longueur&nbsp;: [[l_pref]] bit par symbole au lieu de [[l_fixe]] pour un code de longueur fixe. L’entropie <strong>par bit émis</strong> augmente même, de [[hb_fixe]] à [[hb_pref]]&nbsp;: dans le flux compressé, 0 et 1 sont équiprobables (fréquence des 1&nbsp;: 1/2). Compresser sans perte n’abaisse donc pas l’entropie de l’information&nbsp;; cela la rend plus dense.</p>
<p>Seul un codage non injectif la réduit. En confondant les deux symboles rares (\(c, d \mapsto 11\)), l’entropie de la sortie tombe à [[h_perte]] bit, et [[info_perdue]] bit d’information est définitivement perdu&nbsp;: on ne sait plus lequel des deux a été émis.</p>
<p>D’où trois affirmations distinctes&nbsp;:</p>
<ol><li><strong>une quantité informationnelle diminue</strong>&nbsp;: fait mesurable, qui demande une définition de la quantité et une mesure&nbsp;;</li><li><strong>il existe une compression</strong>&nbsp;: propriété d’un codage, qui n’implique pas la précédente (sans perte, l’entropie des messages est conservée)&nbsp;;</li><li><strong>un simulateur optimise son calcul</strong>&nbsp;: hypothèse sur une cause, qui n’est impliquée ni par 1 ni par 2. Pour qu’une observation la favorise, il faudrait montrer qu’elle est plus probable avec un simulateur que sans&nbsp;; aucun des articles examinés ne calcule ce rapport.</li></ol>
<h3>6. Campbell et al., Wolpert&nbsp;: ce qu’ils affirment réellement</h3>
<p>Campbell, Owhadi, Sauvageau et Watkinson («&nbsp;On testing the simulation theory&nbsp;», arXiv:1703.00058, 2017) «&nbsp;décrivent des expériences conceptuelles de dualité onde-corpuscule destinées à tester la théorie de la simulation&nbsp;», sous l’hypothèse qu’un simulateur aux ressources finies ne «&nbsp;rendrait&nbsp;» le réel qu’au moment de l’observation. Ils écrivent&nbsp;: «&nbsp;nous ne pouvons pas prédire le résultat des expériences proposées&nbsp;». Ce sont des protocoles, pas des résultats&nbsp;; nous n’avons trouvé aucun résultat de ces expériences publié avec comité de lecture.</p>
<p>Wolpert («&nbsp;Implications of computer science theory for the simulation hypothesis&nbsp;», arXiv:2404.16050, version 5 du 19 mars 2026) démontre, par le second théorème de récursion de Kleene, qu’il est «&nbsp;mathématiquement possible&nbsp;» que nous soyons une simulation, y compris exécutée par nous-mêmes. Il précise ne s’intéresser qu’à «&nbsp;la possibilité logique&nbsp;» d’un tel système, sans examiner s’il en existe un «&nbsp;dans notre univers&nbsp;». Un résultat de possibilité n’est pas un indice.</p>
<h2 id="limites">Limites</h2>
<ul><li>Le texte intégral de Vopson (2023) n’a pas été lu&nbsp;: sa dérivation est connue par le résumé qu’en fait l’auteur en 2025&nbsp;; la numérotation «&nbsp;section V&nbsp;» n’est pas vérifiée par nous.</li><li>Nous n’avons examiné que trois démonstrations de Vopson&nbsp;; ses autres arguments (données numériques, génomes, règles de Hund, gravité) ne sont pas audités ici, et l’erreur de 2026 ne les invalide pas à elle seule.</li><li>L’énumération couvre un domaine fini&nbsp;; la validité générale vient de la preuve de concavité, que l’énumération et le contrôle numérique ne font qu’illustrer.</li><li>La détente libre est un modèle de gaz parfait, pas un modèle cosmologique&nbsp;: elle suffit à réfuter l’implication générale «&nbsp;Q = 0 ⇒ ΔS = 0&nbsp;», pas à décrire l’entropie de l’univers.</li><li>Nous n’avons pas vérifié la parution en revue des travaux de Campbell et al. et de Wolpert, lus en préprint.</li><li>Réfuter une démonstration n’établit pas le contraire de sa conclusion&nbsp;: une simulation reste possible, comme le montre Wolpert, et aucun de ces calculs ne peut l’exclure.</li></ul>
""",
}

# Rubriques du blog. Un même article peut appartenir à plusieurs sujets.
REVE_RECIT = {
    'titre': 'Rêve et souvenir : comparer ce qui est signalé et ce qui est raconté',
    'description': 'Audit de huit sources, recalcul d’un tableau individuel et plan d’analyse pour comparer les jugements de durée pendant le rêve et après le réveil.',
    'date': '8 octobre 2026',
    'corps': r"""
<h2>Explication</h2>
<p>Quand une personne raconte un rêve qui lui a semblé très long, à quel moment cette impression s’est-elle formée ? Pour avancer, nous avons cherché des données permettant de comparer ce qu’elle signale pendant le sommeil et ce qu’elle rapporte au réveil, à propos du même intervalle.</p>
<p>Nous avons examiné [[rr_candidats]] sources ou jeux candidats, inspecté les métadonnées ouvertes de DREAM et recalculé un tableau individuel publié en 2026. <strong>Aucun jeu directement exploitable pour comparer deux jugements de durée appariés n’a été récupéré dans ce corpus.</strong> L’effet recherché reste inconnu. Notre contribution est un bilan d’accès, un contrôle des dénominateurs et une méthode exécutable pour une future réanalyse.</p>

<h3>Une réponse pendant le rêve peut différer du souvenir</h3>
<p><a href="https://doi.org/10.1016/j.cub.2021.01.026">Konkoly et ses collègues (2021)</a> décrivent des échanges enregistrés pendant le sommeil dont certains détails sont oubliés ou rapportés différemment après le réveil. Cela justifie de comparer les deux moments. Ces observations ne quantifient pas une accélération du vécu. Une <a href="https://pubmed.ncbi.nlm.nih.gov/15336243/">étude de Conduit et ses collègues (2004)</a> comparait déjà une réponse oculaire à un son et son rappel ultérieur.</p>

<h3>Beaucoup de signaux peuvent venir de peu de personnes</h3>
<p>Dans le tableau de <a href="https://doi.org/10.1162/JOCN.a.107">Konkoly et ses collègues (2026)</a>, [[rr_signaux]] signaux proviennent de [[rr_personnes_signaux]] des [[rr_personnes]] personnes répertoriées. Les deux personnes les plus contributrices en fournissent [[rr_top2]], soit [[rr_part_top2]] %. Ce recalcul descriptif explique pourquoi notre futur contraste sera d’abord calculé par personne.</p>
<figure class="figure-scientifique">
<img src="/fichiers/reve-recit/signaux-par-personne.svg" width="640" height="580" loading="lazy" alt="Répartition de 150 signaux entre 13 lignes du tableau publié : les deux plus grands comptes sont 57 et 45 ; deux personnes n’ont produit aucun signal.">
<figcaption>Décomptes du tableau 1, page 367. L’ordre des lignes source fournit les identifiants P01 à P13. Les nombres de sessions diffèrent ; ce graphique ne compare pas les aptitudes des personnes.</figcaption>
</figure>

<h3>La comparaison proposée</h3>
<p>Il faut un intervalle délimité, puis deux questions comparables portant sur cet intervalle : une réponse donnée pendant le sommeil, et une réponse après le réveil, avant tout retour sur la première réponse ou sur la durée mesurée. Une durée racontée pour toute une histoire ne sera pas comparée à la durée d’une seule tâche.</p>
<p>Un écart indiquerait que le jugement a changé entre les deux rapports. Il ne permettrait pas, à lui seul, de déterminer quand ce changement s’est produit ni d’en attribuer toute la cause à la mémoire. Le fait de répondre, le changement d’état et les difficultés de communication peuvent aussi intervenir.</p>

<h2>Analyse détaillée</h2>
<h3>1. Ce que les sources permettent effectivement d’analyser</h3>
<p>La recherche est ciblée, sans prétention d’exhaustivité. Un jeu non récupéré n’est pas déclaré inexistant. Les déclarations d’accès ci-dessous ont été vérifiées le 8 octobre 2026.</p>
<div class="tableau"><table>
<thead><tr><th>Source ou jeu</th><th>Apport et limite pour cette question</th></tr></thead>
<tbody>
<tr><td>Conduit 2004 ; Erlacher 2014</td><td>Rappel d’événements ou durées de tâches. Aucune paire individuelle de jugements de durée pendant/après récupérée.</td></tr>
<tr><td>Konkoly 2021 et 2026</td><td>Communication pendant le rêve ; données individuelles sur demande ou sous restriction. Tableau de décomptes accessible en 2026.</td></tr>
<tr><td>DREAM / Tononi</td><td>Métadonnées ouvertes : [[rr_dream_lignes]] réveils de [[rr_dream_personnes]] personnes. Classes de durée après réveil ; absence de jugement pendant le sommeil dans ces tables.</td></tr>
<tr><td>Donders 2022</td><td>Dépôt annonçant une publication en préparation ; fichiers nécessaires non disponibles dans la racine examinée.</td></tr>
<tr><td>DreamViews, prépublication 2026</td><td>Récits de forum ; aucun enregistrement physiologique apparié dans la définition du corpus.</td></tr>
<tr><td>MÖBIUS, 2026</td><td>Modèle de confusion rêve/mémoire proposé ; données cliniques individuelles sous restrictions.</td></tr>
</tbody></table></div>
<p>L’archive <a href="https://doi.org/10.26180/23306054.v3">Tononi Serial Awakenings</a> a été contrôlée par son empreinte et les clés communes de ses tables. L’intervalle entre deux réveils ne donne pas le début de l’expérience rapportée. Les classes ordinales restent des classes ; nous ne leur attribuons pas un nombre de secondes arbitraire.</p>
<p>Le <a href="https://github.com/Niloy333/Donders-2022">dépôt Donders</a>, le <a href="https://arxiv.org/abs/2603.26992">corpus DreamViews</a> et le <a href="https://www.nature.com/articles/s42003-026-09781-x">modèle MÖBIUS</a> répondent à d’autres questions utiles. Leur existence ne remplit pas les champs manquants de notre comparaison. Aucun contact, aucune nouvelle collecte et aucune réanalyse EEG n’ont été réalisés dans cette étude.</p>

<h3>2. Un contraste entre rapports, avec un poids égal par personne</h3>
<p>Pour un épisode admissible, notons \(P_{ij}\) l’estimation pendant le rêve et \(A_{ij}\) celle après le réveil, exprimées dans la même unité. Le plan propose :</p>
$$d_{ij}=\log(A_{ij}/P_{ij}),\qquad d_i=\frac{1}{n_i}\sum_j d_{ij},\qquad D=\frac{1}{N}\sum_i d_i.$$
<p>Le rapport géométrique \(e^D\) exprime le changement de jugement moyen selon cette pondération. Une personne produisant beaucoup de réponses ne reçoit pas davantage de poids. L’incertitude est estimée par rééchantillonnage des personnes entières ; les épisodes d’une personne restent groupés.</p>
<p>Le logiciel conserve toutes les tentatives et leurs motifs de non-admissibilité. Il refuse les doublons, les chronologies impossibles et les durées non positives ; il écarte du contraste principal les intervalles ou questions différents, les signaux non vérifiés et les réponses recueillies après retour d’information. Une absence de rappel reste distincte d’un jugement de durée nulle.</p>
<p>Le plan retient un rapport au réveil dans les deux minutes, convention opérationnelle sans prétention biologique. Il prévoit un bootstrap de [[rr_bootstrap]] répétitions et ne produit pas d’intervalle avant [[rr_min_personnes]] personnes admissibles. Ce seuil ne garantit pas la qualité de l’inférence. Une analyse retirant chaque personne à tour de rôle mesure la dépendance du résultat à un seul participant.</p>
<p>Ce plan est proposé pour une réanalyse de données appropriées. Il est enregistré après lecture des articles et avant toute acquisition de paires dans ce dossier ; <strong>il n’est pas préenregistré auprès d’un registre indépendant</strong>. Le tableau publié a, lui, fait l’objet d’une réanalyse exploratoire.</p>

<h3>3. Pourquoi même deux rapports ne donnent pas une vitesse de conscience</h3>
<p>Considérons un modèle de mesure purement illustratif. Pour une durée physique \(T\), un facteur latent hypothétique \(F\) et deux biais de rapport \(B_P\) et \(B_A\), écrivons :</p>
$$P=T F B_P,\qquad A=T F B_A,\qquad \frac{A}{P}=\frac{B_A}{B_P}.$$
<p>Le calcul construit deux scénarios donnant exactement les mêmes observations : pour [[rr_ex_t]] secondes physiques, une réponse de [[rr_ex_p]] secondes pendant le rêve et de [[rr_ex_a]] secondes après. Dans le premier scénario, \(F=1\), \(B_P=1\), \(B_A=2\). Dans le second, \(F=2\), \(B_P=1/2\), \(B_A=1\). Les observations ne départagent pas les deux valeurs de \(F\).</p>
<p>Il s’agit d’un contre-exemple algébrique, sans participant ni modèle neuronal validé. Il montre les hypothèses supplémentaires nécessaires avant d’interpréter un rapport comme une durée consciente absolue. Des contrôles à l’éveil pourraient étudier certains biais de réponse, sans garantir qu’ils restent identiques pendant le sommeil.</p>

<h3>4. Résultat présent et prochaine preuve nécessaire</h3>
<p>Le contrôle du tableau confirme ses totaux ; la concentration de [[rr_part_top2]] % est descriptive. Les formules et le traitement des données manquantes ont été éprouvés sur des cas artificiels, avec vérification numérique séparée. <strong>Le nombre de paires humaines analysées est [[rr_paires]] et l’effet principal reste non estimé.</strong> Cette absence de données n’est pas une preuve d’absence de changement.</p>
<p>La prochaine étape empirique exige un jeu documentant les deux rapports du même intervalle, les consignes, les horodatages et les tentatives sans réponse. Il faudra ensuite confronter le résultat à d’autres personnes ou séances. Un résultat compatible avec zéro ne démontrerait pas non plus l’équivalence des deux rapports sans marge pertinente définie à l’avance.</p>
<p>Cette étude prolonge le <a href="/programme/">carnet sur le rêve, le temps et la mémoire</a>. Elle précise une mesure réalisable en principe et ses limites d’interprétation. Aucun résultat ici ne relie la durée ressentie à la <a href="/gravitation-horloges/">dilatation gravitationnelle des horloges</a> ni à une hypothèse sur l’origine de l’Univers.</p>
""",
}

EINSTEIN_RESTREINTE = {
    'titre': 'Einstein : pourquoi les vitesses et les durées dépendent de l’observateur',
    'description': 'Relativité restreinte, addition des vitesses, lumière et paradoxe des jumeaux : explication, calculs et limites.',
    'date': '8 octobre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>Deux personnes qui suivent des trajectoires différentes peuvent accumuler des durées différentes avant de se retrouver.</strong> Chacune voit pourtant sa propre montre fonctionner normalement. Ce décalage concerne les processus physiques locaux, pas seulement une illusion produite par les signaux lumineux.</p>
<p>Voici un scénario idéalisé. Une personne reste dans un référentiel que nous appellerons « terrestre ». Une autre part puis revient à 80 % de la vitesse de la lumière ; nous négligeons les phases de manœuvre et la gravitation. Entre le départ et les retrouvailles, la première compte 50 ans et la seconde [[voyage_80]] ans. Les mêmes deux événements encadrent deux durées propres différentes. Ce calcul ne décrit aucune technologie de voyage disponible.</p>
<h3 id="vitesses">Pourquoi deux grandes vitesses ne dépassent-elles pas celle de la lumière ?</h3>
<p>Un vaisseau avance à 90 % de la vitesse de la lumière par rapport à la Terre. Il lance vers l’avant un objet à 90 % de cette vitesse, <em>mesurés depuis le vaisseau</em>. La Terre mesure [[addition_90]] % de la vitesse de la lumière pour l’objet. Les vitesses se composent bien, mais la règle ordinaire « 90 + 90 » ne convient plus.</p>
<p>Cette différence implique bien l’espace et le temps, ainsi que la <strong>relativité de la simultanéité</strong> : les observateurs ne donnent pas les mêmes coordonnées de temps et d’espace aux événements éloignés. Ce qui est simultané pour l’un peut ne pas l’être pour l’autre. Distances, durées et synchronisation doivent être transformées ensemble. Il ne s’agit pas d’un espace qui se dilaterait matériellement pour freiner l’objet.</p>
<p>Si le vaisseau allume une lampe, il mesure la lumière dans le vide à la vitesse c, et la Terre aussi. Il n’existe pas de référentiel au repos avec un photon dans lequel on pourrait recommencer la comparaison. Ces règles remontent à la <a href="https://doi.org/10.1002/andp.19053221004">relativité restreinte d’Einstein, publiée en 1905</a>.</p>
<h3>Pourquoi ce n’est pas un simple effet de perspective</h3>
<p>Un objet qui s’éloigne peut nous paraître ralenti parce que ses signaux arrivent de plus en plus tard. Cet effet Doppler et le temps de propagation doivent être distingués de la durée réellement indiquée par sa montre. Dans le scénario des retrouvailles, les deux montres sont réunies au même endroit : la différence demeure.</p>
<p>Le phénomène ne repose pas seulement sur une expérience de pensée. <a href="https://doi.org/10.1126/science.1192720">Chou et ses collègues, en 2010</a>, ont comparé des horloges optiques et mesuré des changements de rythme dus au mouvement à des vitesses inférieures à dix mètres par seconde. L’effet est alors extrêmement petit.</p>

<h2 id="analyse">Analyse détaillée</h2>
<h3>La durée propre et les transformations de Lorentz</h3>
<p>Dans un espace-temps plat, pour une trajectoire de vitesse v(t) dans un référentiel inertiel :</p>
$$\Delta\tau=\int\sqrt{1-\frac{v(t)^2}{c^2}}\,dt.$$
<p>À vitesse constante, cela devient \(\Delta\tau=\Delta t/\gamma\), avec \(\gamma=(1-v^2/c^2)^{-1/2}\). La relativité restreinte peut aussi traiter des trajectoires accélérées dans un espace-temps plat : « restreinte » ne veut pas dire que toute accélération est interdite.</p>
<table class="phrases"><caption>Voyage aller-retour idéalisé : 50 ans dans le référentiel terrestre, manœuvres négligées.</caption><thead><tr><th>Vitesse pendant les trajets</th><th>Durée du voyageur</th></tr></thead><tbody>
<tr><td>80 % de c</td><td>[[voyage_80]] ans</td></tr>
<tr><td>90 % de c</td><td>[[voyage_90]] ans</td></tr>
<tr><td>99 % de c</td><td>[[voyage_99]] ans</td></tr>
<tr><td>99,9 % de c</td><td>[[voyage_999]] ans</td></tr>
</tbody></table>
<p>Les valeurs sont calculées ici, sans mesure humaine. Le demi-tour rend les deux histoires différentes ; on ne peut pas permuter les rôles en conservant un unique référentiel inertiel pour le voyageur. L’écart total se calcule le long des trajectoires. L’accélération n’est pas une substance qui abîmerait l’horloge et produirait à elle seule tout le décalage.</p>
<p>Pour deux référentiels en mouvement relatif v suivant x, la transformation inverse donne :</p>
$$dx=\gamma(dx'+v\,dt'),\qquad dt=\gamma\left(dt'+\frac{v\,dx'}{c^2}\right).$$
<p>Diviser les deux expressions, avec \(u'=dx'/dt'\), fournit la composition colinéaire :</p>
$$u=\frac{u'+v}{1+u'v/c^2}.$$
<p>Pour \(u'=v=0{,}9c\), on obtient \(u/c=1{,}8/1{,}81\). Pour \(u'=c\) et \(|v|\lt c\), le résultat est exactement c. À faibles vitesses, le dénominateur est très proche de un : l’addition quotidienne constitue une excellente approximation.</p>
<h3>Deux objets peuvent pourtant se rapprocher à 1,8 c</h3>
<p>Si deux objets ont chacun une vitesse de 0,9 c en sens opposés <em>dans le même référentiel terrestre</em>, leur distance diminue à 1,8 c dans ces coordonnées. Ce taux de rapprochement n’est la vitesse d’aucun objet dans le référentiel de l’autre. Cette dernière s’obtient par la transformation relativiste et reste inférieure à c.</p>
<h3>Énergie et limite de vitesse</h3>
<p>Pour un objet de masse au repos non nulle, \(E=\gamma mc^2\). Son énergie augmente sans borne quand sa vitesse tend vers c. L’énergie au repos \(E_0=mc^2\) est un cas particulier de la relation \(E^2=p^2c^2+m^2c^4\). Les photons, dont la masse au repos est nulle, ne sont pas des objets massifs accélérés jusqu’à c.</p>
<h3 id="limites">Ce que cette théorie ne résout pas</h3>
<p>La relativité restreinte décrit la physique sur une géométrie plate. Elle ne fournit pas la dynamique d’un champ gravitationnel général : c’est le rôle de la relativité générale. Elle ne détermine pas non plus la sensation subjective du temps. Elle est compatible avec la théorie quantique des champs ; le problème de gravitation quantique ne doit donc pas être présenté comme une contradiction générale entre « Einstein » et « le quantique ».</p>
<p>Ses validations expérimentales ne signifient pas que toute extrapolation à toute énergie imaginable est démontrée. Une éventuelle nouvelle théorie devra expliquer pourquoi les résultats déjà mesurés sont retrouvés dans leur domaine de validité.</p>
<p>Suite : <a href="/gravitation-horloges/">la gravitation, les horloges à un centimètre du sol et le temps près des trous noirs</a>.</p>
""",
}

GRAVITATION_HORLOGES = {
    'titre': 'Vieillit-on moins vite près d’un trou noir et au centre de la Terre ?',
    'description': 'De l’horloge surélevée d’un centimètre au centre terrestre et aux trous noirs : potentiel, durées propres, calculs et conditions.',
    'date': '8 octobre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>Oui, dans des comparaisons bien définies, une horloge plus profondément située dans un puits gravitationnel accumule moins de temps.</strong> Près de la Terre, l’écart est minuscule. Près de l’horizon d’un trou noir, il peut devenir très grand. Il faut toujours préciser les deux positions et les trajectoires comparées.</p>
<ol>
<li>On compare deux horloges identiques, en tenant compte de l’acheminement de leurs signaux.</li>
<li>On place l’une plus haut que l’autre et on les maintient à des positions fixes.</li>
<li>Dans le cas terrestre ordinaire, l’horloge la plus haute prend progressivement de l’avance.</li>
</ol>
<p>Une personne accompagnant chaque horloge ressentirait normalement son propre temps. À conditions biologiques comparables, moins de durée propre signifie moins de temps disponible pour les processus du corps. Cela n’est ni un rajeunissement ni une sensation locale de ralenti. Le vieillissement biologique dépend aussi du milieu ; les calculs ci-dessous comparent d’abord des horloges idéales.</p>
<h3 id="centimetre">Une horloge à un centimètre au-dessus du sol</h3>
<p>Comparée à une horloge identique restée au niveau du sol, elle avance d’environ <strong>[[cm_an_ps]] picosecondes par an</strong> : une picoseconde est un millionième de millionième de seconde. C’est aussi [[cm_jour_fs]] femtosecondes par jour. Il ne s’agit pas d’une accélération continue de son rythme : à hauteur fixe, le petit écart de rythme reste pratiquement constant et l’avance s’accumule.</p>
<p>Ce nombre est notre calcul pour une pesanteur locale de 9,81 m/s². L’effet gravitationnel est mesuré : <a href="https://doi.org/10.1038/s41586-021-04349-7">Bothwell et ses collègues, en 2022</a>, ont résolu des différences de fréquence à travers un échantillon atomique de taille millimétrique. Une horloge optique est une horloge atomique utilisant une transition à fréquence optique ; toute horloge atomique ordinaire n’atteint pas cette précision.</p>
<h3 id="terre">Au centre terrestre : le piège de la force nulle</h3>
<p>Au centre d’une Terre idéale sphérique, les attractions se compensent : l’accélération gravitationnelle nette est nulle. Pourtant, le potentiel gravitationnel y est plus bas qu’à la surface. <strong>Une horloge centrale accumule donc moins de temps.</strong> La force locale indique la pente du potentiel, pas sa profondeur. Une vallée peut avoir un fond plat tout en se trouvant bien plus bas que ses bords.</p>
<p>Le noyau est une région étendue : le nombre cité pour le centre exact ne s’applique pas identiquement à tout le noyau. Plus on descend dans le modèle sphérique stationnaire, plus l’horloge retarde par rapport à la surface. La force de pesanteur, elle, ne croît pas continuellement jusqu’au centre.</p>
<p>L’étude d’<a href="https://arxiv.org/abs/1604.05507">Uggerhøj, Mikkelsen et Faye (2016)</a> donne [[prem_age]] ans d’écart entre centre et surface en extrapolant un modèle de structure terrestre sur 4,54 milliards d’années. C’est une estimation théorique, pas une mesure de deux horloges anciennes. La même extrapolation représente <strong>[[prem_80]] seconde sur 80 ans</strong>. Elle ne signifie pas que les roches du noyau se seraient formées deux ans et demi après celles de la croûte.</p>
<h3 id="trou-noir">Près d’un trou noir : un effet potentiellement beaucoup plus grand</h3>
<p>Considérons un trou noir sans rotation et une horloge maintenue à une position fixe à l’extérieur. À une distance du centre égale aux quatre tiers du rayon de l’horizon, elle compte 30 minutes pendant qu’une horloge très lointaine en compte 60. Localement, ces 30 minutes sont ordinaires. Ce scénario impose toutefois un maintien par poussée ; ce n’est pas une orbite libre stable.</p>
<p>À mesure que la position fixe se rapproche de l’horizon, la poussée nécessaire devient sans borne dans ce modèle. On ne peut pas poser une horloge immobile sur l’horizon. Un observateur qui tombe suit une autre trajectoire et peut franchir l’horizon en un temps propre fini. Le gel apparent de ses derniers signaux pour un observateur lointain ne signifie pas que son temps personnel s’arrête.</p>

<h2 id="analyse">Analyse détaillée</h2>
<h3>Ce que la relativité générale ajoute</h3>
<p>La relativité générale, formulée par Einstein en 1915 et exposée dans son <a href="https://doi.org/10.1002/andp.19163540702">article de synthèse de 1916</a>, relie la géométrie de l’espace-temps au contenu en énergie, impulsion et contraintes. Dans la forme incluant la constante cosmologique :</p>
$$G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}.$$
<p>Le membre de gauche décrit la géométrie, celui de droite le contenu physique qui y contribue. Les horloges mesurent la longueur temporelle de leur trajectoire dans cette géométrie. Parler seulement d’une « force qui ralentit tout » masque cette structure.</p>
<h3>Champ faible et petites hauteurs</h3>
<p>Dans un champ faible et stationnaire, à faibles vitesses, avec un potentiel newtonien Φ nul à l’infini :</p>
$$\frac{d\tau}{dt}\simeq1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}.$$
<p>Pour deux horloges maintenues à proximité l’une de l’autre, une petite différence de hauteur Δh donne, au premier ordre, \(\Delta\Phi\simeq g\Delta h\). D’où :</p>
$$\frac{\Delta f}{f}\simeq\frac{g\Delta h}{c^2}.$$
<p>Pour Δh = 0,01 m, cela donne [[cm_fraction]]. Multiplié par les secondes d’une année de 365,25 jours, on retrouve [[cm_an_ps]] picosecondes. Sur un mètre, l’avance vaut environ [[metre_an_ns]] nanosecondes par an ; sur un kilomètre, [[km_an_us]] microsecondes par an dans l’approximation à g constant. Les vitesses, la rotation terrestre et les variations du potentiel demandent des corrections dans une comparaison précise.</p>
<h3>Pourquoi la formule extérieure ne convient pas au centre de la Terre</h3>
<p>À l’intérieur, la matière située plus loin que l’horloge contribue encore au potentiel, même lorsque sa force nette s’annule par symétrie. On ne doit donc pas prolonger \(-GM/r\) jusqu’à r = 0 en mettant toute la masse terrestre au centre. Pour une sphère homogène de rayon R :</p>
$$\Phi(r)=-\frac{GM}{2R}\left(3-\frac{r^2}{R^2}\right),\qquad 0\leq r\leq R.$$
$$\Phi(R)-\Phi(0)=\frac{GM}{2R},\qquad \frac{\tau_{\rm surface}-\tau_{\rm centre}}{\tau_{\rm surface}}\simeq\frac{GM}{2Rc^2}.$$
<p>Avec le rayon terrestre arrondi à 6 371 km, notre calcul homogène donne [[homogene_age]] ans sur la durée géologique choisie, ou [[homogene_80]] seconde sur 80 ans. Le résultat publié avec le profil de densité PREM, [[prem_age]] ans, tient compte d’un centre plus dense. Nous citons ce résultat et exécutons sa conversion temporelle ; nous n’avons pas refait l’intégration de PREM.</p>
<figure class="mc-resultats">
<img src="/fichiers/gravitation-horloges/terre-horloges.svg" width="480" height="490" loading="lazy" alt="Le retard d’une horloge augmente en allant de la surface au centre. Courbe calculée pour une Terre homogène et point central séparé issu de la valeur PREM publiée.">
<figcaption>Calcul de sphère homogène ; point PREM converti depuis Uggerhøj et al. (2016). La durée de référence de 80 ans appartient à l’horloge de surface. Les deux estimations supposent une structure stationnaire.</figcaption>
</figure>
<p>Le résultat géologique ne retrace pas toute l’accrétion, la différenciation et l’évolution de la planète. Pour une histoire exacte, il faudrait intégrer le potentiel et le mouvement au cours du temps. Aucun organisme ne pourrait séjourner au centre terrestre : la comparaison porte sur la durée propre d’horloges idéales, indépendamment de cette impossibilité matérielle.</p>
<h3>La comparaison de Schwarzschild</h3>
<p>Le rayon de l’horizon d’un trou noir sphérique, non chargé et sans rotation est \(r_s=2GM/c^2\). Pour dix masses solaires nominales, notre calcul donne [[bh_rs_10]] km. Le rayon r utilisé ici est défini par l’aire \(4\pi r^2\) des sphères : sa différence avec r_s n’est pas directement une distance radiale mesurée à la règle.</p>
<p>À une position fixe, pour \(r>r_s\), la durée comparée au temps d’une horloge statique à l’infini satisfait :</p>
$$\frac{d\tau}{dt}=\sqrt{1-\frac{r_s}{r}}.$$
<table class="phrases"><caption>Horloge maintenue à rayon fixe : durée locale pendant 60 minutes très loin du trou noir.</caption><thead><tr><th>Rayon depuis le centre</th><th>Minutes locales</th></tr></thead><tbody>
<tr><td>10 r_s</td><td>[[bh_10_min]]</td></tr>
<tr><td>3 r_s</td><td>[[bh_3_min]]</td></tr>
<tr><td>2 r_s</td><td>[[bh_2_min]]</td></tr>
<tr><td>4 r_s / 3</td><td>[[bh_43_min]]</td></tr>
<tr><td>1,01 r_s</td><td>[[bh_101_min]]</td></tr>
</tbody></table>
<p>Ces chiffres sont des prédictions dans un modèle idéal. Ils ne suffisent pas à proposer un séjour réalisable : poussée, forces de marée, rayonnement environnant et trajet aller-retour doivent aussi être considérés.</p>
<h3>Une orbite n’est pas un maintien statique</h3>
<p>Pour une orbite circulaire géodésique dans le même espace-temps :</p>
$$\frac{d\tau}{dt}=\sqrt{1-\frac{3r_s}{2r}}.$$
<p>Les orbites circulaires stables commencent à \(r=3r_s\), avec stabilité marginale à cette limite. Le rapport vaut alors [[bh_orbite_3]], au lieu d’environ 0,816 pour une horloge statique au même rayon. Le mouvement orbital contribue donc réellement à la différence. Les trous noirs en rotation demandent une autre géométrie et une spécification du sens de l’orbite.</p>
<figure class="mc-resultats">
<img src="/fichiers/gravitation-horloges/trou-noir-horloges.svg" width="480" height="490" loading="lazy" alt="Comparaison des rythmes d’horloges statiques et sur orbites circulaires stables. La courbe orbitale commence à trois rayons d’horizon ; aucune horloge statique n’est définie sur l’horizon.">
<figcaption>Calculs dans la solution de Schwarzschild. Le point à 3 r_s indique l’orbite circulaire marginalement stable. La limite de la courbe statique vers l’horizon ne représente pas une horloge qui pourrait y rester immobile.</figcaption>
</figure>
<h3 id="preuves">Ce qui est testé, et ce qui reste extrapolé</h3>
<p>Les horloges optiques testent directement les écarts de rythme dans le champ terrestre. Près du centre galactique, <a href="https://arxiv.org/abs/1807.09409">GRAVITY a observé dans la lumière de l’étoile S2</a> un signal combinant décalage gravitationnel et Doppler transverse, compatible avec la relativité générale. Ce n’est pas une mesure isolée de la composante gravitationnelle ni une observation à l’horizon.</p>
<p>La <a href="https://arxiv.org/abs/1602.03837">détection GW150914</a> teste une autre prédiction : les ondes gravitationnelles d’une fusion de trous noirs. Ces réussites ne nous donnent pas accès à la singularité intérieure. La distinction est développée dans <a href="/hawking-trous-noirs-limites/">l’étude sur Hawking et les limites des théories</a>.</p>
""",
}

HAWKING_LIMITES = {
    'titre': 'Hawking : ce que les trous noirs révèlent, et ce qui reste inconnu',
    'description': 'Singularités, loi des aires, rayonnement, information et proposition sans bord : distinguer les preuves et les questions ouvertes.',
    'date': '8 octobre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>Hawking n’a pas proposé une théorie unique qui remplacerait celle d’Einstein.</strong> Ses travaux ont exploité la relativité générale, puis l’ont confrontée à la physique quantique. Ils mettent en lumière des résultats puissants et des endroits où notre description reste incomplète.</p>
<p>Il faut suivre trois étapes : la gravitation peut former un horizon ; les champs quantiques sur ce fond prédisent une émission ; l’évolution complète de l’objet, surtout à la fin, demande davantage que ce premier calcul. Chacune de ces étapes possède son propre niveau de preuve.</p>
<ol>
<li><strong>Singularités, avec Penrose :</strong> certaines hypothèses classiques conduisent à des trajectoires incomplètes. Le théorème ne décrit pas une physique de remplacement.</li>
<li><strong>Loi des aires :</strong> sous ses hypothèses classiques, l’aire totale des horizons ne décroît pas. Son domaine exclut des effets quantiques pertinents pour l’évaporation.</li>
<li><strong>Rayonnement de Hawking :</strong> une émission quasi thermique est prédite sur un fond gravitationnel. La détection astronomique directe manque ; l’approximation n’explique pas toute la fin.</li>
<li><strong>Proposition de Hartle–Hawking :</strong> une prescription quantique pour l’état de l’Univers sans bord initial classique. Elle dépend d’hypothèses et n’est pas confirmée comme origine réelle de l’Univers.</li>
</ol>
<h3 id="horizon">L’horizon n’est pas la singularité</h3>
<p>L’horizon sépare les événements pouvant encore envoyer un signal vers l’extérieur lointain de ceux qui ne le peuvent plus. Ce n’est pas une paroi matérielle. Dans le modèle classique d’un grand trou noir, le franchissement peut se produire sans rencontre locale avec une surface solide ; les forces de marée dépendent notamment de la masse et de la trajectoire.</p>
<p>La singularité correspond à une autre difficulté : la description classique cesse de permettre la continuation de certaines trajectoires. Dans la solution de Schwarzschild, la courbure diverge vers r = 0. Cela ne nous autorise pas à affirmer qu’une densité infinie est un objet physiquement observé. Le calcul nous dit où il atteint sa limite.</p>
<h3 id="rayonnement">Comment un trou noir peut-il émettre ?</h3>
<p>Le <a href="https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-43/issue-3/Particle-creation-by-black-holes/cmp/1103899181.pdf">calcul de Hawking de 1975</a> traite des champs quantiques dans une géométrie d’effondrement. L’état qui ressemble au vide avant la formation du trou noir produit une émission pour les observateurs lointains. La description populaire de deux petites particules créées sur le bord est une image limitée, pas le mécanisme complet du calcul.</p>
<p>L’énergie rayonnée réduit la masse du trou noir s’il perd davantage qu’il n’absorbe. Pour les masses stellaires, la température prédite est extraordinairement faible. Le gaz brillant autour d’un trou noir et ses jets ne constituent pas une observation du rayonnement de Hawking.</p>
<p>Des <a href="https://arxiv.org/abs/1510.00621">expériences analogues dans des condensats atomiques</a> étudient des horizons pour des excitations du milieu. Elles sont pertinentes pour les mécanismes d’émission, mais elles ne fabriquent pas un trou noir astrophysique et ne constituent pas sa détection directe.</p>
<h3 id="information">Le problème de l’information, concrètement</h3>
<p>Imaginons deux états quantiques différents qui s’effondrent. Si, après une évaporation complète, ils aboutissaient exactement au même état final de rayonnement, leur distinction aurait disparu. Une évolution quantique unitaire préserve au contraire les distinctions de l’état complet. L’« information » désigne ici ces états et leurs corrélations ; ce n’est pas nécessairement une mémoire humaine récupérable.</p>
<p>Le calcul initial produit un rayonnement dont une partie de la description est thermique et corrélée avec l’intérieur. La question décisive porte sur les corrélations du système complet au cours de l’évaporation. Les progrès récents sur l’entropie apportent des réponses dans des modèles précis, tout en laissant ouverte la description physique complète d’un trou noir astrophysique.</p>

<h2 id="analyse">Analyse détaillée</h2>
<h3>Singularités : un théorème avec des hypothèses</h3>
<p>Le <a href="https://doi.org/10.1098/rspa.1970.0021">théorème de Hawking et Penrose (1970)</a> combine des conditions de causalité, de convergence des trajectoires, d’énergie et de focalisation, avec une hypothèse globale appropriée. Il aboutit à l’incomplétude d’au moins certaines géodésiques temporelles ou nulles. Il ne dit pas que tous les observateurs rencontrent le même point ni que tout indicateur de courbure diverge dans tous les cas.</p>
<p>Une trajectoire temporelle incomplète peut avoir une durée propre finie sans continuation dans l’espace-temps considéré. Pour un rayon lumineux, la notion correspondante utilise un paramètre affine ; il ne s’agit pas du temps indiqué par une montre attachée au photon. Certaines hypothèses classiques peuvent être violées par des effets quantiques. Ce théorème ne prouve donc ni une création à partir du néant ni l’impossibilité de tout modèle cosmologique antérieur.</p>
<p>Dans Schwarzschild, le scalaire de courbure de Kretschmann vaut :</p>
$$K=R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta}=\frac{48G^2M^2}{c^4r^6}=\frac{12r_s^2}{r^6}.$$
<p>Il est fini à l’horizon, \(K(r_s)=12/r_s^4\), et diverge quand r tend vers zéro. La divergence de certaines coordonnées à l’horizon n’est donc pas cette singularité de courbure. Cette distinction explique pourquoi le <a href="/gravitation-horloges/">temps propre du voyageur ne s’arrête pas à l’horizon</a>.</p>
<h3>Température et entropie</h3>
<p>Pour un trou noir non chargé et sans rotation :</p>
$$T_H=\frac{\hbar c^3}{8\pi G M k_B},\qquad S_{BH}=\frac{k_B c^3 A}{4G\hbar}.$$
<p>La température varie comme l’inverse de la masse ; l’entropie comme l’aire. En appliquant ces expressions aux constantes indiquées dans notre analyse, on obtient :</p>
<table class="phrases"><caption>Températures théoriques de Schwarzschild ; masses exprimées en unités solaires nominales.</caption><thead><tr><th>Masse</th><th>Température</th></tr></thead><tbody>
<tr><td>Une masse solaire</td><td>[[hawking_solaire_k]] K</td></tr>
<tr><td>Dix masses solaires</td><td>[[hawking_10_k]] K</td></tr>
<tr><td>Un million de masses solaires</td><td>[[hawking_million_k]] K</td></tr>
</tbody></table>
<p>Pour une masse solaire, \(S_{BH}/k_B\) vaut [[hawking_solaire_s]]. Ces valeurs sont des prédictions, pas des mesures de température ou d’entropie effectuées par Aeternam. Le spectre reçu comporte aussi des facteurs de transmission dus à la propagation des champs dans la géométrie.</p>
<h3>Une loi des aires testée, un rayonnement encore distinct</h3>
<p>L’analyse <a href="https://arxiv.org/abs/2509.08054">GW250114, publiée par LIGO, Virgo et KAGRA en 2025</a>, compare les propriétés avant et après une fusion. Dans les analyses présentées, l’aire finale est supérieure à la somme des aires initiales avec une forte crédibilité. C’est une mise à l’épreuve observationnelle de la loi classique, sous les hypothèses utilisées pour inférer les masses et les rotations.</p>
<p>L’aire peut pourtant décroître pendant une évaporation quantique : les conditions d’énergie du théorème classique ne s’y appliquent plus de la même façon. La loi thermodynamique généralisée concerne alors l’entropie du trou noir <em>et</em> celle de son environnement. Une augmentation d’aire lors d’une fusion ne démontre donc pas la détection de l’émission quantique.</p>
<h3>Évaporation : ce que signifie une durée gigantesque</h3>
<p>Une estimation de corps noir, sans accrétion et sans détail des espèces émises, conduit à :</p>
$$t_{\rm evap}\approx\frac{5120\pi G^2M^3}{\hbar c^4}.$$
<p>Elle donne [[hawking_solaire_ans]] ans pour une masse solaire. Le coefficient dépend de la manière de modéliser l’émission ; les facteurs de transmission et les particules accessibles importent. Ce chiffre est un ordre de grandeur sous hypothèses, pas une date certaine de disparition. La masse, la rotation et l’environnement évoluent, et l’approximation ne décrit pas de manière contrôlée l’ultime phase quantique.</p>
<h3>Courbe de Page et îlots d’entropie</h3>
<p>Dans un scénario idéal d’évaporation unitaire, l’entropie fine du rayonnement commence par augmenter puis redescend lorsque les corrélations deviennent accessibles dans une plus grande partie du rayonnement. Les <a href="https://arxiv.org/abs/1911.12333">calculs de répliques et d’îlots</a> reproduisent cette structure dans certains modèles, notamment bidimensionnels, avec des prescriptions gravitationnelles précises.</p>
<p>La <a href="https://arxiv.org/abs/2006.06872">revue d’Almheiri et de ses collègues</a> explique pourquoi cela constitue un progrès majeur. Calculer une entropie compatible avec l’unitarité n’équivaut cependant pas à disposer d’un dispositif récupérant les informations d’un trou noir réel, ni d’une description universellement admise de toutes les étapes de l’évaporation. Aucun de ces calculs n’est une mesure astronomique de la courbe de Page.</p>
<h3>Hartle–Hawking : une proposition sur l’Univers</h3>
<p>La <a href="https://doi.org/10.1103/PhysRevD.28.2960">proposition sans bord de Hartle et Hawking (1983)</a> cherche à définir un état quantique cosmologique à partir de géométries régulières ne possédant pas le bord initial classique habituel. Elle ne démontre pas que notre Univers n’a jamais commencé, ni qu’il est apparu à partir d’un néant physique défini expérimentalement.</p>
<p>Les prédictions dépendent notamment de la prescription de calcul et des probabilités que l’on en tire. <a href="https://arxiv.org/abs/2403.10510">Maldacena (2024)</a> discute des difficultés dans des modèles inflationnaires. Une <a href="https://arxiv.org/abs/2602.02682">prépublication d’Abdalla et de ses collègues (2026)</a> réexamine la normalisation et montre qu’elle modifie profondément les probabilités obtenues dans son cadre. Cela illustre une question théorique active, pas une origine de l’Univers désormais mesurée.</p>
<h3 id="points-ouverts">Les véritables points ouverts</h3>
<ul>
<li><strong>La gravitation quantique :</strong> quelle description remplace la géométrie classique lorsque ses fluctuations deviennent essentielles, et quelles observations départageront les propositions ?</li>
<li><strong>L’intérieur des trous noirs :</strong> que devient une singularité dans cette description ? L’extérieur observé ne fournit pas une photographie du centre.</li>
<li><strong>L’information :</strong> comment les résultats d’entropie se traduisent-ils en dynamique microscopique pour un effondrement et une évaporation réalistes ?</li>
<li><strong>La fin de l’évaporation :</strong> disparition complète, état résiduel ou autre évolution demandent une physique au-delà de l’extrapolation semi-classique.</li>
<li><strong>L’origine cosmologique :</strong> les modèles classiques singuliers, les propositions sans bord et les autres scénarios n’ont pas le même statut qu’une observation de l’instant initial.</li>
</ul>
<p>Ces limites n’annulent pas les comparaisons d’horloges, les orbites et les ondes gravitationnelles déjà testées. Une description peut être remarquablement fiable dans un domaine tout en restant incomplète dans un autre. La contribution de ces trois études est de préciser les domaines, reproduire des ordres de grandeur et éviter de transformer une formule ou une hypothèse en preuve universelle.</p>
<p>Revenir aux <a href="/einstein-relativite-restreinte/">vitesses et durées d’Einstein</a>, ou aux <a href="/gravitation-horloges/">comparaisons d’horloges du centre terrestre aux trous noirs</a>.</p>
""",
}

SUJETS = {
    'relativite': {
        'chemin': '/sujets/relativite-trous-noirs/',
        'titre': 'Relativité et trous noirs',
        'description': 'Comprendre Einstein et Hawking, comparer les horloges et examiner les limites de nos descriptions du temps et de la gravitation.',
        'intro': '<p>Des horloges séparées d’un centimètre aux horizons des trous noirs, la relativité relie le temps mesuré à la trajectoire et à la gravitation. Cette rubrique distingue les expériences, les calculs théoriques et les questions ouvertes.</p>',
        'questions': (
            'Pourquoi les vitesses ne s’additionnent-elles pas comme dans la vie courante ?',
            'Combien de temps s’écoule près d’un trou noir ou au centre de la Terre ?',
            'Que nous apprennent les travaux de Hawking, et où nos théories atteignent-elles leurs limites ?',
        ),
        'lectures': (
            ('/einstein-relativite-restreinte/', 'Commencer par les vitesses, la lumière et les durées'),
            ('/gravitation-horloges/', 'Comparer les horloges du sol au centre de la Terre et aux trous noirs'),
            ('/hawking-trous-noirs-limites/', 'Distinguer horizon, singularité, évaporation et information'),
        ),
    },
    'vision': {
        'chemin': '/sujets/vision/',
        'titre': 'Vision et perception',
        'description': 'Faire apparaître une perception, restaurer une fonction visuelle et étudier l’idée d’ajouter une image à ce que l’on voit.',
        'intro': '<p>Comment un signal devient-il quelque chose que l’on voit ? Cette rubrique explore les prothèses rétiniennes et corticales, les formes perçues et les modèles de vision artificielle. La question centrale est l’expérience visuelle obtenue.</p>',
        'questions': (
            'Que signifie exactement « injecter une image » dans la vision ?',
            'Comment distinguer une réponse neuronale, une forme reconnue et une perception utile ?',
            'Quels modèles ouverts permettent d’étudier ces questions ?',
        ),
        'lectures': (
            ('/interfaces-cerveau/#vision', 'Des perceptions lumineuses à l’idée d’une scène visuelle'),
            ('/interfaces-cerveau/#prima', 'Lire les résultats et les limites de l’essai PRIMAvera'),
            ('/interfaces-cerveau/#contribuer', 'Les chantiers proposés pour étudier les prothèses visuelles'),
        ),
    },
    'memoire': {
        'chemin': '/sujets/memoire/',
        'titre': 'Mémoire',
        'description': 'Former, renforcer ou modifier un souvenir ; comprendre ce qui relie le rappel, le récit et l’expérience vécue.',
        'intro': '<p>Un souvenir peut concerner une information apprise, un événement personnel ou une impression de familiarité. Ce fil examine les interventions sur la mémoire, les souvenirs artificiels et le lien entre mémoire, rêve et identité.</p>',
        'questions': (
            'Qu’ont réellement montré les expériences de modification de la mémoire ?',
            'Se rappeler une longue histoire implique-t-il de l’avoir vécue ?',
            'Comment évaluer le rappel et la continuité sans confondre leurs mesures ?',
        ),
        'lectures': (
            ('/interfaces-cerveau/#memoire', 'Ce que les interventions sur la mémoire permettent de conclure'),
            ('/interfaces-cerveau/#vingt-ans', 'La question des vingt années : souvenir, croyance et durée vécue'),
            ('/programme/#memoire', 'Étudier le souvenir du rêve et les données manquantes'),
        ),
    },
    'reve-temps': {
        'chemin': '/sujets/reve-temps/',
        'titre': 'Rêve et temps vécu',
        'description': 'Rêve lucide, contenu des rêves, durée ressentie et possibilité de vivre une expérience qui semble plus longue.',
        'intro': '<p>Le rêve ouvre des questions sur la conscience, le contenu de l’expérience et le passage du temps. Les articles examinent les échanges pendant le sommeil, l’influence d’un thème et les différentes façons de mesurer une durée.</p>',
        'questions': (
            'Peut-on reconnaître ou orienter un contenu pendant le rêve ?',
            'Comment mesurer le temps vécu plutôt que la seule durée racontée ?',
            'Que faudrait-il établir pour parler d’une vie en une nuit ?',
        ),
        'lectures': (
            ('/temps-reve/', 'Comprendre les mesures du temps dans les rêves'),
            ('/meg-eeg-reves/', 'Lire et orienter le rêve : preuves et questions ouvertes'),
            ('/projet/', 'Examiner l’hypothèse d’une vie en une nuit'),
        ),
    },
    'bci': {
        'chemin': '/sujets/interfaces-cerveau-machine/',
        'titre': 'Interfaces cerveau-machine',
        'description': 'Lire l’activité cérébrale, communiquer avec une machine et comprendre ce qu’une interface peut réellement décoder.',
        'intro': '<p>Les BCI relient le cerveau à un système informatique. Ce fil rassemble les recherches sur le décodage, les capteurs EEG et MEG, les implants et les interfaces qui associent mesure et intervention.</p>',
        'questions': (
            'Quelle information peut-on extraire du signal cérébral, et dans quelles conditions ?',
            'Que changent les capteurs, les données d’entraînement et les modèles d’IA ?',
            'Comment contribuer avec des données ouvertes et des résultats reproductibles ?',
        ),
        'lectures': (
            ('/interfaces-cerveau/#lire-ecrire', 'Comprendre la différence entre lire une activité et provoquer un effet'),
            ('/meg-eeg-reves/#brain2qwerty', 'Examiner ce que les décodeurs EEG et MEG ont démontré'),
            ('/bci-monte-carlo/#resultats', 'Explorer notre simulation de calibration et de bruit'),
        ),
    },
    'simulation': {
        'chemin': '/sujets/simulation/',
        'titre': 'Théorie de la simulation',
        'description': 'Examiner l’hypothèse d’un monde simulé, ses arguments philosophiques et les signatures de modèles physiques précis.',
        'intro': '<p>Que pourrait-on observer si notre monde était simulé ? Cette rubrique rassemble les arguments, leurs hypothèses et les tests de certaines architectures. Chaque conclusion reste attachée au modèle et aux observations qui la soutiennent.</p>',
        'questions': (
            'Quelles hypothèses rendent l’idée d’une simulation testable ?',
            'Quelles traces une grille, un générateur de hasard ou un calcul à la demande laisseraient-ils ?',
            'Jusqu’où un résultat sur un modèle permet-il de remonter à la nature de notre monde ?',
        ),
        'lectures': (
            ('/synthese/', 'Commencer par la synthèse des résultats et de leurs limites'),
            ('/test-1/', 'Confronter une grille cubique à la propagation de la lumière'),
            ('/audit-infodynamique/', 'Vérifier les démonstrations avancées en faveur d’une simulation'),
        ),
    },
}

ACCUEIL = {
    'titre': 'aeternam — blog de recherche',
    'intro': 'Un blog de recherche sur le cerveau, la perception, la mémoire, le rêve et la nature du réel. '
             'Des lectures, des calculs et des questions à creuser.',
    'methode': 'Chaque article distingue les résultats publiés, les analyses réalisées et les hypothèses encore ouvertes.',
}

A_PROPOS = {
    'titre': 'À propos d’Aeternam',
    'description': 'Un blog de recherche consacré aux BCI, à la vision, à la mémoire, au rêve, au temps vécu, à la relativité, aux trous noirs et à la théorie de la simulation.',
    'corps': r"""
<p>Aeternam est un blog de recherche personnel. L’envie qui le fait vivre : comprendre le cerveau et l’expérience consciente, suivre les technologies qui permettent de les étudier, et contribuer à la recherche avec des travaux vérifiables.</p>
<h2>Les sujets qui m’intéressent</h2>
<p>Les <a href="/sujets/interfaces-cerveau-machine/">interfaces cerveau-machine</a>, la <a href="/sujets/vision/">vision et la perception</a>, la <a href="/sujets/memoire/">mémoire</a>, le <a href="/sujets/reve-temps/">rêve et le temps vécu</a>, la <a href="/sujets/relativite-trous-noirs/">relativité et les trous noirs</a>, ainsi que la <a href="/sujets/simulation/">théorie de la simulation</a>. Ces sujets peuvent se rejoindre dans une question ; chacun garde ses méthodes et ses preuves.</p>
<p>Des idées comme ajouter une image à la vision, modifier un souvenir ou vivre une expérience très longue dans un temps court servent de points de départ. Les articles examinent ce qui a été démontré, ce qui manque et ce que l’on pourrait étudier ensuite.</p>
<h2>Comment les articles sont construits</h2>
<p>Le travail part d’études publiées, de sources primaires et de données ouvertes. Selon l’article, il prend la forme d’une lecture critique, d’une réanalyse de données ou d’un calcul sur des hypothèses explicites. Les recherches sur le cerveau réunies ici s’appuient sur des travaux existants et des calculs ; aucune expérience humaine propre à Aeternam n’est revendiquée.</p>
<p>Les textes développent une explication accessible puis l’analyse détaillée. Les sources sont liées dans le texte. Une proposition de recherche est présentée comme telle ; une simulation numérique indique ce qu’elle suppose. Les limites font partie des résultats.</p>
<h2>Un carnet qui évolue</h2>
<p>Le blog accueille les questions ambitieuses et les vérifications modestes. Une correction, une reproduction ou une comparaison bien définie peuvent être des contributions utiles. Le <a href="https://github.com/aitorgarcia21/aeternam">dépôt public</a> conserve les analyses, les résultats et l’historique des modifications.</p>
<p><a href="/sujets/">Explorer les thèmes</a> · <a href="/recherches/">Lire les articles</a></p>
""",
}

# L’ancienne adresse /projet/ conserve cette question comme article du blog.
PROJET = {
    'titre': 'Une vie en une nuit : une hypothèse à examiner',
    'description': 'Que signifierait vivre une vie en une nuit ? Durée continue, récit et mémoire posent trois questions différentes.',
    'date': '29 septembre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>Vivre une vie entière pendant une nuit est une question de recherche ouverte.</strong> Pour l’examiner, il faut préciser ce que « vivre une vie » signifie : une longue expérience consciente, une histoire qui en représente les moments, ou le souvenir d’une telle histoire.</p>
<p>Le rêve peut produire des scènes, des rencontres et des émotions sans environnement extérieur correspondant. Étudier son contenu et sa durée fournit des prises sur la question. Cela demande des mesures distinctes de l’expérience, du récit au réveil et de la mémoire.</p>
<p>Les articles sur <a href="/temps-reve/">le temps d’un rêve</a>, <a href="/meg-eeg-reves/">la lecture et l’orientation du rêve</a> et <a href="/interfaces-cerveau/#memoire">les interventions sur la mémoire</a> abordent ces différentes composantes.</p>
<h2 id="analyse">Analyse détaillée</h2>
<h3>Définir la durée que l’on cherche à expliquer</h3>
<p>Dans sa lecture littérale, vivre [[vie_ans]] années continues en [[nuit_h]] heures demande un rapport de [[facteur]] entre durée vécue et durée écoulée. Ce nombre vient de la définition de l’hypothèse. Il ne constitue ni une mesure du cerveau ni une prévision de réussite.</p>
<p>Une histoire couvrant quatre-vingts ans avec des ellipses et quatre-vingts années continuellement vécues sont deux objets différents. La continuité narrative est un sujet de recherche utile, dont les résultats doivent rester distincts de ceux sur l’accélération.</p>
<h3>Les premières prises sur le problème</h3>
<p>Le <a href="https://doi.org/10.1016/j.cub.2021.01.026">dialogue pendant le rêve</a> fournit des repères observables. L’<a href="https://doi.org/10.1016/j.concog.2020.102938">incubation thématique</a> donne une manière d’influencer certains contenus. Le <a href="https://doi.org/10.1016/j.concog.2024.103759">travail sur la lucidité à domicile</a> étudie des approches logicielles. Le carnet sur <a href="/programme/">le rêve, le temps et la mémoire</a> examine leurs mesures, leurs dénominateurs et les données disponibles.</p>
<p>Le rejeu neuronal rapide intéresse la mémoire. Il ne mesure pas une vie consciemment accélérée. Un résultat sur le rappel ou la vitesse d’une tâche doit donc garder sa propre unité et sa propre portée.</p>
<h3>Les questions à garder distinctes</h3>
<ul>
<li>Peut-on identifier ou orienter un contenu pendant le sommeil ?</li>
<li>Quels repères permettent de mesurer la durée de l’expérience en cours ?</li>
<li>Qu’est-ce qui demeure au réveil, et comment les épisodes sont-ils reliés dans le souvenir ?</li>
<li>Comment séparer un effet réel d’un biais de sélection, de rappel ou de mesure ?</li>
</ul>
<p>Ces questions appartiennent aux sujets <a href="/sujets/reve-temps/">Rêve et temps vécu</a> et <a href="/sujets/memoire/">Mémoire</a>. La <a href="/sujets/simulation/">théorie de la simulation</a> interroge la nature de notre monde avec d’autres preuves ; les résultats cosmologiques n’établissent pas la faisabilité d’une expérience onirique.</p>
""",
}

BCI_MONTE_CARLO = {
    'titre': 'BCI : simuler la calibration et le bruit',
    'description': 'Une simulation Monte-Carlo calée sur des EEG humains explore le nombre d’essais personnels, la correction du bruit et les limites des prévisions.',
    'date': '3 octobre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>Nous avons exécuté notre propre expérience Monte-Carlo pour étudier combien de données personnelles améliorent un décodeur BCI.</strong> Son générateur est ajusté sur [[mc_essais_reels]] essais EEG de [[mc_reels]] personnes, réellement traités dans notre <a href="/bci-generalisation/">analyse précédente</a>. Les nouvelles campagnes sont simulées&nbsp;: elles prédisent le comportement d’un modèle de mesure humaine, sans constituer de nouvelles mesures chez l’humain.</p>
<p>Chaque personne virtuelle produit des observations de calibration, puis un test indépendant. Nous faisons varier le nombre d’essais personnels, le bruit et la stabilité du signal. Notre critère, choisi pour cette expérience, est un <strong>gain moyen d’au moins cinq points</strong> par rapport au même système sans essai personnel étiqueté. Ce n’est pas un seuil clinique.</p>
<p>Dans le scénario qui conserve les contrastes ajustés aux EEG, ce critère est atteint à <strong>[[mc_budget_ref]] essais étiquetés avec correction par référence, contre [[mc_budget_brut]] avec le bruit ajouté non corrigé</strong>. La correction demande aussi [[mc_reference_n]] observations personnelles non étiquetées. Le résultat porte donc sur la réduction des essais guidés&nbsp;; le coût total de collecte doit inclure cette référence.</p>
<p><strong>Le nombre nécessaire dépend fortement des hypothèses.</strong> Si nous divisons le contraste entre les tâches par deux, ou si nous triplons l’amplitude de la dérive entre blocs, le critère n’est plus atteint jusqu’à [[mc_max]] essais. Une simulation donne ici une réponse conditionnelle et des situations à tester, pas un nombre universel valable pour chacun.</p>

<h2 id="analyse">Analyse détaillée</h2>
<h3 id="mesure">1. Ce que nous simulons d’une mesure humaine</h3>
<p>Notre point de départ est le <a href="https://physionet.org/content/eegmmidb/1.0.0/">jeu EEG Motor Movement/Imagery de PhysioNet</a>, attribué à Gerwin Schalk et aux contributeurs BCI2000. Nous conservons six valeurs par essai&nbsp;: les puissances logarithmiques de C3, Cz et C4 dans deux bandes, de 8 à moins de 13 Hz et de 13 à moins de 30 Hz. Elles proviennent des segments humains de trois secondes déjà extraits.</p>
<p>Pour chaque personne, nous ajustons un niveau moyen, une différence entre les consignes gauche/droite, les fluctuations des six valeurs ensemble et un décalage entre blocs d’enregistrement. Le Monte-Carlo tire de nouvelles observations selon ces distributions. Il produit les valeurs que reçoit notre décodeur&nbsp;; il ne reconstruit ni une anatomie ni une forme d’onde EEG complète.</p>
<p>Chaque campagne choisit l’un des douze profils ajustés. Les onze autres profils génèrent chacun [[mc_source_n]] essais pour le modèle de départ. Le profil cible génère séparément la calibration et [[mc_test]] essais de test. Le décodeur ne reçoit ni les paramètres cachés de la personne virtuelle ni les réponses du test. Les campagnes renouvelées ne créent pas une diversité biologique supplémentaire.</p>
<p>Les données d’origine contiennent 45 essais par personne. Les budgets plus élevés extrapolent les distributions ajustées. Les différences entre classes peuvent aussi contenir des effets de la consigne visuelle ou des artefacts&nbsp;: notre simulation ne prouve pas que toute l’information soit une intention motrice.</p>

<h3 id="experience">2. Une expérience répétée, avec ses hypothèses écrites</h3>
<p>Nous avons exécuté [[mc_repetitions]] campagnes par hypothèse, avec les budgets 0, 4, 8, 16, 32, 64, 128 et 256 essais étiquetés. Les classes sont équilibrées. Un budget contient les premiers essais des budgets suivants&nbsp;; le test est entièrement distinct. Les conditions partagent leurs tirages aléatoires pour permettre une comparaison appariée.</p>
<p>Le modèle de départ est une analyse discriminante linéaire. La calibration personnelle adapte ses moyennes et sa covariance&nbsp;: le poids des essais personnels est \(n/(n+16)\), pour \(n\) essais. Le reste provient du modèle source. La régularisation du décodeur est fixée à 0,1 vers la diagonale de covariance. Nous avons aussi calculé un comparateur utilisant les seuls essais personnels. Les paramètres sont fixés avant les courbes, sans préenregistrement externe.</p>
<p>Les quatre hypothèses conservent les contrastes empiriques, les divisent par deux, triplent la dérive, ou suppriment tout contraste entre classes. Les deux modifications sont des tests de sensibilité choisis, sans prétention à représenter une population clinique particulière. Le cas sans contraste sert de contrôle négatif.</p>

<h3 id="bruit">3. Le bruit ajouté et les moyens de le réduire</h3>
<p>Le niveau initial contient déjà la variabilité issue des EEG humains. Nous ajoutons deux perturbations corrélées entre canaux dans l’espace des caractéristiques. Elles représentent une nuisance commune, avec une intensité fixée. Ce modèle n’est pas une simulation électromagnétique&nbsp;: ses unités ne sont ni des volts ni des teslas, et il ne reproduit pas un parasite temporel à 50 Hz.</p>
<ul>
<li><strong>Sans bruit ajouté.</strong> Conserver la variabilité du générateur ajusté aux données humaines.</li>
<li><strong>Bruit ajouté, sans correction.</strong> Perturber la mesure de la personne cible pendant calibration et test.</li>
<li><strong>Correction par référence.</strong> Mesurer aussi le parasite avec des capteurs virtuels imparfaits, apprendre sa contribution sur [[mc_reference_n]] observations non étiquetées indépendantes, puis la soustraire.</li>
<li><strong>Atténuation supposée.</strong> Réduire à 20&nbsp;% l’amplitude du parasite ajouté. C’est une hypothèse du simulateur, sans performance matérielle démontrée.</li>
<li><strong>Référence contaminée.</strong> Laisser une partie de l’activité utile atteindre le capteur de référence, pour éprouver le risque de la retirer avec le bruit.</li>
</ul>
<p>Les observations de référence sont un coût personnel supplémentaire. Le modèle source utilise également les observations synthétiques des autres profils. «&nbsp;Zéro essai étiqueté&nbsp;» signifie donc une absence de calibration guidée&nbsp;; dans la condition corrigée, il reste des données personnelles de référence.</p>

<h3 id="resultats">4. Combien d’essais améliorent le décodeur dans ce modèle&nbsp;?</h3>
<p>Le critère demande un gain moyen d’au moins cinq points, une borne inférieure Monte-Carlo positive et le maintien du critère à tous les budgets supérieurs testés. Nous retenons le premier budget de la grille qui le satisfait. L’exactitude est équilibrée puisque le test comporte autant d’essais de chaque classe.</p>
[[figure_mc_seuils]]
<p>Avec la référence, le score passe de [[mc_score_ref0]]&nbsp;% à [[mc_score_ref64]]&nbsp;% entre zéro et 64 étiquettes&nbsp;: <strong>[[mc_gain_ref64]] points de gain</strong>, avec un intervalle Monte-Carlo de [[mc_ref64_bas]] à [[mc_ref64_haut]] points. Au même budget de 64, le bruit non corrigé donne [[mc_score_brut64]]&nbsp;%. Le score demeure modeste, même quand le critère exploratoire est atteint.</p>
<p>Le minimum de 128 dans le bruit non corrigé est plus fragile&nbsp;: son gain moyen est de [[mc_brut128_gain]] points, avec un intervalle de [[mc_brut128_bas]] à [[mc_brut128_haut]] points qui traverse la frontière des cinq points. La grille et la précision numérique ne permettent pas d’affirmer qu’un essai de moins ferait échouer la méthode.</p>
<figure class="mc-resultats">
<h4>Gain selon la calibration simulée</h4>
<p>[[mc_repetitions]] campagnes par condition, scénario empirique.</p>
<img src="/fichiers/bci-monte-carlo/calibration-bruit.svg" width="390" height="450" loading="lazy" alt="Courbes du gain moyen selon le nombre d’essais. La correction par référence atteint le critère à 64 essais, le bruit non corrigé à 128, dans le scénario empirique.">
<figcaption>L’abscisse double à chaque graduation. Chaque courbe mesure le gain sur son propre zéro étiquette. Les bandes indiquent la précision Monte-Carlo à 95&nbsp;% sous le modèle fixé, sans inclure l’incertitude humaine sur ses paramètres.</figcaption>
</figure>
[[figure_mc_scores]]
<p>Le budget corrigé comporte 64 essais guidés et 256 observations de référence, soit 320 observations personnelles dans notre construction. Le budget non corrigé de 128 n’a pas ce coût de référence. Nous avons donc mis en évidence une réduction conditionnelle des étiquettes nécessaires, tout en rendant visible le supplément de mesure. Aucune durée de séance humaine n’est déduite de ces nombres.</p>

<h3 id="sensibilite">5. Quand davantage de données ne suffit pas</h3>
<p>Après correction par référence, le gain à 256 essais tombe à [[mc_faible_gain]] points quand le contraste est divisé par deux, et à [[mc_derive_gain]] points quand l’amplitude de la dérive triple. Le critère n’est atteint dans aucun de ces deux scénarios sur la grille étudiée. Cela ne démontre pas qu’il serait impossible à tout budget supérieur&nbsp;; nous n’avons pas simulé ces budgets.</p>
<figure class="mc-resultats">
<h4>Sensibilité aux hypothèses de mesure</h4>
<p>Correction par référence, mêmes campagnes appariées.</p>
<img src="/fichiers/bci-monte-carlo/sensibilite-modele.svg" width="390" height="450" loading="lazy" alt="La courbe empirique franchit cinq points. Les courbes de contraste divisé par deux et de dérive triplée restent sous cinq points jusqu’à 256 essais.">
<figcaption>Les paramètres de sensibilité sont choisis pour éprouver la conclusion. Ils ne sont pas des catégories de patients mesurées. Les intervalles restent conditionnels à chaque modèle.</figcaption>
</figure>
<p>La référence contaminée donne [[mc_fuite_score]]&nbsp;% à 64 essais, contre [[mc_score_ref64]]&nbsp;% avec la référence indépendante du signal utile. Le débruitage peut enlever de l’information recherchée. Une trace plus lisse ou une erreur de reconstruction plus faible ne dispense donc pas de vérifier la tâche finale.</p>
<p>Les contrastes empiriques ont été estimés sur peu d’essais et peuvent être surestimés. Le scénario à contraste réduit montre la conséquence possible de cette incertitude&nbsp;; il n’en fournit pas une correction exacte. La dérive observée vient de trois runs d’une même séance, sans mesure de changement entre jours, de fatigue ni d’apprentissage humain.</p>

<h3 id="laboratoires-chinois">6. Ce que nous retenons des laboratoires chinois</h3>
<p><strong>Beihang et son institut de Ningbo interviennent sur le champ avant la mesure MEG.</strong> <a href="https://doi.org/10.1016/j.isatra.2025.07.050">Dou et al., 2025</a>, associent enceinte blindée, bobines à faible bruit et commande active de compensation. Le capteur mesure le champ résiduel et la commande le corrige. Notre atténuation hypothétique ne reproduit ni ce montage ni ses performances.</p>
<p><strong>À Shenzhen, le NCCLab de SUSTech construit des comparaisons contrôlées.</strong> Dans <a href="https://doi.org/10.1088/1741-2552/ac2bf8">EEGdenoiseNet</a>, les auteurs contaminent des EEG de référence avec des artefacts oculaires ou musculaires et évaluent la reconstruction. Nous retenons ce principe de perturbation connue. Notre expérience utilise son propre modèle statistique, sans reprendre leurs réseaux ni leurs résultats.</p>
<p>Trois problèmes restent distincts&nbsp;: le parasite extérieur mesuré par les capteurs, les artefacts du corps et le changement des caractéristiques entre personnes ou entre séances. Pour l’EEG, <a href="https://mne.tools/stable/auto_tutorials/preprocessing/40_artifact_correction_ica.html">la séparation de composantes</a> et <a href="https://mne.tools/stable/auto_tutorials/preprocessing/25_background_filtering.html">le filtrage fréquentiel</a> sont d’autres outils. Leur effet sur l’information utile doit être contrôlé. Un résultat de compensation magnétique ne donne pas directement un nombre d’essais de calibration EEG.</p>

<h3 id="verification">7. Ce que les contrôles établissent</h3>
<p>Les 48&nbsp;000 décisions d’une campagne vérifiée coïncident avec un calcul indépendant de densités gaussiennes dans SciPy. La correction par référence est vérifiée contre scikit-learn, et les vingt seuils sont recalculés séparément. Un exemple analytique confirme le générateur. Dans le scénario sans différence entre classes, le plus grand écart du score moyen à 50&nbsp;% est de [[mc_nul_ecart]] point.</p>
<p>Nous avons également ajusté un modèle sur deux runs humains et examiné le troisième&nbsp;: [[mc_couverture]]&nbsp;% des observations sont dans une ellipse gaussienne indicative à 95&nbsp;%. Ce diagnostic vérifie un aspect de la dispersion. Les paramètres de l’ellipse étant estimés, ce n’est ni un test exact ni une validation du nombre futur d’essais nécessaires.</p>
<p>Les résultats utiles de cette expérience sont les courbes conditionnelles, leurs coûts de calibration et leur sensibilité. Une étude humaine future devra confronter ces prévisions à de nouvelles séances, mesurer le bruit réel, réserver les essais chronologiquement et compter aussi les commandes involontaires au repos. Le Monte-Carlo nous aide à définir cette étude et à identifier les hypothèses dont son succès dépend.</p>
""",
}

BCI_GENERALISATION = {
    'titre': 'BCI : un décodeur face à une nouvelle personne',
    'description': '540 essais EEG de 12 personnes réanalysés, deux évaluations séparées et quatre études BCI récentes examinées dans leur portée réelle.',
    'date': '3 octobre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>Nous avons traité [[bci_essais]] essais EEG de [[bci_personnes]] personnes pour poser une question précise&nbsp;: un décodeur entraîné sur certains cerveaux fonctionne-t-il sur une personne qu’il n’a jamais vue&nbsp;?</strong> Les enregistrements viennent de données ouvertes existantes. Les participants devaient imaginer un mouvement de la main gauche ou de la main droite, selon une consigne visuelle.</p>
<p>Notre modèle simple atteint [[bci_meme]]&nbsp;% lorsqu’il apprend sur d’autres enregistrements de la même personne, et [[bci_nouvelle]]&nbsp;% lorsque la personne testée est entièrement absente de l’apprentissage. La mesure donne le même poids aux deux classes&nbsp;; une réponse constamment «&nbsp;gauche&nbsp;» vaut [[bci_reference]]&nbsp;%. Le premier résultat indique une association faible dans ce cadre exploratoire. Le second ne suffit pas à établir un décodage au-delà de notre contrôle par mélange des étiquettes.</p>
<p>Ce résultat concerne une méthode élémentaire et un petit sous-ensemble. Il ne fixe aucune limite aux BCI. Il montre pourquoi «&nbsp;le logiciel reconnaît une tâche&nbsp;» et «&nbsp;le logiciel fonctionne pour un nouvel utilisateur&nbsp;» doivent être vérifiés séparément. Nous publions aussi les scores individuels, pour que la moyenne ne cache pas les écarts.</p>
<p>Les interfaces implantées récentes atteignent d’autres capacités, notamment pour communiquer. Nous examinons ci-dessous quatre études de 2026, puis notre propre analyse. Les tâches, les capteurs et les populations diffèrent&nbsp;: leurs pourcentages ne se comparent pas directement à ceux de notre EEG.</p>

<h2 id="analyse">Analyse détaillée</h2>
<h3 id="recherche-recente">1. Quatre résultats récents, quatre difficultés concrètes</h3>
<p><strong>Utiliser une BCI chez soi.</strong> <a href="https://doi.org/10.1038/s41591-026-04414-6">Card et al., juin 2026</a>, documentent plus de [[card_heures]] heures chez une personne implantée, avec [[card_debit]] mots par minute en moyenne en usage personnel. Les [[card_copie]]&nbsp;% d’exactitude par mot concernent une tâche de copie&nbsp;; en usage personnel, [[card_personnel]]&nbsp;% des phrases sont jugées immédiatement entièrement correctes. Les unités diffèrent. L’installation reste assistée et le système se recalibre en arrière-plan.</p>
<p><strong>Parler et faire un geste simultanément.</strong> <a href="https://doi.org/10.1038/s41593-026-02446-2">Brosler et al., septembre 2026</a>, étudient des mouvements isolés chez [[brosler_isoles]] personnes, et des données simultanées chez [[brosler_simultanes]]. La copie simultanée quantifiée en temps réel concerne une personne. L’apprentissage de plusieurs contextes aide à limiter les activations indésirables d’une modalité quand seule l’autre est voulue. Les démonstrations de conversation restent limitées&nbsp;; elles ne valident pas une interaction libre générale.</p>
<p><strong>Mesurer un bénéfice perceptif.</strong> <a href="https://doi.org/10.1038/s41593-026-02281-5">Choudhari et al., mai 2026</a>, décodent l’attention auditive pour renforcer une voix parmi des voix concurrentes. Ils évaluent ensuite compréhension et préférence. Les [[choudhari_n]] participants sont enregistrés par électrodes intracrâniennes pendant un bilan d’épilepsie et déclarent une audition normale. Ce résultat ne valide donc pas un appareil EEG grand public destiné à la perte auditive.</p>
<p><strong>Transférer entre personnes.</strong> <a href="https://doi.org/10.1038/s41467-026-75455-1">Spalding et al., juillet 2026</a>, alignent des signaux de parole effectivement produite chez [[spalding_n]] personnes. L’alignement utilise des données d’apprentissage du patient cible, en gardant ses données de test à part. «&nbsp;Entre personnes&nbsp;» ne signifie donc pas «&nbsp;sans calibration&nbsp;». Le transfert à une personne paralysée demeure une question distincte.</p>
<p>Ces études orientent notre question de recherche&nbsp;: mesurer ce qui reste valable quand les conditions changent. Il faut examiner les données nécessaires au démarrage, les adaptations pendant l’usage, les activations non voulues et le bénéfice fonctionnel. Un score obtenu dans une tâche guidée ne répond pas à toutes ces questions.</p>

<h3 id="donnees">2. Les signaux que nous avons effectivement analysés</h3>
<p>Nous avons téléchargé [[bci_runs]] fichiers EDF du <a href="https://physionet.org/content/eegmmidb/1.0.0/">jeu EEG Motor Movement/Imagery de PhysioNet</a>, attribué à Gerwin Schalk et aux contributeurs BCI2000, sous licence Open Data Commons Attribution 1.0. Le sous-ensemble comprend les identifiants S001 à S012 et les enregistrements 04, 08 et 12. Ces derniers correspondent à l’imagerie main gauche/main droite, comme le précise aussi la <a href="https://mne.tools/stable/generated/mne.datasets.eegbci.load_data.html">documentation MNE</a>.</p>
<p>Les annotations donnent [[bci_gauche]] essais «&nbsp;gauche&nbsp;» et [[bci_droite]] essais «&nbsp;droite&nbsp;». Aucun essai de ces deux classes n’a été écarté selon son amplitude ou son résultat. Les périodes de repos sont hors de la tâche choisie. Le sous-ensemble et les paramètres ont été écrits avant le premier calcul des scores, sans préenregistrement externe ni sélection selon les performances.</p>
<p>Les URL, tailles et empreintes SHA-256 des fichiers bruts sont conservées. Les caractéristiques dérivées, les étiquettes, les prédictions et le protocole sont versionnés. Il s’agit d’une réanalyse de mesures existantes, sans nouvelle collecte humaine Aeternam.</p>

<h3 id="protocole">3. Un modèle volontairement simple, deux séparations des données</h3>
<p>Chaque essai fournit une fenêtre de trois secondes, de 0,5 à 3,5 secondes après la consigne. Nous utilisons trois électrodes, C3, Cz et C4, et deux bandes de fréquences&nbsp;: de 8 à moins de 13 Hz, puis de 13 à moins de 30 Hz. Cela donne [[bci_features]] caractéristiques, les logarithmes des puissances par canal et par bande. Le calcul retire la moyenne du segment, applique une fenêtre de Hann et intègre le périodogramme unilatéral. La référence enregistrée est conservée.</p>
<p>Le classifieur est une analyse discriminante linéaire, avec probabilités a priori égales et une régularisation fixée à 0,1 vers une identité de même trace. La standardisation et le modèle sont ajustés uniquement sur l’apprentissage. Aucun paramètre n’est optimisé sur les résultats présentés.</p>
<ol>
<li><strong>Personne entièrement réservée, évaluation principale.</strong> Apprendre sur onze personnes et prédire les essais de la douzième, puis répéter pour chacune. Aucun signal de la personne testée ne sert à ajuster son décodeur.</li>
<li><strong>Enregistrement réservé, évaluation secondaire.</strong> Pour chaque personne, apprendre sur deux de ses enregistrements et prédire le troisième, puis permuter leurs rôles. Ici, le modèle connaît déjà des données de cette personne.</li>
</ol>
<p>Un enregistrement, ou <em>run</em>, est un bloc de tâches du jeu. Le réserver ne revient pas à tester une autre journée. Les deux runs d’apprentissage peuvent le précéder ou le suivre&nbsp;: ce n’est pas une validation prospective après calibration. Les deux évaluations changent aussi la quantité et la provenance de l’apprentissage. Leur différence n’est pas une estimation causale de l’effet de la calibration.</p>
<p>Il y a [[bci_plis_personnes]] séparations apprentissage/test pour la première évaluation, [[bci_plis_runs]] pour la seconde. Chaque essai est prédit une seule fois hors apprentissage dans chacune. Nous calculons l’exactitude équilibrée sur les prédictions de chaque personne, puis la moyenne des personnes. Aucune fenêtre d’un même essai ne se retrouve des deux côtés.</p>

<h3 id="resultats">4. Résultats et contrôles</h3>
<div class="tableau"><table class="phrases"><thead><tr><th scope="col">Données réservées au test</th><th scope="col">Exactitude équilibrée moyenne</th><th scope="col">p de permutation, corrigé par Holm</th></tr></thead><tbody>
<tr><th scope="row">Personne entière</th><td>[[bci_nouvelle]]&nbsp;%</td><td>[[bci_nouvelle_p]]</td></tr>
<tr><th scope="row">Run, même personne</th><td>[[bci_meme]]&nbsp;%</td><td>[[bci_meme_p]]</td></tr>
</tbody></table></div>
<p>L’exactitude équilibrée est la moyenne du taux de bonnes réponses sur chaque classe. Sa référence constante vaut [[bci_reference]]&nbsp;%, même si les effectifs gauche/droite diffèrent. Entre personnes, les scores observés vont de [[bci_nouvelle_min]] à [[bci_nouvelle_max]]&nbsp;%. Pour les runs réservés, ils vont de [[bci_meme_min]] à [[bci_meme_max]]&nbsp;%. Ces étendues décrivent notre échantillon, pas l’incertitude dans la population.</p>
<figure class="bci-resultats">
<img src="/fichiers/bci-generalisation/resultats-individuels.svg" width="380" height="540" loading="lazy" alt="Scores des douze personnes. Les cercles représentent la personne absente de l’apprentissage, les carrés un run réservé de la même personne. Le tableau suivant fournit les valeurs exactes arrondies.">
<figcaption>Chaque ligne correspond à une personne. La ligne verticale marque 50&nbsp;%. Les différences individuelles sont importantes&nbsp;; aucun score individuel n’est ici présenté comme statistiquement confirmé.</figcaption>
</figure>
[[figure_bci_tableau]]
<p>Le contrôle mélange les étiquettes gauche/droite à l’intérieur de chaque bloc personne/run, puis réentraîne entièrement les deux évaluations. Nous avons exécuté [[bci_permutations]] permutations, avec une graine fixée. Le test est unilatéral&nbsp;: compter les scores mélangés au moins aussi élevés que le score observé, en ajoutant un au numérateur et au dénominateur. Holm corrige les deux tests.</p>
<p><strong>Le résultat sur une personne inconnue ne permet pas de conclure à un décodage établi au-delà de ce contrôle.</strong> Cela ne prouve pas l’absence d’information. Le résultat sur un run réservé indique une association faible, sous les hypothèses du test. Une p-valeur n’est ni la probabilité que le modèle soit vrai, ni celle qu’une prédiction particulière soit juste. Le nombre limité de permutations rend leur estimation grossière.</p>
<p>Nous avons contrôlé le calcul spectral d’un essai contre <em>SciPy</em>, puis les prédictions des deux évaluations contre une implémentation indépendante de l’analyse discriminante dans <em>scikit-learn</em>, avec les mêmes choix de standardisation, de covariance et d’a priori. Aucune prédiction ne diffère. Ce contrôle vérifie les calculs&nbsp;; il ne suffit pas à valider l’interprétation biologique.</p>

<h3 id="limites">5. Ce que cette analyse laisse ouvert</h3>
<p><strong>La consigne n’est pas une mesure pure de l’intention.</strong> Les classes sont associées à une présentation visuelle. Des réponses sensorielles, des mouvements résiduels ou d’autres artefacts peuvent contribuer au signal. Les canaux centraux et la fenêtre après consigne ne suffisent pas à les exclure. Une classification réussie ne démontrerait donc pas, à elle seule, la lecture d’une intention motrice isolée.</p>
<p>Les permutations supposent que les essais sont échangeables à l’intérieur de chaque bloc. Une dépendance temporelle pourrait fragiliser cette hypothèse. Les modèles des différents plis partagent aussi des données d’apprentissage&nbsp;: nous ne traitons pas ces plis comme des expériences indépendantes et ne fabriquons pas un intervalle binomial sur l’ensemble des prédictions.</p>
<p>Le jeu est petit, choisi par commodité, et le modèle utilise seulement trois canaux et six puissances. Il n’évalue ni une architecture performante réglée avec soin, ni tous les participants disponibles. Cette analyse ne reproduit pas un résultat publié de MOABB et ne revendique pas une nouvelle méthode de décodage.</p>
<p>Enfin, nous exploitons une fenêtre complète de trois secondes dans une tâche guidée. Nous n’avons mesuré ni commande en temps réel, ni débit en usage libre, ni fausses commandes pendant le repos. Ces données ne répondent pas non plus aux questions d’<a href="/interfaces-cerveau/#vision">intervention sur la vision</a> ou d’<a href="/interfaces-cerveau/#memoire">intervention sur la mémoire</a>.</p>

<h3 id="suite">6. La prochaine contribution utile</h3>
<p>Nous avons maintenant exécuté une <a href="/bci-monte-carlo/">simulation Monte-Carlo de calibration et de bruit</a>, ajustée aux caractéristiques EEG de cette étude. Elle explore l’effet du nombre d’essais personnels dans un modèle explicite. La comparaison sur de nouvelles mesures humaines réservées demeure une étape distincte&nbsp;: notre modèle simple pourrait servir de témoin face à des filtres spatiaux ou à des modèles de covariance, avec un réglage entièrement séparé du test.</p>
<p>Une seconde question porterait sur l’adaptation&nbsp;: combien d’essais d’une nouvelle personne faut-il pour améliorer son score&nbsp;? Il faudrait séparer chronologiquement calibration et évaluation, à quantité d’apprentissage comparable. Une véritable étude entre journées demanderait un jeu qui documente ces journées. Pour aller vers un usage libre, il faudrait aussi inclure le repos et compter les commandes déclenchées sans intention.</p>
<p>Le travail accompli ici fournit un point de départ vérifiable&nbsp;: des signaux réellement traités, des séparations explicites et un résultat modeste conservé tel quel. Les prochaines comparaisons devront conserver cette séparation entre le choix de la méthode et son évaluation.</p>
""",
}

INTERFACES_CERVEAU = {
    'titre': 'Interfaces cerveau-machine : vision et mémoire',
    'description': 'État des preuves sur les BCI, la vision artificielle et la modification de la mémoire, avec des pistes concrètes pour contribuer à la recherche.',
    'date': '3 octobre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>Nous savons déjà extraire certaines intentions du cerveau et provoquer certaines perceptions. Nous ne savons pas télécharger une vie dans une mémoire.</strong> Les interfaces cerveau-machine, ou BCI, relient une activité cérébrale à un système informatique. Certaines servent à commander ou à communiquer. D'autres interfaces stimulent le système nerveux pour produire un effet. Une boucle bidirectionnelle réunit les deux.</p>
<p>La vision artificielle offre un point d'appui concret&nbsp;: des personnes aveugles peuvent percevoir des formes provoquées par une stimulation, et des implants rétiniens ont amélioré l'acuité visuelle dans des essais cliniques. Il reste une grande distance entre ces capacités et l'apparition volontaire d'une scène réaliste dans le champ visuel.</p>
<p>Les interventions sur la mémoire modifient, dans certains protocoles, la rétention d'informations présentées. Elles ne démontrent pas la création à la demande d'une histoire personnelle complète. Se souvenir de vingt années, croire qu'elles ont eu lieu et les vivre consciemment sont trois objectifs différents.</p>
<p>Pour contribuer dès maintenant, notre piste est logicielle&nbsp;: comparer des méthodes de décodage sur données ouvertes et étudier des modèles de vision artificielle. Une <a href="/bci-generalisation/">première réanalyse de signaux EEG</a> est désormais exécutée. Ces questions rejoignent aussi <a href="/meg-eeg-reves/">la lecture et l'orientation du rêve</a>. L'étude qui suit sépare les résultats établis, les questions ouvertes et les travaux que nous pouvons entreprendre.</p>

<h2 id="analyse">Analyse détaillée</h2>
<h3 id="lire-ecrire">1. Lire et écrire ne sont pas deux versions du même problème</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Direction</th><th>Question</th><th>Exemple de résultat</th></tr></thead><tbody>
<tr><td>Cerveau vers machine</td><td>Quelle variable peut-on prédire à partir du signal&nbsp;?</td><td>Une parole tentée, une commande volontaire ou un état de sommeil dans une tâche définie.</td></tr>
<tr><td>Machine vers cerveau</td><td>Quel effet une intervention provoque-t-elle&nbsp;?</td><td>Une perception lumineuse, une modification sensorielle ou un effet sur une tâche de mémoire.</td></tr>
<tr><td>Boucle bidirectionnelle</td><td>La mesure permet-elle de mieux choisir l'intervention&nbsp;?</td><td>Adapter un système selon sa réponse, puis vérifier un bénéfice perceptif ou fonctionnel.</td></tr>
</tbody></table></div>
<p>Un décodeur apprend une relation statistique entre signal et étiquette. Un dispositif d'intervention doit établir une relation causale entre ce qu'il fait et ce que la personne perçoit ou accomplit. Inverser un réseau de lecture ne suffit pas à obtenir un dispositif d'écriture&nbsp;: plusieurs états peuvent produire des signaux proches, et les effets d'une stimulation dépendent de l'état du cerveau.</p>
<p>L'EEG et la MEG sont des moyens de mesure. Une prothèse rétinienne agit dans la voie visuelle avant le cerveau&nbsp;; une prothèse corticale intervient directement dans celui-ci. Elles ne possèdent ni les mêmes indications ni les mêmes contraintes. L'existence de l'une ne valide pas automatiquement l'autre.</p>

<h3 id="decodage">2. Les BCI de communication ont déjà franchi des étapes importantes</h3>
<p>Dans <a href="https://doi.org/10.1038/s41586-023-06377-x">l'étude de Willett et al. publiée en 2023</a>, une interface intracorticale décode la parole tentée d'une participante paralysée. Les résultats dépendent notamment du vocabulaire et du mode de parole évalués. C'est une capacité de communication volontaire dans un protocole précis, pas un accès indistinct à ses pensées.</p>
<p>Le travail de <a href="https://doi.org/10.1038/s41593-025-01905-6">Littlejohn et al. en 2025</a> avance vers une synthèse vocale continue, à partir d'une interface implantée. Cette progression souligne l'importance du délai de réponse. Le traitement par petits incréments ne doit cependant pas être confondu avec le délai total de toute la chaîne, qui inclut acquisition, décodage et restitution.</p>
<p>Les études invasives et non invasives ne constituent pas une compétition à score unique. La tâche, le nombre de personnes, les données d'entraînement, les conditions de test et la dépendance à un modèle de langage changent la signification d'une performance. Pour une contribution scientifique, une comparaison honnête sur la même tâche vaut davantage qu'un classement assemblant des pourcentages incompatibles.</p>

<h3 id="vision">3. «&nbsp;Injecter une image&nbsp;» recouvre plusieurs capacités</h3>
<p>Le cas le plus simple est une perception lumineuse provoquée, appelée phosphène. Une capacité plus exigeante consiste à placer plusieurs perceptions dans l'espace et dans le temps pour faire reconnaître une forme. Viennent ensuite la reconnaissance d'objets, la navigation, puis une scène riche et stable. Réussir une étape n'établit pas les suivantes.</p>
<p><a href="https://doi.org/10.1016/j.cell.2020.04.033">Beauchamp et al.</a> ont montré chez des participants voyants et aveugles que des séquences de stimulation corticale pouvaient faire reconnaître des formes de lettres. Le résultat donne un rôle au temps et à l'organisation des signaux. Il ne valide pas l'hypothèse qu'une électrode correspondrait à un pixel indépendant d'un écran.</p>
<p>Une étude de <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12632539/">2025 sur le contrôle de l'activité évoquée</a> utilise un modèle appris chez un participant aveugle implanté. Elle montre l'intérêt de prédire la réponse neuronale et d'adapter le contrôle. Mais réussir à rapprocher une activité d'une cible choisie ne démontre pas, à lui seul, que la personne voit exactement l'image voulue. La validation doit porter sur la perception et la fonction, pas uniquement sur la réponse enregistrée.</p>
<p>Une véritable superposition visuelle exigerait aussi un placement cohérent avec le regard, une stabilité entre jours, une interaction maîtrisée avec la vision restante et une mesure des déformations. Un objet reconnaissable dans une tâche préparée et un objet qui paraît présent dans le monde réel sont des résultats différents.</p>

<h3 id="prima">4. La prothèse rétinienne apporte une preuve clinique située</h3>
<p>Dans <a href="https://doi.org/10.1056/NEJMoa2501396">PRIMAvera, mis en ligne en 2025</a>, [[prima_n]] personnes atteintes d'atrophie géographique ont reçu un implant sous-rétinien. Parmi les [[prima_suivis]] évaluées à douze mois, [[prima_reponses]] atteignent le critère d'amélioration de l'acuité, soit [[prima_taux]]&nbsp;%. L'essai est ouvert, avec comparaison au niveau initial, sans groupe témoin randomisé. Il rapporte aussi [[prima_eig]] événements indésirables graves chez [[prima_patients_eig]] participants. Ces éléments font partie du résultat.</p>
<p>Nous avons vérifié les dénominateurs&nbsp;: selon l'issue inconnue des six personnes non évaluées, la proportion sur toutes les implantations serait arithmétiquement comprise entre [[prima_bas]] et [[prima_haut]]&nbsp;%. Cette fourchette n'est pas un intervalle de confiance. L'article propose séparément une estimation par imputation multiple. Le bénéfice observé ne se transpose pas directement à une personne voyante souhaitant ajouter une image à sa vision.</p>

<h3 id="memoire">5. Modifier la mémoire ne signifie pas écrire un souvenir choisi</h3>
<p>Il faut distinguer l'encodage d'une information, sa consolidation, son rappel, le sentiment qu'elle est familière et la conviction qu'un événement a été vécu. Une personne peut mieux reconnaître une image sans disposer d'un nouvel épisode autobiographique. Elle peut aussi raconter davantage sans avoir vécu plus longtemps.</p>
<p>Les travaux humains sur une <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6576290/">prothèse hippocampique en 2018</a>, puis sur des <a href="https://doi.org/10.3389/fncom.2024.1263311">caractéristiques et catégories en 2024</a>, étudient la rétention d'informations effectivement présentées dans des tâches de mémoire. Les résultats de 2024 comprennent des améliorations et des dégradations selon les personnes et les conditions. Ils n'établissent pas qu'un souvenir arbitraire puisse être transféré depuis un ordinateur.</p>
<p>Le travail de <a href="https://doi.org/10.1126/science.1239073">Ramirez et al. chez la souris</a> montre qu'une association mnésique artificielle peut être produite dans un paradigme expérimental. C'est une preuve sur une association de contexte chez l'animal. Elle ne démontre ni le récit, ni la richesse sensorielle, ni la continuité identitaire d'une autobiographie humaine créée de toutes pièces.</p>
<p>Pour revendiquer une «&nbsp;écriture de mémoire&nbsp;», il faudrait préciser quelle information était absente avant l'intervention, ce que la personne retrouve ensuite, sa fidélité, sa durée de conservation et les effets sur ses souvenirs existants. Aucune des études vérifiées ici ne démontre l'injection d'une vie complète.</p>

<h3 id="vingt-ans">6. Vingt années de souvenirs, ou vingt années réellement vécues&nbsp;?</h3>
<p>L'hypothèse de remplacer vingt ans de détention par vingt ans «&nbsp;injectés en mémoire&nbsp;» réunit au moins trois propositions différentes&nbsp;:</p>
<ol>
<li><strong>Une croyance rétrospective.</strong> La personne croit avoir traversé une longue période. Cette conviction ne démontre ni des souvenirs détaillés ni une durée vécue équivalente.</li>
<li><strong>Une histoire autobiographique artificielle.</strong> La personne possède un ensemble cohérent de scènes, de relations et d'événements qu'elle s'attribue. Cette capacité n'est pas démontrée par les études d'intervention mnésique présentées.</li>
<li><strong>Une expérience consciente prolongée.</strong> La personne vit effectivement chaque moment de la période pendant une durée physique courte. C'est une hypothèse d'accélération du vécu, distincte de la mémoire.</li>
</ol>
<p>Par définition, vingt années continues en une heure demanderaient un rapport de [[vingt_ans_une_heure]]&nbsp;; en huit heures, de [[vingt_ans_huit_heures]], avec la convention de 365,25 jours par an. Ces nombres sont une division de durées. Ils ne décrivent aucune performance cérébrale mesurée. Un récit qui couvre vingt ans, comme un film qui les raconte, ne démontre pas ce rapport.</p>
<p>Une mémoire artificielle ne reproduirait pas automatiquement l'apprentissage, le changement de comportement ou les autres conséquences d'une expérience réelle. Leur équivalence devrait être démontrée séparément. Le <a href="/programme/#temps">programme sur le temps vécu</a> conserve cette distinction entre durée, narration et mémoire.</p>
<p>L'application punitive imposée soulève en outre un problème majeur d'intégrité mentale et de consentement&nbsp;: modifier l'histoire qu'une personne s'attribue peut constituer un dommage, même sans longue détention physique. Le <a href="https://www.unesco.org/en/node/86248">cadre de l'UNESCO sur les neurotechnologies</a> place les droits et la protection des personnes au centre de leur développement. Aeternam retient comme directions de recherche l'expérience volontaire et la restauration de capacités, sans protocole de souffrance punitive ou de souvenirs imposés.</p>

<h3 id="contribuer">7. Comment contribuer utilement dès maintenant</h3>
<p>Le progrès ne dépend pas seulement de nouveaux implants. Il dépend aussi de mesures fiables, de comparaisons reproductibles, de modèles qui échouent de façon compréhensible et de logiciels accessibles. Trois chantiers permettent de commencer avec les ressources actuelles.</p>
<div class="tableau"><table class="phrases"><thead><tr><th>Chantier proposé</th><th>Première contribution</th><th>Preuve attendue</th></tr></thead><tbody>
<tr><td>Vision artificielle</td><td>Reproduire un modèle publié avec <a href="https://pulse2percept.readthedocs.io/en/stable/">pulse2percept</a>, puis comparer des représentations de scènes.</td><td>Résultat stable sur de nouvelles scènes et sous plusieurs hypothèses de perception&nbsp;; limites visibles.</td></tr>
<tr><td>Décodage EEG</td><td>Reproduire une référence <a href="https://moabb.neurotechx.com/docs/paper_results.html">MOABB</a> sur un jeu restreint.</td><td>Évaluation entre sessions ou personnes, incertitude, coût de calcul et absence de fuite de données.</td></tr>
<tr><td>Contenu du rêve</td><td>Auditer les annotations et reproduire une analyse EEG de réactivation d'expériences.</td><td>Correspondance entre données, étiquettes et rapports, puis robustesse sur des données réservées.</td></tr>
</tbody></table></div>
<p><strong>Le décodage EEG est le premier chantier effectivement engagé.</strong> Notre <a href="/bci-generalisation/#resultats">réanalyse sur données ouvertes</a> compare un modèle simple selon que la personne est connue ou absente de l’apprentissage. La reproduction d’une référence MOABB reste un travail distinct à réaliser. En vision artificielle, une autre piste serait de comparer une représentation brute, des contours et une sélection d'éléments pertinents pour une tâche, avec des critères fixés avant la comparaison et des scènes réservées.</p>
<p>Il faut toutefois éviter de prendre l'image du simulateur pour ce que verrait une personne. La <a href="https://pulse2percept.readthedocs.io/en/stable/users/faq.html">documentation de pulse2percept</a> insiste sur cette limite. Une méthode peut exploiter les particularités d'un simulateur et perdre son avantage avec d'autres paramètres ou un autre modèle. Une contribution utile mesure précisément cette fragilité.</p>
<p>Pour le décodage, <a href="https://moabb.neurotechx.com/">MOABB</a> propose un cadre commun de comparaison. La question peut être volontairement étroite&nbsp;: une méthode reste-t-elle meilleure sur une nouvelle session, à budget de calcul comparable&nbsp;? Les observations d'une même personne doivent rester regroupées selon le plan d'évaluation. Une différence obtenue après de nombreux essais doit être confirmée sur un jeu encore intact.</p>

<h3 id="programme">8. Un programme de recherche à étapes vérifiables</h3>
<ol>
<li><strong>Établir les preuves et leurs limites.</strong> Cette revue et l'étude <a href="/meg-eeg-reves/">MEG/EEG</a> sont complétées par des <a href="/bci-generalisation/">études BCI récentes et une première analyse de signaux EEG</a>&nbsp;: sources vérifiées, données traitées et calculs contrôlés.</li>
<li><strong>Reproduire une référence ouverte.</strong> Sélectionner une tâche, un petit jeu et une version du logiciel. Vérifier la licence, les annotations et le résultat avant de modifier la méthode. Cette reproduction reste à faire.</li>
<li><strong>Tester une amélioration circonscrite.</strong> Changer un élément, conserver un comparateur crédible, évaluer hors des données de réglage et publier aussi les échecs. Une nouvelle courbe seule ne constitue pas une avancée.</li>
<li><strong>Préparer un dossier scientifique utile à une équipe.</strong> Question, résultat reproductible, incertitudes, ressources nécessaires et expérience manquante. L'accès clinique et les collaborations doivent être établis avant de revendiquer une validation humaine.</li>
</ol>
<p>Cette revue et la réanalyse EEG transforment une intuition en questions mesurables&nbsp;: quelle information lire, quelle perception produire, quel souvenir améliorer, et comment reconnaître une réussite réelle. L’analyse des signaux ouverts constitue notre première mise en pratique sur le décodage&nbsp;; les autres interventions décrites ici restent des travaux de la littérature ou des questions de recherche.</p>
""",
}

MEG_EEG_REVES = {
    'titre': 'Lire et orienter le rêve',
    'description': 'MEG, EEG, IA et sommeil : sources vérifiées, limites du décodage, transfert entre capteurs et programme de recherche testable.',
    'date': '3 octobre 2026',
    'corps': r"""
<h2 id="explication">Explication</h2>
<p><strong>La MEG peut aider à étudier le contenu de l’activité cérébrale. Elle ne fournit pas encore un lecteur de rêves.</strong> Elle mesure de très faibles champs magnétiques liés à l'activité cérébrale. L'EEG mesure des différences de potentiel électrique à la surface du crâne. Leurs signaux permettent d'étudier le cerveau, mais une mesure précise n'indique pas automatiquement ce qu'une personne éprouve.</p>
<p>Le premier objectif utile serait de reconnaître une trace d'expérience apprise avant le sommeil, puis de vérifier si un signal sensoriel favorise sa présence dans un rêve rapporté. Reconnaître une plage parmi quelques thèmes connus serait déjà intéressant. Cela ne restituerait ni les personnes rencontrées, ni les événements, ni le temps vécu.</p>
<p>Notre analyse distingue trois résultats&nbsp;: détecter une activité liée à un contenu, modifier la probabilité d'un contenu rapporté et préserver le sommeil. Chacun doit être démontré séparément. Les travaux étudiés n'établissent pas encore leur réunion dans une même expérience.</p>
<p>Nous avons vérifié les articles, repéré les dépôts ouverts et exécuté des calculs qui montrent comment une expérience pourrait donner une conclusion trompeuse. Le volet <a href="/interfaces-cerveau/">interfaces cerveau-machine, vision et mémoire</a> étend cette recherche aux possibilités d'intervention sur le cerveau.</p>

<h2 id="analyse">Analyse détaillée</h2>
<h3 id="preuves">1. Ce que les résultats permettent de conclure</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Travail</th><th>Résultat utile</th><th>Ce qu'il reste à établir</th></tr></thead><tbody>
<tr><td><a href="https://doi.org/10.1038/s41593-026-02303-2">Brain2Qwerty v1</a></td><td>Décodage de phrases réellement tapées&nbsp;: erreur caractère moyenne de [[bq1_meg]]&nbsp;% en MEG et [[bq1_eeg]]&nbsp;% en EEG.</td><td>Décodage d'une expérience spontanée, sans clavier ni horodatages de frappe.</td></tr>
<tr><td><a href="https://facebookresearch.github.io/brain2qwerty/assets/brain2qwerty_v2.pdf">Brain2Qwerty v2</a></td><td>Prépublication&nbsp;: [[bq2_wer]]&nbsp;% d'erreur sur les mots, avec environ [[bq2_phrases]] phrases tapées par [[bq2_n]] personnes, enregistrées environ [[bq2_h]] heures chacune.</td><td>Une sortie continue à faible délai, puis une généralisation au sommeil.</td></tr>
<tr><td><a href="https://doi.org/10.1111/jsr.70000">Mémoire de vocabulaire à domicile</a></td><td>Amélioration du rappel de certains pseudomots réactivés pendant le sommeil.</td><td>Une modification du rêve, distincte d'un effet de consolidation mnésique.</td></tr>
<tr><td><a href="https://doi.org/10.1016/j.isci.2025.113032">Livres audio et sommeil</a></td><td>Des profils EEG en REM sont plus similaires entre personnes exposées au même livre.</td><td>Un décodeur individuel indiquant à quel instant un contenu est rêvé.</td></tr>
<tr><td><a href="https://doi.org/10.3389/frsle.2026.1812535">Incubation et rêves REM</a></td><td>Un thème se retrouve dans des récits après l'endormissement.</td><td>Un effet causal contrôlé, une histoire dirigée et un sommeil préservé.</td></tr>
</tbody></table></div>

<h3 id="brain2qwerty">2. Brain2Qwerty&nbsp;: une avancée dont il faut conserver la tâche</h3>
<p>La v1 utilise notamment les représentations motrices de la frappe. Les confusions suivent la proximité des touches. Elle ne prouve donc pas que la même information serait disponible pendant une pensée silencieuse ou un rêve. Les EEG et MEG proviennent de sessions distinctes&nbsp;: ce jeu ne fournit pas directement les couples synchronisés nécessaires à un apprentissage de transfert instantané. Ces limites sont décrites dans <a href="https://doi.org/10.1038/s41593-026-02303-2">l'article</a>.</p>
<p>La v2 réduit la dépendance aux événements de frappe fournis à l'inférence, mais sa discussion précise que l'architecture n'est pas causale&nbsp;: elle traite la phrase entière avant de la restituer. Le «&nbsp;temps réel&nbsp;» annoncé n'est donc pas une lecture mot à mot à faible délai. C'est décisif pour une boucle qui doit choisir quand intervenir. La <a href="https://facebookresearch.github.io/brain2qwerty/assets/brain2qwerty_v2.pdf">prépublication</a> rapporte un taux d'erreur sur les mots&nbsp;; son complément ne mesure ni la fidélité d'une pensée ni une proportion de phrases entièrement exactes.</p>
<p><strong>Conséquence pour Aeternam.</strong> Reprendre une architecture peut aider à apprendre le traitement des signaux. Valider un rêve exige une nouvelle tâche, ses propres annotations et une évaluation indépendante. Un modèle de langage peut améliorer la fluidité d'une sortie&nbsp;; cette fluidité ne garantit pas son origine dans le signal cérébral. Il faut le comparer à un modèle privé du signal, à des signaux désynchronisés et à des associations mélangées.</p>

<h3 id="materiel">3. La MEG portable conserve des contraintes physiques</h3>
<p>Les OPM rapprochent les capteurs de la tête et évitent la cryogénie. Cela ne signifie pas que tous fonctionnent intérieurement à température ambiante&nbsp;: les technologies alcalines et à hélium diffèrent. Le <a href="https://www.cea.fr/cea-tech/leti/english/Pages/What%27s-On/News/magnetoencephalography-towards-high-resolution-at-room-temperature.aspx">CEA décrit cette distinction</a>. Un casque mobile dans une salle spécialisée ne devient pas, par ce seul progrès, utilisable dans une chambre ordinaire.</p>
<p><a href="https://doi.org/10.1109/TBME.2024.3465654">Holmes et al.</a> montrent qu'un traitement spatial et temporel peut aider dans une salle moins blindée. Il reste un contrôle de l'environnement magnétique. <a href="https://doi.org/10.1038/s41378-026-01226-z">Cho et al.</a> miniaturisent un détecteur optique intégré à un OPM&nbsp;: la sensibilité annoncée de 33,5 fT/√Hz à 10 Hz n'est ni une mesure de résolution du rêve ni la démonstration d'un casque complet sur puce.</p>
<p>Le <a href="https://quspin.com/products-qzfm/">tarif QuSpin consulté le 3 octobre 2026</a> est de 10&nbsp;000 dollars par QZFM pour une commande de un à trois capteurs, avec supplément triaxial. Le coût d'un capteur ne comprend pas l'installation. Le montant de 830&nbsp;000 euros cité dans le texte initial n'a pas été corroboré par une référence de marché identifiable&nbsp;; il n'est pas retenu comme preuve de coût.</p>
<p>Pour une recherche sur le sommeil, il faut aussi établir le confort, la stabilité sur une nuit, le bruit environnemental, les mouvements et la compatibilité des stimulations sensorielles. Multiplier les voies de mesure ne multiplie pas d'autant les informations indépendantes. Le choix du matériel doit venir après une mesure de ce qu'il apporte à la tâche.</p>

<h3 id="transfert">4. Le transfert MEG vers EEG est une hypothèse à tester</h3>
<p>L'idée est de former un modèle avec un instrument riche, puis d'apprendre à un modèle EEG à en reproduire certaines prédictions. Cela peut améliorer l'apprentissage lorsque le signal EEG contient une information exploitable. Cela ne recrée pas automatiquement une information absente à l'instant du test.</p>
<p>Dans un modèle physique simplifié, les deux instruments observent des projections différentes des courants cérébraux&nbsp;: \(X_E=L_EJ+\varepsilon_E\) et \(X_M=L_MJ+\varepsilon_M\). Les projections, les bruits et la sensibilité aux sources diffèrent. La MEG n'est donc pas une vérité complète dont l'EEG serait simplement une copie floue. La vérité à rechercher concerne la tâche et l'expérience, que les deux instruments mesurent indirectement.</p>
<p>Nous avons calculé un contre-exemple exact. Quatre états sont définis par deux caractéristiques indépendantes. Le professeur voit les deux&nbsp;; l'élève n'en voit qu'une. Même avec un professeur parfait et un apprentissage idéal, l'élève doit encore départager deux états indiscernables.</p>
<div class="tableau"><table class="phrases"><thead><tr><th>Canal abstrait</th><th>Meilleure exactitude possible</th></tr></thead><tbody>
<tr><td>Les deux caractéristiques</td><td>[[info_professeur]]&nbsp;%</td></tr>
<tr><td>Une seule caractéristique</td><td>[[info_eleve]]&nbsp;%</td></tr>
<tr><td>La même, inversée avec une probabilité de 0,2</td><td>[[info_bruite]]&nbsp;%</td></tr>
<tr><td>Aucune information</td><td>[[info_hasard]]&nbsp;%</td></tr>
</tbody></table></div>
<p><strong>Ce tableau ne fixe aucun plafond réel de l'EEG.</strong> Il démontre seulement pourquoi la qualité du professeur ne suffit pas. Nous avons vérifié les valeurs en énumérant tous les classifieurs possibles dans ce petit modèle.</p>
<p>Un test utile comparerait, sur les mêmes données réservées, EEG seul, MEG seule et EEG entraîné avec l'aide de la MEG. Il faudrait ensuite réduire les canaux EEG, puis tester le transfert entre nuits. L'alignement doit être réel, les prétraitements appris sur l'entraînement seulement, et les données de la personne évaluée réservées selon la question posée. Un bénéfice à l'éveil n'établirait pas son maintien en REM.</p>

<h3 id="sommeil">5. Du signal au rêve&nbsp;: le maillon encore incertain</h3>
<p>Dans l'étude des <a href="https://doi.org/10.1016/j.isci.2025.113032">livres audio</a>, la mesure compare des profils de puissance EEG entre participants. Elle ne suit pas directement le passage d'une scène à une autre chez un dormeur. Le rapport est obtenu au réveil&nbsp;: il ne permet pas de dater chaque élément remémoré à l'intérieur du segment enregistré. Le dépôt annoncé exclut environ les 30 à 60 dernières secondes avant le réveil. Cette absence doit rester une absence.</p>
<p>Le travail de <a href="https://doi.org/10.1111/jsr.70000">Salfi et al.</a> analyse 24 personnes sur 31 recrutées. Le +8,6&nbsp;% rapporté concerne la variation de traduction des mots indicés entre le soir et le matin, contre −4,6&nbsp;% pour les autres. Le résultat ne mesure pas une «&nbsp;augmentation des rêves&nbsp;» et ne se transpose pas à une narration choisie.</p>
<p>Le <a href="https://doi.org/10.3389/frsle.2026.1812535">pilote d'incubation</a> compte quatre personnes sur huit avec incorporation au premier rêve REM, soit [[pilote_premier]]&nbsp;%. Le cumul atteint sept sur huit, soit [[pilote_cumul]]&nbsp;%, ou [[pilote_total]]&nbsp;% rapporté aux onze personnes recrutées. Les rappels de consigne après certains réveils et l'absence de contrôle empêchent d'attribuer ce cumul à une persistance spontanée. Les deux dénominateurs sont conservés.</p>

<h3 id="confusion">6. Le piège central&nbsp;: décoder le son envoyé</h3>
<p>Supposons qu'une forêt soit toujours associée au chant d'un oiseau. Après ce son, le modèle annonce «&nbsp;forêt&nbsp;». Il pourrait avoir reconnu la réponse auditive, le fichier diffusé ou son moment de présentation, sans détecter une forêt rêvée. L'erreur devient invisible si l'on utilise le thème du son comme étiquette du rêve.</p>
<p>Notre démonstration associe indépendamment quatre sons à quatre contenus. Un modèle qui identifie parfaitement le son obtient [[cue_score]]&nbsp;% si l'évaluation le compare au son, mais seulement [[cue_contenu]]&nbsp;% si elle le compare au contenu indépendant. Aucun progrès sur le décodage du rêve n'a eu lieu.</p>
<p>Les contrôles proposés sont donc des fenêtres silencieuses, des sons non associés, plusieurs sons par univers, un contrebalancement des associations et une évaluation sur des indices sonores absents de l'entraînement. La réponse auditive immédiate doit être distinguée de l'activité ultérieure. Le <a href="https://doi.org/10.1016/j.neuropsychologia.2025.109229">travail sur les sons en REM</a> motive l'étude de l'incorporation&nbsp;; il ne dispense pas de ces contrôles pour un nouveau décodeur.</p>

<h3 id="experience">7. Une expérience qui sépare lecture et intervention</h3>
<p><strong>Première étape&nbsp;: observation.</strong> Des expériences apprises avant le sommeil servent de thèmes candidats. Le modèle prédit sur des segments silencieux&nbsp;; les prédictions sont enregistrées avant le recueil du récit. Des évaluateurs ignorant la prédiction et la condition codent les rapports selon une grille définie à l'avance. Ils peuvent conclure «&nbsp;aucun&nbsp;», «&nbsp;plusieurs&nbsp;» ou «&nbsp;indéterminé&nbsp;». Forcer chaque rêve dans un des quatre univers transformerait un problème ouvert en exercice artificiellement facile.</p>
<p><strong>Deuxième étape&nbsp;: intervention randomisée.</strong> Après validation de la lecture, comparer indice associé, contrôle sonore et absence de signal. Le contenu rapporté constitue une mesure indépendante&nbsp;; le déplacement du score du modèle est une mesure secondaire. Un système qui optimise son propre score pourrait apprendre à produire des artéfacts qu'il reconnaît lui-même.</p>
<p><strong>Troisième étape&nbsp;: valeur de la boucle.</strong> Comparer une stimulation dépendant de l'état cérébral à une présentation comparable dont le moment ne dépend pas de cet état. Sans ce contraste, on pourrait constater un effet des sons tout en attribuant abusivement le bénéfice au décodeur.</p>
<p>Le plan doit réserver des nuits entières, puis des personnes si l'objectif est la généralisation. Les fenêtres voisines d'une même nuit ne doivent pas se retrouver de part et d'autre de l'évaluation. Les permutations, intervalles et analyses doivent respecter ce regroupement. Les mouvements oculaires et musculaires sont des contrôles nécessaires, notamment pour les fréquences élevées&nbsp;; leur pouvoir prédictif doit être mesuré séparément.</p>
<p>Les rapports manquants restent manquants. Le taux d'incorporation parmi les récits recueillis et le rendement parmi toutes les occasions planifiées répondent à des questions différentes. Le sommeil doit être évalué par sa fragmentation, son architecture et son retentissement diurne. Une absence de différence statistiquement significative ne démontre pas sa préservation&nbsp;: il faut définir ce qui constituerait une dégradation inacceptable et estimer l'incertitude.</p>

<h3 id="mesures">8. Un bon score moyen peut masquer un mauvais détecteur</h3>
<p>Dans un scénario purement hypothétique, le contenu recherché apparaît dans [[rare_prevalence]]&nbsp;% des segments. Même avec une sensibilité de [[rare_sensibilite]]&nbsp;% et une spécificité de [[rare_specificite]]&nbsp;%, seules [[rare_precision]]&nbsp;% des alertes sont correctes. La formule de Bayes donne \(P(C\mid +)=sp/[sp+(1-c)(1-p)]\), où \(p\) est la fréquence du contenu, \(s\) la sensibilité et \(c\) la spécificité. Ce calcul impose de publier les fausses alertes et les abstentions, pas seulement une exactitude globale.</p>
<p>Autre exemple de méthode&nbsp;: quatre classes équilibrées, un test unilatéral fixé à 5&nbsp;%, des épisodes indépendants et une exactitude réelle supposée de 40&nbsp;%. Le calcul binomial exact donne&nbsp;:</p>
<div class="tableau"><table class="phrases"><thead><tr><th>Épisodes indépendants</th><th>Réussites nécessaires</th><th>Probabilité de détecter l'effet supposé</th></tr></thead><tbody>
<tr><td>[[d0_n]]</td><td>[[d0_k]]</td><td>[[d0_puissance]]&nbsp;%</td></tr>
<tr><td>[[d1_n]]</td><td>[[d1_k]]</td><td>[[d1_puissance]]&nbsp;%</td></tr>
<tr><td>[[d2_n]]</td><td>[[d2_k]]</td><td>[[d2_puissance]]&nbsp;%</td></tr>
</tbody></table></div>
<p>Ce ne sont pas des effectifs humains recommandés. Des épisodes répétés chez une même personne, la sélection de nombreux modèles et les absences de rappel changent le calcul. Ces scénarios montrent pourquoi un premier essai peu informatif ne départage pas nettement réussite et échec.</p>

<h3 id="donnees">9. Ce qui est accessible pour commencer</h3>
<div class="tableau"><table class="phrases"><thead><tr><th>Ressource</th><th>Accès vérifié</th><th>Travail pertinent</th></tr></thead><tbody>
<tr><td><a href="https://doi.org/10.60493/31mg4-mfq53">EEG et récits de Kumral</a></td><td>Fiche et métadonnées accessibles&nbsp;; archive annoncée d'environ 46,6 Go. Pas téléchargée ici.</td><td>Vérifier les correspondances entre livres, personnes, segments et récits avant toute réanalyse.</td></tr>
<tr><td><a href="https://osf.io/2bkus/">Code de l'étude des livres audio</a></td><td>Liste des scripts et README lus via l'API publique.</td><td>Reproduire la similarité publiée, puis tester sa robustesse. Aucun rejeu accompli dans cette étude.</td></tr>
<tr><td><a href="https://huggingface.co/datasets/bcbl190626/SpanishBCBL">Brain2Qwerty v1</a></td><td>Fiche et arborescence accessibles. Environ 262 Go annoncés.</td><td>Étudier un sous-ensemble de frappe éveillée. Regrouper les identifiants d'une même personne et respecter la licence indiquée.</td></tr>
<tr><td><a href="https://mne.tools/stable/documentation/datasets.html#sample">MNE Sample</a></td><td>EEG et MEG simultanés documentés.</td><td>Apprendre l'alignement logiciel. La documentation exclut son usage comme évaluation du matériel.</td></tr>
<tr><td><a href="https://github.com/facebookresearch/brain2qwerty">Brain2Qwerty v2</a></td><td>Code publié, données annoncées sous embargo.</td><td>Lire l'architecture&nbsp;; ne pas revendiquer une reproduction complète sans données.</td></tr>
</tbody></table></div>
<p>La priorité proposée est l'étude des livres audio, car elle porte déjà sur le sommeil et le contenu. Brain2Qwerty constitue une école de décodage utile, mais sa tâche est plus éloignée du résultat recherché. L'étape immédiatement réalisable reste l'inventaire des annotations et des droits d'usage, suivi d'une réanalyse limitée compatible avec les moyens disponibles.</p>

<h3 id="decision">10. Le résultat à chercher avant de construire un casque</h3>
<p>Le prochain résultat crédible serait une prédiction de contenu sur de nouvelles données, supérieure aux contrôles, avec ses erreurs et son incertitude. Ensuite viendrait un effet randomisé sur les rapports, puis le bénéfice propre d'une boucle fermée et sa compatibilité avec le sommeil. Aucun de ces jalons ne mesure à lui seul une accélération du temps vécu.</p>
<p>Des équipes françaises possèdent les compétences pertinentes&nbsp;: <a href="https://www.cea.fr/drf/joliot/Pages/Plateformes_et_infrastructures/plateformes_imagerie/plateforme-neurospin.aspx">NeuroSpin</a>, <a href="https://www.cea.fr/cea-tech/leti/Pages/recherche-appliquee/infrastructures-de-recherche/plateforme-CLINATEC.aspx">Clinatec</a> et la recherche sur l'endormissement présentée par <a href="https://www.inserm.fr/actualite/portrait/comprendre-et-controler-lendormissement-le-reve-de-delphine-oudiette/">l'Inserm</a>. Leur existence n'établit ni disponibilité de créneaux ni partenariat avec Aeternam. La fiche CEA-Leti précédemment citée mélange une date de page récente et un début de poste en 2020&nbsp;; elle ne prouve pas une offre actuelle.</p>
<p><strong>Notre décision de recherche&nbsp;:</strong> commencer par les données ouvertes, la qualité des annotations et les contrôles. La MEG devient pertinente lorsqu'un protocole précis permet de mesurer son apport à l'EEG. L'observation et l'intervention se rejoindront sur des preuves, étape par étape.</p>
""",
}

PROGRAMME = {
    'titre': 'Rêve, temps et mémoire : un carnet de calculs',
    'description': 'Accès au rêve, contenu, durée et mémoire : réanalyses de données ouvertes et simulations pour éprouver les méthodes.',
    'date': '29 septembre 2026',
    'corps': r"""

<h2 id="explication">Explication</h2>
<p><strong>Peut-on commencer cette recherche sans laboratoire ni financement&nbsp;? Oui.</strong> Nous avons exécuté une réanalyse de données individuelles, recalculé des résultats publiés et construit un laboratoire numérique. Il permet de tester nos méthodes avant de leur confier une conclusion sur le cerveau.</p>
<p>Ce carnet rassemble des calculs sur l’accès au rêve, son contenu, sa durée et son souvenir. La question de la continuité relie ces thèmes. L’hypothèse d’une vie en une nuit demanderait en plus d’établir un allongement de l’expérience ; chaque question ci-dessous possède sa propre mesure.</p>
[[figure_parcours]]
<h2 id="analyse">Analyse détaillée</h2>
<h3 id="acces">1. Accéder au rêve et établir un échange</h3>
<p>Le tableau de <a href="https://doi.org/10.1016/j.cub.2021.01.026">Konkoly et al. (2021)</a> permet de recalculer deux taux&nbsp;: [[dialogue_tous]]&nbsp;% de réponses correctes sur tous les essais, contre [[dialogue_interpretes]]&nbsp;% parmi les réponses classées correctes ou incorrectes. Les silences et réponses ambiguës représentent [[dialogue_absents]]&nbsp;% des essais. Ces dénominateurs répondent à des questions différentes.</p>
<p>Notre conclusion de conception&nbsp;: un échange ne doit pas être évalué seulement lorsqu’il réussit. Il faut compter les tentatives, les non-réponses, les ambiguïtés et le nombre de personnes concernées. Le taux calculé par essai ne prédit pas la réussite d’une nuit chez un nouvel utilisateur.</p>
<p>Une étude de <a href="https://doi.org/10.1016/j.concog.2024.103759">2024 sur smartphone</a> rapporte davantage de rêves lucides avec des signaux associés à un entraînement préalable. Ses données individuelles sont disponibles sur demande, pas en téléchargement dans l’article. Nous en utilisons le résultat publié, sans prétendre en avoir refait l’analyse individuelle.</p>
<p><strong>Résultat de cet axe.</strong> Les échanges en rêve constituent un point d’appui expérimental existant. Notre apport actuel est le calcul explicite des unités et dénominateurs nécessaires à leur évaluation.</p>
<h3 id="contenu">2. Orienter un contenu et étudier sa persistance</h3>
<p>À partir des décomptes de <a href="https://doi.org/10.1016/j.concog.2020.102938">Dormio (2020)</a>, nous retrouvons une différence de [[incubation_difference]] points entre les proportions de récits contenant le thème avec et sans consigne. Il s’agit de récits répétés, pas de personnes indépendantes. Nous ne calculons donc pas un intervalle binomial comme si chaque récit venait d’une nouvelle personne.</p>
<p>Le <a href="https://doi.org/10.3389/frsle.2026.1812535">pilote de juin 2026</a> apporte une piste de continuité entre sommeil initial et sommeil paradoxal. Le thème apparaît en REM chez 7 des 8 personnes ayant atteint ce stade&nbsp;: [[rem_conditionnel]]&nbsp;%. Rapporté aux 11 participants initiaux, cela représente [[rem_total]]&nbsp;%. Le premier rêve REM contient le thème chez quatre personnes sur huit&nbsp;; le cumul inclut des épisodes ultérieurs et des rappels de consigne. Ces calculs descriptifs ne donnent pas un effet causal&nbsp;: l’étude n’a pas de groupe contrôle.</p>
<p>L’hypothèse à travailler est la persistance d’éléments stables — thème, lieu, personnage — entre épisodes. Le modèle devra compter séparément incorporation immédiate, réapparition et cohérence. Répéter le mot d’un thème ne démontre pas une histoire suivie.</p>
<p><strong>Résultat de cet axe.</strong> Il existe une piste publiée pour relier les épisodes par leur contenu. Les données brutes du pilote étant annoncées sur demande, nous avons recalculé ses dénominateurs, sans inventer de récits absents.</p>
<p>Nous approfondissons maintenant la mesure du contenu avec l'étude <a href="/meg-eeg-reves/">Lire et orienter le rêve</a>&nbsp;: audit des décodeurs MEG, données EEG ouvertes, transfert entre capteurs et contrôles nécessaires pour distinguer un son reconnu d'un contenu rêvé. Les <a href="/interfaces-cerveau/">BCI, la vision artificielle et les interventions sur la mémoire</a> forment un volet complémentaire. Les calculs nouveaux sont des démonstrations de méthode, sans expérience humaine Aeternam.</p>
<h3 id="temps">3. Mesurer le temps sans confondre ses dimensions</h3>
[[figure_dream]]
<p>Nous avons repris les données individuelles de la série Tononi dans <a href="https://doi.org/10.1038/s41467-025-61945-1">DREAM</a>&nbsp;: [[reveils]] réveils, [[sujets]] personnes, tous en stade N2. [[durees]] réveils comportent une déclaration de durée&nbsp;; [[manquantes]] n’en comportent pas. Les durées concernent uniquement les expériences rappelées.</p>
<p>[[longs]] déclarations appartiennent à une classe d’au moins une minute, soit [[part_longue]]&nbsp;% des déclarations disponibles. En donnant le même poids à chaque personne, la moyenne devient [[moyenne_sujets]]&nbsp;%, avec un intervalle de bootstrap par sujet de [[bootstrap_bas]] à [[bootstrap_haut]]&nbsp;%. Cet intervalle porte sur une fréquence de <em>déclaration</em> dans ce corpus. Il ne mesure pas une vitesse de conscience.</p>
<p>Nous avons aussi reconstruit les différences moyennes rêve moins éveil dans les trois tâches lucides publiées, à partir de la différence et du test apparié&nbsp;:</p>
<div class="tableau"><table><thead><tr><th>Tâche</th><th>Différence (s)</th><th>Intervalle à 95&nbsp;% (s)</th></tr></thead><tbody>
<tr><td>Compter</td><td>[[compter_delta]]</td><td>[[compter_bas]] à [[compter_haut]]</td></tr>
<tr><td>Marcher</td><td>[[marcher_delta]]</td><td>[[marcher_bas]] à [[marcher_haut]]</td></tr>
<tr><td>Gymnastique</td><td>[[gym_delta]]</td><td>[[gym_bas]] à [[gym_haut]]</td></tr>
</tbody></table></div>
<p>Ces intervalles utilisent les valeurs publiées arrondies et ne sont pas corrigés pour les trois comparaisons. Ils portent sur des différences de durée de tâches. Nous ne les convertissons pas en plafond de temps vécu.</p>
<p>Le script vérifie deux contre-exemples. Un choix entre deux durées ne sépare pas l’échelle ressentie du critère de réponse. Et une expérience de deux minutes ressenties en une minute peut rester invisible dans un intervalle de trente minutes entre réveils. C’est pourquoi les anciennes bornes globales ont été retirées.</p>
<p><strong>Résultat de cet axe.</strong> Le corpus donne des mesures descriptives et des tâches chronométrées. Il ne démontre pas une accélération générale et ne permet pas de l’exclure par une borne universelle. Pour étudier l’objectif, il faut des repères pendant l’expérience et une mesure distincte du récit final.</p>
<h3 id="memoire">4. Distinguer expérience, souvenir et histoire</h3>
<p>Dans notre réanalyse, une donnée de durée existe pour [[durees]] des [[reveils]] réveils. Remplacer les autres par une durée nulle assimilerait «&nbsp;pas de durée rapportée&nbsp;» à «&nbsp;aucune expérience&nbsp;». Nous les conservons comme données manquantes.</p>
<p>Une exploration compare, chez les [[perception_n]] personnes disposant des deux types de réponse, la fréquence des durées d’au moins une minute lorsque l’expérience est qualifiée de perceptive ou non. La différence moyenne vaut [[perception_delta]] points, avec un intervalle de bootstrap de [[perception_bas]] à [[perception_haut]] points. Il recouvre zéro&nbsp;: cette exploration ne permet pas de conclure à une association stable. Aucun lien causal n’est établi.</p>
<p>Un modèle de scénario illustre l’autre distinction&nbsp;: cent scènes de trois minutes occupent cinq heures. Elles pourraient représenter les moments d’une histoire de quatre-vingts ans, mais elles ne font pas quatre-vingts années continuellement vécues. Ce modèle précise une hypothèse narrative ; il ne simule pas le cerveau.</p>
<p>Le programme devra donc suivre séparément la durée éprouvée, la quantité de contenu remémoré, la cohérence entre épisodes et le sentiment de continuité personnelle. Les gains de mémoire après sommeil étudiés dans la littérature ne suffisent pas à établir ces quatre résultats.</p>
<h3 id="calcul">5. Construire un laboratoire numérique fiable</h3>
[[figure_erreurs]]
<p>Nous avons simulé [[simulations]] jeux de données par scénario, avec 20, 40 ou 80 personnes, trois mesures par personne et plusieurs niveaux de dépendance entre ces mesures. Ce sont des données artificielles&nbsp;: un gain cible de 20&nbsp;% et une dispersion de 0,35 sur les logarithmes sont des paramètres choisis.</p>
<p>Dans le scénario de 40 personnes et une corrélation de 0,6, alors qu’aucun gain n’existe dans le modèle, traiter chaque mesure comme indépendante produit [[faux_naif]]&nbsp;% de faux positifs. L’analyse par personne en produit [[faux_sujet]]&nbsp;%, pour un seuil prévu de 2,5&nbsp;%. Avec un gain simulé de 20&nbsp;%, la détection par personne atteint [[puissance]]&nbsp;% dans ce même scénario.</p>
<p>La simulation vérifie donc un risque concret&nbsp;: multiplier les réveils ne multiplie pas autant les observations indépendantes. Ces résultats de puissance dépendent entièrement des paramètres choisis&nbsp;; ils ne prédisent pas la performance d’un dispositif réel.</p>
<p>Le bootstrap rééchantillonne les personnes entières. Les tests appariés sont reconstruits dans leur unité originale. Les scripts vérifient les jointures, la conservation des effectifs, les données manquantes et le taux d’erreur sous une hypothèse nulle connue.</p>
<h3>Ce que nous avons produit</h3>
<p>Une base de calcul reproductible sur le temps déclaré, une lecture corrigée des résultats de rêve interactif et d’incubation, une séparation entre durée et récit, et un banc de simulation des erreurs statistiques. Aucun participant n’a été recruté et aucune dépense expérimentale n’a été engagée.</p>
<p>La prochaine progression utile est d’ajouter des jeux individuels réellement ouverts permettant de mesurer une action, un contenu ou un souvenir. Un article accessible dont les données sont seulement «&nbsp;sur demande&nbsp;» reste une source documentaire&nbsp;: nous n’en inventons pas les observations.</p>
<p>La <a href="/recherches/#simulation">théorie de la simulation</a> reste une recherche fondamentale distincte. Elle n’entre dans aucun de ces calculs sur le cerveau.</p>

""",
}
