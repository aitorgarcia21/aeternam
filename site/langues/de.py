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
    'verdict': 'Urteil bis heute: keine Spur einer Simulation in den untersuchten Daten.',
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

ARTICLE_2 = {
    'titre': 'Zeichnen die kosmischen Strahlen ein Gitter?',
    'description': 'Die energiereichsten Teilchen, die das Pierre-Auger-Observatorium je registriert hat, '
                   'geprüft auf die Spur, die ein kubisches Gitter bei ihnen hinterlassen müsste.',
    'date': '28. September 2026',
    'corps': r"""
<section class="verdict-net">
<h2>Urteil</h2>
<p><strong>Nein.</strong> Die [[n_evt]] energiereichsten kosmischen Strahlen, die das Pierre-Auger-Observatorium gemessen hat, zeigen keinerlei Würfelsymmetrie. Ein Himmel ganz ohne Gitter erzeugt in [[p4_pct]]&nbsp;% der Fälle ein mindestens ebenso deutliches Muster wie das beobachtete: Was wir sehen, ist gewöhnlicher Zufall.</p>
<p>Dieses „Nein“ hat eine begrenzte Reichweite: Mit [[n_evt]] Teilchen konnte nur ein sehr deutliches Muster sichtbar werden. Ein schwächeres Muster bleibt möglich.</p>
</section>

<h2 id="explication">Erklärung</h2>
<p>Würde unsere Welt von einem Computer berechnet, wäre der Raum vielleicht in winzige Würfel zerlegt, so wie ein Bild aus Pixeln besteht. 2012 wiesen drei Physiker darauf hin, dass eine solche Zerlegung eine Spur hinterließe: Die schnellsten Teilchen des Universums kämen nicht aus allen Richtungen gleich an. Manche Richtungen wären bevorzugt, angeordnet wie die Flächen oder Ecken eines Würfels.</p>
<p>Solche Teilchen gibt es: die kosmische Strahlung, Atomkerne aus dem All mit weit mehr Energie, als unsere Beschleuniger erzeugen. In Argentinien hält das Pierre-Auger-Observatorium mit einem riesigen Netz von Detektoren nach ihnen Ausschau. Es hat die Liste seiner [[n_evt]] energiereichsten Treffer aus den Jahren 2004 bis 2020 veröffentlicht, samt der Richtung, aus der jeder kam.</p>
<p>Wir haben diese [[n_evt]] Richtungen genommen und geprüft, ob sie sich entlang eines Würfels anordnen. Da niemand weiß, wie ein solcher Würfel gedreht wäre, haben wir [[n_orient]] Stellungen ausprobiert. Die beste passt ein wenig zu den Daten. Doch wer so viele Stellungen ausprobiert, findet immer eine, die ein wenig passt, selbst an einem rein zufälligen Himmel.</p>
<p>Um das zu entscheiden, haben wir [[n_ciels]] falsche Himmel zufällig erzeugt, gesehen vom selben Observatorium, und auf jedem genau dieselbe Suche durchgeführt. In [[p4_pct]]&nbsp;% davon passt ein Würfel mindestens ebenso gut. Der echte Himmel ist also nichts Besonderes. Für einen Hinweis hätte er fast alle falschen Himmel übertreffen müssen.</p>
<p>Fazit: keine Spur eines Gitters. Diese Suche konnte aber nur ein starkes Muster sehen: Mit nur [[n_evt]] Teilchen bliebe ein schwaches unbemerkt. Außerdem lenken die Magnetfelder unserer Galaxie diese Teilchen unterwegs ab, was einen Teil des Musters verwischen würde. Dieser Test beweist also nicht, dass der Raum kontinuierlich ist; er zeigt, dass dort, wo wir hinschauen konnten, nichts ist.</p>

<h2 id="analyse">Ausführliche Analyse</h2>

<h3>1. Vom Gitter zu einer prüfbaren Vorhersage</h3>
<p>Auf einem kubischen Gitter mit Gitterabstand \(a\) ersetzt der diskrete Laplace-Operator \(k^{2}\) durch \((2/a)^{2}\sum_i\sin^{2}(k_i a/2)\). Für ein freies Feld gilt</p>
$$\omega^{2}=c^{2}k^{2}\left[1-\frac{(ka)^{2}}{12}\,Q(\mathbf n)+O\!\left((ka)^{4}\right)\right],\qquad Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4},$$
<p>wobei \(\mathbf n\) die Ausbreitungsrichtung in den Gitterachsen ist. Es ist dieselbe Funktion \(Q\) wie in Test Nr.&nbsp;1. Allgemeiner ist jede Wirkung des Gitters auf die Ankunftsrichtungen (Ausbreitung, richtungsabhängiger Abbruch des Spektrums) eine unter der Würfelgruppe \(O_h\) invariante Funktion von \(\mathbf n\). Unter \(O_h\) invariante Kugelflächenfunktionen gibt es aber nur für \(\ell=0,4,6,8,\dots\): Die erste erlaubte Anisotropie ist die kubische Harmonische \(\ell=4\), proportional zu \(Q-3/5\). Das ist unser Haupttest, festgelegt vor dem Öffnen der Daten; \(\ell=6\) wird als zweiter geprüft. Beane, Davoudi und Savage schreiben, die Simulation „könnte sich in den Verteilungen der kosmischen Strahlung höchster Energie zeigen, durch einen Grad an Brechung der Rotationssymmetrie, der die Struktur des zugrunde liegenden Gitters widerspiegelt“.</p>

<h3>2. Die Daten</h3>
<p>Katalog des Pierre-Auger-Observatoriums (ApJS 264, 50, 2023): die [[n_evt]] Luftschauer höchster Energie, aufgezeichnet vom 1.&nbsp;Januar 2004 bis 31.&nbsp;Dezember 2020, von [[e_min]] bis [[e_max]]&nbsp;EeV, mit Zenitwinkeln bis [[zmax]]°. Die offene Datei enthält zudem [[n_calib]] hybride Kalibrierereignisse außerhalb der [[n_evt]]: Wir verwerfen sie. Wir verwenden die vom Oberflächendetektor rekonstruierte Rektaszension und Deklination. Der SHA-256-Fingerabdruck der Datei wird bei jedem Lauf geprüft. Bei diesen Energien ist die Nachweiseffizienz bis [[zmax]]° vollständig, die Exposition also rein geometrisch.</p>

<h3>3. Die Exposition des Detektors</h3>
<p>Ein Bodendetektor auf der geografischen Breite \(a_0\)&nbsp;=&nbsp;[[lat]]°, der Zenitwinkel \(\theta\le\theta_m\)&nbsp;=&nbsp;[[zmax]]° akzeptiert, hat eine in Rektaszension gleichförmige Exposition und in Deklination \(\delta\) (Sommers, 2001):</p>
$$\omega(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$
<p>Der sichtbare Himmel endet bei \(\delta\)&nbsp;=&nbsp;[[dec_max]]°, also bei [[ciel_pct]]&nbsp;% der Sphäre. Ein isotroper Himmel, von Auger gesehen, ist daher nicht gleichförmig: Alles Folgende vergleicht die Daten mit diesem Himmel, nicht mit einer gleichförmigen Sphäre.</p>

<h3>4. Die Teststatistik</h3>
<p>Sei \(R\) eine Orientierung des Gitters mit Zeilen \(\mathbf e_k\) und \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). Für die \(N\) beobachteten Richtungen:</p>
$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-N\,\langle f\rangle_\omega}{\sqrt{N\,\mathrm{Var}_\omega f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$
<p>wobei \(\langle\cdot\rangle_\omega\) der Mittelwert über einen mit der Exposition gewichteten isotropen Himmel ist. \(T>0\) zeigt einen Überschuss entlang der Würfelachsen an, \(T<0\) entlang seiner Diagonalen; der Betrag deckt beides ab. Da \(f\) ein Polynom vom Grad 4 ist, hängt \(T(R)\) von den Daten nur über die 15 Momente \(\sum_i\mathbf n_i^{\alpha}\) ab; Mittelwert und Varianz werden exakt per Gauß-Legendre-Quadratur berechnet. Das Maximum läuft über [[n_orient]] gleichverteilt gezogene Orientierungen (Haar-Maß). Für \(\ell=6\) nehmen wir \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\) mit \(\alpha\)&nbsp;=&nbsp;[[alpha6]] (also \(-15/11\)), was sie orthogonal zu \(\ell=4\) macht; der kombinierte Test maximiert \(T_4^{2}+T_6^{2}\).</p>

<h3>5. Den Zufall kalibrieren</h3>
<p>Die beste von [[n_orient]] Orientierungen zu suchen, bläht \(Z_4\) zwangsläufig auf: Es folgt keiner Normalverteilung. Wir ziehen daher [[n_ciels]] isotrope Himmel mit \(N\) Ereignissen gemäß der Exposition und wenden genau dieselbe Maximierung auf sie an. Unter der Hypothese „kein Gitter“ hat \(Z_4\) den Median [[z4_50]]; es übersteigt [[z4_95]] in 5&nbsp;% der Fälle, [[z4_99]] in 1&nbsp;% und [[z4_999]] in 0,1&nbsp;%. Der p-Wert, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), enthält so den Preis für die Wahl der Orientierung.</p>

<h3>6. Ergebnis</h3>
<div class="tableau"><table>
<thead><tr><th>Test</th><th>Beobachtete Statistik</th><th>p-Wert</th></tr></thead>
<tbody>
<tr><td>\(\ell=4\) (Haupttest)</td><td>\(Z_4\)&nbsp;=&nbsp;[[z4]]</td><td>[[p4]]</td></tr>
<tr><td>\(\ell=6\)</td><td>\(Z_6\)&nbsp;=&nbsp;[[z6]]</td><td>[[p6]]</td></tr>
<tr><td>\(\ell=4\) und \(\ell=6\)</td><td>\(\max(T_4^{2}+T_6^{2})\)&nbsp;=&nbsp;[[z46]]</td><td>[[p46]]</td></tr>
</tbody>
</table></div>
<p>In der besten Orientierung beträgt der Mittelwert von \(Q\) [[q_obs]] gegenüber erwarteten [[q_iso]], ein Überschuss von [[q_ecart_pct]]&nbsp;% zu den Achsen hin. Das ist nicht signifikant: \(p\)&nbsp;=&nbsp;[[p4]] für den Haupttest, und kein Nebentest fällt unter 0,05. Die Daten sind mit dem Fehlen jeder kubischen Symmetrie vereinbar.</p>

<h3>7. Was der Test sehen konnte</h3>
<p>Um die Empfindlichkeit zu beziffern, wird ein kubisches Muster injiziert: Dichte proportional zu \(\omega(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Mit \(\varepsilon>0\) beträgt der Fluss entlang der Achsen das \(1+\varepsilon\)-Fache des Mittels; mit \(\varepsilon<0\) verlagert sich der Überschuss auf die Diagonalen. Für jedes \(\varepsilon\) liefern [[n_ciels_signal]] Himmel mit zufälliger Orientierung die Verteilung von \(Z_4\). Obere Grenze bei 95&nbsp;%: \(\varepsilon\le\)&nbsp;[[eps_axes]] zu den Achsen und \(\lvert\varepsilon\rvert\le\)&nbsp;[[eps_diag]] zu den Diagonalen. Anders gesagt: Ein Überschuss von bis zu etwa [[eps_axes_pct]]&nbsp;% entlang der Achsen (oder [[eps_diag_pct]]&nbsp;% entlang der Diagonalen) ist nicht ausgeschlossen – eine schwache Einschränkung, bedingt durch die geringe Zahl der Ereignisse.</p>
<p>Das Skript prüft zuerst seine eigene Kette: Invarianz von \(Q\) unter der Würfelgruppe, exakte Polynomentwicklung, Exposition null jenseits von [[dec_max]]°, \(T\) unter Isotropie zentriert und normiert, Orthogonalität von \(\ell=6\) zu \(\ell=4\) sowie Nachweis eines deutlich injizierten Musters, dessen Orientierung auf [[ecart_orient]]° genau wiedergefunden wird.</p>

<h3>8. Grenzen</h3>
<ul>
<li>Kosmische Strahlen sind geladen: Galaktische und extragalaktische Magnetfelder lenken ihre Richtungen ab, umso stärker, je schwerer die Kerne sind. Das gesuchte Muster ist breit (eine Achse und eine Diagonale liegen [[angle_diag]]° auseinander) und übersteht mäßige Ablenkungen, doch eine an der Quelle oder während der Ausbreitung geprägte Spur würde teilweise gelöscht.</li>
<li>Wir nehmen das Gitter als fest gegenüber den fernen Sternen an (äquatoriale Koordinaten). Ein ihnen gegenüber bewegtes oder rotierendes Gitter erforderte einen anderen Test.</li>
<li>[[n_evt]] Ereignisse und [[ciel_pct]]&nbsp;% des Himmels: Die statistische Aussagekraft ist gering, wie die obige Grenze zeigt.</li>
<li>Echte astrophysikalische Anisotropien können eine \(\ell=4\)-Komponente enthalten. Ein positives Ergebnis hätte verlangt, sie auszuschließen; ein Nullergebnis hängt nicht von ihnen ab.</li>
<li>Es wird keine Wahrscheinlichkeit berechnet, simuliert zu sein: Der Test betrifft eine bestimmte Signatur, die eines kubischen Gitters.</li>
</ul>

<h3>9. Nachrechnen</h3>
<p>Ein Python-Skript (numpy) rechnet alles in etwa einer Minute nach: Einlesen und Prüfen der Daten, Selbsttests, Statistik, simulierte Himmel, obere Grenze. Der Zufallsgenerator hat einen festen Startwert: Die Ergebnisse sind von Lauf zu Lauf identisch.</p>
<pre><code>python3 analyse.py --out resultats.json</code></pre>
<ul>
<li><a href="/fichiers/test-2/analyse.py" download>analyse.py</a>: das Skript</li>
<li><a href="/fichiers/test-2/resultats.json" download>resultats.json</a>: alle berechneten Werte</li>
<li><a href="/fichiers/test-2/donnees/auger_catalogSD.csv" download>auger_catalogSD.csv</a>: die Daten des Pierre-Auger-Observatoriums (Lizenz CC BY-SA 4.0)</li>
</ul>

<h2 id="sources">Quellen</h2>
<ol class="sources">
<li>S. R. Beane, Z. Davoudi, M. J. Savage, <cite>Constraints on the Universe as a Numerical Simulation</cite>, <a href="https://arxiv.org/abs/1210.1847">arXiv:1210.1847</a> (2012).</li>
<li>Pierre Auger Collaboration, <cite>A Catalog of the Highest-Energy Cosmic Rays Recorded During Phase I of Operation of the Pierre Auger Observatory</cite>, ApJS 264, 50 (2023), <a href="https://arxiv.org/abs/2211.16020">arXiv:2211.16020</a>.</li>
<li>Pierre Auger Collaboration, <cite>Auger Open Data</cite>, release 3, <a href="https://doi.org/10.5281/zenodo.10488964">DOI 10.5281/zenodo.10488964</a>; Nachweiseffizienz: <a href="https://opendata.auger.org/data.php">opendata.auger.org</a>.</li>
<li>P. Sommers, <cite>Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory</cite>, Astroparticle Physics 14, 271 (2001), <a href="https://arxiv.org/abs/astro-ph/0004016">arXiv:astro-ph/0004016</a>.</li>
</ol>
""",
}
