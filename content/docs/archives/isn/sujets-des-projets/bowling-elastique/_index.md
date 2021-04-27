---
author: qu3nt1n
date: 2018-12-25 22:20:33+00:00
draft: false
title: Bowling elastique
weight: 2
---

## PRESENTATION :


Version très appauvrie du BOWLING.

On est loin des [trucs usuels...](https://www.jeuxjeuxjeux.fr/jeux/bowling)
On lance une boule avec "presser, relâcher" vers le haut.
La boule entre en collision avec les quilles qui changent de couleur.
Après quelques secondes, les distances parcourues par les billes s'ajoutent et forment le score.

[video width="518" height="906" mp4="/uploads/uploads/2018/12/bowling_qkzk.mp4" loop="true" autoplay="true"][/video]


## PRINCIPE :


La piste est vue d'au dessus. Les quilles sont modélisées par des disques qui se déplacent comme des boules...
La vitesse de la boule est calculée par les différences de position des événements "mousedown" "mouseup" (attention, cette détection d'événements tend à merder pour une raison inconnue).

La boule et les quilles s'entrechoquent en suivant un [modèle de choc élastique](https://fr.wikipedia.org/wiki/Choc_%C3%A9lastique) (ie. conservation de la quantité de mouvement). Il n'y a pas de perte d'énergie par frottement, les objets ne roulent pas, ne glissent pas les uns sur les autres. Les objets avancent indéfiniment. etc.

Les dimensions des objets sont réalistes, hormis la longueur de la piste, tout est fidèle.


## OBJETS


Boule et quilles sont des instances de classes définies à part.
Chacun de ces objets possède sensiblement les mêmes propriétés.
J'aurais pu créer une classe mère et hériter.
Utiliser les classes via un constructeur est indispensable pour gérer correctement les éléments. Cela alourdit un peu le développement mais rend le code assez lisible finalement.


## CALCULS


Il est nécessaire de définir les outils permettant de calculer les données.
On peut envisager d'utiliser [mathjs](http://mathjs.org/index.html) qui contient certainement de quoi se simplifier la tâche.

Le calcul des vitesses après choc n'est pas si compliqué qu'il en a l'air.

Ces méthodes sont bien connues mais relativement peu documentées.

Voici donc [de quoi vous éviter quelques heures de recherche](http://www.cromod.fr/2016/11/18/modelisation-des-chocs-elastiques/).


## COLLISIONS


C'est la partie la plus délicaite. En particulier il faut s'assurer d'éviter un gros écueil : les collisions devant être détectées à chaque itération de la boucle de rafraîchissement, celle-ci doit laisser le temps aux objets de s'éloigner avant de modifier encore les vitesses...

Plusieurs solutions existent mais celle développée en Python dont je parle plus haut fonctionne proprement, la mienne est mauvaise.


## DIFFICULTES





* Les classes : **
* Détecter un choc : *
* Créer les fonctions mathématiques de calcul (hors choc élastique): **
* Choc élastique (nouvelles vitesses) : ***
* S'assurer que les physiques fonctionnent : *****



## EXTENSIONS


Le sujet est très vaste...
Mon adaptation ressemble beaucoup plus à un jeu de billard qu'à autre chose...
Il est possible d'illustrer le [mouvement Brownien](https://fr.wikipedia.org/wiki/Mouvement_brownien) via ces principes.

[video width="700" height="818" mp4="/uploads/uploads/2018/12/mouvement_brownien.mp4"][/video]

On peut aussi, une fois les collisions intégrées, faire mumuse avec les graphiques et appeler ça de l'art...

[video width="760" height="910" mp4="/uploads/uploads/2018/12/collisions_simples.mp4"][/video]

Se rapprocher du vrai bowling va demander trop d'efforts, il vaudrait mieux repartir de 0 et envisager de la fausse 3D (cf. le projet "Bowling parallax")
Le calcul des scores du bowling est un exercice prisé des développeurs (en particulier américains). Il est possible d'intégrer un vrai calculateur de score ou d'en créer un soi même.

Toujours dans cette direction, on peut soigner les graphismes...


## Cahier des charges





* Créer boules, quilles avec des instances de classe via un constructeur.
* Changer leurs paramètres via des fonctions extérieures.
* Le projet nécessitant beaucoup d'objets, il faut factoriser le code au maximum (ie. éviter d'écrire plusieurs fois la même chose et réutiliser un maximum d'outils).
* Réaliser les calculs mathématiques (idéalement) ou en utilisant des librairies.
* Intégrer un modèle de choc élastique, il faudra le présenter rapidement.
* Définir un canvas et une boucle de rafraîchissement (afficher, déplacer, calculer les collisions).
* On se contentera d'une vue en 2D. Il est possible de faire de la fausse 3D mais les collisions avec le
* Afficher puis animer les objets à l'écran (astuce pour le débogage : arrêter le rafraîchissement dès qu'une collision est détectée, ajouter ensuite un bouton pause permettant de faire la même chose).
* Intégrer un moyen de lancer la boule. Différentes solutions sont possibles, j'ai opté pour celle demandant le moins d’interaction du joueur (presser, relâcher).
