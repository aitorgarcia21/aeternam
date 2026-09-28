"""Espagnol : traduction de la source française (fr.py).

Mêmes marqueurs [[…]], mêmes formules et même structure HTML que la source.
Vérifier avec : python3 site/generer.py --verifier es
"""
NOM = 'Español'
HTML_LANG = 'es'
HREFLANG = 'es'
DIR = 'ltr'
LOCALE_OG = 'es_ES'
DECIMALE = ','

UI = {
    'devise': 'Investigación sobre la teoría de la simulación.',
    'description_site': 'aeternam — investigación sobre la teoría de la simulación',
    'travaux': 'Trabajos',
    'langue': 'Idioma',
    'surtitre': 'Investigación · Prueba n.º 1',
    'meta': 'versión 2 · análisis secundario reproducible',
    'verdict': 'Veredicto hasta hoy: ninguna huella de simulación en los datos examinados.',
    'fichier_pdf': 'aeternam-test-1-es.pdf',
}

ARTICLE = {
    'titre': 'Una red cúbica frente a GRB 221009A',
    'description': 'Lo que los fotones observados por LHAASO imponen al espaciado de la red de un espacio discreto, '
                   'y hasta dónde llega esa restricción.',
    'date': '28 de septiembre de 2026',
    'corps': r"""
<section class="resume">
<h2>En resumen</h2>
<ul>
<li><strong>Si el espacio fuera una red cúbica</strong> en la que la luz se propagara como en una simulación numérica de las ecuaciones de Maxwell, los fotones más energéticos llegarían con retraso. En el estallido GRB&nbsp;221009A, LHAASO no observa ningún retraso de este tipo.</li>
<li><strong>El espaciado de la red es, por tanto, inferior a [[a_resume]]&nbsp;m</strong> con el método más conservador y la orientación más desfavorable, o a [[a_ml_resume]]&nbsp;m con el método de verosimilitud. La escala de energía de la red supera los [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>No es una frontera nueva.</strong> Beane, Davoudi y Savage ya obtuvieron el mismo orden de magnitud en 2012 (alrededor de [[b_beane]]&nbsp;m) a partir de los rayos cósmicos. Este resultado lo confirma de forma independiente, mediante otro observable.</li>
<li><strong>Novedad: el paso de tiempo importa.</strong> Si el tiempo también está discretizado, como en toda simulación numérica, el efecto disminuye. Con el paso máximo estable, la luz ya no sufre ninguna dispersión a lo largo de las ocho direcciones diagonales del cubo: un solo estallido no permite entonces ninguna cota universal. Para el 95&nbsp;% de las orientaciones, el espaciado sigue siendo inferior a [[a95_sigma1]]&nbsp;m.</li>
<li><strong>Una red cuyo error dominante sea lineal</strong> en <em>a</em> queda excluida hasta [[a_lineaire]]&nbsp;m, una décima parte de la longitud de Planck.</li>
<li><strong>Un espaciado del tamaño de Planck sigue fuera de alcance</strong>: su efecto sería demasiado débil para esta prueba, en un factor de aproximadamente [[facteur_planck]].</li>
<li><strong>Al revisar la bibliografía</strong>, detectamos una incoherencia de conversión en un artículo de 2025 (Xi y Shu): su cota cuadrática parece sobrestimada en un factor [[xs_facteur]].</li>
<li><strong>Ninguna detección, ninguna probabilidad de estar simulados.</strong> La prueba acota una arquitectura concreta; no dice nada sobre la existencia de un simulador.</li>
</ul>
</section>

<h2 id="question">1. La pregunta puesta a prueba</h2>
<p>Una simulación numérica representa el espacio mediante un número finito de puntos. Una onda que se propaga en él no se comporta exactamente como en el continuo: su velocidad depende ligeramente de su longitud de onda. En el caso de la luz, la velocidad dependería, pues, de la energía de los fotones. El efecto es minúsculo, pero se acumula a lo largo de distancias cosmológicas.</p>
<p>GRB&nbsp;221009A es el estallido de rayos gamma más brillante jamás registrado. El observatorio LHAASO detectó fotones de este estallido por encima de 10&nbsp;TeV, emitidos hace unos dos mil millones de años (corrimiento al rojo <em>z</em>&nbsp;=&nbsp;[[z]]). Si la velocidad de la luz dependiera de la energía, los fotones de alta energía llegarían después de los de baja energía. La colaboración LHAASO buscó ese retraso y no lo encontró.</p>
<p>La pregunta es, por tanto, precisa: <em>¿qué espaciado de la red sigue siendo compatible con este retraso nulo?</em> No presupone ni que toda simulación utilice una red ni que una red sea prueba de una simulación.</p>

<h2 id="modele">2. El modelo: Maxwell en una red</h2>
<p>Colocamos los campos electromagnéticos en una red cúbica de espaciado <em>a</em>, exactamente como en el esquema de Yee (1966) que utilizan las simulaciones numéricas de las ecuaciones de Maxwell, o como en la formulación hamiltoniana de la electrodinámica en red (Kogut y Susskind, 1975). El tiempo transcurre de forma continua o por pasos \(\Delta t\). Una onda plana de vector de onda \(\mathbf k\) y frecuencia angular \(\omega\) satisface entonces la relación de dispersión:</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>El esquema solo es estable si \(c\,\Delta t\le a/\sqrt{3}\). Escribimos entonces \(c\,\Delta t=\sigma a/\sqrt{3}\), con un número de Courant \(0\le\sigma\le1\); \(\sigma=0\) corresponde al tiempo continuo. Para fotones cuya longitud de onda es mucho mayor que el espaciado, la velocidad de grupo pasa a ser, con \(E=\hbar\omega\):</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) depende de la dirección \(\mathbf n\) del fotón respecto a los ejes de la red: \(Q=1\) a lo largo de un eje y \(Q=1/3\) a lo largo de una diagonal del cubo. Tres propiedades serán importantes en lo que sigue:</p>
<ul>
<li>el efecto es <strong>cuadrático</strong>: un espaciado diez veces menor produce un efecto cien veces más débil;</li>
<li>los fotones se <strong>ralentizan</strong>, nunca se aceleran, mientras el esquema sea estable;</li>
<li>las dos polarizaciones se propagan de la misma manera: <strong>no hay birrefringencia</strong>, por lo que las restricciones basadas en la polarización, muy estrictas, no se aplican aquí.</li>
</ul>

<h2 id="lhaaso">3. La confrontación con LHAASO</h2>
<p>LHAASO describe un retraso cuadrático mediante \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) y publica intervalos para \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\), con \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV (ecuaciones 2, 3 y 5 del artículo). Por identificación:</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>El retraso acumulado entre dos fotones de energías \(E_h\) y \(E_l\) se escribe</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>con la cosmología de LHAASO (<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc, Ω<sub>m</sub>&nbsp;=&nbsp;[[om]], Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]), que da <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s. La medición solo restringe la combinación \(a\sqrt{Q_{\mathrm{eff}}}\). La tabla I de LHAASO recoge, al 95&nbsp;%:</p>
<div class="tableau"><table>
<thead><tr><th>Método</th><th>Límite inferior</th><th>Mejor ajuste</th><th>Límite superior</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML (calibrada)</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>Los tres intervalos contienen el cero: no se detecta ningún retraso. Los tres métodos analizan el mismo estallido; no los combinamos. Un límite superior \(U\) para \(\eta_2\) implica</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>En tiempo continuo se obtiene:</p>
<div class="tableau"><table>
<thead><tr><th>Método</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\), orientación más desfavorable (m)</th><th>\(a\), 95&nbsp;% de las orientaciones (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML (calibrada)</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>El resumen adopta el valor más conservador, [[a_resume]]&nbsp;m: es una envolvente de presentación, no un nuevo intervalo. Con ese valor límite, un fotón de 1&nbsp;TeV llegaría como máximo [[retard_limite]]&nbsp;s después de un fotón de [[e_bas]]&nbsp;TeV.</p>
<p>Algunas predicciones, que no son mediciones (fotón de 1&nbsp;TeV frente a un fotón de [[e_bas]]&nbsp;TeV):</p>
<div class="tableau"><table>
<thead><tr><th>Espaciado</th><th>\(\eta_2\) predicho</th><th>Retraso predicho</th><th>Veredicto</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]] a [[p26_eta_max]]</td><td>[[p26_ret_min]] a [[p26_ret_max]]&nbsp;s</td><td>excluido para cualquier orientación</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]] a [[p27_eta_max]]</td><td>[[p27_ret_min]] a [[p27_ret_max]]&nbsp;s</td><td>excluido cerca de los ejes (\(Q>\)&nbsp;[[q_cal_axe]]) solo por el método calibrado</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]] a [[p28_eta_max]]</td><td>[[p28_ret_min]] a [[p28_ret_max]]&nbsp;ms</td><td>no excluido</td></tr>
<tr><td>[[lpl]]&nbsp;m (Planck)</td><td>[[pl_eta_min]] a [[pl_eta_max]]</td><td>[[pl_ret_min]] a [[pl_ret_max]]&nbsp;s</td><td>fuera de alcance</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. Hasta dónde resiste la cota</h2>
<h3>La orientación de la red</h3>
<p>Se desconoce cómo estaría orientada la red respecto a la dirección del estallido. La cota principal adopta el caso menos favorable, \(Q=1/3\). Sobre un millón de direcciones distribuidas uniformemente, la mediana de \(Q\) es [[q_mediane]], y en el 95&nbsp;% de los casos supera [[q_5]]: la cota varía poco, con [[ccf_95]]&nbsp;m para el 95&nbsp;% de las orientaciones y [[ccf_mediane]]&nbsp;m para la orientación mediana. Estas fracciones son geométricas: no son probabilidades sobre el Universo.</p>
<h3>El tiempo discreto, punto débil de la cota</h3>
<p>Una simulación avanza por pasos de tiempo. Discretizar el tiempo produce un error de signo opuesto, que compensa en parte el del espacio (el término \(-\sigma^{2}/3\)). Para el método conservador:</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>Orientación más desfavorable</th><th>95&nbsp;% de las orientaciones</th><th>Orientación mediana</th></tr></thead>
<tbody>
<tr><td>0 (tiempo continuo)</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1 (paso máximo)</td><td>[[s4_cdt]]</td><td>sin cota</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>Con el paso máximo estable, la compensación es exacta a lo largo de las diagonales del cubo, y no solo a primer orden: en ellas, la relación de dispersión vuelve a dar \(\omega=ck\) para cualquier longitud de onda. Una simulación ajustada de este modo escaparía por completo a esta prueba si la dirección del estallido coincidiera con una de sus ocho direcciones diagonales. Esta es la principal limitación de una cota obtenida a partir de una sola fuente; varias fuentes en direcciones diferentes la eliminarían, porque, salvo coincidencia, no pueden estar todas alineadas con diagonales.</p>
<h3>Un espaciado fijo o estirado por la expansión</h3>
<p>Suponemos un espaciado físico fijo. Si la red se estirara con el Universo (espaciado comóvil), el efecto ya no crecería con el corrimiento al rojo, y habría que sustituir \(I_2\) por \(I_0\): la cota se debilita en un factor \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]], es decir, [[comobile_a]]&nbsp;m. Para <em>z</em>&nbsp;=&nbsp;[[z]], esta elección apenas importa.</p>
<h3>Esquemas más precisos</h3>
<p>Un simulador puede emplear un esquema de orden superior, cuyo error dominante varía como \(a^{4}\). El efecto pasa a ser entonces cuártico en la energía, y la cota sobre \(a\), mucho más débil. LHAASO no publica ninguna restricción de este tipo para este estallido; cuantificarla requeriría los datos fotón a fotón. También escaparían a la cota unos términos diseñados para compensar la dispersión. Son otros modelos, que habría que poner a prueba por separado.</p>
<h3>¿Y si el error fuera lineal?</h3>
<p>Una red simétrica no produce ningún efecto lineal en \(a\). Una discretización que sí lo produjera, al romper la simetría entre los dos sentidos de propagación, quedaría sujeta a la cota lineal de LHAASO, \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\): con un coeficiente de orden uno, \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m, es decir, una décima parte de la longitud de Planck. Cualquier red de este tipo con un espaciado mayor queda excluida.</p>
<h3>La validez del cálculo</h3>
<p>El desarrollo en serie supone \(aE/\hbar c\ll1\). En el valor de la cota, incluso para fotones de 20&nbsp;TeV, \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]. También comparamos el desarrollo con la relación de dispersión exacta: para \(ak\)&nbsp;=&nbsp;[[ak_test]], la desviación relativa no supera [[ecart_dispersion]], como se esperaba.</p>

<h2 id="contexte">5. Su valor frente a los trabajos anteriores</h2>
<p>Beane, Davoudi y Savage (2012) estudiaron una simulación de la cromodinámica cuántica en red. A partir del corte del espectro de los rayos cósmicos, obtuvieron para el inverso del espaciado la cota \(1/b\gtrsim10^{11}\)&nbsp;GeV, es decir, \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m. Nuestra cota conservadora vale [[beane_ratio]] veces la suya; los métodos de verosimilitud de LHAASO dan entre [[beane_ml_min]] y [[beane_ml_max]] veces la suya. Así pues, ambos enfoques coinciden en el orden de magnitud, con observables, partículas e hipótesis diferentes: es una confirmación, no un récord.</p>
<p>La longitud de Planck, [[lpl]]&nbsp;m, queda ocho órdenes de magnitud por debajo. Para un espaciado de ese tamaño, el efecto sería [[facteur_planck_exact]] veces más débil que el límite. Como crece con el cuadrado de la energía, harían falta fotones unos cien millones de veces más energéticos, muy por encima de todo lo observado: a este orden, ninguna prueba de tiempo de vuelo puede alcanzar una red de Planck.</p>

<h2 id="xi-shu">6. Una verificación de la bibliografía: Xi y Shu (2025)</h2>
<p>Xi y Shu analizaron el mismo estallido con otro método y anuncian \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV (su tabla III), unas [[xs_rapport_lhaaso]] veces la cota de LHAASO. Rehaciendo el cálculo con sus propias definiciones, no obtenemos ese valor.</p>
<ul>
<li>Su ecuación (3) expresa el retraso en función de \((E/E_{\mathrm{QG},n})^{n}\). Para \(n=1\), su conversión (6), \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\) con \(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]], es coherente: obtenemos [[xs_c1]].</li>
<li>Para \(n=2\), su ecuación (7), \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\) con \(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]], conserva la forma en \(1/\theta\). Aplicada a su límite \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV², reproduce efectivamente su tabla ([[xs_eq7]]&nbsp;GeV). Pero, como el retraso es cuadrático, su ecuación (3) impone una dependencia en \(1/\sqrt{\theta_2}\): \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\), es decir, \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV.</li>
<li>La discrepancia es de un factor [[xs_facteur]]. Explicación plausible: \(\varepsilon^{2}\theta_2\) vale [[xs_eps2]], y [[xs_c2_imprime]] se parece a la raíz cuadrada de [[xs_eps2_imprime]] tomada solo sobre la potencia de diez.</li>
</ul>
<p>Estado: incoherencia aparente en la versión 1 del artículo, a confirmar con los autores. No reanalizamos sus datos ni juzgamos sus demás resultados. Una vez corregida, su cota seguiría siendo [[xs_vs_lhaaso]] veces más fuerte que la de LHAASO. No la utilizamos.</p>

<h2 id="limites">7. Lo que esta prueba no dice</h2>
<ul>
<li>No detecta nada: un retraso nulo sigue siendo compatible con todas las mediciones.</li>
<li>No calcula ninguna probabilidad de que estemos en una simulación; el «95&nbsp;%» se refiere a un parámetro físico.</li>
<li>Acota una arquitectura concreta: red cúbica, esquema de Yee, espaciado fijo, sin compensación.</li>
<li>Ni siquiera un retraso detectado señalaría a un ordenador: una física fundamentalmente discreta, u otros efectos de gravedad cuántica, producirían la misma señal.</li>
<li>Los intervalos de LHAASO se basan en hipótesis sobre la emisión de la fuente; nosotros las heredamos.</li>
</ul>

<h2 id="suite">8. Próximos pasos</h2>
<ol>
<li>Combinar varias fuentes observadas en direcciones diferentes, para cerrar el punto ciego de las diagonales.</li>
<li>Cuantificar los esquemas de orden superior (efecto en \(a^{4}\)), lo que requiere los datos fotón a fotón.</li>
<li>Pedir a Xi y Shu que aclaren su conversión.</li>
<li>Extender la prueba a otras firmas de una red: anisotropía de los rayos cósmicos, partículas cargadas.</li>
</ol>

<h2 id="reproduire">9. Reproducir</h2>
<p>Todo se recalcula con un script de Python sin dependencias, que primero verifica sus propias fórmulas: desarrollo frente a dispersión exacta, diagonal exacta, conversiones de ida y vuelta, integral cosmológica, media de \(Q\) igual a 3/5.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>: el script (Python&nbsp;3.10 o posterior, biblioteca estándar), con comentarios en francés</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>: todos los valores calculados</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>: esta nota en PDF</li>
</ul>
<p>Una verificación cruzada independiente (numpy, scipy) reproduce la integral cosmológica con una precisión de 10<sup>−15</sup>, los cuantiles de orientación con diez millones de muestras aleatorias y la velocidad de grupo mediante la resolución numérica de la relación de dispersión.</p>
<p>Esta nota sustituye a una primera versión del 28 de septiembre de 2026. Añade el tiempo discreto, la orientación, el espaciado comóvil, el efecto lineal y la comparación con Beane et al.</p>

<h2 id="sources">Fuentes</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a> (revisión del 13 de febrero de 2026): ecuaciones 2, 3 y 5, tabla I.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a> (2025): ecuaciones 3, 6 y 7, tablas I y III.</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302 (1966).</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395 (1975).</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House: dispersión numérica y estabilidad del esquema de Yee.</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>: constantes fundamentales.</li>
</ol>
""",
}

