---
title: "Décimaux"
subtitle: Chapitre 11
theme: metropolis
weight: 11
geometry: "margin=1.5cm"
bookCollapseSection: false
header-includes: |
  \usepackage{amsmath,amsfonts,amsthm}
---

 
---

[pdf](./11_decimaux.pdf)

---


## 1. Les décimaux

### 1.1. Définition

**Définition 1**
L'ensemble des nombres décimaux est noté $\mathbb{D}$. $\mathbb{D}$ est l'ensemble des nombres qui peuvent s'écrire sous la forme d'une fraction dont le numérateur est un entier et le dénominateur est une puissance de 10. C'est ce qu'on appelle une **fraction décimale**.

Un nombre décimal est un nombre qui peut s'écrire sous la forme $\frac{a}{10^n}$ avec $a \in \mathbb{Z}$ et $n \in \mathbb{N}$.


**Remarque 1**
Tout nombre décimal peut donc s'écrire comme la fraction de deux entiers, et donc c'est un rationnel.
Ainsi, par définition $\mathbb{D} \subset \mathbb{Q}$ ($\mathbb{D}$ est **inclus** dans $\mathbb{Q}$).


**Exemple 1**
$\frac{1}{4}$ est un décimal, en effet $\frac{1}{4} = 0.25 = \frac{25}{100} = \frac{25}{10^2}$.



### 1.2. Propriétés

**Propriété 1**
Toute fraction réduite d'entiers (= nombre rationnel) dont le dénominateur se factorise en produit de 2 ou 5 exclusivement est un décimal.


**Exemple 2**
$\dfrac{33}{40} = \dfrac{33}{2^3 \times 5} = \dfrac{33 \times 5^2}{2^3 \times 5^3} = \dfrac{33 \times 25}{(2 \times 5)^3} = \dfrac{825}{10^3}$, c'est bien un décimal.


**Propriété 2**
Toute fraction réduite d'entiers dont la décomposition en facteurs premiers du dénominateur comporte d'autres facteurs que 2 ou 5 n'est pas un décimal.


**Exemple 3**
$\frac{1}{3}$ n'est pas un décimal.

**Démonstration** :
Nous allons raisonner par l'absurde[^1].

Supposons donc que $\frac{1}{3}$ est un décimal.
D'après la définition, cela signifie qu'il existe deux nombres $a \in \mathbb{Z}$ et $n \in \mathbb{N}$ tels que $\frac{1}{3} = \frac{a}{10^n}$.

$$
\frac{1}{3} = \frac{a}{10^n} \Longleftrightarrow \frac{10^n}{3} = a
$$

Or $a \in \mathbb{Z}$, donc $10^n$ est divisible par 3.
Or, la somme des chiffres d'un nombre divisible par 3 est elle-même divisible par 3.
Cependant, les chiffres de $10^n$ avec $n \in \mathbb{N}$ sont un *« 1 »* et $n$ *« 0 »*.
Donc la somme des chiffres de $10^n$ est 1.
Mais $1$ n'est pas divisible par $3$. Contradiction !

Ainsi, la supposition initiale *« $\frac{1}{3}$ est un décimal »* est fausse.

**Conclusion** : Nous avons démontré que $\frac{1}{3}$ n'est pas un décimal.


**Propriété 3**
Tout nombre décimal admet un développement décimal fini. Réciproquement, tout nombre admettant un développement décimal fini est un nombre décimal.


**Exemple 4**
$0.987654321 = \frac{987654321}{10^9}$ est un décimal.


**Exemple 5**
$0.876\overline{543} = 0.876543543543543\ldots$ n'est pas un décimal.


**Remarque 2**
On verra (peut-être) que tout nombre décimal admet *deux* écritures décimales, dont une infinie.
Par exemple, $0.\overline{9} = 0.99999\ldots = 1$, et 1 est bien un décimal.

[^1]: Raisonnement par l'absurde : supposer le contraire de ce qu'on souhaite prouver, réaliser des implications depuis ce postulat, arriver à une contradiction. Cela démontre que la supposition initiale était fausse.
