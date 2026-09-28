"""Deutsch: Übersetzung der französischen Quelle (fr.py).

Jeder Platzhalter [[name]] wird durch eine Zahl aus resultats.json ersetzt, geschrieben
nach den Konventionen der Sprache. Die Formeln $$…$$ und \\(…\\) sind in allen Sprachen
identisch. Rohstring (r\"\"\"…\"\"\") erforderlich wegen der Backslashes.
"""
NOM = 'Deutsch'
HTML_LANG = 'de'
HREFLANG = 'de'
DIR = 'ltr'
LOCALE_OG = 'de_DE'
DECIMALE = ','

UI = {
    'devise': 'Forschung zur Simulationstheorie.',
    'description_site': 'aeternam — Forschung zur Simulationstheorie',
    'travaux': 'Arbeiten',
    'langue': 'Sprache',
    'surtitre': 'Forschung · Test Nr. 1',
    'meta': 'Version 2 · reproduzierbare Sekundäranalyse',
    'fichier_pdf': 'aeternam-test-1-de.pdf',
}

ARTICLE = {
    'titre': 'Ein kubisches Gitter, geprüft an GRB 221009A',
    'description': 'Was die von LHAASO beobachteten Photonen dem Gitterabstand eines diskreten Raums auferlegen '
                   'und wo diese Einschränkung endet.',
    'date': '28. September 2026',
    'corps': r"""
<section class="resume">
<h2>Kurz gefasst</h2>
<ul>
<li><strong>Wäre der Raum ein kubisches Gitter</strong>, auf dem sich Licht wie in einer numerischen Simulation der Maxwell-Gleichungen ausbreitet, kämen die energiereichsten Photonen verspätet an. Beim Gammablitz GRB&nbsp;221009A beobachtet LHAASO keine derartige Verzögerung.</li>
<li><strong>Der Gitterabstand liegt daher unter [[a_resume]]&nbsp;m</strong> bei der konservativsten Methode und der ungünstigsten Orientierung oder unter [[a_ml_resume]]&nbsp;m bei der Likelihood-Methode. Die Energieskala des Gitters liegt über [[echelle_resume]]&nbsp;GeV.</li>
<li><strong>Das ist kein Neuland.</strong> Beane, Davoudi und Savage erhielten bereits 2012 aus der kosmischen Strahlung dieselbe Größenordnung (etwa [[b_beane]]&nbsp;m). Das vorliegende Ergebnis bestätigt dies unabhängig, anhand einer anderen Observablen.</li>
<li><strong>Neu: Der Zeitschritt zählt.</strong> Ist auch die Zeit in Schritte zerlegt, wie in jeder numerischen Simulation, wird der Effekt kleiner. Beim größten stabilen Zeitschritt erfährt das Licht entlang der acht Diagonalrichtungen des Würfels überhaupt keine Dispersion mehr: Ein einzelner Gammablitz erlaubt dann keine universelle Schranke. Für 95&nbsp;% der Orientierungen bleibt der Gitterabstand unter [[a95_sigma1]]&nbsp;m.</li>
<li><strong>Ein Gitter, dessen führender Fehlerterm linear in <em>a</em> wäre</strong>, ist ausgeschlossen, bis hinab zu [[a_lineaire]]&nbsp;m, einem Zehntel der Planck-Länge.</li>
<li><strong>Ein Gitterabstand von der Größe der Planck-Länge bleibt außer Reichweite</strong>: Sein Effekt wäre für diesen Test etwa um den Faktor [[facteur_planck]] zu schwach.</li>
<li><strong>Bei der Überprüfung der Literatur</strong> sind wir in einem Artikel von 2025 (Xi und Shu) auf eine inkonsistente Umrechnung gestoßen: Die dort angegebene quadratische Schranke scheint um einen Faktor [[xs_facteur]] überschätzt zu sein.</li>
<li><strong>Kein Nachweis, keine Wahrscheinlichkeit, simuliert zu sein.</strong> Der Test setzt einer genau bestimmten Architektur Schranken; über die Existenz eines Simulators sagt er nichts aus.</li>
</ul>
</section>

<h2 id="question">1. Die geprüfte Frage</h2>
<p>Eine numerische Simulation stellt den Raum durch endlich viele Punkte dar. Eine Welle, die sich darin ausbreitet, verhält sich nicht genau wie im Kontinuum: Ihre Geschwindigkeit hängt geringfügig von ihrer Wellenlänge ab. Für Licht hinge die Geschwindigkeit also von der Energie der Photonen ab. Der Effekt ist winzig, summiert sich aber über kosmologische Entfernungen auf.</p>
<p>GRB&nbsp;221009A ist der hellste jemals aufgezeichnete Gammablitz. Das Observatorium LHAASO hat von ihm Photonen oberhalb von 10&nbsp;TeV nachgewiesen, die sich vor etwa zwei Milliarden Jahren auf den Weg gemacht haben (Rotverschiebung <em>z</em>&nbsp;=&nbsp;[[z]]). Hinge die Lichtgeschwindigkeit von der Energie ab, kämen die hochenergetischen Photonen nach den niederenergetischen an. Die LHAASO-Kollaboration hat nach dieser Verzögerung gesucht und sie nicht gefunden.</p>
<p>Die Frage ist also präzise: <em>Welchen Gitterabstand lässt diese Verzögerung von null noch zu?</em> Sie setzt weder voraus, dass jede Simulation ein Gitter verwenden würde, noch dass ein Gitter eine Simulation beweisen würde.</p>

<h2 id="modele">2. Das Modell: Maxwell auf einem Gitter</h2>
<p>Die elektromagnetischen Felder werden auf einem kubischen Gitter mit Gitterabstand <em>a</em> angeordnet, genau wie im Yee-Verfahren (1966), das in numerischen Simulationen der Maxwell-Gleichungen verwendet wird, oder wie in der Hamilton-Formulierung der Elektrodynamik auf dem Gitter (Kogut und Susskind, 1975). Die Zeit verläuft entweder kontinuierlich oder in Schritten \(\Delta t\). Eine ebene Welle mit Wellenvektor \(\mathbf k\) und Kreisfrequenz \(\omega\) erfüllt dann die Dispersionsrelation:</p>
$$\left(\frac{2}{c\,\Delta t}\right)^{2}\sin^{2}\frac{\omega\,\Delta t}{2}=\left(\frac{2}{a}\right)^{2}\sum_{i=1}^{3}\sin^{2}\frac{k_i a}{2}.$$
<p>Das Verfahren ist nur stabil, wenn \(c\,\Delta t\le a/\sqrt{3}\). Man schreibt daher \(c\,\Delta t=\sigma a/\sqrt{3}\) mit einer Courant-Zahl \(0\le\sigma\le1\); \(\sigma=0\) entspricht kontinuierlicher Zeit. Für Photonen, deren Wellenlänge sehr groß gegenüber dem Gitterabstand ist, lautet die Gruppengeschwindigkeit mit \(E=\hbar\omega\):</p>
$$\frac{v(E)}{c}\simeq1-\frac{1}{8}\left(Q-\frac{\sigma^{2}}{3}\right)\left(\frac{aE}{\hbar c}\right)^{2},\qquad Q=\sum_{i=1}^{3}n_i^{4}\in\left[\tfrac{1}{3},\,1\right].$$
<p>\(Q\) hängt von der Richtung \(\mathbf n\) des Photons relativ zu den Gitterachsen ab: \(Q=1\) entlang einer Achse, \(Q=1/3\) entlang einer Raumdiagonale. Für das Folgende sind drei Eigenschaften wichtig:</p>
<ul>
<li>der Effekt ist <strong>quadratisch</strong>: Ein zehnmal kleinerer Gitterabstand erzeugt einen hundertmal schwächeren Effekt;</li>
<li>die Photonen werden <strong>verlangsamt</strong>, nie beschleunigt, solange das Verfahren stabil ist;</li>
<li>beide Polarisationen breiten sich gleich aus: <strong>keine Doppelbrechung</strong>, sodass die sehr strengen Schranken aus Polarisationsmessungen hier nicht greifen.</li>
</ul>

<h2 id="lhaaso">3. Der Abgleich mit LHAASO</h2>
<p>LHAASO beschreibt eine quadratische Verzögerung durch \(v/c\simeq1-\tfrac{3}{2}\,(E/E_{\mathrm{QG},2})^{2}\) und veröffentlicht Intervalle für \(\eta_2=10^{-15}\,E_{\mathrm{Pl}}^{2}/E_{\mathrm{QG},2}^{2}\) mit \(E_{\mathrm{Pl}}\)&nbsp;=&nbsp;[[epl]]&nbsp;GeV (Gleichungen 2, 3 und 5 des Artikels). Koeffizientenvergleich liefert:</p>
$$E_{\mathrm{QG},2}=\frac{\sqrt{12}\,\hbar c}{a\sqrt{Q_{\mathrm{eff}}}},\qquad\eta_2=10^{-15}\,\frac{E_{\mathrm{Pl}}^{2}\,Q_{\mathrm{eff}}\,a^{2}}{12\,(\hbar c)^{2}},\qquad Q_{\mathrm{eff}}=Q-\frac{\sigma^{2}}{3}.$$
<p>Die akkumulierte Verzögerung zwischen zwei Photonen der Energien \(E_h\) und \(E_l\) lautet</p>
$$\Delta t=\frac{Q_{\mathrm{eff}}\,a^{2}\,(E_h^{2}-E_l^{2})}{8\,(\hbar c)^{2}}\,I_2(z),\qquad I_n(z)=\int_0^{z}\frac{(1+z')^{n}}{H(z')}\,dz',$$
<p>mit der Kosmologie von LHAASO (<em>H</em><sub>0</sub>&nbsp;=&nbsp;[[h0]]&nbsp;km/s/Mpc, Ω<sub>m</sub>&nbsp;=&nbsp;[[om]], Ω<sub>Λ</sub>&nbsp;=&nbsp;[[ol]]), die <em>I</em><sub>2</sub>&nbsp;=&nbsp;[[i2]]&nbsp;s ergibt. Die Messung schränkt nur die Kombination \(a\sqrt{Q_{\mathrm{eff}}}\) ein. Tabelle I von LHAASO liefert folgende Intervalle (95&nbsp;%):</p>
<div class="tableau"><table>
<thead><tr><th>Methode</th><th>Untere Grenze</th><th>Best-Fit-Wert</th><th>Obere Grenze</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_bas]]</td><td>[[ccf_bf]]</td><td>[[ccf_haut]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_bas]]</td><td>[[min_bf]]</td><td>[[min_haut]]</td></tr>
<tr><td>ML (kalibriert)</td><td>[[cal_bas]]</td><td>—</td><td>[[cal_haut]]</td></tr>
</tbody>
</table></div>
<p>Die Null liegt in allen drei Intervallen: Es wird keine Verzögerung nachgewiesen. Die drei Methoden analysieren denselben Gammablitz; wir kombinieren sie nicht. Eine obere Grenze \(U\) für \(\eta_2\) ergibt</p>
$$a\sqrt{Q_{\mathrm{eff}}}\le\frac{\hbar c}{E_{\mathrm{Pl}}}\sqrt{12\times10^{15}\,U}.$$
<p>Bei kontinuierlicher Zeit erhält man:</p>
<div class="tableau"><table>
<thead><tr><th>Methode</th><th>\(a\sqrt{Q}\) (m)</th><th>\(a\), ungünstigste Orientierung (m)</th><th>\(a\), 95&nbsp;% der Orientierungen (m)</th><th>\(\hbar c/a\) (GeV)</th></tr></thead>
<tbody>
<tr><td>CCF</td><td>[[ccf_arq]]</td><td>[[ccf_pire]]</td><td>[[ccf_95]]</td><td>&gt;&nbsp;[[ccf_ech]]</td></tr>
<tr><td>ML (MINOS)</td><td>[[min_arq]]</td><td>[[min_pire]]</td><td>[[min_95]]</td><td>&gt;&nbsp;[[min_ech]]</td></tr>
<tr><td>ML (kalibriert)</td><td>[[cal_arq]]</td><td>[[cal_pire]]</td><td>[[cal_95]]</td><td>&gt;&nbsp;[[cal_ech]]</td></tr>
</tbody>
</table></div>
<p>Die Kurzfassung übernimmt den konservativsten Wert, [[a_resume]]&nbsp;m: Das ist eine Einhüllende zu Darstellungszwecken, kein neues Intervall. An dieser Grenze käme ein Photon von 1&nbsp;TeV höchstens [[retard_limite]]&nbsp;s nach einem Photon von [[e_bas]]&nbsp;TeV an.</p>
<p>Einige Vorhersagen, die keine Messungen sind (Photon von 1&nbsp;TeV im Vergleich zu einem Photon von [[e_bas]]&nbsp;TeV):</p>
<div class="tableau"><table>
<thead><tr><th>Gitterabstand</th><th>Vorhergesagtes \(\eta_2\)</th><th>Vorhergesagte Verzögerung</th><th>Befund</th></tr></thead>
<tbody>
<tr><td>10<sup>−26</sup>&nbsp;m</td><td>[[p26_eta_min]] bis [[p26_eta_max]]</td><td>[[p26_ret_min]] bis [[p26_ret_max]]&nbsp;s</td><td>für jede Orientierung ausgeschlossen</td></tr>
<tr><td>10<sup>−27</sup>&nbsp;m</td><td>[[p27_eta_min]] bis [[p27_eta_max]]</td><td>[[p27_ret_min]] bis [[p27_ret_max]]&nbsp;s</td><td>nahe den Achsen (\(Q>\)&nbsp;[[q_cal_axe]]) nur durch die kalibrierte Methode ausgeschlossen</td></tr>
<tr><td>10<sup>−28</sup>&nbsp;m</td><td>[[p28_eta_min]] bis [[p28_eta_max]]</td><td>[[p28_ret_min]] bis [[p28_ret_max]]&nbsp;ms</td><td>nicht ausgeschlossen</td></tr>
<tr><td>[[lpl]]&nbsp;m (Planck)</td><td>[[pl_eta_min]] bis [[pl_eta_max]]</td><td>[[pl_ret_min]] bis [[pl_ret_max]]&nbsp;s</td><td>außer Reichweite</td></tr>
</tbody>
</table></div>

<h2 id="robustesse">4. Wie weit die Schranke trägt</h2>
<h3>Die Orientierung des Gitters</h3>
<p>Man weiß nicht, wie das Gitter relativ zur Richtung des Gammablitzes orientiert wäre. Die Hauptschranke legt den ungünstigsten Fall zugrunde, \(Q=1/3\). Für eine Million gleichmäßig verteilter Richtungen hat \(Q\) den Median [[q_mediane]] und übersteigt in 95&nbsp;% der Fälle den Wert [[q_5]]: Die Schranke verschiebt sich nur wenig, mit [[ccf_95]]&nbsp;m für 95&nbsp;% der Orientierungen und [[ccf_mediane]]&nbsp;m für die mediane Orientierung. Diese Anteile sind geometrischer Natur: Es sind keine Wahrscheinlichkeitsaussagen über das Universum.</p>
<h3>Diskrete Zeit, der Schwachpunkt der Schranke</h3>
<p>Eine Simulation schreitet in Zeitschritten voran. Die Diskretisierung der Zeit erzeugt einen Fehler mit entgegengesetztem Vorzeichen, der den räumlichen Fehler teilweise ausgleicht (der Term \(-\sigma^{2}/3\)). Für die konservative Methode:</p>
<div class="tableau"><table>
<thead><tr><th>\(\sigma\)</th><th>\(c\,\Delta t/a\)</th><th>Ungünstigste Orientierung</th><th>95&nbsp;% der Orientierungen</th><th>Mediane Orientierung</th></tr></thead>
<tbody>
<tr><td>0 (kontinuierliche Zeit)</td><td>0</td><td>[[s0_pire]]&nbsp;m</td><td>[[s0_95]]&nbsp;m</td><td>[[s0_med]]&nbsp;m</td></tr>
<tr><td>[[s1_sigma]]</td><td>[[s1_cdt]]</td><td>[[s1_pire]]&nbsp;m</td><td>[[s1_95]]&nbsp;m</td><td>[[s1_med]]&nbsp;m</td></tr>
<tr><td>[[s2_sigma]]</td><td>[[s2_cdt]]</td><td>[[s2_pire]]&nbsp;m</td><td>[[s2_95]]&nbsp;m</td><td>[[s2_med]]&nbsp;m</td></tr>
<tr><td>[[s3_sigma]]</td><td>[[s3_cdt]]</td><td>[[s3_pire]]&nbsp;m</td><td>[[s3_95]]&nbsp;m</td><td>[[s3_med]]&nbsp;m</td></tr>
<tr><td>1 (maximaler Schritt)</td><td>[[s4_cdt]]</td><td>keine Schranke</td><td>[[s4_95]]&nbsp;m</td><td>[[s4_med]]&nbsp;m</td></tr>
</tbody>
</table></div>
<p>Beim größten stabilen Zeitschritt ist die Kompensation entlang der Raumdiagonalen exakt, und zwar nicht nur in erster Ordnung: Die Dispersionsrelation liefert dort für jede Wellenlänge wieder \(\omega=ck\). Eine so eingestellte Simulation entginge diesem Test vollständig, wenn der Gammablitz in einer ihrer acht Diagonalrichtungen läge. Das ist die wichtigste Einschränkung einer Schranke, die aus einer einzigen Quelle gewonnen wird; mehrere Quellen in verschiedenen Richtungen würden sie aufheben, denn diese können, außer durch Zufall, nicht alle auf Diagonalen liegen.</p>
<h3>Fester oder mit der Expansion gedehnter Gitterabstand</h3>
<p>Wir nehmen einen festen physikalischen Gitterabstand an. Dehnte sich das Gitter mit dem Universum (mitbewegter Gitterabstand), wüchse der Effekt nicht mehr mit der Rotverschiebung, und \(I_2\) würde durch \(I_0\) ersetzt: Die Schranke schwächt sich um einen Faktor \(\sqrt{I_2/I_0}\)&nbsp;=&nbsp;[[comobile_facteur]] ab, auf [[comobile_a]]&nbsp;m. Bei <em>z</em>&nbsp;=&nbsp;[[z]] fällt diese Wahl kaum ins Gewicht.</p>
<h3>Genauere Verfahren</h3>
<p>Ein Simulator kann ein Verfahren höherer Ordnung verwenden, dessen führender Fehlerterm wie \(a^{4}\) skaliert. Der Effekt wird dann quartisch in der Energie und die Schranke für \(a\) viel schwächer. LHAASO veröffentlicht für diesen Gammablitz keine Schranke dieser Art; sie zu beziffern, würde die Daten der einzelnen Photonen erfordern. Terme, die zur Kompensation der Dispersion konstruiert sind, entgingen der Schranke ebenfalls. Das sind andere Modelle, die gesondert zu prüfen sind.</p>
<h3>Und wenn der Fehler linear wäre?</h3>
<p>Ein symmetrisches Gitter erzeugt keinen in \(a\) linearen Effekt. Eine Diskretisierung, die durch Brechen der Symmetrie zwischen entgegengesetzten Ausbreitungsrichtungen einen solchen Effekt erzeugte, fiele unter die lineare Schranke von LHAASO, \(E_{\mathrm{QG},1}>10\,E_{\mathrm{Pl}}\): Mit einem Koeffizienten der Ordnung eins gilt \(a<\hbar c/(10\,E_{\mathrm{Pl}})\)&nbsp;≈&nbsp;[[a_lineaire]]&nbsp;m, also ein Zehntel der Planck-Länge. Jedes gröbere Gitter dieser Art ist ausgeschlossen.</p>
<h3>Gültigkeit der Rechnung</h3>
<p>Die Reihenentwicklung setzt \(aE/\hbar c\ll1\) voraus. An der Schranke gilt selbst für Photonen von 20&nbsp;TeV \(aE/\hbar c\)&nbsp;≈&nbsp;[[validite]]. Wir haben die Entwicklung außerdem mit der exakten Dispersionsrelation verglichen: Für \(ak\)&nbsp;=&nbsp;[[ak_test]] übersteigt die relative Abweichung [[ecart_dispersion]] nicht, wie erwartet.</p>

<h2 id="contexte">5. Was das Ergebnis im Vergleich zum Bestehenden wert ist</h2>
<p>Beane, Davoudi und Savage (2012) untersuchten eine Simulation der Gitter-Quantenchromodynamik. Aus dem Abbruch des Spektrums der kosmischen Strahlung leiteten sie für den inversen Gitterabstand die Schranke \(1/b\gtrsim10^{11}\)&nbsp;GeV ab, also \(b\lesssim\)&nbsp;[[b_beane]]&nbsp;m. Das Verhältnis unserer konservativen Schranke zu ihrer beträgt [[beane_ratio]]; mit den Likelihood-Methoden von LHAASO sind es [[beane_ml_min]] bis [[beane_ml_max]]. Beide Ansätze stimmen also in der Größenordnung überein, bei unterschiedlichen Observablen, Teilchen und Annahmen: Das ist eine Bestätigung, kein Rekord.</p>
<p>Die Planck-Länge, [[lpl]]&nbsp;m, liegt acht Größenordnungen tiefer. Für einen Gitterabstand dieser Größe wäre der Effekt um den Faktor [[facteur_planck_exact]] schwächer als die Grenze. Da er mit dem Quadrat der Energie wächst, bräuchte man etwa hundert Millionen Mal energiereichere Photonen, weit jenseits von allem Beobachteten: In dieser Ordnung kann kein Laufzeittest ein Gitter auf der Planck-Skala erreichen.</p>

<h2 id="xi-shu">6. Eine Überprüfung der Literatur: Xi und Shu (2025)</h2>
<p>Xi und Shu haben denselben Gammablitz mit einer anderen Methode analysiert und geben \(E_{\mathrm{QG},2}>\)&nbsp;[[xs_eqg_imprime]]&nbsp;GeV an (ihre Tabelle III), etwa das [[xs_rapport_lhaaso]]-Fache der Schranke von LHAASO. Ausgehend von ihren eigenen Definitionen finden wir diesen Wert nicht wieder.</p>
<ul>
<li>Gleichung (3) der Autoren setzt die Verzögerung proportional zu \((E/E_{\mathrm{QG},n})^{n}\) an. Für \(n=1\) ist ihre Umrechnung (6), \(\varepsilon_{\mathrm{QG},1}\simeq C_1/\theta_1\) mit \(C_1\)&nbsp;=&nbsp;[[xs_c1_imprime]], konsistent: Wir erhalten [[xs_c1]].</li>
<li>Für \(n=2\) behält ihre Gleichung (7), \(\varepsilon_{\mathrm{QG},2}\simeq C_2/\theta_2\) mit \(C_2\)&nbsp;=&nbsp;[[xs_c2_imprime]], die \(1/\theta\)-Form bei. Auf ihre Grenze \(\theta_2\)&nbsp;=&nbsp;[[xs_theta]]&nbsp;s/TeV² angewandt, reproduziert sie tatsächlich den Wert ihrer Tabelle ([[xs_eq7]]&nbsp;GeV). Da die Verzögerung aber quadratisch ist, verlangt ihre Gleichung (3) eine \(1/\sqrt{\theta_2}\)-Abhängigkeit: \(\varepsilon_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_c2]]\(/\sqrt{\theta_2}\), also \(E_{\mathrm{QG},2}\simeq\)&nbsp;[[xs_eqg]]&nbsp;GeV.</li>
<li>Die Abweichung beträgt einen Faktor [[xs_facteur]]. Eine plausible Erklärung: \(\varepsilon^{2}\theta_2\) beträgt [[xs_eps2]], und [[xs_c2_imprime]] sieht aus wie die Wurzel aus [[xs_eps2_imprime]], allein aus der Zehnerpotenz gezogen.</li>
</ul>
<p>Status: mutmaßliche Inkonsistenz in Version 1 des Artikels, noch mit den Autoren zu bestätigen. Wir analysieren ihre Daten nicht neu und beurteilen ihre übrigen Ergebnisse nicht. Korrigiert wäre ihre Schranke immer noch um den Faktor [[xs_vs_lhaaso]] stärker als die von LHAASO. Wir verwenden sie nicht.</p>

<h2 id="limites">7. Was dieser Test nicht aussagt</h2>
<ul>
<li>Er weist nichts nach: Eine Verzögerung von null bleibt mit allen Messungen vereinbar.</li>
<li>Er berechnet keine Wahrscheinlichkeit dafür, dass wir uns in einer Simulation befinden; die Angabe „95&nbsp;%“ bezieht sich auf einen physikalischen Parameter.</li>
<li>Er setzt einer genau bestimmten Architektur Schranken: kubisches Gitter, Yee-Verfahren, fester Gitterabstand, keine Kompensation.</li>
<li>Selbst eine nachgewiesene Verzögerung würde nicht auf einen Computer hindeuten: Eine grundlegend diskrete Physik oder andere Effekte der Quantengravitation würden dasselbe Signal erzeugen.</li>
<li>Die Intervalle von LHAASO beruhen auf Annahmen über die Emission der Quelle; diese übernehmen wir.</li>
</ul>

<h2 id="suite">8. Nächste Schritte</h2>
<ol>
<li>Mehrere Quellen aus verschiedenen Richtungen kombinieren, um den toten Winkel der Diagonalen zu schließen.</li>
<li>Verfahren höherer Ordnung beziffern (Effekt der Ordnung \(a^{4}\)), was die Daten der einzelnen Photonen erfordert.</li>
<li>Xi und Shu bitten, ihre Umrechnung zu klären.</li>
<li>Den Test auf andere Signaturen eines Gitters ausweiten: Anisotropie der kosmischen Strahlung, geladene Teilchen.</li>
</ol>

<h2 id="reproduire">9. Reproduzieren</h2>
<p>Alles wird von einem Python-Skript ohne Abhängigkeiten neu berechnet, das zuerst seine eigenen Formeln prüft: Reihenentwicklung gegen exakte Dispersion, exakter Diagonalfall, Hin- und Rückumrechnungen, kosmologisches Integral, Mittelwert von \(Q\) gleich 3/5.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-1/analyse.py" download>analyse.py</a>: das Skript (Python&nbsp;3.10 oder neuer, Standardbibliothek; Kommentare im Code auf Französisch)</li>
<li><a href="/fichiers/test-1/resultats.json" download>resultats.json</a>: alle berechneten Werte</li>
<li><a href="[[pdf]]" download>[[pdf]]</a>: diese Notiz als PDF</li>
</ul>
<p>Eine unabhängige Gegenprüfung (numpy, scipy) findet das kosmologische Integral bis auf 10<sup>−15</sup> genau wieder, ebenso die Orientierungsquantile über zehn Millionen Zufallsziehungen und die Gruppengeschwindigkeit durch numerisches Lösen der Dispersionsrelation.</p>
<p>Diese Notiz ersetzt eine erste Fassung vom 28. September 2026. Sie ergänzt die diskrete Zeit, die Orientierung, den mitbewegten Gitterabstand, den linearen Effekt und den Vergleich mit Beane et al.</p>

<h2 id="sources">Quellen</h2>
<ol class="sources">
<li>LHAASO Collaboration, <cite>Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A</cite>, <a href="https://arxiv.org/abs/2402.06009v3">arXiv:2402.06009v3</a> (überarbeitete Fassung vom 13. Februar 2026): Gleichungen 2, 3 und 5, Tabelle I.</li>
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Y. Xi, F.-W. Shu, <cite>Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method</cite>, <a href="https://arxiv.org/abs/2508.00656v1">arXiv:2508.00656v1</a> (2025): Gleichungen 3, 6 und 7, Tabellen I und III.</li>
<li>K. S. Yee, <cite>Numerical solution of initial boundary value problems involving Maxwell’s equations in isotropic media</cite>, IEEE Transactions on Antennas and Propagation 14, 302 (1966).</li>
<li>J. Kogut, L. Susskind, <cite>Hamiltonian formulation of Wilson’s lattice gauge theories</cite>, Physical Review D 11, 395 (1975).</li>
<li>A. Taflove, S. C. Hagness, <cite>Computational Electrodynamics: The Finite-Difference Time-Domain Method</cite>, Artech House: numerische Dispersion und Stabilität des Yee-Verfahrens.</li>
<li>NIST, <a href="https://physics.nist.gov/cuu/Constants/">CODATA 2022</a>: Fundamentalkonstanten.</li>
</ol>
""",
}