ARTICLE_2 = {
    'titre': '¿Dibujan los rayos cósmicos una cuadrícula?',
    'description': 'Las partículas más energéticas jamás registradas por el Observatorio Pierre Auger, '
                   'confrontadas con la huella que una cuadrícula cúbica debería dejarles.',
    'date': '28 de septiembre de 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Veredicto</h2>
<p><strong>No.</strong> Los [[n_evt]] rayos cósmicos más energéticos medidos por el Observatorio Pierre Auger no muestran ninguna simetría de cubo. Un cielo sin cuadrícula alguna produce un patrón al menos tan marcado como el observado en el [[p4_pct]]&nbsp;% de los casos: lo que vemos es azar corriente.</p>
<p>Este «no» tiene un alcance limitado: con [[n_evt]] partículas, solo un patrón muy marcado podía aparecer. Un patrón más sutil sigue siendo posible.</p>
</section>

<h2 id="explication">Explicación</h2>
<p>Si nuestro mundo lo calculara un ordenador, el espacio quizá estaría dividido en cubos diminutos, como una imagen está hecha de píxeles. En 2012, tres físicos señalaron que esa división dejaría una huella: las partículas más rápidas del Universo no llegarían igual desde todas las direcciones. Algunas direcciones serían favorecidas, dispuestas como las caras o las esquinas de un cubo.</p>
<p>Esas partículas existen: son los rayos cósmicos, núcleos de átomos llegados del espacio con una energía muy superior a todo lo que producen nuestros aceleradores. En Argentina, el Observatorio Pierre Auger los acecha con una inmensa red de detectores. Ha publicado la lista de sus [[n_evt]] capturas más energéticas, registradas entre 2004 y 2020, con la dirección de la que llegó cada una.</p>
<p>Tomamos esas [[n_evt]] direcciones y buscamos si se alinean a lo largo de un cubo. Como nadie sabe cómo estaría girado ese cubo, probamos [[n_orient]] posiciones. La mejor encaja un poco con los datos. Pero cuando se prueban tantas posiciones, siempre se encuentra una que encaja un poco, incluso en un cielo debido al puro azar.</p>
<p>Para decidir, fabricamos [[n_ciels]] cielos falsos sorteados al azar, vistos por el mismo observatorio, y repetimos exactamente la misma búsqueda en cada uno. En el [[p4_pct]]&nbsp;% de ellos aparece un cubo que encaja al menos igual de bien. El cielo real no tiene, por tanto, nada de especial. Para hablar de un indicio, habría tenido que superar a casi todos los cielos falsos.</p>
<p>Conclusión: ninguna huella de cuadrícula. Pero esta búsqueda solo podía ver un patrón fuerte: con solo [[n_evt]] partículas, uno discreto pasaría inadvertido. Además, los campos magnéticos de nuestra galaxia desvían estas partículas por el camino, lo que emborronaría parte del patrón. Esta prueba no demuestra, pues, que el espacio sea continuo; muestra que, allí donde podíamos mirar, no hay nada.</p>

<h2 id="analyse">Análisis detallado</h2>

<h3>1. De la cuadrícula a una predicción comprobable</h3>
<p>En una red cúbica de espaciado \(a\), el laplaciano discreto sustituye \(k^{2}\) por \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\). Para un campo libre,</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>donde \(\mathbf n\) es la dirección de propagación en los ejes de la red. Es la misma función \(Q\) que en la prueba n.º&nbsp;1. En general, cualquier efecto de la cuadrícula sobre las direcciones de llegada (propagación, corte del espectro dependiente de la dirección) es una función de \(\mathbf n\) invariante bajo el grupo del cubo \(O_h\). Ahora bien, los armónicos esféricos invariantes bajo \(O_h\) solo existen para \(\ell=0,4,6,8,\dots\): la primera anisotropía permitida es el armónico cúbico \(\ell=4\), proporcional a \(Q-3/5\). Es nuestra prueba principal, fijada antes de abrir los datos; \(\ell=6\) se prueba en segundo lugar. Beane, Davoudi y Savage escriben que la simulación «podría revelarse en las distribuciones de los rayos cósmicos de más alta energía, mediante un grado de ruptura de la simetría de rotación que refleje la estructura de la red subyacente».</p>

