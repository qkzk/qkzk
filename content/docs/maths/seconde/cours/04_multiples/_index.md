---
title: "Multiples et diviseurs"
subtitle: Chapitre 4
theme: metropolis
weight: 4
geometry: "margin=1.5cm"
bookCollapseSection: false
header-includes: |
  \usepackage{amsmath,amsfonts,amsthm}
---


--- 

[pdf](./04_multiples.pdf)

---

## 1. Multiples et diviseurs dans $\mathbb{Z}$

### 1.1. Rappels : Ensembles $\mathbb{N}$ et $\mathbb{Z}$

**Définition 1**

- L'ensemble des entiers **naturels** $\\{0, 1, 2, \ldots\\}$ est noté $\mathbb{N}$.
- L'ensemble des entiers **relatifs** $\\{\ldots, -2, -1, 0, 1, 2, \ldots\\}$ est noté $\mathbb{Z}$.



**Propriété 1**

La somme, la différence et le produit de deux entiers relatifs sont des entiers relatifs.



**Propriété 2**

La **division euclidienne** de deux entiers relatifs donne des entiers relatifs :
Pour tout entier $a$ et $b$, avec $b$ non nul, il existe un unique couple d'entiers relatifs $q$ et $r$ tels que :
$$
a = b \times q + r \quad \text{avec} \quad 0 \leq r < |b|
$$
$q$ est appelé **quotient** et $r$ **reste** de la division.


**Exemple 1**

- $37 = 5 \times 7 + 2$. La division euclidienne de $37$ par $5$ a pour quotient $7$ et reste $2$. On a bien $0 \leq 2 < 5$.
- $37 = 5 \times 4 + 17$. $4$ et $17$ ne conviennent pas car $17$ est **plus grand** que $5$.



### 1.2. Multiples et diviseurs dans $\mathbb{Z}$

**Définition 2**

Soient deux entiers relatifs $n$ et $p$. S'il existe un entier $q$ tel que $n = p \times q$, c'est-à-dire si le reste de la division euclidienne de $n$ par $p$ est nul, on dit que :
- $p$ est un **diviseur** de $n$ ou que $n$ est **divisible** par $p$.
- $n$ est un **multiple** de $p$.


**Exemple 2**

$12 = 4 \times 3$ : $12$ est un multiple de $4$, $4$ divise $12$.


**Remarque 1**

- Tout nombre entier relatif non nul a au moins deux diviseurs : $1$ et lui-même.
- Tout nombre entier relatif admet une infinité de multiples. Les multiples de $n$ sont les nombres qui s'écrivent $k \times n$ où $k \in \mathbb{Z}$.


**Propriété 3**

On considère trois entiers relatifs $a$, $n$ et $p$.
Si les entiers $n$ et $p$ sont des multiples de $a$, alors la somme $n + p$, la différence $n - p$ et le produit $n \times p$ le sont aussi.


**Exemple 3**

$36$ et $90$ sont multiples de $9$, donc $126 = 90 + 36$ l'est aussi. En effet, $126 = 9 \times 14$.
Remarquons aussi qu'on a $36 = 9 \times 4$, $90 = 9 \times 10$ et $126 = 9 \times (4 + 10)$.


**Preuve : Pour la somme**

$n$ est multiple de $a$, donc il existe $k \in \mathbb{Z}$ tel que $n = a \times k$.
$p$ est multiple de $a$, donc il existe $l \in \mathbb{Z}$ tel que $p = a \times l$.
On en déduit que :
$$
n + p = a \times k + a \times l = a \times (k + l).
$$
Autrement dit, la somme $n + p$ est multiple de $a$.









## 2. Nombres pairs, nombres impairs

### 2.1. Définitions

**Définition 3 et Propriété**

On considère un entier naturel $n$.
- Si $n$ est divisible par $2$, on dit que $n$ est **pair**.
  Il existe alors un entier $p$ tel que $n = 2 \times p$.
- Sinon, on dit que $n$ est **impair**.
  Il existe alors un entier $p$ tel que $n = 2 \times p + 1$.


**Exemple 4**

$38$ est un nombre pair car $38 = 2 \times 19$.
$17$ est un nombre impair et $17 = 2 \times 8 + 1$.


**Preuve**

On considère un entier naturel $n$. On effectue la division euclidienne de $n$ par $2$.
Il existe donc un entier $p$ (quotient) et un entier $r$ (reste) tels que :
$$
n = 2 \times p + r \quad \text{avec} \quad 0 \leq r < 2.
$$
$r$ est un entier naturel qui vérifie $0 \leq r < 2$, donc $r = 0$ ou $r = 1$.
- Si $r = 0$, alors $n$ est pair et $n = 2 \times p$.
- Sinon, $n$ est impair et $n = 2 \times p + 1$.


**Propriété 4 : Critère de parité**

Un entier naturel $n$ est pair si son chiffre des unités est pair, c'est-à-dire égal à $0$, $2$, $4$, $6$ ou $8$.



### 2.2. Parité et somme d'entiers

**Propriété 5**

- La somme de deux entiers pairs est un entier pair.
- La somme de deux entiers impairs est un entier pair.
- La somme d'un entier pair et d'un entier impair est un entier impair.


**Preuve**

- **Pour deux entiers pairs** :

  Si $n$ et $m$ sont pairs, il existe $p$ et $q$ tels que $n = 2 \times p$ et $m = 2 \times q$.
  On a alors :
  $$
  n + m = 2 \times p + 2 \times q = 2 \times (p + q).
  $$
  Donc $n + m$ est pair.

- **Pour deux entiers impairs** :

  Si $n$ et $m$ sont impairs, il existe $p$ et $q$ tels que $n = 2 \times p + 1$ et $m = 2 \times q + 1$.
  On a alors :
  $$
  n + m = 2 \times p + 1 + 2 \times q + 1 = 2 \times (p + q) + 2 = 2 \times (p + q + 1).
  $$
  Donc $n + m$ est pair.



### 2.3. Parité d'un carré

**Propriété 6**

On considère un entier naturel $n$.
- Si $n$ est pair, alors son carré $n^2$ est pair.
- Si $n$ est impair, alors son carré $n^2$ est impair.


**Exemple 5**

- $12$ est pair et $12^2 = 144$ aussi.
- $9$ est impair et $9^2 = 81$ aussi.


**Preuve**

On considère un entier relatif $n$.

- Si $n$ est pair, alors on peut écrire $n = 2 \times k$ avec $k \in \mathbb{Z}$.
  Donc :
  $$
  n^2 = (2 \times k)^2 = (2k) \times (2k) = 2 \times (2k^2).
  $$
  Donc $n^2$ est pair.

- Si $n$ est impair, alors on peut écrire $n = 2 \times k + 1$ avec $k \in \mathbb{Z}$.
  Donc :
  $$
  n^2 = (2k + 1)^2 = (2k + 1) \times (2k + 1) = (2k)^2 + 2k + 2k + 1 = 2 \times (2k^2 + k + k) + 1.
  $$
  Donc $n^2$ est impair.
  On peut aussi employer l'identité remarquable $(2k + 1)^2 = 4k^2 + 4k + 1$ et obtenir le même résultat.


**Propriété 7**

La réciproque de ce théorème est vraie :
- Si le carré $n^2$ est pair, alors $n$ est pair.
- Si le carré $n^2$ est impair, alors $n$ est impair.
