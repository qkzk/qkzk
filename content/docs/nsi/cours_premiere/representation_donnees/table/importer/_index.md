---
title: 'Importer les données'
author: 'qkzk'
date: '2019/12/22'
weight: 1
---

# Le programme

Les données organisées en table correspondent à une liste de p-uplet nommés qui partagent les mêmes descripteurs. La mobilisation de ce type de structure de données permet de préparer les élèves à aborder la notion de base de données qui ne sera présentée qu'en classe terminale. Il s'agit d'utiliser un tableau doublement indexé ou un tableau de p-uplets, dans un langage de programmation ordinaire et non das un système de gestion de bases de données.

| **Contenus**             	|- 	| **Capacités attendues**                                                                        	| **Commentaires**                                                                                       	  |
|--------------------------	|-- |------------------------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------------------------	|
| Indexation de tables     	| 	| Importer une table depuis un fichier texte tabulé ou un fichier CSV.                           	| Est utilisé un tableau doublement indexé ou un tableau de p-uplets qui partagent les mêmes descripteurs 	|
| Recherche dans une table 	| 	| Rechercher les lignes d'une table vérifiant des critères exprimés en logique propositionnelle. 	| La recherche de doublons, les tests de cohérence d'une table sont présentés                            	  |
| Tri dans une table       	| 	| Trier une table suivant une colonne.                                                           	| Une fonction de tri intégrée au système ou à une bibliothèque peut être utilisée                       	  |
| Fusion de tables         	| 	| Construire une nouvelle table en combinant les données de deux tables                          	| La notion de domaine de valeurs est mise en évidence                                                   	  |


# 1. Les données en table

Par "données en table" on entend ce type d'information :