<h3>2. Los datos</h3>
<p>Catálogo del Observatorio Pierre Auger (ApJS 264, 50, 2023): las [[n_evt]] cascadas de mayor energía registradas del 1 de enero de 2004 al 31 de diciembre de 2020, de [[e_min]] a [[e_max]]&nbsp;EeV, con ángulos cenitales de hasta [[zmax]]°. El archivo abierto contiene además [[n_calib]] eventos híbridos de calibración, fuera de los [[n_evt]]: los descartamos. Usamos la ascensión recta y la declinación reconstruidas por el detector de superficie. La huella SHA-256 del archivo se comprueba en cada ejecución. A estas energías la eficiencia de detección es total hasta [[zmax]]°, de modo que la exposición es puramente geométrica.</p>

<h3>3. La exposición del detector</h3>
<p>Un detector en tierra, a la latitud \(a_0\)&nbsp;=&nbsp;[[lat]]°, que acepta cenits \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]°, tiene una exposición uniforme en ascensión recta y, en declinación \(\delta\) (Sommers, 2001):</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>El cielo visible termina en \(\delta\)&nbsp;=&nbsp;[[dec_max]]°, es decir, el [[ciel_pct]]&nbsp;% de la esfera. Un cielo isótropo visto por Auger no es, por tanto, uniforme: todo lo que sigue compara los datos con ese cielo, no con una esfera uniforme.</p>

