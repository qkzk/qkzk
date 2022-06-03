---
title:
- Parcours séquentiel : td
author:
- qkzk
weight: 1

---

### pdf : [pour impression](/uploads/docsnsi/algo/sequentiel/td_parcours_sequentiel.pdf)

# Se tester

## 1. Appartenance

1. Quel est le rôle du mot clé `in` en Python ?\ 
    Citez deux usages courants.

2. Que retournent ces instructions ?

    ```python
    >>> 3 in [1, 2, 7]
    >>> 4 in range(12)
    >>> '4' in range(12)
    >>> "ZA" in "AZALEE"
    ```

3. On rappelle cet algorithme, vu en cours :

    ```
    fonction (tableau T, objet x) ---> booléen:
      Pour chaque élément e de T,
        Si e = x, alors on retourne Vrai
      Si la boucle se termine, on retourne Faux.
    ```

    a. Quel est le rôle de cet algorithme ?
    b. Écrire un programme Python qui transcrive cet algorithme.
    c. Parmi les exemples présentés à la question 2, quels sont ceux
        pour lesquels votre programme Python obtient la même réponse
        que l'instruction avec `in` ?

4. Adapter l'algorithme précédent pour qu'il retourne soit :
    * le premier indice de $x$ si $x$ figure dans le tableau,
    * -1 si $x$ ne figure pas dans le tableau.

## 2. Recherche d'un élément maximal

On rappelle l'algorithme vu en cours :


```
fonction maximum(tableau T, nombre x) ---> nombre:
  On affecte à max la valeur de l'élément d'indice 0 du tableau.
  Pour chaque élément e du tableau:
    si e > max:
      max = e
  retourner max
```

1. Traduire cet algorithme en Python.
2. Quel est la complexité de cet algorithme ?
3. Démontrer que l'algorithme se termine.
4. Déterminer un invariant pour la boucle de l'algorithme.

# S'entraîner

## 3. Retourner un tableau

1. Proposer un algorithme qui prend un tableau et le retourne. Voici la
    signature attendue :

    ```
    retourner(tableau T) ---> tableau:
    ```

    Ainsi qu'un exemple :

    ```python
    >>> retourner([1, 2, 3])
    [3, 2, 1]
    ```

2. Traduire cet algorithme en Python.\
    On pourra (mais ce n'est pas la seule approche) utiliser l'opérateur `+`
    pour les objets `list` qui _concatène_ deux listes :

    ```python
    >>> [1, 2] + [3, 4]
    [1, 2, 3, 4]
    ```

## 4. Décompte d'éléments

1. Proposer un algorithme qui compte le nombre d'apparitions d'un élément
    dans un tableau.

    ```
    decompte(tableau T, element x) ---> int
    ```

    Exemple :

    ```python
    >>> decompte([1, 1, 2, 1, 1, 2, 1], 1)
    5
    >>> decompte(['a', 'b', 'ab', 'a'], 'a')
    2
    ```

2. Traduire cet algorithme en Python.
3. Adapter votre fonction en une fonction `frequence` qui calcule la fréquence
    d'un élément dans un tableau. (fréquence = effectif de la valeur divisé
    par effectif total)


## 5. Fonction mystere

Voici une fonction mystère :

```python
def mystere(mot: str) -> bool:
    i = 0
    j = len(mot) - 1
    while i <= j:
        if mot[i] != mot[j]:
            return False
        i = i + 1
        j = j - 1
    return True
```

1. Faire tourner cette fonction sur les mots `radar` et `radrar` (qui n'existe
    pas, je sais).
2. Quel est le rôle de cet algorithme ?
3. Démontrer que l'algorithme se termine.
4. Adapter le programme afin qu'il ne compte plus qu'une seule instruction
    `return`.
3. Proposer un algorithme alternatif réalisant la même chose utilisant une fonction introduite dans
    un exercice précédent.

## 6. Correction de l'algorithme `factorielle`

On rappelle la définition de la factorielle :

$0! = 1$ et $n! = 1 \times 2 \times 3 \times \cdots \times n$

Ainsi $1! = 1, 2! = 2, 3! = 6, 4! = 24$ etc.

On considère l'algorithme suivant :

```
factorielle(entier n) ---> entier:
    i = 0
    f = 1
    Tant que i < n:
        i = i + 1
        f = f * i
    retourner f
```

1. Vérifier les exemples cités plus haut pour cette fonction.
1. Justifier que la boucle n'est pas infinie.
2. Montrer, en utilisant la pré-condition $n \geq 0$, que la propriété :
    $$f = i! \text{ et } i \geq n$$

   est un invariant de la boucle.
3. Formuler une post-condition qui établit la correction de cette algorithme.

## 7. Puissance de 2

1. Écrire un algorithme utilisant une boucle _tant que_ permettant de déterminer
    si un entier $n$ strictement positif est une puissance de 2.
2. Montrer que la boucle _tant que_ se termine.
3. Montrer que l'algorithme produit le résultat attendu.

## 8. Le plus vieux

On dispose d'une liste de personnes et de leurs ages sous cette forme :

```python
personnes = [('Joe', 16), ('Zoé', 17), ('Martin', 15)]
```

1. Proposer un algorithme qui détermine le plus âgé des individus.

    ```python
    >>> plus_ages(personnes)
    'Zoé'
    ```

2. Déterminer un invariant pour la boucle de l'algorithme.
2. Traduire votre algorithme en Python.


## 9. Lettres consécutives

Proposer un algorithme qui prend en entrée un tableau de lettres et renvoie en sortie le nombre de fois où deux lettres consécutives sont identiques.

Par exemple :

```
nb_lettres_consecutives(["a", "a", "b", "c", "c", "c"])
```

vaut 3 (`a, a`, `c, c`, `c, c`)

et :

```
nb_lettres_consecutives(["a", "a", "a", "a", "c", "c"])
```

vaut 4.

## 10. Trace et sommes des matrices carrés

En algèbre, la _trace_ d'une matrice carrée est la somme de ses coefficients diagonaux.

Par exemple pour la matrice :

$$\begin{pmatrix}
1 & 2 & 3 \newline
4 & 5 & 6 \newline
7 & 8 & 9
\end{pmatrix}$$


* Cette matrice comporte 3 lignes et 3 colonnes (deux nombres égaux), on dit qu'elle est carrée _de taille 3_.
* Sa trace est $1 + 5 + 9 = 15$, somme des coefficients obtenus en suivant sa diagonale du haut à gauche, en bas à droite.

On considère une matrice carrée d'entiers représentée par des tableaux imbriqués :

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

1. Proposer une fonction qui calcule la trace d'une matrice carrée de taille quelconque.

La somme de deux matrices est obtenue en ajoutant les éléments termes à termes. Cette opération
est définie pour toute paire de matrices qui ont des nombres de lignes et de colonnes égales.

$$\begin{pmatrix}
1 & 2 & 3 \newline
4 & 5 & 6 \newline
7 & 8 & 9
\end{pmatrix} + 
\begin{pmatrix}
7 & 2 & 1 \newline
6 & 3 & 2 \newline
4 & 0 & 1
\end{pmatrix}
 = \begin{pmatrix}
8 & 4 & 4 \newline
10 & 8 & 8 \newline
11 & 8 & 10
\end{pmatrix}$$

2. Proposer une fonction `somme` qui prend deux matrices en paramètres (supposées de mêmes dimensions) et renvoie la matrice somme.

    _On pourra procéder en deux temps, en supposant d'abord que la matrice finale est déjà créée et ensuite en la créant_.
