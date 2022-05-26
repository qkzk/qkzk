---
title: "introduction"
bookCollapseSection: true
author: qkzk
weight: 1

---

# Bases de données relationnelles

## Principe

{{< hint info >}}
Une _base de donnée_ permet de stocker efficacement une immense
quantité d'information. 

Les BDD permettent de croiser facilement les informations
et d'en extraire le contenu.
{{< /hint >}}

Les bases de données _relationnelles_ sont apparues dans les années 60 et sont
encore les plus utilisées à ce jour.

Tous les informaticiens doivent maîtriser un minimum de concepts clés relatifs
aux bases de données et doivent être capables de réaliser les manipulations de
base que nous allons présenter.

Depuis une décennie, les données sont omniprésentes et parfois moins organisées.
On a vu un usage croissant d'un autre type de base de données _NoSQL_ très utilisées
par les grands acteurs du web.


## Définitions

{{< hint info >}}
**Base de donnée (définition large)** : tout ensemble de données stockées numériquement
et pouvant servir à un (ou plusieurs) programmes.

**Base de donnée (définition restreinte)** : on appellera base de données un
ensemble de données numériques qui possède une structure ; c'est à dire dont
l'organisation répond à une logique systématique.
{{< /hint >}}

### Exemple

![données de la table ville](/uploads/docnsitale/bdd/fig/table_ville.png "données de la table ville")\

## Définitions

{{< hint info >}}
* **BDD** : ensemble des tables.
* **Table** (parfois **relation**) : c'est l'ensemble des **enregistrements** qui existent sur les données
* **Colonne** (parfois **champs** ou **attributs**) : "departement", "code" etc. : les différents champs à rempir
* **Ligne**  (parfois **Enregistrement** ou **Relations**) : "1", "2" etc. les données elles-mêmes.
* **Cellules** (parfois **Cases**) : la valeur elle même.
{{< /hint >}}

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


{{< hint info >}}
### Clé primaire (_Primary Key_) (PK)

* Identifie de manière unique une ligne
* Ne doit pas être `NULL` (vide)
* Peut être composée d'une ou plusieurs colonnes
* Ajout d'une colonne dédiée si besoin
{{< /hint >}}

{{< hint info >}}
### Clé étrangère (_Foreign Key_) (FK)
* Référence une ou plusieurs colonnes d'une autre table (représentant
une clé primaire)
* Les colonnes référencées doivent pré-exister dans la table référencée
{{< /hint >}}

### Identifier : une nécessité

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


{{< hint info >}}
### Regrouper les données en tables
* Mettre dans une même table les données relatives à un même sujet
* Créer de nouvelles tables pour éviter la redondance des données
  * Limite les incohérences lors des mises à jour
  * Facilite la construction des requêtes et améliore la pertinence des résultats
{{< /hint >}}

{{< hint info >}}
### Établir les relations entre tables
* Définir les clés primaires
  * Uniques et non NULL
* Définir les clés étrangères
  * Référencent les clés primaires
{{< /hint >}}

{{< hint info >}}
### Définir des colonnes pertinentes
* Facilité d'interrogation des colonnes
* Données cohérentes au sein d'une colonne
* Ne pas conserver des données qui peuvent être calculées
{{< /hint >}}



### Cas des catégories socioprofessionnelles du Nord.

![Fichier d'origine : CSV](/uploads/docnsitale/bdd/fig/categorie_socio_csv.png "Fichier d'origine : CSV")

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


