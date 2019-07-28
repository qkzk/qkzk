---
author: qu3nt1n
date: 2016-07-02 13:40:44+00:00
draft: false
title: Le compte est bon


---

# Le compte est bon




### Projet de base


Le but de ce jeu est d'aboutir à un nombre tiré au sort entre 100 et 999 en effectuant des calculs avec les 4 opérations élémentaires (, , , ) sur 6 nombres entiers également tirés au sort.
Le but du projet est de réaliser ce jeu en javascript. L'interface pourra avoir la forme suivante :



[![doc00020_1](http://qkzk.xyz/wp-content/uploads/2016/07/doc00020_1.jpeg)
](http://qkzk.xyz/wp-content/uploads/2016/07/doc00020_1.jpeg)




Le nombre à obtenir figure tout en haut. En dessous se trouvent les 6 nombres à utiliser qui sont tirés au sort parmi 24 possibilités comportant
deux fois les nombres de 1 à 10 et une fois le 25, le 50, le 75 et le 100.



Pour communiquer ses calculs le joueur devra cliquer sur les nombres et sur les touches d'opérations (à droite) comme avec une calculette.



Le calcul ainsi effectué sera affiché dans la zone centrale, et le nouveau nombre obtenu apparaîtra en dessous des nombres tirés au sort sous forme
de touche pour une utilisation dans la suite des calculs. Chaque nombre ne peut être utilisé qu'une seule fois. La validité de l'opération de soustraction et de division
sera vérifiée (on doit obtenir un entier positif). Si le joueur aboutit au nombre cherché il gagne et le programme lui proposera une nouvelle partie. Si le joueur n'arrive pas au bon résultat il pourra recommencer ses calculs en cliquant sur le bouton « Recommencer ». Enfin
si le joueur juge qu'il n'arrivera jamais à obtenir le bon résultat, il peut utiliser le bouton « Abandonner » et recommencer une nouvelle partie.



L'ensemble sera intégré dans une page web indiquant le fonctionnement du jeu.





### Extensions








 	  * Ajouter un chronomètre : le joueur doit trouver le bon compte en moins de 45 secondes, sinon il a perdu.
 	  * Ajouter des bruitages, une musique de fond.
 	  * Réaliser une version réseau du jeu :

 	    * le joueur se connecte en indiquant son prénom,
 	    * le joueur invite un autre joueur connecté à jouer avec lui (tous les joueurs connectés qui ne jouent pas encore sont affichés dans une liste),
 	    * le jeu se déroule avec arbitrage de l'ordinateur en 5 manches. A chaque manche l'ordinateur propose un compte à trouver, les joueurs ont 45 secondes pour proposer leurs calculs. Au terme des 45 secondes le joueur qui est le plus proche du
résultat marque 5 points (10 points s'il a le bon compte). Si les deux joueurs sont à la même distance du bon compte ils marquent tous les deux
le nombre de points correspondant. A la fin de la partie l'ordinateur proclame le vainqueur. A tout moment un joueur
peut abandonner la partie et ainsi donner la victoire à l'autre joueur.


 	  * Ajouter au programme un algorithme de résolution de compte : si aucun joueur ne trouve le bon compte, l'ordinateur affiche une solution (ou
indique qu'il n'y a pas de solution le cas échéant).

