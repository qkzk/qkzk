---
title: "Conditions"
bookCollapseSection: true
author: "qkzk"
weight: 1

---


# Les structures de contrôle


Pour l'instant nos programmes s'exécutent de haut en bas sans pouvoir contrôler quoi que ce soit.

Nous allons introduire deux structures essentielles :

**les conditions et les boucles**

Mais avant ça :

## L'indentation

_indenter_ le code c'est le décaler de quelques espaces (généralement 4,
parfois 2) depuis la gauche.

En python la structure d'un programme est _imposée_ par l'indentation.
Ne pas respecter l'indentation conduit à des erreurs du type `IndentationError`
qu'il est généralement simple de repérer.

```python
code sans indentation

    code mal indenté # provoquera une erreur
```

## Strucure d'un bloc de code

{{< hint warning >}}
Tous les blocs de code ont la même syntaxe :

```python
mot_cle expression:
    expression 1
    expression 2

fin du bloc
``` 
{{< /hint >}}

Répétons : 

1. mot clé, 
2. expression, 
3. deux points, 
4. à la ligne et indenté d'autres expressions.
5. à la ligne et désindenté, la fin du bloc


## Conditions `if, elif, else`

Une condition décrit un bloc de code qui n'est exécuté que si le test est vérifié.

![Condition](/docs/nsi/cours_premiere/programmation/python/cours_python/03_structure_controle/img/0.png)

Par exemple :


Si j'ai plus de 10 de moyenne au bac, je suis diplômé :


```python
moyenne = 3
if moyenne >= 10:               # ne pas oublier les :
    print("je suis diplomé")        # attention à l'indentation

##  suite du programme
```

Lorsqu'on exécute ce code, il ne se passe rien. La condition `moyenne >= 10`
n'est pas respectée et la ligne `print("je suis displomé")` n'est jamais atteinte.

Ajoutons une ligne pour mieux comprendre le déroulé des instructions :


```python
moyenne = 3
if moyenne >= 10:
    print("je suis diplômé")

print("le programme arrive ici dans tous les cas")
```

Exécutez ce programme, il vous affichera "le code arrive ici dans tous les cas"
parce que cette ligne n'est pas indentée. Elle est donc en dehors du bloc `if`.

{{< python title="if...">}}
moyenne = 3
if moyenne >= 10:
    print("je suis diplômé")

print("le programme arrive ici dans tous les cas")
{{< /python >}}

On peut toujours compléter un bloc `if` à l'aide d'un second bloc `else`, 
(_sinon_), qui ne sera exécuté que si la condition du `if` est fausse :


```python
moyenne = 3
if moyenne >= 10:
    print("je suis diplomé")
else:
    print("j'ai raté le diplome")

print("le programme arrive ici dans tous les cas")

```

Cette fois l'exécution du programme conduit à deux affichages :

* "j'ai raté le diplome", parce que la condition du `if` est fausse, Python exécute le `else`
* "le code arrive arrive ici dans tous les cas" parce que ce bloc n'est pas indenté.

Reprenez cet exemple en changeant la valeur de la moyenne afin d'exécuter le if.

{{< python title="if...else" >}}moyenne = 3
if moyenne >= 10:
    print("je suis diplomé")
else:
    print("j'ai raté le diplome")

print("le programme arrive ici dans tous les cas")
{{< /python >}}

Remarquez que cette fois, le bloc `else` n'est plus exécuté.

C'est l'un ou l'autre.

### `elif`

Entre `if` et `else` on peut insérer autant de bloc `elif condition:` que l'on souhaite.

Par exemple :

```python
moyenne = 3
if moyenne >= 10:
    print("je suis diplome")
elif moyenne >= 8:
    print("je vais à l'oral de rattrapage")
else:
    print("j'ai raté le diplome")
print("le programme arrive ici dans tous les cas")
```

Lorsqu'on exécute ce code avec différentes valeurs de la moyenne (5, 9, 11 par exemple) on
réalise qu'un des blocs `if, elif, else` est exécuté. Jamais deux.

Testez tous les cas en changeant la moyenne :


{{< python title="if...elif...else" >}}moyenne = 3
if moyenne >= 10:
    print("je suis diplome")
elif moyenne >= 8:
    print("je vais à l'oral de rattrapage")
else:
    print("j'ai raté le diplome")
