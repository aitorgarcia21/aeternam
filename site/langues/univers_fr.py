"""Textes du parcours cosmologique. Les dates sont des repères, pas une échelle linéaire."""

SOURCES = {
    'questions': ('ESA · Les questions ouvertes', 'https://www.esa.int/Science_Exploration/Space_Science/Planck/Key_questions'),
    'inflation': ('ESA · Inflation et fond cosmologique', 'https://www.esa.int/Science_Exploration/Space_Science/Planck/The_cosmic_microwave_background_and_inflation'),
    'composition': ('CERN · Quarks, noyaux et atomes', 'https://alicepublic.web.cern.ch/physics-primer'),
    'cern': ('CERN · L’Univers primordial', 'https://home.cern/fr/science/physics/early-universe/'),
    'noyaux': ('NASA · Le Big Bang', 'https://science.nasa.gov/mission/hubble/science/science-behind-the-discoveries/hubble-big-bang/'),
    'histoire': ('NASA · L’histoire cosmique', 'https://science.nasa.gov/universe/overview/'),
    'etoiles': ('NASA · Les premières étoiles et galaxies', 'https://science.nasa.gov/mission/webb/early-universe/'),
    'soleil': ('NASA · Formation du Système solaire', 'https://science.nasa.gov/astrobiology/learning-resources/alp/how-did-our-solar-system-form/'),
    'energie': ('NASA · L’énergie noire', 'https://science.nasa.gov/dark-energy/'),
    'temps': ('Einstein Online · Les horloges en mouvement', 'https://www.einstein-online.info/en/spotlight/light-clocks-time-dilation/'),
    'gravite': ('Einstein Online · Gravité et courbure', 'https://www.einstein-online.info/en/spotlight/geometry_force/'),
    'schwarzschild': ('Université de Groningue · Géométrie de Schwarzschild', 'https://www.astro.rug.nl/~weygaert/tim1publication/cosmo2007/werkcollege1.pdf'),
    'horizon': ('NASA · Anatomie d’un trou noir', 'https://science.nasa.gov/universe/black-holes/anatomy/'),
    'rebond': ('Einstein Online · L’hypothèse d’un rebond', 'https://www.einstein-online.info/en/spotlight/avoiding_the_big_bang/'),
    'sans-bord': ('Hartle et Hawking · Proposition sans bord', 'https://doi.org/10.1103/PhysRevD.28.2960'),
}

