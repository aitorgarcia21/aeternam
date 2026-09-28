"""日本語：フランス語の原文（fr.py）の翻訳。

各 [[マーカー]] は resultats.json の数値に置き換えられ、この言語の慣習に従って書かれる。
数式 $$…$$ と \\(…\\) はすべての言語で同一。バックスラッシュを含むため、生文字列（r\"\"\"…\"\"\"）が必須。
"""
NOM = '日本語'
HTML_LANG = 'ja'
HREFLANG = 'ja'
DIR = 'ltr'
LOCALE_OG = 'ja_JP'
DECIMALE = '.'

UI = {
    'devise': 'シミュレーション仮説の研究。',
    'description_site': 'aeternam — シミュレーション仮説の研究',
    'travaux': '研究',
    'langue': '言語',
    'surtitre': '研究 · 検証1',
    'meta': '第2版 · 再現可能な二次解析',
    'verdict': '現時点での結論：調べたデータの中に、シミュレーションの痕跡は見つかっていない。',
    'fichier_pdf': 'aeternam-test-1-ja.pdf',
}

ARTICLE = {
    'titre': 'GRB 221009A で立方格子を検証する',
    'description': 'LHAASO が観測した光子は、離散的な空間の格子間隔に何を課すのか。'
                   'そして、その制約はどこで途切れるのか。',
    'date': '2026年9月28日',
    'corps': r"""
<section class="resume">
<h2>要約</h2>
<ul>
<li><strong>もし空間が立方格子で</strong>、光がマクスウェル方程式の数値シミュレーションと同じように伝わるとすれば、最もエネルギーの高い光子は遅れて届くはずである。ガンマ線バースト GRB&nbsp;221009A において、LHAASO はそのような遅れを観測していない。</li>
<li><strong>したがって、格子間隔は [[a_resume]]&nbsp;m 未満である</strong>（最も保守的な手法で、最も不利な向きをとった場合）。尤度法を用いれば [[a_ml_resume]]&nbsp;m 未満となる。格子のエネルギースケールは [[echelle_resume]]&nbsp;GeV を超える。</li>
<li><strong>これは新たな限界ではない。</strong>Beane、Davoudi、Savage は 2012 年に、宇宙線からすでに同じ桁の値（約 [[b_beane]]&nbsp;m）を得ていた。本結果は、別の観測量による独立な確認である。</li>
<li><strong>新しい点：時間刻みが効いてくる。</strong>あらゆる数値シミュレーションと同じく時間も離散化されているなら、効果は小さくなる。安定性を保てる最大の時間刻みでは、立方体の 8 つの対角線方向に沿って光はまったく分散しなくなる。そのため、バースト 1 つだけでは普遍的な上限は得られない。95% の向きについては、格子間隔は依然として [[a95_sigma1]]&nbsp;m 未満である。</li>
<li><strong>主要な誤差が <em>a</em> について線形である格子</strong>は、[[a_lineaire]]&nbsp;m、すなわちプランク長の 10 分の 1 まで排除される。</li>
<li><strong>プランク長程度の格子間隔には依然として届かない</strong>。その効果は、この検証で捉えるには約 [[facteur_planck]] 倍も弱すぎる。</li>
<li><strong>文献を確認する過程で</strong>、2025 年の論文（Xi と Shu）に換算の不整合を見つけた。彼らの二次の上限は [[xs_facteur]] 倍過大に見積もられているとみられる。</li>
<li><strong>検出はなく、私たちがシミュレーションの中にいる確率も示さない。</strong>この検証が制約するのは特定の 1 つの構成であり、シミュレーターが存在するかどうかについては何も語らない。</li>
</ul>
</section>

<h2 id="question">1. 検証する問い</h2>
<p>数値シミュレーションは、空間を有限個の点で表す。その中を伝わる波は、連続空間の場合とまったく同じようにはふるまわない。波の速さが波長にわずかに依存するのである。したがって光の場合、速さは光子のエネルギーに依存することになる。この効果はごく小さいが、宇宙論的な距離にわたって蓄積する。</p>
<p>GRB&nbsp;221009A は、これまでに記録された中で最も明るいガンマ線バーストである。LHAASO 観測所は、このバーストから 10&nbsp;TeV を超える光子を検出した。これらの光子は約 20 億年前に放たれたものである（赤方偏移 <em>z</em>&nbsp;=&nbsp;[[z]]）。光速がエネルギーに依存するなら、高エネルギーの光子は低エネルギーの光子より遅れて届く。LHAASO 共同研究グループはこの遅れを探したが、見つからなかった。</p>
<p>したがって、問いは明確である。<em>遅れがゼロであるという結果のもとで、格子間隔はどこまで許されるのか？</em> この問いは、あらゆるシミュレーションが格子を用いるとも、格子がシミュレーションを証明するとも仮定していない。</p>

<h2 id="modele">2. モデル：格子上のマクスウェル方程式</h2>
<p>電磁場を格子間隔 <em>a</em> の立方格子上に置く。これは、マクスウェル方程式の数値シミュレーションで用いられる Yee のスキーム（1966）や、格子電磁気学のハミルトン形式（Kogut と Susskind、1975）とまったく同じ扱いである。時間は連続的に流れるか、刻み \(\Delta t\) で進む。このとき、波数ベクトル \(\mathbf k\)、角振動数 \(\omega\) の平面波は次の分散関係に従う：</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>このスキームは \(c\,\Delta t\le a/\sqrt{3}\) のときに限り安定である。そこで \(c\,\Delta t=\sigma a/\sqrt{3}\) と書く。ここで \(0\le\sigma\le1\) はクーラン数であり、\(\sigma=0\) は連続時間に対応する。波長が格子間隔よりはるかに長い光子について、\(E=\hbar\omega\) とすると、群速度は次のようになる：</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) は格子の軸に対する光子の方向 \(\mathbf n\) に依存し、軸に沿った方向で \(Q=1\)、立方体の体対角線に沿った方向で \(Q=1/3\) となる。以下では次の 3 つの性質が重要である：</p>
<ul>
<li>効果は<strong>二次</strong>である。格子間隔が 10 分の 1 になれば、効果は 100 分の 1 になる。</li>
<li>スキームが安定である限り、光子は<strong>減速</strong>されるだけで、決して加速されない。</li>
<li>2 つの偏光は同じように伝わる。<strong>複屈折は生じない</strong>ため、非常に厳しい偏光による制約はここでは適用されない。</li>
</ul>

<h2 id="lhaaso">3. LHAASO との照合</h2>
<p>LHAASO は二次の遅れを \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) で表し、\(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\) に対する区間を公表している。ここで \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV である（同論文の式 2、3、5）。両者を対応させると：</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>エネルギー \(E_h\) と \(E_l\) の 2 つの光子の間に蓄積する遅れは</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>と書ける。LHAASO の宇宙論パラメータ（<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc、Ω<sub>m</sub>&nbsp;=&nbsp;[[om]]、Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]）を用いると、<em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s となる。測定が制約するのは組み合わせ \(a\sqrt{Q_{\mathrm{eff}}}\) のみである。LHAASO の表 I は、95% の信頼水準で次の値を与える：</p>
<div class="tableau"><table>
<thead><tr><th>手法</th><th>下限</th><th>最良フィット</th><th>上限</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML（較正済み）</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>ゼロは 3 つの区間すべてに含まれる。つまり、遅れは検出されていない。3 つの手法は同じバーストを解析しているので、これらを組み合わせることはしない。\(\eta_2\) の上限 \(U\) からは次が得られる：</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>連続時間の場合、次の結果を得る：</p>
<div class="tableau"><table>
<thead><tr><th>手法</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\)、最も不利な向き (m)</th><th>\(a\)、95% の向き (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML（較正済み）</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>要約では最も保守的な値 [[a_resume]]&nbsp;m を採用した。これは提示のための包絡であり、新たな区間ではない。この上限値では、1&nbsp;TeV の光子は [[e_bas]]&nbsp;TeV の光子より最大で [[retard_limite]]&nbsp;s 遅れて届く。</p>
<p>いくつかの予測値を示す。これらは測定値ではない（1&nbsp;TeV の光子と [[e_bas]]&nbsp;TeV の光子の比較）：</p>
<div class="tableau"><table>
<thead><tr><th>格子間隔</th><th>予測される \(\eta_2\)</th><th>予測される遅れ</th><th>判定</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]]～[[p26_eta_max]]</td><td>[[p26_ret_min]]～[[p26_ret_max]]&nbsp;s</td><td>すべての向きで排除</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]]～[[p27_eta_max]]</td><td>[[p27_ret_min]]～[[p27_ret_max]]&nbsp;s</td><td>軸の近く（\(Q>\)&nbsp;[[q_cal_axe]]）で、較正済みの手法によってのみ排除</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]]～[[p28_eta_max]]</td><td>[[p28_ret_min]]～[[p28_ret_max]]&nbsp;ms</td><td>排除されない</td></tr>
<tr><td>[[lpl]]&nbsp;m（プランク長）</td><td>[[pl_eta_min]]～[[pl_eta_max]]</td><td>[[pl_ret_min]]～[[pl_ret_max]]&nbsp;s</td><td>到達不能</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. 上限はどこまで持ちこたえるか</h2>
<h3>格子の向き</h3>
<p>バーストの方向に対して格子がどう向いているかはわからない。主要な上限は、最も不利な場合 \(Q=1/3\) を採用している。一様に分布させた 100 万の方向について、\(Q\) の中央値は [[q_mediane]] であり、95% の場合に [[q_5]] を超える。上限の変化は小さく、95% の向きでは [[ccf_95]]&nbsp;m、中央値の向きでは [[ccf_mediane]]&nbsp;m となる。これらの割合は幾何学的なものであり、宇宙についての確率ではない。</p>
<h3>離散時間：上限の弱点</h3>
<p>シミュレーションは時間刻みごとに進む。時間を離散化すると逆符号の誤差が生じ、空間の離散化による誤差を部分的に打ち消す（\(-\sigma^{2}/3\) の項）。保守的な手法の場合：</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>最も不利な向き</th><th>95% の向き</th><th>中央値の向き</th></tr></thead>
<tbody>
<tr><td>0（連続時間）</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1（最大の刻み）</td><td>[[s4_cdt]]</td><td>上限なし</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>安定性を保てる最大の刻みでは、体対角線に沿った打ち消しは厳密であり、一次の近似に限った話ではない。その方向では、分散関係があらゆる波長に対して \(\omega=ck\) を与える。このように設定されたシミュレーションは、バーストが 8 つの対角線方向のいずれかに重なっていれば、この検証を完全にすり抜ける。これが単一の天体から得られる上限の主な限界である。異なる方向にある複数の天体を用いれば、この限界は取り除ける。偶然でない限り、それらがすべて対角線に揃うことはないからである。</p>
<h3>固定された格子間隔か、膨張で引き伸ばされる格子間隔か</h3>
<p>ここでは物理的な格子間隔が固定されていると仮定している。格子が宇宙とともに引き伸ばされる（共動格子間隔の）場合、効果は赤方偏移とともに増大しなくなり、\(I_2\) は \(I_0\) に置き換わる。上限は \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]] 倍だけ弱まり、[[comobile_a]]&nbsp;m となる。<em>z</em>&nbsp;=&nbsp;[[z]] では、この選択の影響は小さい。</p>
<h3>より高精度なスキーム</h3>
<p>シミュレーターは、主要な誤差が \(a^{4}\) に比例する高次のスキームを用いるかもしれない。その場合、効果はエネルギーの 4 乗に比例し、\(a\) に対する上限ははるかに弱くなる。LHAASO はこのバーストについてこの種の制約を公表していない。それを定量化するには光子ごとのデータが必要である。分散を打ち消すように設計された項も、この上限をすり抜ける。これらは別のモデルであり、個別に検証すべきものである。</p>
<h3>誤差が線形だったら？</h3>
<p>対称な格子は、\(a\) について線形な効果を生じない。2 つの逆向きの伝播方向の間の対称性を破ることで線形な効果を生む離散化があれば、LHAASO の線形の上限 \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\) の対象となる。係数が 1 程度なら \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m、すなわちプランク長の 10 分の 1 である。これより粗いこの種の格子はすべて排除される。</p>
<h3>計算の妥当性</h3>
<p>展開は \(aE/\hbar c\ll1\) を仮定している。上限値では、20&nbsp;TeV の光子でさえ \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]] である。展開式を厳密な分散関係とも比較した。\(ak\)&nbsp;=&nbsp;[[ak_test]] のとき、相対誤差は予想どおり [[ecart_dispersion]] を超えない。</p>

<h2 id="contexte">5. 既存の結果と比べた意義</h2>
<p>Beane、Davoudi、Savage（2012）は、格子量子色力学のシミュレーションを検討した。彼らは宇宙線スペクトルのカットオフから、格子間隔の逆数に \(1/b\gtrsim10^{11}\)&nbsp;GeV、すなわち \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m という制約を与えた。我々の保守的な上限は彼らの値の [[beane_ratio]] 倍であり、LHAASO の尤度法では [[beane_ml_min]]～[[beane_ml_max]] 倍となる。したがって 2 つのアプローチは、観測量も粒子も仮定も異なるにもかかわらず、桁のレベルで一致する。これは確認であって、記録の更新ではない。</p>
<p>プランク長 [[lpl]]&nbsp;m は、さらに 8 桁小さい。この大きさの格子間隔では、効果は上限の [[facteur_planck_exact]] 分の 1 にすぎない。効果はエネルギーの 2 乗に比例して増大するので、約 1 億倍エネルギーの高い光子が必要となり、これはこれまでに観測されたあらゆるものをはるかに超える。この次数では、いかなる飛行時間の検証もプランクスケールの格子には届かない。</p>

<h2 id="xi-shu">6. 文献の検証：Xi と Shu（2025）</h2>
<p>Xi と Shu は別の手法で同じバーストを解析し、\(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV（彼らの表 III）を報告している。これは LHAASO の上限の約 [[xs_rapport_lhaaso]] 倍である。彼ら自身の定義から出発しても、我々はこの値を再現できない。</p>
<ul>
<li>彼らの式 (3) は、遅れが \((E/E_{\mathrm{QG},n})^{n}\) に比例すると定めている。\(n=1\) については、彼らの換算式 (6) \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\)（\(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]]）は整合的であり、我々の計算でも [[xs_c1]] となる。</li>
<li>\(n=2\) については、彼らの式 (7) \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\)（\(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]]）は \(1/\theta\) の形を保っている。これを彼らの上限 \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV² に適用すると、確かに彼らの表の値（[[xs_eq7]]&nbsp;GeV）が再現される。しかし遅れは二次であるため、彼らの式 (3) からは \(1/\sqrt{\theta_2}\) の依存性が導かれる。すなわち \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\)、つまり \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV となる。</li>
<li>両者の差は [[xs_facteur]] 倍である。考えられる説明：\(\varepsilon^{2}\theta_2\) は [[xs_eps2]] であり、[[xs_c2_imprime]] は、[[xs_eps2_imprime]] の平方根を 10 のべき乗の部分だけについて取ったもののように見える。</li>
</ul>
<p>現状：論文の第 1 版にみられる見かけ上の不整合であり、著者への確認が必要である。我々は彼らのデータを再解析しておらず、他の結果についても評価しない。修正しても、彼らの上限は LHAASO のものより [[xs_vs_lhaaso]] 倍強いままである。我々はこの上限を用いない。</p>

<h2 id="limites">7. この検証が語らないこと</h2>
<ul>
<li>何も検出していない。遅れがゼロであることは、すべての測定と矛盾しない。</li>
<li>私たちがシミュレーションの中にいる確率は一切計算していない。「95%」は物理パラメータについての値である。</li>
<li>制約するのは特定の構成、すなわち立方格子、Yee のスキーム、固定された格子間隔、補償なしという構成である。</li>
<li>遅れが検出されたとしても、それがコンピューターを指し示すわけではない。根本的に離散的な物理や、量子重力の他の効果も同じ信号を生じうる。</li>
<li>LHAASO の区間は、天体での放射に関する仮定に基づいている。我々もそれを引き継いでいる。</li>
</ul>

<h2 id="suite">8. 今後の課題</h2>
<ol>
<li>異なる方向に見える複数の天体を組み合わせ、対角線方向の死角をなくす。</li>
<li>高次のスキーム（\(a^{4}\) の効果）を定量化する。これには光子ごとのデータが必要である。</li>
<li>Xi と Shu に換算についての説明を求める。</li>
<li>格子の他の兆候、すなわち宇宙線の異方性や荷電粒子にも検証を広げる。</li>
</ol>

<h2 id="reproduire">9. 再現する</h2>
<p>すべての値は、外部ライブラリに依存しない Python スクリプトで再計算される。スクリプトはまず自らの式を検証する：展開と厳密な分散関係の比較、対角線上での厳密な結果、往復の換算、宇宙論的積分、そして \(Q\) の平均が 3/5 に等しいこと。</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>：スクリプト（Python&nbsp;3.10 以降、標準ライブラリのみ。コード中のコメントはフランス語）</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>：計算したすべての値</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>：本ノートの PDF 版</li>
</ul>
<p>独立したクロスチェック（numpy、scipy）により、宇宙論的積分が 10<sup>−15</sup> の精度で、向きの分位点が 1000 万回の乱数抽出で、群速度が分散関係の数値解で、それぞれ再現された。</p>
<p>本ノートは 2026 年 9 月 28 日付の初版に代わるものである。離散時間、向き、共動格子間隔、線形効果、Beane らとの比較を追加した。</p>

<h2 id="sources">出典</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>（2026年2月13日改訂版）：式 2、3、5、表 I。</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>（2012）。</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a>（2025）：式 3、6、7、表 I および表 III。</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302（1966）。</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395（1975）。</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House：数値分散と Yee のスキームの安定性。</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>：基礎物理定数。</li>
</ol>
""",
}