<h3>4. El estadístico</h3>
<p>Sea \(R\) una orientación de la cuadrícula, de filas \(\mathbf e_k\), y \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). Para las \(N\) direcciones observadas:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>donde \(\langle\cdot\rangle_\omega\) es la media sobre un cielo isótropo ponderado por la exposición. \(T>0\) indica un exceso a lo largo de los ejes del cubo, \(T<0\) a lo largo de sus diagonales; el valor absoluto cubre ambos casos. Como \(f\) es un polinomio de grado 4, \(T(R)\) solo depende de los datos a través de los 15 momentos \(\sum_i\mathbf n_i^{\alpha}\); media y varianza se calculan exactamente por cuadratura de Gauss-Legendre. El máximo recorre [[n_orient]] orientaciones sorteadas uniformemente (medida de Haar). Para \(\ell=6\) tomamos \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\), con \(\alpha\)&nbsp;=&nbsp;[[alpha6]] (es decir \(-15/11\)), que la hace ortogonal a \(\ell=4\); la prueba combinada maximiza \(T_4^{2}+T_6^{2}\).</p>

<h3>5. Calibrar el azar</h3>
<p>Buscar la mejor orientación entre [[n_orient]] infla mecánicamente \(Z_4\): no sigue una ley normal. Sorteamos por ello [[n_ciels]] cielos isótropos de \(N\) eventos según la exposición y les aplicamos exactamente la misma maximización. Bajo la hipótesis «sin cuadrícula», \(Z_4\) tiene mediana [[z4_50]]; supera [[z4_95]] en el 5&nbsp;% de los casos, [[z4_99]] en el 1&nbsp;% y [[z4_999]] en el 0,1&nbsp;%. El valor p, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), incluye así el coste de elegir la orientación.</p>

