# Données nécessaires pour la prochaine analyse

Ce document décrit un besoin scientifique. Aucun message n'a été envoyé et aucun accès restreint n'est acquis.

## Question à soumettre à une équipe compétente

Disposez-vous d'épisodes comportant, pour le même intervalle de rêve délimité par des signaux enregistrés, une estimation numérique de sa durée communiquée pendant le sommeil puis une estimation de ce même intervalle au réveil ? Les consignes, les délais, les épisodes sans réponse et les validations du sommeil et du décodage sont-ils documentés ?

La demande porte sur la possibilité d'une analyse secondaire dans un cadre de collaboration approprié. Aeternam est un blog personnel de recherche documentaire et de calcul ; aucune affiliation académique ou qualification clinique n'est revendiquée.

## Informations minimales à vérifier avant de demander un export

- Estimation d'une durée ou simple signal de début/fin de tâche ? Deux mesures du même objet sont nécessaires.
- Unité numérique commune ou échelle ordinale ? Les classes ne sont pas remplacées par des secondes.
- Intervalles strictement appariables ? Un récit de rêve entier et une courte tâche ne sont pas interchangeables.
- Rapports au réveil obtenus avant rappel de la durée physique ou de la réponse antérieure ? Conserver tout retour d'information comme variable de contrôle.
- Registre de toutes les tentatives et motifs des absences ? Les épisodes sans rappel ne sont pas des durées nulles.
- Consentement, conditions d'accès, possibilité de réanalyse et de publication d'agrégats compatibles avec le projet ? Les restrictions des données cliniques sont conservées.

Le schéma `schema-paires.csv` formalise ces variables pour notre logiciel. Si aucune source ne possède les deux estimations, l'analyse principale demeure inexécutable : une étude prospective avec une équipe de recherche serait une nouvelle étape, à concevoir et à autoriser séparément. Une simple acquisition EEG supplémentaire ne remplirait pas les champs de jugement manquants.

## Résultat qui ferait avancer la question

Un écart reproductible entre les deux rapports indiquerait un changement de jugement dans les conditions étudiées. Il faudrait encore départager biais de réponse, transition sommeil–éveil et rappel. La stabilité des rapports demanderait une analyse d'équivalence avec une marge préalablement justifiée. Aucun des deux résultats ne suffirait à mesurer une quantité absolue d'expérience consciente.
