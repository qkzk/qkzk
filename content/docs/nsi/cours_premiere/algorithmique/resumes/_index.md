---
title:
- 9 - Résumés
theme:
- Metropolis
author: qkzk
weight: 0
---

# Programme

| Contenus                                    	| Capacités attendues                                                                                                                                              	| Commentaires                                                                                                                                                          	|
|------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Parcours séquentiel d’un tableau            	| Écrire un algorithme de recherche d’une occurrence sur des valeurs de type quelconque. Écrire un algorithme de recherche d’un extremum, de calcul d’une moyenne. 	| On montre que le coût est linéaire.                                                                                                                                   	|
| - | |
| Tris par insertion, par sélection           	| Écrire un algorithme de tri. Décrire un invariant de boucle qui prouve la correction des tris par insertion, par sélection.                                      	| La terminaison de ces algorithmes est à justifier. On montre que leur coût est quadratique dans le pire cas.                                                          	|
| - | |
| Algorithme des k plus proches voisins       	| Écrire un algorithme qui prédit la classe d’un élément en fonction de la classe majoritaire de ses k plus proches voisins.                                       	| Il s’agit d’un exemple d’algorithme d’apprentissage.                                                                                                                  	|
| - | |
| Recherche dichotomique dans un tableau trié 	| Montrer la terminaison de la recherche dichotomique à l’aide d’un variant de boucle.                                                                             	| Des assertions peuvent être utilisées. La preuve de la correction peut être présentée par le professeur.                                                              	|
| - | |
| Algorithmes gloutons                        	| Résoudre un problème grâce à un algorithme glouton.                                                                                                              	| Exemples : problèmes du sac à dos ou du rendu de monnaie. Les algorithmes gloutons constituent une méthode algorithmique parmi d’autres qui seront vues en terminale. 	|


---

# Parcours séquentiel d'un tableau

**Attendus :** Écrire un algorithme de recherche d’une occurrence sur des valeurs de type quelconque. Écrire un algorithme de recherche d’un extremum, de calcul d’une moyenne.

**Commentaire :** On montre que le coût est linéaire.

## Les tableaux en informatique

Un tableau est une série d'objets, généralement situés côte à côté dans la
mémoire.

On suppose pouvoir parcourir le tableau, élément par élément.

## Les tableaux en Python

En Python, pour illustrer les tableaux, on utilise les objets `list`.

Pour le tableau `T=[0, 1, 2, ..., 10]`, on peut :

~~~python
# le définir à la main :
T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# utiliser un range :
T = list(range(11))
~~~


## Recherche d'un élément dans un tableau

**Contexte :** on dispose d'un tableau, par exemple `T=[0, 1, 2, ..., 10]`.

On veut savoir si un nombre $x$ figure dans le tableau.
### Algorithme :

~~~
fonction (tableau T, objet x) ---> booléen:
  Pour chaque élément e de T,
    Si e = x, alors on renvoit Vrai
  Si la boucle se termine, on renvoit Faux.
~~~

En Python :

~~~python
def parcours_sequentiel(tableau, x):
  for elt in tableau:
    if x == e:
      return True
  return False # on n'arrive ici que si l'élément n'est pas dans le tableau
~~~


## Recherche d'extremum

**Contexte :** On cherche la valeur extrème d'un tableau de nombres T.

### Algorithme

~~~
fonction maximum(tableau T, nombre x) ---> nombre:
  On affecte à max la valeur de l'élément d'indice 0 du tableau.
  Pour chaque élément e du tableau:
    si e > max:
      max = e
  renvoyer max
~~~

En Python :

~~~python
def maximum(tableau):
  m = tableau[0]
  for elt in tableau:
    if elt > m:
      m = elt
  return m
~~~


## Moyenne des éléments d'un tableau

**Contexte :** On calcule la moyenne d'un tableau de nombres

### Algorithme

~~~
fonction moyenne(tableau T, nombre x) ---> nombre:
  On affecte à Somme la valeur 0
  On affecte à Effectif la valeur 0
  Pour chaque élément e du tableau:
    Somme = Somme + e
    Effectif = Effectif + 1
  renvoyer Somme / Effectif
~~~

En Python :

~~~python
def moyenne(tableau):
  somme = 0
  effectif = 0
  for elt in tableau:
    somme += elt
    effectif += 1
  return somme / effectif
~~~

Version courte qui n'illustre pas le programme :

~~~python
def moyenne2(tableau):
  return sum(tableau) / len(tableau)
~~~

Difficile de comprendre ce qui se passe réellement avec cette version !


# Recherche dichotomique dans un tableau trié

**Attendus :** Montrer la terminaison de la recherche dichotomique
à l’aide d’un variant de boucle.

