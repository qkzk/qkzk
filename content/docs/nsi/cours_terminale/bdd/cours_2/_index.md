---
title: Conception
lang: fr
weight: 100
---



### pdf : [pour impression](/uploads/docnsitale/bdd/cours_sql2_print.pdf), [diapo](/uploads/docnsitale/bdd/cours_sql2_slides.pdf)


<!-- à compiler par
pandoc -t beamer --slide-level 2 -V "aspectratio=1610" -s cours_sql2.md -o cours_sql2.pdf
-->

## Conception d'une base de données relationnelle

### Menu

* Conception, cas général
    * Généralités
    * Analyse
    * MCD
    * Modèle Relationnel
* Conception à partir d'un csv


# Conception, cas général

## Généralités

### Intérêts d'un Système de Gestion de Base de Données (SGBD)

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

## Généralités

### Type de SGBD
* Bases hiérarchiques (structure arborescente) ou réseau (structure de graphe)
    * navigation entre les données
* Bases relationnelles
    * Données sous forme de table, langage SQL
* Bases déductives
    * Intégration d'ensemble de règles, langage DATALOG
* Bases objet
    * Données sous forme d'objets
* Bases noSQL
    * Pas de structuration des données

## Généralités

### Exemples de SGBD Relationnels (SGDBR)
* Access (suite Microsoft Office)
* SQlite (libre, https://www.sqlite.org/index.html)
* PosgreSQL (libre, https://www.postgresql.org/)
* Oracle (https://www.oracle.com/)
* DB2 (https://www.ibm.com/analytics/db2)
* H2 (libre, www.h2database.com)

## Volumétrie
### Exemple de la banque (BNP Paribas)
* Grande masse d’informations $8.10^6$ clients
    * 4 comptes par client, donc $32.10^6$ comptes
    * 20 écritures par mois par compte, donc $6,4.10^8$ écritures par mois

* Plusieurs utilisateurs simultanément
    * 2140 agences
    * 31.460 collaborateurs
    * des milliers d’accès internet

## Analyse

* Travail préalable à la création de la base de données

* Travail Complexe et Difficile
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

![Entité client](fig/entite_client.png "Entité client")



## MCD: Notion d'Association
* Les entités peuvent être liées par des associations
* Une association est une représentation abstraite de la mémorisation d'un lien entre entités
* Elle est représentée par un cercle entre entités
     * Exemples: `commande`, `est_inscrit`, `travaille_pour`, `est_marie`, `habite_dans`....

  ![Association commande](fig/client_asso_sans_card.png "Association commande")

## MCD: Cardinalités

* Les cardinalités précisent le nombre de fois que l'entité peut intervenir dans une association.
* La valeur minimale est 0 ou 1, la valeur maximale est 1 ou n
* L'association peut-être hiérarchique (maximum 1 d'un côté, n de l'autre)  ou maillée (maximum n des deux côtés), entre une ou plusieurs entités

![Association commande](fig/asso_client_card.png "Association commande")

## MCD: Autres exemples
![Association est_inscrit](fig/etudiant_sans_card.png "Association est_inscrit")

## MCD: Autres exemples
![Association est_inscrit](fig/etudiant_card.png "Association est_inscrit")

## MCD: Autres exemples
![Association est_marie](fig/mariage_sans_card.png "Association est_marie")

## MCD: Autres exemples
![Association est_marie](fig/mariage_card.png "Association est_marie")

## MCD: Autres exemples
![Association est_divorce](fig/divorce_sans_card.png "Association est_divorce")

## MCD: Autres exemples
![Association est_divorce](fig/divorce_card.png "Association est_divorce")

## MCD: Autres exemples
![Association reservation](fig/resa_sans.png "Association reservation")

## MCD: Autres exemples
![Association reservation](fig/resa_avec.png "Association reservation")




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
* Une association (0-n)-(0-1) (lien hiérarchique) se traduit par la migration de la clé primaire côté n vers une clé étrangère (Foreign Key) côté 1

## Lien hiérarchique

![Association est_inscrit](fig/etudiant_card.png "Association est_inscrit")

![Modèle Relationnel-Lien Hiérarchique](fig/etudiant_MLD.png "Modèle Relationnel-Lien Hiérarchique")

## Passage du MCD au Modèle Relationnel
### Lien Maillé
* Une association maillée (0-n)-(0-n) donne lieu à la création d'une nouvelle table dont la clé primaire est l'union des clés primaires des entités qu'elle relie. Ces attributs sont aussi des clés étrangères.

![Association commande](fig/asso_client_card.png "Association commande")



## Lien Maillé

![Modèle Relationnel-Lien Maillé](fig/client_asso_MLD.png "Modèle Relationnel-Lien Maillé")

## Autres exemples
![Association est_marie](fig/mariage_card.png "Association est_marie")

![Modèle Relationnel mariage](fig/mariage_MLD.png "Modèle Relationnel mariage")

## Autres exemples
![Association est_divorce](fig/divorce_card.png "Association est_divorce")

![Modèle Relationnel divorce](fig/divorce_MLD.png "Modèle Relationnel divorce")

## Autres exemples

![MCD Categorie](fig/resa_avec.png "MCD Categorie")

## Autres exemples

![Modèle Relationnel Categorie](fig/resa_MLD.png "Modèle Relationnel Categorie")

# Conception à partir d'un csv

## Retour sur l'exemple des catégories socio-professionnelles
* Dans le cas où on récupère des données réelles, le problème se pose différemment
* Le dictionnaire des données est déduit du csv récupéré
* En revanche, les données réelles peuvent poser d'autres problèmes: doublons, incohérences, données non complétées ou peu exploitables
* En général, il faut faire un travail de "nettoyage" pour pouvoir créer les tables

## Construire une structure optimisée

### Regrouper les données en tables
* Mettre dans une même table les données relatives à un même sujet
* Créer de nouvelles tables pour éviter la redondance des données
  * Limite les incohérences lors des mises à jour
  * Facilite la construction des requêtes et améliore la pertinence des résultats

## Construire une structure optimisée

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

![Fichier d'origine : CSV](fig/categorie_socio_csv.png "Fichier d'origine : CSV")

## Construire une structure pertinente

### Regrouper les données en tables
* Tables = données relatives à un même sujet
  * Données sur les villes et sur les effectifs des catégories

### Éviter la redondance des colonnes
* var = Tranche + categorie
* categorie = abréviation Catégorie socioprofessionnelle

## Construire une structure pertinente


### Éviter la redondance des valeurs
* Les colonnes `departement` et `region` ne contiennent qu'une seule valeur
* À conserver uniquement si volonté d'étendre à d'autres données

### Données cohérentes
* Les colonnes Sexe, Tranche, ... contiennent aussi des totaux !
  * Les totaux peuvent être calculés à l'aide de fonctions et d'agrégats
* Décomposer `coordonnees` en deux REAL

## MCD possible

![MCD Categorie](fig/categorie.png "MCD Categorie")

## Modèle Relationnel possible

![Modèle Relationnel Categorie](fig/categorie_MLD.png "Modèle Relationnel Categorie")

## Modèle Relationnel utilisé

![Modèle Relationnel utlisé](fig/shema_final.png "Modèle Relationnel utlisé")

# Bilan

## Quelques remarques

* Base de données relationnelle: ensemble de tables, aucun lien physique entre les tables
* Contraintes d'intégrité :
    * Clé primaire
    * Clé étrangère (contrainte référentielle)
    * Contrainte de domaine (CHECK prix > 0, CHECK reponse IN ('O','N')...)
* JOIN vs Produit Cartésien: JOIN plus efficace
* JOIN indépendant des contraintes référentielles
* Exécution d'une requête:
SELECT DISTINCT attribut_1, attribut_2 FROM table1 WHERE attribut_3 > 4 ORDER BY attribut_2;


## Important
* Livres
    * Des Bases de Données à l'Internet, Philippe Mathieu, Vuibert
    * Bases de Données, de la modélisation au SQL, Laurent Audibert, Ellipses

* Sources: articles Wikipedia
    * https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_relationnelle
    * https://fr.wikipedia.org/wiki/Mod%C3%A8le_relationnel
    * http://www.capa-invest.fr/portfolio/bnp-paribas-bddf/

* Remerciements
    * Philippe Mathieu pour son aide
    * Maude pour la co-rédaction du sujet de TP
    * Eric et Philippe pour les relectures et corrections
