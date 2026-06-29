---
title: Les nombres réels
subtitle: Chapitre 1
theme: metropolis
weight: 1
geometry: "margin=1.5cm"
bookCollapseSection: false
header-includes: |
  \usepackage{amsmath,amsfonts,amsthm}
---



---

[pdf](./01_reels.pdf)

---


## 1. Les ensembles de nombres

### Propriété 1 *(Admise)*
On peut associer à tout point $M$ d'une droite graduée $\mathcal{D}$ un nombre appelé *abscisse* de $M$.



### Définition 1
L'ensemble des abscisses des points de $\mathcal{D}$ est appelé *ensemble des réels*. Il est noté $\mathbb{R}$.



### Exemple 1
L'abscisse du point $O$ est $0$, celle de $I$ est $1$, celle de $A$ est $-\frac{7}{3}$ et celle de $P$ est $\pi$.


![axe réel](./fig1_axe_reel.png)



### Définition 2
Durant les années antérieures, on a construit différents ensembles de nombres *imbriqués*. $\mathbb{R}$ les contient tous.




| **Ensemble de nombres** | **Notation** | **Éléments et exemples**                                                                         |
|-------------------------|--------------|--------------------------------------------------------------------------------------------------|
| Entiers naturels        | $\mathbb{N}$ | $0 \\;;\\; 1 \\;;\\; 3$ etc.                                                                         |
| Entiers relatifs        | $\mathbb{Z}$ | $-10 \\;;\\; -5 \\;;\\; -1 \\;;\\; 0 \\;;\\; 1 \\;;\\; 2 \\;;\\; 3$                                          |
| Décimaux                | $\mathbb{D}$ | $-1/2 \\;;\\; 0.5 \\;;\\; 12,345 \\;;\\; 1$                                                            |
| Rationnels              | $\mathbb{Q}$ | $\dfrac{1}{3} \\;;\\; -\dfrac{2}{7}$|
| Réels                   | $\mathbb{R}$ | $\pi \\;;\\; \sqrt{2} \\;;\\; \frac{1}{3}$                                                           |



### Propriété 2
Les ensembles de nombres sont contenus les uns dans les autres :
$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{D} \subset \mathbb{Q} \subset \mathbb{R}
$$

![ensembles imbriqués](./ensemble-nombre-operation.png)


### Propriété 3
Les nombres rationnels de l'ensemble $\mathbb{Q}$ peuvent s'écrire $\frac{p}{q}$ avec $p \in \mathbb{Z}$ et $q \in \mathbb{Z}, q \neq 0$.
Ils admettent une *écriture décimale* qui se termine ou qui se répète.





### Exemple 2 *(Nombres rationnels)*
$\frac{1}{3} = 0,3333\underline{3} \qquad \frac{1}{10} = 0,1 \qquad \frac{324}{11} = 29,45\underline{45}$
On souligne les chiffres qui se répètent.



### Remarque 1
Les décimaux, dont l'ensemble est noté $\mathbb{D}$, sont les nombres qui admettent une écriture décimale *qui se termine* comme $\frac{246}{128} = 1,921875$.



### Méthode 1
**Démontrer qu'un nombre n'est pas un décimal.**



### Méthode 2
**Démontrer qu'un nombre n'est pas un rationnel.**



### Remarque 2
L'un des objectifs de cette année est de répondre à la question générale : ce nombre $x$ est-il dans cet ensemble $E$ ?





## 2. Intervalles


### Définition 3
Soient $a$ et $b$ deux réels.
L'ensemble des réels $x$ tels que $a \leq x \leq b$ est noté $[a~;~b]$.
C'est l'intervalle des nombres compris entre $a$ et $b$, bornes incluses.

![Intervalle](./intervalle_ferme.svg)


Il existe plusieurs sortes d'intervalles, selon leurs bornes :




