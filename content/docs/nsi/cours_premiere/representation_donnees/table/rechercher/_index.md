---
title: 'Rechercher dans les données'
author: 'qkzk'
date: '2019/12/22'
weight: 2
---

# 2. Effectuer des recherches dans les données

## Nettoyer la liste

Souvenons nous de ce qu'on a obtenu après notre précédent import :

un dictionnaire Python avec les valeurs provenant d'un fichier csv.

Et, si on imprime, cela donne.

~~~python
>>> print(liste_csv)
[{'nom': 'Nom', 'prenom': 'Prénom', 'email': 'email'},
 {'nom': 'Duchmol', 'prenom': 'Robert', 'email': 'robert@email.com'},
 {'nom': 'Lemeilleur', 'prenom': 'Franky', 'email': 'franky@email.com'},
 {'nom': 'Poivre', 'prenom': 'Jacques', 'email': 'jacque@email.com'}]
~~~

On obtient bien les valeurs, mais pas seulement

Mais pas seulement.

On a aussi un élément surprenant, le premier.

L'entête a été lue comme une série de valeurs. Ce n'est pas correct.

Pour rectifier, plusieurs approches :

1. enlever l'élément de la liste,
2. reparcourir la liste en ne gardant que les suivants, c'est du gâchis,

~~~python
del liste_csv[0]
~~~

## Rechercher les éléments particuliers

Maintenant que nos données sont en mémoire, on peut les traiter comme des
listes Python.

~~~python
liste_csv[]
~~~

Pour chercher un élément, disons un nom particulier, une approche
est de construire la liste des noms.

**Quel est le prénom de l'élève nommé Boulier ?**

~~~python
>>> # liste des noms
>>> noms = [eleve["nom"] for eleve in liste_csv]
>>> # trouver l'élève avec index
>>> noms.index("Boulier")
14
>>> liste_csv(14)
{"nom": "Boulier", "prenom": "Thomas", "moyenne_brute": ""}
>>> liste_csv(14)["prenom"]
"Thomas"
~~~

Attention, `index` lève une exception `ValueError` s'il ne trouve pas l'élément.

On peut être plus prudent :

~~~python
def trouver_element(liste, element):
  '''
  Renvoie l'indice de l'élément dans la liste, -1 s'il n'y figure pas
  @param liste: (list)
  @param element: (any)
  @return: (int)
  '''
  try:
    liste.index(element)
  except ValueError as e:
    return -1
~~~

qui s'utilise ainsi :

~~~python
>>> trouver_element(["a", "b", "c"], "b")
1
>>> trouver_element(["a", "b", "c"], "d")
-1
~~~

## Rechercher des valeurs selon des critères

On souhaite coller tous les élèves sont la moyenne dépasse 14 (par méchanceté)

Deux approches :

1. parcourir et attribuer la colle immédiatement
2. récupérer la liste en question et coller l'ensemble

Selon la difficulté du traitement, on préférera l'une ou l'autre.

La seconde approche est jugée plus propre car les étapes sont clairement
séparées.

Elle nécessite cependant deux parcours.

### Parcourir et traiter ensemble


Voilà le traitement qu'on souhaite appliquer :

~~~python
def coller(nom):
  print(f"{nom} je t'aime pas, tu as 2h !")
~~~

Le parcours est très simple, 3 lignes

~~~python
for eleve in liste_csv:
  if eleve["moyenne"] > 14:
    coller(eleve["nom"])
~~~

### Récupérer et traiter l'ensemble

Par compréhension :

~~~python
punis = [eleve["nom"] for eleve in liste_csv
                      if eleve["moyenne"] > 14]
for nom in punis:
  coller(nom)
~~~

Ce n'est pas beaucoup plus long...

Bien sûr, on peut adapter à des critères plus délicats.
Si nécessaire, créer une fonction booléenne qui renvoie `True` si le critère
est vérifié.

## Doublons

Il arrive fréquemment qu'on croise des données. Celles-ci comporte alors
souvent des doublons qu'il faut nettoyer.

Autre contexte conduisant à des doublons, ajouter des éléments au fur et à
mesure.

1. Supposons que les élèves aient tous des noms différents, repérer les doublons
    est aisé.

    On remplit une liste vide en ne gardant que les individus qui n'y figurent pas déjà.

    liste vide
    * 1er élève Robert : il n'est pas dans la liste, je l'ajoute
    * 2eme élève Martin : il n'est pas dans la liste, je l'ajoute
    * 3eme élève Robert : il est déjà dans la liste, je passe au suivant

    etc.

    ~~~python
    listes_nom_sans_doublon = []
    for eleve in liste_csv:
      if eleve["nom"] not in listes_nom_sans_doublon:
        listes_nom_sans_doublon.append(eleve["nom"])
    ~~~

    Remarquons qu'on n'obtient que les **noms**, pas les données complètes.

    Pour retrouver l'ensemble des valeurs, on peut créer les deux objets en
    même temps :

    ~~~python
    listes_nom_sans_doublon = []
    listes_csv_sans_doublon = []
    for eleve in liste_csv:
      if eleve["nom"] not in listes_nom_sans_doublon:
        listes_nom_sans_doublon.append(eleve["nom"])
        listes_csv_sans_doublon.append(eleve)
    ~~~

2. Plus difficile, si la combinaison "nom, prénom" est unique

    On peut toujours créer des listes qui servent de filtre :

    ~~~python
    liste_nom_complet_sans_doublon = []
    for eleve in liste_csv:
        if (eleve["nom"], eleve["prenom"]) not in liste_nom_complet_sans_doublon:
          liste_nom_complet_sans_doublon.append((eleve["nom"], eleve["prenom"]))
    ~~~

    Cette fois on ajoute un `tuple` (ou une liste, un dictionnaire...)



## Tester la cohérence d'une table

On ouvre ici la boite de Pandore. Toutes les situations sont possibles.

incohérences possibles :

* {"nom": 14, "prenom": "dupont", "moyenne": "thomas"}
* {"nom": "dupont", "prenom": "", "moyenne": 14}

etc.

Que faire ? Tout dépend du contexte.

* Lors d'un enregistrement d'une valeur, il est prudent d’empêcher et d'alerter.
* Lors du calcul d'une moyenne on peut décider à l'avance de planter le programme
  ou seulement d'éviter la valeur.

Dans tous les cas il faut parcourir au moins une fois les valeurs et tester
la cohérence de chacune d'entre elle.
Il est commode de créer une fonction qui teste la cohérence d'un enregistrement.

Ensuite, cela revient à filtrer comme on l'a vu plus haut.
