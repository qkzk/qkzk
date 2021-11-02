---
author: qu3nt1n
date: 2016-07-01 13:01:10+00:00
draft: false
title: RogueLike
bookCollapseSection: true
weight: 8
---


# Rogue

_Projet Python à réserver aux élèves sachant déjà un peu programmer._<br>
_Pour vous situer sa difficulté, j'ai envisagé ce projet pour les futurs élèves
de terminale NSI (première NSI : 4h d'informatique par semaine, terminale NSI :
6h d'informatique par semaine)._

## Présentation

Rogue (voleur, bandit en anglais) est un jeu vidéo crée en 1980 pour les
terminaux Unix. C'est donc un jeu qui se joue en texte dans la console.

Le principe est de diriger un personnage, souvent représenté par un @,
dans des donjons dont les murs et les éléments (monstres, objets, portes etc.)
sont aussi représentés par des caractères.

Le joueur doit descendre d'un niveau à l'autre jusqu'à obtenir une amulette
et remonter. Sur son chemin il rencontre de nombreux ennemis de plus en plus
forts et doit les affronter. Il n'a qu'une seule vie et, généralement, aucune
indication sur ce qu'il faut faire ou les caractéristiques de ce qu'il
ramasse.

C'est un jeu très difficile.

C'est le premier jeu "open source" a avoir été largement distribué sur toutes
les plateformes.

## Roguelike

La simplicité apparente du jeu, sa légèreté, l'absence totale d'éléments
graphiques et sa large distribution ont généré un large enthousiasme chez les
développeurs.

Il existe d'innombrables roguelikes disponibles gratuitement et une large
communauté de développeurs est toujours active sur le sujet.

## Principe du projet

Le but de ce projet est de développer un roguelike le plus complet possible.

Contrairement au jeu d'origine, très difficile, ce projet ne l'est pas forcement.

Dans l'esprit des roguelikes modernes nous allons proposer différentes difficultés.

## Cahier des charges : hard

Un tutoriel complet est disponible à
[cette adresse](https://qkzk.github.io/rogueTuto). Il était en anglais et je
l'ai traduit pour vous.

Il est long mais n'est pas difficile à suivre. Le code complet étant disponible dès le
départ (il est à la fois bien écrit et bien documenté) il vous suffit de
le suivre.

Trois attentes :

1. Finir le tutoriel
2. Comprendre exactement ce qu'il fait et être capable de le justifier
3. Ajouter une extension bien programmée

Une extension est **indispensable**. Elle va nécessiter d'avoir compris le
fonctionnement complet du jeu.

Elle pourra prendre différentes formes :

1. Fin du jeu. Ajouter l'amulette de Yendor et permettre au joueur de remonter
2. Histoire. Ajouter des éléments "roleplay" quand on descend ou ramasse
  certains objets. L'histoire doit être vaguement cohérente et s'enchaîner
  proprement. Certains choix peuvent être proposés au joueur ainsi qu'une
  interaction avec les PNJ.

3. Moteur du jeu. Il est complet mais sommaire. On peut l'étendre de multiples
   manières.
    * Monstres : il n'y en a que 2... on peut en ajouter d'autres
    * Armes et armures : même idée.
    * Effets magiques : seuls trois sorts sont disponibles. même idée à nouveau...
4. Graphique : remplacer l'interface graphique désuète par de jolis
  sprites colorés (bon courage).

## Cahier des charges : hardcore

Si vous vous pensez très fort...

Le principe est beaucoup plus simple : **vous partez de 0.** <br>
C'est vous qui **créez tout le code.**

Vous pouvez vous aider, ou non, de la librairie
[libtcod](https://github.com/libtcod/python-tcod).<br>
Il est préférable de vous en servir, sans quoi le projet devient extrêmement difficile.

### Composants indispensables :

1. Joueur dans un donjon qui se déplace avec les flèches,
2. Ennemis à affronter en tour par tour,
3. Système de combat : points de vie, dégâts, mort des ennemis, du joueur,
4. Différents niveaux (ils peuvent être codés en dur),
5. Récompenses (objets à ramasser ou expérience),

### Composants optionnels :

1. Génération aléatoire des niveaux,
2. Déplacement des ennemis vers le joueur,
3. Champ de vision (carte qui se découvre au fur et à mesure, les murs restent connus mais les objets disparaissent dès qu'on ne peut plus les voir),
3. Variété et difficulté des ennemis,
3. Magie : boule de feu (effet de zone), éclair (cible l'adversaire le plus proche), confusion (sur une cible) etc.
4. Soin : potions de soins, sorts magiques (mana ?) etc.
5. Sauvegarde. Le jeu conserve votre progression en mémoire quand vous quitter et la restaure quand vous revenez. La mort du joueur efface la sauvegarde.

### Implémentation

Il est possible de procéder autrement mais je vous conseille fortement
d'utiliser des classes, en particulier pour toutes les entités qui peuvent
apparaître dans votre jeu.

Une entité c'est à peu près n'importe quoi : un personnage (joueur, non joueur),
un objet, un sort, un mur etc.

Ensuite, soit vous héritez, soit vous ajoutez des composants.

Le principe des composants est plus simple à programmer, vous n'aurez pas à
créer une nouvelle classe pour chaque nouvelle entité qui apparaîtra.

Une autre classe qui me parait indispensable : la gestion des tours. <br>
Pour cela, vous pouvez créer une classe qui suive l'état du jeu
(action, inventaire, mort etc.)<br>
Vous créez donc d'abord des états différents et en ajoutez au fur et à mesure.
<br>
Remarquons que durant son tour, le joueur réalise généralement plus d'une
action : il ouvre son inventaire et lance un soin qui échoue car il est au
maximum de ses points de vie. Il lance ensuite une boule de feu contre un
adversaire qui réussit.
<br>
C'est UN tour.

De nombreuses autres classes sont à envisager.

---

Si vous n'avez strictement rien compris à ce que j'ai écrit depuis
_implémentation_ je pense que ce cahier des charges n'est pas pour vous.
