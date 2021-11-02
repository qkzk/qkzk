---
author: qu3nt1n
date: 2016-07-02 13:55:50+00:00
draft: false
title: Pendu
bookCollapseSection: true


---

### Projet de base





Tout le monde connaît le jeu du pendu : il faut trouver un mot en devinant les lettres qui le composent.



Le projet consiste à réaliser une application en javascript qui permet de jouer contre l'ordinateur.



L'interface pourra prendre la forme suivante :




[![doc00008_1](/uploads/uploads/2016/07/doc00008_1.jpeg)
](/uploads/uploads/2016/07/doc00008_1.jpeg)




Cette interface est divisée en 3 zones :






* La zone du mot à deviner : ce mot sera tiré au sort par l'ordinateur dans une liste.
* La zone du dessin du pendu : le dessin se complétera à chaque mauvaise lettre proposée par le joueur.
* La zone du clavier virtuel : le joueur proposera une lettre par un simple clic, une lettre qui a été déjà proposée
deviendra inactive. 




Il faudra prévoir également la gestion de fin de partie et offrir la possibilité au joueur de recommencer.



L'ensemble sera intégré dans une page web indiquant le fonctionnement du jeu. 





### Extensions








* Ajouter un menu permettant au joueur de choisir une thématique pour les mots à deviner.
* Ajouter des bruitages, une musique de fond.
* Ajouter une option de jeu humain contre humain :

* au départ les prénoms des deux joueurs sont saisis,
* l'ordinateur gère les parties successives (à tour de rôle chaque joueur propose un mot que l'autre joueur doit deviner),
* l'ordinateur gère les scores.

* Réaliser une version réseau du jeu :

* le joueur se connecte en indiquant son prénom,
* le joueur invite un autre joueur connecté à jouer avec lui (tous les joueurs connectés qui ne jouent pas encore sont affichés dans une liste), 
* le jeu se déroule comme dans la version humain/humain mono-poste.


