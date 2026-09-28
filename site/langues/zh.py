"""简体中文：法语源文件（fr.py）的译文。

每个 [[标记]] 都会被替换为 resultats.json 中的数值，并按本语言的习惯书写。
公式 $$…$$ 和 \\(…\\) 在所有语言中完全相同。由于含有反斜杠，必须使用原始字符串（r\"\"\"…\"\"\"）。
"""
NOM = '简体中文'
HTML_LANG = 'zh-Hans'
HREFLANG = 'zh-Hans'
DIR = 'ltr'
LOCALE_OG = 'zh_CN'
DECIMALE = '.'

UI = {
    'devise': '模拟理论研究。',
    'description_site': 'aeternam — 模拟理论研究',
    'travaux': '研究成果',
    'langue': '语言',
    'surtitre': '研究 · 检验一',
    'meta': '第2版 · 可复现的二次分析',
    'verdict': '迄今为止的结论：在所检查的数据中，没有发现任何模拟的痕迹。',
    'fichier_pdf': 'aeternam-test-1-zh.pdf',
}

ARTICLE = {
    'titre': '用 GRB 221009A 检验立方网格',
    'description': 'LHAASO 观测到的光子对离散空间的格点间距施加了什么约束，'
                   '这一约束又止步于何处。',
    'date': '2026年9月28日',
    'corps': r"""
<section class="resume">
<h2>要点</h2>
<ul>
<li><strong>如果空间是一个立方网格</strong>，而光在其中的传播方式与麦克斯韦方程组的数值模拟相同，那么能量最高的光子将会延迟到达。在伽马射线暴 GRB&nbsp;221009A 中，LHAASO 并未观测到此类延迟。</li>
<li><strong>因此，格点间距小于 [[a_resume]]&nbsp;m</strong>（采用最保守的方法并取最不利取向）；若采用似然方法，则小于 [[a_ml_resume]]&nbsp;m。网格的能标超过 [[echelle_resume]]&nbsp;GeV。</li>
<li><strong>这并不是新的界限。</strong>早在2012年，Beane、Davoudi 和 Savage 就已根据宇宙线得到了相同的量级（约 [[b_beane]]&nbsp;m）。本结果通过另一种可观测量，对此作出了独立的确认。</li>
<li><strong>新结果：时间步长不可忽略。</strong>如果时间也像任何数值模拟中那样被离散化，效应就会减弱。在最大稳定步长下，光沿立方体的八个对角线方向传播时完全不发生色散：此时仅凭单个伽马射线暴，无法给出普适的约束。对于95%的取向，格点间距仍小于 [[a95_sigma1]]&nbsp;m。</li>
<li><strong>主导误差与 <em>a</em> 成线性关系的网格</strong>，只要格点间距大于 [[a_lineaire]]&nbsp;m（普朗克长度的十分之一），即被排除。</li>
<li><strong>普朗克尺度的格点间距仍无法触及</strong>：其效应比本检验所能探测的弱约 [[facteur_planck]] 倍。</li>
<li><strong>在核查文献时</strong>，我们发现一篇2025年的论文（Xi 和 Shu）存在换算上的不一致：他们对二次效应的约束似乎被高估了 [[xs_facteur]] 倍。</li>
<li><strong>未探测到任何信号，也不给出我们身处模拟之中的概率。</strong>本检验约束的是一种特定的架构；至于模拟者是否存在，它没有给出任何信息。</li>
</ul>
</section>

<h2 id="question">1. 所检验的问题</h2>
<p>数值模拟用有限个点来表示空间。在其中传播的波，其行为与在连续空间中并不完全相同：波速会随波长略有变化。因此，对光而言，速度将取决于光子的能量。这一效应极其微小，但会在宇宙学距离上不断累积。</p>
<p>GRB&nbsp;221009A 是有记录以来最亮的伽马射线暴。LHAASO 观测站探测到了它发出的 10&nbsp;TeV 以上的光子，这些光子约在20亿年前出发（红移 <em>z</em>&nbsp;=&nbsp;[[z]]）。如果光速依赖于能量，高能光子就会比低能光子晚到。LHAASO 合作组寻找过这种延迟，但没有发现。</p>
<p>因此，问题是明确的：<em>在延迟为零的观测结果下，格点间距最大还能是多少？</em>这一问题既不假定所有模拟都会使用网格，也不假定网格就能证明模拟的存在。</p>

<h2 id="modele">2. 模型：网格上的麦克斯韦方程组</h2>
<p>我们把电磁场放在格点间距为 <em>a</em> 的立方格点上，做法与麦克斯韦方程组数值模拟所用的 Yee 格式（1966）完全相同，也与格点电动力学的哈密顿表述（Kogut 和 Susskind，1975）相同。时间或者连续流逝，或者以步长 \(\Delta t\) 推进。于是，波矢为 \(\mathbf k\)、角频率为 \(\omega\) 的平面波满足如下色散关系：</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>该格式仅在 \(c\,\Delta t\le a/\sqrt{3}\) 时稳定。因此记 \(c\,\Delta t=\sigma a/\sqrt{3}\)，其中 \(0\le\sigma\le1\) 为库朗数；\(\sigma=0\) 对应连续时间。对于波长远大于格点间距的光子，取 \(E=\hbar\omega\)，群速度变为：</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) 取决于光子方向 \(\mathbf n\) 相对于网格坐标轴的取向：沿坐标轴时 \(Q=1\)，沿体对角线时 \(Q=1/3\)。以下三个性质对后文很重要：</p>
<ul>
<li>效应是<strong>二次的</strong>：格点间距缩小为十分之一，效应就减弱为百分之一；</li>
<li>只要格式稳定，光子就只会被<strong>减速</strong>，绝不会被加速；</li>
<li>两种偏振的传播方式相同：<strong>没有双折射</strong>，因此非常严格的偏振约束在这里并不适用。</li>
</ul>

<h2 id="lhaaso">3. 与 LHAASO 观测的对照</h2>
<p>LHAASO 用 \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) 描述二次延迟，并给出了 \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\) 的区间，其中 \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV（见该论文的式2、3和5）。两相对照，可得：</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>能量分别为 \(E_h\) 和 \(E_l\) 的两个光子之间累积的延迟可写为</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>采用 LHAASO 的宇宙学参数（<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc，Ω<sub>m</sub>&nbsp;=&nbsp;[[om]]，Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]），可得 <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s。测量只能约束组合量 \(a\sqrt{Q_{\mathrm{eff}}}\)。LHAASO 论文的表 I 给出了95%置信水平下的结果：</p>
<div class="tableau"><table>
<thead><tr><th>方法</th><th>下限</th><th>最佳拟合</th><th>上限</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML（校准后）</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>三个区间都包含零：没有探测到延迟。三种方法分析的是同一个伽马射线暴；我们不将它们合并。由 \(\eta_2\) 的上限 \(U\) 可得</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>在连续时间情形下，得到：</p>
<div class="tableau"><table>
<thead><tr><th>方法</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\)，最不利取向 (m)</th><th>\(a\)，95%的取向 (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML（校准后）</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>要点中采用的是最保守的值 [[a_resume]]&nbsp;m：这是为便于呈现而取的包络，而不是一个新的区间。在这一极限下，1&nbsp;TeV 光子最多比 [[e_bas]]&nbsp;TeV 光子晚到 [[retard_limite]]&nbsp;s。</p>
<p>以下是几个预测值，它们并非测量结果（比较 1&nbsp;TeV 光子与 [[e_bas]]&nbsp;TeV 光子）：</p>
<div class="tableau"><table>
<thead><tr><th>格点间距</th><th>预测的 \(\eta_2\)</th><th>预测的延迟</th><th>结论</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]]～[[p26_eta_max]]</td><td>[[p26_ret_min]]～[[p26_ret_max]]&nbsp;s</td><td>在所有取向下均被排除</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]]～[[p27_eta_max]]</td><td>[[p27_ret_min]]～[[p27_ret_max]]&nbsp;s</td><td>仅校准后的 ML 方法可在坐标轴附近（\(Q>\)&nbsp;[[q_cal_axe]]）将其排除</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]]～[[p28_eta_max]]</td><td>[[p28_ret_min]]～[[p28_ret_max]]&nbsp;ms</td><td>未被排除</td></tr>
<tr><td>[[lpl]]&nbsp;m（普朗克长度）</td><td>[[pl_eta_min]]～[[pl_eta_max]]</td><td>[[pl_ret_min]]～[[pl_ret_max]]&nbsp;s</td><td>无法触及</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. 这一约束有多稳健</h2>
<h3>网格的取向</h3>
<p>我们不知道网格相对于该伽马射线暴的方向会如何取向。主要约束采用最不利的情形，即 \(Q=1/3\)。在均匀分布的一百万个方向上，\(Q\) 的中位数为 [[q_mediane]]，且在95%的情况下大于 [[q_5]]：约束变化不大，对95%的取向为 [[ccf_95]]&nbsp;m，对中位取向为 [[ccf_mediane]]&nbsp;m。这些比例是几何上的比例，而不是关于宇宙的概率。</p>
<h3>离散时间：约束的薄弱环节</h3>
<p>模拟是按时间步长推进的。对时间进行离散化会产生符号相反的误差，从而部分抵消空间离散化带来的误差（即 \(-\sigma^{2}/3\) 项）。对于保守方法，结果如下：</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>最不利取向</th><th>95%的取向</th><th>中位取向</th></tr></thead>
<tbody>
<tr><td>0（连续时间）</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1（最大步长）</td><td>[[s4_cdt]]</td><td>无约束</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>在最大稳定步长下，沿体对角线的抵消是精确的，而且不只在一阶近似下成立：在这些方向上，色散关系对任意波长都重新给出 \(\omega=ck\)。如果伽马射线暴恰好落在其八个对角线方向之一上，以这种方式设置的模拟将完全逃过本检验。这是由单一源得出的约束的主要局限；位于不同方向的多个源可以消除这一局限，因为除非出现巧合，它们不可能全都与对角线对齐。</p>
<h3>格点间距：固定，还是随膨胀拉伸</h3>
<p>我们假设物理格点间距是固定的。如果网格随宇宙一同拉伸（共动格点间距），效应将不再随红移增大，\(I_2\) 将由 \(I_0\) 代替：约束随之减弱，上限放宽为原来的 \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]] 倍，即 [[comobile_a]]&nbsp;m。在 <em>z</em>&nbsp;=&nbsp;[[z]] 处，这一选择影响不大。</p>
<h3>更精确的格式</h3>
<p>模拟者可以采用高阶格式，其主导误差按 \(a^{4}\) 变化。此时效应随能量的四次方变化，对 \(a\) 的约束也会弱得多。LHAASO 没有公布针对该伽马射线暴的此类约束；要对其作定量估算，需要逐个光子的数据。专门为补偿色散而设计的项，同样会逃过这一约束。这些属于其他模型，需要单独检验。</p>
<h3>如果误差是线性的呢？</h3>
<p>在对称的格点上，不会出现与 \(a\) 成线性关系的效应。若某种离散化破坏了两个相反传播方向之间的对称性而产生这种效应，它就会受到 LHAASO 线性约束 \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\) 的限制：若系数的量级为1，则 \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m，即普朗克长度的十分之一。任何比这更粗的此类网格都被排除。</p>
<h3>计算的有效性</h3>
<p>上述展开假定 \(aE/\hbar c\ll1\)。在约束的极限值下，即使对 20&nbsp;TeV 的光子，也有 \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]。我们还将展开式与精确的色散关系进行了比较：当 \(ak\)&nbsp;=&nbsp;[[ak_test]] 时，相对偏差不超过 [[ecart_dispersion]]，与预期相符。</p>

<h2 id="contexte">5. 与已有结果相比，其价值何在</h2>
<p>Beane、Davoudi 和 Savage（2012）研究了格点量子色动力学的模拟。他们根据宇宙线能谱的截断，将格点间距的倒数约束为 \(1/b\gtrsim10^{11}\)&nbsp;GeV，即 \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m。我们的保守约束是他们的 [[beane_ratio]] 倍；LHAASO 的似然方法给出的是他们的 [[beane_ml_min]]～[[beane_ml_max]] 倍。因此，两种方法在量级上相互吻合，而所用的可观测量、粒子和假设各不相同：这是一次确认，而不是新纪录。</p>
<p>普朗克长度为 [[lpl]]&nbsp;m，还要低八个数量级。对于这样大小的格点间距，效应将比极限弱 [[facteur_planck_exact]] 倍。由于效应随能量的平方增长，所需光子的能量要高出约一亿倍，远远超出迄今观测到的一切：在这一量级上，任何飞行时间检验都无法触及普朗克尺度的网格。</p>

<h2 id="xi-shu">6. 文献核查：Xi 和 Shu（2025）</h2>
<p>Xi 和 Shu 用另一种方法分析了同一个伽马射线暴，给出 \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV（其表 III），约为 LHAASO 约束的 [[xs_rapport_lhaaso]] 倍。按照他们自己的定义重新推导，我们得不到这一数值。</p>
<ul>
<li>他们的式 (3) 规定延迟按 \((E/E_{\mathrm{QG},n})^{n}\) 变化。对于 \(n=1\)，他们的换算式 (6) \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\)（其中 \(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]]）是自洽的：我们得到 [[xs_c1]]。</li>
<li>对于 \(n=2\)，他们的式 (7) \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\)（其中 \(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]]）仍保留 \(1/\theta\) 的形式。将其用于他们的极限 \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV²，确实能重现他们表中的数值（[[xs_eq7]]&nbsp;GeV）。但由于延迟是二次的，他们的式 (3) 要求 \(1/\sqrt{\theta_2}\) 的依赖关系：\(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\)，即 \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV。</li>
<li>两者相差 [[xs_facteur]] 倍。一种可能的解释：\(\varepsilon^{2}\theta_2\) 等于 [[xs_eps2]]，而 [[xs_c2_imprime]] 看起来像是只对 10 的幂次开平方所得的 [[xs_eps2_imprime]] 的“平方根”。</li>
</ul>
<p>现状：该论文第1版中存在明显的不一致，有待与作者确认。我们没有重新分析他们的数据，也不评价他们的其他结果。即使修正后，他们的约束仍比 LHAASO 的强 [[xs_vs_lhaaso]] 倍。我们不采用这一约束。</p>

<h2 id="limites">7. 本检验不能说明什么</h2>
<ul>
<li>它没有探测到任何信号：零延迟与所有测量结果都相容。</li>
<li>它不计算我们身处模拟之中的任何概率；“95%”针对的是一个物理参数。</li>
<li>它约束的是一种特定的架构：立方网格、Yee 格式、固定的格点间距、无补偿。</li>
<li>即使探测到延迟，也不能指向一台计算机：本质上离散的物理，或其他量子引力效应，都会产生同样的信号。</li>
<li>LHAASO 的区间建立在关于源辐射的假设之上；我们沿用了这些假设。</li>
</ul>

<h2 id="suite">8. 下一步</h2>
<ol>
<li>合并在不同方向上观测到的多个源，以消除对角线方向的盲区。</li>
<li>对高阶格式（\(a^{4}\) 效应）作定量估算，这需要逐个光子的数据。</li>
<li>请 Xi 和 Shu 澄清他们的换算。</li>
<li>将检验推广到网格的其他特征：宇宙线的各向异性、带电粒子。</li>
</ol>

<h2 id="reproduire">9. 复现</h2>
<p>所有结果都由一个无外部依赖的 Python 脚本重新计算，脚本会先检验自身的公式：展开式与精确色散关系的比较、对角线方向的精确情形、往返换算、宇宙学积分，以及 \(Q\) 的平均值等于 3/5。</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>：脚本（Python&nbsp;3.10 或更高版本，仅用标准库；代码注释为法语）</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>：全部计算结果</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>：本文的 PDF 版本</li>
</ul>
<p>一项独立的交叉验证（numpy、scipy）以 10<sup>−15</sup> 的精度重现了宇宙学积分，用一千万次随机抽样重现了取向分位数，并通过数值求解色散关系重现了群速度。</p>
<p>本文取代2026年9月28日的第一版，新增了离散时间、取向、共动格点间距、线性效应，以及与 Beane 等人结果的比较。</p>

<h2 id="sources">参考文献</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>（2026年2月13日修订版）：式2、3和5，表 I。</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>（2012）。</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a>（2025）：式3、6和7，表 I 和表 III。</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302（1966）。</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395（1975）。</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House：数值色散与 Yee 格式的稳定性。</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>：基本物理常数。</li>
</ol>
""",
}

