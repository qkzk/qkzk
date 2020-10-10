---
title: "NSI - Terminale"
subtitle: "Bases de données - Travaux dirigés - Langage SQL"
author: "qkzk"
date: ""
theme: metropolis
geometry: margin=1.5cm

---


Pour tous les exercices qui suivent on utilisera la base de données ci-dessous.

Elle est constituées de quatre relations :


**Relation _Stations_**

| NomStation   | Capacite | Lieu       | Region        | Tarif |
|:------------:|:--------:|:----------:|:-------------:| -----: |
| Tanger       | 350      | Maroc      | Afrique       | 1200  |
| La Bourboule | 250      | Auvergne   | Afrique       | 700   |
| Victoria     | 200      | Seychelles | Océan Indient | 1500  |
| Courchevel   | 400      | Alpes      | Europe        | 2200  |

**Relation _Activités_**

| NomStation   | Libelle   | Prix |
|:------------:|:---------:|-----:|
| La Bourboule | Pêche     | 50   |
| La Bourboule | Randonnée | 0    |
| Tanger       | Plongée   | 120  |
| Tanger       | Excursion | 60   |
| Victoria     | Plongée   | 130  |
| Courchevel   | Ski       | 120  |

**Relation _Clients_**

| Id | Nom     | Prenom  | Ville    | Region   | Solde |
|:--:|:-------:|:-------:|:--------:|:--------:|------:|
| 1  | Bauer   | Elmut   | Berlin   | Europe   | 9825  |
| 2  | Smith   | John    | Londres  | Europe   | 12436 |
| 3  | Jonhson | Britney | New York | Amérique | 6721  |

**Relation _Séjours_**

| IdClient | Station      | Arrivée    | NbPlaces |
|:--------:|:------------:|:----------:|:--------:|
| 1        | Courchevel   | 17/02/2019 | 2        |
| 3        | Tanger       | 17/11/2018 | 5        |
| 2        | Courchevel   | 28/01/2018 | 4        |
| 3        | La Bourboule | 20/07/2016 | 3        |
| 3        | Victoria     | 13/09/2015 | 6        |
| 2        | La Bourboule | 13/08/2019 | 3        |
| 3        | Courchevel   | 27/02/2017 | 5        |
| 1        | Victoria     | 05/09/2018 | 3        |



***

**Compétence :** _Exprimer dans le langage SQL des requêtes d'interrogation._

# Exercice 1

Donner l'expression SQL des requêtes suivantes ainsi que le résultat obtenu.

1. Noms des stations ayant strictement plus de 200 places.
2. Noms des clients dont le nom commence par 'J' ou dont le solde est supérieur
    à 10 000.
3. Noms des stations qui proposent de la plongée.

# Exercice 2

Donner l'expression SQL des requêtes suivantes ainsi que le résultat obtenu.

1. Noms des clients qui sont allés à La Bourboule.
2. Noms des stations visitées par des européens.

# Exercice 3

Donner l'expression SQL des requêtes suivantes ainsi que le résultat obtenu.

1. Combien de séjours ont eu lieu à Victoria ? On stockera le résultat dans 
    une colonne nommée 'Total'.
2. Donner le prix moyen d'une activité à Tanger. On stockera le résultat dans
    une colonne nommée 'Prix Moyen Activités Tanger'.

# Exercice 4

1. Donner l'expression SQL de la requête permettant d'afficher la liste des
    stations suivie du lieu (en majuscule) entre parenthèses et du tarif HT
    et TTC comme le montre l'exemple suivant :

    |         Stations        | Tarif HT | Tarif TTC |
    |:-----------------------:|---------:|----------:|
    |      Tanger (MAROC)     |     1200 |      1440 |
    | La Bourboule (AUVERGNE) |      700 |       880 |
    |    Courchevel (ALPES)   |     2200 |      2640 |
    |  Victoria (SEYCHELLES)  |     1500 |      1880 |

    On supposera que le Prix dans la base est le tarif HT et que le taux
    de TVA est de 20%.

2. Les données correspondantes au tarif TTC des stations sont-elles stockées
    dans la base de données ?


# Exercice 5

**Compétence** _Exprimer dans le langage SQL des requêtes d'insertion._

1. Donner l'expression SQL des requêtes permettant d'ajouter la cliente venant
    de Toronto (Canada) suivante : Mme Karibou Juliette avec un solde de 7213€.
    Cette cliente a séjourné (3 places) à La Bourboule le 10/07/2019

2. Peut-on, dans l'état, ajouter à cette base que Mme Karibou a fait de la
    randonnée ?



# Exercice 6

**Compétence** _Exprimer dans le langage SQL des requêtes de mise à jour de valeurs._

1. Donner l'expression SQL de la requête permettant de mettre à jour la capacité
    de la station Courchevel à 450 places ainsi que le nouveau tarif de 2300€.
2. Peut-on changer ici le nom de l'attribut 'Prix' en 'Prix HT' de la relation
    _Activités_ par une requête de type `UPDATE` ?

# Exercice 7

**Compétence** _Exprimer dans le langage SQL des requêtes de suppression_

1. Donner l'expression SQL de la requête permettant tout ce qui concerne Mme
    Karibou (données insérées dans l'exercice 5).

    On supposera que la structure est bien correcte, à savoir que l'attribut `idClient`
    de la relation `Séjours` est bien une clé étrangère liée en référence à
    l'attribut `id` de la relation `Clients` et que l'on a bien spécifié
    `ON DELETE CASCADE` à la création de la clé étrangère de la relation.

2. Que faire si la clé étrangère n'a pas été définie dans la relation séjours ?

