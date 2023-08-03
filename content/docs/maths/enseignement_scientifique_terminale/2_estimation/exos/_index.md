---
title: Exercices Estimation
subtitle: Enseignement Scientifique - Terminale
theme: metropolis
weight: 2
geometry: "margin=1.5cm"
---

[pdf](./exercices_estimation.pdf)

## Exercice 1

Choisir la bonne réponse.

L'intervalle de confiance au niveau de confiance de 95% pour une proportion inconnue d'un caractère présent dans une population à partir d'un échantillon de taille 50 est $[0.07; 0.29]$.

### La fréquence observée du caractère est :

- 7%
- 18%
- 29%

## Exercice 2

L'estimation de la proportion d'un caractère dans une population est-elle plus précise dans un échantillon de 100 individus ou de 1000 individus ?

## Exercice 3

On cherche à estimer la proportion de la lapins touchés par la myxomatose dans un département. 150 lapins sont prélevés : 12 s'avèrent infectés et subiront un traitement ; les 138 autres sont vaccinés puis remis dans leur milieu.

### La taille de l'échantillon étudié est :

- 12
- 138
- 150

### La fréquence de lapins infectés par la myxomatose dans cet échantillon est égale à :

- 8%
- 8.7%
- 92%

### La marge d'erreur étant ici de 4.3%, l'intervalle de confiance au niveau de confiance de 95% est :

- $[0.037; 0.123]$
- $[0.043; 0.086]$
- $[0.907; 0.993]$

## Exercice 4

Pour $f=0.4$ et $n=250$ calculer l'intervalle de confiance au seuil de 95%.

## Exercice 5

On s'intéresse à la proportion d'un cacatère dans une population. Pour ce faire, on prélève un échantillon : si un individu possède ce caractère, alors on note "1" ; sinon on note "0".

Suite à un prélèvement, on a obtenu le résultat suivant :

```
00101010001100111000101101001000100
```

1. Préciser la taille de l'échantillon $n$ et le nombre d'individus $n_E$ possédant le caractère dans cet échantillon. En déduire la fréquence observée $f_{obs}$ du caractère.

2. Calculer la marge d'erreur $\epsilon$ et déterminer l'intervalle de confiance $IC$ au niveau de confiance 95% associé à cet échantillon.

3. Dans des conditions similaires, on a prélevé un autre échantillon dont voici le résultat :

   ```
   11001000000111010011
   00011010011110101000
   01110001000011001000
   00001111100000011100
   10110000001110000001
   00
   ```

   Répondre aux questions 1. et 2. avec cet échantillon.

4. Comparer l'amplitude des deux intervalles de confiance.

## Exercice 6

11% des élèves d'un lycée qui en compte 1600 affirment pratiquer régulièrement un instrument de musique.

Déterminer l'intervalle dans lequel se situe la proportion de pratiquants dans l'ensemble des lycées au seuil des 95%.

## Exercice 7

Un sondage affirme que 55% des personnes intérrogées prévoient partir en vacances au moins deux semaines l'été prochain. Peut-on affirmer, au seuil de 95%, que plus de la moitié des personnes en France est dans ce cas-là si :

1. le sondage porte sur 1030 personnes ?
2. le sondage porte sur 590 personnes ?

## Exercice 8

En France, la proportion de personnes de groupe sanguin $AB$ serait de 10% avec une marge d'erreur de 2.94%.

1. Préciser l'intervalle de confiance au niveau de confiance de 95% pour cette proportion.
2. Quelle était la taille de l'échantillon considéré pour déterminer un tel intervalle de confiance ?

## Exercice 9

1. Justifier que l'amplitude de l'intervalle de confiance $IC$ au niveau de confiance 95% peut s'écrire :

$$3.92\frac{\sqrt{f_{obs}(1-f_{obs})}}{\sqrt{n}}$$

2. À l'aide d'un outil numérique, tracer la courbe représentative de la fonction $t \mapsto \sqrt{t(1-t)}$ sur l'intervalle $[0;1]$.

   Déterminer graphiquement le maximum de cette fonction et la valeur en laquelle il est atteint.

   **Spé maths** Déterminer la dérivée de la fonction étudiée. En déduire ses variations et valider les lectures graphiques.

3. En déduire que l'amplitude de l'$IC$ est majorée par $\frac{1.96}{\sqrt{n}}$.

4. Tracer également la courbe représentative de la fonction $t\mapsto \frac{1.96}{\sqrt{t}}$ sur $]0;1200]$.

   Recopier et compléter les phrases suivantes en justifiant à l'aide du graphique :

   > _"Plus la taille de l'échantillon augmente, plus la marge d'erreur ..."_

   et

   > _"Pour diviser la marge d'erreur par deux, il faudrait multiplier la ... par ..."._

   **Spé maths** justifier les phrases par des arguments algébriques.

## Exercice 10

À la fin des années 1970, une étude anglophone affirmait que les gauchers représentaient environ entre 8% et 15% de la population mondiale.

Quelle était la taille de l'échantillon considéré ?

## Exercice 11

Le coryza du chat est une maladie virale associée à un syndrome respiratoire qui touche principalement les chatons.

Pour estimer la prévalence (proportion de sa présence) dans un département, on a prélevé un échantillon de 145 chatons : 25 s'avèrent porteur de cette maladie.

1. Calculer la fréquence observée de chatons porteurs du coryza dans cet échantillon.
2. Calculer la marge d'erreur et déterminer l'intervalle de confiance au niveau de confiance de 95% pour l'estimation de la proportion de chatons touchés par cette maladie dans ce département.
3. L'amplitude de cet intervalle étant trop importante, il est décidé de prélever un autre échantillon. Quelle devrait être sa taille pour que la marge d'erreur soit proche de 4% ?