ARTICLE_2 = {
    'titre': '宇宙线是否勾勒出一个网格？',
    'description': '皮埃尔·俄歇天文台记录到的能量最高的粒子，'
                   '与立方网格理应在它们身上留下的印记相对照。',
    'date': '2026年9月28日',
    'corps': r"""
<section class="verdict-net">
<h2>结论</h2>
<p><strong>否。</strong>皮埃尔·俄歇天文台测得的 [[n_evt]] 个能量最高的宇宙线，没有显示出任何立方对称性。在完全不存在网格的天空中，有 [[p4_pct]]% 的情况会出现至少与观测结果同样明显的图样：我们看到的只是普通的偶然。</p>
<p>这个“否”的适用范围有限：只有 [[n_evt]] 个粒子，只有非常明显的图样才可能显现出来。更微弱的图样仍有可能存在。</p>
</section>

<h2 id="explication">说明</h2>
<p>如果我们的世界是由一台计算机算出来的，空间也许会被切分成极小的立方体，就像一张图片由像素组成一样。2012年，三位物理学家注意到，这种切分会留下痕迹：宇宙中速度最快的粒子，不会从各个方向同样地到来。某些方向会更“受青睐”，它们的排列就像立方体的面或角。</p>
<p>这样的粒子确实存在：它们就是宇宙线，是来自太空的原子核，能量远远高于我们的加速器所能产生的一切。在阿根廷，皮埃尔·俄歇天文台用一个巨大的探测器网络守候着它们。它公布了2004年至2020年间捕获到的 [[n_evt]] 个能量最高的粒子的清单，并注明了每个粒子到来的方向。</p>
<p>我们取出这 [[n_evt]] 个方向，看看它们是否沿着一个立方体排列。由于没有人知道这个立方体会怎样摆放，我们尝试了 [[n_orient]] 种摆放方式。其中最好的一种与数据略有吻合。但只要尝试这么多种摆放方式，总能找到一种略有吻合的，即使天空完全是随机形成的。</p>
<p>为了做出判断，我们随机生成了 [[n_ciels]] 片假天空，让同一个天文台去“看”它们，并对每一片做了完全相同的搜索。其中 [[p4_pct]]% 都能找到一个吻合得至少同样好的立方体。因此，真实的天空没有任何特别之处。要称得上是一条线索，它必须比几乎所有假天空都吻合得更好。</p>
<p>结论：没有发现网格的痕迹。但这项搜索只能看到明显的图样：只有 [[n_evt]] 个粒子，微弱的图样会被漏掉。此外，银河系的磁场会让这些粒子在途中拐弯，从而把部分图样弄模糊。因此，这项检验并不能证明空间是连续的；它表明的是：在我们能够观察的范围内，什么也没有。</p>

<h2 id="analyse">详细分析</h2>

<h3>1. 从网格到可检验的预言</h3>
<p>在格点间距为 \(a\) 的立方格点上，离散拉普拉斯算子把 \(k^{2}\) 替换为 \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\)。对于自由场，</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>其中 \(\mathbf n\) 是在格点坐标轴下表示的传播方向。这正是检验一中的同一个函数 \(Q\)。更一般地，网格对到达方向的任何影响（传播效应、依赖方向的能谱截断）都是 \(\mathbf n\) 的函数，且在立方群 \(O_h\) 下不变。而在 \(O_h\) 下不变的球谐函数只存在于 \(\ell=0,4,6,8,\dots\)：允许出现的第一个各向异性是立方谐函数 \(\ell=4\)，它正比于 \(Q-3/5\)。这是我们的主检验，在打开数据之前就已确定；\(\ell=6\) 作为第二项检验。Beane、Davoudi 和 Savage 写道，模拟“可能会在最高能宇宙线的分布中显露出来，表现为一定程度的转动对称性破缺，反映出底层格点的结构”。</p>

<h3>2. 数据</h3>
<p>皮埃尔·俄歇天文台的目录（ApJS 264, 50, 2023）：2004年1月1日至2020年12月31日记录的 [[n_evt]] 个能量最高的簇射，能量从 [[e_min]] 到 [[e_max]]&nbsp;EeV，天顶角最大为 [[zmax]]°。公开文件中还包含 [[n_calib]] 个用于校准的混合事例，它们不属于这 [[n_evt]] 个事例：我们将其剔除。我们使用地面探测器阵列重建的赤经和赤纬。每次运行时都会校验文件的 SHA-256 指纹。在这些能量下，天顶角 [[zmax]]° 以内的探测达到全效率，因此曝光完全由几何决定。</p>

<h3>3. 探测器的曝光</h3>
<p>位于纬度 \(a_0\)&nbsp;=&nbsp;[[lat]]°、接收天顶角 \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]° 的地面探测器，其曝光在赤经上是均匀的，在赤纬 \(\delta\) 上为（Sommers，2001）：</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>可见天空止于 \(\delta\)&nbsp;=&nbsp;[[dec_max]]°，即天球的 [[ciel_pct]]%。因此，俄歇天文台看到的各向同性天空并不是均匀的：后文的所有比较都是将数据与这样的天空对比，而不是与均匀的球面对比。</p>

<h3>4. 统计量</h3>
<p>设 \(R\) 为网格的一个取向，其各行为 \(\mathbf e_k\)，并令 \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\)。对于 \(N\) 个观测方向：</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>其中 \(\langle\cdot\rangle_\omega\) 是在按曝光加权的各向同性天空上的平均。\(T>0\) 表示沿立方体坐标轴方向的超出，\(T<0\) 表示沿其对角线方向的超出；取绝对值可同时涵盖两者。由于 \(f\) 是4次多项式，\(T(R)\) 仅通过15个矩 \(\sum_i\mathbf n_i^{\alpha}\) 依赖于数据；平均值和方差用高斯–勒让德求积精确计算。最大值取自 [[n_orient]] 个均匀抽取（哈尔测度）的取向。对于 \(\ell=6\)，取 \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\)，其中 \(\alpha\)&nbsp;=&nbsp;[[alpha6]]（即 \(-15/11\)），使其与 \(\ell=4\) 正交；联合检验对 \(T_4^{2}+T_6^{2}\) 求最大值。</p>

<h3>5. 标定偶然性</h3>
<p>在 [[n_orient]] 个取向中寻找最佳者，会机械地抬高 \(Z_4\)：它并不服从正态分布。因此，我们按曝光抽取 [[n_ciels]] 片各含 \(N\) 个事例的各向同性天空，并对它们施加完全相同的最大化过程。在“没有网格”的假设下，\(Z_4\) 的中位数为 [[z4_50]]；它在5%的情况下超过 [[z4_95]]，在1%的情况下超过 [[z4_99]]，在0.1%的情况下超过 [[z4_999]]。因此，p 值 \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\) 已计入选择取向的代价。</p>

<h3>6. 结果</h3>
<div class="tableau"><table>
<thead><tr><th>检验</th><th>观测统计量</th><th>p 值</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\)（主检验）</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\) 与 \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>在最佳取向下，\(Q\) 的平均值为 [[q_obs]]，而预期值为 [[q_iso]]，即向坐标轴方向超出 [[q_ecart_pct]]%。这并不显著：主检验的 \(p\)&nbsp;=&nbsp;[[p4]]，且没有任何次要检验低于0.05。数据与完全不存在立方对称性相容。</p>

<h3>7. 本检验能看到什么</h3>
<p>为定量评估灵敏度，我们注入一个立方图样：密度正比于 \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\)。当 \(\varepsilon>0\) 时，沿坐标轴的通量是平均值的 \(1+\varepsilon\) 倍；当 \(\varepsilon<0\) 时，超出转移到对角线方向。对每个 \(\varepsilon\)，用 [[n_ciels_signal]] 片随机取向的天空得出 \(Z_4\) 的分布。95%上限：向坐标轴方向 \(\varepsilon\le\)&nbsp;[[eps_axes]]，向对角线方向 \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]]。换言之，沿坐标轴约 [[eps_axes_pct]]%（或沿对角线 [[eps_diag_pct]]%）以内的超出并未被排除：这是一个较弱的约束，受限于事例数少。</p>
<p>脚本首先检验自身的计算链：\(Q\) 在立方群下的不变性、多项式展开的精确性、赤纬超过 [[dec_max]]° 处曝光为零、各向同性下 \(T\) 已标准化（均值为0、方差为1）、\(\ell=6\) 与 \(\ell=4\) 的正交性，以及对注入的明显图样的探测——其取向的恢复误差在 [[ecart_orient]]° 以内。</p>

<h3>8. 局限</h3>
<ul>
<li>宇宙线带电：银河系磁场和河外磁场会使其方向偏转，原子核越重，偏转越大。所寻找的图样尺度很大（坐标轴与对角线相距 [[angle_diag]]°），能经受适度的偏转，但在源处或传播过程中形成的印记会被部分抹去。</li>
<li>我们假设网格相对于遥远的恒星是固定的（赤道坐标）。相对于它们运动或转动的网格需要另一种检验。</li>
<li>[[n_evt]] 个事例、[[ciel_pct]]% 的天空：统计功效较低，上面的上限就说明了这一点。</li>
<li>真实的天体物理各向异性可能包含 \(\ell=4\) 分量。若结果为阳性，就必须先排除它们；零结果则不受其影响。</li>
<li>本检验不计算我们身处模拟之中的概率：它针对的是一个明确的特征，即立方网格的特征。</li>
</ul>

<h3>9. 复现</h3>
<p>一个 Python 脚本（numpy）大约一分钟即可完成全部计算：读取并检查数据、自检、统计量、模拟天空、上限。随机数生成器使用固定种子：每次运行的结果完全相同。</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-2/analyse.py" download>analyse.py</a>：脚本</li>
<li><a href="/fichiers/test-2/resultats.json" download>resultats.json</a>：全部计算结果</li>
<li><a href="/fichiers/test-2/donnees/auger_catalogSD.csv" download>auger_catalogSD.csv</a>：皮埃尔·俄歇天文台的数据（CC BY-SA 4.0 许可）</li>
</ul>

<h2 id="sources">参考文献</h2>
<ol class="sources">
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>（2012）。</li>
<li>Pierre Auger Collaboration, <cite>A Catalog of the Highest-Energy Cosmic Rays Recorded During Phase I of Operation of the Pierre Auger Observatory</cite>, ApJS 264, 50（2023），<a href="https://arxiv.org/abs/2211.16020">arXiv:2211.16020</a>。</li>
<li>Pierre Auger Collaboration, <cite>Auger Open Data</cite>，第3版，<a href="https://doi.org/10.5281/zenodo.10488964">DOI 10.5281/zenodo.10488964</a>；探测效率：<a href="https://opendata.auger.org/data.php">opendata.auger.org</a>。</li>
<li>P. Sommers, <cite>Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory</cite>, Astroparticle Physics 14, 271（2001），<a href="https://arxiv.org/abs/astro-ph/0004016">arXiv:astro-ph/0004016</a>。</li>
</ol>
""",
}

