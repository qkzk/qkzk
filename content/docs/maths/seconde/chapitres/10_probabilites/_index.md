---
title: "Probabilités"
subtitle: Chapitre 10
theme: metropolis
weight: 10
geometry: "margin=1.5cm"
bookCollapseSection: false
header-includes: |
  \usepackage{amsmath,amsfonts,amsthm}
---

 

---

[pdf](./10_probabilites.pdf)

---




## 1. Modélisation d'une expérience aléatoire

On lance un dé cubique et on note le numéro de la face supérieure.

Cette expérience est une **expérience aléatoire** dont les **issues** (ou résultats possibles) sont 1, 2, 3, 4, 5, 6.
L'**ensemble des issues** est $\Omega = \{1, 2, 3, 4, 5, 6\}$.


### 1.1. Définition

**Définition 1**
Définir un modèle de probabilité pour une expérience aléatoire consiste à :

- préciser l'**ensemble des issues** possibles : $\Omega = \{x_1, x_2, \ldots, x_n\}$,
- attribuer à chacune des issues $x_i$ un nombre $p_i$, compris entre 0 et 1, appelé **probabilité** de $x_i$, de sorte que l'on ait $p_1 + p_2 + \ldots + p_n = 1$.

Les probabilités sont des nombres entre 0 et 1 inclus.



### 1.2. Choix d'un modèle

Il y a deux façons de déterminer les probabilités $p_i$ des issues $x_i$ :

#### 1.2.1. Par l'observation statistique des fréquences

Lorsque l'on répète $n$ fois, de façon indépendante, une expérience aléatoire, la **fréquence** $f$ d'une issue a **tendance à se stabiliser**, lorsque $n$ devient grand, autour d'une valeur $p$.
On prend alors cette valeur $p$ comme **probabilité** de l'issue.


**Exemple 1**
Si on lance un dé *« truqué »* : on réalise une étude statistique (en lançant le dé un grand nombre de fois), puis on choisit une distribution de probabilité en accord avec les fréquences observées des issues. Ce peut être, par exemple :




| **Issue**       | 1     | 2     | 3     | 4     | 5   | 6   |
|-----------------|-------|-------|-------|-------|-----|-----|
| **Probabilité** | 0.125 | 0.125 | 0.125 | 0.125 | 0.2 | 0.3 |


#### 1.2.2. Par le choix de l'équiprobabilité

Dans une situation d'**équiprobabilité**, les $n$ issues de l'expérience aléatoire ont la même probabilité de se produire. La probabilité d'une issue est $\dfrac{1}{n}$.

Le choix de ce modèle peut être influencé par certains indices figurant dans la description de l'expérience :

- *« On tire au hasard »*,
- *« Les dés sont supposés équilibrés »*,
- *« Les boules sont indiscernables au toucher »*, etc.


**Exemple 2**
Si on lance un dé cubique équilibré : on attribue à chaque issue la même probabilité $\frac{1}{6}$.


Probabilités pour un dé équilibré


| **Issue**       | 1             | 2             | 3             | 4             | 5             | 6             |
|-----------------|---------------|---------------|---------------|---------------|---------------|---------------|
| **Probabilité** | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ |





## 2. Probabilité d'un événement

### 2.1. Définitions

On lance un dé cubique et l'on considère l'événement $A$ : *« Obtenir au moins 5 »*.

Les issues **favorables à $A$** (qui réalisent $A$) sont 5 et 6 ; on note $A = \{5, 6\}$.

Pour un dé truqué, si $p(5) = 0.2$ et $p(6) = 0.3$, alors $p(A) = 0.2 + 0.3 = 0.5$.

Pour un dé équilibré, $p(5) = p(6) = \frac{1}{6}$. Alors $p(A) = \frac{1}{6} + \frac{1}{6} = \frac{1}{3}$.


### 2.2. Définitions

**Définition 2**
Un **événement** $A$ est un sous-ensemble de $\Omega$ (ensemble des issues).
Sa **probabilité** $p(A)$ est la somme des probabilités des issues favorables à $A$.

- Pour tout événement $A$, $0 \leq p(A) \leq 1$ et $p(\Omega) = 1$ ($\Omega$ est dit **certain**).
- Quand on lance un dé cubique, l'événement $B$ *« obtenir un 7 »* n'a aucune issue favorable. Il est **impossible** et $p(B) = 0$.



### 2.3. Propriété

**Propriété 1**
Dans une situation d'équiprobabilité, la probabilité d'un événement $A$ est :
$$
p(A) = \frac{\text{nombre d'issues favorables à } A}{\text{nombre d'issues possibles}}.
$$





## 3. Opération sur les événements

### 3.1. Définitions

Si $A$ et $B$ sont deux événements :

- $\overline{A}$, événement **contraire** de $A$, est l'ensemble des issues qui ne réalisent pas $A$,
- $A \cap B$ est l'ensemble des issues qui réalisent $A$ et $B$ (les deux à la fois),
- $A \cup B$ est l'ensemble des issues qui réalisent $A$ ou $B$ (au moins l'un des deux).


### 3.2. Exemples

Au lancer d'un dé cubique :

|                                                               |                                 |
|---------------------------------------------------------------|---------------------------------|
| $A$ *« Obtenir un résultat supérieur à 4 »*                   | $A = \{5; 6\}$                  |
| $\overline{A}$ *« Ne pas obtenir un résultat supérieur à 4 »* | $\overline{A} = \{1; 2; 3; 4\}$ |
| $B$ *« Obtenir un résultat pair »*                            | $B = \{2; 4; 6\}$               |
| $A$ et $B$ *« Obtenir un résultat pair et supérieur à 4 »*    | $A \cap B = \{6\}$              |
| $A$ ou $B$ *« Obtenir un résultat pair ou supérieur à 4 »*    | $A \cup B = \{2; 3; 4; 5; 6\}$  |



### 3.3. Propriétés

**Propriété 2**
Soit $A$ et $B$ deux événements :

- $p(\overline{A}) = 1 - p(A)$,
- $p(A \cup B) + p(A \cap B) = p(A) + p(B)$.

Si $A$ et $B$ ne peuvent être réalisés en même temps, $A$ et $B$ sont dits **incompatibles**.
Dans ce cas, $p(A \cap B) = 0$, d'où $p(A \cup B) = p(A) + p(B)$.
