---
title: Evolution des performances
bookCollapseSection: true
author: qkzk
theme: metropolis
weight: 3

---

### PDF [pour impression](./3_performances-Article.pdf) [diapos](./3_performances-Beamer.pdf)


# Évolution des performances

## Loi de Moore

**tous les 18 mois, le nombre de transistor par processeur double**

![loi de moore](https://upload.wikimedia.org/wikipedia/commons/a/a4/Loi_de_Moore.png)

## Loi de Moore

* Énoncée en 1965 par Gordon Moore (pdg d'Intel).
* Restée valable jusqu'en 2005 environ.

## Problème : la chaleur

À cause d'une contrainte physique : en effet plus on augmente la
fréquence d'horloge d'un CPU, plus ce dernier chauffe.

Mais... si la surface diminue, dissiper la chaleur devient impossible.

## Évolutions récentes des processeurs : de multiples coeurs.

Augmenter le nombre de cœurs présent sur un CPU !

## Mais qu'est qu'un cœur dans un microprocesseur ?

Un cœur est principalement composé :

* d'une UAL,
* de registres (R0, R1\...)
* d'une unité de commande

Un cœur est donc capable d'exécuter des programmes de façon autonome.

## Plusieurs coeurs sur une seule puce


Aujourd'hui (en 2019) on trouve sur le marché des CPU possédant jusqu'à 18 cœurs !

le Snapdragon 845 (Samsung Galaxy S9) possède 8 cœurs.

## Plusieurs coeurs = de meilleures performances ?

Pas forcement !

Tirer profit d'un CPU multicœur demande certaines techniques de programmation...

## Parallélisme

Les  différents cœurs d'un CPU se partagent l'accès à la mémoire vive

L'accès aux ressources devient un enjeu. L'état des ressources aussi !

## Parallélisme

* mémoire _123_ : nombre 50

* coeur 1 : exécute les instructions :

  * lire la mémoire à l'adresse _123_
  * fait la somme de cette valeur et du nombre 333
  * écrit le résultat à l'adresse _123_

* coeur 2 : exécute les instructions :

  * lire la mémoire à l'adresse _123_
  * si la valeur de l'adresse _123_ est > 333, afficher _"bonjour"_
  * sinon, afficher _"au revoir"_

## Parallélisme

* Si les instructions s'exécutent dans l'ordre :

    _C1_, **C2**, _C1_, **C2**, _C1_, **C2**, etc on affiche : _"bonjour"_

* Si les instructions s'exécutent dans l'ordre :

    _C1, C1, C1_, **C2, C2, C2**, etc. on affiche _"au revoir"_


## Parallélisme

Comment contrôler l'ordre dans lequel les instructions sont réalisées sur
plusieurs cœurs ?

Les processus communiquent entre eux par message...

_(rassurez vous, c'est hors programme)_