ETAPES = [
    {
        'id': 'debut', 'titre': 'Le début reste une question.',
        'date': 'Aux limites de nos connaissances', 'repere': 'Début',
        'resume': 'Nous savons décrire l’Univers primordial, mais pas son origine ultime.',
        'texte': [
            'En remontant le temps, l’Univers observable était plus chaud et plus dense. Nos modèles décrivent très bien une grande partie de cette histoire.',
            'Mais ils ne nous disent pas encore si le temps a eu un commencement, ni ce qui aurait précédé cette phase. Le Big Bang décrit l’évolution depuis un état primordial chaud et dense ; il ne prouve pas une création à partir de rien.',
        ],
        'source': 'questions', 'legende': 'Limite de nos modèles · schéma conceptuel',
        'detail': 'La singularité obtenue en prolongeant certains modèles classiques jusqu’à leur limite ne constitue pas une observation. Elle indique que cette description ne suffit plus. Une théorie testée de la gravité quantique manque encore.',
    },
    {
        'id': 'inflation', 'titre': 'Une expansion fulgurante ?',
        'date': 'Avant la phase chaude · scénario inflationnaire', 'repere': 'Inflation',
        'resume': 'L’espace aurait grandi très vite : c’est l’hypothèse de l’inflation.',
        'texte': [
            'Une hypothèse propose une très brève accélération de l’expansion : l’inflation. De minuscules fluctuations auraient été étirées à des échelles immenses.',
            'À sa fin, l’énergie responsable de cette phase aurait alimenté un Univers chaud de particules. Ce scénario explique plusieurs observations, mais son mécanisme physique n’est pas établi.',
        ],
        'source': 'inflation', 'legende': 'Distances qui augmentent · illustration de l’hypothèse',
        'detail': 'L’inflation est une famille de modèles. Ses dates, sa durée et le réchauffement qui lui succède dépendent du modèle. On ne lui attribue donc pas ici un instant exact. L’expansion de l’espace ne correspond pas à un objet dépassant localement la lumière.',
    },
    {
        'id': 'particules', 'titre': 'Un Univers de particules.',
        'date': 'Premières fractions de seconde de la phase chaude', 'repere': 'Particules',
        'resume': 'L’Univers est encore trop chaud pour que des atomes se forment.',
        'texte': [
            'La température est trop élevée pour former des atomes. Particules, antiparticules et rayonnement interagissent dans un milieu extrêmement dense.',
            'Les quarks et les gluons ne sont pas encore confinés dans des protons et des neutrons. En s’étendant, l’Univers se refroidit.',
        ],
        'source': 'cern', 'legende': 'Milieu chaud et dense · particules schématiques',
        'detail': 'Les collisions d’ions lourds étudient en laboratoire un plasma de quarks et de gluons. Elles ne recréent ni un Univers entier ni toutes les conditions cosmologiques initiales. Le dessin montre seulement des exemples de quarks up, de quarks down et de gluons. Ni leur proportion, ni leur taille, ni leur position ne sont mesurées ; les couleurs ne représentent pas la charge de couleur.',
    },
    {
        'id': 'protons', 'titre': 'Les quarks se regroupent.',
        'date': 'Quelques millionièmes de seconde', 'repere': 'Protons',
        'resume': 'En refroidissant, les quarks s’assemblent en protons et en neutrons.',
        'texte': [
            'En refroidissant, le milieu permet aux quarks de former des protons et des neutrons. Ces particules deviendront les constituants des noyaux.',
            'Il reste aussi un petit excès de matière sur l’antimatière. L’origine précise de ce déséquilibre est une question ouverte.',
        ],
        'source': 'composition', 'legende': 'Quarks de valence · schéma sans échelle',
        'detail': 'Le schéma montre les quarks de valence : deux up et un down pour un proton, un up et deux down pour un neutron. Gluons et paires quark-antiquark ne sont pas représentés. Les couleurs servent uniquement à distinguer up et down, pas leurs charges de couleur. Les cercles ne sont ni une surface ni une mesure de taille. Le passage du plasma aux hadrons et l’origine de l’asymétrie matière-antimatière sont deux questions différentes.',
    },
    {
        'id': 'noyaux', 'titre': 'Les premiers noyaux.',
        'date': 'Premières minutes', 'repere': 'Noyaux',
        'resume': 'Protons et neutrons s’assemblent pour former des noyaux légers, notamment d’hélium.',
        'texte': [
            'Des protons et des neutrons s’assemblent. Cette nucléosynthèse primordiale produit notamment des noyaux d’hélium, avec du deutérium et des traces de lithium.',
            'La matière ordinaire reste surtout constituée d’hydrogène et d’hélium. Les électrons sont encore libres : un noyau n’est pas encore un atome neutre.',
        ],
        'source': 'noyaux', 'legende': 'Noyaux légers · tailles et abondances schématiques',
        'detail': 'Le proton constitue le noyau de l’hydrogène ordinaire. Le noyau d’hélium 4 contient deux protons et deux neutrons ; le dessin montre leur composition, pas les abondances ni une réaction élémentaire unique. Les réactions des premières minutes fabriquent surtout de l’hélium à partir des nucléons disponibles. Les proportions des éléments légers sont l’un des tests du modèle du Big Bang chaud.',
    },
    {
        'id': 'plasma', 'titre': 'La lumière est piégée.',
        'date': 'Avant environ 380 000 ans', 'repere': 'Plasma',
        'resume': 'Les électrons libres dévient sans cesse la lumière : l’Univers est opaque.',
        'texte': [
            'L’Univers contient un plasma : noyaux, électrons libres et lumière. Les photons rencontrent sans cesse des électrons et changent de direction.',
            'Le milieu est opaque. Il contient déjà de la lumière, mais elle ne peut pas encore traverser librement de grandes distances.',
        ],
        'source': 'histoire', 'legende': 'Photons diffusés par les électrons libres',
        'detail': 'Les traits représentent des trajets de photons schématiques. Leur longueur, leur cadence et les distances entre les rencontres ne sont pas calculées à partir d’une densité réelle. La transparence s’installe progressivement.',
    },
    {
        'id': 'atomes', 'titre': 'La lumière se libère.',
        'date': 'Environ 380 000 ans', 'repere': 'Atomes',
        'resume': 'Les atomes se forment et la lumière peut enfin voyager librement.',
        'texte': [
            'En se refroidissant, les noyaux capturent des électrons. Les premiers atomes neutres se forment. La lumière peut enfin traverser de grandes distances.',
            'Cette lumière existe encore : c’est le fond diffus cosmologique, aujourd’hui étiré en micro-ondes par l’expansion.',
        ],
        'source': 'inflation', 'legende': 'Atomes neutres et lumière libérée · schéma',
        'detail': 'Recombinaison et découplage du rayonnement sont des processus liés, mais distincts. Les halos représentent des atomes de manière symbolique, pas des orbites d’électrons. Ce schéma n’est pas une carte mesurée du fond cosmologique.',
    },
    {
        'id': 'ages-sombres', 'titre': 'Un ciel sans étoiles.',
        'date': 'Après la recombinaison', 'repere': 'Âges sombres',
        'resume': 'La gravité rassemble le gaz, mais aucune étoile ne brille encore.',
        'texte': [
            'Le gaz est principalement neutre. Il n’existe pas encore d’étoiles pour l’éclairer. La lumière du fond cosmologique continue pourtant de traverser l’espace.',
            'La gravité amplifie les différences de densité : certaines régions accumulent davantage de matière. Les futurs foyers d’étoiles se préparent.',
        ],
        'source': 'histoire', 'legende': 'Le gaz se rassemble · contraste de densité exagéré',
        'detail': '« Sombre » ne signifie ni vide ni absence de photons. La matière noire participe à la croissance des structures par ses effets gravitationnels ; sa nature microscopique reste inconnue.',
    },
    {
        'id': 'etoiles', 'titre': 'Les premières étoiles.',
        'date': 'Premières centaines de millions d’années', 'repere': 'Étoiles',
        'resume': 'Le gaz s’effondre sous sa gravité, puis la fusion nucléaire allume les étoiles.',
        'texte': [
            'Des nuages de gaz s’effondrent sous leur propre gravité. Au cœur des premières étoiles, la fusion nucléaire commence.',
            'Leur rayonnement transforme le gaz environnant. La formation des étoiles et la réionisation sont progressives : il n’existe pas une seule date où tout l’Univers s’allume.',
        ],
        'source': 'etoiles', 'legende': 'Allumage progressif des étoiles · illustration',
        'detail': 'La date des toutes premières étoiles reste incertaine. Les observations des premières galaxies et les modèles contraignent cette époque sans fournir un film complet de sa naissance.',
    },
    {
        'id': 'galaxies', 'titre': 'Les galaxies se construisent.',
        'date': 'Du premier milliard d’années jusqu’à aujourd’hui', 'repere': 'Galaxies',
        'resume': 'Les galaxies grandissent, forment des étoiles et fusionnent entre elles.',
        'texte': [
            'Les étoiles se forment dans des galaxies qui grandissent, attirent du gaz et fusionnent. À grande échelle, la matière dessine un réseau de filaments et de vides.',
            'Les générations d’étoiles enrichissent le gaz en éléments plus lourds. C’est dans cette histoire que des planètes rocheuses deviennent possibles.',
        ],
        'source': 'etoiles', 'legende': 'Galaxies et filaments · organisation illustrative',
        'detail': 'La formation des premières galaxies chevauche celle des premières étoiles. Les galaxies dessinées ne sont pas un catalogue observé. Les différents éléments sont fabriqués par plusieurs processus stellaires et événements, pas tous par un même type de supernova.',
    },
    {
        'id': 'systeme-solaire', 'titre': 'Le Soleil et les planètes.',
        'date': 'Il y a environ 4,6 milliards d’années', 'repere': 'Soleil',
        'resume': 'Un nuage de gaz et de poussières donne naissance au Soleil et aux planètes.',
        'texte': [
            'Une région d’un nuage de gaz et de poussières s’effondre. Le Soleil se forme au centre d’un disque, où la matière s’assemble progressivement en planètes.',
            'La Terre vient de cette matière déjà transformée par l’histoire des étoiles. Le Système solaire n’est qu’une petite partie de la Voie lactée.',
        ],
        'source': 'soleil', 'legende': 'Système solaire · tailles, distances et vitesses non à l’échelle',
        'detail': 'Le disque dessiné représente du gaz et des poussières autour du jeune Soleil, où s’assemblent les futures planètes ; les anneaux servent à montrer son orientation, pas des orbites calculées. 4,6 milliards d’années est l’âge approximatif du Système solaire, pas le temps écoulé depuis le Big Bang. Avec un âge cosmologique de 13,8 milliards d’années, cela correspond à environ 9,2 milliards d’années après la phase initiale.',
    },
    {
        'id': 'aujourdhui', 'titre': 'L’expansion continue.',
        'date': 'Aujourd’hui · environ 13,8 milliards d’années', 'repere': 'Aujourd’hui',
        'resume': 'L’expansion accélère ; la nature de l’énergie noire reste inconnue.',
        'texte': [
            'L’Univers poursuit son expansion. À grande échelle, cette expansion accélère. Dans le modèle cosmologique standard, on décrit cette accélération par une composante appelée énergie noire.',
            'Sa nature reste inconnue. Les galaxies, les étoiles et les planètes continuent d’évoluer ; leur organisation locale dépend aussi de la gravité.',
        ],
        'source': 'energie', 'legende': 'Réseau cosmique · illustration, pas une carte observée',
        'detail': 'L’âge d’environ 13,8 milliards d’années est inféré des observations dans le cadre du modèle cosmologique standard. L’expansion ne signifie pas que les atomes, les planètes ou les systèmes gravitationnellement liés grandissent avec le facteur d’échelle.',
    },
]

