---
author: qu3nt1n
date: 2017-06-14 11:44:09+00:00
draft: false
title: Space orbit
weight: 11
---

[embed]https://games.tcdn.co/media/6/movie.sd.mp4[/embed]

[Space orbit](https://www.gameeapp.com/game/R4k6GrC) est un jeu très simple.

Un vaisseau tourne autour d'une planète et doit ramasser des bonus disposés régulièrement sur sa trajectoire.
Il peut changer de sens de rotation en pressant un bouton ou l'écran selon le terminal utilisé.
Quand il a ramassé tous les bonus le niveau augmente et les bonus réapparaissent.
La planète tire régulièrement des missiles qui avancent tout droit. Ils sont soit dirigés vers le vaisseau (et le heurtent alors) soit légèrement derrière lui.
Chaque contact avec un missile entraîne la mort et la fin de la partie.


### L'objectif de ce projet est de réaliser ce jeu en p5js. Il faut donc avoir suivi un tutoriel à ce sujet.


Ce projet n'est pas simple car il nécessite de créer plusieurs fois le même objet (le missile, les bonus) les programmer individuellement. Il est donc préférable d'employer des classes. Néanmoins, je suis parvenu à le réaliser avant que ma chérie n'ait fini de se préparer, c'est donc faisable.


## Cahier des charges





 	  1. Dessiner l'orbite du vaisseau (un cercle) et la planète (un disque).
 	  2. Dessiner le vaisseau sommairement (un triangle) et l'animer sur sa trajectoire.
 	  3. Animer automatiquement le vaisseau de façon ce qu'il tourne tout seul et change de sens après chaque tour (ce sera plus facile ainsi)
 	  4. Les bonus.

 	    * Représenter les bonus (des disques) et les positionner régulièrement. Créer un tableau contenant l'état des bonus (vrai : ramassé, faux : pas encore ramassé).
 	    * Mettre à jour l'affichage des bonus en fonction de leur état (ils s'affichent s'ils ne sont pas ramassés).
 	    * Gérer la collision du vaisseau est des bonus. Le score (nombre de bonus) apparaît à l'écran.
 	    * Les bonus réapparaissent une fois tous ramassés.


 	  5. Les missiles.

 	    * Tirer un missile (un disque) tout droit qui sort de l'écran vers la droite.
 	    * Tirer un missile tout droit qui heurte le vaisseau (mais ne provoque rien).
 	    * Tirer un missile tout droit vers le vaisseau OU légèrement derrière lui.
 	    * Créer un tableau des missiles qui sera mis à jour au fur et à mesure des tirs.
 	    * Retirer régulièrement du tableau les missiles sortis de l'écran.
 	    * Détecter la collision du vaisseau et des missiles et donc la fin de partie.
 	    * Gérer la nouvelle partie sans devoir recharger la page. Gestion d'un high score. Éventuellement dans un cookie
 	    * La difficulté augmente quand on a ramassé tous les bonus : les missiles vont plus vite.


 	  6. Evénements clavier et "touch" : on presse une touche (ou l'écran) pour changer de direction, on presse entrée pour recommencer la partie.



### Extensions





 	  * Améliorer les graphismes et les animations
 	  * Intégrer le jeu dans un serveur web et le rendre accessible sur internet
 	  * Deux vaisseaux à l'écran en même temps ! L'objectif est de ramasser plus de bonus que l'autre avant de mourir. Les missiles sont plus nombreux et visent régulièrement l'un ou l'autre des joueurs.
Deux modes possibles
