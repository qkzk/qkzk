---
title: Cours
theme: metropolis
weight: 1
bookCollapseSection: true
---

**Documents :** [diapos](dicho_slides.pdf) & [imprimable](dicho_cours.pdf)

---

Le tableau `T` contient-il `x` ? À quelle position ?

{{< hint info >}}
_C'est un problème déjà rencontré lors des parcours séquentiels. Nous allons étudier un algorithme beaucoup plus rapide... mais qui ne s'applique qu'aux tableaux **triés**_.
{{< /hint >}}

## Introduction : recherche par balayage

Déjà abordé lors des _[parcours séquentiels](/docs/nsi/cours_premiere/algorithmique/sequentiel/cours/#algorithmes-sur-les-tableaux-1)_

```python
x = 5
T = [11,  7,  9,  5, 15, 13,  3,  1]
      0   1   2   3   4   5   6   7
                  ^
```

{{< hint info >}}

```python
def recherche(T, x):
    Pour i allant de 0 à len(T) - 1:
        Si x == T[i]:
            renvoyer i
    renvoyer -1
```

{{< /hint >}}

{{< python title="Recherche par balayage">}}
def recherche(T: list, x: int):
    for i in range(len(T)):
        if x == T[i]:
            return i
    return -1

x = 5
T = [11, 7, 9, 5, 15, 13, 3, 1]

print(recherche(T, x))
{{< /python >}}

### Déroulé

```python
i = 0           5 != 11
i = 1           5 != 7
i = 2           5 != 9
i = 3           5 == 5
```

### Remarques

{{< hint warning >}}

1. La boucle étant bornée (`for`), l'algorithme termine toujours.

2. **Au pire `len(T)` étapes**. La coût calculatoire d'un parcours séquentiel est _linéaire_.
   {{< /hint >}}

## Recherche dichotomique

### Présentation

{{< hint info >}}
On suppose maintenant que le tableau `T` est **trié** par ordre croissant

```python
x = 5
T = [ 1,  3,  5,  7,  9, 11, 13, 15]
      0   1   2   3   4   5   6   7
```

{{< /hint >}}

**Stratégie du Jeu de "+ ou -"** : viser le centre des éléments restant et éliminer la moitié des nombres à chaque étape.

{{< hint info >}}
Donc : comparer la valeur centrale à `x` et **éliminer la moitié des valeurs restantes**
{{< /hint >}}

### Déroulé

1. Premier tour

   ```python
   x = 5
   T = [ 1,  3,  5,  7,  9, 11, 13, 15]
         g           ^               d
   ```

   ```python
   g = 0, d = 7
   m = (g + d) // 2 = (0 + 7) // 2 = 3
       x = 5 < T[3] = 7    =>   Chercher à gauche
   ```

   On recommence avec

   - `d = m - 1 = 2`
   - `g` inchangé

2. Second tour

   ```python
   x = 5
   T = [ 1,  3,  5,  7,  9, 11, 13, 15]
         g   ^   d
   ```

   ```python
   g = 0, d = 2
   m = (g + d) // 2 = (0 + 2) // 2 = 1
       x = 5 > T[1] = 3    =>   Chercher à droite
   ```

   On recommence avec

   - `d` inchangé
   - `g = m + 1 = 2`

3. Troisième tour

   ```python
   x = 5
   T = [ 1,  3,  5,  7,  9, 11, 13, 15]
            g=d
   ```

   ```python
   g = 2, d = 2
   m = (g + d) // 2 = (2 + 2) // 2 = 2
       x = 5 == T[2] = 5    =>   Trouvé !
   ```

   On peut renvoyer `2`.

## Construction de l'algorithme

{{< expand "" "Construction de l'algorithme" >}}


{{< columns >}}
**Précondition**\
**Plusieurs étapes**\
**Nombre inconnu d'étapes**\
**Arrêt**
<--->

`T` un tableau trié par ordre croissant\
Il faut une boucle\
Boucle non bornée (`while`)\
`g > d` donc `while g <= d:`\
 {{< /columns >}}

**Corps de la boucle**

`m = (g + d) // 2`

3 cas :

- Si `x == T[m]` $\quad\quad\Rightarrow\quad$ `return m`

- Si `x < m` $\quad\quad\qquad\Rightarrow\quad$ `d = m - 1`

- Si `x > m` $\quad\quad\qquad\Rightarrow\quad$ `d = m + 1`

**Et si la boucle termine ?**

- `T` ne contient pas `x` $\Rightarrow\quad$ `return -1`

{{< /expand >}}

## Codes à compléter

### Exemples pour tester votre fonction

{{< expand "" "..." >}}
```python
# tableau vide
assert recherche_dichotomique([], 0) == -1

# tableau à 1 élément
assert recherche_dichotomique([1], 0) == -1
assert recherche_dichotomique([1], 1) == 0
assert recherche_dichotomique([1], 2) == -1

# tableau plus grand
tableau = [0, 2, 4, 6, 8, 10]
for cle in tableau:
    assert recherche_dichotomique(tableau, cle) == cle // 2

for cle in [-1, 1, 3, 5, 7, 9, 11]:
    assert recherche_dichotomique(tableau, cle) == -1
```
{{< /expand >}}

### Fonction à compléter

{{< tabs "uniqueid" >}}
{{< tab "Difficile" >}}

```python
def recherche_dichotomique(T: list, x: list) -> int:
    """
    Renvoie l'indice de `x` dans `T`.
    Renvoie -1 si `x` n'est pas dans `T`.

    Précondition : `T` est trié par ordre croissant
    """
    ...
```

{{< /tab >}}

{{< tab "Moyen" >}}

```python
def recherche_dichotomique(T: list, x: list) -> int:
    """
    Renvoie l'indice de `x` dans `T`.
    Renvoie -1 si `x` n'est pas dans `T`.

    Précondition : `T` est trié par ordre croissant
    """
    g = ...
    d = ...
    while ...:
        m = ...
        if x == ...:
            return ...
        elif x > ...:
            ...
        else:
            ...
    return ...
```

{{< /tab >}}
{{< tab "Facile" >}}

```python
def recherche_dichotomique(T: list, x: list) -> int:
    """
    Renvoie l'indice de `x` dans `T`.
    Renvoie -1 si `x` n'est pas dans `T`.

    Précondition : `T` est trié par ordre croissant
    """
    g = 0
    d = len(T) - 1
    while g <= d:
        m = ...
        if x == ...:
            return m
        elif x > ...:
            g = ...
        else:
            d = ...
    return -1
```

{{< /tab >}}
{{< /tabs >}}


{{< python title="Recherche dichotomique">}}
def recherche_dichotomique(T: list, x: int):
     ...

x = 5
T = [1,  3,  5,  7,  9, 11, 13, 15]

print(recherche_dichotomique(T, x))
{{< /python >}}



## Déroulé de l'algorithme

```python
x = 5
T = [ 1,  3,  5,  7,  9, 11, 13, 15]
```

On débute avec `g = 0` et `d = 8 - 1 = 7`.

1. `[1,  3,  5,  7,  9, 11, 13, 15]`

   `g = 0 <= d = 7`

   `m = (0 + 7) // 2 = 3`

   `5 < 7 => d = 3 - 1 = 2`

2. `[1,  3,  5]`

   `g = 0 <= d = 2`

   `m = (0 + 2) // 2 = 1`

   `5 > 3 => g = 1 + 1 = 2`

3. `[5]`

   `g = 2 <= d = 2`

   `m = (2 + 2) // 2 = 2`

   `5 == 5 => return 2`

## Remarques

{{< hint danger >}}

### Précondition

**`T` doit être trié par ordre croissant**

{{< /hint >}}

### Terminaison

- `while g <= d:` la boucle s'arrête lorsque `g` devient plus grand que `d`.

- `d - g` décroit strictement à chaque étape (`d = m - 1` ou `g = m + 1` avec `g <= m <= d`)

- En nombre fini d'étapes, on arrive à `d > g` et l'algorithme s'arrête

{{< hint info >}}

### Coût

- `d - g` est _grossièrement_ divisé par deux à chaque étape
- Autrement dit, **si le tableau double de taille, il ne faut qu'une étape supplémentaire.**

- Ex. Si `len(T)` $= 16 = 2 ^ 4$, il faut **~4 étapes**.\
   Dans ce cas, la _recherche par balayage_ demande au pire 16 étapes.

- Ex. En partant d'un tableau _trié_ contenant 10 milliards d'éléments, il faut au plus 34 étapes pour trouver un de ses éléments : $2^{34} > 10^{10}$\
   Une recherche par balayage demande au pire... 10 milliards d'étapes.

  {{< /hint >}}

## Conclusion

- La recherche dichotomique permet de gagner beaucoup d'étapes par rapport au parcours séquentiel du tableau.

- Elle nécessite d'avoir un tableau **trié** sans quoi on ne peut l'appliquer.

### Algorithme

{{< expand "" "..." >}}

```python
def recherche_dichotomique(T: list, x: list) -> int:
    """
    Renvoie l'indice de `x` dans `T`.
    Renvoie -1 si `x` n'est pas dans `T`.

    Précondition : `T` est trié par ordre croissant
    """
    g = 0
    d = len(T) - 1
    while g <= d:
        m = (g + d) // 2
        if x == T[m]:
            return m
        elif x > T[m]:
            g = m + 1
        else:
            d = m - 1
    return -1
```

{{< /expand >}}

### Remarques sur le coût

- Si on ne souhaite l'appliquer qu'une seule fois, il n'est pas intéressant de trier le tableau pour chercher. C'est généralement trop long.
- Mais si on doit souvent effectuer des recherches dans le tableau, alors c'est efficace.

### Nombre d'étapes

- **parcours séquentiel** : autant que d'éléments dans le tableau dans le pire des cas.

  Le parcours séquentiel prend (dans le pire des cas) $n$ étapes.

- **recherche dichotomique** : $\log_2 n$ étapes.

  $\log_2 n \approx$ le nombre de divisions entières de $n$ par 2 qu'on peut effectuer
  avant de trouver un quotient nul

  $\log_2 n \approx$ le nombre de bits de $n$ en binaire.
