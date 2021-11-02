---
author: qu3nt1n
date: 2017-07-02 13:26:54+00:00
draft: false
title: Sandpiles
bookCollapseSection: true
weight: 9
---

# les piles de sable abéliennes


[caption id="attachment_1291" align="aligncenter" width="599"]![Backtang2](/uploads/uploads/2017/07/Backtang2.png)
28 millions de grains sur une grille de 1024 x 1024[/caption]

Une **pile de sable abélienne** est un automate cellulaire modélisant sommairement une vraie pile de sable. Nous la voyons comme une grille infinie de cellules carrées. Chaque cellule peut comporter un certain nombre de grains.
Chaque seconde nous déposons un grain dans la cellule (0,0). Si le nombre de grains d'une pile est supérieur ou égal à 4 alors la pile s'effondre immédiatement et les grains partent simultanément vers les quatre cellules avoisinantes (à gauche, à droite, au dessus, en dessous).

![sandpiles_1](/uploads/uploads/2017/07/sandpiles_1.png)

![sandpiles_2](/uploads/uploads/2017/07/sandpiles_2.png)


![sandpiles_3](/uploads/uploads/2017/07/sandpiles_3.png)














De manière générale les voisins de la cellule (x,y) sont donc (x-1, y), (x+1, y), (x, y-1) et (x, y+1).

**Quelques remarques importantes :**



* Quand une cellule s'effondre, cela peut provoquer l'effondrement des cellules avoisinantes.
* Les avalanches s'arrêtent forcement car il n'y a qu'un nombre fini de grains à répartir sur une grille infinie.
* L'ordre des opérations n'a pas d'importance, le résultat sera toujours le même.

**Exemple**




    3 secs      4 secs

    .....        .....
    .....        ..1..
    ..3..        .1.1.
    .....        ..1..
    .....        .....

    15 secs     16 secs

    .....       ..1..
    ..3..       .212.
    .333.       11.11
    ..3..       .212.
    .....       ..1..



Voici une représentation de cette pile finale en colorant les cases :

[caption id="attachment_1295" align="aligncenter" width="181"]![](/uploads/uploads/2017/07/puiss_4-taille_5-steps_6-temps_0.00-color_grayscale_crop.png)
16 grains. 0 : blanc, 1 : gris clair, 2  : gris foncé, 3 : noir.[/caption]


### **Cahier des charges :**


L'objectif de ce projet est de réaliser un programme qui prenne en entrée un nombre n de grains à déposer et qui affiche le résultat des effondrements de la grille une fois stabilisée.
On produira une image, de dimensions optimales, présentant la configuration finale. Elle pourra être en niveaux de gris pour pouvoir être imprimée facilement.

Votre algorithme doit être capable de renvoyer rapidement l'image obtenue quand on dépose plus de 100.000 grains (afin de respecter la symétrie de la figure on dépose généralement une puissance de 2 au centre, donc ici 2 à la puissance 17).





[caption id="attachment_1302" align="aligncenter" width="840"]![puiss_17-taille_267-steps_132320-temps_88.88-color_hot](/uploads/uploads/2017/07/puiss_17-taille_267-steps_132320-temps_88.88-color_hot-1024x1012.png)
2 puissance 17 grains. La structure fractale apparaît clairement.[/caption]

**Plan envisageable**



1. Grille carré de taille 5 x 5 avec 4 puis 16 grains au centre. Produire une sortie en mode texte du résultat après stabilisation.
2. Amélioration de l'algorithme : davantage de grains, grille plus grande de taille prédéfinie.
3. Générer une image de qualité quelconque (cette partie est très délicate).
4. Proposer différents modes : génération de l'image, sauvegarde de l'image, enregistrement d'une étape sous forme de tableau de nombre etc.
5. Agrandir la taille de la grille quand cela est nécessaire uniquement.
6. Optimisation de l'algorithme pour réduire le temps de calcul.
7. Optimisation de l'image : précision, dimensions, couleurs, espace disque etc.
8. Génération d'une animation : une image à chaque étape, une image toutes les x étapes.
9. Les extensions sont infinies : dépôt aléatoire, dépôt en suivant un parcours spécifique, rencontre de deux sandpiles éloignées et étude des motifs etc.