print("le programme arrive ici dans tous les cas")
{{< /python >}}

### Exercice 0

1. Que vaut la valeur finale de la variable `b` ?

  ```python
  a = 7
  b = 12
  if a > 5:
      b = b - 4
  if b >= 10:
      b = b + 1
  ```

2. Que vaut la valeur finale de la variable `b` ?

  ```python
  a = 7
  b = 12
  if a > 5:
      b = b - 4
  elif b >= 10:
      b = b + 1
  ```

3. Que vaut la valeur finale de la variable `b` ?

  ```python
  a = 7
  b = 12
  if a > 5:
      b = b - 4
  else:
      b = b + 1
  ```

4. Que vaut la valeur finale de la variable `a` ?

  ```python
  a = 10
  if a < 5:
      a = 20
  elif a < 100:
      a = 500
  else:
      a = 0
  ```

### Exercice 1

Les codes suivants sont-ils valides (on ne demande pas ce qu'ils font) ?
S'ils sont invalides, rectifiez les.

1. Code 1 :

  ```python
  a = 10
  if a == 5:
  a = 2
  ```
2. Code 2 :

  ```python
  a = 10
  elif a == 5:
    a = 2
  ```

3. Code 3 :

  ```python
  a = 10
  if a = 5:
    a == 2
  ```
4. Code 4 : 

  ```python
  a = 10
  if a == 5:
  a = 2
  ```

### Exercice 2

Complétez le programme "moyenne" afin d'afficher la mention obtenue par le candidat :

* Très bien (>= 16 de moyenne),
* Bien (>= 14 de moyenne),
* Assez Bien (>= 12 de moyenne),

### Exercice 3

Un client de boite de nuit est décrit par trois variables : son genre ("Masculin" ou "Féminin"),
sa tenue ("Bien sapé", "Mal sapé") et son portefeuille ("Épais", "Mince").

1. Écrire un programme qui affiche si le client peut entrer en respectant les conditions suivantes :


      * Un client pauvre mais bien sapé peut entrer.
      * Les clientes entrent toujours,
      * Un client pauvre et mal sapé n'entre pas.

2. Testez le dans tous les cas.
3. Si ce n'est pas déjà fait, écrire ce programme à l'aide d'un bloc `if` et d'un bloc `else`

### Exercice 4

Jean-Raoul a un hygiène de vie très stricte. Ils se pèse tous les matins. 

* S'il pèse moins de 100 kilos, durant la journée, il ne boit que de la bière.
* S'il pèse entre 100 et 120 kilos, durant la journée, il ne boit que du vin.
* Si son poids dépasse 120 kilos, durant la journée il ne boit que de l'eau.

Quel athlète !

Ecrire un script qui demande sa masse et affiche le régime qu'il doit suivre.

_Exemples :_

```
Combien pèses-tu ? 140
Eau
Combien pèses-tu ? 95
Bière
Combien pèses-tu ? 105
Vin
```


Attention, `input` retourne toujours _une chaîne de caractères_ du type `str`.\
Pour en faire un entier (du type  `int`) :

```python
poids = int(input("Combien..."))
```

### Exercice 5

L'impôt sur le revenu de Groland est assez simple à calculer :

* un particulier qui gagne moins de 20.000€ de revenus par an doit verser 50% en impôt,
* entre 50.000 et 100.000€ on doit verser 30% aux impôts,
* au dela de 100.000€ de revenus, on doit verser 1€ d'impôt symbolique.

Ecrire un script qui demande à un utilisateur le montant de ses revenus annuels
et affiche le montant des impots qu'il doit verser.

_je précise aux plus naïfs que Groland n'existe pas._



### Exercice 6 - Niveau première en mathématiques

Ecrire un script qui résout l'équation du second degré : $ax^2 + bx + c = 0$\
Par exemple :


    Résolution de l'équation du second degré : ax² + bx + c = 0
    Coefficient a ? 1
    Coefficient b ? -0.9
    Coefficient c ? 0.056
    Discriminant :  0.586
    Deux solutions :
    0.0672468158199
    0.83275318418


    Résolution de l'équation du second degré : ax² + bx + c = 0
    Coefficient a ? 2
    Coefficient b ? 1.5
    Coefficient c ? 4
    Discriminant :  -29.75
    Il n'y a pas de solution.

---

