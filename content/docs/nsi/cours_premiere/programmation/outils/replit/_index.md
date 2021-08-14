---
title: REPL.it
author: qkzk
weight: 7
---

### pdf : [pour impression](/uploads/docsnsi/programmation/repl/presentation_repl_print.pdf) et [diaporama](/uploads/docsnsi/programmation/repl/presentation_repl_slides.pdf)

# REPL

## REPL

L'acronyme **Read-Eval-Print loop** désigne une interface dans laquelle on peut
écrire une commande, l'exécuter, voir s'afficher une réponse et recommencer.

En programmation on parle souvent **console** et dans l'utilisation d'un
système unix de **shell** ou d'interface en ligne de commande **CLI**.

## repl.it

**[repl.it](https://repl.it)** est un site fondé par la startup américaine du
même nom que nous allons utiliser cette année pour les exercices sur Python.

Certains d'entre vous connaissent déjà repl et vont à nouveau pester contre
son interface...

Nous allons principalement utiliser les exercices en ligne sans trop nous
intéresser aux autres fonctionnalités de repl.

## Programmes en ligne

**repl** permet aussi de réaliser un programme en ligne dans de nombreux langages.

Si vous avez accès à internet, vous pouvez développer dans repl.

## Exemple de programme en ligne

![myRepl](/uploads/docsnsi/programmation/repl/myrpl.png)

## Exemple de programme en ligne

La fenêtre se découpe en 4 parties :

1. tout à gauche `Files` présente les différents fichiers
2. La grande colonne blanche présente les sources du fichier actuellement ouvert
3. A droite on trouve les sorties. Ici ce programme comporte à la fois un site
    web (blanc) et une sortie console (noir).

## Que fait ce programme ?

C'est en fait un bot discord (qui ne fait pas grand chose).

Le site web force repl.it à laisser le bot tourner tant qu'un utilisateur se
connecte toutes les heures.

J'utilise donc un autre outil en ligne pour rafraîchir une page toutes les 30
minutes et le programme tourne presque indéfiniment.

Il se relance chaque fois que repl.it installe une mise à jour majeure.



## Exercices en ligne

Repl permet de partager des exercices auto corrigés. Vous avez un énoncé,
tentez de répondre et soumettez votre réponse. Dès qu'elle est validée,
vous pouvez passer au suivant.

# Exemple

## Interface

![repl_student](/uploads/docsnsi/programmation/repl/repl_student.png)

## Interface

L'interface comporte donc 3 parties et 2 boutons importants

* Haut gauche : le code source de votre programme
* Bas gauche : la console Python dans laquelle vous pouvez le tester
* Droite : la consigne
* le bouton RUN : permet d'exécuter votre script pour l'essayer
* le bouton vert SUBMIT : envoie votre programme et le soumet à des tests.
  S'ils passent tous, vous pouvez avancer. Sinon on vous dit pourquoi ils échouent.

## Entrées / Sorties

L'intérêt de repl est manifeste : vous progressez sans que je doive valider
chacune de vos réponses...

L'inconvénient est que nous allons devoir utiliser deux fonctions qu'il faut
"normalement" éviter : `input` et `print`

Ce ne sont des fonctions qui ne servent qu'à **lire depuis la console** et
**afficher dans la console.**

Les entrées et sorties d'un programme traditionnel ne sont pas "`input`" et "`print`"

## Remarques sur les consignes

Les consignes présentent **toujours un exemple issu des tests.**

# S'inscrire et rejoindre la classe

## S'inscrire

1. Dans le navigateur rendez-vous sur [repl.it](https://repl.it)
2. Si vous n'avez pas encore de compte, cliquez sur **sign up**.

    Utilisez google et le mail fourni pour classroom

3. Si vous avez déjà un compte : **login**

## Accéder aux exercices

Vous devez vous inscrire dans une **classe** en mode **student**. La dernière
page du diaporama contient le lien d'invitation vers la classe.

Il vous suffit de le copier dans votre navigateur Chrome.

Vous aurez alors accès à cette page dans laquelle vous pouvez cliquer sur la
classe et choisir un exercice.

## Réaliser un exercice ensemble

la consigne est simple :

Statement

Ecricre un programme qui prenne trois nombres et imprime leur somme. Chaque
nombre est donné sur une ligne à part.

Exemple d'entrée

~~~
2
3
6
~~~

Exemple de sortie

~~~
11
~~~


## Réaliser un exercice ensemble

Le code source se présente ainsi :

~~~python
# Ce programme lit deux nombres
# en entrée et imprime leur somme :
a = int(input())
b = int(input())
# c =

# Pouvez-vous le modifier afin qu'il imprime
# la somme de trois nombres ??

print(a + b)
~~~

Si on soumet maintenant les tests vont échouer

## Réaliser un exercice ensemble

Le code source se présente ainsi :

~~~python
# Ce programme lit deux nombres
# en entrée et imprime leur somme :
a = int(input())
b = int(input())
c = int(input())

# Pouvez-vous le modifier afin qu'il imprime
# la somme de trois nombres ??

print(a + b + c)
~~~

## Réaliser un exercice ensemble

Cliquer sur **run**, taper 3 nombres dans la console :

* 1 ENTREE
* 2 ENTREE
* 3 ENTREE

On voit alors apparaître leur somme. C'est juste !

On clique sur **submit** et les tests sont validés.


## Résumé

1. Lire la consigne
2. Comprendre la consigne (c'est mieux)
2. Essayer jusqu'à réussir
3. Soumettre