**Commentaire :** Des assertions peuvent être utilisées.
La preuve de la correction peut être présentée par le professeur.


### Le coût est linéaire

Le "coût" désigne ici le nombre d'opérations qu'on effectue lors d'un parcours
séquentiel.

Qu'on soit en train d'afficher les valeurs ou de calculer quelque chose, on réalise
les mêmes opérations à chaque parcours.

De plus, lorsqu'on accède à un élément d'un tableau, il faut toujours le même temps
d'exécution.

Nous allons compter les opérations nécessaires au calcul de la moyenne.
Parce qu'on travaille avec un tableau, on peut supposer que ces opérations prennent toutes
le même temps d'exécution.


~~~
fonction moyenne(tableau T, nombre x) ---> nombre:
  On affecte à Somme la valeur 0
  On affecte à Effectif la valeur 0
  Pour chaque élément e du tableau:
    Somme = Somme + e
    Effectif = Effectif + 1
  renvoyer Somme / Effectif
~~~

On note $nombre$ le nombre d'opérations.

* début de l'algorithme : $nombre=0$
* `On affecte à Somme`, `on affecte à Effectif`... : $nombre=2$
* `Pour chaque élément e du tableau`:
  * on note $N$ le nombre d'éléments du tableau,
      ces opérations seront répétées $N$ fois.

      `Somme =  Somme + e` : 2 opérations

      `Effectif = Effectif + 1` : 2 opérations

      Dans la boucle complète il y a donc : $4 \times N$ opérations

  * A la fin de la boucle : $nombre = 4\times N + 2$
* `renvoyer... ` : $nombre = 4\times N +3$

En considérant que le tableau est immense, le nombre $3$ est _négligeable_ devant $N$.
On peut considérer que notre décompte $nombre \leq 5 \times N$, qui est une fonction linéaire.


Qu'est ce que cela signifie en pratique ?

* Si votre algorithme est programmé (implémenté) dans un programme qui nécessite 1 seconde pour calculer  la moyenne d'un tableau de taille 1000,
* il prendra : 2 secondes pour un tableau de taille 2000,
* il prendra : 1000 secondes pour un tableau de taille 1 million etc.

on que _le coût est linéaire._

### coût = la complexité

En appliquant ces méthodes de décompte, on peut ranger les algorithmes en catégories

* coût constant : on note $O(1)$
* coût linéaire : on note $O(n)$
* coût quadratique ($n^2$) : on note $O(n^2)$
* coût exponentiel ($2^n$) : on note $O(2^n)$

Plus un avance dans ces catégorie, plus l'algorithme est MAUVAIS...

Dans le tableau suivant on suppose avoir des algorithmes qui prennent tous 1 seconde à s'exécuter
pour un tableau de taille 1000.

On les exécute avec un tableau de taille 1000 fois plus grande, combien de temps vont-ils mettre
à s'exécuter ?

| catégorie   | complexité | $n=1000$  | $n=1.000.000$      |
|-------------|------------|-----------|--------------------|
| constant    | $O(1)$     | 1 seconde | 1 seconde          |
| linéaire    | $O(n)$     | 1 seconde | 1000 secondes      |
| quadratique | $O(n^2)$   | 1 seconde | 1.000.000 secondes |
| exponentiel | $O(2^n)$   | 1 seconde | $10^{302}$ secondes  |

$1.000.000$ secondes = $11$ jours.

Pour information, l'age de l'univers est de 13.7 milliards d'années soit :

~~~python
>>> age = 13.7 * 10 ** 9 * 365 * 24 * 3600
>>> age
4.320432e+17
~~~

La partie suivante s'intéresse à une autre manière de chercher les éléments d'un tableau : la dichotomie.

Cette fois le complexité est bien meilleure.


---

# Recherche dichotomique dans un tableau trié

## Principe de la recherche dichotomique

C'est celui du jeu du "plus ou moins"

* Un tableau trié : `T = [0, 1, 2, ... ,9]`
* L'élément 3 est-il dans le tableau ?
* L'objectif : répondre Oui ou Non en réalisant **le moins d'opérations** possibles.

## Pré condition

Pour cet algorithme on suppose une précondition : le tableau est
**trié par ordre croissant.**

C'est un effort important qui a déjà été réalisé et nous allons en tirer partie.


## Description de l'algorithme

* À chaque étape on teste la valeur centrale
* Si c'est l'élément cherché, on a trouvé et la réponse est Oui.
* Si la valeur centrale est supérieure à l'élément cherché on recommence avec
    la partie gauche
* Sinon on recommence avec la partie droite.
* Si la partie gauche ou la partie droite est vide, l'élément n'est pas dans le
    tableau et la réponse est : Non.

## Terminaison de l'algorithme

