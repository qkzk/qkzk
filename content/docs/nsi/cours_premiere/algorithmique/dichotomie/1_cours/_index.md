---
title: "Cours : dichotomie"
bookCollapseSection: true
author: qkzk
weight: 1

---

# Recherche dichotomique dans un tableau

pdf [présentation](/uploads/docsnsi/algo/dicho/dicho_exemple-Article.pdf) et [slides](/uploads/docsnsi/algo/dicho/dicho_exemple-Beamer.pdf)

## Présentation

{{< hint info >}}
La _recherche dichotomique dans un tableau trié_ est un algorithme efficace
qui permet de répondre à différentes questions :

* Ce tableau trié contient-il cet élément ?

ou

* Quel est l'indice de cet élément dans ce tableau trié ?
{{< /hint >}}


## Dichotomie vs recherche séquentielle

Bien sûr, on sait déjà comment répondre à une telle question :

on regarde les éléments un par un avec une boucle `for` et lorsqu'on rencontre l'élément, on fait quelque chose.

C'est une recherche séquentielle qui fonctionne parfaitement mais qui est beaucoup plus lente que la recherche
dichotomique.


{{< hint info >}}
La recherche _séquentielle_ s'applique à tous les tableaux.

La recherche _dichotomique_ ne s'applique qu'aux tableaux **triés** mais est **beaucoup plus rapide**.
{{< /hint >}}

## Principe

Il est similaire à la méthode efficace pour gagner au "plus ou moins".

{{< expand "Le jeu du plus ou moins" "...">}}
Votre adversaire a choisi un nombre entre 1 et 100 et vous devez le déviner.

Il ne peut répondre que par "c'est plus", "c'est moins" ou "gagné".

Une approche qui gagne toujours consiste à partir de 1 et augmenter de 1 en 1 :

* 1 ? C'est plus,
* 2 ? C'est plus, etc.

Elle termine toujours et trouve toujours la réponse. Pourquoi s'embêter ?

Parce qu'on peut gagner en 7 coups alors qu'il en faut 100 si l'adversaire choisit 100...

Comment gagner en 7 coups ?

**Choisir la valeur centrale parmi les valeurs restantes.**

Et c'est tout.


* La première approche (1, 2, 3...) est _séquentielle_, 
* La seconde approche (50, 25, 12...) est _dichotomique_.
{{< /expand >}}


## Contexte

* Un tableau trié : `T = [0, 1, 2, ... ,9]`

* L'élément 3 est-il dans le tableau ?

* L'objectif : répondre Oui ou Non en réalisant **le moins d'opérations** possibles.



## Dichotomie

* À chaque étape on teste la valeur centrale du tableau considéré
* Si c'est l'élément cherché, on a trouvé et la réponse est Oui.
* Si la valeur centrale est supérieure à l'élément cherché on recommence avec
    la partie gauche
* Sinon on recommence avec la partie droite.
* Si la partie gauche ou la partie droite est vide, l'élément n'est pas dans le
    tableau et la réponse est : Non.


## Déroulé sur l'exemple, à la main.

`T=[0,1,2,...,9]`. On cherche 3.

1. On propose : 4.

    4 > 3 donc on recommence avec la partie avant 4 : `T1 = [0,1,2,3]`

2. On propose : 2

    2 < 3 donc on recommence avec la partie après 2 : `T2 = [3]`

3. On propose : 3

    3 = 3 donc **on a trouvé l'élément et la réponse est : Oui, 3 est dans T.**

## L'algorithme


{{< hint info >}}
```python
rechercheDicho(liste, clé)
  bas = 0
  haut = longueur(liste) - 1
  Tant que (bas < haut) :
      med = (bas + haut) // 2
      si clé == liste[med]:
          bas = med
          haut = med
      sinon si clé > liste[med]: bas = med + 1
      sinon: haut = med - 1
  si cle == liste[bas]: renvoyer Vrai
  sinon: renvoyer Faux
```
{{< /hint >}}

## Même exemple, avec les variables


Voici un déroulé de l'algorithme à la main.

Notre tableau `T` est `[0, 1, 2, ..., 9]` et on cherche `3`.

On dispose des variables :

* `début`, `milieu`, `fin` qui sont des éléments du tableau
* `trouvé` qui est un booléen (vrai / faux)
* et `val > milieu` (booléen, qui va nous aider à choisir)

On présent les éléments dans une table :


### Déroulé

Voici un déroulé de l'algorithme à la main.

Notre tableau `T` est `[0, 1, 2, ..., 9]` et on cherche `3`.

