---
author: qu3nt1n
date: 2016-07-01 22:54:37+00:00
draft: false
title: 3.1 Représentation binaire
weight: 1

---






Notions abordées



* représentations : binaire, octal, hexadécimal
* calcul booléen









# Représentation binaire




Habituellement, nous représentons les valeurs entières dans le système décimal, on dit aussi en base 10. Nous utilisons les dix chiffres de 0 à 9. La position des chiffres définit la valeur associée à ce chiffre. Par exemple, 542 est compris comme

542 = 5 x 100 + 4 x 10 + 2

Les différents chiffres correspondent aux puissances successives de 10 :


542 = 5 × 102 + 4 × 101 + 2 × 100


L'information numérique, qu'il s'agisse de valeurs entières, de textes, d'images, ou de sons est en fin de compte représentée par des suites de 0 et de 1. On parle de bit : un bit peut prendre deux valeurs, 0 ou 1.


D'où vient le mot _bit_ ?





Le système binaire permet d'écrire les valeurs entières en n'utilisant que ces les deux chiffres 0 et 1. On utilise alors la base 2.

De même que pour la base 10, les positions des chiffres sont associées aux puissances successives de 2


20 = 1 ;  21 = 2 ;  22 = 4 ;  23 = 8 ;  24 = 16 ;  25 = 32 ;  26 = 64 ; _etc_.


Ainsi la valeur entière qui correspond à la représentation binaire 101010 est


1 × 25 + 0 × 24 + 1 × 23 +  0 × 22 + 1 × 21 + 0 × 20
= 1 × 32 + 0 × 16 + 1 × 8 + 0 × 4 + 1 × 2 + 0 × 1
= 42


Il nous faut pouvoir indiquer que 101010 est une représentation binaire et non une représentation décimale, qui serait comprise _cent un mille dix_ (ou encore une représentation dans une autre
base...).

On notera par exemple 0b101010 ou 1010102.

On distingue donc les **valeurs entières** (les entiers) et leur représentation.






* On utilise habituellement la **représentation décimale**.
* D'autres représentations sont possibles. En particulier, dans le monde du numérique, la **représentation binaire** est souvent utilisée.

À une valeur entière donnée est associée une représentation décimale, mais aussi une représentation binaire.











Expliquez ce que peut signifier le signe '=' dans l'équation suivante


10 = 2 que l'on préférera écrire 0b10 = 2












Donnez les valeurs entières représentées par 0b0100, 0b10101, 0b101, 0b0101 et 0b00101.

Comparez les valeurs entières représentées par 0b11 et 0b100, 0b111 et 0b1000.









Quelle est la représentation binaire de 14 et 78 ?







De manière générale, quelle méthode employer pour trouver la représentation binaire d'une valeur entière ?













#### LA suite de ce TP n'est plus au programme de l'ISN. Elle est laissée pour le lecteur curieux désirant approfondir ce sujet.











# Octets et Représentation hexadécimale




