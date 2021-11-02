---
author: qu3nt1n
date: 2016-07-01 13:23:17+00:00
draft: false
title: Snake (js, canvas)
bookCollapseSection: true
weight: 10
---

# Snake




### Projet de base



![](http://static2.businessinsider.com/image/51647cb1eab8ea9d4c00000c/snake.gif)
Ce projet vise à créer un jeu de Snake, jouable au clavier dans un page html.

Le snake grandit en mangeant un morceau de viande et meurt si sa tête rencontre un élément de son corps.

**Deux versions sont possibles** : il traverse les murs ou meurt à leur contact.

Le joueur gagne quand il remplit tout l'écran.

Le score est donné par le nombre de morceaux mangés par le snake.



**C'est un projet relativement difficile, en particulier pour les novices.**

Vous créerez une page html contenant un canvas animé par un script javascript.
Le snake est repéré par un tableau contenant les coordonnées de sa tête et de ses écailles ; il est important de bien comprendre le déplacement du snake. Pour que sa queue puisse le suivre, chaque écaille se déplace à chaque étape.
On envisagera les animations bloc par bloc.


### Cahier des charges





* Création de la page, de ses éléments statiques ou immobiles et du canvas.
* Appel du canvas, premier affichage, boucle de rafraîchissement.
* Description des fonctions nécessaires et des variables qu'elles utilisent.
* Affichage d'un score.
* Affichage du snake, de la viande.
* Animation du snake selon une direction prédéfinie (l'étape la plus difficile selon moi).
* Le snake mange la viande.
* La tête du snake tourne (peut-être fait beaucoup plus tôt).
* Le snake meurt (peut-être envisagé dès qu'il se déplace).



### Extensions


On pourra ajouter des fonctionnalités, voici quelques suggestions (liste non limitative et non hiérarchisée) :



* Dimensions variables de la page proportionnelle à la fenêtre ou réglable par le joueur (assez facile).
* Difficulté variable : le joueur choisit sa difficulté ou le snake accélère avec son score ou avec le temps (facile).
* Graphismes : les améliorer (possibilités infinies).
* Animations : rendre fluide le déplacement du snake, il se déplace alors continuellement mais les positions de la viande et les "tournants" sont toujours bloc par bloc (difficile)
* Bonus / malus : la viande change de couleur et apporte plusieurs écailles (difficulté moyenne) ou change la direction du snake (facile) etc.
* Mode automatique : l'ordinateur joue tout seul et meurt parfois (difficile) ; l'ordinateur joue tout seul et remplit l'écran (solides connaissances en algorithmique nécessaire).