* **Avant la boucle.** début, fin et trouvé sont initialisées (0, 9, faux). La variable milieu et le booléen `val > milieu` n'existent pas encore.



| Tour            	| début 	| milieu 	| fin 	| trouvé 	    | `val > milieu` 	|
|-----------------	|-------	|--------	|-----	|------------	|----------------	|
| Avant la boucle 	| 0     	| /      	| 9   	| faux   	    | /              	|





Notre tableau `T` est `[0, 1, 2, ..., 9]` et on cherche `3`.

1. **Premier tour.** On descend début et fin.

    On calcule milieu (0+9)/2 = 4.5 dont la partie entière est 4. Donc milieu = 4.

    Est-ce que 3==4 ? Faux.

    Est-ce-que "3>4" ? Faux. Dans ce cas, c'est `fin` qui prend la valeur de `milieu`



    | Tour            	| début 	| milieu 	| fin 	| trouvé 	    | `val > milieu` 	|
    |-----------------	|-------	|--------	|-----	|------------	|----------------	|
    | Avant la boucle 	| 0     	| /      	| 9   	| faux   	    | /              	|
    | 1er tour        	| 0     	| 4      	| 9   	| faux   	    | 3 > 4 : faux   	|



2. **Second tour.** On a descendu début, on donne à fin la valeur précédente de milieu (4). Et on calcule les nouveaux éléments. milieu = (0+4)/2 = 2 (entier).

    Est-ce-que 3==2 ? Faux.

    Est-ce-que 3>2 ? Vrai. Dans ce cas, c'est début qui change et prend la valeur de milieu + 1.




    | Tour            	| début 	| milieu 	| fin 	| trouvé 	    | `val > milieu` 	|
    |-----------------	|-------	|--------	|-----	|------------	|----------------	|
    | Avant la boucle 	| 0     	| /      	| 9   	| faux   	    | /              	|
    | 1er tour        	| 0     	| 4      	| 9   	| faux   	    | 3 > 4 : faux   	|
    | 2ème tour       	| 0     	| 2      	| 4   	| faux   	    | 3 > 2 : vrai   	|



3. **Troisième tour**. On a descendu la valeur de fin et donné à début l'ancienne valeur de milieu + 1 (3). Et on recommence.

    Milieu = (3 + 4)/2 = 3.5 dont la partie entière est 3. Est-ce-que 3==3 ? Oui.



    | Tour            	| début 	| milieu 	| fin 	| trouvé 	    | `val > milieu` 	|
    |-----------------	|-------	|--------	|-----	|------------	|----------------	|
    | Avant la boucle 	| 0     	| /      	| 9   	| faux   	    | /              	|
    | 1er tour        	| 0     	| 4      	| 9   	| faux   	    | 3 > 4 : faux   	|
    | 2ème tour       	| 0     	| 2      	| 4   	| faux   	    | 3 > 2 : vrai   	|
    | 3ème tour       	| 3     	| 3      	| 4   	| **vrai**   	| /              	|


L'algorithme est terminé et la sortie est "VRAI". Le nombre 3 est bien un élément du tableau [0, 1, **3**, 4, 5, ..., 9].



### Complexité

* **parcours séquentiel** : autant que d'éléments dans le tableau dans le pire des cas.
  Le parcours séquentiel prend (dans le pire des cas) $n$ étapes.
* **recherche dichotomique** (après le tri) : $\log_2 n$ étapes.
    $\log_2 n$ est (grosso modo) la taille de l'entier représenté en base 2 (= son nombre de bits).

## Conclusion

{{< hint info >}}
* La recherche dichotomique permet de gagner beaucoup d'étape par rapport au parcours
séquentiel du tableau.

* Elle nécessite d'avoir un tableau **trié** sans quoi on ne peut l'appliquer.

* Une recherche séquentielle dans un tableau de taille $n$ demande jusqu'à $n$ étapes,
* Une recherche dichotomique dans un tableau trié de taille $n$ demande $\log_2(n)$ étapes.
{{< /hint >}}

---

### Meilleure stratégie : recherche séquentielle ou tri + recherche dichotomique ?

Supposons partir d'un tableau _non trié_. Est-il plus efficace de le trier avant de faire une recherche ?

* Si on ne souhaite l'appliquer qu'_une_ seule fois, il n'est pas intéressant de trier avant de chercher. C'est trop long.

* Mais si on doit effectuer beaucoup de recherches dans le tableau et qu'il ne change pas, alors c'est plus envisageable.

