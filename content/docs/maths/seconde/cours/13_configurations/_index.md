---
title: "Configurations du plan"
subtitle: Chapitre 13
theme: metropolis
bookCollapseSection: false
weight: 13
geometry: "margin=1.5cm"
header-includes: |
  \usepackage{amsmath,amsfonts,amsthm,yhmath}
---

 
---

[pdf](./13_configurations.pdf)


---


## 1. Problèmes de longueur et d'angles

### 1.1. Calculer des longueurs

**Propriété 1 : Théorème de Pythagore**
Dans tout triangle $ABC$ rectangle en $A$, on a la relation de Pythagore :
$$
BC^2 = AB^2 + AC^2
$$
Réciproquement, lorsque les côtés d'un triangle vérifient la relation $BC^2 = AB^2 + AC^2$, alors le triangle $ABC$ est rectangle en $A$.


**Remarque 1**
Si $BC^2 \neq AB^2 + AC^2$, alors le triangle n'est pas rectangle en $A$.


**Exemple 1**
Dans le triangle $DEF$ rectangle en $E$ :
$$
\begin{array}{lrl}
                & DF^2 &= ED^2 + EF^2 \\
\Leftrightarrow & 5^2 &= 4^2 + EF^2 \\
\Leftrightarrow & 25 &= 16 + EF^2 \\
\Leftrightarrow & EF^2 &= 25 - 16 \\
\Leftrightarrow & EF^2 &= 9 \\
\Leftrightarrow & EF &= \sqrt{9} = 3
\end{array}
$$

![Triangle rectangle DEF](fig0.svg)

**Propriété 2 : Théorème de Thalès**


On considère l'une des configurations ci-dessous, dite de Thalès.


Si les droites $(AB)$ et $(CD)$ sont parallèles, alors les longueurs des triangles $SAB$ et $SDC$ sont proportionnelles
et on a $\dfrac{SA}{SC} = \dfrac{SB}{SD} =\dfrac{AB}{CD}.$ 


Réciproquement, si les côtés des triangles $SAB$ et $SDC$ sont proportionnels, alors les droites $(AB)$ et $(CD)$ sont parallèles.

 $~$![Configuration 1](fig2_.svg)![Configuration 2](fig3.svg)

### 1.2. Calculer des angles

**Propriété 3 : Relations trigonométriques**
Dans un triangle $ABC$ rectangle en $A$, les côtés et les angles sont liés par des **relations trigonométriques** :
$$
\cos \widehat{B} = \dfrac{AB}{BC} \quad ; \quad \sin \widehat{B} = \dfrac{AC}{BC} \quad ; \quad \tan \widehat{B} = \dfrac{AC}{AB}
$$

![Triangle rectangle avec angles](fig4.svg)


**Exemple 2**
Dans le triangle $DEF$ rectangle en $E$ :
$$
\begin{array}{rl}
\cos \widehat{D} &= \dfrac{ED}{FD} \\
\cos \widehat{D} &= \dfrac{4}{5} \\
\widehat{D} &= \cos^{-1} \left( \dfrac{4}{5} \right) \approx 36.9^\circ
\end{array}
$$

![Triangle rectangle DEF](fig01.svg)


**Remarque 2**
La trigonométrie permet de calculer des longueurs ou des angles.


**Propriété 4**
Pour tout angle aigu $\alpha$ d'un triangle rectangle, on a la relation trigonométrique suivante :
$$
\cos^2 \alpha + \sin^2 \alpha = 1
$$


**Propriété 5**
Dans un triangle, la somme des angles fait $180^\circ$.


**Propriété 6**
Deux droites parallèles et une sécante engendrent des angles alternes-internes et correspondants, de même mesure.

![Alternes-internes et correspondants](./fig5.png)




## 2. Configurations du plan

### 2.1. Quadrilatères particuliers



|                                                  | Les côtés                                                                            | Les diagonales                                       | Les symétries                                                                          |
|--------------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Parallélogramme** ![Parallélogramme](fig6.png) | $(AB) \parallel (DC)$ et $(AD) \parallel (BC)$ ou $(AB) \parallel (DC)$ et $AB = DC$ | Les diagonales $[AC]$ et $[BD]$ ont même milieu $O$. | $O$ est le centre de symétrie                                                          |
| **Rectangle** ![Rectangle](fig7.png)             | C'est un parallélogramme et $(AB) \perp (AC)$                                        | $AC = BD$                                            | Les médiatrices de $[AD]$ et de $[AB]$ sont des axes de symétrie                       |
| **Losange** ![Losange](fig8.png)                 | C'est un parallélogramme et $AB = AD$                                                | $(AC) \perp (BD)$                                    | Les diagonales sont des axes de symétrie                                               |
| **Carré** ![Carré](fig9.png)                     | C'est un parallélogramme et $(AB) \perp (AD)$, $AB = AD$                             | $(AC) \perp (BD)$, $AC = BD$                         | Les médiatrices de $[AD]$ et $[AB]$ ainsi que les diagonales sont des axes de symétrie |