5 ans après la rédaction de ce cours je n'ai toujours pas le courage de terminer cette partie. Aussi...
La version ["simple"](http://cours-informatique-gratuit.fr/cours/octets-et-grandeurs-informatique/) avec des couleurs.
La version ["compliquée"](http://robert.cireddu.free.fr/SI/Cours%20sur%20la%20numeration-codage.pdf) avec des calculs.

A lire seulement, rassurez-vous.

(c'est tellement compliqué qu'on a longtemps enseigné les changements de base de nombre à l'école primaire...)





# Supplément : Calcul booléen





Le terme _booléen_ vient du nom du mathématicien britannique [George
Boole](http://fr.wikipedia.org/wiki/George_Boole). Il est le créateur de la logique moderne qui s'appuie sur l'algèbre qui porte désormais son nom : l'_algèbre de Boole_. Un booléen est une donnée dont la valeur ne peut prendre que deux états, soit l'état _vrai_ soit à l'état _faux_. On utilise également le bit pour représenter des booléens : ainsi un 0 représente la valeur _faux_ et un 1 représente la valeur _vrai_.




## Opérateurs booléens


On définit sur ces valeurs booléennes trois opérations : la négation, la conjonction et
la disjonction, également appelées le NON, le ET et le OU logiques.


### Le NON logique


Le NON logique d'un booléen _a_ se définit par :



<table class="verite droite" >
<tbody >
<tr >
a
NON a
</tr>
<tr >

<td >0
</td>

<td >1
</td>
</tr>
<tr >

<td >1
</td>

<td >0
</td>
</tr>
</tbody>
</table>
NON _a_ vaut VRAI si et seulement si _a_ vaut FAUX.

Cet opérateur peut également être défini par sa table de vérité présentée ci-contre.






### Le ET logique


Le ET logique entre deux booléens _a_ et _b_ se définit par :



<table class="verite droite" >
<tbody >
<tr >
a
b
a ET b
</tr>
<tr >

<td >0
</td>

<td >0
</td>

<td >0
</td>
</tr>
<tr >

<td >0
</td>

<td >1
</td>

<td >0
</td>
</tr>
<tr >

<td >1
</td>

<td >0
</td>

<td >0
</td>
</tr>
<tr >

<td >1
</td>

<td >1
</td>

<td >1
</td>
</tr>
</tbody>
</table>
_a_ ET _b_ vaut VRAI si et seulement si _a_ vaut VRAI et _b_ vaut VRAI

Cet opérateur peut également être défini par sa table de vérité présentée ci-contre.






### Le OU logique


Le OU logique entre deux booléens _a_ et _b_ se définit par :



<table class="verite droite" >
<tbody >
<tr >
a
b
a OU b
</tr>
<tr >

<td >0
</td>

<td >0
</td>

<td >0
</td>
</tr>
<tr >

<td >0
</td>

<td >1
</td>

<td >1
</td>
</tr>
<tr >

<td >1
</td>

<td >0
</td>

<td >1
</td>
</tr>
<tr >

<td >1
</td>

<td >1
</td>

<td >1
</td>
</tr>
</tbody>
</table>
_a_ OU _b_ vaut VRAI si et seulement si _a_ vaut VRAI ou _b_ vaut VRAI

Cet opérateur peut également être défini par sa table de vérité présentée ci-contre.






### Equivalences


Il est possible de définir l'opérateur OU logique à partir du NON logique et du ET logique. En effet, si _a_ et _b_ sont des booléens alors _a OU B = NON ((NON a) ET (NON B))_.

On peut utiliser les tables de vérités pour démontrer cette égalité. On construit une table dans lesquelles les colonnes représentent les différentes sous-expressions dont nous avons
besoin. Les contenus des colonnes sont construits en appliquant aux colonnes connues les tables de vérité connues définies ci-dessus.

Dans notre cas en plus de _a_, _b_, parmi les expressions utiles à notre calcul on trouve NON _a_,
NON _b_. Une fois la table remplie pour ces deux expressions on peut déterminer celle de l'expression (NON _a_) ET (NON _b_) : si on définit _x_=NON _a _et _y_= NON _b_,

alors (NON _a_) ET (NON _b_)=_x_ ET _y_.
<table class="verite" >
<tbody >
<tr >
a
b
NON a
NON b
(NON a) ET (NON b)
</tr>
<tr >


x
y
x ET y
</tr>
<tr >

<td >0
</td>

<td >0
</td>

<td >1
</td>

<td >1
</td>

<td class="highlight" >1
</td>
</tr>
<tr >

<td >0
</td>

<td >1
</td>

<td >1
</td>

<td >0
</td>

<td class="highlight" >0
</td>
</tr>
<tr >

<td >1
</td>

<td >0
</td>

<td >0
</td>

<td >1
</td>

<td class="highlight" >0
</td>
</tr>
<tr >

<td >1
</td>

<td >1
</td>

<td >0
</td>

<td >0
</td>

<td class="highlight" >0
</td>
</tr>
</tbody>
</table>
On complète alors la table avec les expressions :

NON ((NON _a_) ET (NON _b_)) et (_a_ OU _b_)
<table class="verite" >
<tbody >
<tr >
a
b
NON a
NON b
(NON a) ET (NON b)
((NON _a_) ET (NON _b_))
(_a_ OU _b_)
</tr>
<tr >


x
y
(x ET y) = z
NON z

</tr>
<tr >

<td >0
</td>

<td >0
</td>

<td >1
</td>

<td >1
</td>

<td >1
</td>

<td class="highlight" >0
</td>

<td class="highlight" >0
</td>
</tr>
<tr >

<td >0
</td>

<td >1
</td>

<td >1
</td>

<td >0
</td>

<td >0
</td>

<td class="highlight" >1
</td>

<td class="highlight" >1
</td>
</tr>
<tr >

<td >1
</td>

<td >0
</td>

<td >0
</td>

<td >1
</td>

<td >0
</td>

<td class="highlight" >1
</td>

<td class="highlight" >1
</td>
</tr>
<tr >

<td >1
</td>

<td >1
</td>

<td >0
</td>

<td >0
</td>

<td >0
</td>

<td class="highlight" >1
</td>

<td class="highlight" >1
</td>
</tr>
</tbody>
</table>
L'égalité des contenus des deux dernières colonnes démontrent l'équivalence des deux expressions.






1. Trouvez une expression équivalente à _a_ ET _b _construite uniquement à partir des opérateurs NON et OU.
2. Démontrez que votre proposition est correcte à l'aide des tables de vérité.










1. Démontrez les règles de distributivité suivantes :

  1. _a_ ET (_b_ OU _c_) = (_a_ ET _b_) OU (_a_ ET _c_)
  2. _a_ OU (_b_ ET _c_) = (_a_ OU _b_) ET (_a_ OU _c_)


2. Démontrez les lois de Morgan :

  1. NON (_a_ OU _b_) = (NON _a_) ET (NON _b_)
  2. NON (_a_ ET _b_) = (NON _a_) OU (NON _b_)









<table class="droite verite" >
<tbody >
<tr >
a
b
a XOR b
</tr>
<tr >

<td >0
</td>

<td >0
</td>

<td >0
</td>
</tr>
<tr >

<td >0
</td>

<td >1
</td>

<td >1
</td>
</tr>
<tr >

<td >1
</td>

<td >0
</td>

<td >1
</td>
</tr>
<tr >

<td >1
</td>

<td >1
</td>

<td >0
</td>
</tr>
</tbody>
</table>
On rencontre également défini l'opérateur OU-exclusif, également appelé XOR (pour "eXclusive OR"). Vous trouvez sa table de vérité ci-contre.



1. Démontrez l'équivalence : _a_ XOR _b_ = (_a_ ET (NON _b_))) OU ((NON _a_) ET _b_)






## Application : les masques de sous-réseau




Très largement inspiré de [cet article](http://fr.wikipedia.org/wiki/Sous-r%C3%A9seau#Masque_de_sous-r.C3.A9seau) de Wikipedia.


Les adresses réseau des ordinateurs sont également appelé **adresse IP**, pour _Internet Protocol_. Les
adresses IP de version 4, IPv4, sont codés sur 32 bits. Elle est généralement représentée en notation décimale avec quatre nombres compris entre 0 et 255, séparés par des points, ce qui donne par exemple  : 192.168.100.2.

Les adresses réseau de type IPv4 sont composées de deux parties : le _sous-réseau_ et l'_hôte_. Les masques de sous-réseau utilisent la même représentation que celles des adresses IPv4. Bien que la norme IPv4 n'interdise pas que la partie significative du masque contienne des bits à 0, on utilise
en pratique des masques constitués (sous leur forme binaire) d'une suite de 1 suivis d'une suite de 0, il y a donc 32 masques réseau possibles. Un exemple possible est le masque `255.255.255.0`.

Pour obtenir l'adresse du sous-réseau on applique l'opérateur ET entre les notations binaires de l'adresse IPv4 et du masque de sous-réseau. L'adresse de l'hôte à l'intérieur du sous-réseau est quant à elle obtenue en appliquant l'opérateur ET entre l'adresse IPv4 et la négation (NON) du
masque.






1. Calculez le code binaire correspondant à l'adresse `192.168.100.2` (ou partez de l'adresse de votre machine).
2. Calculez le code binaire correspondant au masque `255.255.255.0`.
3. Calculez l'adresse binaire du sous-réseau puis donnez sa forme décimale.
4. Calculez l'adresse hôte puis donnez sa forme décimale.






## Vers l'électronique et le calcul






A chaque porte est associée une représentation graphique. Voici pour les portes ET et XOR :


![porte ET](/uploads/docs/doc03/porte-et.png)

![porte XOR](/uploads/docs/doc03/porte-xor.png)



Image tirée de Wikimedia Commons








Les opérations logiques évoquées ci-dessus sont mises en œuvre en électronique sous forme de portes logiques. Ainsi les circuits électroniques calculent des fonctions logiques de l'algèbre
de Boole. Pour chacun des opérateurs logiques évoquées ci-dessus (et d'autres) il existe donc des portes logiques appelés _porte ET_, _porte NON_, etc. Les valeurs _vrai _et _faux_ sont représentées par deux niveaux de
tension, _haut_ et _bas_. Un circuit de type _porte ET_ dispose donc de deux entrées et une sortie et la
valeur du niveau de tension en sortie dépend des niveaux de tension appliquées à chaque entrée, en respectant la table de vérité du ET. Les portes peuvent être connectées entre elles pour réaliser des
circuits logiques et on peut ainsi réaliser des calculs.

Prenons l'exemple de ce circuit :


![demi additionneur](/uploads/docs/doc03/demi-additionneur.png)



Il est appelé _demi-additionneur_ car il réalise l'addition de 2 bits (**A** et **B**), le résultats de cette somme est
représentée par **S** et la retenue éventuelle par **R**.


Vérifiez, avec une table de vérité par exemple, que **S** et **R** correspondent bien aux valeurs de la somme et de la retenue sur 1 bit de **A** et **B**.






Circuit intégré 7400 contenant 4 portes NON-ET (NAND). Les deux autres broches servent à l'alimentation 0V / 5V.




![circuit intégré 7400](/uploads/docs/doc03/circuit-7400.jpg)



Images tirées de Wikimedia Commons








A partir de ce circuit on peut en construire d'autres plus complexes permettant d'additionner des nombres de plusieurs bits.
Voir [sur cette page](http://fr.wikipedia.org/wiki/Additionneur) par exemple.

Et dans le même esprit, l'utilisation combinée des différentes portes de base permet de construire des circuits intégrés de plus en plus complexes, jusqu'au micro-processeur qui réalise les calculs au sein
d'un ordinateur. Il "suffit" de trouver la bonne organisation. C'est un peu comme les Légo en somme...
Vous pourrez trouver [ici quelques compléments.](http://fr.wikipedia.org/wiki/Circuit_logique)
