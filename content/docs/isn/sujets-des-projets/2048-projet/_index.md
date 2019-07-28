---
author: qu3nt1n
date: 2017-06-14 11:22:58+00:00
draft: false
title: 2048 - projet
weight: 1
---

# 2048 - projet


![](https://articles-images.sftcdn.net/wp-content/uploads/sites/9/2014/03/Corner-Test.gif)


L'objectif de ce projet est de réaliser une version jouable de 2048.

J'imagine que vous connaissez tous ce jeu, sinon il convient d'essayer [quelques parties](https://gabrielecirulli.github.io/2048/) pour en comprendre le fonctionnement.

Les malins parmi vous remarqueront que le code source original est disponible depuis le premier jour. Bien. Il ne vous servira à rien car il n'est pas commenté. D'autant que je vous ne raterai pas si vous comptez vous reposer là dessus.


## Principe


Deux grandes étapes sont à distinguer :



 	  1. la réalisation du jeu en mode texte. Vous jouez dans la console ou dans une page.
 	  2. La réalisation de la partie graphique. Cette partie est moins importante.

Le principe du jeu est simple, une grille de 4x4 contient des nombres qui sont tous des puissances de 2 : des tuiles.
Vous déplacez le contenu de cette grille dans une direction et les tuiles se dirigent au maximum dans cette direction.
Deux tuiles identiques s'ajoutent alors et n'en font plus qu'une.
L'objectif est d'atteindre 2048, voire les tuiles supérieures (4096 etc.).




## Cahier des charges


Le jeu est découpé en deux parties presque indépendantes : son fonctionnement et sa représentation graphique.

Le langage employé peut-être Python (on jouera dans la console puis dans pygame) ou javascript (page html en texte puis page html + canvas). Le jeu me parait plus facile à développer en Python.



 	  1. Votre grille est figurée par un tableau de 4x4. Présentation textuelle de ce tableau. Ici se découpe le projet.
 	  2. **Le fonctionnement du jeu.**

 	    * Déplacement vers la gauche.
Vous allez d'abord réaliser la simplification des zéros. Les éléments non vide doivent se déplacer.
Ensuite l'addition de deux éléments identiques et la simplification.
Enfin l'apparition de nouvelles tuiles et la détection de la fin de partie.
 	    * Les autres déplacements peuvent être obtenus par des symétries. Cela évite d'avoir à tout réécrire trois fois.
La symétrie selon un axe vertical central ("retourner") échange gauche et droite. Pour se déplacer à droite on peut donc :
1. "retourner", 2. déplacer à gauche, 3. "retourner".
 	    * L'échange abscisse/ordonnée ("transposer") permet de déplacer selon un axe vertical.
Pour se déplacer verticalement (dans quel sens ?) on peut donc :
1. "transposer", 2. déplacer à gauche, 3. "transposer".
 	    * Le dernier déplacement vertical, nécessite une combinaison des deux précédents. Je vous laisse le soin de le décrire.
A cette étape votre jeu est jouable en mode texte


 	  3. **La représentation graphique** se découpe ainsi :

 	    1. Représenter une grille vide.
 	    2. Représenter une tuile et lui attribuer automatiquement une couleur.
 	    3. Représenter à chaque étape votre grille et adapter les commandes.


 	  4. La dernière étape est **l'intégration des deux parties**.
Selon le langage employé on pourra rendre le jeu jouable sur mobile en gérant aussi les événements "touch / swipe etc."
