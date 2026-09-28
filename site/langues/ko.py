"""한국어: 프랑스어 원문(fr.py)의 번역.

각 [[표지]]는 resultats.json의 수치로 바뀌며, 이 언어의 관례에 따라 표기된다.
수식 $$…$$와 \\(…\\)는 모든 언어에서 동일하다. 역슬래시 때문에 원시 문자열(r\"\"\"…\"\"\")이 필요하다.
수치 표지 바로 뒤에는 받침에 따라 형태가 바뀌는 조사를 붙이지 않는다(값이 바뀔 수 있으므로).
"""
NOM = '한국어'
HTML_LANG = 'ko'
HREFLANG = 'ko'
DIR = 'ltr'
LOCALE_OG = 'ko_KR'
DECIMALE = '.'

UI = {
    'devise': '시뮬레이션 가설 연구.',
    'description_site': 'aeternam — 시뮬레이션 가설 연구',
    'travaux': '연구',
    'langue': '언어',
    'surtitre': '연구 · 검증 1',
    'meta': '제2판 · 재현 가능한 2차 분석',
    'verdict': '현재까지의 판정: 검토한 데이터에서 시뮬레이션의 흔적은 발견되지 않았다.',
    'fichier_pdf': 'aeternam-test-1-ko.pdf',
}