ARTICLE_3 = {
    'titre': '光在某些方向上走得更慢吗？',
    'description': '分布在全天的八个伽马射线源联合起来，弥补检验一的盲区，'
                   '并在任意取向下约束立方网格的格点间距。',
    'date': '2026年9月28日',
    'corps': r"""
<section class="verdict-net">
<h2>结论</h2>
<p><strong>否。</strong>所研究的 [[n_src]] 个源中，没有一个显示出网格会造成的延迟。将它们的方向结合起来，无论网格取向如何、时间步长如何，格点间距大于或等于 [[a_exclue]]&nbsp;m 的立方网格都被排除：检验一的盲区已被消除。</p>
</section>

<h2 id="explication">说明</h2>
<p>如果宇宙是在一个网格上计算出来的，就像图片由像素组成一样，那么光在其中各个方向上前进的速度就不会完全相同。能量最高的光会有极其微小的延迟，沿网格棱边方向的延迟比沿对角线方向的更大。经过数十亿年的旅程，这种延迟就会变得可以测量。</p>
<p>检验一在有史以来观测到的最亮的伽马射线暴中寻找这种延迟，结果一无所获。但当时还留有一个漏洞：如果模拟以尽可能大的步长在时间上推进，光沿网格对角线传播时就不再有任何延迟。于是，一个恰好位于对角线上的单一源无法得出任何结论。</p>
<p>这里，我们同时观察天空中不同方向上的 [[n_src]] 个源：三次遥远的恒星爆发、四个中心黑洞非常活跃的星系，以及蟹状星云中的脉冲星。对每一个源，天文学家团队都已测得：在一定精度内没有出现任何延迟。我们重读了每一篇论文，把所有结果换算到同一约定下，然后寻找对隐藏网格最有利的网格取向，也就是使限制最弱的那个取向。</p>
<p>不可能让所有的源同时落在对角线上。即使在最有利的取向下，仍有三个源离对角线足够远，本应出现延迟。因此，格子尺寸至少为 [[a_exclue]]&nbsp;m 的网格在所有取向下都被排除。这一尺寸仍约为普朗克长度的 [[planck_x]] 倍：精细得多的网格仍然完全可能存在。</p>

<h2 id="analyse">详细分析</h2>

<h3>1. 模型</h3>
<p>与检验一相同：格点间距为 \(a\) 的立方格点上的麦克斯韦方程组（Yee 格式），时间步长 \(c\,\Delta t=\sigma a/\sqrt{3}\)，其中 \(0\le\sigma\le1\)。在主导阶，</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\,Q_{\mathrm{eff}}\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3},\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>由于 \(1/3\le Q\le1\)，有 \(Q_{\mathrm{eff}}\ge0\)：光子总是被减速；当 \(\sigma=1\) 时，在体对角线上恰好 \(Q_{\mathrm{eff}}=0\)。在最终约束处，对 20&nbsp;TeV 的光子有 \(aE/\hbar c\)&nbsp;=&nbsp;[[ae]]：展开式成立。</p>

<h3>2. 从已发表的极限到格点间距的约束</h3>
<p>这八篇论文都用 \(v/c\simeq1-\tfrac{3}{2}(E/E_{\mathrm{QG},2})^{2}\) 描述二次延迟，并使用 Jacob 和 Piran 的距离 \(K_2=\int_0^{z}(1+z')^{2}\,dz'/H(z')\)。两相对照，</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}}\quad\Longrightarrow\quad a\sqrt{Q_{\mathrm{eff}}(\mathbf n_i)}\le B_i=\frac{\sqrt{12}\,\hbar c}{E_i}.$$
<p>事先确定的规则：95%置信极限、亚光速情形、飞行时间、每篇论文中限制最弱的方法。每个极限都通过 \(E_i\sqrt{K_2^{\mathrm{LHAASO}}(z_i)/K_2^{(i)}(z_i)}\) 换算到 LHAASO 的宇宙学参数；该因子不超过 [[fc_max]]。每一个已发表的换算都根据论文印出的参数重新计算，并重现了论文中的数值（自检）。</p>
<div class="tableau"><table>
<thead><tr><th>源</th><th>仪器</th><th>\(z\) 或距离</th><th>已发表的 \(E_{\mathrm{QG},2}\) (GeV)</th><th>统一宇宙学参数 (GeV)</th><th>\(B_i\) (m)</th></tr></thead>
<tbody>
<tr><td>GRB 221009A</td><td>LHAASO</td><td>[[s0_z]]</td><td>[[s0_pub]]</td><td>[[s0_com]]</td><td>[[s0_b]]</td></tr>
<tr><td>GRB 190114C</td><td>MAGIC</td><td>[[s1_z]]</td><td>[[s1_pub]]</td><td>[[s1_com]]</td><td>[[s1_b]]</td></tr>
<tr><td>GRB 090510</td><td>Fermi-LAT</td><td>[[s2_z]]</td><td>[[s2_pub]]</td><td>[[s2_com]]</td><td>[[s2_b]]</td></tr>
<tr><td>Mrk 501</td><td>H.E.S.S.</td><td>[[s3_z]]</td><td>[[s3_pub]]</td><td>[[s3_com]]</td><td>[[s3_b]]</td></tr>
<tr><td>Mrk 421</td><td>MAGIC</td><td>[[s4_z]]</td><td>[[s4_pub]]</td><td>[[s4_com]]</td><td>[[s4_b]]</td></tr>
<tr><td>PKS 2155-304</td><td>H.E.S.S.</td><td>[[s5_z]]</td><td>[[s5_pub]]</td><td>[[s5_com]]</td><td>[[s5_b]]</td></tr>
<tr><td>PG 1553+113</td><td>H.E.S.S.</td><td>[[s6_z]]</td><td>[[s6_pub]]</td><td>[[s6_com]]</td><td>[[s6_b]]</td></tr>
<tr><td>蟹状星云（脉冲星）</td><td>MAGIC</td><td>[[s7_z]]&nbsp;kpc</td><td>[[s7_pub]]</td><td>[[s7_com]]</td><td>[[s7_b]]</td></tr>
</tbody>
</table></div>

<h3>3. 最不利取向</h3>
<p>对于格点的一个取向 \(R\)，各源共同给出的约束为</p>
$$a\le A(R)=\min_i\frac{B_i}{\sqrt{Q_{\mathrm{eff}}(R\mathbf n_i)}},$$
<p>其中位于对角线上的源在 \(\sigma=1\) 时不提供任何约束。我们寻找 \(\max_R A(R)\)：先用均匀抽取的 [[n_orient]] 个旋转和构造出的取向（将每个源置于一条对角线上，再绕该对角线旋转），然后进行局部细化。另一个独立的随机种子以 [[ecart_graines]] 的相对精度得到了相同的最大值。优化程序已在已知情形下得到验证：单个源在 \(\sigma=1\) 时不提供任何约束；两个相隔两条对角线夹角的源可以同时置于对角线上。</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>最不利取向 (m)</th><th>95%的取向 (m)</th></tr></thead>
<tbody>
<tr><td>0</td><td>[[pire0]]</td><td>[[q95_0]]</td></tr>
<tr><td>0.5</td><td>[[pire05]]</td><td>[[q95_05]]</td></tr>
<tr><td>0.9</td><td>[[pire09]]</td><td>[[q95_09]]</td></tr>
<tr><td>1</td><td>[[pire1]]</td><td>[[q95_1]]</td></tr>
</tbody>
</table></div>
<p>当 \(\sigma<1\) 时，与检验一相比没有任何变化：GRB&nbsp;221009A 起主导作用，其他源的灵敏度低 [[x_min]]～[[x_max]] 倍。一切取决于 \(\sigma=1\)：仅把 GRB&nbsp;221009A 放在对角线上已经不够，因为其他源此时会从斜向“看到”网格。最不利的折中使 GRB&nbsp;221009A 偏离最近的对角线 [[ang_grb]]°（\(Q_{\mathrm{eff}}\)&nbsp;=&nbsp;[[qeff_grb]]），并使 [[n_actives]] 个约束相互平衡：GRB&nbsp;221009A、GRB&nbsp;090510 和蟹状星云。此时约束为 [[pire1]]&nbsp;m，即能标 \(\hbar c/a\ge\)&nbsp;[[echelle]]&nbsp;GeV。由于对任意取向 \(A(R)\) 都随 \(\sigma\) 增大，该约束对所有 \(\sigma\le1\) 均成立。在 \(\sigma=1\) 时，各取向的中位数为 [[med1]]&nbsp;m。</p>
<p>消除盲区并非理所当然：GRB&nbsp;190114C 与 GRB&nbsp;090510 相隔 [[ang_190_090]]°，几乎等于两条对角线之间的夹角（[[ang_diag]]°），而 GRB&nbsp;090510 与 PKS&nbsp;2155-304 仅相距 [[ang_090_pks]]°。正是天空其余部分源的多样性消除了盲区。</p>

<h3>4. 稳健性</h3>
<p>\(\sigma=1\) 时的最不利取向随各种选择的变化：</p>
<ul>
<li>去掉 GRB&nbsp;221009A：[[v_sans_lhaaso]]&nbsp;m，盲区仍然被消除；</li>
<li>已发表的极限不作宇宙学换算：[[v_sans_cosmo]]&nbsp;m；</li>
<li>Fermi 结果计入源内效应（该论文表 V）：[[v_fermi]]&nbsp;m；</li>
<li>仅用伽马射线暴：[[v_sursauts]]&nbsp;m；</li>
<li>仅用耀变体和脉冲星：[[v_blazars]]&nbsp;m。</li>
</ul>

<h3>5. 比较</h3>
<p>对任意取向和任意时间步长都成立的约束，比检验一在连续时间下的约束弱 [[x_test1]] 倍。Beane、Davoudi 和 Savage 根据宇宙线能谱的截断得到 \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m；我们在连续时间下的约束是他们的 [[x_beane0]] 倍，普适约束是他们的 [[x_beane]] 倍。</p>

<h3>6. 局限</h3>
<ul>
<li>对每个取向，联合约束取的是逐一发表的95%置信极限中最严格的一个：这不是联合似然，各论文也没有公布联合似然。由于在最不利取向下有三个极限起作用，所保证的覆盖率至少为 [[couverture]]%，而不是95%。</li>
<li>每篇论文都假设不存在补偿或模仿延迟的源内时间偏移。</li>
<li>Mrk&nbsp;421 和 PG&nbsp;1553+113 的红移不确定；这两个源在最不利取向下不起作用。起作用的蟹状星云，其距离已包含在 MAGIC 的不确定度中。</li>
<li>高阶格式（\(a^{4}\) 误差）、补偿项、非立方网格或随膨胀拉伸的网格，都不受此约束限制。</li>
<li>二次分析：没有重新分析任何光子。取向比例是几何上的比例，而不是关于宇宙的概率。</li>
</ul>

<h3>7. 复现</h3>
<p>脚本在几秒钟内完成全部计算，并首先检验自身的公式和每一个已发表的换算。每个输入数值都在 <code>sources.md</code> 中注明出处（页码和表格）。</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-3/analyse.py" download>analyse.py</a>：脚本</li>
<li><a href="/fichiers/test-3/resultats.json" download>resultats.json</a>：全部计算结果</li>
<li><a href="/fichiers/test-3/sources.md" download>sources.md</a>：每个输入数值的引文</li>
</ul>

<h2 id="sources">参考文献</h2>
<ol class="sources">
<li>LHAASO Collaboration, GRB 221009A, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>，表 I。</li>
<li>MAGIC Collaboration, GRB 190114C, <a href="https://arxiv.org/abs/2001.09728v4">arXiv:2001.09728v4</a>，表 I。</li>
<li>Fermi-LAT Collaboration, GRB 090510, <a href="https://arxiv.org/abs/1305.3463v1">arXiv:1305.3463v1</a>，表 IV 和表 V。</li>
<li>H.E.S.S. Collaboration, Mrk 501, <a href="https://arxiv.org/abs/1901.05209v1">arXiv:1901.05209v1</a>。</li>
<li>MAGIC Collaboration, Mrk 421, <a href="https://arxiv.org/abs/2406.07140v1">arXiv:2406.07140v1</a>，表 2。</li>
<li>H.E.S.S. Collaboration, PKS 2155-304, <a href="https://arxiv.org/abs/1101.3650v2">arXiv:1101.3650v2</a>。</li>
<li>H.E.S.S. Collaboration, PG 1553+113, <a href="https://arxiv.org/abs/1501.05087v1">arXiv:1501.05087v1</a>，表 5。</li>
<li>MAGIC Collaboration，蟹状星云脉冲星，<a href="https://arxiv.org/abs/1709.00346v1">arXiv:1709.00346v1</a>，表 6。</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>。</li>
<li>坐标：<a href="https://simbad.cds.unistra.fr/simbad/">SIMBAD</a>（CDS，斯特拉斯堡）。</li>
</ol>
""",
}

