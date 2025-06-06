---
title: "Hexa : Cours"
bookCollapseSection: true
weight: 1

---

pdf pour [impression](/uploads/docsnsi/donnees_qkzk_img/hexa_print.pdf) et [diaporama](/uploads/docsnsi/donnees_qkzk_img/hexa_slides.pdf)


## Hexadécimal


Les nombres en binaires sont longs.
On utilise souvent la base 16 pour les manipuler plus facilement.
$16=2^4$ et utiliser une puissance a de nombreux avantages.

Le principe reste la notation positionnelle déjà abordée en binaire et utilisée en décimal.


### Chiffre hexadécimaux

On utilise 16 chiffres :

|   Hexa  	| 0 	| 1 	| 2 	| 3 	| 4 	| 5 	| 6 	| 7 	| 8 	| 9 	|  A 	|  B 	|  C 	|  D 	|  E 	|  F 	|
|:-------:	|:-:	|:-:	|:-:	|:-:	|:-:	|:-:	|:-:	|:-:	|:-:	|:-:	|:--:	|:--:	|:--:	|:--:	|:--:	|:--:	|
| Décimal 	| 0 	| 1 	| 2 	| 3 	| 4 	| 5 	| 6 	| 7 	| 8 	| 9 	| 10 	| 11 	| 12 	| 13 	| 14 	| 15 	|


### 16 chiffres : 0 1 2 4 5 6 7 8 9 A B C D E F

{{< hint info >}}
**Je répète : il y a 16 chiffres en hexadécimal : 0 1 2 4 5 6 7 8 9 A B C D E F**

**3** est un chiffre en hexadécimal. Il vaut 3 en décimal.\
**A** est un chiffre en hexadécimal. Il vaut 10 en décimal.\
**F**  est un chiffre en hexadécimal. Il vaut 15 en décimal.
{{< /hint >}}

{{< hint danger >}}
**il y a 16 chiffres en hexadécimal : 0 1 2 4 5 6 7 8 9 A B C D E F**

Quels sont les chiffres hexadécimaux :

**0 1 2 4 5 6 7 8 9 A B C D E F**

**A** est un chiffre hexadécimal qui vaut dix.

**E** est un chiffre hexadécimal qui vaut quatorze.


_Apprenez le, on vous le demandera en devoir._
{{< /hint >}}



### Notations

| Maths       	| Python   	| CSS     	|
|-------------	|----------	|---------	|
| $A3BC_{16}$ 	| `0xA3BC` 	| `#A3BC` 	|


### Utilisation en Python 

```python 
>>> 0xc0ffee                      # un entier noté en hexadécimal 
12648430
>>> hex(424242)                   # obtenir la représentation hexa. d'un entier 
'0x67932'
>>> int("0x123456789ABCDEF", 16)  # de l'hexa au binaire
81985529216486895
```

---

## Représenter facilement des octets

Pour la machine, l'unité de stockage la plus petite n'est pas le bit mais
l'octet.

_On ne peut pas écrire un bit en mémoire, on doit écrire au moins un octet à la fois_.

### Comment représenter facilement un octet ?

256 octets possibles... 256 symboles ? Difficile...

Mais ! $256 = 16^2$ on peut utiliser 2 symboles en base 16.

{{< hint info >}}
**Un octet est représenté par 2 chiffres hexadécimaux**
{{< /hint >}}

Ainsi, lorsqu'on lit depuis la mémoire `0xA4` cela représente _un octet_ valant 164.

L'interprétation dépend du contexte (caractère ? nombre ? ou tout autre chose...)

---

## Conversions

### Hexadécimal -> binaire

Convertir un binaire en hexa est facile.
**Chaque paquet de 4 bits donne un chiffre hexa :**

```
1010 0011 1011 1100
A    3    B    C
```

Pour aller vite on peut utiliser une table

![Table de conversion](/uploads/docsnsi/donnees_qkzk_img/table_hexa.png)


### Hexadécimal -> décimal

Pour convertir $4D5_{16}$ de l'hexa. vers le décimal,\
on commence par le dernier chiffre :

* $5 \times 16^0$ et on recule :
* $D \times 16 = 13 \times 16^1$ ($D$ correspond au nombre 13)
* $4 \times 16^2$

$$4D5_{16} = 5 \times 16^0 + 13\times 16^1 + 4\times 16^2 = 1~237_{10}$$

### Décimal -> hexadécimal

Divisions entières successives par **16** _jusqu'à trouver 0_.\
Les **restes** donnent les chiffres dans l'ordre **inverse**

$$959 = 59 \times 16 + 15  \longrightarrow F$$
$$59 = 3 \times 16 + 11    \longrightarrow B$$
$$3 = 0 \times 16 + 3  \longrightarrow 3$$
$$959_{10} = 3BF_{16}$$

### Python

```python
>>> int('3BF', 16)
959
>>> hex(959)
'0x3bf'
>>> 0xA3BC # c'est un entier pas une chaîne !!!
41916
>>> 0xa3bc # majuscule ou minuscule
41916
```

