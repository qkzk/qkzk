---
title: "Modèle relationnel"
bookCollapseSection: true
author: "qkzk"
date: "2020/10/09"
theme: metropolis
weight: 2

---

**pdf [pour impression](/uploads/docnsitale/bdd/BDD_TD.pdf)**

**Compétence** : _Savoir analyser un modèle Entités/Associations_

# Exercice 1

On souhaite gérer des réservations dans une compagnie d'hôtels.\
On considère donc le modèle Entités/Associations suivant :

![fig1](/uploads/docnsitale/bdd/fig/fig1.png)

À l'aide de ce modèle, répondre aux questions suivantes :

1. Peut-on avoir des clients homonymes ?
2. Un client peut-il réserver plusieurs chambres à une date donnée ?
3. Est-il possible de réserver une chambre sur plusieurs jours ?
4. Peut-on savoir si une chambre est libre à une date donnée ?
5. Peut-on réserver plusieurs fois une chambre à une date donnée ?

# Exercice 2

On donne le modèle Entités/associations représentant des visites dans un
centre médical.

![fig2](/uploads/docnsitale/bdd/fig/fig2.png)

En utilisant ce modèle, répondre aux questions suivantes: 

1. Un patient peut-il effectuer plusieurs visites ?
2. Un médecin peut-il recevoir plusieurs patients dans la même consultation ?
3. Peut-on prescrire plusieurs médicaments dans une même consultation ?
4. Deux médecins différents peuvent-ils prescrire le même médicament ?

***

**Compétence** : _Savoir passer du modèle Entités/Associations au modèle relationnel._

# Exercice 3

Donner le schéma relationnel de la base de donnée "compagnie d'Hôtels" décrite
par le modèle Entités/Associations dans l'exercice 1.

# Exercice 4

Donner le schéma relationnel de la base de données "visites médicales" décrite
par le modèle Entités/Associations dans l'exercice 2.

***

**Compétence** : _Identifier le type des données ainsi que les contraintes d'intégrité
dans un modèle relationnel._

# Exercice 5

À partir du modèle relationnel construit dans l'exercice 3, remplir le tableau
ci-dessous :

| Relation    | Attribut  | Type | Unicité | Domaine éventuel | Valeur nulle permise | Clé |
|-------------|-----------|------|---------|------------------|----------------------|-----|
| Chambre     | Nom_hotel |      |         |                  |                      |     |
| Chambre     | Prix      |      |         |                  |                      |     |
| Réservation | Date_resa |      |         |                  |                      |     |
| Client      | Numéro    |      |         |                  |                      |     |

* Pour la colonne _Type_, on choisira parmi : Entier, Réel, Texte, Date.
* Pour les colonnes _Unicité_ et _Valeur nulle permise_, on répondra par Oui ou Non.
* Pour la colonne _Clé_, on mettra CP pour la clé primaire et CE pour la clé étrangère 
    ou on laissera vide.
* Pour la colonne _Domaine Éventuel_, on précisera le domaine possible.

***

**Compétence** : _Identifier les anomalies parmi les occurrences d'une relation
donnée._

# Exercice 6

On donne ci-dessous les occurrences de la relation _Consultation_ issue du
modèle relationnel construit dans l'exercice 4. Citer les anomalies
constatées :

| Numéro | Matricule | Numéro_SS       | Date_construit |
|--------|-----------|-----------------|----------------|
| 1      | 123       |                 | 21/11/2018     |
| 2      | 123       | 182086926825812 |                |
| 2      | 526       | 'Aspirine'      | 13/09/2020     |


***

**Compétence** : _Convertir une relation du modèle relationnel au modèle physique_

# Exercice 7

Supposons que la base de données de l'exercice 4 existe dans le SGBD SQlite.
On a déjà écrit les requêtes suivantes pour la création des relations _Patient_,
_Médecin_ et _Médicament_.

```sql
CREATE TABLE Patient (
    Numero_SS INT,
    Nom_patient TEXT,
    PRIMARY KEY(Numero_SS)
)

CREATE TABLE Medecin (
    Matricule INT,
    Nom_medecin TEXT,
    PRIMARY KEY (Matricule)
)

CREATE TABLE Medicament (
    Code INT,
    Libelle TEXT,
    PRIMARY KEY (Code)
)
```

Donner l'écriture avec le langage SQL permettant la création des relations
_Consultation_ et _Prescrire_.


***

# Exercice 8. Bilan

Pendant la phase de conception, toutes les donnée recueillies et spécifiées
sont inscrites dans ce que l'on appelle un dictionnaire des données. On dispose
du dictionnaire de données suivant :

| Code de la donnée | Description                   | Type   |
|-------------------|-------------------------------|--------|
| Code_ven          | Identifiant du vendeur        | Entier |
| Nom_ven           | Nom du vendeur                | Texte  |
| Ville_ven         | Ville où travaille le vendeur | Texte  |
| Code_cli          | Identifiant du client         | Entier |
| Nom_cli           | Nom du client                 | Entier |
| Rue_cli           | Rue où habite le client       | Texte  |
| Cp_cli            | Code postal du client         | Entier |
| Ville_cli         | Ville où habite le client     | Texte  |
| Dnaiss_cli        | Date de naissance du client   | Date   |
| Email_cli         | Adresse mail du client        | Texte  |
| Num_fact          | Identifiant de la facture     | Entier |
| Date_fact         | Date de facturation           | Date   |
| Num_prod          | Identifiant du produit        | Entier |
| Des_prod          | Désignation du produit        | Texte  |
| Prix_prod         | Prix du produit               | Réel   |
| Quantite          | Quantité commandée            | Entier |

1. À partir de l'analyse du dictionnaire de données précédent :

    a. Identifier les différentes entités en jeu ainsi que leurs identifiants
    b. Les 3 associations mises en jeu par ces entités seront nommées "Établir"
        "Recevoir" et "Ajouter". Pour chacune d'entre elle, spécifier leur
        cardinalité et éventuellement leurs attributs.

2. Compléter les données manquantes au modèle conceptuel Entités/Associations
    suivant :

    ![fig3](/uploads/docnsitale/bdd/fig/fig3.png)

3. En déduire le modèle relationnel
4. Donner la commande pour créer la relation _Facture_ dans le SQBD SQlite
    en considérant que la date de facturation ne peut pas être nulle.




