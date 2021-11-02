---
author: qu3nt1n
date: 2018-08-18 09:35:52+00:00
draft: false
title: Othello / Reversi
bookCollapseSection: true
weight: 6
---

# Othello


## Présentation


Othello (aussi connu sous le nom Reversi) est un jeu de plateau à deux joueurs. Il se joue sur un tablier unicolore de 64 cases, 8 sur 8. Les joueurs disposent de 64 pions bicolores, noirs d'un côté et blancs de l'autre. En début de partie, quatre pions sont déjà placés au centre de l'othellier : deux noirs, en _e4_ et _d5_, et deux blancs, en _d4_ et _e5_. Chaque joueur, noir et blanc, pose l'un après l'autre un pion de sa couleur sur l'othellier selon des règles précises. Le jeu s'arrête quand les deux joueurs ne peuvent plus poser de pion. On compte alors le nombre de pions. Le joueur ayant le plus grand nombre de pions de sa couleur sur l'othellier a gagné.


## Règles du jeu


Noir commence toujours la partie. Puis les joueurs jouent à tour de rôle, chacun étant tenu de capturer des pions adverses lors de son mouvement. Si un joueur ne peut pas capturer de pion(s) adverse(s), il est forcé de passer son tour. Si aucun des deux joueurs ne peut jouer, ou si l'othellier ne comporte plus de case vide, la partie s'arrête. Le gagnant en fin de partie est celui qui possède le plus de pions.

La capture de pions survient lorsqu'un joueur place un de ses pions à l'extrémité d'un alignement de pions adverses contigus et dont l'autre extrémité est déjà occupée par un de ses propres pions. Les alignements considérés peuvent être une colonne, une ligne, ou une diagonale. Si le pion nouvellement placé vient fermer plusieurs alignements, il capture tous les pions adverses des lignes ainsi fermées. La capture se traduit par le retournement des pions capturés. Ces retournements n'entraînent pas d'effet de capture en cascade : seul le pion nouvellement posé est pris en compte.

Par exemple, la figure de gauche ci-dessous montre la position de départ. La figure centrale montre les 4 cases où Noir peut jouer, grâce à la capture d'un pion Blanc. Enfin, la figure de droite montre la position résultante si Noir joue en **d3**. Le pion Blanc **d4** a été capturé (retourné), devenant ainsi un pion Noir.

