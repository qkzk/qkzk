---
title: Ms Paint
author: qkzk
date: 2025-12-12
theme: metropolis
weight: 1300
bookCollapseSection: true
geometry: "margin=1.5cm"

---

## Présentation 

L'objectif de ce projet est de créer une "application" de dessin très simple en Python + pgzero.

![mspaint](./mspaint.png)

## Ambitions minimales

1. pouvoir dessiner des lignes de couleurs différentes en cliquant et gardant le bouton gauche enfoncé.
2. changer de couleur (aléatoirement, en cliquant sur des cases, avec le clavier... comme vous voulez)
3. pouvoir exporter une capture d'écran vers un fichier
4. pouvoir vider l'écran et repartir d'une page vierge


## Contraintes

Le projet doit être rédigé en Python + PG zero. 

Il n'est pas nécessaire d'employer beaucoup de pygame pur pour en venir à bout, pgzero fournit tout le nécessaire.

## Extensions

La majorité des fonctions de MsPaint peuvent être implantées relativement facilement mais certaines sont délicates.

1. sélectionner (via un rectangle ou une forme) : difficile 
2. effacer / gomme (plus ou moins facile)
3. selectionner une couleur depuis l'image : facile 
4. écrire du texte : moyen
5. tracer des lignes, rectangles, cercles : moyen 
6. changer de crayon / pinceau : facile 
7. "pot de peinture" : difficile
8. sauvegarder dans un format spécifique : bmp, jpg, png : de facile à très difficile selon l'approche envisagée
9. ouvrir un fichier et l'éditer : de facile à très difficile selon l'approche envisagée
