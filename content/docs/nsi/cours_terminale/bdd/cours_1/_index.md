---
title: "introduction"
bookCollapseSection: true
author: qkzk
weight: 2

---





pdf : [pour impression](/uploads/docnsitale/bdd/cours_sql1_print.pdf), [diapo](/uploads/docnsitale/bdd/cours_sql1_slides.pdf)

<!-- à compiler par
pandoc -t beamer --slide-level 2 -V "aspectratio=1610" -s cours_sql1.md -o cours_sql1_slides.pdf
-->

# Bases de données relationnelles

## Principe

Une _base de donnée_ permet de stocker efficacement une immense
quantité d'information. 

Les BDD permettent de croiser facilement les informations
et d'en extraire le contenu.

Les bases de données _relationnelles_ sont apparues dans les années 60 et sont
encore les plus utilisées à ce jour.

Tous les informaticiens doivent maîtriser un minimum de concepts clés relatifs
aux bases de données et doivent être capables de réaliser les manipulations de
base que nous allons présenter.

Depuis une décennie, les données sont omniprésentes et parfois moins organisées.
On a vu un usage croissant d'un autre type de base de données _NoSQL_ très utilisées
par les grands acteurs du web.


## Définitions

**Base de donnée (définition large)** : tout ensemble de données stockées numériquement
et pouvant servir à un (ou plusieurs) programmes.

**Base de donnée (définition restreinte)** : on appellera base de données un
ensemble de données numériques qui possède une structure ; c'est à dire dont
l'organisation répond à une logique systématique.

### Exemple

![données de la table ville](/uploads/docnsitale/bdd/fig/table_ville.png "données de la table ville")\

## Définitions

* **BDD** : ensemble des tables.
* **Table** (parfois **relation**) : c'est l'ensemble des **enregistrements** qui existent sur les données
* **Colonne** (parfois **champs** ou **attributs**) : "departement", "code" etc. : les différents champs à rempir
* **Ligne**  (parfois **Enregistrement** ou **Relations**) : "1", "2" etc. les données elles-mêmes.
* **Cellules** (parfois **Cases**) : la valeur elle même.

## BDD relationnelle

Dans une même base de donnée, on rencontre souvent plusieurs tables.

Par exemple, pour un compte bancaire :

1. table des transactions du compte courant avec comme champs :

    date, numero_transaction, montant, libelle

    Exemple d’enregistrement :

    * date : 2019-06-23
    * numero_transaction : "TR123455667"
    * montant : "-123.45"

2. table des différents comptes avec comme champs :

    numero_compte, nom_compte, date_ouverture

3. table des différents soldes avec comme champs :

    numero_compte, date, solde


## Identifier les enregistrements

Chaque fois qu'on enregistre quelque chose dans la base de donnée
il faut s'assurer que la donnée n'est pas _déjà_ présente.

On résout ce problème avec la notion de "clé".

### Clé primaire (_Primary Key_) (PK)

* Identifie de manière unique une ligne
* Ne doit pas être `NULL` (vide)
* Peut être composée d'une ou plusieurs colonnes
* Ajout d'une colonne dédiée si besoin

### Clé étrangère (_Foreign Key_) (FK)
* Référence une ou plusieurs colonnes d'une autre table (représentant
une clé primaire)
* Les colonnes référencées doivent pré-exister dans la table référencée

## Identifier : une nécessité

Il arrive qu'un ordre de transaction ne parvienne pas jusqu'au bout...
et qu'on doive le relancer. Comment éviter de facturer plusieurs fois la même chose ?

Chaque enregistrement se voit attribuer une clé primaire unique
et quand on essaie d'enregistrer la même transaction, la base
de donnée empêche cet ajout.

* Pour notre exemple des comptes, la clé primaire est le numéro de compte. etc.

* Pour notre exemple des transactions, la clé primaire est le numéro de
    transaction. Le numéro de compte est alors une clé étrangère (le compte doit
    déjà exister avant qu'on n'y réalise des transactions).


