---
title: Water Ripple
author: qkzk
date: 2025-12-12
theme: metropolis
weight: 1000
bookCollapseSection: true
geometry: "margin=1.5cm"

---


## Description

![Water ripple](./water_ripple.png)

L'objectif de ce projet est de mettre en oeuvre un algorithme appelé "_damping_" et qui permet de modéliser des ondes aquatiques.

Lorsque des pierres tombent dans l'eau, des ondes se propagent depuis le point d'impact et peuvent se rencontrer.

L'algorithme, cité plus bas, nécessite beaucoup de calculs et doit être appliqué à un nombre restreint de "tuiles" qui sont des carrés de pixels.

L'interface finale va présenter une fenêtre dans laquelle on peut faire partir des ondes depuis l'endroit où on clique.

## Algorithme

```
damping = some non-integer between 0 and 1

  begin loop 
      for every non-edge element:
      loop
          Buffer2(x, y) = (Buffer1(x-1,y)
                           Buffer1(x+1,y)
                           Buffer1(x,y+1)
                           Buffer1(x,y-1)) / 2 - Buffer2(x,y)
 
          Buffer2(x,y) = Buffer2(x,y) * damping
      end loop

      Display Buffer2
      Swap the buffers 

  end loop
```

Le principe est simple :

On garde une grille (tableau 2D) avec la couleur des tuiles.

- Lorsqu'on clique quelque part, on change la valeur de la tuile à la valeur maximale.
- D'une frame à l'autre, on copie les pixels, on calcule le nouvel état et il remplace le précédent état.

## Objectif 

- Implémenter convenablement cet algorithme. Son code doit être clair et bien découpé
- Implémenter une interface avec **pgzero** (pas pygame seul) où l'on peut cliquer pour créer des vagues.

Dans le resultat, les vagues rebondissent sur les bords.


## Source

* [the coding train - challenge 102](https://www.youtube.com/watch?v=BZUdGqeOD0w)
* [water effect](https://web.archive.org/web/20160418004149/http://freespace.virgin.net/hugo.elias/graphics/x_water.htm)

