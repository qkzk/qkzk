---
title: k plus proches voisins - exercices
weight: 2
---

## Trouver la classe avec les k plus proches voisins

Supposons que l’on a un problème de classification qui consiste à déterminer la classe d’appartenance de nouvelles instances $X_i$. Le domaine de valeurs des classes possibles est ${1, 2, 3}$.

Selon la base de connaissance suivante, déterminez à la main (ou à l'aide d'un tableur) la classe de l’instance $X_6$, dont les valeurs pour les attributs numériques $A1$ à $A5$ sont $<3, 12, 4, 7, 8>$, à l’aide de l’algorithme des k-voisins les plus proches (K-NN) avec $K=1$ puis $K=3$.

Montrez tous les calculs.

| Instances    |  A1 |  A2 |  A3 |  A4 |  A5 | Classe  |
| ------------ | --- | --- | --- | --- | --- | ------- |
| $X_1$        |  3  |  5  |  4  |  6  |  1  |  1      |
| $X_2$        |  4  |  6  | 10  |  3  |  2  |  2      |
| $X_3$        |  8  |  3  | 4   |  2  |  6  |  3      |
| $X_4$        |  2  |  1  | 4   |  3  |  6  |  3      |
| $X_5$        |  2  |  5  | 1   |  4  |  8  |  2      |

## Autre exemple simple

Soit les points de coordonnées suivantes :

$A(1, 6), B(2, 6), C(3, 1), D(4, 2), E(6, 0), F(7, 5), G(7, 3), H(10, 3)$

En utilisant la distance euclidienne, quels sont les deux plus proches voisins du point $P(5,5)$ ?

## Exemple tiré d'un _sujet 0_

Dans le quadrillage ci-dessous 14 points sont dessinés, dont 7 de la classe C1, avec des ronds noirs $\bullet$, et 7 de la classe C2, avec des losanges $\lozenge$. On introduit un nouveau point A, dont on cherche la classe à l'aide d'un algorithme des k plus proches voisins pour la distance géométrique habituelle, en faisant varier la valeur de k parmi 1, 3 et 5. Quelle est la bonne réponse (sous la forme d'un triplet de classes pour le triplet (1,3,5) des valeurs de k) ?


$~~~~~~$![knn](https://github.com/qkzk/data_colab/raw/master/img/214_knn.png)





## Couleur d'un fruit

On cherche à prédire la couleur d’un fruit en fonction de sa largeur ($L$) et de sa hauteur ($H$). \
On dispose des données d’apprentissage suivantes :

| largeur | hauteur | couleur |
| ------- | ------- | ------- |
| 2       | 6       | red     |
| 5       | 6       | yellow  |
| 2       | 5       | orange  |
| 6       | 5       | purple  |
| 1       | 2       | red     |
| 4       | 2       | blue    |
| 2       | 1       | violet  |
| 6       | 1       | green   |

Ces données sont placées dans un repère ($L$ en abscisse, $H$ en ordonnée).

![](/uploads/docsnsi/algo/knn/fruit-color.png)

L’objectif ici est d’étudier l’influence des voisins sur la propriété de couleur d’un fruit.

Soit $U$ le nouveau fruit de largeur $L = 1$, et de hauteur $H = 4$.

1. Indiquez pour chaque point sa couleur.
1. Quelle est sa couleur si l'on considère 1 voisin ?
2. Quelle est sa couleur si l'on considère 3 voisins ?
3. Plutôt que le vote majoritaire, on voudrait considérer le vote des voisins pondérés par la distance. Chaque voisin vote selon un poids $w$ inversement proportionnel au carré de sa distance  : $w = 1/d^2$. \
On prend  3 voisins, quelle est la couleur de $U$ ? \
Comparez vos résultats à ceux de la question 2.

## Distance sur des données non numériques

Arrivé dans la cantina de la planète Tatooine, Han Solo décide de donner des indications à Luke pour qu’il ne provoque pas les extraterrestres belliqueux. Il repère quelques caractéristiques et vous demande de l’aider à fournir des éléments à Luke pour ne pas créer de problèmes et donc pouvoir définir un extraterrestre belliqueux.

| *Couleur* | *Taille* | *Poids* | *Yeux par pair ?* | *Belliqueux* |
|-----------|----------|---------|-------------------|--------------|
| jaune     | moyenne  | léger   | non               | non          |
| jaune     | grande   | moyen   | oui               | oui          |
| vert      | petite   | moyen   | oui               | oui          |
| jaune     | petite   | moyen   | non               | non          |
| rouge     | moyenne  | lourd   | non               | non          |
| vert      | grande   | lourd   | non               | oui          |
| vert      | moyenne  | lourd   | non               | oui          |
| jaune     | petite   | léger   | oui               | oui          |


Élaborez une distance pour pouvoir mettre en œuvre KNN sur cet exemple.

## Distance sur des données mixtes

Après avoir mis un place un entrepôt de données pour stocker les résultats des votes à différentes élections, l’objectif est de maintenant d’exploiter les différentes données de cet entrepôt. Différents partis politiques font donc appel à vous pour les aider à mieux comprendre leurs électeurs.

Un parti cherche à comprendre la composition des votants pour son candidat. Il fait donc appel à vos services pour identifier les différents profils des votants.

On a par exemple les deux votants suivants :

* V1 : {F ; 43 ; NON ; 55.000 ; 14% ; CONTRE}
* V2 : {M ; 38 ; NON ; 28.000 ; 14% ; POUR}

les attributs correspondent à :

* sexe : {F ; M}
* âge : {min : 18 ; max : 102 ; std : 30 ; moy : 50}
* propriétaire : {OUI, NON}
* salaire annuel imposable : {min : 412 ; max : 350.000 ; std : 30.000 ; moy : 32.000}
* taux d'imposition : {0% ; 14% ; 30% ; 41% ; 45%}
* opinion sur le nucléaire : {POUR, CONTRE, NSP}

Définissez formellement une distance permettant de considérer tous les attributs pour mettre en œuvre KNN.

Donnez la distance de V1 à V2 avec cette définition.
