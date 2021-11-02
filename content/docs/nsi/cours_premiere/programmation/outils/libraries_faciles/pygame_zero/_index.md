---
author: qkzk
date: 2019-12-10 07:08:58+00:00
draft: false
title: Pygame Zero
bookCollapseSection: true
weight: 2
---


# Pygame Zero


_Cette brève présentation est une traduction de la page d'accueil de la_
_[documentation officielle](https://pygame-zero.readthedocs.io/en/stable/)_
_de la librairie._

## Pygame Zero

Pygame Zero permet de créer des jeux sans devoir répéter des dizaines
d'instructions.

Elle est conçue pour être employée dans l'éducation afin de se
concentrer sur la programmation de base sans devoir détailler le
fonctionnement de l'API de Pygame ou écrire une boucle d'événement.

## Introduction à Pygame Zero

D'abord, créer un fichier vide appelé `intro.py`

Vérifiez qu'il tourne et crée bien une fenêtre vide en lançant :

~~~bash
$ pgzrun intro.py
~~~

Tout est optionnel dans Pygame Zero ; un fichier vide est un script
Pygame Zero valide !

Vous pouvez quitter le jeu en cliquant sur la croix ou en pressant `CTRL+Q`.
Si le jeu cesse de répondre pour n'importe quelle raison, vous pouvez
l'arrêter en pressant CTRL+C

## Dessiner une fenêtre

Maintenant, ajoutons une fonction `draw()` et réglons les dimensions de la
fenêtre. PygameZero va appeler cette fonction à chaque fois qu'il
doit redessiner la fenêtre.

Dans `intro.py` ajouter les lignes suivantes :

~~~pygame
WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((128, 0, 0))
~~~

Relancez `pgzrun intro.py` et l'écran devrait être un carré rouge.

Que fait ce code ?

`WIDTH` et `HEIGHT` définissent la largeur et la hauteur de votre fenêtre.
Le code permet de définir une fenêtre de 300 pixels dans chaque direction.

`screen` est un objet interne qui représente la fenêtre d'affichage. Il
dispose d'un [vaste panel de méthodes pour dessiner des sprites et des formes.](https://pygame-zero.readthedocs.io/en/stable/builtins.html#screen).
L'appel à la méthode `screen.fill()` remplit l'écran à l'aide d'une couleur unie
spécifié dans un tuple de couleur `(red, green, blue)`. `(128, 0, 0)` sera un
rouge plutôt sombre.

Essayez de changer ces valeurs par des nombres entre 0 et 255 et regardez la
couleurs que vous obtenez.

[(...)](https://pygame-zero.readthedocs.io/en/stable/introduction.html)