ARTICLE = {
    'titre': 'GRB 221009A로 검증한 입방 격자',
    'description': 'LHAASO가 관측한 광자가 이산적인 공간의 격자 간격에 부과하는 제약, '
                   '그리고 그 제약이 멈추는 지점.',
    'date': '2026년 9월 28일',
    'corps': r"""
<section class="resume">
<h2>요약</h2>
<ul>
<li><strong>공간이 입방 격자이고</strong> 그 위에서 빛이 맥스웰 방정식의 수치 시뮬레이션에서처럼 전파된다면, 에너지가 가장 높은 광자는 늦게 도착할 것이다. 감마선 폭발 GRB&nbsp;221009A에서 LHAASO는 이런 지연을 관측하지 못했다.</li>
<li><strong>따라서 격자 간격은 [[a_resume]]&nbsp;m 미만이다</strong>(가장 보수적인 방법과 가장 불리한 방향을 택한 경우). 가능도 방법을 쓰면 [[a_ml_resume]]&nbsp;m 미만이다. 격자의 에너지 척도는 [[echelle_resume]]&nbsp;GeV를 넘는다.</li>
<li><strong>새로운 한계는 아니다.</strong> Beane, Davoudi, Savage는 이미 2012년에 우주선으로부터 같은 크기 정도의 값(약 [[b_beane]]&nbsp;m)을 얻었다. 이 결과는 다른 관측량을 통한 독립적인 확인이다.</li>
<li><strong>새로운 점: 시간 간격이 중요하다.</strong> 모든 수치 시뮬레이션에서처럼 시간도 잘게 나뉘어 있다면 효과는 줄어든다. 안정성이 유지되는 최대 시간 간격에서는 정육면체의 여덟 대각선 방향을 따라 빛에 분산이 전혀 일어나지 않는다. 따라서 폭발 하나만으로는 보편적인 한계를 얻을 수 없다. 방향의 95%에 대해서는 격자 간격이 여전히 [[a95_sigma1]]&nbsp;m 미만이다.</li>
<li><strong>주된 오차가 <em>a</em>에 대해 선형인 격자</strong>는 플랑크 길이의 10분의 1인 [[a_lineaire]]&nbsp;m까지 배제된다.</li>
<li><strong>플랑크 크기의 격자 간격에는 여전히 닿지 않는다</strong>. 그 효과는 이 검증으로 잡아내기에는 약 [[facteur_planck]]배나 약하다.</li>
<li><strong>문헌을 확인하는 과정에서</strong> 2025년 논문(Xi와 Shu)의 환산에서 불일치를 발견했다. 그들의 이차 한계는 [[xs_facteur]]배 과대평가된 것으로 보인다.</li>
<li><strong>검출은 없으며, 우리가 시뮬레이션 속에 있을 확률도 제시하지 않는다.</strong> 이 검증은 하나의 특정한 구조를 제약할 뿐, 시뮬레이터의 존재에 대해서는 아무것도 말하지 않는다.</li>
</ul>
</section>

<h2 id="question">1. 검증하는 질문</h2>
<p>수치 시뮬레이션은 유한한 개수의 점으로 공간을 나타낸다. 그 안에서 전파되는 파동은 연속 공간에서와 정확히 같게 행동하지 않는다. 파동의 속도가 파장에 따라 조금씩 달라지는 것이다. 따라서 빛의 경우, 속도가 광자의 에너지에 따라 달라지게 된다. 이 효과는 아주 작지만, 우주론적 거리에 걸쳐 누적된다.</p>
<p>GRB&nbsp;221009A는 지금까지 기록된 가장 밝은 감마선 폭발이다. LHAASO 관측소는 이 폭발에서 10&nbsp;TeV가 넘는 광자를 검출했는데, 이 광자들은 약 20억 년 전에 출발했다(적색편이 <em>z</em>&nbsp;=&nbsp;[[z]]). 빛의 속도가 에너지에 따라 달라진다면 고에너지 광자는 저에너지 광자보다 늦게 도착할 것이다. LHAASO 협력단은 이 지연을 찾았지만 발견하지 못했다.</p>
<p>따라서 질문은 명확하다. <em>지연이 0이라는 결과가 여전히 허용하는 격자 간격은 얼마인가?</em> 이 질문은 모든 시뮬레이션이 격자를 쓸 것이라고도, 격자가 시뮬레이션을 증명할 것이라고도 가정하지 않는다.</p>

<h2 id="modele">2. 모형: 격자 위의 맥스웰 방정식</h2>
<p>전자기장을 격자 간격이 <em>a</em>인 입방 격자 위에 놓는다. 이는 맥스웰 방정식의 수치 시뮬레이션에 쓰이는 Yee 기법(1966)이나, 격자 전기역학의 해밀턴 형식(Kogut와 Susskind, 1975)과 정확히 같은 방식이다. 시간은 연속적으로 흐르거나 \(\Delta t\) 간격으로 진행한다. 이때 파동 벡터가 \(\mathbf k\)이고 각진동수가 \(\omega\)인 평면파는 다음 분산 관계를 따른다:</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>이 기법은 \(c\,\Delta t\le a/\sqrt{3}\)일 때만 안정하다. 따라서 \(c\,\Delta t=\sigma a/\sqrt{3}\)로 쓰며, 여기서 \(0\le\sigma\le1\)은 쿠랑 수이다. \(\sigma=0\)은 연속 시간에 해당한다. 파장이 격자 간격보다 훨씬 긴 광자에 대해 \(E=\hbar\omega\)로 두면, 군속도는 다음과 같다:</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\)는 격자 축에 대한 광자의 방향 \(\mathbf n\)에 따라 달라진다. 축을 따라서는 \(Q=1\)이고, 정육면체의 체대각선을 따라서는 \(Q=1/3\)이다. 이후 논의에서는 세 가지 성질이 중요하다:</p>
<ul>
<li>효과는 <strong>이차</strong>이다. 격자 간격이 10배 촘촘해지면 효과는 100배 약해진다.</li>
<li>기법이 안정한 한, 광자는 <strong>느려질</strong> 뿐 결코 빨라지지 않는다.</li>
<li>두 편광이 같은 방식으로 전파된다. <strong>복굴절이 없으므로</strong> 매우 강력한 편광 제약은 여기에 적용되지 않는다.</li>
</ul>

<h2 id="lhaaso">3. LHAASO와의 대조</h2>
<p>LHAASO는 이차 지연을 \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\)로 기술하고, \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\)에 대한 구간을 발표한다. 여기서 \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV이다(논문의 식 2, 3, 5). 두 식을 대응시키면:</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>에너지가 \(E_h\)와 \(E_l\)인 두 광자 사이에 누적되는 지연은 다음과 같다.</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>LHAASO의 우주론 매개변수(<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc, Ω<sub>m</sub>&nbsp;=&nbsp;[[om]], Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]])를 쓰면 <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s이다. 측정은 조합 \(a\sqrt{Q_{\mathrm{eff}}}\)만을 제약한다. LHAASO 논문의 표 I은 95% 신뢰 수준에서 다음 값을 제시한다:</p>
<div class="tableau"><table>
<thead><tr><th>방법</th><th>하한</th><th>최적 적합</th><th>상한</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML (보정)</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>세 구간 모두 0을 포함한다. 즉 지연은 검출되지 않았다. 세 방법은 같은 폭발을 분석하므로 결합하지 않는다. \(\eta_2\)의 상한 \(U\)로부터 다음을 얻는다.</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>연속 시간에서는 다음 결과를 얻는다:</p>
<div class="tableau"><table>
<thead><tr><th>방법</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\), 가장 불리한 방향 (m)</th><th>\(a\), 방향의 95% (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML (보정)</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>요약에서는 가장 보수적인 값인 [[a_resume]]&nbsp;m를 택했다. 이는 제시를 위한 포락선이지 새로운 구간이 아니다. 이 한계에서 1&nbsp;TeV 광자는 [[e_bas]]&nbsp;TeV 광자보다 최대 [[retard_limite]]&nbsp;s 늦게 도착한다.</p>
<p>측정값이 아닌 몇 가지 예측(1&nbsp;TeV 광자와 [[e_bas]]&nbsp;TeV 광자의 비교):</p>
<div class="tableau"><table>
<thead><tr><th>격자 간격</th><th>예측 \(\eta_2\)</th><th>예측 지연</th><th>판정</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]]~[[p26_eta_max]]</td><td>[[p26_ret_min]]~[[p26_ret_max]]&nbsp;s</td><td>모든 방향에서 배제</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]]~[[p27_eta_max]]</td><td>[[p27_ret_min]]~[[p27_ret_max]]&nbsp;s</td><td>축 부근(\(Q>\)&nbsp;[[q_cal_axe]])에서 보정 방법으로만 배제</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]]~[[p28_eta_max]]</td><td>[[p28_ret_min]]~[[p28_ret_max]]&nbsp;ms</td><td>배제되지 않음</td></tr>
<tr><td>[[lpl]]&nbsp;m (플랑크 길이)</td><td>[[pl_eta_min]]~[[pl_eta_max]]</td><td>[[pl_ret_min]]~[[pl_ret_max]]&nbsp;s</td><td>도달 불가</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. 한계는 어디까지 버티는가</h2>
<h3>격자의 방향</h3>
<p>폭발의 방향에 대해 격자가 어떻게 놓여 있는지는 알 수 없다. 주된 한계는 가장 불리한 경우인 \(Q=1/3\)을 택한다. 균일하게 분포한 100만 개의 방향에서 \(Q\)의 중앙값은 [[q_mediane]]이고, 95%의 경우 [[q_5]]보다 크다. 한계는 거의 변하지 않아, 방향의 95%에 대해 [[ccf_95]]&nbsp;m, 중앙값 방향에 대해 [[ccf_mediane]]&nbsp;m이다. 이 비율은 기하학적인 것이며, 우주에 대한 확률이 아니다.</p>
<h3>이산 시간: 한계의 약점</h3>
<p>시뮬레이션은 시간 간격 단위로 진행한다. 시간을 이산화하면 부호가 반대인 오차가 생겨, 공간 이산화의 오차를 일부 상쇄한다(\(-\sigma^{2}/3\) 항). 보수적인 방법의 경우:</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>가장 불리한 방향</th><th>방향의 95%</th><th>중앙값 방향</th></tr></thead>
<tbody>
<tr><td>0 (연속 시간)</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1 (최대 간격)</td><td>[[s4_cdt]]</td><td>한계 없음</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>안정성이 유지되는 최대 간격에서는 체대각선을 따른 상쇄가 정확하며, 1차 근사에서만 그런 것이 아니다. 그 방향에서는 분산 관계가 모든 파장에 대해 \(\omega=ck\)를 그대로 돌려준다. 이렇게 설정된 시뮬레이션은 폭발이 여덟 대각선 방향 중 하나에 놓인다면 이 검증을 완전히 피해 간다. 이것이 단일 천체에서 얻은 한계의 주된 약점이다. 서로 다른 방향에 있는 여러 천체를 쓰면 이 약점을 없앨 수 있다. 우연이 아니라면 그 천체들이 모두 대각선 위에 놓일 수는 없기 때문이다.</p>
<h3>고정된 격자 간격인가, 팽창에 따라 늘어나는 격자 간격인가</h3>
<p>여기서는 물리적 격자 간격이 고정되어 있다고 가정한다. 격자가 우주와 함께 늘어난다면(공동 격자 간격), 효과는 더 이상 적색편이에 따라 커지지 않으며 \(I_2\)는 \(I_0\)로 바뀐다. 이때 한계는 \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]]배만큼 약해져 [[comobile_a]]&nbsp;m가 된다. <em>z</em>&nbsp;=&nbsp;[[z]]에서는 이 선택이 거의 중요하지 않다.</p>
<h3>더 정밀한 기법</h3>
<p>시뮬레이터는 주된 오차가 \(a^{4}\)에 비례하는 고차 기법을 쓸 수도 있다. 그러면 효과는 에너지의 네제곱에 비례하게 되고, \(a\)에 대한 한계는 훨씬 약해진다. LHAASO는 이 폭발에 대해 이런 종류의 제약을 발표하지 않았다. 이를 정량화하려면 광자 하나하나의 데이터가 필요하다. 분산을 상쇄하도록 설계된 항 역시 이 한계를 피해 간다. 이들은 다른 모형이며, 따로 검증해야 한다.</p>
<h3>오차가 선형이라면?</h3>
<p>대칭적인 격자는 \(a\)에 대해 선형인 효과를 만들지 않는다. 서로 반대인 두 전파 방향 사이의 대칭을 깨뜨려 그런 효과를 만드는 이산화가 있다면, LHAASO의 선형 한계 \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\)에 걸린다. 계수가 1 정도라면 \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m, 즉 플랑크 길이의 10분의 1이다. 이보다 거친 이런 유형의 격자는 모두 배제된다.</p>
<h3>계산의 타당성</h3>
<p>전개는 \(aE/\hbar c\ll1\)을 가정한다. 한계값에서는 20&nbsp;TeV 광자에 대해서도 \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]이다. 전개식을 정확한 분산 관계와도 비교했다. \(ak\)&nbsp;=&nbsp;[[ak_test]]일 때 상대 편차는 예상대로 [[ecart_dispersion]] 이하이다.</p>

<h2 id="contexte">5. 기존 결과와 비교한 의미</h2>
<p>Beane, Davoudi, Savage(2012)는 격자 양자 색역학의 시뮬레이션을 연구했다. 그들은 우주선 스펙트럼의 차단으로부터 격자 간격의 역수를 \(1/b\gtrsim10^{11}\)&nbsp;GeV, 즉 \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m로 제한했다. 우리의 보수적 한계는 그들 값의 [[beane_ratio]]배이고, LHAASO의 가능도 방법으로는 [[beane_ml_min]]~[[beane_ml_max]]배이다. 따라서 두 접근은 관측량, 입자, 가정이 서로 다르지만 크기 정도에서 일치한다. 이는 확인이지 기록 경신이 아니다.</p>
<p>플랑크 길이 [[lpl]]&nbsp;m는 여기서 여덟 자릿수 더 아래에 있다. 이 크기의 격자 간격이라면 효과는 한계보다 [[facteur_planck_exact]]배 약할 것이다. 효과는 에너지의 제곱에 비례해 커지므로 약 1억 배 더 에너지가 높은 광자가 필요한데, 이는 지금까지 관측된 어떤 것보다도 훨씬 높다. 이 차수에서는 어떤 비행시간 검증도 플랑크 크기의 격자에 닿을 수 없다.</p>

<h2 id="xi-shu">6. 문헌 검증: Xi와 Shu(2025)</h2>
<p>Xi와 Shu는 다른 방법으로 같은 폭발을 분석해 \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV(그들의 표 III)를 보고했는데, 이는 LHAASO 한계의 약 [[xs_rapport_lhaaso]]배이다. 그들 자신의 정의에서 출발해도 우리는 이 값을 재현하지 못한다.</p>
<ul>
<li>그들의 식 (3)은 지연이 \((E/E_{\mathrm{QG},n})^{n}\)에 비례하도록 정한다. \(n=1\)의 경우, 그들의 환산식 (6) \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\)(\(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]])은 일관적이다. 우리가 얻은 값은 [[xs_c1]]이다.</li>
<li>\(n=2\)의 경우, 그들의 식 (7) \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\)(\(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]])은 \(1/\theta\) 형태를 유지한다. 이를 그들의 한계 \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV²에 적용하면 실제로 그들의 표 값([[xs_eq7]]&nbsp;GeV)이 재현된다. 그러나 지연이 이차이므로, 그들의 식 (3)은 \(1/\sqrt{\theta_2}\) 의존성을 요구한다. 즉 \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\)이고, 따라서 \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV이다.</li>
<li>차이는 [[xs_facteur]]배이다. 그럴듯한 설명: \(\varepsilon^{2}\theta_2\)의 값은 [[xs_eps2]]이며, [[xs_c2_imprime]]의 형태는 [[xs_eps2_imprime]]의 제곱근을 10의 거듭제곱 부분에만 취한 결과와 닮았다.</li>
</ul>
<p>현황: 논문 제1판에 나타난 외견상의 불일치이며, 저자들에게 확인이 필요하다. 우리는 그들의 데이터를 재분석하지 않았으며 다른 결과를 평가하지도 않는다. 수정하더라도 그들의 한계는 LHAASO의 한계보다 [[xs_vs_lhaaso]]배 강하다. 우리는 이 한계를 사용하지 않는다.</p>

<h2 id="limites">7. 이 검증이 말하지 않는 것</h2>
<ul>
<li>아무것도 검출하지 않는다. 지연 0은 모든 측정과 양립한다.</li>
<li>우리가 시뮬레이션 속에 있을 확률은 전혀 계산하지 않는다. ‘95%’는 물리적 매개변수에 관한 것이다.</li>
<li>제약하는 것은 특정한 구조, 즉 입방 격자, Yee 기법, 고정된 격자 간격, 보상 없음이라는 구조이다.</li>
<li>지연이 검출되더라도 컴퓨터를 가리키지는 않는다. 근본적으로 이산적인 물리학이나 다른 양자 중력 효과도 같은 신호를 만들 것이다.</li>
<li>LHAASO의 구간은 천체에서의 방출에 관한 가정에 기반하며, 우리는 그 가정을 그대로 물려받는다.</li>
</ul>

<h2 id="suite">8. 다음 단계</h2>
<ol>
<li>서로 다른 방향에서 관측된 여러 천체를 결합해 대각선 방향의 사각지대를 없앤다.</li>
<li>고차 기법(\(a^{4}\) 효과)을 정량화한다. 이를 위해서는 광자 하나하나의 데이터가 필요하다.</li>
<li>Xi와 Shu에게 환산 방식에 대한 해명을 요청한다.</li>
<li>검증을 격자의 다른 징후로 확장한다: 우주선의 비등방성, 하전 입자.</li>
</ol>

<h2 id="reproduire">9. 재현</h2>
<p>모든 값은 외부 의존성이 없는 Python 스크립트로 다시 계산되며, 스크립트는 먼저 자신의 공식을 검사한다: 정확한 분산 관계와 전개식의 비교, 대각선에서의 정확한 결과, 왕복 환산, 우주론적 적분, 그리고 \(Q\)의 평균이 3/5와 같다는 점.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>: 스크립트(Python&nbsp;3.10 이상, 표준 라이브러리만 사용, 코드 주석은 프랑스어)</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>: 계산된 모든 값</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>: 이 노트의 PDF 판</li>
</ul>
<p>독립적인 교차 검증(numpy, scipy)으로 우주론적 적분을 10<sup>−15</sup> 이내의 정밀도로, 방향 분위수를 1,000만 번의 무작위 추출로, 군속도를 분산 관계의 수치 풀이로 각각 재현했다.</p>
<p>이 노트는 2026년 9월 28일의 첫 판을 대체한다. 이산 시간, 방향, 공동 격자 간격, 선형 효과, Beane 등과의 비교를 추가했다.</p>

<h2 id="sources">출처</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>(2026년 2월 13일 개정판): 식 2, 3, 5, 표 I.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>(2012).</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a>(2025): 식 3, 6, 7, 표 I 및 표 III.</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302(1966).</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395(1975).</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House: 수치 분산과 Yee 기법의 안정성.</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>: 기본 물리 상수.</li>
</ol>
""",
}

