---
title: "Binaire - cours"
bookCollapseSection: true
author: qkzk
weight: 1

---

# Représenter des entiers en machine : le système binaire

pdf [pour impression](/uploads/docsnsi/donnees_qkzk_img/binaire_print.pdf) et [diaporama](/uploads/docsnsi/donnees_qkzk_img/binaire_slides.pdf)

## Binaire

### Différentes bases

Dans la vie courante on utilise la base 10.

En informatique on rencontre d'autres manières de représenter les nombres :

* binaire
* complément à 2
* octal
* hexadécimal etc.
* nombres à virgules flottantes

{{< expand "" "..." >}}
Quand on creuse, c'est encore plus complexe. Par exemple le langage Rust utilise 14 types différents pour représenter les nombres !

Pourquoi autant ?

Définir plusieurs types permet d'économiser de l'espace mémoire :

- `u8` est un type d'entiers positifs occupant 8 bits donc s'étant de 0 à $2^8 - 1 = 255$
- `u64`, la même chose mais de 0 à $2^{64} - 1$.
- `i8` cette fois on s'autorise des nombres négatifs, toujours sur 8 bits, de $-2^7=-128$ à $2^7 - 1 = 127$.
- etc.

Cette complexité supplémentaire offre une connaissance précise de la représentation en mémoire.

En Python, par contre, on se situe beaucoup plus haut : les entiers n'ont pas de limite de taille et peuvent être positifs ou négatifs. Il est impossible de savoir précisemment comment un entier sera représenté en mémoire sans entrer dans les détails du code.
{{< /expand >}}

### Système de représentation par position

Qu'on utilise la base 10, 2, 8, 16 ou autre, on emploie toujours
_la numération par position._


{{< hint info >}}
**Représentation par position** : La position d'un chiffre définit la valeur associée à ce chiffre.
{{< /hint >}}

### Numération par position

**Exemple** : En base 10 :

$345 = 3\times100 + 4\times10 + 5 = 3\times 10^2 + 4\times10^1+5\times10^0$

Le $3$ de $345$ représente donc $300$, le $4$ représente $40$ etc. On a pourtant $3 < 4$...

En binaire, on a deux chiffres. Chaque chiffre est un _bit_ (=**bi**nary digi**t**).

$0b1101 = 1 \times 2^3 + 1\times 2^2 + 0\times2^1 + 1\times2^0 = 13$

Afin d'indiquer une représentation binaire on utilise $0b$ avant le nombre ou $_2$ après le nombre :

$0b$


### Les puissances de 2

Les puissances de 10 c'est facile : 1, 10, 100, 1000 etc. mais celles de 2 demandent un effort.

| Exposant $n$   | 0   | 1   | 2   | 3   | 4    | 5    | 6    | 7     | 8     | 9     | 10     | 11     | 12     | 13     | 14      |
| :------------: | :-: | :-: | :-: | :-: | :--: | :--: | :--: | :---: | :---: | :---: | :----: | :----: | :----: | :----: | :-----: |
| $2^n$          | 1   | 2   | 4   | 8   | 16   | 32   | 64   | 128   | 256   | 512   | 1024   | 2048   | 4096   | 8192   | 16384   |

