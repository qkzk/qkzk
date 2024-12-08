---
title: "TP Commandes"
author: qkzk
theme: metropolis
weight: 100
---

{{< hint info >}}
Ce TP intéractif s'exécute directement dans le navigateur... ou presque.
Certaines questions sont débranchées et doivent être traitées à l'extérieur.

Chaque chargement de la page réinitialise vos requêtes, pensez à sauvegarder vos requêtes au fur et à mesure.
{{< /hint >}}

{{< hint danger >}}
Ce TP couvre le programme... et le dépasse largement !
{{< /hint >}}

# Première partie : Jean-Pierre Combani, un aventurier moderne.

Le magasin SuperDéco souhaite augmenter son chiffre d'affaire.
Pour cela ils envisagent d'améliorer l'enregistrement des commandes.

Ils souhaitent utiliser une base de donnée et font appel à vos services (personne ne rit).

Voici leurs objectifs :

- associer une commande à un client,
- associer une commande à un vendeur,
- enregistrer des clients et vendeurs homonymes,
- connaître les dates, montant des commandes et mode de paiement,
- recenser les adresses postales et mail de leurs clients,
- connaître la position hierarchique et la date d'embauche des vendeurs.

## Modèle relationnel

{{< hint danger >}}
Décrire un modèle relationnel permettant de réaliser cet objectif.
{{< /hint >}}

On n'oubliera pas les clés primaires et étrangères.

On peut répondre par un diagramme complet ou un schéma relationnel.

## Conformité du modèle

Voici les requêtes ayant servi à la construction des tables `commande`, `client` et `vendeur`.

```sql
CREATE TABLE "vendeur" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"Nom"	        TEXT    NOT NULL,
	"Prenom"	    TEXT    NOT NULL,
	"Grade"	        INTEGER NOT NULL,
	"Embauche"	    TEXT    NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "client" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"Nom"	        TEXT    NOT NULL,
	"Prenom"	    NUMERIC NOT NULL,
	"Ville"	        TEXT    NOT NULL,
	"code_postal"	TEXT    NOT NULL,
	"Adresse"	    TEXT    NOT NULL,
	"email"	        TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "commande" (
	"id"	        INTEGER NOT NULL UNIQUE,
	"id_vendeur"	INTEGER NOT NULL,
	"id_client"	    INTEGER NOT NULL,
	"montant"	    INTEGER NOT NULL,
	"reglement"	    TEXT    NOT NULL,
	"date"	        TEXT    NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("id_client")  REFERENCES "client"("id"),
	FOREIGN KEY("id_vendeur") REFERENCES "vendeur"("id")
);
```

{{< hint danger >}}

1. Ce modèle est-il conforme à celui que vous avez retenu ? S'il y a des différences expliquez les.
   {{< /hint >}}

Depuis que l'informaticien stagiaire non rémunéré est devenu influenceur, la base de donnée n'est plus enretenue.

Cinq ventes, présentées ci-dessous, ont été réalisées par le nouveau vendeur, Jean-Pierre Combani.
Elles concernent de nouveaux clients.

| Client           | Vendeur             | Date       | Paiment | Montant |
| ---------------- | ------------------- | ---------- | ------- | ------: |
| Durpet Micheline | Combani Jean-Pierre | 2022/04/19 | Espèce  |   1234€ |
| Siterne Frank    | Combani Jean-Pierre | 2022/04/21 | Chèque  |   3495€ |
| Siterne Frank    | Combani Jean-Pierre | 2022/05/02 | Espèce  |    625€ |
| Morteau Chaïna   | Combani Jean-Pierre | 2022/05/12 | Espèce  |   2455€ |
| Siterne Frank    | Combani Jean-Pierre | 2022/05/18 | Espèce  |     75€ |

{{< hint danger >}} 2. Dans quel ordre saisir les éléments dans la base ? Justifier. **On ne demande pas encore d'écrire de requêtes, seulement l'ordre.**
{{< /hint >}}

## Sélections simple

{{< hint danger >}}

1. Écrire une requête permettant d'afficher tous les clients.
2. Écrire une requête affichant les vendeurs triés par date de recrutement.
3. Écrire une requête affichant les clients habitant Lille.
   {{< /hint >}}

{{< sql title="Sélections simples" init="editions.sql">}}

{{< /sql >}}

## Modifications

{{< hint danger >}}

1. Écrire une requête insérant le nouveau vendeur : Jean-Pierre Combani, recruté le 10 avril 2022, grade 2.
2. Ajouter les clients Durpet Micheline et Siterne Frank habitant tous deux au 1, avenue des Fleurs à Lille, 59000 et d'emails
   respectifs cemimi@exemple.com et frankyyy@exemple.com.
   Ainsi que Morteau Chaïna, habitant 23, rue de la République à Lille, 59000: cjeje@exemple.com.
3. Suite à des travaux réalisés par Jean-Pierre Combani dans la chambre du couple Durpet-Siterne, le couple s'est séparé.
   Modifier l'adresse de Siterne Frank qui a déménagé au 23 rue Basse à Lille.
4. Vérifier tous les ajouts et modifications avec une ou plusieurs requêtes.
   {{< /hint >}}

{{< sql title="Modifications" init="editions.sql">}}

{{< /sql >}}

## Requêtes complexes

{{< hint danger >}}

1.  Afficher toutes les numéros de commande, nom et prénom du client des commandes dont le montant dépasse 1000€.
2.  Afficher tous les clients (nom, prénom, email) ayant passé une commande à la vendeuse Kezac Annie.
3.  Écrire une requête affichant les commandes (nom & prénom du client, du vendeur, date, mode de paiement, montant)
    d'un montant qui dépasse 1000€.
4.  Ajouter les commandes du tableau précédent.

    _On pourra commencer en utilisant les `id` des clients et du vendeur récupérées dans des requêtes préalables._

    _Ensuite, pour pouvoir ajouter une commande en une requête n'utilisant que les noms du vendeur et du client il faut utiliser :_

    ```sql
    INSERT INTO table
    SELECT (...);
    ```

    _Par exemple :_

    ```sql
    INSERT INTO table1 ( column1, column2, someInt, someString )
    SELECT  table2.column1, table2.column2, 8, 'some string etc.'
    FROM    table2
    WHERE   table2.ID = 7;
    ```

    _Documentation : [W3 Schools](https://www.w3schools.com/sql/sql_insert_into_select.asp)_

    {{< /hint >}}

{{< sql title="Requêtes complexes" init="editions.sql">}}

{{< /sql >}}

# Seconde partie : les ravages de Jean-Pierre Combani

Un an s'est écoulé... Et de nombreuses commandes ont eu lieu.
Les comptes de SuperDéco ne se sont guère améliorés mais, grace à la base de donnée
ils peuvent enfin comprendre d'où vient le problème.

Jean-Pierre Combani a été licencié pour faute grave et un procès est en cours d'instruction.
Il a diminué le montant de toutes ses commandes en espèce de 200€ afin de voler l'entreprise !

Il faut prévenir ses clients et rectifier les montants dans la base de donnée.

## Modifications complexes

{{< hint danger >}}

1. Afficher toutes les informations des clients de Jean-Pierre Combani
   (nom, prenom, adresse postale) ayant payé en espèce.
   Afin d'éviter les envois multiples de recommandés on retirera les doublons.

2. Compter les commandes réglées en espèces à Jean-Pierre Combani. Calculer le
   total de ce qu'il a volé.

3. Rectifier les montants des commandes frauduleuses dans la base de donnée.
   {{< /hint >}}

{{< sql title="Modifications complexes" init="editions_partie2.sql">}}

{{< /sql >}}
