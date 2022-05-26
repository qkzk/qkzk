---
title: "Cours - partie 2"
bookCollapseSection: true
lang: fr
weight: 2

---

# Concevoir une base de donnée

pdf : [pour impression](/uploads/docnsitale/bdd/cours_sql2_print.pdf), [diapo](/uploads/docnsitale/bdd/cours_sql2_slides.pdf)


## Généralités

### Intérêts d'un Système de Gestion de Base de Données (SGBD)

{{< hint info >}}
* Assure la persistance des données
* Structure l'information
* Permet de trouver rapidement une information
* Multi-utilisateurs
* Sécurise les données
    * Filtre les données qu'un groupe d'utilisateurs peut voir
    * Centralise la sauvegarde et la mise à jour des données
* Maintient la cohérence des données
    * Non redondance
    * Contrôle de l'intégrité des données (lors de la saisie, de la mise à jour, de la suppression)
{{< /hint >}}


### Type de SGBD
* Bases hiérarchiques (structure arborescente) ou réseau (structure de graphe)
    * navigation entre les données

{{< hint info >}}
* Bases relationnelles
    * Données sous forme de table, langage SQL
{{< /hint >}}

* Bases déductives
    * Intégration d'ensemble de règles, langage DATALOG
* Bases objet
    * Données sous forme d'objets
* Bases noSQL
    * Pas de structuration des données