ARTICLE_2 = {
    'titre': '宇宙線は格子を描き出しているか？',
    'description': 'ピエール・オージェ観測所がこれまでに記録した最もエネルギーの高い粒子を、'
                   '立方格子が残すはずの痕跡と照らし合わせる。',
    'date': '2026年9月28日',
    'corps': r"""
<section class="verdict-net">
<h2>判定</h2>
<p><strong>否。</strong>ピエール・オージェ観測所が測定した最もエネルギーの高い [[n_evt]] 個の宇宙線には、立方体の対称性はまったく見られない。格子がまったく存在しない空でも、観測されたものと少なくとも同程度にはっきりした模様が [[p4_pct]]% の場合に現れる。見えているのは、ありふれた偶然にすぎない。</p>
<p>この「否」が及ぶ範囲は限られている。粒子が [[n_evt]] 個では、非常にはっきりした模様しか現れようがなかった。より控えめな模様が存在する可能性は残る。</p>
</section>

<h2 id="explication">解説</h2>
<p>もし私たちの世界がコンピューターで計算されているとしたら、画像がピクセルでできているように、空間もごく小さな立方体に区切られているかもしれない。2012 年、3 人の物理学者が、そのような区切りは痕跡を残すはずだと指摘した。宇宙で最も速い粒子が、あらゆる方向から同じようにはやって来なくなるというのである。いくつかの方向が選ばれやすくなり、それらは立方体の面や角のように並ぶはずだという。</p>
<p>そうした粒子は実在する。宇宙線、つまり宇宙からやって来る原子核であり、私たちの加速器が生み出すどんなものよりもはるかに大きなエネルギーを持つ。アルゼンチンでは、ピエール・オージェ観測所が巨大な検出器網でそれを待ち受けている。観測所は、2004 年から 2020 年までにとらえた最もエネルギーの高い [[n_evt]] 個の一覧を、それぞれがやって来た方向とともに公開した。</p>
<p>私たちはこの [[n_evt]] 個の方向を取り出し、それらが立方体に沿って並んでいるかどうかを調べた。その立方体がどう傾いているかは誰にもわからないため、[[n_orient]] 通りの向きを試した。最もよい向きは、データにわずかに合っていた。しかし、これほど多くの向きを試せば、まったくの偶然でできた空でも、わずかに合う向きは必ず見つかる。</p>
<p>判断を下すため、同じ観測所から見た偽の空を無作為に [[n_ciels]] 個作り、それぞれにまったく同じ探索を行った。そのうち [[p4_pct]]% で、少なくとも同じくらいよく合う立方体が見つかる。したがって、本物の空に特別なところは何もない。手がかりと呼べるためには、ほとんどすべての偽の空よりもよく合っている必要があった。</p>
<p>結論：格子の痕跡はない。ただし、この探索で見えるのははっきりした模様だけであった。粒子が [[n_evt]] 個しかないため、控えめな模様なら見逃される。さらに、私たちの銀河の磁場がこれらの粒子の進路を途中で曲げるので、模様の一部はぼやけてしまうだろう。したがって、この検証は空間が連続であることを証明するものではない。調べることのできた範囲には何もなかった、ということを示すものである。</p>

<h2 id="analyse">詳細な分析</h2>

<h3>1. 格子から検証可能な予言へ</h3>
<p>格子間隔 \(a\) の立方格子上では、離散ラプラシアンが \(k^{2}\) を \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\) で置き換える。自由場に対しては</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>となる。ここで \(\mathbf n\) は格子の軸で表した伝播方向である。これは検証1と同じ関数 \(Q\) である。より一般に、到来方向に対する格子のあらゆる効果（伝播、方向に依存するスペクトルのカットオフ）は、立方体群 \(O_h\) のもとで不変な \(\mathbf n\) の関数である。ところが \(O_h\) 不変な球面調和関数は \(\ell=0,4,6,8,\dots\) にしか存在しない。許される最初の異方性は立方調和関数 \(\ell=4\) であり、\(Q-3/5\) に比例する。これがデータを開く前に定めた主検定であり、\(\ell=6\) は 2 番目に検定する。Beane、Davoudi、Savage は、シミュレーションは「最高エネルギー宇宙線の分布において、背後にある格子の構造を反映した、ある程度の回転対称性の破れとして現れうる」と書いている。</p>

<h3>2. データ</h3>
<p>ピエール・オージェ観測所のカタログ（ApJS 264, 50, 2023）：2004 年 1 月 1 日から 2020 年 12 月 31 日までに記録された最高エネルギーの空気シャワー [[n_evt]] 個で、エネルギーは [[e_min]]～[[e_max]]&nbsp;EeV、天頂角は最大 [[zmax]]° である。公開ファイルには、この [[n_evt]] 個とは別に、較正用のハイブリッド事象 [[n_calib]] 個も含まれているが、これらは除外する。地表検出器で再構成された赤経と赤緯を用いる。ファイルの SHA-256 ハッシュは実行のたびに照合する。これらのエネルギーでは天頂角 [[zmax]]° まで検出効率が完全であるため、露出は純粋に幾何学的に決まる。</p>

<h3>3. 検出器の露出</h3>
<p>緯度 \(a_0\)&nbsp;=&nbsp;[[lat]]° にあり、天頂角 \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]° を受け入れる地上検出器の露出は、赤経については一様で、赤緯 \(\delta\) については次のようになる（Sommers、2001）：</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>見える空は \(\delta\)&nbsp;=&nbsp;[[dec_max]]° までで、天球の [[ciel_pct]]% にあたる。したがって、オージェ観測所から見た等方的な空は一様ではない。以下ではすべて、データを一様な球面ではなく、この空と比較する。</p>

<h3>4. 統計量</h3>
<p>\(R\) を格子の向きとし、その行を \(\mathbf e_k\)、\(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\) とする。観測された \(N\) 個の方向について：</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>ここで \(\langle\cdot\rangle_\omega\) は、露出で重み付けした等方的な空での平均である。\(T>0\) は立方体の軸に沿った超過を、\(T<0\) は対角線に沿った超過を示し、絶対値をとることで両方を扱う。\(f\) は 4 次の多項式なので、\(T(R)\) がデータに依存するのは 15 個のモーメント \(\sum_i\mathbf n_i^{\alpha}\) を通じてのみである。平均と分散はガウス・ルジャンドル求積で厳密に計算する。最大値は、一様に（ハール測度に従って）抽出した [[n_orient]] 個の向きについてとる。\(\ell=6\) については \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\) とし、\(\alpha\)&nbsp;=&nbsp;[[alpha6]]（すなわち \(-15/11\)）とすることで \(\ell=4\) と直交させる。組み合わせ検定では \(T_4^{2}+T_6^{2}\) を最大化する。</p>

<h3>5. 偶然の較正</h3>
<p>[[n_orient]] 個の向きから最良のものを探すと、\(Z_4\) は機械的に大きくなり、正規分布には従わない。そこで、露出に従って \(N\) 個の事象からなる等方的な空を [[n_ciels]] 個生成し、それらにまったく同じ最大化を適用する。「格子なし」の仮説のもとで、\(Z_4\) の中央値は [[z4_50]] であり、5% の場合に [[z4_95]]、1% の場合に [[z4_99]]、0.1% の場合に [[z4_999]] を超える。こうして p 値 \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\) には、向きを選ぶことの代償が含まれる。</p>

<h3>6. 結果</h3>
<div class="tableau"><table>
<thead><tr><th>検定</th><th>観測された統計量</th><th>p 値</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\)（主検定）</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\) と \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>最良の向きにおいて、\(Q\) の平均は [[q_obs]] で、期待値 [[q_iso]] に対して軸方向へ [[q_ecart_pct]]% の超過となる。これは有意ではない。主検定で \(p\)&nbsp;=&nbsp;[[p4]] であり、どの副次的な検定も 0.05 を下回らない。データは、立方対称性がまったく存在しないことと矛盾しない。</p>

<h3>7. この検定で見えたはずのもの</h3>
<p>感度を定量化するため、立方対称な模様を注入する。密度を \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\) に比例させる。\(\varepsilon>0\) では軸方向のフラックスが平均の \(1+\varepsilon\) 倍となり、\(\varepsilon<0\) では超過は対角線方向に移る。各 \(\varepsilon\) について、向きをランダムにした [[n_ciels_signal]] 個の空から \(Z_4\) の分布を得る。95% 上限は、軸方向で \(\varepsilon\le\)&nbsp;[[eps_axes]]、対角線方向で \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]] である。言い換えれば、軸方向に約 [[eps_axes_pct]]%（あるいは対角線方向に [[eps_diag_pct]]%）までの超過は排除されない。事象数が少ないことによる、弱い制約である。</p>
<p>スクリプトはまず、自らの処理の連鎖を検証する：立方体群のもとでの \(Q\) の不変性、多項式展開の厳密性、赤緯 [[dec_max]]° を超える領域での露出ゼロ、等方性のもとで \(T\) が平均 0・分散 1 に標準化されていること、\(\ell=6\) と \(\ell=4\) の直交性、そして注入したはっきりした模様の検出（その向きは [[ecart_orient]]° 以内の精度で復元される）。</p>

<h3>8. 限界</h3>
<ul>
<li>宇宙線は電荷を帯びている。銀河系および銀河系外の磁場がその方向を曲げ、原子核が重いほど曲がりは大きい。探している模様は大きなスケールのもの（軸と対角線は [[angle_diag]]° 離れている）で、ほどほどの偏向には耐えるが、発生源や伝播の途中で刻まれた痕跡は部分的に消されてしまう。</li>
<li>格子は遠方の恒星に対して固定されている（赤道座標）と仮定している。それらに対して運動または回転している格子には、別の検定が必要となる。</li>
<li>[[n_evt]] 個の事象と空の [[ciel_pct]]%：上の上限が示すとおり、統計的検出力は低い。</li>
<li>実際の天体物理的な異方性が \(\ell=4\) 成分を含むこともありうる。陽性の結果であればそれらを除外する必要があったが、ゼロの結果はそれらに左右されない。</li>
<li>シミュレーションの中にいる確率は計算していない。この検定が対象とするのは、立方格子という特定の兆候である。</li>
</ul>

<h3>9. 再現する</h3>
<p>Python スクリプト（numpy）が約 1 分ですべてをやり直す：データの読み込みと検査、自己テスト、統計量、シミュレーションした空、上限。乱数生成器のシードは固定されており、実行のたびに同じ結果が得られる。</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-2/analyse.py" download>analyse.py</a>：スクリプト</li>
<li><a href="/fichiers/test-2/resultats.json" download>resultats.json</a>：計算したすべての値</li>
<li><a href="/fichiers/test-2/donnees/auger_catalogSD.csv" download>auger_catalogSD.csv</a>：ピエール・オージェ観測所のデータ（CC BY-SA 4.0 ライセンス）</li>
</ul>

<h2 id="sources">出典</h2>
<ol class="sources">
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>（2012）。</li>
<li>Pierre Auger Collaboration, <cite>A Catalog of the Highest-Energy Cosmic Rays Recorded During Phase I of Operation of the Pierre Auger Observatory</cite>, ApJS 264, 50（2023）、<a href="https://arxiv.org/abs/2211.16020">arXiv:2211.16020</a>。</li>
<li>Pierre Auger Collaboration, <cite>Auger Open Data</cite>、リリース 3、<a href="https://doi.org/10.5281/zenodo.10488964">DOI 10.5281/zenodo.10488964</a>。検出効率：<a href="https://opendata.auger.org/data.php">opendata.auger.org</a>。</li>
<li>P. Sommers, <cite>Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory</cite>, Astroparticle Physics 14, 271（2001）、<a href="https://arxiv.org/abs/astro-ph/0004016">arXiv:astro-ph/0004016</a>。</li>
</ol>
""",
}

