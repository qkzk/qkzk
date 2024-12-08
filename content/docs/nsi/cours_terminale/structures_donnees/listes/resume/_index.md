---
subtitle: "Résumé : listes"
author: qkzk
weight: 100

---

pdf: [pour impression](/uploads/docnsitale/listes/listes_resume.pdf)


## La structure de donnée linéaire **liste**


- de _définir_ la structure de données liste. Pour cela nous allons nous concentrer sur ses méthodes,
- de _manipuler_ cette structure de données,
- d'appréhender la notion de _mutabilité_ des listes (elles peuvent changer),
- d'appréhender la _complexité_ de la manipulation des listes,
- de comprendre que ce qui est appelé `List` _en Python n'est pas une liste au sens commun du terme_.


## Qu'est-ce qu'une liste ?

* Intuitivement. Une liste est une collection finie d'éléments qui se suivent. C'est donc une structure de données *linéaire*.

* Une liste peut contenir un nombre quelconque d'éléments y compris nul (la liste vide).

## Obtenir une définition formelle

Prenons une liste comme par exemple $\ell_1 = [3, 1, 4]$.  C'est une liste à trois éléments.


* la liste $\ell_1$ possède un premier élément $3$ qu'on nommera élément de *tête*,
* et que vient après cet élément de tête la liste $\ell_2 = [1, 4]$ des éléments qui suivent,
  liste qu'on nommera *reste*.


Peut être répété pour la liste $\ell_2$ qui est donc constituée :

* d'un élément de *tête* : $1$,
* et d'un *reste* : $\ell_3 = [4]$.

La liste $\ell_3$ est donc constituée :

* d'un élément de *tête* : $4$,
* et d'un *reste* : $\ell_4 = []$.

$\ell_4$ étant vide : pas d'élément de tête, ne peut donc pas être décomposée comme nous venons.



Si on convient d'utiliser la notation $(x,\ell)$ pour désigner le couple constitué de
l'élément $x$ de tête, et du reste $\ell$ d'une liste, on peut alors écrire :


$$\ell_1 = (3, (1, (4, [])))$$



## Définition


Une *liste* d'éléments d'un ensemble $E$ est

* soit la liste vide
* soit un couple $(x,\ell)$ constitué d'un élément $x\in E$
 et d'une liste $\ell$ d'éléments de $E$.

Les listes peuvent donc être vues comme _des structures de données récursives_.

## Primitives sur les listes


Primitives

>   Les _opérations primitives_ d'une structure de donnée sont les opérations minimales qui permettent de définir la structure et de lui donner les méthodes attendues.




Une structure de donnée **liste** doit implémenter :

1. **La construction** à partir d'une liste vide ou à partir d'un couple tête (élément) et reste (liste).
2. **La sélection** de l'élément de tête ou du reste.
3. **Prédicat.** on doit pouvoir répondre à la question : "cette liste est-elle vide ?"

## Liste vs tableaux

### Qu'est ce qui différencie les listes des tableaux ?

les _tableaux_ sont aussi des structures linéaires. Ils contiennent un nombre
prédéfini d'emplacements mémoire (qu'on peut parfois modifier).

* On accède en temps constant à une valeur.
* Insérer un élément demande de décaler tous les suivants. C'est long.

Python utilise des tableaux dynamiques qu'il appelle `list` (parce qu'ils sont mutables).

Ce ne sont ni des "listes" ni des "tableaux" tels qu'on vient de les décrire.

## Complexité


Pourquoi implémenter plusieurs structures ? Après tout, on peut
_tout faire_ avec des listes Python !

Parce que l'efficacité est fondamentale. Certaines structures sont plus adaptées à certains problèmes.


### Accéder à un élément : tableau

Pour accéder à l'élément 2 du tableau

```python
T = ['a', 'b', 'c']
```

1. On se rend à l'adresse où débute `T`
2. On se déplace de deux positions. On lit : `'c'`

Le temps est constant : Accéder se fait en complexité $O(1)$.

### Accéder à un élément : liste

Pour accéder à l'élément 2 de la liste

```python
L = ('a', ('b', ('c', [])))
```

1. On se rend à l'adresse où débute `L`
2. On suit le lien jusque l'adresse de la queue du premier élément
2. On suit le lien jusque l'adresse de la queue du second élément
3. On lit la valeur de la tête : `'c'`

Le temps est linéaire : Accéder se fait en complexité $O(n)$.

---


## Implémenter une structure minimale en Python

Pour implémenter une structure de donnée il faut :

1. avoir décrit les primitives
2. décrire les méthodes qui seront à construire plus tard
3. Utilise la programmation objet pour créer un nouveau _type_ de données

{{< columns >}} <!-- begin columns block -->
### Constructeurs

```python

class Liste:
    def __init__(self, *args):
        if len(args) == 0:
            self.__tete = None
            self.__queue = None
        else:
            self.__tete = args[0]
            self.__queue = args[1]
```
<---> <!-- magic separator, between columns -->


### Exemple

```python
>>> l = Liste()
>>> g = Liste(1, l)
>>> h = Liste(2, g)      
>>> isinstance(l, Liste) 
True                     
```

{{< /columns >}}

{{< columns >}}
### Sélecteurs

```python
    def tete(self):
        return self.__tete

    def queue(self):
        return self.__queue
```
<--->
### Exemple

```python
>>> g.tete()
1
>>> h.queue()
<__main__.Liste object at 0x7f66fbdecf70>
>>> isinstance(h, Liste)
True 
>>> # objet de type liste
```
{{< /columns >}}

{{< columns >}}
### Prédicat
```python
    def est_vide(self):
        return (
            self.__tete is None 
            and self.__queue is None
        )
```
<--->
### Exemple
```python
>>> h.est_vide()
False
>>> l.est_vide()
True
```
{{< /columns >}}



# Méthodes utiles

## Notre structure de donnée est incomplète

Il manque des méthodes pratiques : `longueur`, `index`, `ajouter`, `supprimer`.