## Structurer les données

Comment choisir convenablement la présentation des données ?

Imaginez-vous à la tête du service informatique de la sécurité sociale.

Comment enregistrer :

* les patients (des dizaines de millions),
* les actes médicaux (des centaines de milliers par jour),
* sans occuper un espace monstrueux ?

## Structurer les données

Il faut au moins deux tables (en pratique sûrement une centaine...)

* pour les patients avec leur numéro de sécu (on suppose que tous les individus
    en ont un pour simplifier)
* pour les actes

Dans la table des patients on enregistre les données "permanentes" :

* n° de sécu, nom, prénom, date de naissance, date de décès éventuel etc.

Dans la table des actes médicaux, on ne reprend pas toute la fiche du patient,
seulement son numéro de sécu.

Ainsi, le numéro de sécu est à la fois :

* _la clé primaire_ de la table "patients"
* _une clé secondaire_ de la table "actes"

## Construire une structure optimisée

### Regrouper les données en tables
* Mettre dans une même table les données relatives à un même sujet
* Créer de nouvelles tables pour éviter la redondance des données
  * Limite les incohérences lors des mises à jour
  * Facilite la construction des requêtes et améliore la pertinence des résultats

### Établir les relations entre tables
* Définir les clés primaires
  * Uniques et non NULL
* Définir les clés étrangères
  * Référencent les clés primaires

### Définir des colonnes pertinentes
* Facilité d'interrogation des colonnes
* Données cohérentes au sein d'une colonne
* Ne pas conserver des données qui peuvent être calculées


## Construire une structure optimisée

### Cas des catégories socioprofessionnelles du Nord.