| Intervalle      | Inéquation        | Représentation graphique              |
|-----------------|-------------------|---------------------------------------|
| $[a ; b]$       | $a \leq x \leq b$ | ![Intervalle](./intervalle_ferme.svg) |
| $[a ; b[$       | $a \leq x < b$    | ![Intervalle](./intervalle_2.svg)     |
| $]a ; b]$       | $a < x \leq b$    | ![Intervalle](./intervalle_3.svg)     |
| $]a ; b[$       | $a < x < b$       | ![Intervalle](./intervalle_4.svg)     |
| $[a ; +\infty[$ | $a \leq x$        | ![Intervalle](./intervalle_5.svg)     |
| $]a ; +\infty[$ | $x > a$           | ![Intervalle](./intervalle_6.svg)     |
| $]-\infty ; b[$ | $x < b$           | ![Intervalle](./intervalle_7.svg)     |
| $]-\infty ; b]$ | $x \leq b$        | ![Intervalle](./intervalle_8.svg)     |

Le symbole $\infty$ se lit *« infini »*. Ce n'est pas un nombre réel.
Du côté de l'infini, le crochet est toujours tourné vers l'extérieur : $]-\infty;3]$ ou $]4;+\infty[$.



### Méthode 3
**Représenter un intervalle sur une droite graduée**



### Définition 4
Soient $I$ et $J$ deux intervalles.
1. L'ensemble des réels qui appartiennent à la fois à $I$ et à $J$ est appelé **l'intersection** de $I$ et $J$.
   Cet ensemble est noté $I \cap J$.
2. L'ensemble des réels qui appartiennent à $I$ ou à $J$ est appelé **la réunion** de $I$ et $J$.
   Cet ensemble est noté $I \cup J$.



### Exemple 3 *(Intersections et réunions d'intervalles)*
1. $[4;5] \cap [2;3] = \emptyset$
2. $[2;5] \cap [2;3] = [2;3]$
3. $[4;7] \cap [6;8] = [6;7]$
4. $[4;7] \cup [6;8] = [4;8]$



### Méthode 4
**Déterminer l'intersection, la réunion de deux intervalles**



### Propriété 4 *(Résolution d'équations affines)*
On considère une *expression affine* : $ax + b$ où $a$ et $b$ sont deux nombres réels **avec $a \neq 0$**.
L'*équation* $ax + b = 0$ admet pour unique *solution* $x = -\frac{b}{a}$.



### Méthode 5 *(Résolution d'inéquations affines)*
Toutes les inéquations affines se résolvent de la même manière, en remplaçant *l'inégalité* par le symbole correspondant.

Résolvons $ax + b > 0$ :
$$ax + b > 0 \Leftrightarrow ax > -b \qquad (I)$$

- Si $a > 0$, $(I) \Leftrightarrow x > -\frac{b}{a}$.
  Les solutions sont $\left]-\frac{b}{a}; +\infty\right[$.
- Si $a < 0$, $(I) \Leftrightarrow x < -\frac{b}{a}$.
  Les solutions sont $\left]-\infty; -\frac{b}{a}\right[$.



### Propriété 5 *(Signe d'une expression affine : le tableau de signes)*

On peut résumer toutes les solutions d'inéquations affines dans un _tableau de signe_ :

Si $a<0$
$$
\begin{array}{|c|ccccc|}
\hline
x & -\infty & & -\frac{b}{a} & & +\infty \\\ \hline
ax+b & & + & 0 & - & \\\ \hline
\end{array}
$$
_Lecture du tableau_ : Le symbole $+$  signifie que si $x < -\frac{b}{a}$ alors $ax + b > 0$.

Si $a>0$

$$
\begin{array}{|c|ccccc|}
\hline
x & -\infty & & -\frac{b}{a} & & +\infty \\\ \hline
ax+b & & - & 0 & + & \\\ \hline
\end{array}
$$




### Méthode 6
**Résoudre une inéquation**





## 3. Encadrer un réel par deux nombres


### Définition 5
On dit que les nombres réels $a$ et $b$ *encadrent* le nombre réel $x$ si :
$$a < x < b$$
$b - a$ est *l'amplitude* de cet encadrement.



### Théorème *(Admis)*
Tout nombre réel $x$ peut être encadré par deux nombres décimaux avec une amplitude choisie.



### Exemple 4
- $1,2 < \sqrt{2} < 2$ est un encadrement de $\sqrt{2}$ d'amplitude $0,8$.
- $1,4 < \sqrt{2} < 1,5$, encadrement d'amplitude $0,1$ (au dixième).
- $1,41 < \sqrt{2} < 1,42$, encadrement d'amplitude $0,01$ (au centième).


**Vocabulaire :**
- $1,41$ est une *valeur approchée par défaut*,
- $\sqrt{2}$ est la *valeur exacte*,
- $1,42$ est une *valeur approchée par excès*.



### Méthode 7
**Trouver des valeurs approchées d'un nombre réel.**





## 4. Valeur absolue d'un nombre réel


### Définition 6
On appelle *valeur absolue* d'un nombre réel $a$, le nombre noté $|a|$ et défini par :
$$
|a|=
\begin{cases}
a & \text{si } a \geq 0, \\
-a & \text{si } a < 0.
\end{cases}
$$



### Exemple 5
$|3| = 3$ car $3 > 0$, $|-2| = -(-2) = 2$ car $-2 < 0$.



### Propriété 5 *(Admise)*
- Pour tout nombre réel $a$, $|a| \geq 0$,
- $a$ et $-a$ ont la même valeur absolue,
- $|a - b| = |b - a|$ ; $|a \times b| = |a| \times |b|$ et $|a + b| \leq |a| + |b|$.



### Définition 7 *(Distance entre deux nombres réels)*
La *distance* entre les réels $a$ et $b$ est $|b - a|$.
C'est ce qu'on appelle souvent *l'écart* entre ces nombres.



### Exemple 6
La distance entre $3,5$ et $10$ est $|10 - 3,5| = |6,5| = 6,5$.



### Remarque 3
On réalise **d'abord** les additions et soustractions dans les valeurs absolues avant d'essayer de les enlever.



### Méthode 8
**Résoudre des inéquations et des équations comportant des valeurs absolues.**


