"""Chinois simplifié : traduction de fr.py (langue source).

Mêmes marqueurs, mêmes formules et même structure HTML que la source ;
le corps est une chaîne brute à cause des barres obliques inverses.
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
<li><strong>这并未超越已有的界限。</strong>早在2012年，Beane、Davoudi 和 Savage 就已根据宇宙线得到了相同的量级（约 [[b_beane]]&nbsp;m）。本结果通过另一种可观测量，对此作出了独立的确认。</li>
<li><strong>新结果：时间步长不可忽略。</strong>如果时间也像任何数值模拟中那样被离散化，效应就会减弱。在最大稳定步长下，光沿立方体的八个对角线方向传播时完全不发生色散：此时仅凭单个伽马射线暴，无法给出普适的约束。对于95%的取向，格点间距仍小于 [[a95_sigma1]]&nbsp;m。</li>
<li><strong>主导误差与 <em>a</em> 成线性关系的网格</strong>，只要格点间距大于 [[a_lineaire]]&nbsp;m（普朗克长度的十分之一），即被排除。</li>
<li><strong>普朗克尺度的格点间距仍无法触及</strong>：其效应将比本检验所能探测的弱约 [[facteur_planck]] 倍。</li>
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
<tr><td>校准后的 ML</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
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
<tr><td>校准后的 ML</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>要点中采用的是最保守的值 [[a_resume]]&nbsp;m：这是为便于呈现而取的包络，而不是一个新的区间。在这一极限下，1&nbsp;TeV 光子最多比 [[e_bas]]&nbsp;TeV 光子晚到 [[retard_limite]]&nbsp;s。</p>
<p>以下是几个预测值，它们并非测量结果（比较 1&nbsp;TeV 光子与 [[e_bas]]&nbsp;TeV 光子）：</p>
<div class="tableau"><table>
<thead><tr><th>格点间距</th><th>预测的 \(\eta_2\)</th><th>预测的延迟</th><th>结论</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]]～[[p26_eta_max]]</td><td>[[p26_ret_min]]～[[p26_ret_max]]&nbsp;s</td><td>在所有取向下均被排除</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]]～[[p27_eta_max]]</td><td>[[p27_ret_min]]～[[p27_ret_max]]&nbsp;s</td><td>仅校准后的 ML 可在坐标轴附近（\(Q>\)&nbsp;[[q_cal_axe]]）将其排除</td></tr>
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
<p>在对称的格点上，不会出现与 \(a\) 成线性关系的效应。若某种离散化破坏了两个传播方向之间的对称性而产生这种效应，它就会受到 LHAASO 线性约束 \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\) 的限制：若系数的量级为1，则 \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m，即普朗克长度的十分之一。任何比这更粗的此类网格都被排除。</p>
<h3>计算的有效性</h3>
<p>上述展开假定 \(aE/\hbar c\ll1\)。在约束的极限值下，即使对 20&nbsp;TeV 的光子，也有 \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]。我们还将展开式与精确的色散关系进行了比较：当 \(ak\)&nbsp;=&nbsp;[[ak_test]] 时，相对偏差不超过 [[ecart_dispersion]]，与预期相符。</p>
""",
}
