---
title: "Chapitre 10 : Probablités"
subtitle: Mathématiques - Exercices
theme: metropolis
weight: 10
bookCollapseSection: false
geometry: "margin=1.5cm"
---

[pdf](./ch10.pdf)

## I. Modélisation d'une expérience aléatoire

#### Exercice 1

On Lance deux dés à six faces et on note la somme obtenue. Modélisez cette expérience aléatoire en énumérant l'ensemble des issues possibles.

#### Exercice 2

Une urne contient 3 boules rouges, 2 boules bleues et 5 boules vertes.

1. Modélisez cette expérience aléatoire en énumérant l'ensemble des issues possibles lors du tirage d'une boule.
2. Quelle est la probabilité d'obtenir une boule en particulier ?
3. Calculer la probabilité d'obtenir une boule rouge.

#### Exercice 3

On Lance une pièce deux fois.

1. Modélisez cette expérience aléatoire en énumérant l'ensemble des issues possibles.
2. On suppose la pièce équilibrée. Quelle est la probabilité d'obtenir deux fois "face" ?

## II. Probabilité d'un événement

_Pour chaque exercice de cette partie, on décrira l'**univers** et l'**évenement** considéré._

#### Exercice 4

Dans un jeu de cartes classique à 32 cartes, quelle est la probabilité de tirer un as ?

#### Exercice 5

Un sac contient 4 boules rouges, 3 boules vertes et 3 boules jaunes. Quelle est la probabilité de tirer une boule verte ?

#### Exercice 6

Lors du lancer d'un dé à six faces, quelle est la probabilité d'obtenir un nombre pair ?

#### Exercice 7

Lors d'un tirage au sort un élève d'une classe en comportant 32 dont 14 filles. Quelle est la probabilité de choisir une fille ?

## III. Équiprobabilité

#### Exercice 8

Expliquez le concept d'équiprobabilité dans le cadre du lancer d'une pièce de monnaie.

#### Exercice 9

On lance un dé à six faces. Est-ce toujours une expérience équiprobable ? Quelle hypothèse supplémentaire est nécessaire ?

#### Exercice 10

Une urne contient 3 boules rouges et 2 boules bleues dont on tire une boule au hasard. On considère deux modèles :

- **Modèle 1 :** $\Omega = \{R, B\}$
- **Modèle 2 :** $\Omega = \{R_1, R_2, R_3, B_1, B_2\}$

1. Lequel de ces modèle présente une situation d'équiprobabilité ?
2. Jonas affirme : "J'utilise le premier modèle. Il y a deux issues donc la probabilité d'obtenir une boule rouge est 0.5". Qu'en pensez-vous ?

## IV. Opérations sur les événements

_Dans cette série d'exercice, on décrira l'**univers** et **les** événements décrits. Celui sur lequel porte la question sera traduit en terme d'union, d'intersection ou de complémentaires d'événéments._

#### Exercice 11

Dans un jeu de cartes à 32 cartes, quelle est la probabilité de tirer une carte qui est un roi ou un cœur ?

#### Exercice 12

Lors du lancer d'un dé à six faces, quelle est la probabilité d'obtenir un 2 ou un nombre pair ?

#### Exercice 13

Trouvez la probabilité de l'événement complémentaire de "obtenir un nombre inférieur ou égal à 4" lors du lancer d'un dé à six faces.

#### Exercice 14

On lance un dé équilibré à 20 faces (NB. Cela existe). Quelle est la probabilité d'obtenir un nombre plus grand que 12 et impair ?

## V. Lois de probabilité

#### Exercice 15

Soit la loi de probabilité suivante pour une variable aléatoire $X$ :

| $X$    | 1   | 2   | 3   | 4   |
| ------ | --- | --- | --- | --- |
| $P(X)$ | 0.2 | 0.3 | 0.4 | 0.1 |

1. Cette situation est-elle équiprobable ? Justifier.
2. Calculez $P(X \leq 2)$.

#### Exercice 16

Une urne contient 2 boules rouges, 3 boules vertes et 5 boules jaunes. Décrivez la loi de probabilité associée à la _couleur_ d'une boule tirée au hasard.

#### Exercice 17

Soit une variable aléatoire $Y$ avec la loi de probabilité suivante :

