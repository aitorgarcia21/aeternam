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
<li><strong>The lattice spacing is therefore below [[a_resume]]&nbsp;m</strong> with the most conservative method and the least favorable orientation, or below [[a_ml_resume]]&nbsp;m with the likelihood method. The energy scale of the lattice exceeds [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>This is not a new frontier.</strong> Beane, Davoudi and Savage already obtained the same order of magnitude in 2012 (about [[b_beane]]&nbsp;m) from cosmic rays. The present result confirms it independently, through a different observable.</li>
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
<p>Beane, Davoudi and Savage (2012) studied a simulation of lattice quantum chromodynamics. From the cutoff in the cosmic-ray spectrum, they derived the bound \(1/b\gtrsim10^{11}\)&nbsp;GeV on the inverse lattice spacing, i.e. \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m. Our conservative bound is [[beane_ratio]] times theirs; LHAASO’s likelihood methods give [[beane_ml_min]] to [[beane_ml_max]] times theirs. The two approaches therefore agree in order of magnitude, with different observables, particles and assumptions: this is a confirmation, not a record.</p>
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
