---
author: qu3nt1n
date: 2016-07-02 13:42:21+00:00
draft: false
title: Jeu de la vie
weight: 4
---




### Description du Jeu de la Vie









[![jeudelavie](http://qkzk.xyz/wp-content/uploads/2016/07/jeudelavie.gif)
](http://qkzk.xyz/wp-content/uploads/2016/07/jeudelavie.gif)




Le Jeu de la Vie, est un automate cellulaire inventé par le mathématicien John Horton Conway en 1970.

C'est un jeu "sans joueur", ce qui signifie que son évolution est entièrement déterminée par son état initial, sans autre intervention de l'utilisateur.

L'univers du Jeu de la Vie est une grille orthogonale à deux dimensions infinie composée de cellules carrées. Chacune d'entre elles possédant deux états : vivant ou mort. Chaque cellule intéragit avec ses huit voisines (horizontales, verticales et diagonales). A chaque pas la transition se déroule ainsi :



 	  * Une cellule vivante ayant deux voisins vivants ou moins meurt, comme si cela était causé par sous-population.
 	  * Une cellule vivante avec deux ou trois voisins vivants le reste.
 	  * Une cellule vivante avec plus de trois voisins vivants meurt, comme si cela était causé par surpopulation.
 	  * Toute cellule morte avec exactement trois voisins vivants devient vivante, comme si cela était causé par la reproduction.

L'état initial est la racine du système. La première génération est créée en appliquant les règles citées ci-dessus simultanément à toutes les cellules de la racine. Les naissances et les morts ont lieu simultanément à intervalle régulier. En d'autres termes chaque génération n'est fonction que de l'état précédent. Les règles continuent d'être appliquées de manière répétées pour créer les générations futures.






### Projet de base




Ce projet vise à créer un réseau d'automates initiés aléatoirement et se générant automatiquement.






Vous créerez une grille de taille 100x100 affichée dans une page web. (html, css pour les éléments fixes ; js, canvas pour les éléments dynamiques).
Chaque élément de la grille est un automate cellulaire suivant les règles du jeu de la vie.

Les bords de la grilles sont reliés : le bord gauche avec le droit, celui du haut avec celui du bas (on obtient donc un tore).

Le jeu de la vie se déroule de la manière suivante. Chaque cellule a deux états possibles : morte ou vivante.

A chaque étape, l'évolution d'une cellule est entièrement déterminée par l'état de ses huit cellules voisines :

Une cellule morte dont exactement trois voisines sont vivantes devient vivante.

Une cellule vivante dont deux ou trois cellules sont vivantes le reste.

Un bouton permettra de mettre en pause ou de reprendre l'évolution.

La lecture détaillée [ de l'article wikipedia](http://fr.wikipedia.org/wiki/Jeu_de_la_vie) correspondant est fortement conseillée.

[ L'easter egg](http://www.google.fr/search?q=conway%27s+game+of+life) de google est sans doute l'illustration la plus facile d'accès.

Pour découvrir d'autres motifs  : [en ligne](http://conwaylife.appspot.com/pattern/acorn) et d'autres algorithmes similaires : [Golly](http://golly.sourceforge.net/) (à installer chez vous de préférence).






### Plan





Voici une liste d'étapes à franchir dans la réalisation du projet. Celles-ci reprennent, grosso-modo les étapes du mini-projet "feu de forêt"






 	  1. comprendre les règles.
 	  2. faire des exemples à la main, sur qq grilles simples.
 	  3. rédiger les règles - > obtenir l'algorithme le plus simple qui soit.
 	  4. code : html créer la page -> choix des variables, dimensions.
 	  5. code : css, mettre en page
 	  6. code : créer une grille random, canvas : afficher une grille
 	  7. code : js, rédiger les transitions. Le jeu doit alors tourner tout seul et l'objectif initial est atteint. Cette dernière étape est à la fois la plus importante et la plus difficile. Elle dépend énormément de votre bonne compréhension du mécanisme du jeu.
 	  8. papier : grilles préatablies pour tester des situations
 	  9. code : charger les grilles









### Extensions





On pourra ajouter des fonctionnalités, voici quelques suggestions (liste non limitative et non hierarchisée) :






 	  * Coloration des cellules en fonction du nombre de cellules voisines vivantes.
 	  * Illustration de figures prédéfinies (oscillateurs, vaisseaux, mathusalems, canons, pushers etc.).
 	  * Création d'une interface permettant de générer sa propre grille à la main (en cliquant sur certaines cases) et d'en regarder l'évolution.
 	  * Illustration d'autres automates cellulaires suivant des règles similaires.