ARTICLE_3 = {
    'titre': '光は特定の方向で遅くなるのか？',
    'description': '空に散らばる 8 つのガンマ線源を組み合わせて検証1の死角を埋め、'
                   '向きによらず立方格子の格子間隔に上限を与える。',
    'date': '2026年9月28日',
    'corps': r"""
<section class="verdict-net">
<h2>判定</h2>
<p><strong>否。</strong>調べた [[n_src]] 個の天体のいずれにも、格子が生むはずの遅れは見られない。それらの方向を組み合わせると、向きがどうであれ、時間刻みがどうであれ、格子間隔が [[a_exclue]]&nbsp;m 以上の立方格子は排除される。検証1の死角は閉じられた。</p>
</section>

<h2 id="explication">解説</h2>
<p>画像がピクセルでできているように、宇宙が格子の上で計算されているとすれば、光はあらゆる方向にまったく同じ速さで進むわけではなくなる。最もエネルギーの高い光はごくわずかに遅れ、その遅れは格子の対角線に沿った方向よりも、辺に沿った方向で大きい。何十億年もの旅を経れば、この遅れは測定可能になる。</p>
<p>検証1では、これまでに観測された中で最も明るいガンマ線バーストでこの遅れを探したが、何も見つからなかった。しかし抜け穴が残っていた。シミュレーションが可能な限り大きな時間刻みで進むなら、格子の対角線に沿った光はまったく遅れなくなる。そのため、対角線上にある天体 1 つだけでは何の結論も出せなかった。</p>
<p>ここでは、空の異なる方向にある [[n_src]] 個の天体を同時に見る。遠方の恒星の爆発が 3 つ、非常に活発なブラックホールを中心に持つ銀河が 4 つ、そしてかに星雲のパルサーである。いずれについても、天文学者のチームが、ある精度までは遅れが現れないことをすでに測定している。私たちは各論文を読み直し、すべての結果を同じ約束事にそろえたうえで、隠れた格子にとって最も有利な格子の向き、つまり制限を最も弱める向きを探した。</p>
<p>すべての天体を同時に対角線上に置くことはできない。最も有利な向きでも、3 つの天体は対角線から十分に離れており、遅れが現れていなければならなかった。したがって、ます目の大きさが [[a_exclue]]&nbsp;m 以上の格子は、あらゆる向きで排除される。この大きさはなおプランク長の約 [[planck_x]] 倍であり、はるかに細かい格子は依然として十分にありうる。</p>

<h2 id="analyse">詳細な分析</h2>

<h3>1. モデル</h3>
<p>検証1と同じく、格子間隔 \(a\) の立方格子上のマクスウェル方程式（Yee のスキーム）を考え、時間刻みを \(c\,\Delta t=\sigma a/\sqrt{3}\)、\(0\le\sigma\le1\) とする。主要次数では</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\,Q_{\mathrm{eff}}\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3},\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>\(1/3\le Q\le1\) なので \(Q_{\mathrm{eff}}\ge0\) である。光子は常に減速され、\(\sigma=1\) のとき体対角線上でちょうど \(Q_{\mathrm{eff}}=0\) となる。最終的な上限において、20&nbsp;TeV の光子に対し \(aE/\hbar c\)&nbsp;=&nbsp;[[ae]] であり、展開は妥当である。</p>

<h3>2. 公表された制限から格子間隔の上限へ</h3>
<p>8 本の論文はいずれも二次の遅れを \(v/c\simeq1-\tfrac{3}{2}(E/E_{\mathrm{QG},2})^{2}\) で表し、Jacob と Piran の距離 \(K_2=\int_0^{z}(1+z')^{2}\,dz'/H(z')\) を用いている。両者を対応させると、</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}}\quad\Longrightarrow\quad a\sqrt{Q_{\mathrm{eff}}(\mathbf n_i)}\le B_i=\frac{\sqrt{12}\,\hbar c}{E_i}.$$
<p>事前に定めた規則：95% の制限、光速より遅い場合、飛行時間、各論文で最も制約の弱い手法。各制限は \(E_i\sqrt{K_2^{\mathrm{LHAASO}}(z_i)/K_2^{(i)}(z_i)}\) によって LHAASO の宇宙論パラメータに換算する。この係数は [[fc_max]] を超えない。公表された換算はすべて、印刷されたパラメータから計算し直し、論文の値を再現している（自己テスト）。</p>
<div class="tableau"><table>
<thead><tr><th>天体</th><th>観測装置</th><th>\(z\) または距離</th><th>公表された \(E_{\mathrm{QG},2}\) (GeV)</th><th>共通の宇宙論 (GeV)</th><th>\(B_i\) (m)</th></tr></thead>
<tbody>
<tr><td>GRB 221009A</td><td>LHAASO</td><td>[[s0_z]]</td><td>[[s0_pub]]</td><td>[[s0_com]]</td><td>[[s0_b]]</td></tr>
<tr><td>GRB 190114C</td><td>MAGIC</td><td>[[s1_z]]</td><td>[[s1_pub]]</td><td>[[s1_com]]</td><td>[[s1_b]]</td></tr>
<tr><td>GRB 090510</td><td>Fermi-LAT</td><td>[[s2_z]]</td><td>[[s2_pub]]</td><td>[[s2_com]]</td><td>[[s2_b]]</td></tr>
<tr><td>Mrk 501</td><td>H.E.S.S.</td><td>[[s3_z]]</td><td>[[s3_pub]]</td><td>[[s3_com]]</td><td>[[s3_b]]</td></tr>
<tr><td>Mrk 421</td><td>MAGIC</td><td>[[s4_z]]</td><td>[[s4_pub]]</td><td>[[s4_com]]</td><td>[[s4_b]]</td></tr>
<tr><td>PKS 2155-304</td><td>H.E.S.S.</td><td>[[s5_z]]</td><td>[[s5_pub]]</td><td>[[s5_com]]</td><td>[[s5_b]]</td></tr>
<tr><td>PG 1553+113</td><td>H.E.S.S.</td><td>[[s6_z]]</td><td>[[s6_pub]]</td><td>[[s6_com]]</td><td>[[s6_b]]</td></tr>
<tr><td>かに星雲（パルサー）</td><td>MAGIC</td><td>[[s7_z]]&nbsp;kpc</td><td>[[s7_pub]]</td><td>[[s7_com]]</td><td>[[s7_b]]</td></tr>
</tbody>
</table></div>

<h3>3. 最も不利な向き</h3>
<p>格子の向き \(R\) に対し、天体は全体として次の上限を与える。</p>
$$a\le A(R)=\min_i\frac{B_i}{\sqrt{Q_{\mathrm{eff}}(R\mathbf n_i)}},$$
<p>ここで、\(\sigma=1\) で対角線上にある天体は何も制約しない。\(\max_R A(R)\) を求めるため、一様に抽出した [[n_orient]] 個の回転と、構成した向き（各天体を対角線上に置き、その対角線の周りに回転させたもの）を調べ、さらに局所的な精密化を行う。独立な第 2 のシードでも、相対差 [[ecart_graines]] で同じ最大値が得られる。最適化の手順は既知の場合で検証済みである。単独の天体は \(\sigma=1\) で何も制約せず、2 本の対角線のなす角だけ離れた 2 つの天体は、同時に対角線上に置くことができる。</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>最も不利な向き (m)</th><th>95% の向き (m)</th></tr></thead>
<tbody>
<tr><td>0</td><td>[[pire0]]</td><td>[[q95_0]]</td></tr>
<tr><td>0.5</td><td>[[pire05]]</td><td>[[q95_05]]</td></tr>
<tr><td>0.9</td><td>[[pire09]]</td><td>[[q95_09]]</td></tr>
<tr><td>1</td><td>[[pire1]]</td><td>[[q95_1]]</td></tr>
</tbody>
</table></div>
<p>\(\sigma<1\) では検証1から何も変わらない。GRB&nbsp;221009A が支配的であり、他の天体の感度は [[x_min]]～[[x_max]] 倍低い。すべては \(\sigma=1\) で決まる。GRB&nbsp;221009A を対角線上に置くだけではもはや足りない。そうすると、他の天体が格子を斜めから見ることになるからである。最も不利な妥協点では、GRB&nbsp;221009A は最も近い対角線から [[ang_grb]]° 離れ（\(Q_{\mathrm{eff}}\)&nbsp;=&nbsp;[[qeff_grb]]）、[[n_actives]] 個の制約、すなわち GRB&nbsp;221009A、GRB&nbsp;090510、かに星雲がつり合う。このとき上限は [[pire1]]&nbsp;m、すなわちエネルギースケール \(\hbar c/a\ge\)&nbsp;[[echelle]]&nbsp;GeV となる。\(A(R)\) はどの向きでも \(\sigma\) とともに増大するので、この上限はすべての \(\sigma\le1\) で成り立つ。\(\sigma=1\) での向きの中央値は [[med1]]&nbsp;m である。</p>
<p>死角が閉じることは自明ではなかった。GRB&nbsp;190114C と GRB&nbsp;090510 は [[ang_190_090]]° 離れており、これは 2 本の対角線のなす角（[[ang_diag]]°）にほぼ等しい。また、GRB&nbsp;090510 と PKS&nbsp;2155-304 は互いに [[ang_090_pks]]° しか離れていない。死角を閉じるのは、空の残りの部分に散らばる天体の多様性である。</p>

<h3>4. 頑健性</h3>
<p>\(\sigma=1\) における最も不利な向きの上限は、選択によって次のように変わる：</p>
<ul>
<li>GRB&nbsp;221009A を除いた場合：[[v_sans_lhaaso]]&nbsp;m。死角は閉じたままである。</li>
<li>宇宙論の換算をせずに公表値を用いた場合：[[v_sans_cosmo]]&nbsp;m</li>
<li>Fermi について天体固有の効果を含めた場合（論文の表 V）：[[v_fermi]]&nbsp;m</li>
<li>ガンマ線バーストのみ：[[v_sursauts]]&nbsp;m</li>
<li>ブレーザーとパルサーのみ：[[v_blazars]]&nbsp;m</li>
</ul>

<h3>5. 比較</h3>
<p>あらゆる向きとあらゆる時間刻みで成り立つ上限は、連続時間での検証1の上限より [[x_test1]] 倍弱い。Beane、Davoudi、Savage は宇宙線スペクトルのカットオフから \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m を得た。我々の連続時間での上限は彼らの値の [[x_beane0]] 倍、普遍的な上限は [[x_beane]] 倍である。</p>

<h3>6. 限界</h3>
<ul>
<li>組み合わせた上限は、向きごとに、個別に公表された 95% の制限のうち最も厳しいものをとっている。これは組み合わせた尤度ではなく、論文もそれを公表していない。最も不利な向きでは 3 つの制限が効いているため、保証される被覆率は 95% ではなく、少なくとも [[couverture]]% である。</li>
<li>各論文は、天体固有の時間のずれが遅れを打ち消したり模倣したりしないと仮定している。</li>
<li>Mrk&nbsp;421 と PG&nbsp;1553+113 の赤方偏移は不確かだが、この 2 天体は最も不利な向きでは効いていない。効いているかに星雲の距離は、MAGIC の不確かさに含まれている。</li>
<li>高次のスキーム（\(a^{4}\) の誤差）、補償項、立方でない格子や膨張で引き伸ばされる格子は、この上限の対象外である。</li>
<li>二次解析であり、光子の再解析は行っていない。向きの割合は幾何学的なものであり、宇宙についての確率ではない。</li>
</ul>

<h3>7. 再現する</h3>
<p>スクリプトは数秒ですべてをやり直し、まず自らの式と公表された各換算を検証する。入力値はすべて、ページと表を明記して <code>sources.md</code> に出典を示している。</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-3/analyse.py" download>analyse.py</a>：スクリプト</li>
<li><a href="/fichiers/test-3/resultats.json" download>resultats.json</a>：計算したすべての値</li>
<li><a href="/fichiers/test-3/sources.md" download>sources.md</a>：各入力値の出典</li>
</ul>

<h2 id="sources">出典</h2>
<ol class="sources">
<li>LHAASO Collaboration, GRB 221009A, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>、表 I。</li>
<li>MAGIC Collaboration, GRB 190114C, <a href="https://arxiv.org/abs/2001.09728v4">arXiv:2001.09728v4</a>、表 I。</li>
<li>Fermi-LAT Collaboration, GRB 090510, <a href="https://arxiv.org/abs/1305.3463v1">arXiv:1305.3463v1</a>、表 IV および表 V。</li>
<li>H.E.S.S. Collaboration, Mrk 501, <a href="https://arxiv.org/abs/1901.05209v1">arXiv:1901.05209v1</a>。</li>
<li>MAGIC Collaboration, Mrk 421, <a href="https://arxiv.org/abs/2406.07140v1">arXiv:2406.07140v1</a>、表 2。</li>
<li>H.E.S.S. Collaboration, PKS 2155-304, <a href="https://arxiv.org/abs/1101.3650v2">arXiv:1101.3650v2</a>。</li>
<li>H.E.S.S. Collaboration, PG 1553+113, <a href="https://arxiv.org/abs/1501.05087v1">arXiv:1501.05087v1</a>、表 5。</li>
<li>MAGIC Collaboration、かに星雲パルサー、<a href="https://arxiv.org/abs/1709.00346v1">arXiv:1709.00346v1</a>、表 6。</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>。</li>
<li>座標：<a href="https://simbad.cds.unistra.fr/simbad/">SIMBAD</a>（CDS、ストラスブール）。</li>
</ol>
""",
}

