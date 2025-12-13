---
title: Flappy Bird
author: qkzk
date: 2025-12-12
theme: metropolis
weight: 1200
bookCollapseSection: true
geometry: "margin=1.5cm"

---




[Dépôt spécifique](git@github.com:qkzk/flappy_bird.git)

### Présentation

Flappy Bird est un jeu mobile crée en 2013 et qui connu un grand succès avant
d'être retiré en 2014.

Étant à la fois simple, difficile et addictif le jeu est resté célèbre.
Il est aussi devenu un passage obligé des débutants en programmation étant
donné qu'il peut être écrit rapidement et permet des développements intéressants.
C'est donc un projet abordable pour nous.

## Concept

C'est un jeu d'adresse en vue lattérale en deux dimensions.

On déplace un oiseau, dont l'abscisse est constante et l'ordonnée varie.

Soumis à la gravité, l'oiseau tombe en permanence. Afin de ne pas quitter l'écran
le joueur peut battre des ailes ce qui fait monter l'oiseau.

Des tuyaux se déplacent vers la gauche et, afin de les éviter, l'oiseau doit passer dans un vide entre les tuyaux.

Chaque sortie de l'écran (haut ou bas) et chaque contact avec un tuyau provoque la mort de l'oiseau.

Chaque tuyau passé rapporte un point.

L'objectif est d'atteindre le score le plus élevé.

## Éléments du jeu


![Flappy_bird](./flappy_bird.png)

### L'oiseau

Sa chute est décrite, de manière classique ainsi :

* `y` son ordonnée, orientée _vers le bas_,
* `v` sa vitesse verticale,
* `g` la gravité,

**Sans action du joueur**

À chaque frame, on fait :

* `v = v + g`
* `y = y + v`
* Si `v > v_max`, `v = v_max` 

La chute se fait donc de manière accélérée, avec une vitesse limite.

**Si le joueur saute**

* `v = v_saut`
* `y = y + v`

Et voilà !

### Les tuyaux

La hauteur du vide central entre les tuyaux est constante.

Les tuyaux sont donc repérés par un seul point, celui du coin "haut gauche" de cet écart.

Toutes les autres coordonnées peuvent-être calculées depuis cette donnée.

À l'écran, on ne voit jamais plus de deux tuyaux. Donc on se contentera d'en avoir
deux en mémoire.

**Déplacement**

* À chaque frame, les tuyaux bougent vers la gauche,
* si l'abscisse devient trop négative (ie. le tuyau est entièrement sorti à gauche),

    * on réinitialise son absisse à droite de l'écran, avec un petit paramètre aléatoire,

    * on réinitialise la hauteur du vide aléatoirement.

**Collision**

Chaque collision de l'oiseau avec un tuyau doit provoquer sa mort.

pygame permet de gérer les collisions entre certains oblets (rectangles ou _acteurs_)
aussi nous ne les programmerons pas nous même.

Les programmer requiert beaucoup de comparaisons sans apporter grand chose d'intéressant. C'est à réserver à une extension ultérieure.

## Constantes

Afin de pouvoir s'entendre, différentes constantes sont données, certaines sont
illustrées dans la figure ci-dessous.

Vous pouvez partir de 0 et les calculer vous même, à nouveau, dans une extension.

Ajuster ces constantes afin d'améliorer la jouabilité est un processus long
et fastidieux que je vous épargne.


# Extensions

## Compléter le jeu avec des images

On peut remplacer les rectangles par des `Actor`s et utiliser des images.


### Images du jeu

Une [version en ligne](https://flappybird.io) du jeu peut servir de référence.

Vous trouverez facilement des images du jeu en ligne.