<h3>6. Resultado</h3>
<div class="tableau"><table>
<thead><tr><th>Prueba</th><th>Estadístico observado</th><th>Valor p</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (principal)</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\) y \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>En la mejor orientación, la media de \(Q\) vale [[q_obs]] frente a [[q_iso]] esperado, un exceso del [[q_ecart_pct]]&nbsp;% hacia los ejes. No es significativo: \(p\)&nbsp;=&nbsp;[[p4]] para la prueba principal, y ninguna prueba secundaria baja de 0,05. Los datos son compatibles con la ausencia de toda simetría cúbica.</p>

<h3>7. Lo que la prueba podía ver</h3>
<p>Para cuantificar la sensibilidad, se inyecta un patrón cúbico: densidad proporcional a \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Con \(\varepsilon>0\), el flujo a lo largo de los ejes es \(1+\varepsilon\) veces la media; con \(\varepsilon<0\), el exceso se desplaza a las diagonales. Para cada \(\varepsilon\), [[n_ciels_signal]] cielos de orientación aleatoria dan la distribución de \(Z_4\). Límite superior al 95&nbsp;%: \(\varepsilon\le\)&nbsp;[[eps_axes]] hacia los ejes y \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]] hacia las diagonales. Dicho de otro modo, no se excluye un exceso de hasta aproximadamente el [[eps_axes_pct]]&nbsp;% a lo largo de los ejes (o el [[eps_diag_pct]]&nbsp;% a lo largo de las diagonales): una restricción débil, fijada por el reducido número de eventos.</p>
<p>El script comprueba primero su propia cadena: invariancia de \(Q\) bajo el grupo del cubo, desarrollo polinómico exacto, exposición nula más allá de [[dec_max]]°, \(T\) centrado y reducido bajo isotropía, ortogonalidad de \(\ell=6\) respecto a \(\ell=4\), y detección de un patrón inyectado nítido, cuya orientación se recupera con un error de [[ecart_orient]]°.</p>