ARTICLE_4 = {
    'titre': '量子随机性是否暴露出一个程序？',
    'description': '来自量子实验的数百万个比特，接受一系列检验的筛查；'
                   '这些检验能够识破模拟可能使用的伪随机数生成器。',
    'date': '2026年9月28日',
    'corps': r"""
<section class="verdict-net">
<h2>结论</h2>
<p><strong>否。</strong>在我们检验的、来自量子测量的原始比特中，没有出现任何伪随机数生成器的特征，而同样的检验却识破了作为对照的四个简单生成器。有一点必须先说明：分析之前确定的规则，在按原样发布的 IBM 数据上被触发了；但原因已经查明——九台机器中有一台在整批整批的测量中一直卡在 0 或 1 上——而这种缺陷并不具有生成器的结构。将这台机器排除在外，是在看过数据之后才决定的；我们如实指出这一点。</p>
<p>这个“否”的适用范围有限：它排除的是从简单生成器中取得量子测量结果的模拟，而不是使用密码学级生成器的模拟——这类生成器在原理上就无法与真正的随机区分。</p>
</section>

<h2 id="explication">说明</h2>
<p>如果世界是一场模拟，它就必须给出每一次量子测量的结果：0 或 1。物理学告诉我们，这个结果在本质上是不可预测的。而计算机做不出真正的随机：它只能按照一套计算配方把随机“制造”出来。一个精打细算的模拟会采用快速而简单的配方，而简单的配方会留下痕迹：重复、隐藏的规律，以及可以通过计算找出来的结构。</p>
<p>因此，我们选取了真实量子实验产生、并由实验者公开发布的 0 和 1 序列，在其中寻找这些痕迹。第一个难点是：大多数公开的量子随机源在发布结果之前，都会先把结果送进一台数学“搅拌机”。这台搅拌机的设计目的就是抹去一切结构；检验它的输出，对源头本身说明不了任何问题。我们仍然检验了这些数据，但它们不计入结论。</p>
<p>剩下两个原始来源：一个是美国俄勒冈州波特兰大学的纠缠光子装置，它按原样公布自己的比特；另一个是 IBM 的九台量子计算机，人们让它们用单个量子比特掷了数百万次硬币。光子通过了所有检验。IBM 的机器给出的 0 略多了一些，这是一个已知的缺陷，数据的作者已作过解释；校正这种不平衡之后，它们也能通过。其中一台名为 Belem 的机器，在整批整批的测量中一直卡住不动：这是故障，而不是计算配方。</p>
<p>对照生成器的表现与预期一致：简单的配方被识破，其中包括一个非常流行、却能通过 NIST 官方测试套件的生成器；复杂精巧的配方没有被识破，2 的平方根的各位数字也没有——尽管这些数字完全可以计算出来。这正是本检验的局限：一场精心设计的模拟不会留下任何这类痕迹。</p>

<h2 id="analyse">详细分析</h2>

<h3>1. 什么是可以检验的</h3>
<p>统计检验只能反映一串比特所经历的最后一道处理：经密码学函数哈希处理后的输出，无论输入是什么，看起来都像完美的随机。我们共检验了 [[bits_total]] 个比特，其中原始比特 [[bits_bruts]] 个：</p>
<div class="tableau"><table>
<thead><tr><th>数据集</th><th>来源</th><th>处理</th><th>比特数</th></tr></thead>
<tbody>
<tr><td>parity</td><td>偏振纠缠光子（Kavulich 等，2021）</td><td>无</td><td>[[n_parity]]</td></tr>
<tr><td>ibm</td><td>单个量子比特，Hadamard 门，测量；九台机器（Root 和 Becker，2024）</td><td>无</td><td>[[n_ibm]]</td></tr>
<tr><td>anu</td><td>真空涨落，ANU</td><td>AES-128</td><td>[[n_anu]]</td></tr>
<tr><td>beacon</td><td>NIST Beacon 2.0</td><td>SHA-512</td><td>[[n_beacon]]</td></tr>
</tbody>
</table></div>
<p>只有 parity 和 ibm 能反映量子随机性的本质。NIST 于 2015 年进行的无漏洞贝尔检验，其原始数据未被采用：该实验中测量设置的选择结合了物理随机源和一个伪随机源，而且探测结果并不是均匀分布的比特。对于 Beacon，我们在 [[engagements]] 对相邻脉冲上核验了其公布的承诺链。</p>

<h3>2. 第一级：NIST SP 800-22 测试套件</h3>
<p>官方测试套件的 15 项检验均已重新实现，并以 [[annexe_ecart]] 以内的偏差重现了该文件附录 B 中的 [[annexe_n]] 个 p 值（有一项检验的偏差为 [[annexe_ecart_chev]]）。数据被切分为 [[n_seq]] 个长度为 10<sup>6</sup> 比特的序列；全部 [[np1]] 个 p 值构成一个检验族，用 Holm 方法校正，总体显著性水平为 1%。</p>
<ul>
<li>parity：[[par_np1]] 个 p 值，未出现拒绝（最小校正后 p 值：[[par_p1]]）；比特为 1 的比例：[[par_frac]]。</li>
<li>anu 和 beacon：未出现拒绝（anu 的最小校正后 p 值：[[anu_p1]]）。</li>
<li>ibm：共 [[ibm_np1]] 个 p 值，拒绝 [[ibm_rej1]] 次；比特为 1 的比例：[[ibm_frac]]，即偏离 [[ibm_z]] 个标准差。排除 Belem 这台机器后，经冯·诺依曼提取器（它能精确消除恒定偏差）处理，剩下 [[vn_bits]] 个比特，[[vn_np]] 个 p 值中未出现拒绝（[[vn_p]]）：失败源于数据作者所描述的偏差。</li>
</ul>

<h3>3. 第二级：生成器的特征</h3>
<p>NIST 测试套件能说明一个序列是否偏离理想的随机，却不能说明原因。以下三项检验专门针对算法生成器特有的缺陷：</p>
<ul>
<li><strong>线性复杂度。</strong>Berlekamp-Massey 算法给出能复现一段 \(n\) 比特序列的最短线性反馈移位寄存器的长度 \(L\)。对随机序列，\(L\simeq n/2\)；在 \(\mathrm{GF}(2)\) 上、状态少于 \(n/2\) 比特的任何线性生成器都会给出 \(L<n/2\)。所用片段长 [[seg_bm]] 比特，或连续读取，或每 48 个比特取 1 个、每 64 个比特取 1 个：状态不超过 [[etat_max]] 比特的生成器均在覆盖范围内。</li>
<li><strong>重复。</strong>每个 64 比特的窗口都与所有其他窗口比较；相同窗口对的期望数目约为 [[rep_attendu]]。哪怕只出现一次重复，也意味着存在周期或重复使用的种子。</li>
<li><strong>长程相关。</strong>计算滞后 17 至 [[lag_max]] 的自相关，并作 Bonferroni 校正。</li>
</ul>
<p>主检验族，以 1% 的水平对 [[np2]] 个 p 值作 Holm 校正：parity 未出现拒绝（[[par_p2]]）；其 \(L\) 与 \(n/2\) 的最大偏差为 [[par_ecart_l]]；没有任何重复；长程相关：[[par_auto]]。anu 和 beacon 未出现拒绝。ibm 出现 [[ibm_rej2]] 次拒绝。</p>

<h3>4. IBM 数据中的拒绝：一台卡住的机器</h3>
<p>IBM 数据由 [[ibm_essais]] 次试验组成，每次试验包含 8192 次测量。其中 [[ibm_const]] 次试验的结果完全恒定（[[ibm_const0]] 次全为 0，[[ibm_const1]] 次全为 1），另有 [[ibm_quasi]] 次的恒定程度超过 99%；它们全部来自 Belem 这台机器。相同的窗口对共有 [[ibm_paires]] 对，全都由各位比特完全相同的窗口构成：在组成正常的窗口中，相同窗口对的数目为 [[ibm_paires_typ]]。卡死不变的输出不是伪随机数生成器的输出，而是输出的缺失。</p>
<p>排除 Belem 是在看过数据之后才决定的：因此这是一项次要分析，有其独立的 Holm 校正，初始规则的结果也照样公布。在其余八台机器上（[[sb_bits]] 个比特），第二级检验未出现拒绝（[[sb_np2]] 个 p 值，最小校正后 p 值为 [[sb_p2]]）；\(L\) 与 \(n/2\) 的最大偏差为 [[sb_ecart_l]]，且没有任何重复。滞后 1 处存在相关（[[sb_r1]]，即 [[sb_z1]] 个标准差）：这是一种短程的测量缺陷，与生成器的结构无关。第一级检验在这里出现 [[sb_rej1]] 次拒绝（共 [[sb_np1]] 个 p 值），原因在于偏差。</p>

<h3>5. 对照生成器</h3>
<p>同一套流程被应用于每个已知生成器的 [[bits_ctrl]] 个比特；如果某个对照生成器的表现不符合预期，脚本就会中止。</p>
<div class="tableau"><table>
<thead><tr><th>生成器</th><th>预期</th><th>结果（最小校正后 p 值，第一级和第二级）</th></tr></thead>
<tbody>
<tr><td>20 阶 LFSR</td><td>检出</td><td>检出：\(L\)&nbsp;=&nbsp;[[l20_lmin]]，重复</td></tr>
<tr><td>31 阶 LFSR</td><td>检出</td><td>检出：\(L\)&nbsp;=&nbsp;[[l31_lmin]]，\(\log_{10}p\)&nbsp;=&nbsp;[[l31_log10p]]</td></tr>
<tr><td>32 位 LCG</td><td>检出</td><td>检出：频谱检验，长程相关</td></tr>
<tr><td>Mersenne Twister</td><td>检出</td><td>仅由第二级检出：\(L\)&nbsp;=&nbsp;[[mt_lmin]]，\(\log_{10}p\)&nbsp;=&nbsp;[[mt_log10p]]；NIST 测试套件毫无反应（[[mt_p1]]）</td></tr>
<tr><td>PCG64</td><td>未检出</td><td>无（[[pcg_p1]]；[[pcg_p2]]）</td></tr>
<tr><td>计数器模式下的 SHA-256</td><td>未检出</td><td>无（[[sha_p1]]；[[sha_p2]]）</td></tr>
<tr><td>\(\sqrt{2}\) 的二进制展开数字</td><td>未检出</td><td>无（[[r2_p1]]；[[r2_p2]]）</td></tr>
</tbody>
</table></div>
<p>Mersenne Twister 的结果表明，第二级检验确实为官方测试套件增加了灵敏度。PCG64、SHA-256 和 \(\sqrt{2}\) 则表明，一个完全确定性的序列可以没有任何可检测的特征。</p>

<h3>6. 局限</h3>
<ul>
<li>密码学级的生成器无法与真正的随机区分：本检验排除的是使用简单生成器的模拟，而不是精心设计的模拟。SP 800-22 文件本身也指出：任何一组检验都不能取代密码分析。</li>
<li>第二级检验的覆盖范围：线性生成器只有在其状态少于 [[etat_max]] 比特时才会被检出；重复只有在周期短于数据长度时才会被检出。</li>
<li>原始数据量不大，而且两个原始来源都没有经过无漏洞贝尔检验的认证。</li>
<li>排除 Belem 这台机器是事后作出的决定；其原因有据可查，未作排除的结果也已公布。</li>
<li>ANU 和 Beacon 数据集衡量的只是 AES-128 和 SHA-512 的质量。</li>
</ul>

<h3>7. 复现</h3>
<p>数据由 <code>telecharger.py</code> 重新获取，它会校验数据的指纹；随后 <code>analyse.py</code> 无需联网即可运行，连同自检在内用时不到两分钟。</p>
<pre><code>python3 telecharger.py
python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-4/analyse.py" download>analyse.py</a>：分析脚本</li>
<li><a href="/fichiers/test-4/telecharger.py" download>telecharger.py</a>：带校验的数据下载</li>
<li><a href="/fichiers/test-4/resultats.json" download>resultats.json</a>：全部计算结果</li>
<li><a href="/fichiers/test-4/sources.md" download>sources.md</a>：每项陈述的出处引文</li>
</ul>

<h2 id="sources">参考文献</h2>
<ol class="sources">
<li>J. T. Kavulich, B. P. Van Deren, M. Schlosshauer, <cite>Searching for evidence of algorithmic randomness and incomputability in the output of quantum random number generators</cite>, Physics Letters A 388, 127032（2021），<a href="https://arxiv.org/abs/2101.01238">arXiv:2101.01238</a>；数据：<a href="https://zenodo.org/records/4440318">Zenodo 4440318</a>。</li>
<li>B. P. Van Deren, J. T. Kavulich, M. Schlosshauer, <cite>Parity-based, bias-free optical quantum random number generation with min-entropy estimation</cite>, <a href="https://arxiv.org/abs/2006.11425">arXiv:2006.11425</a>。</li>
<li>O. Root, M. Becker, <cite>Does True Randomness Exist? Efficacy Testing IBM Quantum Computers via Statistical Randomness</cite>, <a href="https://arxiv.org/abs/2401.12250">arXiv:2401.12250</a>；数据：<a href="https://doi.org/10.5281/zenodo.10542216">DOI 10.5281/zenodo.10542216</a>。</li>
<li>J. Y. Haw et al., <cite>Maximization of Extractable Randomness in a Quantum Random-Number Generator</cite>, <a href="https://arxiv.org/abs/1411.4512">arXiv:1411.4512</a>。</li>
<li>NIST, <cite>A Reference for Randomness Beacons: Format and Protocol Version 2</cite>, <a href="https://csrc.nist.gov/pubs/ir/8213/ipd">NISTIR 8213</a>。</li>
<li>L. K. Shalm et al., <cite>A strong loophole-free test of local realism</cite>, <a href="https://arxiv.org/abs/1511.03189">arXiv:1511.03189</a>。</li>
<li>NIST, <cite>A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications</cite>, <a href="https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final">SP 800-22 Rev. 1a</a>。</li>
</ol>
""",
}
