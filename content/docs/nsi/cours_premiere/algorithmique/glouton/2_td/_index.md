---
title: '2. TD'
bookCollapseSection: true
author: qkzk
weight: 2

---

# Gloutons : 2. TD

pdf [pour impression](/uploads/docsnsi/algo/glouton/2_td.pdf)

## 1. Le problème du sac à dos

Un cambrioleur possède un sac à dos d'une contenance maximum de 30 kg.
Au cours d'un de ses cambriolages, il a la possibilité de dérober 4
objets A, B, C et D. Voici un tableau qui résume les caractéristiques de
ces objets :


| objet            | A     | B     | C     | D     |
|------------------|-------|-------|-------|-------|
| masse            | 13 kg | 12 kg | 8 kg  | 10 kg |
| valeur marchande | 700 € | 400 € | 300 € | 300 € |


On ajoute les contraintes suivantes :

* le sac à dos a une contenance de 30 kg
* le cambrioleur cherche à obtenir un gain maximum.


1. Déterminez les objets que le cambrioleur aura intérêt à dérober.
2. Quel critère pourrait-on choisir pour trier les objets ?
    Proposer un algorithme glouton pour résoudre le problème du sac à dos.
3. Retourne-t-il la solution optimale ?
4. Reprendre le problème avec les objets suivants :


    | objet            | A     | B     | C     | D     |
    |------------------|-------|-------|-------|-------|
    | masse            | 35 kg | 41 kg | 28 kg | 39 kg |
    | valeur marchande | 70 €  | 40 €  | 30 €  | 30 €  |



    a. Si le sac peut contenir 100 kg,
    b. Si le sac peut contenir 85 kg.

5. Écrire une fonction Python qui calcule les valeurs massiques d'une liste
    d'objets passés en paramètre.
6. Écrire une fonction Python qui renvoie le contenu d'un sac à dos depuis
    une liste d'objets et une contenance de sac à dos passés en paramètres.
    Cette fonction utilisera l'algorithme glouton présenté plus haut.

## 2. Le rendu de monnaie.

On considère un jeu de pièce et une somme à rendre.
Nous allons étudier deux situations générales, pour lesquelles l'algorithme
glouton retourne la solution optimale ou non.

1. On considère un jeu de pièce similaire à l'euro :
    1 cts, 2 cts, 5 cts, 10 cts, 20 cts, 50 cts, 1 €, 2 €, 5 €, 10 €, 20 €, 50 €,
    100 €, 200 €.

    Rappeler l'algorithme glouton qui renvoie les pièces à rendre sous la
    forme d'une liste à partir d'un jeu de pièces et d'un montant passés
    en paramètres.

2. Donner les étapes pour le rendu de 71€73

2. Écrire une fonction Python qui traite le problème exposé à la question
    précédente.

Cette fonction retourne toujours une réponse mais celle-ci n'est pas forcement
la meilleure.

3. Proposer un algorithme qui teste toutes les combinaisons possibles
    et renvoie la meilleure.

4. Comparer les complexités de deux algorithmes : glouton et exhaustif.

{{< expand "Système monétaire canonique" "...">}}

Afin de résoudre en pratique les problèmes de monnaie on crée des systèmes de monnaie
qui permettent **de rendre la monnaie de manière optimale en suivant l'algorithme glouton**.

Un tel jeu de pièce -- comme l'Euro -- est dit _canonique_.

Il faut donc comprendre qu'on prend le problème à l'envers : le système monétaire est inventé **pour** respecter l'algorithme glouton.

Cela n'a pas toujours été le cas et certains systèmes étaient notoirement mauvais.
{{< /expand >}}

## 3. Somme de $n$ nombres maximale

On cherche à sélectionner **cinq** nombres de la liste suivante en maximisant leur somme et en s'interdisant de choisir deux nombres voisins.

Ainsi, si la liste contient la séquence `1, 2, 3`, et qu'on choisit `2`, il ne sera plus possible de choisir `1` ou `3`.

`Liste = 15, 4, 20, 17, 11, 8, 11, 16, 7, 14, 2, 7, 5, 17, 19, 18, 4, 5, 13, 8`

1. Décrire une stratégie gloutonne pour résoudre ce problème.
2. Mettre en oeuvre cette stratégie sur cet exemple.
3. Vérifier que `20, 18, 17, 16, 15` est une solution acceptable.
4. Comparer ces solutions.

## 4. Retour sur le voyageur de commerce

_à traiter après avoir étudié le problème en TP machine_

On rappelle rapidement le principe du problème :

Un voyageur a ciblé plusieurs villes qu'il souhaite visiter. Il cherche un itinéraire passant par toutes ces villes, depuis un point de départ et revenant
à la ville de départ. Il ne doit passer qu'une et une seule fois par chaque ville.

Par exemple : Nancy, Metz, Paris, Reims, Troye, Nancy est un trajet possible.

|        | Nancy | Metz | Paris | Reims | Troyes |
|--------|-------|------|-------|-------|--------|
| Nancy  |       | 55   | 303   | 188   | 183    |
| Metz   |       |      | 306   | 176   | 203    |
| Paris  |       |      |       | 142   | 153    |
| Reims  |       |      |       |       | 123    |

1. Décrire la stratégie gloutonne.
2. Mettre en oeuvre la stratégie et mesurer la distance parcourue.
3. Comparer à : Nancy, Metz, Reims, Paris, Troyes, Nancy.
4. Estimer le nombre de trajets possibles (départ & retour à Nancy).

## 5. Le parc d'attractions

Vous visitez un parc d'attractions proposant des spectables à différents horaires. Voici les horaires des spectacles :

| Spectacle | A       | B           | C         | D         | E       | F       | G         | H         | I       | J         |
|-----------|---------|-------------|-----------|-----------|---------|---------|-----------|-----------|---------|-----------|
| Horaires  | 10h-11h | 10h30-11h30 | 11h-12h30 | 11h30-12h | 12h-13h | 13h-15h | 13h30-14h | 14h-15h30 | 15h-16h | 16h-17h30 |

Vous avez remarqué qu'il n'était pas possible d'assister à tous les spectacles puisque certains ont lieu
à des moments communs; Vous souhaitez assister à un maximum de spectacles. Quels spectacles choisir ?

Voici deux stratégies gloutonnes possibles :

* **Stratégie 1** : choisir le spéctacle dont l'heure de début arrive le plus tot parmi les spectacles
    dont l'heure de début est postérieure à l'heure de fin des spectacles déjà choisis. 
    Cette stratégie minimise le temps d'attente.
* **Stratégie 2** : choisir le spectacle dont l'heure de fin arrive le plus tôt parmi les spectacles
    dont l'heure de début est postérieure à l'heure de fin des spectacles déjà choisis.
    Cette stratégie maximise le temps restant aux autres spectacles.

1. Appliquer ces deux stratégies aux données.
2. Laquelle est la meilleure ?

_Remarque théorique_ : la seconde stratégie gloutone donne toujours la meilleure solution.

