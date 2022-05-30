---
title: '6. TP : fusion et tris. Mini projet "TP randonnée"'
bookCollapseSection: true
author: 'qkzk'
date: '2020/07/31'
weight: 6

---

### pdf : [pour impression](/uploads/docsnsi/table_csv/6_tp.pdf)

# Exercice 1 : Fusion et tri de tables

Il est possible de fusionner 2 tableaux de données qui ont une colonne commune :

Afin de travailler sur cette fusion, nous allons travailler avec 2 fichiers au
format CSV : [fiches_client.csv](https://pixees.fr/informatiquelycee/n_site/asset/fiches_client.csv) et [fiches_com.csv](https://pixees.fr/informatiquelycee/n_site/asset/fiches_com.csv).

1. Importez ces deux fichiers dans des tables `client` et `commande`

Rien de bien complexe, nous avons un tableau qui référence les clients 
(nom, prénom, ville), chaque client possède un numéro de client. 
Le deuxième tableau référence des commandes : pour chaque commande, nous avons
un numéro de commande, une date et le numéro du client qui a passé la commande,
ce numéro de client correspond évidemment au numéro de client que l'on trouve
dans le premier tableau.

2. Affichez la table commande par numéro de commande croissant.\
    Recommencez mais cette fois par numéro de client croissant.

Sachant que nous avons deux colonnes contenant les mêmes types d'information
(numéros de client), nous allons pouvoir fusionner les deux tableaux en un seul.

3. Réaliser une fusion des deux tables en les joignant sur le numéro de client
    dans une nouelle table appelée `cl_com`.
    Prenez garde aux clients n'ayant pas passé de commandes, ils ne doivent pas
    figurer dans la table finale.
    Même chose pour les commandes ne faisant pas référence à un client de la
    table `client`, elles ne doivent pas apparaître.


Prenons l'exemple de Mme Julie Gabriaux qui habite à Bordeaux
(n° de client 2454) et de la commande effectuée le 02/02/2012 par le client
ayant le n° 2454 (commande n° 45). La cliente qui a passé cette commande n° 45
est bien Mme Gabriaux, nous avons une ligne dans notre tableau "cl-com" :

![commande Gabriaux](/docs/nsi/cours_premiere/donnees_structurees/table/6_tp/img/0.png)

4. Écrire une fonction qui renvoie le client ayant passé la dernière commande.

5. Écrire une fonction qui prend une ville et une table en paramètre et
    retourne tous les numéros de commande adressés à des clients de cette ville.

# Exerice 2 : TP randonnée


Traiter le TP sur les randonnées.
