---
author: qu3nt1n
date: 2016-07-01 13:20:51+00:00
draft: false
title: Zagzig (js, canvas)
bookCollapseSection: true
weight: 14
---

# Zagzig


ZagZig est un remake du jeu ZigZag disponible sur google play et itunes.

![zigzag](/uploads/uploads/2016/07/zigzag-168x300.jpg)







L'objectif de ce projet est de réaliser le jeu complet en javascript à l'aide de l'outil canvas.
Essentiellement, le moteur du jeu crée une cellule (un losange) en haut de l'écran, partageant un bord avec la dernière cellule crée et fait défiler vers le bas l'ensemble. Cet ensemble crée l'impression de continuité. La bille se déplace horizontalement à vitesse constante et change de direction quand on agit (pression sur l'écran ou une touche du clavier). Chaque action rapporte un point (les bonus 2 points). Le joueur perd dès que la bille n'est plus sur une cellule.








On créera ce jeu dans une page html à l'aide de javascript et canvas, la mise en page est faite en css. Le jeu est considéré comme "jouable" dès que la défaite (chute de la bille) est correctement gérée et qu'on voit le score.






##  Cahier des charges


On créera dans cet ordre les éléments :



* une cellule
* le déplacement de cette cellule
* un "ruban" continu de cellule - c'est clairement la première étape cruciale
* la balle et son déplacement
* la défaite (tomber) - voici la deuxième étape importante
* le score
* le rebord vertical des cellules
* les bonus (les diamants mauves)
* le changement aléatoire de couleur






### Extensions





On pourra ajouter des fonctionnalités, voici quelques suggestions (liste non limitative et non triée par difficulté) :






* meilleur score dans un cookie
* la chute des cellules parvenues en bas de l'écran
* la chute de la balle qui tombe
* les menus : pause, restart etc.
* les autres statistiques du joueur : nombre de parties, de bonus etc.
* l'effet de lumière autour de la bille (regardez bien)
* des sons
* différentes résolutions
* rendre le jeu jouable sur un écran tactile



### Pour commencer


Tutoriel : créer un jeu en html, js, canvas : [le bon vieux casse brique](http://www.lafermeduweb.net/tutorial/creer-un-jeu-en-html-canvas-et-javascript-13.html)