EXPERIENCES = r"""
<section id="espace-temps" class="univ-laboratoire" aria-label="Espace et temps">
  <article class="univ-experience" id="evenements">
<h2>L’espace et le temps situent les événements.</h2>
<div class="univ-explication">
      <p>Un événement a un lieu et un instant : trois coordonnées d’espace, une de temps.</p>
      <details><summary>Analyse détaillée</summary><p>L’espace permet de dire <em>où</em> quelque chose se passe : trois directions suffisent pour repérer une position. Le temps permet de dire <em>quand</em>.</p>
      <p>Un événement est une position et un instant. L’ensemble forme l’espace-temps. Une horloge mesure la durée le long de son propre parcours, appelée <em>temps propre</em>.</p><p>Les trois axes représentent l’espace. La ligne sous le cube représente séparément le temps : ce dessin n’affiche pas quatre directions spatiales. Les unités spatiales sont arbitraires. Dans un autre référentiel, les coordonnées du même événement peuvent changer.</p></details>
    </div>
<div class="univ-manipulation"><figure class="univ-demonstration">
      <canvas id="espace-canvas" role="img" aria-label="Un événement repéré par trois coordonnées spatiales et un instant. Les curseurs déplacent le point et son repère temporel."></canvas>
      <figcaption id="evenement-valeur" aria-live="polite">Événement : (2 ; 1 ; 1), à 3 s</figcaption>
    </figure>
<div class="univ-controles coordonnees">
        <label for="coord-x">Position x <output id="val-x">2</output><input id="coord-x" type="range" min="-4" max="4" step="0.1" value="2"></label>
        <label for="coord-y">Position y <output id="val-y">1</output><input id="coord-y" type="range" min="-4" max="4" step="0.1" value="1"></label>
        <label for="coord-z">Position z <output id="val-z">1</output><input id="coord-z" type="range" min="-4" max="4" step="0.1" value="1"></label>
        <label for="coord-t">Instant t <output id="val-t">3 s</output><input id="coord-t" type="range" min="0" max="10" step="0.1" value="3"></label>
      </div>
</div>
</article>
  <article class="univ-experience" id="expansion">
<h2>C’est l’espace qui s’étend.</h2>
<div class="univ-explication">
      <p>À grande échelle, les galaxies s’éloignent avec l’expansion de l’espace.</p>
      <details><summary>Analyse détaillée</summary><p>À grande échelle, les distances entre les galaxies emportées par l’expansion augmentent. Le Big Bang n’est pas une bombe qui explose depuis un centre dans une pièce vide.</p>
      <p>Dans ce schéma, les repères s’écartent ensemble. Les galaxies gardent leur taille : un système lié ne suit pas simplement l’expansion cosmique.</p><p>Pour des repères comobiles, la distance propre vaut d(t) = a(t) × χ, où χ est la distance comobile constante. La lumière est elle aussi étirée : sa longueur d’onde est proportionnelle à a. Le centre du dessin est seulement un choix de coordonnées, pas le centre de l’Univers. Ce curseur ne résout pas les équations de l’expansion.</p><p><a href="https://science.nasa.gov/universe/overview/">NASA · Expansion cosmique</a></p></details>
    </div>
<div class="univ-manipulation"><figure class="univ-demonstration"><canvas id="expansion-canvas" role="img" aria-label="Des galaxies s’écartent sur une grille qui s’étend, tandis que leur taille reste constante."></canvas><figcaption>Une portion d’espace · distances relatives</figcaption></figure>
<div class="univ-controles"><label for="echelle">Facteur d’échelle <output id="val-echelle">1,00</output><input id="echelle" type="range" min="1" max="3" step="0.01" value="1"></label><div class="univ-presets" role="group" aria-label="Valeurs à comparer"><button type="button" data-field="echelle" data-value="1" aria-pressed="false">× 1</button><button type="button" data-field="echelle" data-value="2" aria-pressed="false">× 2</button><button type="button" data-field="echelle" data-value="3" aria-pressed="false">× 3</button></div></div>
<p class="univ-sr" id="expansion-resultat" aria-live="polite">Distance entre A et B : 1,00 unité</p></div>
</article>
  <article class="univ-experience" id="vitesse-temps">
<h2>Le temps dépend du mouvement.</h2>
<div class="univ-explication">
      <p>Dans le référentiel choisi, plus une horloge se déplace vite, moins elle accumule de temps.</p>
      <details><summary>Analyse détaillée</summary><p>Deux horloges peuvent accumuler des durées différentes. Dans le référentiel choisi, une horloge en mouvement bat plus lentement. À bord, chaque seconde reste normale.</p>
      <p>Pour dix ans dans le référentiel choisi, une horloge à 80 % de la vitesse de la lumière mesure six ans. La comparaison dépend du référentiel ; il n’existe pas d’horloge universelle.</p><p>Pour une vitesse constante : Δτ = Δt √(1 − v²/c²). Les valeurs affichées sont calculées avec Δt = 10 ans. Elles comparent deux événements de l’horloge mobile, datés dans le référentiel choisi à l’aide d’horloges synchronisées. Il ne s’agit pas d’un aller-retour de jumeaux.</p><p>Sans gravité ni accélération, la situation est réciproque lorsqu’on change de référentiel. Un objet massif ne peut pas atteindre c. Les aiguilles illustrent le rapport des cadences ; les nombres donnent les durées sur dix ans.</p><p><a href="https://www.einstein-online.info/en/spotlight/light-clocks-time-dilation/">Einstein Online · Dilatation du temps</a> · <a href="/einstein-relativite-restreinte/">L’analyse d’Aeternam</a></p></details>
    </div>
<div class="univ-manipulation"><figure class="univ-demonstration">
      <canvas id="vitesse-canvas" role="img" aria-label="Deux horloges battent à des cadences comparées : celle au repos et celle en mouvement."></canvas>
      <figcaption class="univ-comparaison" aria-live="polite"><span>Dans le référentiel choisi<strong>10,00 ans</strong></span><span>Horloge mobile<strong id="temps-mobile">6,00 ans</strong></span></figcaption>
    </figure>
<div class="univ-controles"><label for="vitesse">Vitesse de l’horloge mobile <output id="val-vitesse">80 % de c</output><input id="vitesse" type="range" min="0" max="99.9" step="0.1" value="80"></label><div class="univ-presets" role="group" aria-label="Valeurs à comparer"><button type="button" data-field="vitesse" data-value="0" aria-pressed="false">Au repos</button><button type="button" data-field="vitesse" data-value="80" aria-pressed="false">80 % de c</button><button type="button" data-field="vitesse" data-value="99.9" aria-pressed="false">99,9 % de c</button></div></div>
<p class="univ-precision">c est la vitesse de la lumière dans le vide.</p><p class="univ-sr" id="vitesse-observation" aria-live="polite">À cette vitesse, l’horloge mobile accumule 4,00 ans de moins.</p></div>
</article>
  <article class="univ-experience" id="gravite">
<h2>La gravité change le temps.</h2>
<div class="univ-explication">
      <p>Une horloge maintenue près d’un objet compact avance moins vite qu’une horloge très éloignée.</p>
      <details><summary>Analyse détaillée</summary><p>En relativité générale, la matière et l’énergie influencent la géométrie de l’espace-temps. La chute libre suit les trajectoires naturelles de cette géométrie.</p>
      <p>Près d’un objet compact, une horloge maintenue immobile peut accumuler moins de temps qu’une horloge très éloignée. Ce n’est pas un défaut de l’horloge.</p><p>Modèle de Schwarzschild : objet sphérique, sans rotation ni charge ; horloge stationnaire, soutenue à r &gt; rₛ. Δτ = Δt √(1 − rₛ/r), avec rₛ = 2GM/c². L’horloge de référence est idéalement à l’infini. L’accélération nécessaire pour rester immobile devient très grande près de l’horizon.</p><p>La surface représente une coupe spatiale équatoriale, dont l’immersion vérifie z = 2√[rₛ(r − rₛ)]. Elle ne représente ni toutes les dimensions ni le temps. L’espace n’est pas une toile qui s’enfonce dans une direction physique supplémentaire.</p><p><a href="https://www.astro.rug.nl/~weygaert/tim1publication/cosmo2007/werkcollege1.pdf">Université de Groningue · Schwarzschild</a> · <a href="/gravitation-horloges/">L’analyse d’Aeternam</a></p></details>
    </div>
<div class="univ-manipulation"><figure class="univ-demonstration"><canvas id="gravite-canvas" role="img" aria-label="Coupe spatiale courbe autour d’un horizon. Le point indique la position de l’horloge stationnaire."></canvas><figcaption>Coupe spatiale de Schwarzschild</figcaption></figure>
<div class="univ-controles"><label for="rayon">Distance au centre <output id="val-rayon">3,00 rayons d’horizon</output><input id="rayon" type="range" min="1.05" max="10" step="0.01" value="3"></label><div class="univ-presets" role="group" aria-label="Valeurs à comparer"><button type="button" data-field="rayon" data-value="10" aria-pressed="false">Loin de l’horizon</button><button type="button" data-field="rayon" data-value="3" aria-pressed="false">À 3 rₛ</button><button type="button" data-field="rayon" data-value="1.05" aria-pressed="false">Près de l’horizon</button></div></div>
<div class="univ-comparaison" aria-live="polite"><span>Très loin<strong>10,00 ans</strong></span><span id="position-horloge">À 3,00 rayons d’horizon<strong id="temps-gravite">8,16 ans</strong></span></div></div>
</article>
  <article class="univ-experience" id="trou-noir">
<h2>Un horizon pour la lumière.</h2>
<div class="univ-explication">
      <p>La gravité dévie la lumière ; une fois l’horizon franchi, elle ne peut plus ressortir.</p>
      <details><summary>Analyse détaillée</summary><p>La lumière suit elle aussi la géométrie de l’espace-temps. Un rayon passant près d’un objet compact est dévié.</p>
      <p>Un trou noir possède un horizon : une frontière au-delà de laquelle aucun signal lumineux ne peut revenir vers l’extérieur. Ce n’est pas une surface solide.</p><p>La trajectoire est intégrée numériquement dans Schwarzschild : u″ + u = 3u²/2, avec u = rₛ/r et les dérivées par rapport à l’angle φ. Le paramètre d’impact b est l’écart asymptotique, exprimé en rₛ. La capture se produit pour b &lt; 3√3/2 ≈ 2,598. La sphère des photons est à 1,5 rₛ.</p><p>Le dessin utilise les coordonnées (r cos φ, r sin φ), pas des distances euclidiennes mesurées sur place. Le point lumineux anime un tracé ; sa vitesse sur l’écran n’est pas une vitesse physique. La singularité classique indique une limite de description. Elle ne prouve pas l’existence d’un passage vers un autre univers.</p><p><a href="https://science.nasa.gov/universe/black-holes/anatomy/">NASA · Anatomie d’un trou noir</a> · <a href="https://web.mit.edu/8.962/www/lecnotes/8_962TA-lec-all.pdf">MIT · Notes de relativité générale</a></p></details>
    </div>
<div class="univ-manipulation"><figure class="univ-demonstration"><canvas id="lumiere-canvas" role="img" aria-label="Une trajectoire lumineuse calculée est déviée ou capturée par un trou noir suivant son paramètre d’impact."></canvas><figcaption>Géodésique lumineuse · trou noir sans rotation</figcaption></figure>
<div class="univ-controles"><label for="impact">Écart du rayon à l’arrivée <output id="val-impact">3,50 rₛ</output><input id="impact" type="range" min="1.8" max="7" step="0.01" value="3.5"></label><div class="univ-presets" role="group" aria-label="Valeurs à comparer"><button type="button" data-field="impact" data-value="7" aria-pressed="false">Faible déviation</button><button type="button" data-field="impact" data-value="2.7" aria-pressed="false">Près de la capture</button><button type="button" data-field="impact" data-value="2.5" aria-pressed="false">Capture</button></div></div>
<p class="univ-resultat" id="sort-lumiere" aria-live="polite">Le rayon est dévié puis repart.</p></div>
</article>
</section>
<section id="avant-apres" class="univ-questions" aria-labelledby="titre-avant">
  <article>
    <h2 id="titre-avant">Et avant le Big Bang ?</h2>
    <div>
      <p class="univ-reponse">Nous ne savons pas.</p>
      <details><summary>Analyse détaillée</summary>
      <p>Le Big Bang décrit une évolution depuis un état chaud et dense. Il ne démontre pas une création à partir de rien.</p>
      <p>Un vide physique n’est pas le néant : il suppose déjà des champs et des lois.</p>
      <p>Le Big Bang chaud est fortement étayé. La singularité de certains modèles classiques, elle, n’est pas observée : elle marque une limite de description. L’inflation ne résout pas à elle seule la question d’une origine absolue.</p><p>L’absence de réponse ne prouve ni une création à partir de rien ni une phase antérieure.</p>
    <div class="univ-hypotheses">
      <div><h3>Un commencement du temps</h3><p>Certains modèles font émerger le temps sans phase antérieure définie. Ces descriptions de l’origine restent théoriques.</p><p class="univ-source"><a href="https://doi.org/10.1103/PhysRevD.28.2960">Hartle et Hawking · Proposition sans bord</a></p></div>
      <div><h3>Un rebond</h3><p>Une contraction pourrait précéder l’expansion. Plusieurs modèles étudient cette possibilité ; aucun n’établit qu’un rebond a réellement eu lieu.</p><p class="univ-source"><a href="https://www.einstein-online.info/en/spotlight/avoiding_the_big_bang/">Einstein Online · Hypothèse du rebond</a></p></div>
      <div><h3>Une physique encore inconnue</h3><p>Relier la gravité et la physique quantique reste un problème ouvert. Nos théories actuelles ne permettent pas de reconstruire avec certitude une origine ultime.</p><p class="univ-source"><a href="https://www.esa.int/Science_Exploration/Space_Science/Planck/Key_questions">ESA · Questions ouvertes</a></p></div>
    </div>
      </details>
    </div>
  </article>
  <article>
    <h2>Et après aujourd’hui ?</h2>
    <div><p class="univ-reponse">Un avenir qui dépend de l’énergie noire.</p>
      <details><summary>Analyse détaillée</summary><p>Si elle se comporte comme une constante cosmologique, l’expansion accélérée se poursuit. Les régions lointaines deviennent de moins en moins accessibles et la formation de nouvelles étoiles finit par s’épuiser.</p><p>C’est la conséquence d’un modèle, pas un futur observé. Une énergie noire différente pourrait changer cette évolution.</p><p class="univ-source"><a href="https://science.nasa.gov/dark-energy/">NASA · L’énergie noire et l’expansion</a></p></details></div>
  </article>
</section>
"""
