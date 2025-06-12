---
title: "Cours"
bookCollapseSection: true
author: qkzk
weight: 100
---

# Calculabilité - Problème de l'arrêt en Python

## Programme 

{{< expand "" "..." >}}


> _Parallèlement, on montre l’universalité et les limites de la notion de calculabilité._ 
> 
> ### Contenus 
> 
> _Notion de programme en tant que donnée. Calculabilité, décidabilité_ 
> 
> ### Capacités attendues 
> 
> _Comprendre que tout programme est aussi une donnée. Comprendre que la calculabilité ne dépend pas du langage de programmation utilisé. Montrer, sans formalisme théorique, que le problème de l’arrêt est indécidable._ 
> 
> ### Commentaires 
> 
> _L’utilisation d’un interpréteur ou d’un compilateur, le téléchargement de logiciel, le fonctionnement des systèmes d’exploitation permettent de comprendre un programme comme donnée d’un autre programme._ 
{{< /expand >}}

[Version intéressante de Gilles Lassus](https://glassus.github.io/terminale_nsi/T2_Programmation/2.3_Calculabilite_Decidabilite/cours/)

## Un programme en tant que donnée


{{< hint info >}}
Un _programme_ est un texte écrit en langage machine et que la machine peut exécuter. 
{{< /hint >}}
Généralement les programmes prennent la forme de fichiers exécutables.

Le code source d'un programme est transformé par un _compilateur_ en un _programme_.
Ce résultat est donc la donnée de sortie d'un compilateur.

{{< expand "" "..." >}}
```bash 
$ cat hello.c             # affiche le contenu du fichier texte hello.c
#include <stdio.h>

int main(void) { printf("Hello, World!\n"); }
$ gcc hello.c -o hello    # compile hello.c en un fichier binaire hello
$ chmod +x hello          # rend le fichier `hello` exécutable 
$ ./hello                 # exécute `hello`
Hello, World!
```
{{< /expand >}}

Pour exécuter ce programme, je le localise sur ma machine, par exemple avec un _explorateur de fichiers_, puis je l'exécute.

Cependant, compiler soi même ses programmes n'est pas courant. Généralement on télecharge des programmes déjà compilés avec un navigateur ou un gestionnaire de téléchargement... ensuite on l'installe (c'est à dire qu'on copie ses fichiers au bons endroits).

Ce téléchargement transfère donc les données du programme pour en faire un fichier exécutable sur notre machine.

{{< hint warning >}}
Les programmes sont donc _des données_ de ces logiciels (navigateur, gestionnaire de téléchargement, explorateur de fichier, compilateur etc.)
{{< /hint >}}

## Équivalence des langages de programmation

Les différents langages de programmation disposent tous d'une propriété commune : ils sont **Turing Complets**. 

{{< hint danger >}}
**Cela signifie qu'un problème qu'on peut résoudre dans l'un est résoluble dans un autre.**
{{< /hint >}}

Attention, cela ne dit rien de l'_efficacité_ des langages. Python est lent et n'est pas adapté à l'écriture de pilotes matériels... mais pourrait le faire.

Ainsi, Python est généralement interprété par un programme (`python.exe` sous windows) qui est programmé en C. Cet interpréteur pourrait être écrit en Python lui même... [et ça existe](https://github.com/pypy/pypy).

### Turing Complet ?

{{< expand "" "..." >}}
Que signifie le terme "Turing Complet" ?

Malheureusement, définir précisément ce terme dépasse largement le cadre du programme. Cela n'a rien d'infaisable mais notre ambition n'est pas de faire de vous des informaticiens théorique.

Ceci étant dit, on peut tenter une approche.

Il existe de nombreux modèles théoriques dont on a démontré mathématiquement l'équivalence. C'est la thèse de Church-Turing.

À l'origine, trois modèles étaient en compétition pour définir ce qu'une machine devait être capable de faire.

- les machines de Turing,
- le $\lambda$-Calcul d'Alonzo Church, ($\lambda$ = lambda)
- les "fonctions récursives générales" de Kurt Gödel et Stephen Kleene. (Attention, on ne parle pas uniquement de fonction qui s'appelle elle-même, comme nous le faisons dans le chapitre sur la récursion.)

Church et Turing ont démontré que ces modèles étaient _équivalents._

Ainsi, on pourrait construire une machine de Turing qui serait, par exemple, un interpréteur Python. Ce serait un travail colossal... mais théoriquement faisable.

Oui mais... qu'est-ce qu'il faut au minimum :

En simplifiant énormément les contraintes des _fonctions récursives générales_ :

{{< hint info >}}
Si un langage permet de :

- définir la constante `0`,
- incrémenter (`x <- x + 1`),
- affecter une variable et accéder à son contenu,
- concaténer des programmes (c'est-à-dire mettre des instructions les unes après les autres),
- écrire des boucles for décroissantes : `for (x to 0) do ... end`
- écrire des boucles while `while (x != 0) do ... end`

Alors ce langage est Turing-Complet.
{{< /hint >}}

Remarquons que tout ça est trivial en Python, ce qui prouve bien que Python est Turing-Complet.

### Exemples 

Les langages modernes sont tous Turing-Complets, les assembleurs ARM et x86 aussi.

- HTML seul ne l'est pas. Mais HTML+CSS l'est.
- SQL est Turing-Complet,
- TeX (un langage de description de documents employé par tous les matheux qui se respectent) est Turing-Complet,
- Excel l'est aussi.

Certains _jeux_ sont Turing-Complet :

- Dwarf Fortress,
- Cities: Skylines,
- Minecraft (red stone etc. chercher Minecraft turing machine),
- Magic: The Gathering,
- une grille infinie de démineur,
- baba is you,

D'autres trucs plus ésotériques :

- le jeu de la vie de John Conway,
- le formatage des chaînes de caractères du C, utilisé notamment dans `printf` est Turing-Complet,
- l'instruction `MOV` de l'assembleur x86 est Turing-Complete. Cela signifie qu'on pourrait écrire TOUS les programmes de la terre avec une seule instruction...


Comme on s'en apperçoit, les conditions minimales ne sont pas très restrictives, raison pour laquelle il existe autant de langages de programmation.
{{< /expand >}}
## Terminaison

On dit qu'une fonction **termine** si elle renvoie une valeur ou si elle lève une exception (par exemple `ZeroDivisionError` si une division par zéro est tentée).

Ainsi, une fonction qui **ne termine pas** est une fonction qui entre dans une boucle infinie.

Avec cette définition, seulement deux situations peuvent se présenter lorsqu'on appelle une fonction :

- Elle _termine_,

ou

- Elle _continue de calculer indéfiniment_

### Remarque 

Ici, on n'envisage que des programmes très simples, **sans intéraction avec l'utilisateur**.

Ainsi, la boucle principale d'une application utilisateur :

```python 
mise_en_route()

while True:
    lire_les_entrees()
    mettre_a_jour_l_etat()
    afficher()
```
N'est pas envisagée.

Justement parce que dans `lire_les_entrees` on dispose d'un moyen de signaler qu'on veut arrêter le programme... et que dans `mettre_a_jour_l_etat` on l'arrête si nécessaire.

---


Ainsi, la fonction `ma_fonction` (voir ci-dessous), termine pour un entier `n` inférieur ou égal à 10 (elle renvoie `None`) et ne termine pas pour `n` strictement plus grand que 10.

En outre, cette fonction termine pour une chaîne de caractères `n` (en levant l'exception `TypeError` à cause de l'opération `+`).

```python
def ma_fonction(n):
  while n != 10 :
    n = n + 1
```

## Décidabilité 

TODO

## Calculabilité

En langage simple :

> _Que peut-on faire faire à une machine ?_
> _Et que ne peut-on pas lui faire faire ?_

{{< hint info >}}
Une fonction $f$ est _calculable_ s'il existe un algorithme qui, étant donné une entrée $x$, permet d'obtenir $f(x)$.
{{< /hint >}}

Python étant un langage Turing-Complet, on peut s'en servir pour illustrer cette notion :

{{< hint info >}}
Une fonction est calculable si elle est programmable en Python.
{{< /hint >}}


### Quel intérêt ?

Jusqu'ici, tous les problèmes qu'on a pu aborder avaient une solution. Parfois très lente, parfois très difficile mais nous sommes parvenus à répondre à tous les problèmes.

{{< hint danger >}}
Existe-t-il des fonctions non calculables ?
{{< /hint >}}


## Problème de l'arrêt

### De l'utilité d'une fonction `arret`

On pourrait penser qu'il serait utile d'avoir en Python une fonction `arret` :

{{< hint info >}}
- qui termine sur toutes les entrées possibles,
- telle que `arret(f, x)` renvoie `True` si le calcul de `f(x)` termine
- et `False` sinon.
{{< /hint >}}

Une telle fonction, si elle était ajoutée au langage, permettrait d'éviter les boucles infinies en faisant un simple test.

Si on voulait programmer une telle fonction, il serait naturel que la fonction `arret` accède au code de la fonction `f` (ce qui est possible grâce au module `dis`), et analyse ce code, par quelque moyen compliqué, pour en déduire si oui ou non le calcul de `f(x)` va un jour terminer.

## Le Problème de l'arrêt...

La question :

{{< hint info >}}
_Est-il possible de programmer la fonction `arret` ?_
{{< /hint >}}

est connue sous le nom du **problème de l'arrêt**.

## C'est impossible

Nous allons montrer qu'une telle fonction ne peut pas exister.

Pour cela, nous allons employer un _raisonnement par l'absurde_.

{{< expand "" "..." >}}
**Raisonnement par l'absurde.**

L'idée est de supposer _le contraire de ce qu'on souhaite prouver_ et de démontrer que cela est impossible _en aboutissant à une contradiction_, une absurdité_.

Un exemple vous éclairera davantage qu'une définition formelle :

#### Énoncé : "$0$ n'a pas d'inverse".

_Rappel : l'inverse_ d'un nombre réel $x$ est l'unique nombre réel $y$ tel que $x \times y = 1$.

#### Preuve : 

**Supposons le contraire, à savoir que $0$ a un inverse** (Hypothèse du raisonnement par l'absurde)

Notons $a$ cet inverse.

Alors $0 \times a = 1$ par définition de l'inverse.

Mais...$0 \times a = a \times 0$. (le produit des réels est commutatif)

D'autre part, $a \times (0 + 0) = a \times 0 + a \times 0$. (simple distributivité)

Donc $a \times (0 + 0) = 1 + 1$ d'après le résultat précédent et $a \times (0 + 0) = 2$.

Donc $0 + 0 = 0$. ($0$ est l'élément neutre de l'addition des réels.)

Donc $a \times (0 + 0) = a \times 0$.

En utilisant les résultats précédents cela dit que $2 = 1$.

Cette dernière affirmation **est fausse** et contredit la construction des nombres réels.

Donc le raisonnement est faux... mais où est l'erreur ? Dans la supposition initiale : "_Supposons que $0$ à un inverse_".

Donc la supposition de départ est fausse et $0$ n'a pas d'inverse.
{{< /expand >}}

### Hypothèse

Supposons que quelqu'un ait réussi à programmer cette fonction `arret`.

```python
def arret(f, x) -> bool:
    """
    Prend une fonction f et ses paramètres x en entrée.
    * Termine toujours
    * Renvoie `True` si `f(x)` termine
    * Renvoie `False` si `f(x)` ne termine pas.
    """
    ...
```

### La fonction `strange`

Nous pouvons alors l'utiliser pour programmer la fonction `strange` suivante :

```python
def strange(f, x):
  if arret(f, x):
    while True:
      pass
```

Cette fonction teste si le calcul de `f(x)` termine.

- si `f(x)` termine, elle rentre dans une boucle infinie dans laquelle elle ne fait rien.

- Sinon, elle ne fait rien et termine.

**Autrement dit, `strange(f, x)` termine si et seulement si `f(x)` ne termine pas.**

### La fonction `paradox`

La précédente fonction nous permet d'en définir une nouvelle, la fonction `paradox`.

```python
def paradox(f):
  strange(f, f)
```

Par construction, le calcul de `paradox(f)` termine si et seulement si le calcul de `f(f)` ne termine pas. Appelons (1) cette propriété.

> (1) _le calcul de `paradox(f)` termine si et seulement si le calcul de `f(f)` ne termine pas_

### `paradox(paradox)` ?

Maintenant, demandons-nous si le calcul de `paradox(paradox)` termine.

Pour cela, dans la propriété (1), remplaçons `f` par `paradox`.

La propriété devient :

> _Le calcul de paradox(paradox) termine si et seulement si le calcul de paradox(paradox) ne termine pas._

Cette dernière propriété est évidemment absurde (elle se contredit elle même).

Nous pouvons donc conclure notre raisonnement par l'absurde et affirmer qu'il est impossible de programmer la fonction `arret`.

## Complément

### Limitation du problème

Le problème de l'arrêt reste impossible même si on se limite à ce que les arguments de arrêt soient une
fonction `f` des entiers dans les entiers et un entier `x`.

Pourquoi ? Simplement parce que n'importe quelle valeur de n'importe quel type sera représenté en machine par une suite d'octet, soit à peu près un entier naturel.

### Historique

La résolution du problème de l'arrêt par Alonzo Church et Alan Turing, en 1936 a eu de nombreuses conséquences
en informatique et en mathématiques. La résolution de ce problème a conduit Alan Turing à créer les machines de Turing, modèle mathématiques à l'origine des ordinateurs modernes...

En particulier, il n'est pas possible d'écrire un assistant de programmation qui repère
tous les problèmes qu'un code présente avant de l'avoir exécuté.


### Ramasse miettes 

Il n'est pas non plus possible d'écrire un ramasse miette (_garbage collector_) qui soit parfait.
Un ramasse miette cherche à libérer des zones de la mémoire après leur dernière utilisation dans un programme.
Ces outils existent dans beaucoup de langages modernes (python, java, Golang etc.) mais ne sont jamais parfaits, en effet, l'existence d'un ramasse miette parfait est équivalente au problème de l'arrêt.

{{< expand "" "..." >}}
Pourquoi utiliser des ramasses-miettes s'ils sont, par essence, imparfaits ?

Parce qu'ils font généralement mieux qu'un développeur, même très bon.

Mieux que quoi ?

La cause _majeure_ de bugs dans les programmes modernes est la gestion de la mémoire.
Dans un langage où il faut gérer la mémoire à la main, comme C ou C++, il faut allouer (=réserver) de la mémoire pour enregistrer les données avec `malloc` ou autre.
Après l'utilisation des données, il faut la libérer avec `free`

Easy.

Sauf que non. En pratique :

1. on en réserve trop,
1. on n'en réserve pas assez,
1. on oublie de libérer la mémoire et le programme en consomme de plus en plus, finissant par paralyser le système,
1. on tente de la libérer plusieurs fois...

Le ramasse miette tente de résoudre ce problème. Certes il ne sera jamais parfait mais... il évite de fait les problèmes 1, 2 et 4. Pour le problème 3, c'est insoluble.

Par exemple :

```python 
class A:
  def __init__(self):
    self.a = None 

class B:
  def __init__(self):
    self.b = None 

x = A()
y = B()

x.a = y 
y.b = x

# suite du programme, on n'utilise plus x ou y
```


Après la ligne `y.b = x`, les variables `x` et `y` ne sont plus jamais employées.

Le ramasse miette _devrait_ les libérer pour nous. Il ne le fera jamais car `y.b -> x` et `x.a -> y`, ces deux variables se réfèrent elles-mêmes.

Un autre inconvénient du ramasse miette est qu'à des moments difficiles à prédire, il s'exécute et parcourt la mémoire à la recherche d'espaces à libérer. Cela peut être coûteux en ressources.

Alors... si pas de ramasse miette, existe-t-il d'autres solutions ?

Oui, par exemple, le _borrow checker_ de Rust. Une approche totalement différente dans laquelle la construction de l'exemple plus haut est proscrite. Ce n'est _pas non plus parfait_ et cela demande un temps d'adaptation.
{{< /expand >}}

### complément machine de Turing 

TODO

### complément lambda calcul 

TODO 
## Vidéo

Voici une [vidéo](https://www.youtube.com/watch?v=a5MNIzu9Ia4) de l'université de Rennes qui expose la preuve précédente.