ARTICLE_2 = {
    'titre': '우주선은 격자를 그려 내는가?',
    'description': '피에르 오제 관측소가 기록한 가장 높은 에너지의 입자들을, '
                   '입방 격자가 남겼어야 할 흔적과 대조한다.',
    'date': '2026년 9월 28일',
    'corps': r"""
<section class="verdict-net">
<h2>판정</h2>
<p><strong>아니다.</strong> 피에르 오제 관측소가 측정한, 에너지가 가장 높은 우주선 [[n_evt]]개에는 정육면체 대칭이 전혀 보이지 않는다. 격자가 전혀 없는 하늘에서도 관측된 것만큼 뚜렷하거나 더 뚜렷한 무늬가 [[p4_pct]]%의 경우에 나타난다. 우리가 보는 것은 평범한 우연일 뿐이다.</p>
<p>이 ‘아니다’가 미치는 범위는 제한적이다. 입자가 [[n_evt]]개뿐이어서 아주 뚜렷한 무늬만 드러날 수 있었다. 더 미묘한 무늬는 여전히 있을 수 있다.</p>
</section>

<h2 id="explication">설명</h2>
<p>우리 세계가 컴퓨터로 계산되고 있다면, 이미지가 픽셀로 이루어져 있듯이 공간도 아주 작은 정육면체들로 나뉘어 있을지 모른다. 2012년, 세 명의 물리학자가 이런 분할이 흔적을 남긴다는 점에 주목했다. 우주에서 가장 빠른 입자들이 모든 방향에서 똑같이 오지는 않으리라는 것이다. 어떤 방향들이 더 자주 나타나고, 그 방향들은 정육면체의 면이나 꼭짓점처럼 배열될 것이다.</p>
<p>이런 입자는 실제로 존재한다. 바로 우주선이다. 우주에서 날아온 원자핵으로, 우리의 가속기가 만들어 내는 어떤 것보다도 훨씬 큰 에너지를 지니고 있다. 아르헨티나의 피에르 오제 관측소는 거대한 검출기 망으로 이 입자들을 기다린다. 관측소는 2004년부터 2020년까지 포착한, 에너지가 가장 높은 [[n_evt]]개의 목록을 각각이 날아온 방향과 함께 공개했다.</p>
<p>우리는 이 [[n_evt]]개의 방향을 가져와 정육면체를 따라 늘어서 있는지 살펴보았다. 그 정육면체가 어떻게 돌아가 있을지는 아무도 모르기 때문에 [[n_orient]]가지 자세를 시험했다. 가장 좋은 자세는 데이터와 조금 들어맞았다. 하지만 이렇게 많은 자세를 시험하면, 순전히 우연으로 만들어진 하늘에서도 조금 들어맞는 자세는 언제나 하나쯤 나온다.</p>
<p>판단을 내리기 위해, 같은 관측소에서 본 가짜 하늘 [[n_ciels]]개를 무작위로 만들고 각각에 똑같은 탐색을 수행했다. 그중 [[p4_pct]]%에서 적어도 그만큼 잘 들어맞는 정육면체가 발견된다. 따라서 실제 하늘에는 특별한 점이 없다. 단서라고 부르려면 거의 모든 가짜 하늘보다 더 잘 들어맞았어야 했다.</p>
<p>결론: 격자의 흔적은 없다. 하지만 이 탐색은 뚜렷한 무늬만 볼 수 있었다. 입자가 [[n_evt]]개뿐이라 희미한 무늬는 눈에 띄지 않고 지나갈 것이다. 게다가 우리 은하의 자기장이 이 입자들을 도중에 휘게 하므로 무늬의 일부가 흐려질 것이다. 그러므로 이 검증은 공간이 연속적이라는 것을 증명하지 않는다. 우리가 볼 수 있었던 곳에는 아무것도 없다는 것을 보여 줄 뿐이다.</p>

<h2 id="analyse">상세 분석</h2>

<h3>1. 격자에서 검증 가능한 예측으로</h3>
<p>격자 간격이 \(a\)인 입방 격자에서 이산 라플라시안은 \(k^{2}\)을 \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\)로 바꾼다. 자유장에 대해</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>이며, 여기서 \(\mathbf n\)은 격자 축으로 나타낸 전파 방향이다. 이는 검증 1과 같은 함수 \(Q\)이다. 더 일반적으로, 도래 방향에 대한 격자의 모든 효과(전파, 방향에 따라 달라지는 스펙트럼 차단)는 정육면체 군 \(O_h\)에 대해 불변인 \(\mathbf n\)의 함수이다. 그런데 \(O_h\)에 대해 불변인 구면 조화 함수는 \(\ell=0,4,6,8,\dots\)에서만 존재한다. 허용되는 첫 비등방성은 입방 조화 함수 \(\ell=4\)이며, 이는 \(Q-3/5\)에 비례한다. 이것이 데이터를 열어 보기 전에 정해 둔 주 검정이며, \(\ell=6\)은 두 번째로 검정한다. Beane, Davoudi, Savage는 시뮬레이션이 “최고 에너지 우주선의 분포에서, 바탕에 있는 격자의 구조를 반영하는 어느 정도의 회전 대칭 깨짐으로 드러날 수 있다”고 썼다.</p>

<h3>2. 데이터</h3>
<p>피에르 오제 관측소 카탈로그(ApJS 264, 50, 2023): 2004년 1월 1일부터 2020년 12월 31일까지 기록된, 에너지가 가장 높은 공기 샤워 [[n_evt]]개로, 에너지는 [[e_min]]~[[e_max]]&nbsp;EeV, 천정각은 최대 [[zmax]]°이다. 공개 파일에는 이 [[n_evt]]개와 별도로 보정용 하이브리드 사건 [[n_calib]]개도 들어 있으며, 이들은 제외한다. 표면 검출기로 재구성한 적경과 적위를 사용한다. 파일의 SHA-256 지문은 실행할 때마다 확인한다. 이 에너지에서는 천정각 [[zmax]]°까지 검출 효율이 완전하므로, 노출은 순전히 기하학적으로 정해진다.</p>

<h3>3. 검출기의 노출</h3>
<p>위도 \(a_0\)&nbsp;=&nbsp;[[lat]]°에 있고 천정각 \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]°를 받아들이는 지상 검출기의 노출은 적경에 대해 균일하며, 적위 \(\delta\)에 대해서는 다음과 같다(Sommers, 2001):</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>보이는 하늘은 \(\delta\)&nbsp;=&nbsp;[[dec_max]]°에서 끝나며, 이는 천구의 [[ciel_pct]]%이다. 따라서 오제 관측소에서 본 등방적 하늘은 균일하지 않다. 이후의 모든 비교는 데이터를 균일한 구가 아니라 바로 이 하늘과 비교한다.</p>

<h3>4. 통계량</h3>
<p>격자의 방향을 \(R\), 그 행을 \(\mathbf e_k\)라 하고, \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\)이라 하자. 관측된 \(N\)개의 방향에 대해:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>여기서 \(\langle\cdot\rangle_\omega\)는 노출로 가중한 등방적 하늘에 대한 평균이다. \(T>0\)은 정육면체 축을 따른 초과를, \(T<0\)은 대각선을 따른 초과를 나타내며, 절댓값은 둘 다 포괄한다. \(f\)가 4차 다항식이므로 \(T(R)\)은 15개의 모멘트 \(\sum_i\mathbf n_i^{\alpha}\)를 통해서만 데이터에 의존한다. 평균과 분산은 가우스-르장드르 구적법으로 정확히 계산한다. 최댓값은 균일하게(하르 측도에 따라) 추출한 [[n_orient]]개의 방향에 대해 취한다. \(\ell=6\)에 대해서는 다음 함수를 쓴다: \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). 여기서 \(\alpha\)&nbsp;=&nbsp;[[alpha6]](즉 \(-15/11\))로 두어 \(\ell=4\)와 직교하게 한다. 결합 검정은 \(T_4^{2}+T_6^{2}\)을 최대화한다.</p>

<h3>5. 우연의 보정</h3>
<p>[[n_orient]]개의 방향 중 최선을 찾으면 \(Z_4\)는 기계적으로 커지며, 정규 분포를 따르지 않는다. 그래서 노출에 따라 \(N\)개의 사건으로 된 등방적 하늘 [[n_ciels]]개를 추출하고, 여기에 똑같은 최대화를 적용한다. ‘격자 없음’ 가설 아래에서 \(Z_4\)의 중앙값은 [[z4_50]]이고, 5%의 경우 [[z4_95]], 1%의 경우 [[z4_99]], 0.1%의 경우 [[z4_999]]보다 커진다. 이렇게 하여 p값 \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\)에는 방향 선택의 대가가 포함된다.</p>

<h3>6. 결과</h3>
<div class="tableau"><table>
<thead><tr><th>검정</th><th>관측 통계량</th><th>p값</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (주 검정)</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\)와 \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>최적 방향에서 \(Q\)의 평균은 [[q_obs]]이며 기댓값은 [[q_iso]]이다. 즉 축 방향으로 [[q_ecart_pct]]% 초과한다. 이는 유의하지 않다. 주 검정의 \(p\)&nbsp;=&nbsp;[[p4]]이며, 어떤 부차 검정도 0.05 아래로 내려가지 않는다. 데이터는 입방 대칭이 전혀 없다는 가정과 양립한다.</p>

<h3>7. 이 검정이 볼 수 있었던 것</h3>
<p>민감도를 정량화하기 위해 입방 무늬를 주입한다. 밀도는 \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\)에 비례한다. \(\varepsilon>0\)이면 축을 따른 선속이 평균의 \(1+\varepsilon\)배가 되고, \(\varepsilon<0\)이면 초과가 대각선으로 옮겨 간다. 각 \(\varepsilon\)에 대해 방향이 무작위인 하늘 [[n_ciels_signal]]개로 \(Z_4\)의 분포를 얻는다. 95% 상한: 축 방향으로 \(\varepsilon\le\)&nbsp;[[eps_axes]], 대각선 방향으로 \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]]. 다시 말해 축을 따라 약 [[eps_axes_pct]]%(또는 대각선을 따라 [[eps_diag_pct]]%)까지의 초과는 배제되지 않는다. 사건 수가 적어서 생기는 약한 제약이다.</p>
<p>스크립트는 먼저 자신의 처리 과정을 검사한다: 정육면체 군에 대한 \(Q\)의 불변성, 정확한 다항식 전개, 적위 [[dec_max]]° 너머에서 노출 0, 등방성 아래에서 \(T\)의 표준화(평균 0, 분산 1), \(\ell=6\)과 \(\ell=4\)의 직교성, 그리고 뚜렷하게 주입한 무늬의 검출(그 방향은 [[ecart_orient]]° 이내로 복원된다).</p>

<h3>8. 한계</h3>
<ul>
<li>우주선은 전하를 띤다. 은하 자기장과 은하 간 자기장이 그 방향을 휘게 하며, 원자핵이 무거울수록 더 크게 휜다. 찾는 무늬는 규모가 커서(축과 대각선은 [[angle_diag]]° 떨어져 있다) 적당한 편향에는 견디지만, 발생원이나 전파 과정에서 새겨진 흔적은 일부 지워질 것이다.</li>
<li>격자가 먼 별들에 대해 고정되어 있다고(적도 좌표) 가정한다. 그 별들에 대해 움직이거나 회전하는 격자에는 다른 검정이 필요하다.</li>
<li>사건 [[n_evt]]개와 하늘의 [[ciel_pct]]%: 위의 상한이 보여 주듯 통계적 검정력이 낮다.</li>
<li>실제 천체물리학적 비등방성에 \(\ell=4\) 성분이 들어 있을 수 있다. 양성 결과였다면 이를 배제해야 했겠지만, 영(null) 결과는 이에 좌우되지 않는다.</li>
<li>시뮬레이션 속에 있을 확률은 계산하지 않는다. 이 검정은 입방 격자라는 특정한 징후를 대상으로 한다.</li>
</ul>

<h3>9. 재현</h3>
<p>Python 스크립트(numpy)가 약 1분 만에 모든 것을 다시 수행한다: 데이터 읽기와 점검, 자체 테스트, 통계량, 모의 하늘, 상한. 난수 생성기의 시드가 고정되어 있어 실행할 때마다 결과가 같다.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-2/analyse.py" download>analyse.py</a>: 스크립트</li>
<li><a href="/fichiers/test-2/resultats.json" download>resultats.json</a>: 계산된 모든 값</li>
<li><a href="/fichiers/test-2/donnees/auger_catalogSD.csv" download>auger_catalogSD.csv</a>: 피에르 오제 관측소 데이터(CC BY-SA 4.0 라이선스)</li>
</ul>

<h2 id="sources">출처</h2>
<ol class="sources">
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>(2012).</li>
<li>Pierre Auger Collaboration, <cite>A Catalog of the Highest-Energy Cosmic Rays Recorded During Phase I of Operation of the Pierre Auger Observatory</cite>, ApJS 264, 50(2023), <a href="https://arxiv.org/abs/2211.16020">arXiv:2211.16020</a>.</li>
<li>Pierre Auger Collaboration, <cite>Auger Open Data</cite>, 릴리스 3, <a href="https://doi.org/10.5281/zenodo.10488964">DOI 10.5281/zenodo.10488964</a>; 검출 효율: <a href="https://opendata.auger.org/data.php">opendata.auger.org</a>.</li>
<li>P. Sommers, <cite>Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory</cite>, Astroparticle Physics 14, 271(2001), <a href="https://arxiv.org/abs/astro-ph/0004016">arXiv:astro-ph/0004016</a>.</li>
</ol>
""",
}