On se demande si cet algorithme va réellement se terminer ?
Il utilise une boucle, celle-ci n'est-elle pas infinie ?

À chaque étape, le nombre d'élément restant est divisé par deux (au moins).
En un nombre fini d'étapes, on n'aura plus qu'un élément à tester. Donc l'algorithme
se termine bien.


## Déroulé sur l'exemple, à la main.

`T=[0,1,2,...,9]`. On cherche 3.

1. On propose : 4.

    4 > 3 donc on recommence avec la partie avant 4 : `T1 = [0,1,2,3]`

2. On propose : 2

    2 < 3 donc on recommence avec la partie après 2 : `T2 = [3]`

3. On propose : 3

    3 = 3 donc **on a trouvé l'élément et la réponse est : Oui, 3 est dans T.**

## L'algorithme complet

~~~python
rechercheDicho(liste, clé)
  bas = 0
  haut = longueur(liste) - 1
  Tant que (bas < haut) :
    med = (bas + haut) // 2
    si clé == liste[med]:
      haut = med
      bas = med
    Sinon :
      si clé > liste[med]:
        bas = med + 1
      sinon:
        haut = med - 1
  si cle == liste[bas]:
    renvoyer Vrai
  sinon:
    renvoyer Faux
~~~

## Tableau pour présenter les étapes


| Tour            	| début 	| milieu 	| fin 	| trouvé ?    | `val > milieu` ?|
|-----------------	|-------	|--------	|-----	|------------	|----------------	|
| Avant la boucle 	| 0     	| /      	| 9   	| faux   	    | /              	|
| 1er tour        	| 0     	| 4      	| 9   	| faux   	    | 3 > 4 : faux   	|
| 2ème tour       	| 0     	| 2      	| 4   	| faux   	    | 3 > 2 : vrai   	|
| 3ème tour       	| 3     	| 3      	| 4   	| **vrai**   	| /              	|



---



## En Python

~~~python
def dicho(tableau, cle):
  bas = 0
  haut = len(tableau) - 1
  while bas < haut:
    med = (bas + haut) // 2
    if cle == tableau[med]:
      return True
    elif cle < tableau[med]:
      haut = med - 1
    else:
      bas = med + 1
  return cle == tableau[bas]
~~~

Attention, il faut aussi tester si la clé n'est pas égale à la dernière valeur !

## Verifications

~~~python
>>> tableau = list(range(10))
>>> for cle in tableau:
...    assert dicho(tableau, cle) # on trouve bien les 10 clés
>>> assert not dicho(tableau, -1) # -1 n'est pas dans le tableau
>>> assert not dicho(tableau, 11) # 11 n'est pas dans le tableau
~~~


---

# Tableaux à deux dimensions

On rencontre souvent des données qui sont présentées sous la forme d'un tableau
à deux dimensions :

~~~
1234
5678
~~~

Ces tableaux sont appelés des matrices. Celle-ci a 2 lignes et 4 colonnes

### Affecter une matrice à une variable

Chaque ligne de la matrice est dans un tableau.

~~~python
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8]]
~~~

### Atteindre un élément.

Disons qu'on veut atteindre le nombre 3. Il est dans la première ligne, 3ème
colonne :

~~~python
>>> mat[0][2]
3
~~~

On utilise deux série de [] pour les lignes puis pour les colonnes.

### Parcourir une matrice pour afficher ses éléments

On utilise toujours deux boucles **imbriquées** pour parcourir une matrice

~~~python
for ligne in mat:
  for cellule in ligne:
    print(cellule, end=', ')
~~~

Va nous afficher :

~~~
1, 2, 3, 4, 5, 6, 7, 8,
~~~

#### Application : calculer la somme des éléments "à la main"

~~~python
somme = 0
for ligne in mat:
  for cellule in ligne:
    somme += cellule
~~~

va nous renvoyer `36`

### D'autres représentations des matrices

On a vu dans le TP sur les tableaux à 2 dimensions qu'il était parfois nécessaire
de connaître la position d'une cellule dans la matrice, par exemple, pour
construire un dégradé de pixels.

Dans l'exemple suivant, non seulement nous parcourons le tableau à l'aide
d'indices, mais en plus les éléments de la matrice sont atteints autrement.

~~~python
from PIL import image
from IPython.display import display # si on travaille dans Colab
img = Image.new('RGB', (255, 128)) # nouvelle image, 255 de large, 128 de haut
pixels = img.load() # on charge la matrice des pixels

for x in range(255):
  for y in range(128):
    # attention à la notation [x, y] !!!
    pixels[x, y] = (255 - x, 0, 0)

display(img) # afficher dans colab
# img.show() # afficher dans la console
~~~


![Degradé rouge -> noir](/uploads/docsnsi/algo/degrade.jpg)
