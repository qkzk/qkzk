---
title:
- Les algorithmes de tris - Résumé
subtitle:
- NSI 1ère
author:
- QK
theme:
  metropolis
weigth:
  2

---

## Définition

Algorithme de **tri**

Algorithme qui, partant d'un tableau, renvoie une version **ordonnée** du tableau.
$$[5,1,4,3,2] \rightarrow [1,2,3,4,5]$$


## Tris par comparaison

Tous les algorithmes étudiés reposent sur les _comparaisons_.
Tout ce qu'on peut faire c'est :

* comparer deux éléments entre eux et choisir le plus petit
* échanger deux éléments dans le tableau.

Et c'est suffisant.

Il existe de nombreux algorithmes de tri disposant de complexités différentes.

En première : tri par **insertion** et tri par **sélection**.

## Python

Python utilise **TimSort** qui est plus efficace et mieux implémenté que ce
que nous ferons.

```python
>>> tableau = [4, 3, 1, 2]
>>> sorted(tableau) # renvoie une copie triée
[1, 2, 3, 4]
>>> tableau # l'objet de départ N'EST PAS MODIFIÉ
[4, 3, 1, 2]
>>> tableau.sort() # trie DANS l'objet, ne renvoie rien
>>> tableau # l'objet de départ EST MODIFIE
[1, 2, 3, 4]
```

## Tri par sélection

### Description

On cherche à trier des boîtes. Tout ce qu'on peut faire c'est le comparer 1 à 1 et les échanger.

### Pseudo code

```
Je débute avec un alignement vide de boîtes triées
Tant qu'il y a des boîtes non triées :
   Je cherche la plus légère parmi les boîtes non triées
   Je la place à la suite des boîtes déjà triées.
fin Tant que
```

Et pour la fonction `trouver la boite la plus légère` :

```
Entrée : Des boîtes
Sortie : La boite la plus légère
Effet de Bord : Enlève une boite

Je prends une boîte (main gauche)
Pour chacune des autres (main droite) :
    Si elle est plus légère que la boite dans ma main,
    Alors j'échange.
	Fin Si
	Je mets l'autre de côté.
Fin Pour
```

### Python

```python
def selection(tableau):
    '''
    tri par sélection d'un tableau.
    @param tableau: (list) objets pouvant être comparés dans Python
    @return: None
    @Effet de bord: modifie le tableau
    '''
    n = len(tableau)
    for i in range(n):
        m = i  # on cherche l'indice du min
        for j in range(i+1, n):
            if tableau[m] > tableau[j]:
                m = j
        tableau[m], tableau[i] = tableau[i], tableau[m]  # on echange

```



### Exemple

| Triés        	| Non Triés    	| Plus petit restant 	|
|--------------	|--------------	|--------------------	|
| ()           	| (1, 3, 4, 2) 	| (1)                	|
| (1)          	| (3, 4, 2)    	| (2)                	|
| (1, 2)       	| (3, 4)       	| (3)                	|
| (1, 2, 3)    	| (4)          	| (4)                	|
| (1, 2, 3, 4) 	|              	|                    	|

## Tri par insertion



#### En français

```
    Je débute avec un alignement vide de boîtes triées
    Tant qu'il y a des boîtes non triées :
       Je choisis une boite
	   Je l'insère dans l'alignement de telle sorte
     qu'il reste trié
    fin Tant
```

et, pour l'opération **d'insérer :**

```
Entree : Un alignement de boîtes trié, une boîte b
Sortie : rien
Effet de bord: l'alignement reste trié

Prends la boîte la plus à droite (la plus lourde)
Tant que cette boite est plus lourde que b
     passe à la boite suivante
insère b à la droite de la boite courante
```

---

### Exemple

| Triés        	| Non Triés    	| Élément le plus à gauche 	|
|--------------	|--------------	|--------------------------	|
| ()           	| (1, 3, 4, 2) 	| (1)                      	|
| (1)          	| (3, 4, 2)    	| (3)                      	|
| (1, 3)       	| (4, 2)       	| (4)                      	|
| (1, 3, 4)    	| (2)          	| (4)                      	|
| (1, 2, 3, 4) 	|              	|                          	|


### Python

```python
def tri_insertion(tableau):
  '''
  tri par insertion d'un tableau.
  @param tableau: (list) objets pouvant être comparés dans Python
  @return: None
  @Effet de bord: modifie le tableau
  '''
  for i in range(1, len(tableau)):
    j = i
    while j > 0 and tableau[j-1] > tableau[j]:
      tableau[j-1], tableau[j] = tableau[j], tableau[j-1]
      j = j - 1
```

## Propriétés communes des tris par insertion et sélection

### Caractéristiques :

* Tris _stables_ : ils ne changent pas l'ordre de deux éléments "égaux"
* Tris en _place_ : ils n'utilisent pas plus de mémoire que le tableau initial


### Invariant de boucle et terminaison

Un _invariant de boucle_ est un propriété qui est vraie avant et après chaque tour d'une boucle.

Durant le tour n° `i` de la boucle extérieure :

* les `i` premiers éléments du tableau sont triés.
* le nombre d'élément à trier diminue de 1.

Donc ces algorithmes _trient bien la liste_ et _ils s'arrêtent_.

### Complexité

Ils sont de complexité **quadratique** : $O(n^2)$.
_Le nombre de comparaisons (et la durée d'exécution) sont proportionnels_
_au carré de la taille du tableau._