<h3>8. Límites</h3>
<ul>
<li>Los rayos cósmicos tienen carga: los campos magnéticos galácticos y extragalácticos desvían sus direcciones, tanto más cuanto más pesados son los núcleos. El patrón buscado es amplio (un eje y una diagonal distan [[angle_diag]]°) y resiste desviaciones modestas, pero una huella fijada en la fuente o durante la propagación quedaría en parte borrada.</li>
<li>Suponemos la cuadrícula fija respecto a las estrellas lejanas (coordenadas ecuatoriales). Una cuadrícula en movimiento o en rotación respecto a ellas exigiría otra prueba.</li>
<li>[[n_evt]] eventos y el [[ciel_pct]]&nbsp;% del cielo: la potencia estadística es baja, como muestra el límite anterior.</li>
<li>Anisotropías astrofísicas reales pueden contener una componente \(\ell=4\). Un resultado positivo habría exigido excluirlas; un resultado nulo no depende de ellas.</li>
<li>No se calcula ninguna probabilidad de estar simulados: la prueba se refiere a una firma precisa, la de una cuadrícula cúbica.</li>
</ul>

<h3>9. Reproducir</h3>
<p>Un script de Python (numpy) lo rehace todo en un minuto aproximadamente: lectura y control de los datos, autopruebas, estadístico, cielos simulados, límite superior. El generador aleatorio tiene una semilla fija: los resultados son idénticos de una ejecución a otra.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-2/analyse.py" download>analyse.py</a>: el script</li>
<li><a href="/fichiers/test-2/resultats.json" download>resultats.json</a>: todos los valores calculados</li>
<li><a href="/fichiers/test-2/donnees/auger_catalogSD.csv" download>auger_catalogSD.csv</a>: los datos del Observatorio Pierre Auger (licencia CC BY-SA 4.0)</li>
</ul>