_Pour des questions de temps je n'ai réalisé ce projet qu'en Python à l'aide des librairies **numpy** (calculs numériques optimisés pour d'énormes matrices) et **matplotlib** (qui permet de visualiser ce qui numpy produit). Python n'est pas optimal pour atteindre d'importantes dimensions et on obtient de meilleurs résultats en C ou dans un langage de programmation fonctionnelle. Ce projet est parfaitement faisable en javascript mais, à nouveau, il sera peut-être délicat d'atteindre de grandes dimensions._


### Informations complémentaires


On peut considérer qu'on dépose immédiatement un très grand nombre de grains sur la cellule ou qu'on les dépose un par un, cela ne changera pas le résultat final, seulement la vitesse d'exécution. De même, quand deux cellules doivent s'effondrer, l'ordre dans lequel on le fait n'importe pas. Cette propriété donne son qualificatif d'abélien aux piles de sables [_Niels Henrik Abel 1802-1829 - mathématicien norvégien connu pour ses travaux en analyse en algèbre_]. D'autres propriétés mathématiques sont sous-entendues dans ce terme, nous en parlerons plus tard.

Il faut remarquer que ce projet peut être écrit en quelques lignes à peine ! Des librairies de génération de sandpiles sont présentes dans de nombreux langages. Nous ne les utiliserons qu'en fin de projet, pour comparer l'efficacité et illustrer.

**Vous devez donc écrire vous même le code.**

Remarquons enfin qu'atteindre des dimensions intéressantes (~1 million de grains) demande une quantité hallucinante de calculs : le dépôt de 2 puissance 18 grains (~260 000 grains) conduit à 1.142.525.672 effondrements individuels... Mal programmé, cela peut demander un temps conséquent à une machine. En améliorant légèrement l'algorithme on peut réduire le nombre de transformations à 275.351 (en réalisant étape par étape, toutes les avalanches en même temps) et diviser le temps par un multiple de 10. On est encore loin des meilleurs algorithmes.

Enfin, si ce sujet est très étudié il n'en reste pas moins délicat. Les sandpiles sont peu documentées en français et on tombe rapidement sur des articles de recherche (en anglais) datant des années 1990.


##### **Quelques remarques sur l'histoire du sujet.**


Les sandpiles ont été découvertes (ou inventées) par _Per Bak_, _Chao Tang_ et _Kurt Wiesenfeld_ en 1987. Elles sont depuis très étudiées dans de nombreux domaines :



* En **physique** : elles sont une approche de modélisation des systèmes "granulaires" dont la complexité dépasse vite l'entendement et qui ne respectent pas les principes usuels de la physique macroscopique. Les grains pris séparément se comportent comme des solides mais dès qu'on en manipule une faible quantité alors les prédictions s'effondrent : ce ne sont plus vraiment des solides usuels et ce ne sont pas non plus des liquides. C'est encore un sujet brûlant en Physique et les applications concrètes nombreuses. Les sandpiles présentent une "complexité" (notion délicate à définir, voir plus bas) similaire à celle de vrais tas de sables... mais qu'on rencontre aussi dans de nombreux domaines !
* En **informatique théorique** : les sandpiles sont des **automates cellulaires** (ensemble de cellules qui se comportent de manière prédéfinie et automatique). On peut démontrer que ce sont des machines de Turing : en programmant correctement un sandpile, on peut lui faire faire n'importe quel algorithme ! (En théorie...)
* En **algèbre** : les sandpiles ont des structures très intéressantes. Correctement définis on y voit apparaître des groupes (*). En effet on peut réaliser des opérations sur les sandpiles et faire apparaître une addition, une soustraction, un élément neutre etc. C'est l'autre raison du terme "abélien". Il est à noter qu'une extension possible de ce projet est justement de s'intéresser à ces propriétés. Il existe une quantité incroyable de domaines dans lesquels on peut les appliquer.
* En **mathématiques et en informatique** : les sandpiles présentent des **structures fractales**. Le dépôt d'un grand nombre de grains au centre conduit à une image faisant apparaître des répétitions de formes exactement comme les autres fractales.![](http://static.nautil.us/5779_7d3d5bcad324d3edc08e40738e663554.png)