ARTICLE_4 = {
    'titre': '量子のランダムさはプログラムの存在を露呈するか？',
    'description': '量子実験から得た数百万ビットを、シミュレーションが使うであろう'
                   '擬似乱数生成器を見破るための検定にかける。',
    'date': '2026年9月28日',
    'corps': r"""
<section class="verdict-net">
<h2>判定</h2>
<p><strong>否。</strong>検定した量子由来の生のビットには、擬似乱数生成器の痕跡はまったく現れない。一方、同じ検定は、対照として用いた 4 つの単純な生成器を見破る。最初に述べておくべき点がある。解析前に定めた規則は、公開されたままの IBM のデータに対しては反応する。しかし原因は特定されている。9 台のマシンのうち 1 台が、いくつもの測定系列のあいだ、ずっと 0 または 1 に張り付いたままになっていたのであり、この欠陥は生成器の構造を持たない。このマシンを除外することは、データを見た後で決めた。そのことをここに明記しておく。</p>
<p>この「否」が及ぶ範囲は限られている。これが排除するのは、量子測定の結果を単純な生成器から引き出すシミュレーションであって、暗号学的な品質の生成器を用いるシミュレーションではない。そのような生成器は、原理的に真の乱数と見分けがつかない。</p>
</section>

<h2 id="explication">解説</h2>
<p>もし世界がシミュレーションなら、量子測定のたびに、その結果である 0 か 1 かを生み出さなければならない。物理学によれば、この結果は本質的に予測できない。ところがコンピューターは本物の偶然をつくることができず、計算の手順、いわばレシピによって偶然をこしらえる。計算を節約したいシミュレーションなら、速くて単純なレシピを使うだろう。そして単純なレシピは痕跡を残す。繰り返し、隠れた規則性、計算によって見つけ出せる構造である。</p>
<p>そこで私たちは、実際の量子実験で得られ、研究者自身が公開した 0 と 1 の列を取り上げ、その中にこうした痕跡を探した。最初の難点がある。公開されている量子乱数の源の多くは、結果を公開する前に数学的な「ミキサー」に通している。このミキサーはあらゆる構造を消すように設計されているので、その出力を調べても、もとの源については何もわからない。私たちはこれらのデータも検定したが、判定には数えていない。</p>
<p>残るのは生の源 2 つである。1 つは米国オレゴン州のポートランド大学にある、もつれた光子を用いる装置で、ビットをそのまま公開している。もう 1 つは IBM の 9 台の量子コンピューターで、たった 1 個の量子ビットでコイン投げをするよう、何百万回も指示されたものである。光子はすべての検定に合格する。IBM のマシンは 0 がわずかに多すぎるが、これはデータの作成者が説明している既知の欠陥であり、この偏りを補正すれば合格する。そのうちの 1 台、Belem は、いくつもの測定系列のあいだ、ずっと固まったままだった。これは故障であって、計算のレシピではない。</p>
<p>比較用の生成器は予想どおりにふるまう。単純なレシピは見破られる。その中には、NIST の公式の検定群には合格してしまう、非常に広く使われている生成器も含まれる。一方、精巧なレシピは見破られない。2 の平方根の数字の並びも見破られないが、これは完全に計算できるものである。ここにこの検証の限界がある。入念に作られたシミュレーションなら、この種の痕跡を何も残さないだろう。</p>

<h2 id="analyse">詳細な分析</h2>

<h3>1. 何が検定できるか</h3>
<p>統計的検定からわかるのは、ビット列が最後に受けた処理についてだけである。暗号学的関数でハッシュ処理された出力は、入力が何であれ完全な乱数のように見える。私たちは合計 [[bits_total]] ビットを検定した。そのうち生のビットは [[bits_bruts]] ビットである：</p>
<div class="tableau"><table>
<thead><tr><th>データセット</th><th>由来</th><th>処理</th><th>ビット数</th></tr></thead>
<tbody>
<tr><td>parity</td><td>偏光もつれ光子（Kavulich ら、2021）</td><td>なし</td><td>[[n_parity]]</td></tr>
<tr><td>ibm</td><td>量子ビット 1 個、アダマールゲート、測定。9 台のマシン（Root と Becker、2024）</td><td>なし</td><td>[[n_ibm]]</td></tr>
<tr><td>anu</td><td>真空ゆらぎ、ANU</td><td>AES-128</td><td>[[n_anu]]</td></tr>
<tr><td>beacon</td><td>NIST Beacon 2.0</td><td>SHA-512</td><td>[[n_beacon]]</td></tr>
</tbody>
</table></div>
<p>量子のランダムさの本質について手がかりを与えるのは、parity と ibm だけである。NIST が 2015 年に行った抜け穴のないベルテストの生データは採用しなかった。その測定設定の選択は物理的な乱数源と擬似乱数源を組み合わせたものであり、検出結果も一様なビットではないからである。Beacon については、公開されているコミットメントの連鎖を、連続する [[engagements]] 組のパルスについて検証した。</p>

<h3>2. レベル 1：NIST SP 800-22 の検定群</h3>
<p>公式の検定群の 15 種類の検定をすべて実装し直した。これらは、文書の付録 B にある [[annexe_n]] 個の p 値を [[annexe_ecart]] 以内の差で再現する（1 つの検定では [[annexe_ecart_chev]]）。データは 10<sup>6</sup> ビットの系列 [[n_seq]] 本に分ける。[[np1]] 個の p 値全体を 1 つのファミリーとし、全体の有意水準 1% でホルム法により補正する。</p>
<ul>
<li>parity：p 値 [[par_np1]] 個、棄却なし（調整済み p 値の最小値：[[par_p1]]）。1 のビットの割合：[[par_frac]]。</li>
<li>anu と beacon：棄却なし（anu の調整済み p 値の最小値：[[anu_p1]]）。</li>
<li>ibm：[[ibm_np1]] 個中 [[ibm_rej1]] 個を棄却。1 のビットの割合：[[ibm_frac]]、すなわち標準偏差の [[ibm_z]] 倍のずれ。Belem を除くと、一定の偏りを厳密に取り除くフォン・ノイマン抽出器の後に [[vn_bits]] ビットが残り、[[vn_np]] 個の p 値に棄却は 1 つもない（[[vn_p]]）。不合格の原因は、データの作成者が述べている偏りである。</li>
</ul>

<h3>3. レベル 2：生成器の痕跡</h3>
<p>NIST の検定群からわかるのは、列が理想的な乱数からずれているかどうかであって、その理由ではない。次の 3 つの検定は、アルゴリズムによる生成器に特有の欠陥を狙う：</p>
<ul>
<li><strong>線形複雑度。</strong>バーレカンプ・マッシー法は、\(n\) ビットの区間を再現する最短の線形帰還シフトレジスタの長さ \(L\) を与える。ランダムな列では \(L\simeq n/2\) である。\(\mathrm{GF}(2)\) 上の線形生成器で、内部状態が \(n/2\) ビットに満たないものは、どれも \(L<n/2\) を与える。区間の長さは [[seg_bm]] ビットで、連続して読むか、48 ビットに 1 ビット、64 ビットに 1 ビットの割合で間引いて読む。これにより、[[etat_max]] ビットまでの内部状態がカバーされる。</li>
<li><strong>繰り返し。</strong>64 ビットの窓を、それぞれ他のすべての窓と比較する。一致する対の期待数は [[rep_attendu]] 程度である。繰り返しが 1 つでもあれば、周期か、シードの再利用を示すことになる。</li>
<li><strong>長距離相関。</strong>ラグ 17 から [[lag_max]] までの自己相関を、ボンフェローニ補正を施して調べる。</li>
</ul>
<p>主要ファミリー（p 値 [[np2]] 個、有意水準 1% のホルム法）：parity では棄却なし（[[par_p2]]）。\(L\) と \(n/2\) の差の最大値は [[par_ecart_l]]、繰り返しはなく、長距離相関は [[par_auto]] である。anu と beacon でも棄却なし。ibm では [[ibm_rej2]] 回の棄却がある。</p>

<h3>4. IBM での棄却：固まったマシン</h3>
<p>IBM のデータは、8192 ショットからなる試行 [[ibm_essais]] 回分でできている。そのうち [[ibm_const]] 回は完全に一定で（すべて 0 が [[ibm_const0]] 回、すべて 1 が [[ibm_const1]] 回）、ほかに [[ibm_quasi]] 回が 99% 以上一定である。これらはすべて Belem のものである。一致する窓の対 [[ibm_paires]] 組は、どれも同じビットだけが並んだ窓どうしであり、ふつうの組成の窓どうしで一致する対は [[ibm_paires_typ]] 組である。固まった出力は擬似乱数生成器の出力ではない。出力がないということである。</p>
<p>Belem の除外は、データを見た後で決めた。したがってこれは副次的な解析であり、独自のホルム補正を施している。当初の規則による結果も引き続き公開している。残る 8 台のマシン（[[sb_bits]] ビット）では、レベル 2 は何も棄却しない（p 値 [[sb_np2]] 個、調整済み p 値の最小値 [[sb_p2]]）。\(L\) と \(n/2\) の差の最大値は [[sb_ecart_l]] で、繰り返しは 1 つもない。ラグ 1 の相関は存在する（[[sb_r1]]、すなわち標準偏差の [[sb_z1]] 倍）。これは短距離の測定上の欠陥であり、生成器の構造とは関係がない。レベル 1 では、偏りのために [[sb_np1]] 個中 [[sb_rej1]] 個が棄却される。</p>

<h3>5. 対照</h3>
<p>同じ処理の連鎖を、既知の各生成器の [[bits_ctrl]] ビットに適用する。対照のいずれかが予想どおりにふるまわなければ、スクリプトは停止する。</p>
<div class="tableau"><table>
<thead><tr><th>生成器</th><th>予想</th><th>結果（調整済み p 値の最小値、レベル 1 と 2）</th></tr></thead>
<tbody>
<tr><td>次数 20 の LFSR</td><td>検出</td><td>検出：\(L\)&nbsp;=&nbsp;[[l20_lmin]]、繰り返し</td></tr>
<tr><td>次数 31 の LFSR</td><td>検出</td><td>検出：\(L\)&nbsp;=&nbsp;[[l31_lmin]]、\(\log_{10}p\)&nbsp;=&nbsp;[[l31_log10p]]</td></tr>
<tr><td>32 ビット LCG</td><td>検出</td><td>検出：スペクトル検定、長距離相関</td></tr>
<tr><td>Mersenne Twister</td><td>検出</td><td>レベル 2 のみで検出：\(L\)&nbsp;=&nbsp;[[mt_lmin]]、\(\log_{10}p\)&nbsp;=&nbsp;[[mt_log10p]]。NIST の検定群は反応せず（[[mt_p1]]）</td></tr>
<tr><td>PCG64</td><td>非検出</td><td>何もなし（[[pcg_p1]]、[[pcg_p2]]）</td></tr>
<tr><td>カウンターモードの SHA-256</td><td>非検出</td><td>何もなし（[[sha_p1]]、[[sha_p2]]）</td></tr>
<tr><td>\(\sqrt{2}\) の 2 進展開の数字</td><td>非検出</td><td>何もなし（[[r2_p1]]、[[r2_p2]]）</td></tr>
</tbody>
</table></div>
<p>Mersenne Twister の結果は、レベル 2 が公式の検定群に本当の感度を上乗せしていることを示す。PCG64、SHA-256、\(\sqrt{2}\) は、完全に決定論的な列でも、検出できる痕跡を何も持たないことがありうると示している。</p>

<h3>6. 限界</h3>
<ul>
<li>暗号学的な品質の生成器は、真の乱数と見分けがつかない。この検証が排除するのは、単純な生成器を使うシミュレーションであって、入念に作られたシミュレーションではない。SP 800-22 の文書自身も、いかなる検定の組み合わせも暗号解析の代わりにはならないと述べている。</li>
<li>レベル 2 の適用範囲：線形生成器が検出されるのは、内部状態が [[etat_max]] ビット未満の場合に限られる。繰り返しが検出されるのは、周期がデータより短い場合に限られる。</li>
<li>生データの量は多くない。また、2 つの生の源のいずれも、抜け穴のないベルテストによって認証されてはいない。</li>
<li>Belem の除外は事後的な決定である。その原因は記録されており、除外前の結果も公開している。</li>
<li>ANU と Beacon のデータセットが測っているのは、AES-128 と SHA-512 の品質にすぎない。</li>
</ul>

<h3>7. 再現する</h3>
<p>データは <code>telecharger.py</code> が取得し直し、そのハッシュを照合する。そのあと <code>analyse.py</code> はネットワークなしで動き、自己テストを含めて 2 分足らずで終わる。</p>
<pre><code>python3 telecharger.py
python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-4/analyse.py" download>analyse.py</a>：解析</li>
<li><a href="/fichiers/test-4/telecharger.py" download>telecharger.py</a>：検証付きのデータ取得</li>
<li><a href="/fichiers/test-4/resultats.json" download>resultats.json</a>：計算したすべての値</li>
<li><a href="/fichiers/test-4/sources.md" download>sources.md</a>：各記述の出典</li>
</ul>

<h2 id="sources">出典</h2>
<ol class="sources">
<li>J. T. Kavulich, B. P. Van Deren, M. Schlosshauer, <cite>Searching for evidence of algorithmic randomness and incomputability in the output of quantum random number generators</cite>, Physics Letters A 388, 127032（2021）、<a href="https://arxiv.org/abs/2101.01238">arXiv:2101.01238</a>。データ：<a href="https://zenodo.org/records/4440318">Zenodo 4440318</a>。</li>
<li>B. P. Van Deren, J. T. Kavulich, M. Schlosshauer, <cite>Parity-based, bias-free optical quantum random number generation with min-entropy estimation</cite>, <a href="https://arxiv.org/abs/2006.11425">arXiv:2006.11425</a>。</li>
<li>O. Root, M. Becker, <cite>Does True Randomness Exist? Efficacy Testing IBM Quantum Computers via Statistical Randomness</cite>, <a href="https://arxiv.org/abs/2401.12250">arXiv:2401.12250</a>。データ：<a href="https://doi.org/10.5281/zenodo.10542216">DOI 10.5281/zenodo.10542216</a>。</li>
<li>J. Y. Haw et al., <cite>Maximization of Extractable Randomness in a Quantum Random-Number Generator</cite>, <a href="https://arxiv.org/abs/1411.4512">arXiv:1411.4512</a>。</li>
<li>NIST, <cite>A Reference for Randomness Beacons: Format and Protocol Version 2</cite>, <a href="https://csrc.nist.gov/pubs/ir/8213/ipd">NISTIR 8213</a>。</li>
<li>L. K. Shalm et al., <cite>A strong loophole-free test of local realism</cite>, <a href="https://arxiv.org/abs/1511.03189">arXiv:1511.03189</a>。</li>
<li>NIST, <cite>A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications</cite>, <a href="https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final">SP 800-22 Rev. 1a</a>。</li>
</ol>
""",
}
