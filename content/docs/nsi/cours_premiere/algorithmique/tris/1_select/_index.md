---
title: "Intro - selection"
bookCollapseSection: true
weight: 1
---

# Trier

PDF : [Pour impression](./1_cours_selection.pdf)

## Définition.

Algorithme de **tri**

{{< hint info >}}
Algorithme qui, partant d'une liste, renvoie une version ordonnée de la liste.
`[5,1,4,3,2] -> [1,2,3,4,5]`
{{< /hint >}}

## Pourquoi ?

Trier est une opération fréquente, certains algorithmes (dichotomie par
exemple) partent d'un tableau **déjà trié**.

Tous les langages "haut niveau" proposent une fonction native pour trier
les tableaux.

En terminale on utlisera des bases de données pour répondre
à des questions du type :

> _" Quels sont les 5 films les plus vus au cinéma ? "_

ou bien :

> _" Déterminer les 100 derniers inscrits à un jeu en ligne "_

Ces sélections **nécessitent un tri**

Notre objectif n'est pas _d'utiliser_ en pratique nos algorithmes
mais de **comprendre leur fonctionnement.**

## De nombreux algorithmes

Il existe de nombreux algorithmes de tri et ils ne se valent pas.
Certains sont plus efficaces que d'autres de manière générale, d'autres sont pratiques
dans des cas particuliers.

Citons par exemple :

- **Tri par insertion** -> 1ère
- **Tri par sélection** -> 1ère
- Tri à bulle
- Tri rapide
- **Tri fusion** -> Terminale
- Tri par tas
- Smoothsort
- **Timsort** -> Python

Les algorithmes de première ont des caractéristiques communes : il sont simples et lents.

## Activité : Trier des boîtes

L'important, c'est **comment ?**

### Description de la séquence

- Vous disposez de boîtes opaques contenant des poids différents,
- Vous pouvez aisément comparer deux boîtes entre elles afin de repérer la plus
  légère,
- Il est impossible de connaître la masse des boîtes.

Vous avez 25 minutes pour :

1. écrire un algorithme "papier" qui réalise le tri des boites
2. permette à n'importe qui de le reproduire et d'aboutir au résultat
3. aucune explication supplémentaire ne doit être apportée

---

Généralement, les élèves proposent un des trois algorithmes "naturels" :

- tri par sélection,
- tri par insertion,
- tri à bulle.

Nous allons d'abord étudier le _tri par sélection_.

## Tri par sélection

{{< hint info >}}

```
Je débute avec un tableau non trié plein et un tableau trié vide.
Tant qu'il y a des objets non triés :
   Je cherche le plus petit des objets non triés,
   Je le place à la suite des objets déjà triés.
fin Tant que
```

{{< /hint >}}

## Le plus petit des objets non triés

{{< hint info >}}

```
Entrée : Des objets
Sortie : L'objet le plus petit

Je prends un objet
Pour chacun des autres:
    S'il est plus petit que l'objet choisi
      Alors j'échange.
	Fin Si
	Je mets l'autre de côté.
Fin Pour
```

{{< /hint >}}