**Conseil :** retenez les par coeur en jouant à [2048](https://play2048.co/).

### Vocabulaire 

- _bit_ : symbole 0 ou 1. Ce sont les _chiffres_ de la représentation binaire.
- _octet_ : bloc de 8 bits. La _mémoire_ de l'ordinateur n'est pas capable de lire 1 bit à la fois. Elle répond avec des _blocs_ d'un ou de plusieurs octets. 
- _byte_ : traduction anglaise de l'octet.

Par exemple : 2MB = 2 Mega Octets = $2 \times 10^6$ octets = $16\hspace{2mm}000\hspace{2mm}000$ bits.

## Du binaire au décimal.

{{< hint info >}}
Pour convertir un entier donné en binaire on le lit depuis la droite et on fait la somme.

$0b10011$ = 1 + 2 + 0 + 0 + 16 = 19.

Autre notation : $10011_2 = 19_{10}$
{{< /hint >}}

Autre exemple :

La représentation décimale de $0b101010$ est

$$1\times2^5+0\times2^4+1\times2^3+0\times2^2+1\times2^1+0\times2^0$$
$$=32+8+2$$
$$=42$$

Encore un :

$0b10011011 = 2^7 + 2^4+2^3+2^1+2^0 = 128 + 16 + 8 + 2 + 1 = 155$

![Binaire -> décimal](./binary_decimal.jpg)



### Exercice 1

* Donnez les valeurs entières représentées par $0b0100$, $0b10101$, $0b101$,
$0b0101$ et $0b00101$.

* Trier par ordre croissant $0b11$, $0b100$, $0b111$ et $0b1000$.


## Du décimal au binaire.

Deux algorithmes majeurs.

* Facile _à programmer_ : les divisions successives.
* Facile _de tête_ : soustraire des puissances de 2.


### Décimal au binaire avec les puissances de 2.

Écrire 57 en base 2 (=donner sa représentation binaire).

* $32<57<64$.

    Donc on fait $57 = 32 + 25 = 2^5 + 25$. On a un chiffre 1 à la position 6.

* $16<25<32$. 

    Donc on fait $25 = 16 + 9 = 2^4 + 9$. On a un chiffre 1 à la position 5.

* $8<9<16$. 

    Donc on fait $9 = 8 + 1 = 2^3 + 1$. On a un chiffre 1 à la position 4.

* $1=2^0$. 

    On peut s'arrêter dès qu'on atteint une puissance de 2. On a un chiffre 1 à la position 1.

$$57 = 0b111001$$

En une ligne : $57 = 32 + 16 + 8 + 1 = 0b111001$


_Autre exemple :_

$$123 = 64 + 59 = 64 + 32 + 27$$
$$123 = 64 + 32 + 16 + 11$$
$$123 = 64 + 32 + 16 + 8 + 3$$
$$123 = 64 + 32 + 16 + 8 + 2 + 1$$

Donc 

$$123 = 0b1111011$$



![10 types of people](/uploads/docsnsi/donnees_qkzk_img/10typesofppl.jpg)

### Du décimal au binaire avec les divisions successives


{{< hint info >}}
**Algorithme des divisions successives**

1. On divise par 2 **jusqu'à ce que le quotient soit 0**
2. On lit les bits en montant de droite à gauche : 
{{< /hint >}}

![Division euclidienne](./divisioneuclidienne.png)

![Division euclidienne exemple](./cas-particulier-division-euclidienne.jpg)

_Pour nous, c'est plus facile, le diviseur est toujours 2 donc le reste est toujours 0 ou 1_.

_Dans $n : 2$, le reste est $0$ si $n$ pair et $1$ si $n$ est impair_.


Donner la représentation binaire de 167.

![divisions successives](/uploads/docsnsi/donnees_qkzk_img/divisions.png)

`167 = 0b10100111`

---

### Exercice 2

Quelle est la représentation binaire de 14 et 78 ?

## Binaire en Python

Python dérivant du langage C, les nombres en binaire sont notés `0bxxxx`

Python converti naturellement un entier **d'une base *b* vers le décimal** avec `int(nombre, b)`

La conversion **vers le binaire** se fait avec `bin` et renvoie une _chaîne de caractères_.

```python
>>> 0b111011
59
>>> a = '0b11'
>>> int(a, 2)
3
>>> b = 10
>>> bin(b)
'0b1010'
```

Faites bien attention :

* `0b111011` est un `int` qu'on a écrit sous forme binaire et dont la valeur est 59.
* `"0b111011"` est une `str` qu'on peut _convertir_ en entier avec `int`.

### Les nombres en mémoire

{{< hint info >}}
**ATTENTION** En mémoire, ce sont des entiers encodés en binaire.

```python
>>> 4 + 5
9
```

Ainsi, pour réaliser l'opération `4+5` Python converti d'abord en binaire,
additionne puis converti en décimal pour afficher `9`.
{{< /hint >}}



<!-- Complément info : convertisseur binaire à la main, algo à la main -->

### Taille d'un nombre en binaire

Le **nombre de bit** d'un entier nous indique l'espace mémoire _minimal_ qu'il
faudra pour le stocker.

$123 = 0b1111011$ il faut au moins 7 bits pour stocker ce nombre.

En pratique, les machines utilisent des blocs de taille 1 octet (=8 bits), ce nombre entre dans un octet.

### Taille et opérations

{{< hint info >}}
Si $x$ occupe `n` bits et $y$ occupe `p` bits alors :

* **SOMME**  : $x + y$ occupe au plus `max(n, p) + 1` bits,
* **PRODUIT** : $x \times y$ occupe au plus `n + p` bits.

| Nombre         	| $x$ 	| $y$ 	| $x+y$                	| $x\times y$     	|
|----------------	|-----	|-----	|----------------------	|-----------------	|
| Nombre de bits 	| $n$ 	| $p$ 	| $\leq max(n, p) + 1$ 	| $\leq n + p$     	|
{{< /hint >}}

### Le logarithme binaire

En mathématique, la fonction $\ln$ pour _logarithme népérien_ ou _logarithme naturel_
est une fonction ayant d'importantes propriétés.

Rendue populaire par Napier, elle a permis de considérablement simplifier les calculs à la main.

_Vous verrez en mathématiques qu'elle permet de transformer les produits en somme : $\ln (a \times b) = \ln a + \ln b$_

Une de ses propriétés est de donner une mesure du nombre de chiffres d'un nombre dans une base :

Si $t$ est la taille de $x$ en base $b$ alors $$\frac{\ln(n)}{\ln(b)} \leq t < 1 + \frac{\ln(n)}{\ln(b)}$$


Pour nous, cela se traduit ainsi :


{{< hint info >}}
En notant $\log_2 (n) = \frac{\ln n}{\ln 2}$ et $\lceil x \rceil$ l'arrondi supérieur de $x$ :

Le nombre de bits d'un entier $n$ est $\lceil \log_2(x + 1) \rceil$.
{{< /hint >}}

---