---

## Les couleurs

En informatique on distingue

* les couleurs à l'écran : synthèse additive
* les couleurs imprimées : synthèse soustractive

![synthèses additive et soustractive](/uploads/docsnsi/donnees_qkzk_img/syntheses.jpg)


### Synthèse additive

![synthèse additive](/uploads/docsnsi/donnees_qkzk_img/synthese_additive.png)

* En **synthèse additive** on utilise 256 niveaux de couleur pour les composantes Rouge, Vert et Bleu.
* Chaque niveau de couleur est codé sur un octet.

Par exemple :

`#FF0080` : `FF` rouge à fond, `00` pas de vert, `80` bleu à moitié :\
un joli rose, noté parfois : `rgb(255, 0, 128)`

![#FF0080](/uploads/docsnsi/donnees_qkzk_img/ff0080.jpg)

Quelques exemples :

~~~
blanc #FFFFFF     noir    #000000
rouge #FF0000     jaune   #FFFF00
vert  #00FF00     cyan    #00FFFF
bleu  #0000FF     magenta #FF00FF
~~~

Il convient d'être capable de _vaguement_ reconnaître une couleur à partir de sa valeur :

```
??? #FF8800 ???
```


{{< expand  "résultat ???" "..." >}}
<div style="background-color:#FF8800; text-align: center; height=30px;">
De l'orange...
</div>
{{< /expand >}}


{{< hint info >}}
Dans ce modèle (1 octet par niveau de rouge / vert / bleu), on peut représenter : $256^3 = 16^6= 2^{24} = 16 777 216$ de couleurs.

Le résultat n'a pas grande importance, la méthode si.
{{< /hint >}}


### Synthèse soustractive

* En **synthèse soustractive** on utilise souvent **CMJN** :\
  cyan, magenta, jaune et noir.

* Le niveau de noir permet d'économiser les encres et améliore le rendu.\
  On a développé de nombreuses méthodes.

![synthèse soustractive](/uploads/docsnsi/donnees_qkzk_img/synthese_soustractive.png)


{{< expand  "Remarques" "..." >}}
Afin d'économiser les coûts, les imprimeurs utilisent le moins de couleurs possible.

Les tracts qu'on distribuent n'en utilisent souvent que 2 !

![tract](./tract.jpeg)

On réalise par exemple des aplats (_surface de couleur uniforme, qui ne varie ni en luminosité, ni en pureté_).

![aplat](./cinq-heures.jpg)

Lorsqu'on veut imprimer davantage de couleurs, il faut :

* du papier de meilleure qualité,
* des encres différentes,
* plusieurs passages dans la machine, voire plusieurs machines.

Pour aller un peu plus loin, [cette vidéo](https://www.youtube.com/watch?v=h6_vRSoTqPY) pour enfant avec accent québéquois.

{{< /expand >}}

---

## Le contenu d'un fichier

Un fichier en machine n'est pas toujours lisible directement.

Ouvrir une _image_ avec un lecteur de _texte_ produit un résultat décevant.\
Comment lire facilement les octets qui la constituent ?


```bash
$ hexdump img/ff0080.jpg | head
0000000 d8ff e0ff 1000 464a 4649 0100 0101 4800
0000010 4800 0000 e2ff 8823 4349 5f43 5250 464f
0000020 4c49 0045 0101 0000 7823 636c 736d 1002
0000030 0000 6e6d 7274 4752 2042 5958 205a df07
0000040 0b00 0a00 0c00 1200 3800 6361 7073 6e2a
0000050 7869 0000 0000 0000 0000 0000 0000 0000
0000060 0000 0000 0000 0000 0000 0000 d6f6 0100
0000070 0000 0000 2dd3 636c 736d 0000 0000 0000
0000080 0000 0000 0000 0000 0000 0000 0000 0000
*
```


### Que fait la commande ?

```bash
hexdump img/ff0080.jpg | head
```

* `hexdump` : renvoie les octets d'un fichier sous forme hexadécimale
* `img/ff0080.jpg` : l'image avec la couleur rose vue plus tôt
* `| head` : ne garder que le début du fichier

### Comment lire le résultat ?

* Première colonne : position dans le fichier
  ```
  0000000
  0000010   <--- Cette ligne commence à l'octet x10
  0000020
  0000030
  ```

* `0000020 4c49 0045` :

  | Position 	| `x20` 	| `x21` 	| `x22` 	| `x23` 	|
  |:--------:	|:-----:	|:-----:	|:-----:	|:-----:	|
  |  Contenu 	| `x4c` 	| `x49` 	| `x00` 	| `x45` 	|
  |  Contenu 	| `76`     	| `73`     	| `0`      	| `69`     	|

Le contenu de mon image .jpg est donc _un nombre énorme_ encodé en binaire, que
la machine interprète à l'aide d'un programme et affiche à l'écran.
