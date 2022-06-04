---
title: "TD : Complexité"
bookCollapseSection: true
weight: 6

---


### PDF : [Pour impression](./6_cout_td.pdf)


## Exercice 1 - Ordre de grandeur des complexité

1. Tracer sur la calculatrice les fonctions suivantes :

    $$f(x) = x$$ 
    $$g(x) = x^2$$ 
    $$h(x) = \ln (x)$$
    $$k(x) = x \ln(x)$$

    On prendra $x$ entre $10$ et $100$

2. Trier ces fonctions par _vitesse de croissance_. De celle qui explose
  le moins vite à celle qui explose le plus vite quand $x$ tend vers $+\infty$


3. Reprenons les fonctions de la question 1.

    On considère maintenant $F, G, H, K$ des algorithmes.
    Ils prennent tous en entrée une seule donnée dont la taille est $x$ et leur coût est 
    est donné par la fonction correspondante.

    Ainsi, _le coût de l'algorithme $F$ pour $x=3$ est $f(3)$

    Estimer les temps d'exécution pour $x = 100$.

    On multiplie la taille de l'entrée par $2$. Estimer les temps d'exécution.

4. Recommencer avec l'exponentielle : $l(x) = 2^x$.


## Exercice 2 - Logarithme binaire

Le logarithme est une fonction très utilisé en science et qui dispose
de beaucoup de propriétés.

En informatique on utilise notamment le fait qu'il permet de mesurer
le nombre de bits nécessaires pour écrire un nombre.

1. Combien de bits sont nécessaires pour écrire $N = 3~567$ en mémoire ?
2. Calculer $\dfrac{\ln x}{\ln 2}$ à l'aide de la calculatrice.

  Cette fonction est appelé _logarithme en base 2_ et permet d'encadrer
  le nombre de bits utilisé par un entier. Elle est généralement notée $\log_2$

3. Proposer une formule pour encadrer la taille d'un entier en mémoire avec le logarithme
  en base 2.


{{< hint info >}}
Le nombre de bits nécessaire pour représenter un entier $n$ est $\lceil \log_2(n+1) \rceil$
{{< /hint >}}

où $\lceil x \rceil$ est l'arrondi à l'entier supérieur de $x$.

## Exercice 3 - Complexité de quelques fonctions

1. On considère la fonction `indice_mini` utilisée dans le tri par sélection.
    Quelle est sa complexité ?

2. Que fait la fonction suivante ?

    ```python
    def mystere(tableau):
      somme = 0
      nb_elements = 0
      for element in tableau:
        somme = somme + element
        nb_elements = nb_elements + 1

      return somme / nb_elements
    ```

3. Quelle est la complexité de la fonction `mystere` ?

4. Recommencer avec la fonction suivante :

    ```python
    def mystere(tableau):
        somme = 0
        for i in range(len(tableau)):
            for j in range(i):
                somme = somme + tableau[j]
        return somme
    ```

    1. Que fait-elle ? Commencez par un exemple : `mystere([1, 2, 3, 4])`
    2. Estimer sa complexité.


5. Recommencer avec la fonction suivante :

    ```python
    def mystere(tableau):
        x = 0
        y = 0
        for i in range(len(tableau)):
            if tableau[i] < tableau[x]:
                x = i
        for j in range(len(tableau)):
            if tableau[j] > tableau[j]:
                y = j
        return (x, y)
    ```

  6. Existe-t-il une relation immédiate entre la complexité
      d'un algorithme et le nombre de boucle qu'il contient ?

      Que dire du cas où les boucles sont _imbriquées_  (= l'une dans l'autre) ?


## Exercice 4 - Tableau `insert` et `append`

Python propose deux méthodes sur les tableaux :

```python
>>> t = [2, 4, 6]
>>> t.append(8)
>>> t
[2, 4, 6, 8]
>>> t.insert(0, 12)
>>> t
[12, 2, 4, 6, 8]
>>> t.insert(2, 20)
>>> t
[12, 2, 20, 4, 6, 8]
```

1. Donner la signature de ces méthodes :

    * à quel objet s'appliquent-elles ?
    * que prennent-elles en entrée ?
    * que font-elles ?
    * que renvoient-elles ?

{{< hint info >}}
En mémoire, un objet `list` est représenté par un tableau de cases mémoires
  contigues (côte à côte).

Lorsqu'on crée une liste, Python réserve un grand nombre de cases à l'avance
et celles-ci sont vides.

À chaque fois qu'on ajoute un élément dans le tableau,
un attribut, _sa longueur_ est augmentée.

Ainsi, on sait toujours combien d'éléments il contient.
{{< /hint >}}

2. D'après la description de précédente, quelle est la complexité de la fonction
  `len` ?

3. Toujours d'après cette description, laquelle des deux méthodes `insert` et
  `append` est la plus efficace ?

    Donner leur complexité.


Considérons :

```python
>>> t = [4, 5, 6]
>>> t[0]
4
>>> t[-1]
6
```

{{< hint info >}}
Lorsqu'on accède à un élément par son indice, Python doit simplement se rendre
à l'adresse de l'emplacement mémoire correspondant. Ensuite il renvoie la valeur
contenue dans cet emplacement.
{{< /hint >}}


4. Va-t-on plus vite lorsqu'on souhaite accéder au premier élément ? Au dernier ?


5. Il existe une autre méthode pour ajouter des éléments à un tableau, l'opération
  `+`.

    ```python
    >>> t1 = [1, 2, 3]
    >>> t2 = [4, 5, 6]
    >>> t1 + t2
    >>> [1, 2, 3, 4, 5, 6]
    >>> t1
    [1, 2, 3]
    >>> t2
    [4, 5, 6]
    ```

    Que fait l'opération `+` sur les tableaux ? Quels sont ses opérandes et son
    résultat ? Modifie-t-elle les objets sur lesquels elle s'applique ?

6. Proposer une autre manière d'ajouter un élément à la fin d'un tableau, ou
  au début de celui-ci en utilisant `+`.

7.  Quelle est sa complexité ?


---

## Remarques 

* Pour retirer un élément, la méthode `pop` est très rapide. Elle renvoie le dernier
  élément (celui dont l'indice est `len(tableau) - 1`) et modifie la longueur
  du tableau, indiquant simplement qu'il a perdu un élément.

  Pour retirer un autre élément, d'indice quelconque, c'est plus délicat, il
  faut déplacer tous les éléments qui étaient après lui et cela prend du temps.

* Bien-sûr, lorsqu'on a rempli une liste... celle-ci est pleine.
  Python réserve alors d'autres emplacements mémoire pour pouvoir continuer
  à agrandir arbitrairement le tableau.

* On préfère éviter les _copies_ lorsqu'on peut se contenter d'ajouter
    à la fin d'un tableau :

    ```python
    >>> t = [1, 2, 3]
    >>> t.append(4)
    >>> t
    [1, 2, 3, 4]
    ```

    et 

    ```python
    >>> t = [1, 2, 3]
    >>> t = t + [4]
    >>> t
    [1, 2, 3, 4]
    ```

    Produisent le même résultat mais la première est beaucoup plus rapide que la seconde.
