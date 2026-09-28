"""English: translation of the French source (fr.py).

Each [[placeholder]] is replaced by a number from resultats.json, written according to
the conventions of the language. The formulas $$…$$ and \\(…\\) are identical in all
languages. A raw string (r\"\"\"…\"\"\") is required because of the backslashes.
"""
NOM = 'English'
HTML_LANG = 'en'
HREFLANG = 'en'
DIR = 'ltr'
LOCALE_OG = 'en_US'
DECIMALE = '.'

UI = {
    'devise': 'Research on simulation theory.',
    'description_site': 'aeternam — research on simulation theory',
    'travaux': 'Work',
    'langue': 'Language',
    'surtitre': 'Research · Test No. 1',
    'meta': 'version 2 · reproducible secondary analysis',
    'verdict': 'Verdict so far: no. We have no better reason to believe we are simulated than to believe the opposite; our tests detect no signature of a simulation, though they cannot rule out an undetectable one.',
    'introuvable': 'Page not found.',
    'fichier_pdf': 'aeternam-test-1-en.pdf',
}

ARTICLE = {
    'titre': 'A cubic lattice tested against GRB 221009A',
    'description': 'What the photons observed by LHAASO impose on the lattice spacing of a discrete space, '
                   'and where this constraint ends.',
    'date': '28 September 2026',
    'corps': r"""
<section class="resume">
<h2>In brief</h2>
<ul>
<li><strong>If space were a cubic lattice</strong> on which light propagates as it does in a numerical simulation of Maxwell’s equations, the most energetic photons would arrive late. In the gamma-ray burst GRB&nbsp;221009A, LHAASO observes no delay of this kind.</li>
<li><strong>The lattice spacing is therefore below [[a_resume]]&nbsp;m</strong>, for a cubic lattice in continuous time, with the most conservative method and the least favorable orientation, or below [[a_ml_resume]]&nbsp;m with the likelihood method. The energy scale of the lattice exceeds [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>This is not a new frontier.</strong> Beane, Davoudi and Savage already obtained the same order of magnitude in 2012 (about [[b_beane]]&nbsp;m) from cosmic rays. We obtain a comparable order of magnitude, with a different observable and different assumptions; the two bounds concern different models and are not interchangeable.</li>
<li><strong>New: the time step matters.</strong> If time is also divided into steps, as in any numerical simulation, the effect shrinks. At the largest stable time step, light no longer undergoes any dispersion along the eight diagonal directions of the cube: a single burst then allows no universal bound. For 95% of orientations, the lattice spacing remains below [[a95_sigma1]]&nbsp;m.</li>
<li><strong>A lattice whose leading error would be linear</strong> in <em>a</em> is excluded down to [[a_lineaire]]&nbsp;m, one tenth of the Planck length.</li>
<li><strong>A Planck-sized lattice spacing remains out of reach</strong>: its effect would be about [[facteur_planck]] times too weak for this test.</li>
<li><strong>While checking the literature</strong>, we found a conversion inconsistency in a 2025 paper (Xi and Shu): their quadratic bound appears to be overestimated by a factor of [[xs_facteur]].</li>
<li><strong>No detection, no probability of being simulated.</strong> The test bounds one specific architecture; it says nothing about the existence of a simulator.</li>
</ul>
</section>

<h2 id="question">1. The question under test</h2>
<p>A numerical simulation represents space by a finite number of points. A wave propagating through it does not behave exactly as in the continuum: its speed depends slightly on its wavelength. For light, the speed would therefore depend on the energy of the photons. The effect is tiny, but it accumulates over cosmological distances.</p>
<p>GRB&nbsp;221009A is the brightest gamma-ray burst ever recorded. The LHAASO observatory detected photons from it above 10&nbsp;TeV, which set out about two billion years ago (redshift <em>z</em>&nbsp;=&nbsp;[[z]]). If the speed of light depended on energy, high-energy photons would arrive after low-energy ones. The LHAASO collaboration searched for this delay and did not find it.</p>
<p>The question is therefore precise: <em>what lattice spacing does this zero delay still allow?</em> It assumes neither that every simulation would use a lattice, nor that a lattice would prove a simulation.</p>

<h2 id="modele">2. The model: Maxwell on a lattice</h2>
<p>We place the electromagnetic fields on a cubic lattice with spacing <em>a</em>, exactly as in the Yee scheme (1966) used in numerical simulations of Maxwell’s equations, or as in the Hamiltonian formulation of lattice electrodynamics (Kogut and Susskind, 1975). Time runs either continuously or in steps of \(\Delta t\). A plane wave with wave vector \(\mathbf k\) and angular frequency \(\omega\) then obeys the dispersion relation:</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>The scheme is stable only if \(c\,\Delta t\le a/\sqrt{3}\). We therefore write \(c\,\Delta t=\sigma a/\sqrt{3}\), with a Courant number \(0\le\sigma\le1\); \(\sigma=0\) corresponds to continuous time. For photons whose wavelength is much larger than the lattice spacing, the group velocity becomes, with \(E=\hbar\omega\):</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) depends on the direction \(\mathbf n\) of the photon relative to the lattice axes: \(Q=1\) along an axis, \(Q=1/3\) along a body diagonal. Three properties matter for what follows:</p>
<ul>
<li>the effect is <strong>quadratic</strong>: a lattice spacing ten times finer produces an effect a hundred times weaker;</li>
<li>photons are <strong>slowed down</strong>, never sped up, as long as the scheme is stable;</li>
<li>both polarizations propagate in the same way: <strong>no birefringence</strong>, so the very strong polarization constraints do not apply here.</li>
</ul>

<h2 id="lhaaso">3. Confronting the model with LHAASO</h2>
<p>LHAASO models a quadratic delay through \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) and publishes intervals on \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\), with \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV (equations 2, 3 and 5 of the paper). Matching the two expressions:</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>The delay accumulated between two photons of energies \(E_h\) and \(E_l\) is</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>with the LHAASO cosmology (<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc, Ω<sub>m</sub>&nbsp;=&nbsp;[[om]], Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]), which gives <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s. The measurement constrains only the combination \(a\sqrt{Q_{\mathrm{eff}}}\). LHAASO’s Table I gives, at 95%:</p>
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
<thead><tr><th>Method</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\), worst-case orientation (m)</th><th>\(a\), 95% of orientations (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML (calibrated)</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>The summary keeps the most conservative value, [[a_resume]]&nbsp;m: this is a presentation envelope, not a new interval. At this limit, a 1&nbsp;TeV photon would arrive at most [[retard_limite]]&nbsp;s after a [[e_bas]]&nbsp;TeV photon.</p>
<p>A few predictions, which are not measurements (a 1&nbsp;TeV photon compared with a [[e_bas]]&nbsp;TeV photon):</p>
<div class="tableau"><table>
<thead><tr><th>Lattice spacing</th><th>Predicted \(\eta_2\)</th><th>Predicted delay</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]] to [[p26_eta_max]]</td><td>[[p26_ret_min]] to [[p26_ret_max]]&nbsp;s</td><td>excluded for every orientation</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]] to [[p27_eta_max]]</td><td>[[p27_ret_min]] to [[p27_ret_max]]&nbsp;s</td><td>excluded near the axes (\(Q>\)&nbsp;[[q_cal_axe]]) by the calibrated method alone</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]] to [[p28_eta_max]]</td><td>[[p28_ret_min]] to [[p28_ret_max]]&nbsp;ms</td><td>not excluded</td></tr>
<tr><td>[[lpl]]&nbsp;m (Planck)</td><td>[[pl_eta_min]] to [[pl_eta_max]]</td><td>[[pl_ret_min]] to [[pl_ret_max]]&nbsp;s</td><td>out of reach</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. How far the bound holds</h2>
<h3>The orientation of the lattice</h3>
<p>We do not know how the lattice would be oriented relative to the direction of the burst. The main bound assumes the least favorable case, \(Q=1/3\). Over one million uniformly distributed directions, \(Q\) has a median of [[q_mediane]] and exceeds [[q_5]] in 95% of cases: the bound moves little, with [[ccf_95]]&nbsp;m for 95% of orientations and [[ccf_mediane]]&nbsp;m for the median orientation. These fractions are geometric: they are not probabilities about the Universe.</p>
<h3>Discrete time, the weak point of the bound</h3>
<p>A simulation advances in time steps. Discretizing time produces an error of opposite sign, which partly offsets the spatial error (the term \(-\sigma^{2}/3\)). For the conservative method:</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>Worst-case orientation</th><th>95% of orientations</th><th>Median orientation</th></tr></thead>
<tbody>
<tr><td>0 (continuous time)</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1 (maximum step)</td><td>[[s4_cdt]]</td><td>no bound</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>At the largest stable time step, the compensation is exact along the body diagonals, and not only at first order: there, the dispersion relation recovers \(\omega=ck\) for every wavelength. A simulation tuned this way would escape this test entirely if the burst lay along one of its eight diagonal directions. This is the main limitation of a bound drawn from a single source; several sources in different directions would remove it, because, barring coincidence, they cannot all be aligned with diagonals.</p>
<h3>A fixed lattice spacing, or one stretched by expansion</h3>
<p>We assume a fixed physical lattice spacing. If the lattice stretched with the Universe (comoving lattice spacing), the effect would no longer grow with redshift, and \(I_2\) would be replaced by \(I_0\): the bound weakens by a factor \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]], to [[comobile_a]]&nbsp;m. At <em>z</em>&nbsp;=&nbsp;[[z]], this choice matters little.</p>
<h3>More accurate schemes</h3>
<p>A simulator may use a higher-order scheme, whose leading error scales as \(a^{4}\). The effect then becomes quartic in energy, and the bound on \(a\) much weaker. LHAASO does not publish a constraint of this type for this burst; quantifying it would require the photon-by-photon data. Terms designed to compensate for dispersion would also escape the bound. These are different models, to be tested separately.</p>
<h3>What if the error were linear?</h3>
<p>A symmetric lattice produces no effect linear in \(a\). A discretization that did produce one, by breaking the symmetry between opposite directions of propagation, would fall under LHAASO’s linear bound, \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\): with a coefficient of order unity, \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m, i.e. one tenth of the Planck length. Any coarser lattice of this type is excluded.</p>
<h3>Validity of the calculation</h3>
<p>The expansion assumes \(aE/\hbar c\ll1\). At the bound, even for 20&nbsp;TeV photons, \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]. We also compared the expansion with the exact dispersion relation: for \(ak\)&nbsp;=&nbsp;[[ak_test]], the relative deviation does not exceed [[ecart_dispersion]], as expected.</p>

<h2 id="contexte">5. What this is worth compared with existing work</h2>
<p>Beane, Davoudi and Savage (2012) studied a simulation of lattice quantum chromodynamics. From the cutoff in the cosmic-ray spectrum, they derived the bound \(1/b\gtrsim10^{11}\)&nbsp;GeV on the inverse lattice spacing, i.e. \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m. Our conservative bound is [[beane_ratio]] times theirs; LHAASO’s likelihood methods give [[beane_ml_min]] to [[beane_ml_max]] times theirs. The two bounds are of the same order of magnitude, but they rest on different observables, particles and models: they do not confirm each other in the strict sense and are not interchangeable.</p>
<p>The Planck length, [[lpl]]&nbsp;m, lies eight orders of magnitude lower. For a lattice spacing of that size, the effect would be [[facteur_planck_exact]] times weaker than the limit. Since it grows with the square of the energy, photons about a hundred million times more energetic would be needed, far beyond anything observed: at this order, no time-of-flight test can reach a Planck-scale lattice.</p>

<h2 id="xi-shu">6. A check of the literature: Xi and Shu (2025)</h2>
<p>Xi and Shu analyzed the same burst with a different method and report \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV (their Table III), about [[xs_rapport_lhaaso]] times LHAASO’s bound. Starting from their own definitions, we do not recover this value.</p>
<ul>
<li>Their equation (3) makes the delay scale as \((E/E_{\mathrm{QG},n})^{n}\). For \(n=1\), their conversion (6), \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\) with \(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]], is consistent: we find [[xs_c1]].</li>
<li>For \(n=2\), their equation (7), \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\) with \(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]], keeps the \(1/\theta\) form. Applied to their limit \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV², it does reproduce their table ([[xs_eq7]]&nbsp;GeV). But since the delay is quadratic, their equation (3) requires a \(1/\sqrt{\theta_2}\) dependence: \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\), i.e. \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV.</li>
<li>The discrepancy is a factor of [[xs_facteur]]. A plausible explanation: \(\varepsilon^{2}\theta_2\) equals [[xs_eps2]], and [[xs_c2_imprime]] looks like the square root of [[xs_eps2_imprime]] with the root taken on the power of ten alone.</li>
</ul>
<p>Status: apparent inconsistency in version 1 of the paper, to be confirmed with the authors. We do not reanalyze their data and do not assess their other results. Once corrected, their bound would still be [[xs_vs_lhaaso]] times stronger than LHAASO’s. We do not use it.</p>

<h2 id="limites">7. What this test does not say</h2>
<ul>
<li>It detects nothing: a zero delay remains compatible with all the measurements.</li>
<li>It computes no probability that we are in a simulation; the “95%” refers to a physical parameter.</li>
<li>It bounds one specific architecture: cubic lattice, Yee scheme, fixed lattice spacing, no compensation.</li>
<li>Even a detected delay would not point to a computer: fundamentally discrete physics, or other quantum gravity effects, would produce the same signal.</li>
<li>LHAASO’s intervals rest on assumptions about the emission at the source; we inherit them.</li>
</ul>

<h2 id="suite">8. Next steps</h2>
<ol>
<li>Combine several sources seen in different directions, to close the blind spot of the diagonals.</li>
<li>Quantify higher-order schemes (an effect in \(a^{4}\)), which requires the photon-by-photon data.</li>
<li>Ask Xi and Shu to clarify their conversion.</li>
<li>Extend the test to other signatures of a lattice: cosmic-ray anisotropy, charged particles.</li>
</ol>

<h2 id="reproduire">9. Reproducing the results</h2>
<p>Everything is recomputed by a dependency-free Python script, which first checks its own formulas: expansion against exact dispersion, the exact diagonal case, round-trip conversions, the cosmological integral, and the mean of \(Q\) equal to 3/5.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>: the script (Python&nbsp;3.10 or later, standard library; code comments are in French)</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>: all computed values</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>: this note as a PDF</li>
</ul>
<p>An independent cross-check (numpy, scipy) recovers the cosmological integral to within 10<sup>−15</sup>, the orientation quantiles over ten million random draws, and the group velocity by numerically solving the dispersion relation.</p>
<p>This note replaces a first version dated 28 September 2026. It adds discrete time, orientation, the comoving lattice spacing, the linear effect and the comparison with Beane et al.</p>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a> (revised 13 February 2026): equations 2, 3 and 5, Table I.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a> (2025): equations 3, 6 and 7, Tables I and III.</li>
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
                   'checked against the imprint a cubic grid should leave on them.',
    'date': '28 September 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No.</strong> The test detects no significant departure from isotropy in the directions of the [[n_evt]] most energetic cosmic rays measured by the Pierre Auger Observatory: under the isotropic model, [[p4_pct]]% of simulated skies, put through the same search, show a cubic pattern at least as strong as the observed one.</p>
<p>This “no” has a limited reach. This number is neither the probability that chance explains the data, nor the probability that a grid exists. A weaker pattern is not excluded, and the absence of an observable cubic pattern does not prove the absence of a grid.</p>
</section>

<h2 id="explication">Explanation</h2>
<p>If our world were computed by a machine, space might be cut into tiny cubes, the way an image is made of pixels. In 2012, three physicists pointed out that such a cutting would leave a mark: the fastest particles in the Universe would not arrive equally from every direction. Some directions would be favoured, arranged like the faces or the corners of a cube.</p>
<p>Such particles exist: they are cosmic rays, atomic nuclei coming from space with far more energy than anything our accelerators produce. In Argentina, the Pierre Auger Observatory watches for them with a huge network of detectors. It has published the list of its [[n_evt]] most energetic catches, recorded between 2004 and 2020, with the direction each one came from.</p>
<p>We took these [[n_evt]] directions and asked whether they line up along a cube. Since nobody knows how such a cube would be turned, we tried [[n_orient]] positions. The best one fits the data a little. But when you try that many positions, you always find one that fits a little, even in a sky made by pure chance.</p>
<p>To settle it, we built [[n_ciels]] fake skies drawn at random, seen by the same observatory, and ran exactly the same search on each. In [[p4_pct]]% of them, a cube fits at least as well. The real sky therefore cannot be told apart from these fake skies. To speak of a hint, it would have had to beat almost all the fake skies.</p>
<p>Conclusion: no trace of a grid is detected. But this search could only see a strong pattern: with just [[n_evt]] particles, a faint one would go unnoticed. Moreover, the magnetic fields of our galaxy bend these particles on their way, which would blur part of the pattern. So this test does not prove that space is continuous; it shows that, where we could look, there is nothing.</p>

<h2 id="analyse">Detailed analysis</h2>

<h3>1. From the grid to a testable prediction</h3>
<p>On a cubic lattice of spacing \(a\), the discrete Laplacian replaces \(k^{2}\) with \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\). For a free field,</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>where \(\mathbf n\) is the propagation direction in the lattice axes. This is the same function \(Q\) as in test No. 1. More generally, any effect of the grid on arrival directions (propagation, a direction-dependent spectral cutoff) is a function of \(\mathbf n\) invariant under the cube group \(O_h\). Spherical harmonics invariant under \(O_h\) exist only for \(\ell=0,4,6,8,\dots\): the first allowed anisotropy is the cubic harmonic \(\ell=4\), proportional to \(Q-3/5\). This is our main test, fixed before opening the data; \(\ell=6\) is tested second. Beane, Davoudi and Savage write that the simulation “could reveal itself in the distributions of the highest energy cosmic rays exhibiting a degree of rotational symmetry breaking that reflects the structure of the underlying lattice”.</p>

<h3>2. The data</h3>
<p>Catalogue of the Pierre Auger Observatory (ApJS 264, 50, 2023): the [[n_evt]] highest-energy showers recorded from 1 January 2004 to 31 December 2020, from [[e_min]] to [[e_max]]&nbsp;EeV, with zenith angles up to [[zmax]]°. The open file also contains [[n_calib]] hybrid calibration events outside the [[n_evt]]: we discard them. We use the right ascension and declination reconstructed by the surface detector. The file’s SHA-256 fingerprint is checked at every run. At these energies the detection efficiency is full up to [[zmax]]°, so the exposure is purely geometric.</p>

<h3>3. The detector exposure</h3>
<p>A ground detector at latitude \(a_0\)&nbsp;=&nbsp;[[lat]]° accepting zenith angles \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]° has an exposure that is uniform in right ascension and, in declination \(\delta\) (Sommers, 2001):</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>The visible sky ends at \(\delta\)&nbsp;=&nbsp;[[dec_max]]°, that is [[ciel_pct]]% of the sphere. An isotropic sky seen by Auger is therefore not uniform: everything below compares the data with that sky, not with a uniform sphere.</p>

<h3>4. The statistic</h3>
<p>Let \(R\) be an orientation of the grid, with rows \(\mathbf e_k\), and \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). For the \(N\) observed directions:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>where \(\langle\cdot\rangle_\omega\) is the average over an isotropic sky weighted by the exposure. \(T>0\) signals an excess along the cube axes, \(T<0\) along its diagonals; the absolute value covers both. Since \(f\) is a degree-4 polynomial, \(T(R)\) depends on the data only through the 15 moments \(\sum_i\mathbf n_i^{\alpha}\); mean and variance are computed exactly by Gauss–Legendre quadrature. The maximum runs over [[n_orient]] orientations drawn uniformly (Haar measure). For \(\ell=6\) we take \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\), with \(\alpha\)&nbsp;=&nbsp;[[alpha6]] (that is \(-15/11\)), which makes it orthogonal to \(\ell=4\); the combined test maximises \(T_4^{2}+T_6^{2}\).</p>

<h3>5. Calibrating chance</h3>
<p>Searching for the best of [[n_orient]] orientations mechanically inflates \(Z_4\): it does not follow a normal law. We therefore draw [[n_ciels]] isotropic skies of \(N\) events according to the exposure and apply exactly the same maximisation to them. Under the “no grid” hypothesis, \(Z_4\) has median [[z4_50]]; it exceeds [[z4_95]] in 5% of cases, [[z4_99]] in 1% and [[z4_999]] in 0.1%. The p-value, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), thus includes the cost of choosing the orientation.</p>

<h3>6. Result</h3>
<div class="tableau"><table>
<thead><tr><th>Test</th><th>Observed statistic</th><th>p-value</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (main)</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\) and \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>At the best orientation, the mean of \(Q\) is [[q_obs]] against [[q_iso]] expected, an excess of [[q_ecart_pct]]% towards the axes. It is not significant: \(p\)&nbsp;=&nbsp;[[p4]] for the main test, and no secondary test falls below 0.05. The data are consistent with the absence of any cubic symmetry.</p>

<h3>7. What the test could see</h3>
<p>To quantify the sensitivity, we inject a cubic pattern: density proportional to \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Along an axis (\(Q=1\)), the flux is \(1+\varepsilon\) times the mean; along a diagonal (\(Q=1/3\)), it is \(1-2\varepsilon/3\) times the mean. With \(\varepsilon>0\), the excess therefore lies along the axes; with \(\varepsilon<0\), it lies along the diagonals and equals \(2\lvert\varepsilon\rvert/3\).</p>
<p>The 95% upper limit depends on the convention adopted for the orientation. If the orientation of the grid is drawn at random for each simulated sky ([[n_ciels_signal]] skies per amplitude), we obtain a limit averaged over orientations: \(\varepsilon\le\)&nbsp;[[eps_axes]] and \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]]. An average does not guarantee coverage for each orientation: we therefore redo the calculation at fixed orientation, for [[n_orient_fixes]] orientations including the one least visible to Auger ([[n_ciels_fixes]] skies per amplitude). The limit then ranges from [[eps_axes_fix_min]] to [[eps_axes_fix]] towards the axes and from [[eps_diag_fix_min]] to [[eps_diag_fix]] towards the diagonals; we keep the least constraining value. A flux excess of up to about [[exces_axes_pct]]% along the axes, or [[exces_diag_pct]]% along the diagonals, is therefore not excluded. This is a weak constraint, set by the small number of events, established for the orientations tested and not demonstrated for all of them.</p>
<p>The script first checks its own chain: invariance of \(Q\) under the cube group, exact polynomial expansion, zero exposure beyond [[dec_max]]°, \(T\) centred and reduced under isotropy, orthogonality of \(\ell=6\) to \(\ell=4\), and detection of a strong injected pattern, whose orientation is recovered to within [[ecart_orient]]°.</p>

<h3>8. Limits</h3>
<ul>
<li>Cosmic rays are charged: galactic and extragalactic magnetic fields deflect their directions, all the more for heavy nuclei. The pattern sought is broad (an axis and a diagonal are [[angle_diag]]° apart) and withstands modest deflections, but an imprint set at the source or during propagation would be partly erased.</li>
<li>We assume the grid is fixed with respect to distant stars (equatorial coordinates). A grid moving or rotating relative to them would need another test.</li>
<li>[[n_evt]] events and [[ciel_pct]]% of the sky: the statistical power is low, as the limit above shows.</li>
<li>Genuine astrophysical anisotropies may contain an \(\ell=4\) component. A positive result would have required ruling them out; a null result does not depend on them.</li>
<li>No probability of being simulated is computed: the test concerns one precise signature, that of a cubic grid.</li>
</ul>

<h3>9. Reproduce</h3>
<p>A Python script (numpy) redoes everything in a few minutes: reading and checking the data, self-tests, statistic, simulated skies, upper limits. The random generator has a fixed seed: results are identical from one run to the next.</p>
<p>Corrections of 28 September 2026, after review: the flux excess along the diagonals had been confused with the parameter \(\lvert\varepsilon\rvert\), whereas it equals \(2\lvert\varepsilon\rvert/3\); the fixed-orientation limit has been added; the verdict has been reworded so as not to present the p-value as a probability about the hypotheses.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-2/analyse.py" download>analyse.py</a>: the script</li>
<li><a href="/fichiers/test-2/resultats.json" download>resultats.json</a>: every computed value</li>
<li><a href="/fichiers/test-2/donnees/auger_catalogSD.csv" download>auger_catalogSD.csv</a>: the Pierre Auger Observatory data (CC BY-SA 4.0 licence)</li>
</ul>

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
                   'of test No. 1 and to bound the spacing of a cubic grid whatever its orientation.',
    'date': '28 September 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No.</strong> None of the [[n_src]] sources studied shows the delay a grid would produce. Combining their directions, a cubic grid with a spacing of [[a_exclue]]&nbsp;m or more is excluded, whatever its orientation and whatever its time step: the blind spot of test No.&nbsp;1 is closed.</p>
</section>

<h2 id="explication">Explanation</h2>
<p>If the Universe were computed on a grid, the way an image is made of pixels, light would not travel at quite the same speed in every direction. The most energetic light would fall very slightly behind, more so along the edges of the grid than along its diagonals. Over billions of years of travel, this delay would become measurable.</p>
<p>Test No.&nbsp;1 looked for this delay in the brightest gamma-ray burst ever observed, and saw nothing. But one loophole remained: if the simulation moves forward in time by the largest possible step, light no longer falls behind at all along the diagonals of the grid. A single source lying on a diagonal then allowed no conclusion.</p>
<p>Here we look at [[n_src]] sources at once, in different directions across the sky: three explosions of distant stars, four galaxies with a very active black hole, and the pulsar of the Crab Nebula. For each one, a team of astronomers has already measured that no delay appears, down to a certain fineness. We reread every paper, brought all the results to the same convention, then searched for the orientation that would best let a grid stay hidden, the one that weakens the limit the most.</p>
<p>It is impossible to place all the sources on diagonals at the same time. Even in the most favourable orientation, three sources remain far enough from a diagonal that a delay should have appeared. A grid whose cells measure at least [[a_exclue]]&nbsp;m is therefore excluded in every orientation. This size is still about [[planck_x]] times larger than the Planck length: a much finer grid remains entirely possible.</p>

<h2 id="analyse">Detailed analysis</h2>

<h3>1. The model</h3>
<p>As in test No.&nbsp;1: Maxwell’s equations on a cubic lattice of spacing \(a\) (Yee scheme), with time step \(c\,\Delta t=\sigma a/\sqrt{3}\) and \(0\le\sigma\le1\). At leading order,</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\,Q_{\mathrm{eff}}\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3},\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>Since \(1/3\le Q\le1\), \(Q_{\mathrm{eff}}\ge0\): the photon is always slowed down, and \(Q_{\mathrm{eff}}=0\) exactly along the body diagonals when \(\sigma=1\). At the final bound, \(aE/\hbar c\)&nbsp;=&nbsp;[[ae]] for a 20&nbsp;TeV photon: the expansion is valid.</p>

<h3>2. From published limits to a bound on the lattice spacing</h3>
<p>The eight papers describe a quadratic delay through \(v/c\simeq1-\tfrac{3}{2}(E/E_{\mathrm{QG},2})^{2}\), with the Jacob–Piran distance \(K_2=\int_0^{z}(1+z')^{2}\,dz'/H(z')\). Matching the two expressions,</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}}\quad\Longrightarrow\quad a\sqrt{Q_{\mathrm{eff}}(\mathbf n_i)}\le B_i=\frac{\sqrt{12}\,\hbar c}{E_i}.$$
<p>Rule fixed in advance: 95% limit, subluminal case, time of flight, and the least constraining method of each paper. Each limit is brought to the LHAASO cosmology through \(E_i\sqrt{K_2^{\mathrm{LHAASO}}(z_i)/K_2^{(i)}(z_i)}\); the factor does not exceed [[fc_max]]. Each published conversion is redone from the printed parameters and recovers the paper’s value (self-tests).</p>
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

<h3>3. The worst-case orientation</h3>
<p>For an orientation \(R\) of the lattice, the sources jointly impose</p>
$$a\le A(R)=\min_i\frac{B_i}{\sqrt{Q_{\mathrm{eff}}(R\mathbf n_i)}},$$
<p>a source on a diagonal at \(\sigma=1\) bounding nothing. We look for \(\max_R A(R)\): [[n_orient]] uniformly drawn rotations, constructed orientations (each source placed on a diagonal, then rotated about it), then a local refinement. A second, independent seed recovers the same maximum to within [[ecart_graines]]. The optimiser is validated on known cases: a single source bounds nothing at \(\sigma=1\), and two sources separated by the angle between two diagonals can be placed on diagonals together.</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>Worst-case orientation (m)</th><th>95% of orientations (m)</th></tr></thead>
<tbody>
<tr><td>0</td><td>[[pire0]]</td><td>[[q95_0]]</td></tr>
<tr><td>0.5</td><td>[[pire05]]</td><td>[[q95_05]]</td></tr>
<tr><td>0.9</td><td>[[pire09]]</td><td>[[q95_09]]</td></tr>
<tr><td>1</td><td>[[pire1]]</td><td>[[q95_1]]</td></tr>
</tbody>
</table></div>
<p>For \(\sigma<1\), nothing changes compared with test No.&nbsp;1: GRB&nbsp;221009A dominates, the other sources being [[x_min]] to [[x_max]] times less sensitive. Everything is decided at \(\sigma=1\): placing GRB&nbsp;221009A on a diagonal is no longer enough, because the other sources then see the lattice at an angle. The worst compromise moves GRB&nbsp;221009A [[ang_grb]]° away from the nearest diagonal (\(Q_{\mathrm{eff}}\)&nbsp;=&nbsp;[[qeff_grb]]) and balances [[n_actives]] constraints: GRB&nbsp;221009A, GRB&nbsp;090510 and the Crab. The bound is then [[pire1]]&nbsp;m, i.e. an energy scale \(\hbar c/a\ge\)&nbsp;[[echelle]]&nbsp;GeV. Since \(A(R)\) increases with \(\sigma\) for every orientation, the bound holds for every \(\sigma\le1\). At \(\sigma=1\), the median orientation gives [[med1]]&nbsp;m.</p>
<p>Closing the gap was not a foregone conclusion: GRB&nbsp;190114C and GRB&nbsp;090510 are [[ang_190_090]]° apart, almost the angle between two diagonals ([[ang_diag]]°), and GRB&nbsp;090510 and PKS&nbsp;2155-304 are only [[ang_090_pks]]° from each other. It is the diversity of the rest of the sky that closes the blind spot.</p>

<h3>4. Robustness</h3>
<p>Worst-case orientation at \(\sigma=1\), depending on the choices:</p>
<ul>
<li>without GRB&nbsp;221009A: [[v_sans_lhaaso]]&nbsp;m, the blind spot stays closed;</li>
<li>published limits without cosmology conversion: [[v_sans_cosmo]]&nbsp;m;</li>
<li>Fermi with source-intrinsic effects (Table V of the paper): [[v_fermi]]&nbsp;m;</li>
<li>gamma-ray bursts only: [[v_sursauts]]&nbsp;m;</li>
<li>blazars and pulsar only: [[v_blazars]]&nbsp;m.</li>
</ul>

<h3>5. Comparisons</h3>
<p>The bound valid for every orientation and every time step is [[x_test1]] times weaker than that of test No.&nbsp;1 in continuous time. Beane, Davoudi and Savage obtained \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m from the cutoff in the cosmic-ray spectrum; our continuous-time bound is [[x_beane0]] times theirs, and our universal bound [[x_beane]] times.</p>

<h3>6. Limits</h3>
<ul>
<li>For each orientation, the combined bound takes the most constraining of the published 95% limits, one at a time: this is not a combined likelihood, which the papers do not publish. With three limits active at the worst-case orientation, the guaranteed coverage is at least [[couverture]]%, not 95%.</li>
<li>Each paper assumes that no source-intrinsic lag offsets or mimics the delay.</li>
<li>The redshifts of Mrk&nbsp;421 and PG&nbsp;1553+113 are uncertain; neither source is active at the worst-case orientation. The distance of the Crab pulsar, an active source, is included in MAGIC’s uncertainties.</li>
<li>A higher-order scheme (error in \(a^{4}\)), compensating terms, or a non-cubic lattice or one stretched by expansion escape this bound.</li>
<li>Secondary analysis: no photon is reanalysed. The fractions of orientations are geometric, not probabilities about the Universe.</li>
</ul>

<h3>7. Reproduce</h3>
<p>The script redoes everything in a few seconds and first checks its formulas and every published conversion. Every input figure is cited, with page and table, in <code>sources.md</code>.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-3/analyse.py" download>analyse.py</a>: the script</li>
<li><a href="/fichiers/test-3/resultats.json" download>resultats.json</a>: every computed value</li>
<li><a href="/fichiers/test-3/sources.md" download>sources.md</a>: the citation for each input figure</li>
</ul>

<h2 id="sources">Sources</h2>
<ol class="sources">
<li>LHAASO Collaboration, GRB 221009A, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>, Table I.</li>
<li>MAGIC Collaboration, GRB 190114C, <a href="https://arxiv.org/abs/2001.09728v4">arXiv:2001.09728v4</a>, Table I.</li>
<li>Fermi-LAT Collaboration, GRB 090510, <a href="https://arxiv.org/abs/1305.3463v1">arXiv:1305.3463v1</a>, Tables IV and V.</li>
<li>H.E.S.S. Collaboration, Mrk 501, <a href="https://arxiv.org/abs/1901.05209v1">arXiv:1901.05209v1</a>.</li>
<li>MAGIC Collaboration, Mrk 421, <a href="https://arxiv.org/abs/2406.07140v1">arXiv:2406.07140v1</a>, Table 2.</li>
<li>H.E.S.S. Collaboration, PKS 2155-304, <a href="https://arxiv.org/abs/1101.3650v2">arXiv:1101.3650v2</a>.</li>
<li>H.E.S.S. Collaboration, PG 1553+113, <a href="https://arxiv.org/abs/1501.05087v1">arXiv:1501.05087v1</a>, Table 5.</li>
<li>MAGIC Collaboration, Crab pulsar, <a href="https://arxiv.org/abs/1709.00346v1">arXiv:1709.00346v1</a>, Table 6.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>.</li>
<li>Coordinates: <a href="https://simbad.cds.unistra.fr/simbad/">SIMBAD</a> (CDS, Strasbourg).</li>
</ol>
""",
}

