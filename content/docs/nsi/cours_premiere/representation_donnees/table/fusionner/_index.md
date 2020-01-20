---
title: 'Fusionner des tables'
author: 'qkzk'
date: '2019/12/22'
weight: 4
---

# 4. Fusionner des tables

On accuse Raoul d'être sévère. Son avenir ? Le Goulag.

Afin de contredire ses détracteurs, il souhaite calculer la moyenne de chacun
de ses élèves.

Problème ? Les données sont dispersées dans différents fichiers !

Ils ont tous le même format

| Nom        	| Prénom  	| moyenne 	|
|------------	|---------	|---------	|
| Duchmol    	| Robert  	| 3       	|
| Lemeilleur 	| Franky  	| 14      	|
| Poivre     	| Jacques 	| 12      	|


L'approche est de récupérer chaque fichier dans une liste, de regrouper
tous les éléments dans une même liste et d'appliquer le traitement sur la liste
agglomérée.

## Construire une nouvelle table en combinant les données de deux tables

imaginons avoir deux fichiers :

`seconde2.csv` et `premiere1.csv` au format précédent.

~~~python
import csv

# on crée les listes vides.
liste_seconde = [] # les données brutes

with open('seconde2.csv', newline='') as csv_file:
  nom_eleve = csv.reader(csv_file, delimiter=';')
  for row in nom_eleve:
    liste_seconde.append(row)

# on recommence avec l'autre classe
liste_premiere = [] # les données brutes

with open('premiere1.csv', newline='') as csv_file:
  nom_eleve = csv.reader(csv_file, delimiter=';')
  for row in nom_eleve:
    liste_premiere.append(row)
~~~

À cette étape on a les deux ensembles, il faut encore nettoyer les éventuels
éléments inutiles, par exemple les champs `["nom", "prenom", "moyenne"]`

~~~python
del liste_seconde[0]
del liste_premiere[0]
~~~

Et créer l'objet complet :

~~~python
notes = liste_seconde + liste_premiere
~~~

## Domaine de valeur

Gros problème en perspective : si les données ont des formats différents ???


**seconde**


| Nom        	| Prénom  	| moyenne 	| avis 	      |
|------------	|---------	|---------	|------------	|
| Duchmol    	| Robert  	| 3       	| nul       	|
| Lemeilleur 	| Franky  	| 19      	| moyen      	|
| Poivre     	| Jacques 	| 12      	| méchant   	|

**première**

| Nom        	| Prénom  	| DS1     	| DS2 	      | moyenne 	|
|------------	|---------	|---------	|------------	|---------	|
| Durant    	| Martine  	| 1       	| 5         	| 3       	|
| Philonard 	| Albert  	| 16      	| 12        	| 14      	|
| Pommier    	| Fanny   	| 13      	| 14        	| 12      	|

On considère alors ce qu'on peut qualifier de **domaine de valeur**, c'est
l'ensemble des champs qui sont communs.

Ici : Nom, Prénom, moyenne

Il faut ajouter une étape, de formatage des valeurs, consistant à donner
à chaque enregistrement la même allure qu'aux autres.


Par exemple, pour formater un enregistrement :

~~~python
def formater_eleve(eleve):
  return {"nom": eleve["nom"],
          "prenom": eleve["prenom"],
          "moyenne":eleve["moyenne"]}
~~~

On doit parcourir la liste et en créer une nouvelle, avant de fusionner :

~~~python
premieres_formatees = [formater_eleve(eleve) for eleve in liste_premiere]
secondes_formatees = [formater_eleve(eleve) for eleve in liste_seconde]
~~~

Chaque série ayant un format particulier, il peut-être nécessaire de les traiter
individuellement.

Enfin, on peut tout regrouper et obtenir l'ensemble avec un format cohérent :

~~~python
eleves_formates = secondes_formatees + premieres_formatees
~~~

## Enregistrer les données

Cette notion n'est pas explicitement au programme mais me parait indispensable,
une fois un formatage effectué, on peut souhaiter conserver les valeurs.

On se contentera donc d'écrire avec le module csv.

Exemple adapté de la documentation :

~~~python
import csv
with open('notes.csv', 'wb') as csvfile:
    moyenne_writer = csv.writer(csvfile, delimiter=',')
    moyenne_writer.writerow(['nom', 'prenom', 'moyenne'])
    moyenne_writer.writerow(['Duchmol', 'Robert', '3'])
    moyenne_writer.writerow(['Dupond', 'Francine', 18.5])
    moyenne_writer.writerow(['Durand', 'Franky', 14])
~~~

remarquons que les "moyennes" ne sont pas homogènes (str, float, int).

csv.writer s'en moque, il écrira des chaînes de caractères !

Remarquons aussi les paramètres utilisés pour "ouvrir" le fichier : `wb`

* `w` : ouvrir en mode écriture
* `b` : pour binary, effectue des transformations spécifiques à chaque plateforme (windows, linux etc.) qui évitent de corrompre les données. Pour du texte, comme nous, c'est juste de la prudence.

Enfin, le `delimiter` est la virgule, pas le 'point-virgule'

C'est un choix comme un autre, il faudra s'en souvenir !

Bien sûr, on peut faire une boucle qui parcourt la liste entière et ajoute chaque élément...

~~~python
import csv
with open('notes.csv', 'wb') as csvfile:
    moyenne_writer = csv.writer(csvfile, delimiter=',')
    moyenne_writer.writerow(['nom', 'prenom', 'moyenne'])
    for eleve in eleves_formates:
      moyenne_writer.writerow([eleve['nom'], eleve['prenom'], eleve['moyenne']])
~~~

## Conclusion

* On a vu dans ce chapitre comment importer dans Python des données d'un format
  texte courant, le CSV
* On sait maintenant comment chercher des données et tester leur cohérence
* On peut aussi trier ces tables de données selon un critère donné
* Enfin, on peut regrouper des données de différentes sources, en s'assurant
  que les domaines de valeurs correspondent.
* Les enregistrer dans un format particulier peut-être commode et ne présente
  pas de difficulté.
