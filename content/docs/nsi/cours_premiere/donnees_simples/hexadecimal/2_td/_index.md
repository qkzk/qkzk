---
title: "Hexa : TD"
bookCollapseSection: true
weight: 2

---

pdf : [pour impression](./hexa_td.pdf)

## Exercice 1

1. Convertir en binaire et en décimal :

    * `0x10`
    * `0xA0`
    * `0xFF`
    * `0xA0 FA`

2. Convertir en hexadécimal :

    * `0b1000 0000`
    * `0b1101 1100`
    * `0b1110 1001`
    * `0b1001 1010`

3. Convertir en hexadécimal :

    * 80
    * 160
    * 128
    * 233

## Exercice 2 : les couleurs

Il existe différentes manières d'encoder les couleurs. 

Voici un exemple qui nous servira de référence :

[color picker](https://imagecolorpicker.com/color-code/bb3344)

Si les couleurs ne sont pas visibles à l'écran, on voit un _rouge un peu rosé_

```python
>>> hex(212)
"0xd4"
```

Dans l'encodage RGB des couleurs on utilise 3 octets pour représenter une couleur.
Elle est généralement donnée en hexadécimal et la notation est :

```
#RRGGBB
```

où `RR` représente les chiffres hexadécimaux représentant le niveau de rouge,
`GG` ceux de vert (_green_) et `BB`... je vous laisse deviner.

Dans l'image on peut voir qu'ils sont traduits en décimal.

Ainsi la couleur `#D43750` est traduite en `rgb(212, 55, 80)`

1. Selon ce modèle, comment obtenir un rouge _pur_ ? Un vert ? un bleu ?

    On donnera les représentations décimales et hexadécimales.
2. Même chose pour le blanc et le noir.

3. Lisons une couleur : traduire en français la couleur : `#ff8800`.
4. Même chose pour la couleur `rgb(0, 255, 170)`.


Cette représentation des couleurs est commode pour afficher à l'écran.

Avec un pixel constitué de LEDs ("rouge", "verte" et "bleue"), on donne
à chaque LED l'intensité correspondant à la valeur et la lumière émise
correspond à la couleur désirée.

Ce modèle ne convient pas pour _imprimer_. En effet, l'écran éteint est _noir_,
alors que la feuille sur laquelle on imprime est _blanche_...

5. Dans une imprimante jet d'encre couleur, quelles sont les couleurs des cartouches ?

6. Pourquoi utiliser aussi une cartouche de _noir_ alors qu'il suffit d'ajouter
  toutes les couleurs précédentes pour en construire ?

6. Donner l'encodage `RGB` des couleurs en question.

Pour imprimer on utilise l'encodage des couleurs `CMYK`.

Il existe d'autres encodages pour les couleurs, qui sont adaptés aux travaux
de graphisme, en particulier HSV : hue (_teinte_), saturation, value qui convient
davantage à la perception humaine des couleurs.

![hsv](./Triangulo_HSV.png)




