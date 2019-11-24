---
title: "Résumé binaire, hexadécimal, booléen"
---

## Numération par position

Différentes bases (10, 2 et 16) mais un même système : _numération par position_.

| systeme     | base | chiffres         |
|-------------|------|------------------|
| Décimal     | 10   | 0123456789       |
| Binaire     | 2    | 01               |
| Héxadécimal | 16   | 0123456789ABCDEF |

Convertir en décimal :

* **Décimal** : $2019 = 2\times1000 + 1\times10 + 9 = 2\times10^3 + 1\times10^1 + 9\times10^0$

* **Binaire** : $0b1101 = 1 \times 2^3 + 1 \times 2^2 + 1 \times 2^0 = 8 + 4 + 1 = 13$

* **Hexadécimal** : $0xA5F = 0xA \times 16^2 + 0x5\times 16^1 + 0xF \times 16^0 = 10 \times 256 + 5 \times 16 + 15 = 2655$

Les _entiers_ ne changent pas, leur _représentation_ varie : `103 = 0b1100111 = '0x67'`

**Remarques :**

* Dans la mémoire d'une machine : binaire. À l'écran, ça varie, on peut avoir les trois.


* **Taille** (= nombre de chiffre) des résultats opérations. Même principe dans toutes les bases :

    * la taille d'une **somme** est $\leq$ à la plus grande des deux tailles + 1.
    * la taille d'un **produit** est $\leq$ à la somme des deux tailles.


## Convertir en binaire, convertir en hexadécimal

On utilise l'algorithme des divisions successives :

![divisions successives](/uploads/docsnsi/resume_binaire/divisions.png)

1. On divise par 2 **jusqu'à ce que le quotient soit 0**
2. On lit les bits en montant de droite à gauche : `167 = 0b10100111`

Cet algorithme se programme en python :

~~~python
def bina(entier):
  bits = ''
  while entier != 0:
    reste = entier % 2
    entier = entier // 2
    bits = str(reste) + bits
  return bits
~~~

La conversion `décimal -> hexadécimal` se fait par des divisions par 16.

## Information dans la machine.

On regroupe les bits par paquet de 8 bits : 8 bits = 1 octet.

Attention, en anglais : octet se dit _byte_ !

Les notations : 1000 bits = 1 kilo bit = 1kb ; 1000 octets = 1 kilo octet = 1ko = 1kB

Il faut 2 chiffres hexadécimaux pour représenter un octet : `0xaf = 175`

## Booléens et portes logiques.

George Boole (1815-1864) créateur de l'_algèbre de Boole_ qu'on utilise pour représenter la logique interne de la machine.

Utilise deux états "Vrai : 1", "Faux : 0". Notés `True` et `False` en python.

### Opérateurs booléens.
| opérateur | description | exemple                | python                   |
|-----------|-------------|------------------------|:------------------------:|
| `non`     | contraire   | `non vrai = faux`      | `not`                    |
| `et`      | et logique  | `vrai et faux = faux`  | `and`                    |
| `ou`      | ou logique  | `vrai ou faux = vrai`  | `or`                     |
| `xor`     | ou exclusif | `vrai xor faux = vrai` | pas implémenté en Python |

On utilise des _tables de vérité_ pour les représenter :


| A | B | A XOR B |
|---|---|:-------:|
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

### Circuits : le demi additionneur


![demi-additionneur](/uploads/docsnsi/resume_binaire/demi-additionneur.png)

Il est appelé *demi-additionneur* car il réalise l'addition de 2 bits
(**A** et **B**), le résultats de cette somme est représentée par **S**
et la retenue éventuelle par **R**.


## Opérations bits à bits (pas eu le temps en cours)

Masque = `et` bit à bit.

| | |
|--------------|-----------|
| nombre       | 1011.1100 |
| masque       | 1101.0101 |
| et bit à bit | 1001.0100 |