ARTICLE_4 = {
    'titre': 'Does quantum randomness betray a program?',
    'description': 'Millions of bits drawn from quantum experiments, put through the tests that unmask '
                   'the pseudorandom generators a simulation would use.',
    'date': '28 September 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Verdict</h2>
<p><strong>No.</strong> In the raw quantum bits tested, no signature of a pseudorandom generator appears, whereas the same tests unmask four simple generators used as controls. One point must be made at the outset: the rule fixed before the analysis is triggered by the IBM data as published, but the cause has been identified — one of the nine machines stayed stuck at 0 or at 1 for entire series — and this defect does not have the structure of a generator. The decision to set that machine aside was made after seeing the data; we flag it as such.</p>
<p>This “no” has a limited reach: it rules out a simulation that would draw its quantum measurements from a simple generator, not a simulation that would use a cryptographic-quality generator, indistinguishable by design.</p>
</section>

<h2 id="explication">Explanation</h2>
<p>If the world were a simulation, the result of every quantum measurement, 0 or 1, would have to be produced. Physics says this result is unpredictable by nature. A computer, however, cannot produce true randomness: it manufactures it by following a recipe of calculations. A frugal simulation would use a quick, simple recipe, and simple recipes leave fingerprints: repetitions, hidden regularities, a structure that calculation can uncover.</p>
<p>So we took sequences of 0s and 1s produced by real quantum experiments and published by their authors, and searched them for these fingerprints. First difficulty: most public sources of quantum randomness put their results through a mathematical “blender” before publishing them. This blender is designed to erase all structure; testing its output says nothing about the source. We tested these data anyway, but they do not count towards the verdict.</p>
<p>Two raw sources remain: a device using entangled photons at the University of Portland (Oregon), which publishes its bits just as they come, and nine IBM quantum computers that were asked, millions of times, to toss a coin with a single qubit. The photons pass every test. The IBM machines give slightly too many 0s, a known defect explained by the authors of the data; once this imbalance is corrected, they pass. One of them, Belem, stayed stuck for entire series of measurements: a breakdown, not a recipe of calculations.</p>
<p>The controls behave as expected: the simple recipes are unmasked, including a very widely used generator that nonetheless passes NIST’s official test battery; the sophisticated recipes are not, and neither are the digits of the square root of 2, even though they are perfectly computable. This is the limit of this test: a carefully built simulation would leave no trace of this kind.</p>

<h2 id="analyse">Detailed analysis</h2>

<h3>1. What can be tested</h3>
<p>A statistical test only tells us about the last processing a bit sequence has undergone: output hashed by a cryptographic function looks perfectly random whatever the input. We tested [[bits_total]] bits, [[bits_bruts]] of them raw:</p>
<div class="tableau"><table>
<thead><tr><th>Dataset</th><th>Origin</th><th>Processing</th><th>Bits</th></tr></thead>
<tbody>
<tr><td>parity</td><td>polarisation-entangled photons (Kavulich et al., 2021)</td><td>none</td><td>[[n_parity]]</td></tr>
<tr><td>ibm</td><td>one qubit, Hadamard gate, measurement; nine machines (Root and Becker, 2024)</td><td>none</td><td>[[n_ibm]]</td></tr>
<tr><td>anu</td><td>vacuum fluctuations, ANU</td><td>AES-128</td><td>[[n_anu]]</td></tr>
<tr><td>beacon</td><td>NIST Beacon 2.0</td><td>SHA-512</td><td>[[n_beacon]]</td></tr>
</tbody>
</table></div>
<p>Only parity and ibm say anything about the nature of quantum randomness. The raw data from NIST’s loophole-free Bell test (2015) were not used: their measurement choices combine physical sources with a pseudorandom source, and their detection outcomes are not uniform bits. For the Beacon, the published chain of commitments was verified on [[engagements]] consecutive pairs.</p>

<h3>2. Level 1: the NIST SP 800-22 battery</h3>
<p>The 15 tests of the official battery are reimplemented and reproduce the [[annexe_n]] p-values of Appendix B of the document to within [[annexe_ecart]] ([[annexe_ecart_chev]] for one test). The data are cut into [[n_seq]] sequences of 10<sup>6</sup> bits; the [[np1]] p-values form a single family, corrected by Holm’s method at a family-wise error rate of 1%.</p>
<ul>
<li>parity: [[par_np1]] p-values, no rejection (smallest adjusted p-value: [[par_p1]]); fraction of bits equal to 1: [[par_frac]].</li>
<li>anu and beacon: no rejection (smallest adjusted p-value for anu: [[anu_p1]]).</li>
<li>ibm: [[ibm_rej1]] rejections out of [[ibm_np1]]; fraction of bits equal to 1: [[ibm_frac]], a departure of [[ibm_z]] standard deviations. Without the Belem machine, the von Neumann extractor, which removes a constant bias exactly, leaves [[vn_bits]] bits and no rejection out of [[vn_np]] p-values ([[vn_p]]): the failures come from the bias described by the authors.</li>
</ul>

<h3>3. Level 2: the signatures of a generator</h3>
<p>The NIST battery says whether a sequence departs from ideal randomness, not why. Three tests target the defects specific to algorithmic generators:</p>
<ul>
<li><strong>Linear complexity.</strong> The Berlekamp–Massey algorithm gives the length \(L\) of the shortest linear feedback shift register that reproduces a segment of \(n\) bits. For a random sequence, \(L\simeq n/2\); any linear generator over \(\mathrm{GF}(2)\) whose state has fewer than \(n/2\) bits gives \(L\lt n/2\). Segments of [[seg_bm]] bits, read contiguously or keeping one bit in 48 and one bit in 64: a state of up to [[etat_max]] bits is covered.</li>
<li><strong>Repetitions.</strong> Each 64-bit window is compared with all the others; the expected number of identical pairs is of the order of [[rep_attendu]]. A single repetition would signal a period or a reused seed.</li>
<li><strong>Long-range correlations.</strong> Autocorrelation at lags 17 to [[lag_max]], with Bonferroni correction.</li>
</ul>
<p>Main family, Holm at 1% over [[np2]] p-values: parity rejects nothing ([[par_p2]]); its largest deviation of \(L\) from \(n/2\) is [[par_ecart_l]]; no repetition; long-range correlations: [[par_auto]]. anu and beacon reject nothing. ibm rejects [[ibm_rej2]] times.</p>

<h3>4. IBM’s rejections: a stuck machine</h3>
<p>The IBM data consist of [[ibm_essais]] trials of 8&nbsp;192 shots each. Of these, [[ibm_const]] are constant ([[ibm_const0]] entirely 0, [[ibm_const1]] entirely 1) and [[ibm_quasi]] others are more than 99% constant; all of them come from the Belem machine. The [[ibm_paires]] pairs of identical windows are all runs of equal bits: among windows of ordinary composition, there are [[ibm_paires_typ]]. A frozen output is not the output of a pseudorandom generator: it is the absence of output.</p>
<p>The decision to set Belem aside was made after seeing the data: it is therefore a secondary analysis, with its own Holm correction, and the result of the original rule remains published. On the other eight machines ([[sb_bits]] bits), level 2 rejects nothing ([[sb_np2]] p-values, smallest adjusted p-value [[sb_p2]]); the largest deviation of \(L\) from \(n/2\) is [[sb_ecart_l]] and there is no repetition. A correlation at lag 1 is present ([[sb_r1]], i.e. [[sb_z1]] standard deviations): a short-range measurement defect, unrelated to the structure of a generator. On these machines, level 1 rejects [[sb_rej1]] times out of [[sb_np1]], because of the bias.</p>

<h3>5. The controls</h3>
<p>The same analysis chain is applied to [[bits_ctrl]] bits from each known generator; the script stops if a control does not behave as expected.</p>
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
<p>The Mersenne Twister shows that level 2 adds genuine sensitivity to the official battery. PCG64, SHA-256 and \(\sqrt{2}\) show that an entirely deterministic sequence can have no detectable signature.</p>

<h3>6. Limits</h3>
<ul>
<li>A cryptographic-quality generator is indistinguishable: this test rules out a simulation that would use a simple generator, not a carefully built one. The SP 800-22 document says so itself: no set of tests replaces cryptanalysis.</li>
<li>Coverage of level 2: a linear generator is detected only if its state has fewer than [[etat_max]] bits; a repetition, only if the period is shorter than the data.</li>
<li>Modest volume of raw data, and neither of the two raw sources is certified by a loophole-free Bell test.</li>
<li>The exclusion of the Belem machine is a post hoc decision; its cause is documented and the raw result is published.</li>
<li>The ANU and Beacon datasets measure only the quality of AES-128 and SHA-512.</li>
</ul>

<h3>7. Reproduce</h3>
<p>The data are rebuilt by <code>telecharger.py</code>, which checks their fingerprints; <code>analyse.py</code> then runs offline in under two minutes, self-tests included.</p>
<pre><code>python3 telecharger.py
python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-4/analyse.py" download>analyse.py</a>: the analysis</li>
<li><a href="/fichiers/test-4/telecharger.py" download>telecharger.py</a>: the verified download of the data</li>
<li><a href="/fichiers/test-4/resultats.json" download>resultats.json</a>: every computed value</li>
<li><a href="/fichiers/test-4/sources.md" download>sources.md</a>: the citation for each claim</li>
</ul>

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
