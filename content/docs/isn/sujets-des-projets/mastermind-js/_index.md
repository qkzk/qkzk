---
author: qu3nt1n
date: 2016-07-01 13:05:39+00:00
draft: false
title: Mastermind (js)
weight: 5
---




# Mastermind




# ![doc00022](http://qkzk.xyz/wp-content/uploads/2016/07/doc00022.jpeg)





### Projet de base


Le Mastermind est un jeu de société de réflexion et de déduction inventé par Mordecai Meirowitz dans les années 1970.

Il se présente généralement sous la forme d'un plateau perforé de 10 rangées de quatre trous pouvant accueillir des pions de couleurs.
Le nombre de pions de couleurs différentes est de 8 et les huit couleurs sont généralement : rouge ; jaune ; vert ; bleu ; orange ; blanc ; violet ; fuchsia.
Il y a également des pions blancs et rouges (ou noirs) utilisés pour donner des indications à chaque étape du jeu : blanc le nombre de couleurs bien placées, rouge le nombre de couleurs présentes dans la combinaison mais mal placées.

Le projet consiste à créer une version modulable du jeu de Mastermind. Le joueur est toujours celui qui doit deviner la bonne combinaison. L'ordinateur répond à chaque tour et détecte la victoire ou la défaite du joueur.

Il existe de nombreuses variantes suivant le nombre de couleurs, de rangées ou de trous.


### Cahier des charges





 	  * Création de la page et des éléments statiques
 	  * Les boutons permettant de choisir une combinaison (on créera si nécessaire une version où le joueur TAPE la combinaison : "RRVB")
 	  * Génération aléatoire du code secret
 	  * Affichage des éléments : coups réstants, propositions ratées, jetons indiquant le nombre de "bons", de "mauvais" etc. A cette étape, le programme ne tournera pas encore, seuls les éléments sont affichables et vous entrerez dans le script vos propositions
Bien étoffé ce point peut faire l'objet d'une partie en soi presque indépendante du reste (pour un membre d'une équipe de trois). Cela nécessite alors un aménagement du cahier des charges et une très bonne communication dans l'équipe.
 	  * Algorithme papier : Test de victoire.
 	  * Programmation du dit algorithme.
 	  * Algorithme papier : compter les bons "mal placés".
 	  * Programmation du dit algorithme.
 	  * Mise en commun de tous les éléments.

L'ensemble sera intégré dans une page html fournissant les explications nécessaires à l'utilisation du logiciel.


### Extensions


On pourra ajouter des fonctionnalités, voici quelques suggestions (liste non limitative) :



 	  * modification de la grille, des jetons disponibles
 	  * gestion du temps
 	  * affichages, graphismes, animations