![Fichier d'origine : CSV](/uploads/docnsitale/bdd/fig/categorie_socio_csv.png "Fichier d'origine : CSV")

## Construire une structure pertinente

### Regrouper les données en tables
* Tables = données relatives à un même sujet
  * Données sur les villes et sur les effectifs des catégories

### Éviter la redondance des colonnes
* var = Tranche + categorie
* categorie = abréviation Catégorie socioprofessionnelle

### Éviter la redondance des valeurs
* Les colonnes `departement` et `region` ne contiennent qu'une seule valeur
* À conserver uniquement si volonté d'étendre à d'autres données

### Données cohérentes
* Les colonnes Sexe, Tranche, ... contiennent aussi des totaux !
  * Les totaux peuvent être calculés à l'aide de fonctions et d'agrégats
* Décomposer `coordonnees` en deux REAL


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
  * ...


* Contrôle des données et des transactions
  * Gestion des autorisations d'accès aux données par les différents utilisateurs
  * Gestion de l'exécution de transactions
    * Transaction = suite d'opérations de modification de la base de données




### SGBDR = Système de Gestion de Bases de Données Relationnelle
* Logiciel permettant de manipuler le contenu des bases de données relationnelles
* Garantit la qualité, la pérennité et la confidentialité des informations
* Exemple : [SQLite](https://sqlite.org/) ![logo SQLite](/uploads/docnsitale/bdd/fig/SQLite370.svg.png) est un SGBDR dont le code
source est dans le domaine public 

### C'est un langage déclaratif
* Décrit le résultat voulu sans décrire la manière de l'obtenir
* Les SGBDR déterminent automatiquement la manière optimale d'effectuer
les opérations nécessaires à l'obtention du résultat

## Différents SGBDR

* SQLite : open source. n'utilise pas de serveur. Stocke la base dans un unique fichier.
    Très rapide pour des bases "modestes" (< 1 million d'enregistrements)

* MySQL, PostgreSQL, Oracle etc. : (Oracle n'est pas open source). Utilisent un serveur.
    Très rapides pour des bases "conséquentes".

La majorité de ces logiciels sont écrits en C ou en C++.

* Certains sont spécialisés (graphiques, données numériques précises etc)
* D'autres sont fournis avec un serveur dans le cloud etc.

Tous implémentent les fonctions de base de SQL + quelques fonctions "perso"
parfois commodes.

## SQLite

Nous utiliserons SQLite qui est programmé en C et qu'on peut utiliser depuis

* en Python (`import sqlite3`)
* sous windows / linux / osx (DB Browser, `$ sqlitebrowser`)
* ainsi [qu'en ligne](https://inloop.github.io/sqlite-viewer/).
* ou même sur mon site [Editeur](https://qkzk.xyz/docs/nsi/cours_terminale/bdd/sqljs/) et [TP commande](https://qkzk/docs/nsi/cours_terminale/bdd/tp_commandes/).

mais aussi

* iOS,
* Android etc.

À noter, toutes les applications mobiles qui enregistrent _localement_ beaucoup de données utilisent SQLite. Ce n'est pas le seul moyen d'enregistrer quelque chose sur le téléphone : fichiers, "local storage = dictionnaire" etc.

## Extraction des données d'une table

```sql
SELECT noms_colonnes_séparés_par_virgules
    FROM nom_table;
```

Sélectionne toutes les lignes d'une table


### `*` pour toutes les colonnes

```sql
SELECT *
    FROM nom_table;
```

Avant de se lancer, une petite parenthèse :

### Les cellules de code exécutables. 

Cette page présente des cellules comme celle ci-dessous, exécutables.

Durant tout ce cours, on utilisera les mêmes données issues de deux tables.

Intéressons nous d'abord à la table `employees`.

Voici le code qui a permis de la créer puis de la remplir :

```sql

DROP TABLE IF EXISTS employees;
CREATE TABLE employees( id integer,
                        name text,
                        designation text,     
                        manager integer,
                        hired_on date,     
                        salary integer,
                        commission float,    
                        dept integer);

INSERT INTO employees VALUES (1,'JOHNSON','ADMIN',6,'1990-12-17',18000,NULL,4);
INSERT INTO employees VALUES (2,'HARDING','MANAGER',9,'1998-02-02',52000,300,3);
INSERT INTO employees VALUES (3,'TAFT','SALES I',2,'1996-01-02',25000,500,3);
INSERT INTO employees VALUES (4,'HOOVER','SALES I',2,'1990-04-02',27000,NULL,3);
INSERT INTO employees VALUES (5,'LINCOLN','TECH',6,'1994-06-23',22500,1400,4);
INSERT INTO employees VALUES (6,'GARFIELD','MANAGER',9,'1993-05-01',54000,NULL,4);
INSERT INTO employees VALUES (7,'POLK','TECH',6,'1997-09-22',25000,NULL,4);
```

* La première ligne efface la table si elle existe déjà.
* Ensuite on la crée avec tous ses attributs (et généralement des contraintes, pas ici.)
* Ensuite on insère un par un les enregistrements.

Voilà le résultat :

{{< sql title="Séléctionner toute une table" init="init.sql">}}
SELECT * FROM employees;
{{< /sql >}}


### `DISTINCT` pour sélectionner une seule occurrence de chaque valeur de la colonne en question

```sql
SELECT DISTINCT nom_colonne
    FROM nom_table;
```

Exemple :

```sql
SELECT DISTINCT categorie, genre
    FROM evolution;
```


{{< sql title="avec et sans DISTINCT" init="init.sql">}}
SELECT manager FROM employees;

SELECT DISTINCT manager FROM employees;
{{< /sql >}}

### Sélectionne uniquement les lignes qui respectent la clause du `WHERE`

```sql
SELECT noms_colonnes_séparés_par_virgules
    FROM nom_table
    WHERE nom_colonne op_comp valeur op_bool nom_colonne op_comp valeur;
```

{{< sql title="WHERE" init="init.sql">}}
SELECT name, salary, commission FROM employees
WHERE salary > 50000;
{{< /sql >}}



### La clause porte sur les valeurs des colonnes

* Utilisation d'opérateurs de comparaison (op_comp) : `=`, `<>`, `!=`, `>`, `>=`, `<`, `<=`
* Utilisation d'opérateurs booléens (op_bool) : `AND`, `OR`
  * `AND` : combinaisons de conditions sur des colonnes différentes
  * `OR` : plusieurs valeurs possibles pour une même colonne

Exemples :

```sql
SELECT code, effectif
	FROM evolution
	WHERE categorie="Agriculteurs Exploitants" AND genre="Femmes";

SELECT code, categorie, effectif
	FROM evolution
	WHERE categorie="Agriculteurs Exploitants" OR categorie="Ouvriers";
```


{{< sql title="WHERE, opération booléennes" init="init.sql">}}
SELECT name, salary, commission FROM employees
WHERE salary > 20000 AND commission > 0;
{{< /sql >}}

## Extraction des données d'une table

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

{{< sql title="avec et sans AS" init="init.sql">}}
SELECT name, manager FROM employees;
SELECT name AS superman, manager AS superpower FROM employees;
{{< /sql >}}


### `ORDER BY`

* Trie les données selon la colonne précisée.
* Par défaut, le tri est dans l'ordre croissant, `DESC` permet d'obtenir
l'ordre décroissant.

## Fonctions de calcul sur les données extraites.

```sql
SELECT FONCTION(nom_colonne)
    FROM nom_table;
```


{{< sql title="ORDER BY" init="init.sql">}}
SELECT name, manager FROM employees
ORDER BY salary ASC;
{{< /sql >}}

Applique une fonction sur les valeurs d'une colonne

* `COUNT` : compte le nombre de lignes sélectionnées.

* `MIN`, `MAX` : renvoie la valeur minimum ou maximum de la colonne,
parmi les lignes sélectionnées

* `SUM`, `AVG` : calcule la somme ou la moyenne des valeurs
**numériques** de la colonne, parmi les lignes sélectionnées



<!-- new slide -->
### Aggrétats

Exemple :

```sql
SELECT AVG(effectif) AS Moy_employes
	FROM evolution
	WHERE categorie="Employés";
```

* Pas au programme, `GROUP BY` : agrège ensemble les valeurs identiques
d'une colonne pour appliquer une fonction à chacun des sous-ensembles

Exemple :

```sql
SELECT code, AVG(effectif) AS Moy_employes
	FROM evolution
	WHERE categorie="Employés"
    GROUP BY code;
```

Calcule la moyenne des effectifs des `Employés` (`Hommes` et `Femmes`)
pour chaque ville.

## Exemples avec ou sans agrégat

![résultats avg sans GROUP BY](/uploads/docnsitale/bdd/fig/avg.png "sans agrégat") ![résultats avg avec GROUP BY](/uploads/docnsitale/bdd/fig/avg_group_by.png "avec agrégat")

{{< sql title="AVERAGE" init="init.sql">}}
SELECT AVG(salary) FROM employees;

SELECT manager, AVG(salary) AS salary FROM employees
GROUP BY manager;

SELECT dept, AVG(salary) AS salary FROM employees
GROUP BY dept;
{{< /sql >}}


## Extraction des données de deux tables

### Produit cartésien
* Comme son nom l'indique, génère de façon exhaustive toutes les
associations possibles entre les lignes des deux tables
  * Nb_total_lignes = Nb_lignes_ville * Nb_lignes_evolution = 650 * 10400
* Non pertinent

![](/uploads/docnsitale/bdd/fig/produit_cartesien.png)

{{< sql title="Produit cartésien" init="init_2_tables.sql">}}
SELECT * FROM department;

SELECT * FROM department, employees
{{< /sql >}}

Une autre manière d'écrire la même chose, parfois commode, `CROSS JOIN` :

`CROSS`, comme la croix du produit... $2 \times 3 = 6$

{{< sql title="Produit cartésien avec CROSS" init="init_2_tables.sql">}}
SELECT * FROM department;

SELECT * FROM department
CROSS JOIN employees
{{< /sql >}}

### `JOIN ON`

Génère uniquement les associations entre les lignes qui sont liées
par des clés primaires et étrangères identiques.

Permet d'associer deux tables qui sont en relation.

**C'est la notion la plus importante et la plus délicate du chapitre.**

![](/uploads/docnsitale/bdd/fig/join_on.png)

Dans l'exemple du code, `employees.dept` est un clé étrangère faisant référence à `departement.id`

On fait donc une jointure sur cette clé :

{{< sql title="Jointure" init="init_2_tables.sql">}}

SELECT * FROM department
JOIN employees ON employees.dept=department.id;
{{< /sql >}}


Qu'on peut affiner un peu, par exemple :

{{< sql title="Jointure mieux présentée" init="init_2_tables.sql">}}

SELECT e.name AS name, d.name AS dept FROM department AS d
JOIN employees AS e ON e.dept=d.id
ORDER BY d.id;
{{< /sql >}}

## Modification des données

### Ajouter avec `INSERT`

`INSERT` : ajoute une nouvelle ligne de données dans une table

```sql
INSERT INTO nom_table VALUES (liste_valeurs_dans_ordre_colonnes_table);
INSERT INTO nom_table (liste_nom_colonnes_à_remplir)
    VALUES (liste_des_valeurs_à_insérer_dans_ordre_liste_colonnes);
```


{{< sql title="Insertion avant, après" init="init_2_tables.sql">}}
SELECT * FROM department;
INSERT INTO department VALUES (5,"Comms");
SELECT * FROM department;
{{< /sql >}}


Depuis une base vide, les données sont insérées de la même manière...

{{< sql title="vide" init="empty.sql">}}
DROP TABLE IF EXISTS department;
CREATE TABLE department(
    id integer,
    name text,
	PRIMARY KEY("id")
);


  INSERT INTO department VALUES (1,"Sales");
  INSERT INTO department VALUES (2,"Admin");
  INSERT INTO department VALUES (3,"IT");
  INSERT INTO department VALUES (4,"Foreign");

  SELECT * FROM department;
{{< /sql >}}

### Aparté hors programme

Il exite une autre manière d'insérer des données, très utilisée en pratique :

```sql
INSERT INTO table
SELECT ( requete de selection )
```

Cela permet d'insérer des données en faisant référence à une autre table.
C'est parfois indispensable, en particulier quand une table sert de pont entre deux tables :

Par exemple pour des commande d'une client à un vendeur, on utilise trois tables :

* client: les clients et leurs données statiques,
* vendeur: les vendeurs idem,
* commande: chaque commande avec une clé étrangère vers client et un autre vers vendeur.

Pour insérer une commande du client A au vendeur B valant x€, il faudrait connaître les 
identifiants du client et du vendeur.

On utilise alors `INSERT INTO commande SELECT (...)`

Ceci est largement hors programme et franchement mal documenté sur internet.

### Mettre à jour avec `UPDATE`

`UPDATE` : met à jour la ou les lignes qui respectent la clause du `WHERE`

```sql
UPDATE nom_table SET nom_colonne1=valeur1, nom_colonne2=valeur2
    WHERE nom_colonne op_comp valeur op_bool nom_colonne op_comp valeur;
```


{{< sql title="UPDATE" init="init_2_tables.sql">}}
SELECT * FROM department;
UPDATE department SET name="Foreign Affair" WHERE name="Foreign";
SELECT * FROM department;
{{< /sql >}}

### Effacer avec `DELETE`


`DELETE` : efface la ou les lignes d'une table qui respectent la clause du `WHERE`

```sql
DELETE FROM nom_table WHERE nom_colonne op_comp valeur op_bool nom_colonne op_comp valeur;
```

{{< sql title="DELETE" init="init_2_tables.sql">}}
SELECT * FROM department;
DELETE FROM department WHERE name="Foreign";
SELECT * FROM department;
{{< /sql >}}

## Respect de l'intégrité des données

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
