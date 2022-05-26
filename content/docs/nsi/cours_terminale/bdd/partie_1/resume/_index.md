---
title: "Résumé"
bookCollapseSection: true
author: qkzk
weight: 10

---


### pdf : [Résumé des commandes](/uploads/docnsitale/bdd/sqlite_sheet_fr.pdf), [pour impression](/uploads/docnsitale/bdd/bdd_resume.pdf)


# Bases de données relationnelles


## Définitions


**Base de donnée (définition large)** : tout ensemble de données stockées numériquement
et pouvant servir à un (ou plusieurs) programmes.

**Base de donnée (définition restreinte)** : on appellera base de données un
ensemble de données numériques qui possède une structure ; c'est à dire dont
l'organisation répond à une logique systématique.



* **BDD** : ensemble des tables.
* **Table** (parfois **relation**) : c'est l'ensemble des **enregistrements** qui existent sur les données
* **Colonne** (parfois **Champs** ou **attributs**) : "departement", "code" etc. : les différents champs à rempir
* **Ligne**  (parfois **Enregistrement** ou **relations**) : "1", "2" etc. les données elles-mêmes.
* **Cellules** (parfois **cases**) : la valeur elle même.



## BDD relationnelle

Dans une même base de donnée, on rencontre souvent plusieurs tables.

Par exemple, pour un compte bancaire :

1. table des transactions du compte courant avec comme champs :

    date, numero_transaction, montant, libelle

2. table des différents comptes avec comme champs :

    numero_compte, nom_compte, date_ouverture

3. table des différents soldes avec comme champs :

    numero_compte, date, solde


## Identifier les enregistrements

Pour chaque enregistrement il faut s'assurer que la donnée n'est pas _déjà_ présente.

On résout ce problème avec la notion de "clé"

### Clé primaire = Primary Key (PK)

* Identifie de manière unique une ligne
* Ne doit pas être `NULL` (vide)
* Peut être composée d'une ou plusieurs colonnes
* Ajout d'une colonne dédiée si besoin

### Clé étrangère = Foreign Key (FK)

* Référence une ou plusieurs colonnes d'une autre table (représentant
une clé primaire)
* Les colonnes référencées doivent pré-exister dans la table référencée


# SQL : Structured Query Language

## Description de SQL

### Langage informatique servant à exploiter des bases de données relationnelles

* Manipulation des données
  * Recherche de données : `SELECT`
  * Ajout de données : `INSERT`
  * Modification de données : `UPDATE`
  * Suppression de données : `DELETE`
* Définition des données
  * Manipule les structures de données de la base
  * Création de tables et autres structures : `CREATE`
* Contrôle des données et des transactions
  * Gestion des autorisations d'accès aux données par les différents utilisateurs
  * Gestion de l'exécution de transactions :

    Transaction = suite d'opérations de modification de la base de données

### SGBDR = Système de Gestion de Bases de Données Relationnelle

* Logiciel permettant de manipuler le contenu des bases de données relationnelles
* Garantit la qualité, la pérennité et la confidentialité des informations
* Exemple : [SQLite](https://sqlite.org/) est un SGBDR dont le code
source est dans le domaine public

### C'est un langage déclaratif

* Décrit le résultat voulu sans décrire la manière de l'obtenir
* Les SGBDR déterminent automatiquement la manière optimale d'effectuer
    les opérations nécessaires à l'obtention du résultat



## Extraction des données d'une table

```sql
SELECT noms_colonnes_séparés_par_virgules
    FROM nom_table;
```

Sélectionne toutes les lignes d'une table


* `*` pour toutes les colonnes

* `DISTINCT` pour sélectionner une seule occurrence de chaque valeur de la colonne en question


```sql
SELECT DISTINCT categorie, genre
    FROM evolution;
```

```sql
SELECT noms_colonnes_séparés_par_virgules
    FROM nom_table
    WHERE nom_colonne op_comp valeur op_bool nom_colonne op_comp valeur;
```

Sélectionne uniquement les lignes qui respectent la clause du `WHERE`

### La clause porte sur les valeurs des colonnes

* Utilisation d'opérateurs de comparaison (op_comp) : `=`, `<>`, `!=`, `>`, `>=`, `<`, `<=`
* Utilisation d'opérateurs booléens (op_bool) : `AND`, `OR`

Exemple :

```sql
SELECT code, effectif
	FROM evolution
	WHERE categorie="Agriculteurs Exploitants" AND genre="Femmes";
```


```sql
SELECT abrev.nom_colonne AS nom_affiché
    FROM nom_table AS abrev
    ORDER BY nom_colonne [DESC];
```

Change l'affichage et le nommage des données

### `AS`

* Associé à un nom de colonne : change le nom affiché de la colonne
dans le résultat.

* Associé à un nom de table : permet d'abrévier le nom de la table pour
préciser de quelle table provient une colonne dont le nom est utilisé
par plusieurs tables. Cette abréviation **doit** être utilisée dans le
reste de la requête.


## Fonctions de calcul sur les données extraites.


Applique une fonction sur les valeurs d'une colonne

* `COUNT` : compte le nombre de lignes sélectionnées.

* `MIN`, `MAX` : renvoie la valeur minimum ou maximum de la colonne,
parmi les lignes sélectionnées

* `SUM`, `AVG` : calcule la somme ou la moyenne des valeurs
**numériques** de la colonne, parmi les lignes sélectionnées



Exemple :

```sql
SELECT AVG(effectif) AS Moy_employes
	FROM evolution
	WHERE categorie="Employés";
```

## Modification des données

```sql
INSERT INTO nom_table (liste_nom_colonnes_à_remplir)
    VALUES (liste_des_valeurs_à_insérer_dans_ordre_liste_colonnes);
```

```sql
UPDATE nom_table SET nom_colonne1=valeur1, nom_colonne2=valeur2
    WHERE nom_colonne op_comp valeur op_bool nom_colonne op_comp valeur;
```

```sql
DELETE FROM nom_table 
WHERE nom_colonne op_comp valeur op_bool nom_colonne op_comp valeur;
```


## Extraction des données de deux tables

### Produit cartésien
* Comme son nom l'indique, génère de façon exhaustive toutes les
associations possibles entre les lignes des deux tables
  * Nb_total_lignes = Nb_lignes_ville * Nb_lignes_evolution = 650 * 10400
* Non pertinent


### `JOIN ON`
* Génère uniquement les associations entre les lignes qui sont liées
par des clés primaires et étrangères identiques.
  * Nb_total_lignes = Nb_lignes_table_clé_étrangère = NB_lignes_evolution
* À utiliser pour associer deux tables




### Respect de l'intégrité des données

* Une clé primaire doit être unique et non NULL
  * On ne peut pas insérer une ligne avec une clé primaire qui existe déjà.
  * On ne peut pas modifier la valeur d'une clé primaire en une autre valeur
  qui existe déjà.
* Une clé étrangère doit référencer une clé primaire existante
  * Il faut créer la ligne contenant la clé primaire avant une ligne
  contenant une clé étrangère la référençant.
  * On ne peut pas modifier une clé primaire si elle est déjà référencée.
  * On ne peut pas effacer une ligne contenant une clé primaire déjà référencée.
* Il est possible de mettre des contraintes sur les clés pour gérer
les cascades de modifications (interdiction ou gestion automatique)