### Exemples de SGBD Relationnels (SGDBR)
* Access (suite Microsoft Office)
* [SQlite](https://www.sqlite.org/index.html), libre
* [PosgreSQL](https://www.postgresql.org/), libre
* [Oracle](https://www.oracle.com/), non libre
* [DB2](https://www.ibm.com/analytics/db2), non libre
* [H2](www.h2database.com), libre 

## Volumétrie

### Exemple de la banque (BNP Paribas)

Grande masse d’informations $8 \times 10^6$ clients

* 4 comptes par client, donc $32\times 10^6$ comptes
* 20 écritures par mois par compte, donc $6.4 \times 10^8$ écritures par mois

Plusieurs utilisateurs simultanément

* 2140 agences
* 31.460 collaborateurs
* des milliers d’accès internet

## Analyse

* Travail préalable à la création de la base de données

* Travail complexe et difficile
* Déterminer les informations qui sont nécessaires à l'application
    * gestion de la paie, des congés, du stock
    * application web

### Dictionnaire de données
* Parmi toutes les informations, on repère les données élémentaires ou propriétés
    * niveau de granularité dépend du contexte (adresse, client,... )
* Le dictionnaire de données représente l'ensemble des données élémentaires


## Modèle Conceptuel de Données: MCD

* Le MCD est une représentation du système d'informations à l'aide d'entités et d'associations
* C'est le résultat du travail des analystes, il sert de base à la création de la base de données
* Peut être lu et compris par des non informaticiens
* Un MCD est toujours contextuel

## MCD: Notion d'Entité

* Une entité regroupe les propriétés relatives à un même sujet, qui a du sens
    * Exemple: une voiture, un individu...
* Comporte un identifiant
    * peut être composé par une seule ou plusieurs propriétés
    * est unique: ne peut être le même pour deux entités
* Se représente par un rectangle, l'identifiant est souligné

![Entité client](/uploads/docnsitale/bdd/fig/entite_client.png "Entité client")



## MCD: Notion d'Association

* Les entités peuvent être liées par des associations
* Une association est une représentation abstraite de la mémorisation d'un lien entre entités
* Elle est représentée par un cercle entre entités
     * Exemples: `commande`, `est_inscrit`, `travaille_pour`, `est_marie`, `habite_dans`....

  ![Association commande](/uploads/docnsitale/bdd/fig/client_asso_sans_card.png "Association commande")

## MCD: Cardinalités

* Les cardinalités précisent le nombre de fois que l'entité peut intervenir dans une association.
* La valeur minimale est 0 ou 1, la valeur maximale est 1 ou n
* L'association peut-être hiérarchique (maximum 1 d'un côté, n de l'autre)  ou maillée (maximum n des deux côtés), entre une ou plusieurs entités

![Association commande](/uploads/docnsitale/bdd/fig/asso_client_card.png "Association commande")

## MCD: Autres exemples
![Association est_inscrit](/uploads/docnsitale/bdd/fig/etudiant_sans_card.png "Association est_inscrit")

Un (`min=1, max=1`) étudiant peut être inscrit dans aucune ou plusieurs (`min = 0` `max = n`) universités. 

![Association est_inscrit](/uploads/docnsitale/bdd/fig/etudiant_card.png "Association est_inscrit")

![Association est_marie](/uploads/docnsitale/bdd/fig/mariage_sans_card.png "Association est_marie")

Un individu peut-être marié à au plus une personne. Il peut ne pas être marié. `min=0, max=0` des deux côtés.

![Association est_marie](/uploads/docnsitale/bdd/fig/mariage_card.png "Association est_marie")

![Association est_divorce](/uploads/docnsitale/bdd/fig/divorce_sans_card.png "Association est_divorce")

Un individu peut-être divorcé à plusieurs personnes. Il peut ne pas être divorcé. `min=0, max=n` des deux côtés.

![Association est_divorce](/uploads/docnsitale/bdd/fig/divorce_card.png "Association est_divorce")

![Association reservation](/uploads/docnsitale/bdd/fig/resa_sans.png "Association reservation")

![Association reservation](/uploads/docnsitale/bdd/fig/resa_avec.png "Association reservation")


## Complément sur les cardinalités

[http://tony3d3.free.fr/files/Les-Cardinalites.pdf](http://tony3d3.free.fr/files/Les-Cardinalites.pdf)


## Modèle Relationnel

* La traduction concrète du MCD dépend du modèle de la base
* Dans le cas d'une base de données relationnelle, on obtient un modèle relationnel

### Principe

* Données sous forme de tables
* Chaque table et chaque colonne (ou attribut) porte un nom
* Chaque attribut est typé
* Chaque ligne représente un enregistrement
* Pas de lien physique entre les tables


## Passage du MCD au Modèle Relationnel

### Principe
* Chaque entité devient une table
* Chaque propriété d'une entité devient un attribut
* L'identifiant d'une entité devient la clé primaire de la table (Primary Key)

### Lien hiérarchique

{{< hint info >}}
Une association `(0-n)`--`(0-1)` est un lien hiérarchique.

Elle se traduit par la migration de la clé primaire côté n vers une clé étrangère (Foreign Key) côté 1
{{< /hint >}}


![Association est_inscrit](/uploads/docnsitale/bdd/fig/etudiant_card.png "Association est_inscrit")


{{< hint info >}}
On l'indique avec une flêche **de la clé étrangère vers la clé primaire**.
{{< /hint >}}

![Modèle Relationnel-Lien Hiérarchique](/uploads/docnsitale/bdd/fig/etudiant_MLD.png "Modèle Relationnel-Lien Hiérarchique")


### Lien Maillé

{{< hint info >}}
Une association maillée (0-n)-(0-n) donne lieu à la création d'une nouvelle table dont la clé primaire est l'union des clés primaires des entités qu'elle relie. 

Ces attributs sont aussi des clés étrangères.
{{< /hint >}}

![Association commande](/uploads/docnsitale/bdd/fig/asso_client_card.png "Association commande")


{{< hint info >}}
On l'indique donc avec deux flêches, de la table `relation` vers les tables contenant les clés primaires.
{{< /hint >}}

![Modèle Relationnel-Lien Maillé](/uploads/docnsitale/bdd/fig/client_asso_MLD.png "Modèle Relationnel-Lien Maillé")

## Autres exemples

### Est marié

![Association est_marie](/uploads/docnsitale/bdd/fig/mariage_card.png "Association est_marie")

![Modèle Relationnel mariage](/uploads/docnsitale/bdd/fig/mariage_MLD.png "Modèle Relationnel mariage")

### Est divorcé

![Association est_divorce](/uploads/docnsitale/bdd/fig/divorce_card.png "Association est_divorce")

![Modèle Relationnel divorce](/uploads/docnsitale/bdd/fig/divorce_MLD.png "Modèle Relationnel divorce")

### Réservation

![MCD Categorie](/uploads/docnsitale/bdd/fig/resa_avec.png "MCD Categorie")


![Modèle Relationnel Categorie](/uploads/docnsitale/bdd/fig/resa_MLD.png "Modèle Relationnel Categorie")

# Conception à partir d'un csv

## Retour sur l'exemple des catégories socio-professionnelles

Dans le cas où on récupère des données réelles, le problème se pose différemment.

Le dictionnaire des données est déduit du csv récupéré.

En revanche, les données réelles peuvent poser d'autres problèmes: doublons, incohérences, données non complétées ou peu exploitables.

En général, il faut faire un travail de "nettoyage" pour pouvoir créer les tables.

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

## MCD possible

![MCD Categorie](/uploads/docnsitale/bdd/fig/categorie.png "MCD Categorie")


![Modèle Relationnel Categorie](/uploads/docnsitale/bdd/fig/categorie_MLD.png "Modèle Relationnel Categorie")


![Modèle Relationnel utlisé](/uploads/docnsitale/bdd/fig/shema_final.png "Modèle Relationnel utlisé")

# Bilan

## Quelques remarques

* Base de données relationnelle: ensemble de tables, aucun lien physique entre les tables
* Contraintes d'intégrité :
    * Clé primaire
    * Clé étrangère (contrainte référentielle)
    * Contrainte de domaine (CHECK prix > 0, CHECK reponse IN ('O','N')...)
* `JOIN` vs Produit Cartésien: `JOIN` plus efficace
* `JOIN` indépendant des contraintes référentielles
* Exécution d'une requête:

    ```sql
    SELECT DISTINCT attribut_1, attribut_2
    FROM table1
    WHERE attribut_3 > 4 
    ORDER BY attribut_2;
    ```


## Sources

Ce cours est librement adapté d'un cours de Lille 1

* Livres
    * Des Bases de Données à l'Internet, **Philippe Mathieu**, _Vuibert_
    * Bases de Données, de la modélisation au SQL, **Laurent Audibert**, _Ellipses_

* Sources: articles Wikipedia
    * https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_relationnelle
    * https://fr.wikipedia.org/wiki/Mod%C3%A8le_relationnel
    * http://www.capa-invest.fr/portfolio/bnp-paribas-bddf/
