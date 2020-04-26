---
title: Diviser pour régner.
author: qkzk
date: 2020/04/26
weight: 1
---



### pdf: [pour impression](/uploads/docnsitale/algo/divide_n_conquer/diviser_pour_regner_print.pdf), [diaporama](/uploads/docnsitale/algo/divide_n_conquer/diviser_pour_regner_slides.pdf)

<!-- pandoc diviser_pour_regner.md -o diviser_pour_regner_print.pdf -->
<!-- pandoc -t beamer diviser_pour_regner.md --slide-level=2 -o diviser_pour_regner_slides.pdf -->

# Diviser pour régner

### Diviser pour régner:
###

> Classe d'algorithme où l'on découpe un problème en sous problèmes
> qui s'énoncent de la même manière

> et qu'on recompose à la fin pour former une solution

###

> C'est une approche "du haut vers les bas".

###

> Généralement, les algorithmes sont récursifs

# Recherche du maximum dans une liste

On dispose d'un tableau de nombres, on en cherche le plus grand élément.

```
tableau = [5, 71, 23, 45, 28, 89, 63, 39]
```

## Algorithme itératif naturel

On a déjà vu un algorithme en première :

1. On initialise `max = tableau[0]`, on parcourt élément par élément,
2. Pour chaque élément `elt` du tableau,

    Si `elt > max` alors `max = elt`
3. On retourne `max`

## Version diviser pour régner


fonction `maximum`:  `tableau ---> entier`

0. Le maximum d'un tableau de taille 1 est son unique élément.
1. On sépare le tableau en deux parties (sensiblement de même taille),
2. on retourne le plus grand des maxima des parties gauche et droite.

```
tableau = [5, 71, 23, 45, 28, 89, 63, 39]
```

##

1. séparer

    ```
            [5, 71, 23, 45, 28, 89, 63, 39]
                  /                 \
          [5, 71, 23, 45]       [28, 89, 63, 39]
            /       \             /         \
        [5, 71]   [23, 45]     [28, 89]   [63, 39]
        /   \      /    \       /   \       /   \
    [5] , [71],  [23], [45], [28],  [89], [63], [39]
    ```

##

2. Recombiner : on ne garde que le plus grand de chaque paire

    ```
    [5, 71],   [23, 45],  [28, 89],  [63, 39]
      \           /           \        /
      [71]      [45]         [89]     [63]
          [71, 45]             [89, 63]
               \                 /
               [71]          [89]
                    [71,  89]
                        |
                       [89]
    ```


## Est-ce plus efficace ? Non... c'est même plus lent !

![maximum](/uploads/docnsitale/algo/divide_n_conquer/figure/maximum.png)\



## Recherche d'un élément dans une liste (pas forcément trié)

On dispose d'un tableau d'entiers. On cherche à savoir s'il contient un élément.

## Version itérative (cf première)

fonction `chercher` : `(tableau, clé) ----> booléen`

1. on initialisé `trouvé = Faux`
2. on parcourt le tableau élément par élément:

    * Si `élément == clé`, alors `trouvé = Vrai`

3. on retourne `trouvé`

## Version diviser pour régner


fonction `chercher` : `(tableau, clé) ----> booléen`

1. Pour un tableau de taille 1, il contient la clé si valeur est la clé
2. On sépare le tableau en deux parties sensiblement de même taille (gauche et droite)
2. Le tableau contient la clé si \
    `chercher(gauche, clé)` ou `chercher(droite, clé)`\
     est vrai.

## Exemple

```
tableau = [4, 10, 20, 5]
clé = 10
```

A-t-on `clé` dans `tableau` ?

## Exemple

```
clé = 10
                 [4, 10, 20, 5]
diviser      [4, 10]       [20, 5]
diviser     [4]   [10]     [20]   [5]
combiner   Faux ou Vrai | Faux ou Faux
combiner       Vrai    ou    Faux
combiner              Vrai
```

## C'est mieux cette fois ??? Toujours pas.

![Recherche](/uploads/docnsitale/algo/divide_n_conquer/figure/recherche.png)\

Le coût est toujours linéaire, avec un coefficient assez mauvais.

## Pourquoi est-ce inefficace dans ces cas ?

* Pour le maximum, on fait autant de comparaison que dans la méthode itérative.
* Pour la recherche on fait autant de comparaison ET on ajoute `n-1` "Vrai ou Faux".

## Quand est-ce intéressant ?

* **Quand on a une structure particulière,**
* **Quand on peut éviter beaucoup d'étapes**
* **Quand on peut remplacer un calcul coûteux par un calcul moins coûteux,**

## Dichotomie : c'est diviser pour régner

En première on a vu la recherche dichotomique, rappelons rapidement le principe

On cherche **dans un tableau trié** la présence d'un élément.

* On initialisé `trouvé = False`
* On regarde l'élément central du tableau,
* S'il est égal à la clé : `trouvé = Vrai`
* S'il est plus grand que la clé, on cherche entre le début et la _valeur centrale_,
* Sinon, on cherche entre _la valeur centrale_ et la fin,

## Dichotomie : récursif

La version que nous avions étudiée était itérative.

On peut l'écrire en récursif.

En Python, ce n'est pas plus rapide :(

Python, n'est pas un langage _fonctionnel_, les récursions ne sont pas optimisées.

## Mais

![dichotomie](/uploads/docnsitale/algo/divide_n_conquer/figure/dichotomie.png)\

## Calculer la puissance d'un nombre

Comment calculer $3^7$ ?

$$3^7 = 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3$$

C'est déjà un algorithme !

## Algorithme naïf pour $y^n$

Puissance : $(y, n) \mapsto  y^n$

1. On initialise $p = 0$ et $i = 0$
2. Tant que $i < n$ faire
    * $p = p \times y$
    * $i = i + 1$
3. Retourner $p$

## Complexité ?

Clairement linéaire. Une seule boucle qui itère autant de fois que la puissance
voulue.

## Exponentiation rapide


$ExpoRapide : (y, n) \mapsto y^n$

Si $n = 0$ alors

* retourner $1$

Sinon si $n$ est pair

* $a = ExpoRapide(y, n // 2)$
* retourner $a \times a$

Sinon

* retourner $y * ExpoRapide(y, n - 1)$

## Vitesses

![expo](/uploads/docnsitale/algo/divide_n_conquer/figure/exponentiation.png)\

##

![expo](/uploads/docnsitale/algo/divide_n_conquer/figure/expon_rapide_natif.png)\

## Conclusion

La méthode **_diviser pour régner_** :

* découper le problème en sous-problèmes qui s'énoncent de la même manière
* résoudre les cas limites
* combiner les solutions

## Algorithmes récursifs, implémentation

### Algorithmes

Les algorithmes présentés s'énoncent facilement de manière récursive.

Ce ne sont pas toujours les meilleurs.

### Implémentation

Elle n'est pas toujours plus efficace. Cela dépend du langage employé.

<!--
## Exos

 Utiliser le principe de la recherche dichotomique pour rédiger une fonction Caml calculant la
racine carrée entière d’un entier n ∈ N, à savoir E(sqrt(n)), avec un coût logarithmique -->