* sans mise en forme

  ![dans un tableur](http://www.cours-excel.fr/wp-content/uploads/2013/01/csv_1.png)

* avec mise en forme

  ![dans un tableur](https://www.mydsomanager.com/img/help/fr-creation-fichier-csv.jpg)

* depuis un fichier texte

  ![dans un fichier texte](https://www.ente-aix.fr/documents/177-qgisv2/M08/res/i_30_10_Edition_fichier_Bati_remarquable_csv.png)

Excel et les tableurs évolués réalisent un traitement complexe des données mais on peut toujours exporter
un tableau de données vers un fichier au format particulier ou importer un tel fichier.

## Le format CSV

CSV, pour Comma Separated Values (valeurs séparées par des virgules), est un format standard utilisé pour stocker des données
dans des fichiers textes.

~~~csv
Nom,prenom,email
Duchmol,Robert,robert@email.com
Lemeilleur,Franky,franky@email.com
Poivre,Jacques,jacque@email.com
~~~


* Une **première ligne** peut-être utilisée pour **présenter les contenus** des colonnes
* Les **lignes suivantes** contiennent les **données** séparées par un même symbole, _normalement_ la virgule.

En France on rencontre souvent la séparation par des **points virgules**, étant donné
que la virgule est le séparateur décimal le plus souvent employé.


Ce qui donne :

| Nom        	| Prénom  	| email            	|
|------------	|---------	|------------------	|
| Duchmol    	| Robert  	| robert@email.com 	|
| Lemeilleur 	| Franky  	| franky@email.com 	|
| Poivre     	| Jacques 	| jacque@email.com 	|


## Le stockage de données

Soyons honnête, stocker des données dans un fichier texte est une mauvaise idée.
Ce n'est pas génant quand on a peu de données ou pour les partager mais cela devient
vite pénible de les manipuler.

Vous vous doutez bien que Facebook ou Netflix ne stockent pas vos informations dans un fichier texte...

En terminale on étudiera les **bases de données** et en particulier SQL.

Ce sont des programmes qui permettent à plusieurs utilisateurs d'accéder aux ressources,
de conserver une trace de ce qui est fait sur les données etc.

## Nos objectifs

Cette année nous allons apprendre à

* importer un fichier CSV en Python (de deux manières)
* manipuler les données dans Python :
  * chercher,
  * modifier,
  * trier selon des critères,
  * fusionner des tables
* écrire des données dans un fichier

## Les autres formats texte

Il existe de nombreux formats permettant de stocker des données, citons :

* CSV, le plus couramment employé, démocratisé par Excel (Microsoft)
* JSON (Javascript Object Notation)

~~~json
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
~~~

* XML (eXtensible Markup Language) - avis perso : berk. Du HTML amélioré

~~~xml
<!DOCTYPE glossary PUBLIC "-//OASIS//DTD DocBook V3.1//EN">
 <glossary><title>example glossary</title>
  <GlossDiv><title>S</title>
   <GlossList>
    <GlossEntry ID="SGML" SortAs="SGML">
     <GlossTerm>Standard Generalized Markup Language</GlossTerm>
     <Acronym>SGML</Acronym>
     <Abbrev>ISO 8879:1986</Abbrev>
     <GlossDef>
      <para>A meta-markup language, used to create markup
languages such as DocBook.</para>
      <GlossSeeAlso OtherTerm="GML">
      <GlossSeeAlso OtherTerm="XML">
     </GlossDef>
     <GlossSee OtherTerm="markup">
    </GlossEntry>
   </GlossList>
  </GlossDiv>
 </glossary>
~~~

Mais aussi :

* YAML (yet another markup language)

~~~yaml
-  martin:
    name: Martin D'vloper
    job: Developer
    skills:
      - python
      - perl
      - pascal
-  tabitha:
    name: Tabitha Bitumen
    job: Developer
    skills:
      - lisp
      - fortran
      - erlang
~~~

Pour simplifier :

* Généré par un programme ? Souvent XML
* Crée à la main depuis un tableur ? CSV
* Utilisé par des machines pour communiquer via une API ? JSON
* Pour stocker des configurations de programme ? Yaml, INI, format propriétaire

L'informatique étant la science des données, vous aurez fréquemment à
en manipuler.


## Importer un fichier CSV en Python

Voyons d'abord comment réaliser chacune des étapes (c'est un attendu) puis
comment le faire à l'aide des outils proposés.

### 1. à la main

~~~python
CHAMPS = ["nom", "moyenne", "moyenne_brute"]

def lire_fichier_csv(filename, delimiter=',', champs=CHAMPS):
  res = []
  with open(filename) as f:
    f.readline() # on zappe la première ligne...
    l = f.readline()
    while l != '':
      args = l.replace('"', '').strip().split(delimiter)
      try:
        enregistrement = {}
        for i in range(len(args)):
          enregistrement[champs[i]] = args[i]
        res.append(enregistrement)
      except ValueError:
        pass
      l = f.readline()
    return res

liste_csv = lire_fichier_csv('2nde-14-liste.csv', delimiter=';')
~~~

ouch !

#### Commentaires détaillés sur la fonction `lire_fichier_csv`

* ligne 3 : on crée la liste des enregistrements
* ligne 4 : on ouvre le fichier et on le stocke dans une variable temporaire `f`
* ligne 5 : `f.readline()` : lire une ligne et avancer à la suivante
* ligne 6 : on a zappé la première ligne et on lit la seconde
* ligne 4 : tant qu'on a des lignes non vides
* ligne 8 : on nettoie la ligne : virer les ", les espaces de début et de fin et on sépare la ligne tous les 'delimiter'
* ligne 9 : on essaye de créer l'enregistrement
* ligne 10 : c'est un dictionnaire
* ligne 11 : on affecte à chaque champ son nom
* ligne 12 : on l'ajoute à la liste des enregistrements
* ligne 15 : si jamais la ligne est imparfaite, on la zappe
* ligne 16 :  on avance à la ligne suivante

### 2. avec le module csv

C'est beaucoup plus simple !

~~~python
import csv

# on crée les listes vides.
liste_csv = [] # les données brutes

with open('2nde-14-liste.csv', newline='') as csv_file:
  nom_eleve = csv.reader(csv_file, delimiter=';')
  for row in nom_eleve:
    liste_csv.append(row)
~~~

Remarquons que `csv.reader` et `lire_fichier_csv` ont la même signature.


## Résultat d'un chargement

Qu'obtient-on à cette étape ?

Tout dépend du traitement !

Si vous avez fait un traitement "propre" des données, elles sont déjà rangées
dans une liste avec :

* 1 ligne du fichier par élément de la liste
* pas de ligne pour l'entête inutile
* des dictionnaires Python avec de la forme `{"nom": "Boutemps", "prenom": "Robert"...}`