**Exemple 3**

![Rectangle 2](fig10.png)

Le quadrilatère $ABCD$ est un parallélogramme car ses diagonales $[AC]$ et $[BD]$ se coupent en leur milieu. Ses diagonales ont la même longueur, donc c'est un rectangle.


**Remarque 3**
Un carré est à la fois un rectangle et un losange.



### 2.2. Cercles et angles

**Définition 1**
$O$ est un point et $r$ est un nombre réel strictement positif.
L'ensemble des points $M$ du plan vérifiant $OM = r$ est le cercle de centre $O$ et de rayon $r$.

**Vocabulaire** :

- $[OA]$ est un rayon,
- $[BB']$ est un diamètre,
- $\widehat{BB'A}$ est un angle inscrit,
- $\widehat{BOA}$ est un angle au centre,
- $[AB]$ est une corde,

![Cercle avec arc et corde](fig11.png)


**Propriété 7**
Lorsqu'un angle inscrit $\alpha$ intercepte le même arc qu'un angle au centre $\beta$, alors :
$$
\beta = 2\alpha
$$

![Angle au centre et angle inscrit](fig12.png)


**Exemple 4**
![Exemple angle au centre et angle inscrit](fig14.png)

Puisque l'angle au centre $\widehat{BOC}$ intercepte le même arc $\wideparen{CB}$ que l'angle inscrit $\widehat{BDC}$, alors :
$$
\widehat{BDC} = \dfrac{1}{2} \widehat{BOC} = 25^\circ
$$


**Définition 2**
La tangente à un cercle $\mathcal{C}$ de centre $O$ en un point $M$ est la droite passant par $M$ et perpendiculaire au rayon $[OM]$.
Elle coupe le cercle $\mathcal{C}$ en l'unique point $M$.

![Tangente au cercle](fig15.png)





## 3. Droites remarquables du triangle

### 3.1. Médiatrices

**Définition 3**
La médiatrice d'un segment est l'ensemble des points du plan équidistants des extrémités de ce segment.


**Propriété 8**
C'est la droite passant par le milieu et perpendiculaire à ce segment.


**Propriété 9**
Les trois médiatrices d'un triangle sont concourantes en un point $O$ appelé *centre du cercle circonscrit au triangle*.


**Exemple 5**
![Médiatrices](fig16.png)


**Remarque 4**
Lorsque le triangle est rectangle, le centre du cercle circonscrit est le milieu de l'hypoténuse.



### 3.2. Autres droites remarquables du triangle

**Définition 4**
- Une **hauteur** est une droite passant par un sommet du triangle et perpendiculaire au côté opposé à ce sommet.
- Une **médiane** est une droite passant par un sommet du triangle et le milieu du côté opposé à ce sommet.
- La **bissectrice** d'un angle est la demi-droite passant par un sommet de cet angle et qui le coupe en deux angles égaux.

![Hauteur](fig17.png)
![Médiane](fig18.png)
![Bissectrice](fig19.png)


**Propriété 10**
Dans un triangle :
- les trois hauteurs sont concourantes en un point appelé *orthocentre du triangle*,
- les trois médianes sont concourantes en un point appelé *centre de gravité du triangle*,
- les trois bissectrices sont concourantes en un point appelé *centre du cercle inscrit au triangle*.


**Propriété 11**
Dans $ABC$ isocèle en $A$, la médiane et la hauteur issue de $A$, la bissectrice de $\hat{A}$ et la médiatrice de $[BC]$ sont confondues.





## 4. Projeté orthogonal d'un point sur une droite

Soit $D$ une droite du plan et $A$ un point.

**Définition 5**
On appelle **projeté orthogonal** de $A$ sur $D$ le point d'intersection de la droite $D$ avec la perpendiculaire à $D$ passant par $A$.


**Exemple 6**
$H$ est le projeté orthogonal de $A$ sur $D$.

![Projeté orthogonal](fig20.png)


**Propriété 12**
La distance du point $A$ à la droite $D$ est la plus petite distance séparant un point de $D$ avec $A$.
Elle est égale à $AH$, où $H$ est le projeté orthogonal du point $A$ sur $D$.


**Preuve**
Notons $d$ la distance entre $A$ et $D$. Soit $M$ un point de $D$, distinct de $H$.
Le triangle $AHM$ est rectangle en $H$.
Grâce au théorème de Pythagore, on peut affirmer que l'hypoténuse $[AM]$ est le plus grand des côtés du triangle $AHM$. Donc $AM > AH$.
Ainsi, la plus petite distance séparant $A$ d'un point de $D$ est égale à $AH$.
On en déduit que $AH = d$.