ARTICLE_3 = {
    'titre': '빛은 어떤 방향에서 더 느리게 가는가?',
    'description': '하늘에 흩어진 여덟 개의 감마선 천체를 결합해 검증 1의 사각지대를 메우고, '
                   '방향과 관계없이 입방 격자의 격자 간격을 제한한다.',
    'date': '2026년 9월 28일',
    'corps': r"""
<section class="verdict-net">
<h2>판정</h2>
<p><strong>아니다.</strong> 조사한 천체 [[n_src]]개 가운데 어느 것도 격자가 만들어 낼 지연을 보이지 않는다. 이들의 방향을 결합하면, 방향이 어떠하든 시간 간격이 어떠하든, 격자 간격이 [[a_exclue]]&nbsp;m 이상인 입방 격자는 배제된다. 검증 1의 사각지대는 닫혔다.</p>
</section>

<h2 id="explication">설명</h2>
<p>이미지가 픽셀로 이루어지듯 우주가 격자 위에서 계산되고 있다면, 빛은 모든 방향으로 정확히 같은 속도로 나아가지 않을 것이다. 에너지가 가장 높은 빛은 아주 약간 늦어지며, 그 지연은 격자의 대각선을 따라서보다 모서리를 따라서 더 크다. 수십억 년의 여행을 거치면 이 지연은 측정할 수 있을 만큼 커진다.</p>
<p>검증 1은 지금까지 관측된 가장 밝은 감마선 폭발에서 이 지연을 찾았지만 아무것도 발견하지 못했다. 그러나 허점이 하나 남아 있었다. 시뮬레이션이 가능한 한 가장 큰 시간 간격으로 진행한다면, 격자의 대각선을 따라가는 빛은 전혀 늦어지지 않는다. 그래서 대각선 위에 놓인 천체 하나로는 아무 결론도 내릴 수 없었다.</p>
<p>여기서는 하늘의 서로 다른 방향에 있는 천체 [[n_src]]개를 한꺼번에 본다. 먼 별의 폭발 세 개, 매우 활발한 블랙홀을 품은 은하 네 개, 그리고 게 성운의 펄서이다. 각 천체에 대해 천문학자들이 이미 일정한 정밀도까지 지연이 나타나지 않음을 측정했다. 우리는 각 논문을 다시 읽고 모든 결과를 같은 규약으로 맞춘 뒤, 숨은 격자에 가장 유리한 격자 방향, 즉 한계를 가장 약하게 만드는 방향을 찾았다.</p>
<p>모든 천체를 동시에 대각선 위에 놓는 것은 불가능하다. 가장 유리한 방향에서도 세 천체는 대각선에서 충분히 멀리 떨어져 있어 지연이 나타났어야 했다. 따라서 칸의 크기가 [[a_exclue]]&nbsp;m 이상인 격자는 모든 방향에서 배제된다. 이 크기는 여전히 플랑크 길이의 약 [[planck_x]]배이므로, 훨씬 더 촘촘한 격자는 충분히 가능하다.</p>

<h2 id="analyse">상세 분석</h2>

<h3>1. 모형</h3>
<p>검증 1과 같이, 격자 간격이 \(a\)인 입방 격자 위의 맥스웰 방정식(Yee 기법)을 다루며, 시간 간격은 \(c\,\Delta t=\sigma a/\sqrt{3}\), \(0\le\sigma\le1\)이다. 주된 차수에서</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\,Q_{\mathrm{eff}}\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3},\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$
<p>\(1/3\le Q\le1\)이므로 \(Q_{\mathrm{eff}}\ge0\)이다. 광자는 언제나 느려지며, \(\sigma=1\)일 때 체대각선 위에서 정확히 \(Q_{\mathrm{eff}}=0\)이다. 최종 한계에서 20&nbsp;TeV 광자에 대해 \(aE/\hbar c\)&nbsp;=&nbsp;[[ae]]이므로 전개는 타당하다.</p>

<h3>2. 발표된 한계에서 격자 간격의 한계로</h3>
<p>여덟 편의 논문은 모두 이차 지연을 \(v/c\simeq1-\tfrac{3}{2}(E/E_{\mathrm{QG},2})^{2}\)로 기술하고, Jacob와 Piran의 거리 \(K_2=\int_0^{z}(1+z')^{2}\,dz'/H(z')\)를 쓴다. 두 식을 대응시키면</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}}\quad\Longrightarrow\quad a\sqrt{Q_{\mathrm{eff}}(\mathbf n_i)}\le B_i=\frac{\sqrt{12}\,\hbar c}{E_i}.$$
<p>미리 정한 규칙: 95% 한계, 광속보다 느린 경우, 비행시간, 각 논문에서 가장 덜 제약적인 방법. 각 한계는 \(E_i\sqrt{K_2^{\mathrm{LHAASO}}(z_i)/K_2^{(i)}(z_i)}\)로 LHAASO의 우주론 매개변수에 맞춰 환산하며, 이 인자는 [[fc_max]] 이하이다. 발표된 각 환산은 인쇄된 매개변수로부터 다시 계산했으며, 논문의 값을 재현한다(자체 테스트).</p>
<div class="tableau"><table>
<thead><tr><th>천체</th><th>관측 장비</th><th>\(z\) 또는 거리</th><th>발표된 \(E_{\mathrm{QG},2}\) (GeV)</th><th>공통 우주론 (GeV)</th><th>\(B_i\) (m)</th></tr></thead>
<tbody>
<tr><td>GRB 221009A</td><td>LHAASO</td><td>[[s0_z]]</td><td>[[s0_pub]]</td><td>[[s0_com]]</td><td>[[s0_b]]</td></tr>
<tr><td>GRB 190114C</td><td>MAGIC</td><td>[[s1_z]]</td><td>[[s1_pub]]</td><td>[[s1_com]]</td><td>[[s1_b]]</td></tr>
<tr><td>GRB 090510</td><td>Fermi-LAT</td><td>[[s2_z]]</td><td>[[s2_pub]]</td><td>[[s2_com]]</td><td>[[s2_b]]</td></tr>
<tr><td>Mrk 501</td><td>H.E.S.S.</td><td>[[s3_z]]</td><td>[[s3_pub]]</td><td>[[s3_com]]</td><td>[[s3_b]]</td></tr>
<tr><td>Mrk 421</td><td>MAGIC</td><td>[[s4_z]]</td><td>[[s4_pub]]</td><td>[[s4_com]]</td><td>[[s4_b]]</td></tr>
<tr><td>PKS 2155-304</td><td>H.E.S.S.</td><td>[[s5_z]]</td><td>[[s5_pub]]</td><td>[[s5_com]]</td><td>[[s5_b]]</td></tr>
<tr><td>PG 1553+113</td><td>H.E.S.S.</td><td>[[s6_z]]</td><td>[[s6_pub]]</td><td>[[s6_com]]</td><td>[[s6_b]]</td></tr>
<tr><td>게 성운(펄서)</td><td>MAGIC</td><td>[[s7_z]]&nbsp;kpc</td><td>[[s7_pub]]</td><td>[[s7_com]]</td><td>[[s7_b]]</td></tr>
</tbody>
</table></div>

<h3>3. 가장 불리한 방향</h3>
<p>격자의 방향 \(R\)에 대해 천체들은 함께 다음 한계를 준다.</p>
$$a\le A(R)=\min_i\frac{B_i}{\sqrt{Q_{\mathrm{eff}}(R\mathbf n_i)}},$$
<p>여기서 \(\sigma=1\)일 때 대각선 위에 있는 천체는 아무것도 제한하지 않는다. \(\max_R A(R)\)을 찾기 위해 균일하게 추출한 회전 [[n_orient]]개와 구성한 방향(각 천체를 대각선 위에 놓고 그 대각선을 축으로 회전시킨 것)을 조사한 뒤, 국소적으로 세밀화한다. 독립적인 두 번째 시드도 상대 차이 [[ecart_graines]] 이내에서 같은 최댓값을 준다. 최적화 과정은 알려진 경우로 검증했다. 천체 하나는 \(\sigma=1\)에서 아무것도 제한하지 않으며, 두 대각선 사이의 각만큼 떨어진 두 천체는 함께 대각선 위에 놓일 수 있다.</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>가장 불리한 방향 (m)</th><th>방향의 95% (m)</th></tr></thead>
<tbody>
<tr><td>0</td><td>[[pire0]]</td><td>[[q95_0]]</td></tr>
<tr><td>0.5</td><td>[[pire05]]</td><td>[[q95_05]]</td></tr>
<tr><td>0.9</td><td>[[pire09]]</td><td>[[q95_09]]</td></tr>
<tr><td>1</td><td>[[pire1]]</td><td>[[q95_1]]</td></tr>
</tbody>
</table></div>
<p>\(\sigma<1\)에서는 검증 1과 달라지는 것이 없다. GRB&nbsp;221009A가 지배적이며, 다른 천체들은 감도가 [[x_min]]~[[x_max]]배 낮다. 모든 것은 \(\sigma=1\)에서 결정된다. GRB&nbsp;221009A를 대각선 위에 놓는 것만으로는 더 이상 충분하지 않은데, 그러면 다른 천체들이 격자를 비스듬히 보게 되기 때문이다. 가장 불리한 절충에서는 GRB&nbsp;221009A가 가장 가까운 대각선에서 [[ang_grb]]° 벗어나며(\(Q_{\mathrm{eff}}\)&nbsp;=&nbsp;[[qeff_grb]]), 제약 [[n_actives]]개, 즉 GRB&nbsp;221009A, GRB&nbsp;090510, 게 성운이 균형을 이룬다. 이때 한계는 [[pire1]]&nbsp;m, 즉 에너지 척도 \(\hbar c/a\ge\)&nbsp;[[echelle]]&nbsp;GeV이다. \(A(R)\)은 모든 방향에서 \(\sigma\)에 따라 증가하므로, 이 한계는 모든 \(\sigma\le1\)에서 성립한다. \(\sigma=1\)에서 방향들의 중앙값은 [[med1]]&nbsp;m이다.</p>
<p>사각지대가 닫히는 것은 당연한 일이 아니었다. GRB&nbsp;190114C와 GRB&nbsp;090510은 [[ang_190_090]]° 떨어져 있어 두 대각선 사이의 각([[ang_diag]]°)에 가깝고, GRB&nbsp;090510과 PKS&nbsp;2155-304는 서로 [[ang_090_pks]]°밖에 떨어져 있지 않다. 사각지대를 닫는 것은 하늘의 나머지 부분에 있는 천체들의 다양성이다.</p>

<h3>4. 견고성</h3>
<p>\(\sigma=1\)에서 가장 불리한 방향의 한계는 선택에 따라 다음과 같다:</p>
<ul>
<li>GRB&nbsp;221009A 제외: [[v_sans_lhaaso]]&nbsp;m, 사각지대는 여전히 닫혀 있다;</li>
<li>우주론 환산 없이 발표된 한계 사용: [[v_sans_cosmo]]&nbsp;m;</li>
<li>천체 고유 효과를 포함한 Fermi 결과(논문의 표 V): [[v_fermi]]&nbsp;m;</li>
<li>감마선 폭발만: [[v_sursauts]]&nbsp;m;</li>
<li>블레이저와 펄서만: [[v_blazars]]&nbsp;m.</li>
</ul>

<h3>5. 비교</h3>
<p>모든 방향과 모든 시간 간격에 대해 성립하는 한계는 연속 시간에서의 검증 1 한계보다 [[x_test1]]배 약하다. Beane, Davoudi, Savage는 우주선 스펙트럼의 차단으로부터 \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m를 얻었다. 우리의 연속 시간 한계는 그들 값의 [[x_beane0]]배이고, 보편적 한계는 [[x_beane]]배이다.</p>

<h3>6. 한계</h3>
<ul>
<li>결합한 한계는 각 방향에 대해, 개별적으로 발표된 95% 한계 중 가장 엄격한 것을 취한다. 이는 결합 가능도가 아니며, 논문들도 그것을 발표하지 않았다. 가장 불리한 방향에서 세 한계가 작용하므로, 보장되는 포함 확률은 95%가 아니라 최소 [[couverture]]%이다.</li>
<li>각 논문은 천체 고유의 시간 어긋남이 지연을 상쇄하거나 흉내 내지 않는다고 가정한다.</li>
<li>Mrk&nbsp;421과 PG&nbsp;1553+113의 적색편이는 불확실하지만, 이 두 천체는 가장 불리한 방향에서 작용하지 않는다. 작용하는 게 성운의 거리는 MAGIC의 불확도에 포함되어 있다.</li>
<li>고차 기법(\(a^{4}\) 오차), 보상 항, 입방이 아니거나 팽창에 따라 늘어나는 격자는 이 한계를 벗어난다.</li>
<li>2차 분석이며, 광자는 전혀 재분석하지 않았다. 방향의 비율은 기하학적인 것이며, 우주에 대한 확률이 아니다.</li>
</ul>

<h3>7. 재현</h3>
<p>스크립트는 몇 초 만에 모든 것을 다시 수행하며, 먼저 자신의 공식과 발표된 각 환산을 검사한다. 모든 입력 수치의 출처는 쪽과 표까지 <code>sources.md</code>에 인용되어 있다.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-3/analyse.py" download>analyse.py</a>: 스크립트</li>
<li><a href="/fichiers/test-3/resultats.json" download>resultats.json</a>: 계산된 모든 값</li>
<li><a href="/fichiers/test-3/sources.md" download>sources.md</a>: 각 입력 수치의 인용</li>
</ul>

<h2 id="sources">출처</h2>
<ol class="sources">
<li>LHAASO Collaboration, GRB 221009A, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a>, 표 I.</li>
<li>MAGIC Collaboration, GRB 190114C, <a href="https://arxiv.org/abs/2001.09728v4">arXiv:2001.09728v4</a>, 표 I.</li>
<li>Fermi-LAT Collaboration, GRB 090510, <a href="https://arxiv.org/abs/1305.3463v1">arXiv:1305.3463v1</a>, 표 IV 및 표 V.</li>
<li>H.E.S.S. Collaboration, Mrk 501, <a href="https://arxiv.org/abs/1901.05209v1">arXiv:1901.05209v1</a>.</li>
<li>MAGIC Collaboration, Mrk 421, <a href="https://arxiv.org/abs/2406.07140v1">arXiv:2406.07140v1</a>, 표 2.</li>
<li>H.E.S.S. Collaboration, PKS 2155-304, <a href="https://arxiv.org/abs/1101.3650v2">arXiv:1101.3650v2</a>.</li>
<li>H.E.S.S. Collaboration, PG 1553+113, <a href="https://arxiv.org/abs/1501.05087v1">arXiv:1501.05087v1</a>, 표 5.</li>
<li>MAGIC Collaboration, 게 성운 펄서, <a href="https://arxiv.org/abs/1709.00346v1">arXiv:1709.00346v1</a>, 표 6.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a>.</li>
<li>좌표: <a href="https://simbad.cds.unistra.fr/simbad/">SIMBAD</a>(CDS, 스트라스부르).</li>
</ol>
""",
}