| $Y$    | 0   | 1   | 2   | 3   |
| ------ | --- | --- | --- | --- |
| $P(Y)$ | 0.2 | 0.4 | 0.2 | 0.2 |

1. Calculer $P(Y > 1)$.
2. Calculer $P(Y \neq 1)$.

## VI. Arbres de probabilité

#### Exercice 18

1. Représenter par un arbre de probabilité le lancer consécutif de trois pièces équilibrées.
2. Calculer la probabilité d'obtenir trois faces.
3. Calculer la probabilité d'obtenir une face (et donc deux piles).

_Dans les deux exercices suivants, dessiner l'arbre où on distingue chaque boule est fastidieux. Il est préférable de regrouper les couleurs et de dénombrer les boules restantes après le premier tirage._

#### Exercice 19

Un sac contient 5 boules blanches et 3 boules noires. Deux boules sont tirées _avec remise_. Dessinez l'arbre de probabilité et calculez la probabilité de tirer une boule blanche suivie d'une boule noire.

#### Exercice 20

Dans une urne, il y a 4 boules rouges et 6 boules bleues. Si deux boules sont tirées _sans remise_, dessinez l'arbre de probabilité et calculez la probabilité de tirer deux boules rouges.

## VII. Exercices bilan 

#### Exercice 21 - roulette française simple


Un joueur affronte le casino dans le jeu de la roulette. Voici les étapes simplifiée du jeu :

- Le joueur choisit parmi 37 cases, de 0 à 36 et y place sa mise. 
- Le croupier fait tourner une roue et y lance une bille. La roue finit par s'arrêter et la bille se stabilise dans une case numérotée. Toutes les cases ont la même taille.
- Deux cas se présentent : la bille a terminé sa course dans la case choisie par le joueur ou non.
- Si le joueur a choisi la bonne case, il récupère 36 fois sa mise.
- Sinon, il perd sa mise.

1. Quelle est la probabilité de gagner ?
2. Si le joueur a mise 1€, combien peut-il espérer gagner en moyenne s'il répète un grand nombre de partie ?

#### Exercice 22 - roulette suite.

On suppose maintenant qu'il est possible de réaliser différentes mises. Par exemple, le joueur peut choisir une _couleur_ rouge ou noir.

- Les cases de 1 à 36 sont noires ou rouges selon leur parité (impair : rouge, paire : noir)
- La case 0 est verte.

Dans cette situation, le joueur récupère 2 fois sa mise.

1. Quelle est la probabilité de gagner ?
2. Si le joueur a mise 1€, combien peut-il espérer gagner en moyenne s'il répète un grand nombre de partie ?

_Bilan :_ d'autres mises plus élaborées sont possibles mais toutes ont le même résultat, lorsqu'on répète un grand nombre de parties, le jeu favorise _toujours_ le casino.

C'est aussi le cas des jeux à gratter (buraliste) ou des paris sportifs : ils sont toujours favorables à l'organisateur (FDJ, site de pari) et jamais au joueur. 

Ainsi, il n'existe aucune raison objective de joueur aux jeux d'argent.

#### Exercie 23


Deux joueurs, Alfred et Béatrice s'affrontent à un jeu d'argent.

Alfred mise 1€. Il tire ensuite une boule dans une urne et gagne ou perd selon la couleur.

Dans l'urne, il y a 10 boules rouges (qui font perdre), deux boules vertes (qui rapporte 3 fois la mise) et une boule bleue (qui rapporte 6 fois la mise).

L'objectif est d'ajuster un nombre de boules rouges afin de rendre le jeu équitable.

1. Donner la loi de probabilité du gain dans la situation d'Alfred.
2. Calculer l'espérance du gain (= la moyenne pondérée des gains).
3. (_Difficile_) Reprendre les calculs avec $x$ boules rouges et déterminer le nombre de boules rouges qui rendent l'espérance nulle.

#### Exercice 24

On lance trois fois une pièce équilibrée et on ajoute les valeurs suivantes (pile : 0, face : 1).

1. Quelles sont les valeurs possibles ?
2. Construire un arbre probabilisé représentant la situation.
3. Démontrer que la loi n'est pas équiprobable.
4. Construire la loi de probabilité du jeu.
5. Quelle est l'espérance de ce jeu ?



