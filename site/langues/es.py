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
