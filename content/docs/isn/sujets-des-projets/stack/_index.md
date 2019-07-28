---
author: qu3nt1n
date: 2017-06-14 12:13:40+00:00
draft: false
title: Stack
weight: 12
---

![](https://lh3.googleusercontent.com/EbKHPs7mrWU9wqLihX9zqPEk0OsZgBxwF0bC0A-I7nBlDxiAa07i0C2YcVDM1cP8gGw=h900-rw)




Stack est un jeu pour smartphone consistant à déposer régulièment des tuiles les une sur les autres. Chaque tuile arrive alternativement de la gauche ou la droite et se déplace en ligne droite. Le joueur arrête ce déplacement et la tuile se dépose alors.
Toute la partie qui dépasse de la pile tombe et seule la partie restante est conservée.
La nouvelle tuile a la même taille que la partie restante.

Le jeu s'arrête quand la tuile est déposée dans le vide.


### L'objectif de ce projet est de réaliser ce jeu dans une page html avec un canvas.


C'est l'un des deux plus difficiles. Le cahier des charges est peu détaillé.


## Cahier des charges





* Réaliser une tuile à l'écran du canvas, au centre, immobile.
* Animer cette tuile dans un sens puis l'autre. Elle quitte l'écran.
* Faire rebondir la tuile au bord de l'écran et changer de sens.
* Gérer le seul événement : le joueur presse une touche et la tuile s'arrête
* A chaque arrêt une nouvelle tuile apparaît depuis l'autre côté. La précédente est d'abord effacée. Elle reste ensuite sur place (ça sera très moche).
* Gérer la pile (le stack) sur laquelle la tuile se dépose. A chaque pression du joueur, la pile descend d'un étage.
* Gérer l'alignement des tuiles, les bords qui dépassent sont supprimés.
* Gérer la pile qui conserve ses états précédents et s'anime régulièrement. Le score apparaît à l'écran.
* Introduire des couleurs aléatoires qui doivent respecter une certaine palette.



### Extension





* Les graphismes.
* Les animations
* Les bonus (quand des tuiles sont parfaitement alignés). Quelques bonus de suite augmentent les dimensions du sommet de la pile
