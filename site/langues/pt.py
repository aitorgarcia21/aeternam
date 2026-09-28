"""Portugais (Brésil) : traduction de la source française (fr.py).

Mêmes marqueurs [[…]], mêmes formules et même structure HTML que la source.
Vérifier avec : python3 site/generer.py --verifier pt
"""
NOM = 'Português'
HTML_LANG = 'pt-BR'
HREFLANG = 'pt'
DIR = 'ltr'
LOCALE_OG = 'pt_BR'
DECIMALE = ','

UI = {
    'devise': 'Pesquisa sobre a teoria da simulação.',
    'description_site': 'aeternam — pesquisa sobre a teoria da simulação',
    'travaux': 'Trabalhos',
    'langue': 'Idioma',
    'surtitre': 'Pesquisa · Teste nº 1',
    'meta': 'versão 2 · análise secundária reprodutível',
    'fichier_pdf': 'aeternam-test-1-pt.pdf',
}

ARTICLE = {
    'titre': 'Uma rede cúbica diante do GRB 221009A',
    'description': 'O que os fótons observados pelo LHAASO impõem ao espaçamento da rede de um espaço discreto, '
                   'e até onde vai essa restrição.',
    'date': '28 de setembro de 2026',
    'corps': r"""
<section class="resume">
<h2>Em resumo</h2>
<ul>
<li><strong>Se o espaço fosse uma rede cúbica</strong> na qual a luz se propagasse como em uma simulação numérica das equações de Maxwell, os fótons mais energéticos chegariam atrasados. No surto GRB&nbsp;221009A, o LHAASO não observa nenhum atraso desse tipo.</li>
<li><strong>O espaçamento da rede é, portanto, inferior a [[a_resume]]&nbsp;m</strong> com o método mais conservador e a orientação mais desfavorável, ou a [[a_ml_resume]]&nbsp;m com o método de verossimilhança. A escala de energia da rede ultrapassa [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>Não é uma fronteira nova.</strong> Beane, Davoudi e Savage já obtiveram a mesma ordem de grandeza em 2012 (cerca de [[b_beane]]&nbsp;m) a partir dos raios cósmicos. Este resultado o confirma de forma independente, por meio de outro observável.</li>
<li><strong>Novidade: o passo de tempo importa.</strong> Se o tempo também for discretizado, como em toda simulação numérica, o efeito diminui. No passo máximo estável, a luz já não sofre nenhuma dispersão ao longo das oito direções diagonais do cubo: um único surto não permite, então, nenhum limite universal. Para 95% das orientações, o espaçamento continua inferior a [[a95_sigma1]]&nbsp;m.</li>
<li><strong>Uma rede cujo erro dominante seja linear</strong> em <em>a</em> está excluída até [[a_lineaire]]&nbsp;m, um décimo do comprimento de Planck.</li>
<li><strong>Um espaçamento do tamanho de Planck continua fora de alcance</strong>: seu efeito seria fraco demais para este teste, por um fator de cerca de [[facteur_planck]].</li>
<li><strong>Ao verificar a literatura</strong>, identificamos uma incoerência de conversão em um artigo de 2025 (Xi e Shu): o limite quadrático deles parece superestimado por um fator de [[xs_facteur]].</li>
<li><strong>Nenhuma detecção, nenhuma probabilidade de sermos simulados.</strong> O teste restringe uma arquitetura específica; não diz nada sobre a existência de um simulador.</li>
</ul>
</section>

<h2 id="question">1. A questão testada</h2>
<p>Uma simulação numérica representa o espaço por um número finito de pontos. Uma onda que se propaga nele não se comporta exatamente como no contínuo: sua velocidade depende ligeiramente de seu comprimento de onda. No caso da luz, a velocidade dependeria, assim, da energia dos fótons. O efeito é minúsculo, mas se acumula ao longo de distâncias cosmológicas.</p>
<p>O GRB&nbsp;221009A é o surto de raios gama mais brilhante já registrado. O observatório LHAASO detectou fótons desse surto acima de 10&nbsp;TeV, emitidos há cerca de dois bilhões de anos (desvio para o vermelho <em>z</em>&nbsp;=&nbsp;[[z]]). Se a velocidade da luz dependesse da energia, os fótons de alta energia chegariam depois dos de baixa energia. A colaboração LHAASO procurou esse atraso e não o encontrou.</p>
<p>A questão é, portanto, precisa: <em>que espaçamento da rede ainda é compatível com esse atraso nulo?</em> Ela não pressupõe que toda simulação use uma rede, nem que uma rede seja prova de uma simulação.</p>

<h2 id="modele">2. O modelo: Maxwell em uma rede</h2>
<p>Colocamos os campos eletromagnéticos em uma rede cúbica de espaçamento <em>a</em>, exatamente como no esquema de Yee (1966), usado pelas simulações numéricas das equações de Maxwell, ou como na formulação hamiltoniana da eletrodinâmica na rede (Kogut e Susskind, 1975). O tempo flui de forma contínua ou em passos \(\Delta t\). Uma onda plana de vetor de onda \(\mathbf k\) e frequência angular \(\omega\) satisfaz então a relação de dispersão:</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>O esquema só é estável se \(c\,\Delta t\le a/\sqrt{3}\). Escrevemos então \(c\,\Delta t=\sigma a/\sqrt{3}\), com um número de Courant \(0\le\sigma\le1\); \(\sigma=0\) corresponde ao tempo contínuo. Para fótons cujo comprimento de onda é muito maior que o espaçamento, a velocidade de grupo passa a ser, com \(E=\hbar\omega\):</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) depende da direção \(\mathbf n\) do fóton em relação aos eixos da rede: \(Q=1\) ao longo de um eixo e \(Q=1/3\) ao longo de uma diagonal do cubo. Três propriedades serão importantes a seguir:</p>
<ul>
<li>o efeito é <strong>quadrático</strong>: um espaçamento dez vezes menor produz um efeito cem vezes mais fraco;</li>
<li>os fótons são <strong>desacelerados</strong>, nunca acelerados, enquanto o esquema for estável;</li>
<li>as duas polarizações se propagam da mesma maneira: <strong>não há birrefringência</strong>, de modo que as restrições baseadas na polarização, muito rigorosas, não se aplicam aqui.</li>
</ul>

<h2 id="lhaaso">3. O confronto com o LHAASO</h2>
<p>O LHAASO descreve um atraso quadrático por meio de \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) e publica intervalos para \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\), com \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV (equações 2, 3 e 5 do artigo). Por identificação:</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>O atraso acumulado entre dois fótons de energias \(E_h\) e \(E_l\) é dado por</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>com a cosmologia do LHAASO (<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc, Ω<sub>m</sub>&nbsp;=&nbsp;[[om]], Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]), que dá <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s. A medição só restringe a combinação \(a\sqrt{Q_{\mathrm{eff}}}\). A tabela I do LHAASO fornece, a 95%:</p>
<div class="tableau"><table>
<thead><tr><th>Método</th><th>Limite inferior</th><th>Melhor ajuste</th><th>Limite superior</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML (calibrada)</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>Os três intervalos contêm o zero: nenhum atraso é detectado. Os três métodos analisam o mesmo surto; não os combinamos. Um limite superior \(U\) para \(\eta_2\) implica</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>Em tempo contínuo, obtemos:</p>
<div class="tableau"><table>
<thead><tr><th>Método</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\), orientação mais desfavorável (m)</th><th>\(a\), 95% das orientações (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML (calibrada)</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>O resumo adota o valor mais conservador, [[a_resume]]&nbsp;m: trata-se de uma envoltória de apresentação, não de um novo intervalo. Com esse valor-limite, um fóton de 1&nbsp;TeV chegaria no máximo [[retard_limite]]&nbsp;s depois de um fóton de [[e_bas]]&nbsp;TeV.</p>
<p>Algumas previsões, que não são medições (fóton de 1&nbsp;TeV comparado a um fóton de [[e_bas]]&nbsp;TeV):</p>
<div class="tableau"><table>
<thead><tr><th>Espaçamento</th><th>\(\eta_2\) previsto</th><th>Atraso previsto</th><th>Veredito</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]] a [[p26_eta_max]]</td><td>[[p26_ret_min]] a [[p26_ret_max]]&nbsp;s</td><td>excluído para qualquer orientação</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]] a [[p27_eta_max]]</td><td>[[p27_ret_min]] a [[p27_ret_max]]&nbsp;s</td><td>excluído perto dos eixos (\(Q>\)&nbsp;[[q_cal_axe]]) apenas pelo método calibrado</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]] a [[p28_eta_max]]</td><td>[[p28_ret_min]] a [[p28_ret_max]]&nbsp;ms</td><td>não excluído</td></tr>
<tr><td>[[lpl]]&nbsp;m (Planck)</td><td>[[pl_eta_min]] a [[pl_eta_max]]</td><td>[[pl_ret_min]] a [[pl_ret_max]]&nbsp;s</td><td>fora de alcance</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. Até onde o limite resiste</h2>
<h3>A orientação da rede</h3>
<p>Não se sabe como a rede estaria orientada em relação à direção do surto. O limite principal adota o caso menos favorável, \(Q=1/3\). Em um milhão de direções distribuídas uniformemente, a mediana de \(Q\) é [[q_mediane]], e em 95% dos casos o valor supera [[q_5]]: o limite muda pouco, com [[ccf_95]]&nbsp;m para 95% das orientações e [[ccf_mediane]]&nbsp;m para a orientação mediana. Essas frações são geométricas: não são probabilidades sobre o Universo.</p>
<h3>O tempo discreto, ponto fraco do limite</h3>
<p>Uma simulação avança em passos de tempo. Discretizar o tempo produz um erro de sinal oposto, que compensa em parte o do espaço (o termo \(-\sigma^{2}/3\)). Para o método conservador:</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>Orientação mais desfavorável</th><th>95% das orientações</th><th>Orientação mediana</th></tr></thead>
<tbody>
<tr><td>0 (tempo contínuo)</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1 (passo máximo)</td><td>[[s4_cdt]]</td><td>sem limite</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>No passo máximo estável, a compensação é exata ao longo das diagonais do cubo, e não apenas em primeira ordem: nelas, a relação de dispersão volta a dar \(\omega=ck\) para qualquer comprimento de onda. Uma simulação ajustada dessa forma escaparia inteiramente a este teste se a direção do surto coincidisse com uma de suas oito direções diagonais. Essa é a principal limitação quando o limite vem de uma única fonte; várias fontes em direções diferentes a eliminariam, pois, salvo coincidência, elas não podem estar todas alinhadas com diagonais.</p>
<h3>Um espaçamento fixo ou esticado pela expansão</h3>
<p>Supomos um espaçamento físico fixo. Se a rede se esticasse com o Universo (espaçamento comóvel), o efeito já não cresceria com o desvio para o vermelho, e \(I_2\) seria substituído por \(I_0\): o limite se enfraquece por um fator \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]], ou seja, [[comobile_a]]&nbsp;m. Em <em>z</em>&nbsp;=&nbsp;[[z]], essa escolha pesa pouco.</p>
<h3>Esquemas mais precisos</h3>
<p>Um simulador pode empregar um esquema de ordem superior, cujo erro dominante varia como \(a^{4}\). O efeito passa então a ser quártico na energia, e o limite para \(a\), muito mais fraco. O LHAASO não publica restrição desse tipo para este surto; quantificá-la exigiria os dados fóton a fóton. Termos concebidos para compensar a dispersão também escapariam ao limite. São outros modelos, a serem testados separadamente.</p>
<h3>E se o erro fosse linear?</h3>
<p>Uma rede simétrica não produz nenhum efeito linear em \(a\). Uma discretização que o produzisse, ao quebrar a simetria entre os dois sentidos de propagação, estaria sujeita ao limite linear do LHAASO, \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\): com um coeficiente de ordem um, \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m, ou seja, um décimo do comprimento de Planck. Qualquer rede desse tipo com espaçamento maior está excluída.</p>
<h3>A validade do cálculo</h3>
<p>A expansão pressupõe \(aE/\hbar c\ll1\). No valor do limite, mesmo para fótons de 20&nbsp;TeV, \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]. Também comparamos a expansão com a relação de dispersão exata: para \(ak\)&nbsp;=&nbsp;[[ak_test]], o desvio relativo não passa de [[ecart_dispersion]], como esperado.</p>

<h2 id="contexte">5. O que isso vale, comparado ao que já existe</h2>
<p>Beane, Davoudi e Savage (2012) estudaram uma simulação da cromodinâmica quântica na rede. A partir do corte do espectro dos raios cósmicos, obtiveram para o inverso do espaçamento o limite \(1/b\gtrsim10^{11}\)&nbsp;GeV, ou seja, \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m. Nosso limite conservador vale [[beane_ratio]] vezes o deles; os métodos de verossimilhança do LHAASO dão entre [[beane_ml_min]] e [[beane_ml_max]] vezes o deles. As duas abordagens concordam, portanto, na ordem de grandeza, com observáveis, partículas e hipóteses diferentes: é uma confirmação, não um recorde.</p>
<p>O comprimento de Planck, [[lpl]]&nbsp;m, fica oito ordens de grandeza abaixo. Para um espaçamento desse tamanho, o efeito seria [[facteur_planck_exact]] vezes mais fraco do que o limite. Como ele cresce com o quadrado da energia, seriam necessários fótons cerca de cem milhões de vezes mais energéticos, muito além de tudo o que se observa: nessa ordem, nenhum teste de tempo de voo pode alcançar uma rede de Planck.</p>

<h2 id="xi-shu">6. Uma verificação da literatura: Xi e Shu (2025)</h2>
<p>Xi e Shu analisaram o mesmo surto com outro método e anunciam \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV (tabela III do artigo), cerca de [[xs_rapport_lhaaso]] vezes o limite do LHAASO. Refazendo o cálculo com as próprias definições dos autores, não obtemos esse valor.</p>
<ul>
<li>A equação (3) dos autores expressa o atraso em função de \((E/E_{\mathrm{QG},n})^{n}\). Para \(n=1\), sua conversão (6), \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\) com \(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]], é coerente: encontramos [[xs_c1]].</li>
<li>Para \(n=2\), sua equação (7), \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\) com \(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]], mantém a forma em \(1/\theta\). Aplicada ao limite obtido por eles, \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV², ela de fato reproduz a tabela deles ([[xs_eq7]]&nbsp;GeV). Mas, como o atraso é quadrático, sua equação (3) impõe uma dependência em \(1/\sqrt{\theta_2}\): \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\), ou seja, \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV.</li>
<li>A discrepância é de um fator [[xs_facteur]]. Explicação plausível: \(\varepsilon^{2}\theta_2\) vale [[xs_eps2]], e [[xs_c2_imprime]] se parece com a raiz quadrada de [[xs_eps2_imprime]] tomada apenas sobre a potência de dez.</li>
</ul>
<p>Situação: incoerência aparente na versão 1 do artigo, a ser confirmada com os autores. Não reanalisamos seus dados nem julgamos seus outros resultados. Uma vez corrigido, o limite deles continuaria [[xs_vs_lhaaso]] vezes mais forte que o do LHAASO. Não o utilizamos.</p>

<h2 id="limites">7. O que este teste não diz</h2>
<ul>
<li>Não detecta nada: um atraso nulo continua compatível com todas as medições.</li>
<li>Não calcula nenhuma probabilidade de estarmos em uma simulação; o “95%” se refere a um parâmetro físico.</li>
<li>Restringe uma arquitetura específica: rede cúbica, esquema de Yee, espaçamento fixo, sem compensação.</li>
<li>Mesmo um atraso detectado não apontaria para um computador: uma física fundamentalmente discreta, ou outros efeitos de gravidade quântica, produziriam o mesmo sinal.</li>
<li>Os intervalos do LHAASO se baseiam em hipóteses sobre a emissão da fonte; nós as herdamos.</li>
</ul>

<h2 id="suite">8. Próximos passos</h2>
<ol>
<li>Combinar várias fontes observadas em direções diferentes, para fechar o ponto cego das diagonais.</li>
<li>Quantificar os esquemas de ordem superior (efeito em \(a^{4}\)), o que exige os dados fóton a fóton.</li>
<li>Pedir a Xi e Shu que esclareçam sua conversão.</li>
<li>Estender o teste a outras assinaturas de uma rede: anisotropia dos raios cósmicos, partículas carregadas.</li>
</ol>

<h2 id="reproduire">9. Reproduzir</h2>
<p>Tudo é recalculado por um script em Python sem dependências, que primeiro verifica suas próprias fórmulas: expansão versus dispersão exata, diagonal exata, conversões de ida e volta, integral cosmológica, média de \(Q\) igual a 3/5.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>: o script (Python&nbsp;3.10 ou mais recente, biblioteca padrão), com comentários em francês</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>: todos os valores calculados</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>: esta nota em PDF</li>
</ul>
<p>Uma verificação cruzada independente (numpy, scipy) reproduz a integral cosmológica com precisão de 10<sup>−15</sup>, os quantis de orientação com dez milhões de amostras aleatórias e a velocidade de grupo pela resolução numérica da relação de dispersão.</p>
<p>Esta nota substitui uma primeira versão, de 28 de setembro de 2026. Ela acrescenta o tempo discreto, a orientação, o espaçamento comóvel, o efeito linear e a comparação com Beane et al.</p>

<h2 id="sources">Fontes</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a> (revisão de 13 de fevereiro de 2026): equações 2, 3 e 5, tabela I.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a> (2025): equações 3, 6 e 7, tabelas I e III.</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302 (1966).</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395 (1975).</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House: dispersão numérica e estabilidade do esquema de Yee.</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>: constantes fundamentais.</li>
</ol>
""",
}