Ces propriétés ont conduit à une étude intense de ce sujet et à une généralisation à de nombreuses structures (graphes). On ne se contente plus de grilles carrées mais on dépose les grains sur les sommets d'un graphe et l'effondrement se déroule vers les sommets voisins. Et voici la troisième extension possible de votre projet : générer des grilles obtenues en changeant la forme de la grille ou le motif d'effondrement. Deux exemples pour des grilles hexagonales (chaque cellule a 6 voisins et s'effondre quand on atteint 6 grains) :

[caption id="" align="aligncenter" width="362"]![](http://4.bp.blogspot.com/-B-G-t3sMpNg/UL7OPxDYxLI/AAAAAAAAB6A/JQrwGnaig5s/s400/growing.JPG)
Quelques structures finales après dépôt de grains au centre[/caption]

[caption id="" align="aligncenter" width="360"]![](http://people.reed.edu/~davidp/sand/gallery/hex12.png)
La grille "identité" pour une grille hexagonale de largeur 12.[/caption]


### La notion de complexité auto-organisée


[caption id="" align="alignnone" width="1186"]![](http://iopscience.iop.org/1347-4065/53/1S/01AA02/downloadHRFigure/figure/MB13050Rfig01)
Hierarchical network device concept of the fractal atomic switch network composed of "small world" regions of densely interconnected nodes and integrated with a macroscopic electrical I/O platform (a). Voronoi diagram-based simulation of metallic fractal growth by electroless deposition of a randomly distributed network of self-similar nodes from randomly distributed copper microsphere seeds (b–d).[/caption]

[source](http://iopscience.iop.org/article/10.7567/JJAP.53.01AA02)

La renommée (scientifique) des sandpiles est due à l'autre notion qui a accompagné leur découverte : **celle de complexité auto organisée** (self-organized criticality). C'est la propriété des systèmes dynamiques qui ont un point critique (pensez à l'état de la neige instable sur une pente) et un attracteur (la neige est attirée par la terre et risque de tomber). Le moindre flocon peut déclencher l'avalanche !
On considère que c'est une des manières selon laquelle la complexité se manifeste dans la nature. Ces concepts ont donc été appliqués avec grand succès à d'innombrables domaines : géophysique, cosmologie physique, biologie de l'évolution, écologie, optimisation (en mathématiques), systèmes dynamiques (en informatique), économie, physique quantique, sociologie, étude du soleil, étude des plasmas de gaz, neurobiologie etc. Le sujet est très loin d'être épuisé.

L'image ci-dessus compare un modèle théorique (a) de réseau fractal avec une simulation d'accroissement d'un cristal métallique cuivre (b)-(c)-(d) dans des conditions particulières et qui dépassent mes connaissances en chimie. Il est possible de mesurer la complexité des deux structures et on s'aperçoit qu'elle vérifie des propriétés similaires à celle des sandpiles.

En faisant varier l'échelle (spatiale et ou temporelle) on fait apparaître les mêmes comportements de points critiques et de changement de phase mais sans devoir ajuster les paramètres d'entrée. Le système se dirige lui même vers un état critique.

![](https://www.tuxboard.com/photos/2013/01/Michael-Grab-pierre-equilibre-2.jpg)




Les pierres en équilibre sont instables mais ne sont généralement pas obtenues naturellement. Il faut "ajuster" le système pour qu'il atteigne ce point critique.

Pour nos sandpiles, l'état critique est une zone maximale, remplie de 3, et le changement de phase le fait d'ajouter un grain n'importe où dans cette zone en provoquant une avalanche.

![](https://github.com/esdalmaijer/abelian_sandpile/raw/master/abelian_sandpiles_10000_500x500_gray_hot_jet.png)


Voici ce qu'on obtient en déposant non plus tous les grains au centre mais en suivant des courbes complexes... Les structures sont très similaires à celles obtenues précédemment.



---





## Sources


Les sources d'inspiration sont nombreuses. L'[article wikipédia](https://en.wikipedia.org/wiki/Abelian_sandpile_model) est intéressant mais n'existe qu'en anglais. De même que [la vidéo](https://www.youtube.com/watch?v=1MtEUErz7Gg) de la chaîne Numberphile qui m'a donné envie de vous proposer ce projet.

[caption id="" align="aligncenter" width="1204"]![](http://people.reed.edu/~davidp/sand/gallery/dump.gif)
4 millions de grains au centre.[/caption]

La page du [mathématicien](http://people.reed.edu/~davidp/) figurant dans la vidéo et dont proviennent ces images : _Pr David Perkinson_.

L'[applet webGL](http://people.reed.edu/~davidp/web_sandpiles/) avec lequel vous pouvez vous amuser.

Et, pour conclure, deux vidéos hypnotisantes (à regarder chez vous en haute résolution) : [2x1 million de grains](https://www.youtube.com/watch?v=GViAq_IWOg4) et une [grille hexagonale avec 500.000 grains](http://(à regarder chez vous en haute résolution).) (rien ne vous contraint à le faire).



---





### Quelques mots sur la structure algébrique.


Intéressons nous exclusivement aux grilles carré de taille 3 x 3. Chaque grain du bord qui s'effondre disparaît.

On définit sur cet ensemble l'addition de 2 piles en ajoutant case par case :


    0 3 2   1 1 0    1 4 2     2 0 3    2 1 3    2 2 3    3 2 4    3 3 0
    1 2 1 + 1 0 1 =  2 2 2 ->  2 3 3 -> 2 4 3 -> 4 0 4 -> 0 2 0 -> 1 2 1
    0 1 3   3 1 2    3 2 5     3 4 1    4 0 2    3 2 2    4 1 3    0 2 3


Ouch !

Parmi ces piles on s'intéresse à **l'ensemble des cellules obtenues en ajoutant n'importe quelle pile à la pile maximale :**


    3 3 3
    3 3 3
    3 3 3


Cet ensemble est très particulier, il forme une structure de GROUPE mathématique.

Muni de cette "addition" de pile il comporte un élément neutre appelé ("identity" en anglais) :


    2 1 2
    1 0 1
    2 1 2


Cela signifie qu'en partant de n'importe quelle pile de cet ensemble particulier et en ajoutant cette pile identité on obtient la pile de départ !

par exemple :


    2 2 2   2 1 2   4 3 4    0 5 0    2 1 2    2 2 2
    2 2 2 + 1 0 1 = 3 2 3 -> 5 2 5 -> 1 6 1 -> 2 2 2
    2 2 2   2 1 2   4 3 4    0 5 0    2 1 2    2 2 2


Remarquons que la grille remplie de 0 fait la même chose... mais il n'est pas possible, en partant de la grille maximale d'arriver à la grille remplie de 0 en lui en ajoutant une autre.

Cette propriété se généralise à toutes les tailles... voici par exemple la sandpile "identité" de taille 500.

[caption id="" align="aligncenter" width="500"]![](https://i.stack.imgur.com/q8Sqm.png)
identity sandpile de taille 500 x 500 -  blue = 3, green = 2, red = 1, white = 0[/caption]

La première partie de la vidéo de Numberphile est consacrée à ce sujet.

Il n'est pas envisageable de trouver "à la main" cette pile identité et des algorithmes les produisant existent.

_Remarque du 2 juillet 2017 - je suis supposé trouver quelques heures un weekend pour décortiquer ces algorithmes et vous les proposer, ce n'est pas encore fait. On verra si j'y pense, si j'ai le temps..._