ARTICLE_4 = {
    'titre': '양자 무작위성은 프로그램을 드러내는가?',
    'description': '양자 실험에서 얻은 수백만 개의 비트를, 시뮬레이션이 쓸 법한 '
                   '의사난수 생성기를 가려내는 검정들로 샅샅이 살핀다.',
    'date': '2026년 9월 28일',
    'corps': r"""
<section class="verdict-net">
<h2>판정</h2>
<p><strong>아니다.</strong> 검정한 원시 양자 난수 비트에서는 의사난수 생성기의 징후가 전혀 나타나지 않는다. 반면 같은 검정은 대조군으로 쓴 단순한 생성기 네 개의 정체를 드러낸다. 처음부터 밝혀 둘 점이 있다. 분석 전에 정한 규칙은 공개된 그대로의 IBM 데이터에서 반응한다. 그러나 원인은 밝혀져 있다. 아홉 대의 기계 중 한 대가 여러 측정 계열 내내 0이나 1에 고정된 채 멈춰 있었으며, 이 결함에는 생성기의 구조가 없다. 이 기계를 제외하기로 한 것은 데이터를 본 뒤의 결정이며, 우리는 이 점을 그대로 밝혀 둔다.</p>
<p>이 ‘아니다’가 미치는 범위는 제한적이다. 이것이 배제하는 것은 양자 측정 결과를 단순한 생성기에서 뽑아 쓰는 시뮬레이션이지, 암호학적 품질의 생성기를 쓰는 시뮬레이션이 아니다. 그런 생성기는 원리상 진짜 무작위와 구별할 수 없다.</p>
</section>

<h2 id="explication">설명</h2>
<p>세계가 시뮬레이션이라면, 양자 측정을 할 때마다 그 결과인 0 또는 1을 만들어 내야 한다. 물리학에 따르면 이 결과는 본질적으로 예측할 수 없다. 그런데 컴퓨터는 진짜 우연을 만들 줄 모른다. 계산 절차, 말하자면 레시피에 따라 우연을 만들어 낼 뿐이다. 계산을 아끼는 시뮬레이션이라면 빠르고 단순한 레시피를 쓸 것이고, 단순한 레시피는 흔적을 남긴다. 반복, 숨은 규칙성, 계산으로 찾아낼 수 있는 구조 같은 것이다.</p>
<p>그래서 우리는 실제 양자 실험에서 나와 연구자들이 직접 공개한 0과 1의 수열을 가져와, 그 안에서 이런 흔적을 찾았다. 첫 번째 어려움이 있다. 공개된 양자 난수 공급원 대부분은 결과를 공개하기 전에 수학적 ‘믹서’에 통과시킨다. 이 믹서는 모든 구조를 지우도록 설계되어 있으므로, 그 출력을 검정해서는 원래의 공급원에 대해 아무것도 알 수 없다. 우리는 이 데이터도 검정해 보았지만, 판정에는 반영하지 않았다.</p>
<p>남는 것은 원시 공급원 두 가지이다. 하나는 미국 오리건주 포틀랜드 대학교의 얽힌 광자 장치로, 비트를 있는 그대로 공개한다. 다른 하나는 IBM의 양자 컴퓨터 아홉 대로, 큐비트 하나로 동전 던지기를 하라는 요청을 수백만 번 받았다. 광자는 모든 검정을 통과한다. IBM의 기계들은 0을 약간 지나치게 많이 내놓는데, 이는 데이터를 만든 저자들이 설명한 알려진 결함이며, 이 불균형을 보정하면 통과한다. 그중 한 대인 Belem은 여러 측정 계열 내내 멈춘 채 굳어 있었다. 이는 고장이지, 계산 레시피가 아니다.</p>
<p>비교용으로 쓴 생성기들은 예상대로 반응한다. 단순한 레시피는 정체가 드러난다. NIST의 공식 검정 모음은 통과하는, 매우 널리 쓰이는 생성기도 예외가 아니다. 반면 정교한 레시피는 드러나지 않으며, 완전히 계산할 수 있는 2의 제곱근의 숫자들도 마찬가지이다. 바로 여기에 이 검증의 한계가 있다. 공들여 만든 시뮬레이션이라면 이런 종류의 흔적을 전혀 남기지 않을 것이다.</p>

<h2 id="analyse">상세 분석</h2>

<h3>1. 무엇을 검정할 수 있는가</h3>
<p>통계적 검정이 알려 주는 것은 비트 수열이 마지막으로 거친 처리에 관한 것뿐이다. 암호학적 함수로 해시 처리된 출력은 입력이 무엇이든 완벽한 무작위처럼 보인다. 우리는 모두 [[bits_total]]비트를 검정했으며, 그중 원시 비트는 [[bits_bruts]]비트이다:</p>
<div class="tableau"><table>
<thead><tr><th>데이터</th><th>기원</th><th>처리</th><th>비트 수</th></tr></thead>
<tbody>
<tr><td>parity</td><td>편광 얽힘 광자(Kavulich 외, 2021)</td><td>없음</td><td>[[n_parity]]</td></tr>
<tr><td>ibm</td><td>큐비트 하나, 아다마르 게이트, 측정; 기계 아홉 대(Root와 Becker, 2024)</td><td>없음</td><td>[[n_ibm]]</td></tr>
<tr><td>anu</td><td>진공 요동, ANU</td><td>AES-128</td><td>[[n_anu]]</td></tr>
<tr><td>beacon</td><td>NIST Beacon 2.0</td><td>SHA-512</td><td>[[n_beacon]]</td></tr>
</tbody>
</table></div>
<p>양자 무작위성의 본질에 대해 알려 주는 것은 parity와 ibm뿐이다. NIST가 2015년에 수행한 허점 없는 벨 검증의 원시 데이터는 채택하지 않았다. 이 실험에서 측정 설정의 선택은 물리적 공급원과 의사난수 공급원을 결합한 것이고, 검출 결과는 균일한 비트가 아니기 때문이다. Beacon의 경우, 공개된 커밋먼트 연쇄를 연속한 펄스 쌍 [[engagements]]개에 대해 확인했다.</p>

<h3>2. 1단계: NIST SP 800-22 검정 모음</h3>
<p>공식 검정 모음의 15개 검정을 모두 새로 구현했으며, 이 구현은 문서 부록 B의 p값 [[annexe_n]]개를 [[annexe_ecart]] 이내의 차이로 재현한다(한 검정은 [[annexe_ecart_chev]]). 데이터는 10<sup>6</sup>비트짜리 수열 [[n_seq]]개로 나눈다. p값 [[np1]]개는 하나의 검정군을 이루며, 전체 유의수준 1%에서 홀름 방법으로 보정한다.</p>
<ul>
<li>parity: p값 [[par_np1]]개, 기각 없음(가장 작은 보정 p값: [[par_p1]]). 1인 비트의 비율: [[par_frac]].</li>
<li>anu와 beacon: 기각 없음(anu의 가장 작은 보정 p값: [[anu_p1]]).</li>
<li>ibm: [[ibm_np1]]개 중 [[ibm_rej1]]개 기각. 1인 비트의 비율: [[ibm_frac]], 즉 표준편차의 [[ibm_z]]배만큼 벗어남. Belem 기계를 빼면, 일정한 편향을 정확히 제거하는 폰 노이만 추출기를 거친 뒤 [[vn_bits]]비트가 남고, p값 [[vn_np]]개 중 기각은 하나도 없다([[vn_p]]). 실패는 데이터 저자들이 기술한 편향에서 비롯된다.</li>
</ul>

<h3>3. 2단계: 생성기의 징후</h3>
<p>NIST 검정 모음은 수열이 이상적인 무작위에서 벗어나는지는 알려 주지만, 왜 벗어나는지는 알려 주지 않는다. 다음 세 검정은 알고리즘 생성기에 고유한 결함을 겨냥한다:</p>
<ul>
<li><strong>선형 복잡도.</strong> 벌레캄프-매시 알고리즘은 \(n\)비트 구간을 재현하는 가장 짧은 선형 되먹임 시프트 레지스터의 길이 \(L\)을 준다. 무작위 수열에서는 \(L\simeq n/2\)이다. 상태가 \(n/2\)비트보다 작은 \(\mathrm{GF}(2)\) 위의 선형 생성기에서는 언제나 \(L\lt n/2\)이다. 구간은 [[seg_bm]]비트 길이이며, 연속으로 읽거나 48비트마다 1비트, 64비트마다 1비트씩 솎아 읽는다. 이렇게 해서 [[etat_max]]비트까지의 상태를 다룰 수 있다.</li>
<li><strong>반복.</strong> 64비트 창 하나하나를 다른 모든 창과 비교한다. 똑같은 쌍의 기대 개수는 [[rep_attendu]] 정도이다. 반복이 단 한 번이라도 나타나면 주기나 재사용된 시드를 뜻할 것이다.</li>
<li><strong>장거리 상관.</strong> 지연 17부터 [[lag_max]]까지의 자기상관을 본페로니 보정과 함께 조사한다.</li>
</ul>
<p>주 검정군(p값 [[np2]]개, 유의수준 1%의 홀름 방법): parity에서는 기각이 없다([[par_p2]]). \(L\)과 \(n/2\)의 최대 차이는 [[par_ecart_l]]이고, 반복은 없으며, 장거리 상관은 [[par_auto]]이다. anu와 beacon에서도 기각이 없다. ibm에서는 기각이 [[ibm_rej2]]번 나온다.</p>

<h3>4. IBM의 기각: 멈춰 버린 기계 한 대</h3>
<p>IBM 데이터는 8192샷으로 이루어진 시행 [[ibm_essais]]회로 구성된다. 그중 [[ibm_const]]회는 완전히 일정하고(전부 0인 것이 [[ibm_const0]]회, 전부 1인 것이 [[ibm_const1]]회), 다른 [[ibm_quasi]]회는 99% 넘게 일정하다. 이들은 모두 Belem 기계에서 나왔다. 똑같은 창의 쌍 [[ibm_paires]]개는 모두 같은 비트만 이어진 창끼리의 쌍이며, 구성이 평범한 창들 가운데 똑같은 쌍은 [[ibm_paires_typ]]개이다. 굳어 버린 출력은 의사난수 생성기의 출력이 아니다. 출력이 없는 것이다.</p>
<p>Belem을 제외하기로 한 것은 데이터를 본 뒤의 결정이다. 따라서 이는 자체 홀름 보정을 적용한 부차 분석이며, 처음 규칙에 따른 결과도 그대로 공개되어 있다. 나머지 기계 여덟 대([[sb_bits]]비트)에서 2단계는 아무것도 기각하지 않는다(p값 [[sb_np2]]개, 가장 작은 보정 p값 [[sb_p2]]). \(L\)과 \(n/2\)의 최대 차이는 [[sb_ecart_l]]이고, 반복은 하나도 없다. 지연 1에서는 상관이 있다([[sb_r1]], 즉 표준편차의 [[sb_z1]]배). 이는 짧은 범위의 측정 결함으로, 생성기의 구조와는 관계가 없다. 1단계는 편향 때문에 여기서 [[sb_np1]]개 중 [[sb_rej1]]개를 기각한다.</p>

<h3>5. 대조군</h3>
<p>같은 처리 과정을 알려진 각 생성기의 [[bits_ctrl]]비트에 적용한다. 대조군 중 하나라도 예상대로 움직이지 않으면 스크립트는 멈춘다.</p>
<div class="tableau"><table>
<thead><tr><th>생성기</th><th>예상</th><th>결과(가장 작은 보정 p값, 1단계와 2단계)</th></tr></thead>
<tbody>
<tr><td>차수 20의 LFSR</td><td>검출</td><td>검출: \(L\)&nbsp;=&nbsp;[[l20_lmin]], 반복</td></tr>
<tr><td>차수 31의 LFSR</td><td>검출</td><td>검출: \(L\)&nbsp;=&nbsp;[[l31_lmin]], \(\log_{10}p\)&nbsp;=&nbsp;[[l31_log10p]]</td></tr>
<tr><td>32비트 LCG</td><td>검출</td><td>검출: 스펙트럼 검정, 장거리 상관</td></tr>
<tr><td>Mersenne Twister</td><td>검출</td><td>2단계에서만 검출: \(L\)&nbsp;=&nbsp;[[mt_lmin]], \(\log_{10}p\)&nbsp;=&nbsp;[[mt_log10p]]; NIST 검정 모음은 반응 없음([[mt_p1]])</td></tr>
<tr><td>PCG64</td><td>검출되지 않음</td><td>없음([[pcg_p1]]; [[pcg_p2]])</td></tr>
<tr><td>카운터 모드의 SHA-256</td><td>검출되지 않음</td><td>없음([[sha_p1]]; [[sha_p2]])</td></tr>
<tr><td>\(\sqrt{2}\)의 이진 전개 숫자</td><td>검출되지 않음</td><td>없음([[r2_p1]]; [[r2_p2]])</td></tr>
</tbody>
</table></div>
<p>Mersenne Twister는 2단계가 공식 검정 모음에 실질적인 민감도를 더해 준다는 것을 보여 준다. PCG64, SHA-256, \(\sqrt{2}\)는 완전히 결정론적인 수열도 검출 가능한 징후를 전혀 갖지 않을 수 있음을 보여 준다.</p>

<h3>6. 한계</h3>
<ul>
<li>암호학적 품질의 생성기는 진짜 무작위와 구별할 수 없다. 이 검증이 배제하는 것은 단순한 생성기를 쓰는 시뮬레이션이지, 공들여 만든 시뮬레이션이 아니다. SP 800-22 문서 자체도, 어떤 검정 모음으로도 암호 분석을 대신할 수 없다고 밝히고 있다.</li>
<li>2단계의 적용 범위: 선형 생성기는 상태가 [[etat_max]]비트보다 작을 때만 검출되고, 반복은 주기가 데이터보다 짧을 때만 검출된다.</li>
<li>원시 데이터의 양이 많지 않으며, 두 원시 공급원 모두 허점 없는 벨 검증으로 인증된 것이 아니다.</li>
<li>Belem 기계의 제외는 사후 결정이다. 그 원인은 기록되어 있으며, 제외하기 전의 결과도 공개했다.</li>
<li>ANU와 Beacon 데이터가 측정하는 것은 AES-128과 SHA-512의 품질뿐이다.</li>
</ul>

<h3>7. 재현</h3>
<p>데이터는 <code>telecharger.py</code>가 다시 내려받으며, 이때 지문을 확인한다. 그다음 <code>analyse.py</code>가 네트워크 없이 실행되며, 자체 테스트를 포함해 2분이 채 걸리지 않는다.</p>
<pre><code>python3 telecharger.py
python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-4/analyse.py" download>analyse.py</a>: 분석</li>
<li><a href="/fichiers/test-4/telecharger.py" download>telecharger.py</a>: 검증을 거친 데이터 내려받기</li>
<li><a href="/fichiers/test-4/resultats.json" download>resultats.json</a>: 계산된 모든 값</li>
<li><a href="/fichiers/test-4/sources.md" download>sources.md</a>: 각 주장의 인용</li>
</ul>

<h2 id="sources">출처</h2>
<ol class="sources">
<li>J. T. Kavulich, B. P. Van Deren, M. Schlosshauer, <cite>Searching for evidence of algorithmic randomness and incomputability in the output of quantum random number generators</cite>, Physics Letters A 388, 127032(2021), <a href="https://arxiv.org/abs/2101.01238">arXiv:2101.01238</a>; 데이터: <a href="https://zenodo.org/records/4440318">Zenodo 4440318</a>.</li>
<li>B. P. Van Deren, J. T. Kavulich, M. Schlosshauer, <cite>Parity-based, bias-free optical quantum random number generation with min-entropy estimation</cite>, <a href="https://arxiv.org/abs/2006.11425">arXiv:2006.11425</a>.</li>
<li>O. Root, M. Becker, <cite>Does True Randomness Exist? Efficacy Testing IBM Quantum Computers via Statistical Randomness</cite>, <a href="https://arxiv.org/abs/2401.12250">arXiv:2401.12250</a>; 데이터: <a href="https://doi.org/10.5281/zenodo.10542216">DOI 10.5281/zenodo.10542216</a>.</li>
<li>J. Y. Haw et al., <cite>Maximization of Extractable Randomness in a Quantum Random-Number Generator</cite>, <a href="https://arxiv.org/abs/1411.4512">arXiv:1411.4512</a>.</li>
<li>NIST, <cite>A Reference for Randomness Beacons: Format and Protocol Version 2</cite>, <a href="https://csrc.nist.gov/pubs/ir/8213/ipd">NISTIR 8213</a>.</li>
<li>L. K. Shalm et al., <cite>A strong loophole-free test of local realism</cite>, <a href="https://arxiv.org/abs/1511.03189">arXiv:1511.03189</a>.</li>
<li>NIST, <cite>A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications</cite>, <a href="https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final">SP 800-22 Rev. 1a</a>.</li>
</ol>
""",
}
