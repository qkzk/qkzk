---
author: qu3nt1n
date: 2018-12-27 14:13:36+00:00
draft: false
title: Bowling Parallaxe
weight: 3
---

## Présentation




[video width="662" height="776" mp4="http://qkzk.xyz/wp-content/uploads/2018/12/bowling_paralax_1.mp4"][/video]

Dans cette version du jeu de Bowling on s'approche davantage des jeux de bowling type "bowling 3D"  concernant les graphismes et on s'en éloigne d'un point de vue de la physique.

On représente la piste en vue à la première personne avec les quilles dans le fond.
Le joueur est représenté par sa boule de bowling qu'il lance pour faire tomber les quilles.

Collisions, rigoles, calcul des scores sont implémentés mais grandement simplifiés pour rendre le jeu raisonnable.


## Principe


La piste est représentée en 2D avec une vue "avec point de fuite". Un point "à l'infini" est choisi au delà du décor et les bords de la piste convergent vers ce point.
Un lancer "tout droit" de la boule converge aussi vers ce point.
A chaque lancer on anime la boule, détecte les collisions, déclenche les animations des quilles et compte les points.
On initialise ensuite la partie avec le lancer suivant.


### Cahier des charges






* Il est important de comprendre le principe avant de se lancer. Une figure détaillée sur géogebra peut servir de point de départ. Je peux la fournir si nécessaire. Les coordonnées des objets doivent être bien connues et comprises. Il n'est pas possible de réaliser ce jeu "à l'arrache" en développant au fur et à mesure sans une compréhension globale du principe.
* Le décor est fixe. On ne dessinera d'abord QUE LA PISTE (un trapèze). inutile de passer des heures à faire des dessins, cela ne sert à rien.
* La boule est un objet qui a une position (x, y), un rayon (dépendant de y).
Plus y est proche de 0 (le haut de l'écran), plus le rayon est petit. Elle semble donc PLUS LOIN au fur et à mesure qu'elle monte sur l'écran.
(regarder la vidéo si ce n'est pas clair).
Ce principe est appelé parallaxe, on l'utilise souvent en jeux vidéos pour simuler la 3D.

* Les quilles sont toutes identiques, seule leur position à l'écran change.
Elles peuvent "tomber", c'est à dire tourner sur elle même et se déplacer de façon à simuler grossièrement une chute (cette partie est presque une extension, on peut se contenter de les colorier autrement pendant tout le développement).
Elles ont de nombreux statuts : "touchée", "tombée", "en jeu" (selon le 1er ou 2nd lancer)


* Les rigoles sont des trapèzes noirs représentés de manière fixe.
On détermine quand la boule y entre en résolvant une équation affine :
_ si (x< telle fonction de y) alors (suivre la rigole de gauche) _pour la rigole de gauche
_si (x> autre fonction de y) alors (suivre la rigole de droite)_
* Le lancer d'une boule s'effectue en 2 temps. On se place sur l'écran et on fait glisser la boule avec la souris. On calcule alors une vitesse et la boule se déplace.
Pour rendre le jeu jouable, on mesurera l'écart des x entre un "glisser" tout droit et le "glisser" du joueur et on adaptera la trajectoire de la boule. Cela peut paraître compliqué mais rendra l'ajustement facile.
Pour le développement on introduira un lancer par pression sur "espace" qui va forcement tout droit.
* Les collisions sont gérées de manière très très simplifiée :
Si la boule passe trop près d'un quille en jeu, celle-ci devient "touchée". Elle devient alors "tombée". On garde la liste des quilles "touchées".

* Si certaines combinaisons sont touchées, cela déclenche un strike et toutes tombent.
* D'autres combinaisons font tomber certaines quilles à coup sûr.


* Les scores sont grandement simplifiés par rapport aux règles du bowling.

  * 12 tours. Fin de partie au 13ème (on développera avec moins, bien sûr)
  * 2 lancers par tours. Un strike fait passer au premier lancer du tour suivant.
  * Chaque boule rapporte un point, un strike (toutes les quilles au premier lancer) en ajoute 10. Un spare (toutes les quilles après le second lancer) en ajoute 5.





## Extensions





* Améliorer la physique du jeu. Les possibilités sont infinies :

  * collisions des quilles entre elles,
  * choc élastique entre les objets,


* Graphismes. De toute évidence, il y a de la marge. Là aussi c'est infini.
* Interface. Les données apparaissent simplement dans des balises HTML. On pourrait faire apparaître les informations à l'écran. Je n'avais plus le temps de m'en occuper.
* Contrôles. Le principe est sommaire... On peut chercher d'autres manières de faire. Les développeurs ont beaucoup de mal avec ce point, d'ailleurs.