<h2 id="sources">Fuentes</h2>
<ol class="sources">
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Pierre Auger Collaboration, <cite>A Catalog of the Highest-Energy Cosmic Rays Recorded During Phase I of Operation of the Pierre Auger Observatory</cite>, ApJS 264, 50 (2023), <a href="https://arxiv.org/abs/2211.16020">arXiv:2211.16020</a>.</li>
<li>Pierre Auger Collaboration, <cite>Auger Open Data</cite>, release 3, <a href="https://doi.org/10.5281/zenodo.10488964">DOI 10.5281/zenodo.10488964</a>; eficiencia de detección: <a href="https://opendata.auger.org/data.php">opendata.auger.org</a>.</li>
<li>P. Sommers, <cite>Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory</cite>, Astroparticle Physics 14, 271 (2001), <a href="https://arxiv.org/abs/astro-ph/0004016">arXiv:astro-ph/0004016</a>.</li>
</ol>
""",
}

ARTICLE_3 = {
    'titre': '¿Viaja la luz más despacio en algunas direcciones?',
    'description': 'Ocho fuentes de rayos gamma repartidas por el cielo, combinadas para cerrar el punto ciego '
                   'de la prueba n.º 1 y acotar el espaciado de una cuadrícula cúbica sea cual sea su orientación.',
    'date': '28 de septiembre de 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Veredicto</h2>
<p><strong>No.</strong> Ninguna de las [[n_src]] fuentes estudiadas muestra el retraso que produciría una cuadrícula. Combinando sus direcciones, queda excluida una cuadrícula cúbica de espaciado igual o superior a [[a_exclue]]&nbsp;m, sea cual sea su orientación y sea cual sea su paso de tiempo: el punto ciego de la prueba n.º&nbsp;1 queda cerrado.</p>
</section>

<h2 id="explication">Explicación</h2>
<p>Si el Universo se calculara sobre una cuadrícula, como una imagen está hecha de píxeles, la luz no avanzaría exactamente a la misma velocidad en todas las direcciones. La luz más energética se retrasaría muy ligeramente, más a lo largo de las aristas de la cuadrícula que a lo largo de sus diagonales. Tras miles de millones de años de viaje, ese retraso se volvería medible.</p>
<p>La prueba n.º&nbsp;1 buscaba ese retraso en el estallido de rayos gamma más brillante jamás observado, y no vio nada. Pero quedaba un resquicio: si la simulación avanza en el tiempo con el mayor paso posible, la luz ya no se retrasa en absoluto a lo largo de las diagonales de la cuadrícula. Una única fuente situada sobre una diagonal no permitía entonces ninguna conclusión.</p>
<p>Aquí observamos [[n_src]] fuentes a la vez, en distintas direcciones del cielo: tres explosiones de estrellas lejanas, cuatro galaxias con un agujero negro muy activo y el púlsar de la nebulosa del Cangrejo. Para cada una, un equipo de astrónomos ya midió que no aparece ningún retraso, hasta cierta finura. Releímos cada artículo, llevamos todos los resultados a la misma convención y buscamos después la orientación que mejor permitiría a una cuadrícula pasar inadvertida, la que más debilita el límite.</p>
<p>Es imposible colocar todas las fuentes sobre diagonales al mismo tiempo. Incluso en la orientación más favorable, tres fuentes quedan lo bastante lejos de una diagonal como para que hubiera debido aparecer un retraso. Una cuadrícula cuyas casillas midan al menos [[a_exclue]]&nbsp;m queda, por tanto, excluida en todas las orientaciones. Ese tamaño sigue siendo unas [[planck_x]] veces mayor que la longitud de Planck: una cuadrícula mucho más fina sigue siendo totalmente posible.</p>

<h2 id="analyse">Análisis detallado</h2>

<h3>1. El modelo</h3>
<p>Como en la prueba n.º&nbsp;1: ecuaciones de Maxwell sobre una red cúbica de espaciado \(a\) (esquema de Yee), con paso de tiempo \(c\,\Delta t=\sigma a/\sqrt{3}\) y \(0\le\sigma\le1\). A orden dominante,</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\,Q_{\mathrm{eff}}\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3},\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>Como \(1/3\le Q\le1\), \(Q_{\mathrm{eff}}\ge0\): el fotón siempre se ralentiza, y \(Q_{\mathrm{eff}}=0\) exactamente sobre las diagonales del cubo cuando \(\sigma=1\). En la cota final, \(aE/\hbar c\)&nbsp;=&nbsp;[[ae]] para un fotón de 20&nbsp;TeV: el desarrollo es válido.</p>

<h3>2. De los límites publicados a una cota sobre el espaciado</h3>
<p>Los ocho artículos describen un retraso cuadrático mediante \(v/c\simeq1-\tfrac{3}{2}(E/E_{\mathrm{QG},2})^{2}\), con la distancia de Jacob y Piran \(K_2=\int_0^{z}(1+z')^{2}\,dz'/H(z')\). Por identificación,</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}}\quad\Longrightarrow\quad a\sqrt{Q_{\mathrm{eff}}(\mathbf n_i)}\le B_i=\frac{\sqrt{12}\,\hbar c}{E_i}.$$
<p>Regla fijada de antemano: límite al 95&nbsp;%, caso subluminal, tiempo de vuelo y el método menos restrictivo de cada artículo. Cada límite se lleva a la cosmología de LHAASO mediante \(E_i\sqrt{K_2^{\mathrm{LHAASO}}(z_i)/K_2^{(i)}(z_i)}\); el factor no supera [[fc_max]]. Cada conversión publicada se rehace a partir de los parámetros impresos y reproduce el valor del artículo (autopruebas).</p>
<div class="tableau"><table>
<thead><tr><th>Fuente</th><th>Instrumento</th><th>\(z\) o distancia</th><th>\(E_{\mathrm{QG},2}\) publicada (GeV)</th><th>Cosmología común (GeV)</th><th>\(B_i\) (m)</th></tr></thead>
<tbody>
<tr><td>GRB 221009A</td><td>LHAASO</td><td>[[s0_z]]</td><td>[[s0_pub]]</td><td>[[s0_com]]</td><td>[[s0_b]]</td></tr>
<tr><td>GRB 190114C</td><td>MAGIC</td><td>[[s1_z]]</td><td>[[s1_pub]]</td><td>[[s1_com]]</td><td>[[s1_b]]</td></tr>
<tr><td>GRB 090510</td><td>Fermi-LAT</td><td>[[s2_z]]</td><td>[[s2_pub]]</td><td>[[s2_com]]</td><td>[[s2_b]]</td></tr>
<tr><td>Mrk 501</td><td>H.E.S.S.</td><td>[[s3_z]]</td><td>[[s3_pub]]</td><td>[[s3_com]]</td><td>[[s3_b]]</td></tr>
<tr><td>Mrk 421</td><td>MAGIC</td><td>[[s4_z]]</td><td>[[s4_pub]]</td><td>[[s4_com]]</td><td>[[s4_b]]</td></tr>
<tr><td>PKS 2155-304</td><td>H.E.S.S.</td><td>[[s5_z]]</td><td>[[s5_pub]]</td><td>[[s5_com]]</td><td>[[s5_b]]</td></tr>
<tr><td>PG 1553+113</td><td>H.E.S.S.</td><td>[[s6_z]]</td><td>[[s6_pub]]</td><td>[[s6_com]]</td><td>[[s6_b]]</td></tr>
<tr><td>Cangrejo (púlsar)</td><td>MAGIC</td><td>[[s7_z]]&nbsp;kpc</td><td>[[s7_pub]]</td><td>[[s7_com]]</td><td>[[s7_b]]</td></tr>
</tbody>
</table></div>

<h3>3. La orientación más desfavorable</h3>
<p>Para una orientación \(R\) de la red, las fuentes imponen conjuntamente</p>
$$a\le A(R)=\min_i\frac{B_i}{\sqrt{Q_{\mathrm{eff}}(R\mathbf n_i)}},$$
<p>ya que una fuente situada sobre una diagonal con \(\sigma=1\) no acota nada. Buscamos \(\max_R A(R)\): [[n_orient]] rotaciones sorteadas uniformemente, orientaciones construidas (cada fuente colocada sobre una diagonal y girada después en torno a ella) y, por último, un refinamiento local. Una segunda semilla independiente reproduce el mismo máximo con una diferencia de [[ecart_graines]]. El optimizador se valida con casos conocidos: una sola fuente no acota nada con \(\sigma=1\), y dos fuentes separadas por el ángulo entre dos diagonales pueden colocarse a la vez sobre diagonales.</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>Orientación más desfavorable (m)</th><th>95&nbsp;% de las orientaciones (m)</th></tr></thead>
<tbody>
<tr><td>0</td><td>[[pire0]]</td><td>[[q95_0]]</td></tr>
<tr><td>0,5</td><td>[[pire05]]</td><td>[[q95_05]]</td></tr>
<tr><td>0,9</td><td>[[pire09]]</td><td>[[q95_09]]</td></tr>
<tr><td>1</td><td>[[pire1]]</td><td>[[q95_1]]</td></tr>
</tbody>
</table></div>
<p>Para \(\sigma<1\), nada cambia respecto a la prueba n.º&nbsp;1: domina GRB&nbsp;221009A, y las demás fuentes son entre [[x_min]] y [[x_max]] veces menos sensibles. Todo se decide en \(\sigma=1\): colocar GRB&nbsp;221009A sobre una diagonal ya no basta, porque entonces las demás fuentes ven la red en oblicuo. El peor compromiso aparta GRB&nbsp;221009A [[ang_grb]]° de la diagonal más cercana (\(Q_{\mathrm{eff}}\)&nbsp;=&nbsp;[[qeff_grb]]) y equilibra [[n_actives]] restricciones: GRB&nbsp;221009A, GRB&nbsp;090510 y el Cangrejo. La cota vale entonces [[pire1]]&nbsp;m, es decir, una escala \(\hbar c/a\ge\)&nbsp;[[echelle]]&nbsp;GeV. Como \(A(R)\) crece con \(\sigma\) para cualquier orientación, la cota vale para todo \(\sigma\le1\). Con \(\sigma=1\), la orientación mediana da [[med1]]&nbsp;m.</p>
<p>El cierre no estaba garantizado: GRB&nbsp;190114C y GRB&nbsp;090510 distan [[ang_190_090]]°, casi el ángulo entre dos diagonales ([[ang_diag]]°), y GRB&nbsp;090510 y PKS&nbsp;2155-304 están a solo [[ang_090_pks]]° uno de otro. Es la diversidad del resto del cielo la que cierra el punto ciego.</p>

<h3>4. Robustez</h3>
<p>Orientación más desfavorable con \(\sigma=1\), según las elecciones:</p>
<ul>
<li>sin GRB&nbsp;221009A: [[v_sans_lhaaso]]&nbsp;m; el punto ciego sigue cerrado;</li>
<li>límites publicados sin conversión de cosmología: [[v_sans_cosmo]]&nbsp;m;</li>
<li>Fermi con efectos propios de la fuente (tabla V del artículo): [[v_fermi]]&nbsp;m;</li>
<li>solo estallidos de rayos gamma: [[v_sursauts]]&nbsp;m;</li>
<li>solo blazares y púlsar: [[v_blazars]]&nbsp;m.</li>
</ul>

<h3>5. Comparaciones</h3>
<p>La cota válida para cualquier orientación y cualquier paso de tiempo es [[x_test1]] veces menos restrictiva que la de la prueba n.º&nbsp;1 en tiempo continuo. Beane, Davoudi y Savage obtenían \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m a partir del corte del espectro de los rayos cósmicos; nuestra cota en tiempo continuo vale [[x_beane0]] veces la suya, y nuestra cota universal, [[x_beane]] veces.</p>

<h3>6. Límites</h3>
<ul>
<li>La cota combinada toma, para cada orientación, el más restrictivo de los límites publicados al 95&nbsp;% uno a uno: no es una verosimilitud combinada, que los artículos no publican. Como hay tres límites activos en la orientación más desfavorable, la cobertura garantizada es de al menos el [[couverture]]&nbsp;%, no del 95&nbsp;%.</li>
<li>Cada artículo supone que ningún desfase propio de la fuente compensa o imita el retraso.</li>
<li>Los corrimientos al rojo de Mrk&nbsp;421 y de PG&nbsp;1553+113 son inciertos; ninguna de estas dos fuentes está activa en la orientación más desfavorable. La distancia del púlsar del Cangrejo, fuente activa, está incluida en las incertidumbres de MAGIC.</li>
<li>Un esquema de orden superior (error en \(a^{4}\)), unos términos compensadores o una red no cúbica o estirada por la expansión escapan a esta cota.</li>
<li>Análisis secundario: no se reanaliza ningún fotón. Las fracciones de orientaciones son geométricas, no probabilidades sobre el Universo.</li>
</ul>

<h3>7. Reproducir</h3>
<p>El script lo rehace todo en unos segundos y comprueba primero sus fórmulas y cada conversión publicada. Cada dato de entrada se cita, con página y tabla, en <code>sources.md</code>.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-3/analyse.py" download>analyse.py</a>: el script</li>
<li><a href="/fichiers/test-3/resultats.json" download>resultats.json</a>: todos los valores calculados</li>
<li><a href="/fichiers/test-3/sources.md" download>sources.md</a>: la cita de cada dato de entrada</li>
</ul>

<h2 id="sources">Fuentes</h2>
<ol class="sources">
<li>LHAASO Collaboration, GRB 221009A, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>, tabla I.</li>
<li>MAGIC Collaboration, GRB 190114C, <a href="https://arxiv.org/abs/2001.09728v4">arXiv:2001.09728v4</a>, tabla I.</li>
<li>Fermi-LAT Collaboration, GRB 090510, <a href="https://arxiv.org/abs/1305.3463v1">arXiv:1305.3463v1</a>, tablas IV y V.</li>
<li>H.E.S.S. Collaboration, Mrk 501, <a href="https://arxiv.org/abs/1901.05209v1">arXiv:1901.05209v1</a>.</li>
<li>MAGIC Collaboration, Mrk 421, <a href="https://arxiv.org/abs/2406.07140v1">arXiv:2406.07140v1</a>, tabla 2.</li>
<li>H.E.S.S. Collaboration, PKS 2155-304, <a href="https://arxiv.org/abs/1101.3650v2">arXiv:1101.3650v2</a>.</li>
<li>H.E.S.S. Collaboration, PG 1553+113, <a href="https://arxiv.org/abs/1501.05087v1">arXiv:1501.05087v1</a>, tabla 5.</li>
<li>MAGIC Collaboration, púlsar del Cangrejo, <a href="https://arxiv.org/abs/1709.00346v1">arXiv:1709.00346v1</a>, tabla 6.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>.</li>
<li>Coordenadas: <a href="https://simbad.cds.unistra.fr/simbad/">SIMBAD</a> (CDS, Estrasburgo).</li>
</ol>
""",
}
