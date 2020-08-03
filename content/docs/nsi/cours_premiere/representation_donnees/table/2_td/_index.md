---
title: '2. TD : importer, exporter, trier'
author: 'qkzk'
date: '2020/07/31'
weight: 2

---

### pdf : [pour impression](/uploads/docsnsi/table_csv/2_td.pdf)

# 1. Importer une table

On considère le fichier csv `films.csv` dont voici un extrait.

![films](/uploads/docsnsi/table_csv/data-visualization-movies_csv-1024x686.png){height=300px}

Pour chaque question on donnera une syntaxe Python permettant d'obenir la
réponse ainsi que la valeur de celle-ci lorsque l'information est connue.


1. Importer le fichier en Python vers un tableau de dictionnaires appelé `table`
2. Quel est le nombre d'enregistrements ?
3. Combien de champs différents comporte cette table ?
3. Quelles sont les différents champs ?

# 2. Exporter une table, sélections, projections

Les joueurs d'échecs sont classés selon les résultats de leurs parties.
Chaque partie permet de gagner ou perdre des points élo et les joueurs
sont classés selon leur score.

On a crée en Python une table dans une variable appelée `joueur` dont voici
un extrait :

```python
joueurs = [
    {'nom': 'Carlsen, Magnus', 'pays':'nor', 'elo': 2863},
    {'nom': 'Caruana, Fabiano', 'pays':'usa', 'elo': 2835},
    {'nom': 'Ding, Liren', 'pays':'chi', 'elo': 2791},
    {'nom': 'Nepomniachtchi, Ian', 'pays':'rus', 'elo': 2784},
    {'nom': 'Vachier-Lagrave, Maxime', 'pays':'fra', 'elo': 2778},
    {'nom': 'Grischuk, Alexander', 'pays':'rus', 'elo': 2777},
    {'nom': 'Aronian, Levon', 'pays':'arm', 'elo': 2773},
    {'nom': 'So, Wesley', 'pays':'usa', 'elo': 2770},
    {'nom': 'Radjabov, Teimour', 'pays':'aze', 'elo': 2765},
    {'nom': 'Giri, Anish', 'pays':'nl', 'elo': 2764},
    ...
]
```

## Enregistrer

1. Enregistrer cette table au format CSV.

## Parcourir les données

2. Comment accéder aux différents champs ?
3. Comment connaître le nombre d'enregistrements ?

## Sélections

2. Comment sont enregistrées les nationalités ?
3. Créer la table des joueurs français.
4. Créer la table des joueurs ayant plus de 2780 points élo.
5. Compter les joueurs de la table ayant entre 2700 et 2800 points élo.

## Projections

6. Créer la projection des noms de joueurs. Limiter ensuite cette table
    au top 5.
7. Créer la projection des scores élo. Calculer le score élo moyen des 10
    premiers joueurs.
8. Créer une fonction qui prend la table en paramètre ainsi qu'un entier
    `nombre` et retourne le score moyen des "`nombre`" premiers joueurs.\
    Si `nombre` est trop grand on se limitera à la taille du tableau.