![Début d'une partie](/uploads/uploads/2018/08/othello.jpg)
<center>_Début d'une partie d'Othello_</center>

Le texte précédent est un extrait [de wikipedia](https://fr.wikipedia.org/wiki/Othello_(jeu)).


## Cahier des charges


Le projet présente deux parties et la deuxième est réservée à des élèves experts.


## Jeu à deux joueurs - niveau intermédiaire


Vous réaliserez une page web (html, css, js) ou un jeu pygame permettant à deux joueurs de s'affronter.



* Page web présentant l'Othellier. La page peut être un grand tableau bien mis en page dans lequel chaque case est une cellule. Idéalement, l'othellier occupe le maximum de place disponible à l'écran et s'adapte aux différentes résolutions (responsive design).
* On intégrera les références des cases selon les notations officielles
* Un lien vers les règles et quelques illustrations doivent être présents
* Chaque clic sur une case y ajoute un jeton et retourne les jetons capturés
* Votre script empêche un coup illégal et affiche un message d'erreur dans la page (pas de popup dans la version finale)
* Si aucun coup n'est possible pour un joueur un message est affiché
* Votre script détecte la fin de partie et affiche le résultat
* On peut alors rejouer et le score finale vient s'ajouter. Il est possible de réinitialiser les scores sans rafraîchir la page.

De toute évidence il faut d'abord savoir jouer. Installer une version gratuite sur son smartphone est un point de départ.


## Jeu contre l'ordinateur - niveau expert


**A envisager lorsque le mode deux joueurs est réalisé convenablement.**

Il existe déjà de nombreux programmes (mobile, pc, console...) permettant d'affronter l'ordinateur. Ce fut d'ailleurs l'un des premiers jeu d'arcade Nintendo et l'un des premiers jeux console.

A chaque tour l'ordinateur calcule le meilleur coup selon vos critères et le réalise.

L'objectif de cette partie est donc d'intégrer un adversaire informatique qui permet de joueur seul.

On pourra s'aider de cette référence [wikipédia en anglais](https://en.wikipedia.org/wiki/Computer_Othello).

Si ce travail s'apparente à celui d'un jeu de dames ou d'échecs il y a une différence fondamentale : à chaque tour il n'y a que très peu de coups.
La partie ne peut durer plus d'une soixantaine de coups et, surtout, à chaque tour il n'y a que quelques coups disponibles. Ensuite, l'Othellier est symétrique.

Il n'est pas encore envisageable sur nos machines d'explorer tous les coups jusqu'à la fin de la partie - c'est possible sur un othellier 4x4 ou 6x6 et on dit que le jeu est résolu - et il convient donc d'évaluer une position et de la noter convenablement. On pourra s'inspirer des échecs pour le score :



* score = 0 : la position est nulle.
* score > 0 : les blancs ont un avantage, plus le score est élevé plus cet avantage est grand.
* score < 0 : inversement, les noirs ont un avantage.

De nombreux algorithmes existent déjà, une version "light" de cette partie peut-être d'en implémenter un. Dans ce cas on s'attend à ce que le programme tourne convenablement à la fin du projet.

L'objectif réel est que vous créiez votre algorithme puis que vous l'implémentiez, quitte à ce qu'il ne fonctionne pas parfaitement à la fin de l'année.

Votre programme doit répondre un coup en un temps donné (1, 5, 10, 30, 60... secondes) préétabli. Il doit toujours répondre à temps.


### Evaluer un coup


Différentes stratégies existent mais aucune n'est parfaite.

Toutes emploient l'algorithme [minimax](https://fr.wikipedia.org/wiki/Algorithme_minimax) ou sa version améliorée [élagage alpha-beta](https://fr.wikipedia.org/wiki/%C3%89lagage_alpha-b%C3%AAta)



* Maximiser à chaque tour le nombre de jetons capturés - c'est une stratégie très faible qui ne peut servir que de premier jet.
* Pondérer chaque case en fonction de sa position. Chaque case se voit affecter une valeur et l'ordinateur cherche la meilleure combinaison possible - cette stratégie ne gagnera pas contre un joueur humain un peu expérimenté.
* Optimiser la mobilité : le nombre de coups disponibles et minimiser les disques frontières (voisins d'une case vide) - cela devrait vaincre sans problème un humain "normal" :)
* Reconnaissance de schémas : maximiser la mobilité, minimiser les disques frontières et découper localement des configurations. On évalue ensuite la meilleure configuration depuis une base de donnée de parties et on calcule les statistiques des meilleurs résultats.

La grande difficulté de ce travail consiste donc à explorer les différents coups possibles en les repérant, les triant convenablement puis en les évaluant. Ensuite la contrainte de temps est majeure : l'ordinateur doit répondre à temps.

Il convient donc de maîtriser un minimum l'exploration de graphes (profondeur, largeur, dijkstra, A* etc.)

Une dernière possibilité est de commencer par un othelier 4x4 qui limite considérablement le nombre de coups et de parties possibles. L'exploration complète n'étant pas possible pour un 8x8, il faudra adapter la démarche.


## Variantes du projet


De toute évidence on peut adapter la première partie du projet à d'autres jeux à deux joueurs.

Le morpion, les dames, les échecs, puissance 4 etc.

Le niveau augmente alors considérablement étant donné la variété des coups et la complexité des règles.
Passer aux échecs est déjà beaucoup plus difficile étant donné la variété des pièces et la complexité de certaines règles (échec, mat, pat, roque, prise en passant, promotion, nulle par répétition etc.). Un projet de niveau très solide est déjà de réaliser un jeu d'échecs à deux joueurs.

N'espérez pas créer un adversaire informatique aux dames ou aux échecs en ISN.


## Version du projet proposée par l'université de Lille : les jeux à deux joueurs.

_Réaliser une implémentation des jeux à deux joueurs en Python de façon modulaire._

Un module moteur gère une partie et importe un autre module par jeu (nim, morpion, othello etc.).
Le module "moteur" ne change pas, seul l'import diffère. Un troisième module, minimax est ensuite réalisé.
Celui-ci est générique et fonctionne avec n'importe quel jeu à deux joueurs.

Tous les jeux à deux joueurs doivent être à _connaissance parfaite_ (les deux joueurs connaissent parfaitement l'état du jeu, pas de carte cachée, pas d'aléatoire) et à _somme nulle_ (ce qui est bon pour un joueur est mauvais pour l'autre).

On propose alors trois modes de jeu : 2 humains, humain vs random, humain vs minimax.

* L'extension majeure de cette version du projet consiste à fournir une fonction d'évaluation pour chaque jeu.
  Autant c'est facile au morpion ou au nim, autant c'est déjà délicat pour Othello voire infaisable pour les dames et les échecs.

* Il est possible d'envisager un moteur en Python avec un serveur web et un client web. C'est encore plus difficile...

Si ce projet vous intéresse, venez m'en parler, j'ai de quoi vous occuper trois ans sur le sujet.
