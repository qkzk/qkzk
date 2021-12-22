---
title: "Intro - selection"
bookCollapseSection: true
weight: 1

---

### PDF : [Pour impression](./1_cours_selection.pdf)

# Trier

## Trier : définition.

Algorithme de **tri**

> Algorithme qui, partant d'une liste, renvoie une version ordonnée de la liste.
> $$[5,1,4,3,2] \rightarrow [1,2,3,4,5]$$

## Trier : pourquoi ?

Trier est une opération fréquente, certains algorithmes (dichotomie par
exemple) partent d'un tableau déjà trié.


Tous les langages "haut niveau" proposent une fonction native pour trier
les tableaux. 

En terminale on utlisera des bases de données et on apprendra à répondre
à des questions du type : "quels sont les 5 films les plus vus au cinéma ?"
ou bien "déterminer les 100 derniers inscrits à un jeu en ligne".

Ces sélections **nécessitent un tri**

Notre objectif n'est pas _d'utiliser_ en pratique nos algorithmes
mais de **comprendre leur fonctionnement.**


## Trier : de nombreux algorithmes

Tous les algorithmes de tri ne se valent pas. Nous allons les étudier de plus en plus précisemment.


## Trier : de nombreux algorithmes


Il existe de nombreux algorithmes de tri.

* **Tri par insertion** -> 1ère
* **Tri par sélection** -> 1ère
* Tri à bulle
* Tri rapide
* **Tri fusion** -> Terminale
* Tri par tas
* Smoothsort
* **Timsort** -> Python

## Activité : Trier des boîtes

L'important, c'est **comment ?**

### Description de la séquence

* Vous disposez de boîtes opaques contenant des poids différents,
* Vous pouvez aisément comparer deux boîtes entre elles afin de repérer la plus
légère,
* Il est impossible de connaître la masse des boîtes.

Vous avez 25 minutes pour :

1. écrire un algorithme "papier" qui réalise le tri des boites
2. permette à n'importe qui de le reproduire et d'aboutir au résultat
3. aucune explication supplémentaire ne doit être apportée

---


# Tri par sélection 

## Tri par sélection 

```
Je débute avec un tableau non trié plein et un tableau trié vide.
Tant qu'il y a des objets non triées :
   Je cherche le plus petit des objets non triés,
   Je le place à la suite des objets déjà triée.
fin Tant que
```


## Le plus petit des objets non triés

```
Entrée : Des objets
Sortie : L'objet le plus petit

Je prends un objet
Pour chacune des autres:
    S'il est plus petit que l'objet choisi
      Alors j'échange.
	Fin Si
	Je mets l'autre de côté.
Fin Pour
```
