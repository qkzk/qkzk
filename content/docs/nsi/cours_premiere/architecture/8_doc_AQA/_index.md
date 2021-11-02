---
title: Documentation Assembleur AQA
bookCollapseSection: true
author: qkzk
theme: metropolis
weight: 9

---


# Traduction de la documentation d'AQA

## Contexte

L'objectif de ce simulateur est de permettre aux étudiants de se familiariser avec le langage assembleur spécifié par AQA et utilisé dans les niveaux AS et A des examens de science informatique.

_Remarque du traducteur :_ AQA est un centre d'examen qui offre aux lycéens du royaume uni un diplome équivalent du baccalauréat. Il comporte une option science informatique. A level ~ baccalauréat. AS level ~ baccalauréat technologique.

## Suppositions


AQA ne spécifie pas son langage assez précisemment pour créer un assembleur donc certaines suppositions ont dû être faites.


_Remarque du traducteur :_ cette partie n'intéresse que les enseignants qui cherchent à créer un sujet et le tester dans l'assembleur.

## Le jeu instructions AQA

* `LDR Rd, <memory ref>` charge une valeur enregistrée en mémoire à une adresse précisée par `<memory ref>` dans un registre `d`

* `STR Rd, <memory ref>` enregistre la valeur du registre `d` dans la mémoire à l'adresse `<memory ref>`.

* `ADD Rd, Rd, <operand2>` ajoute la valeur spécifiée dans `<operand2>` à celle enregistrée dans le registre `n` et l'enregistre dans le registre `d`

* `SUB Rd, Rd, <operand2>` soustraie la valeur spécifiée dans `<operand2>` à celle enregistrée dans le registre `n` et l'enregistre dans le registre `d`

* `MOV Rd, <operand2>` copie la valeur spécifiée par `<operand2>` dans le registre `d`.

* `B <label>` (branch) réalise un saut (sans condition) jusqu'à l'instruction située à la position `<label>` dans le programme.

* `B<condition> <label>` réalise un saut jusqu'à la position `<label>` si la dernière comparaison réalisée vérifie une condition. Les valeurs possibles pour `<condition>` sont : `EQ` (équal, égal), `NE` (not equal, différent), `GT` (Greater Than, plus grand que), `LT` (Less than, plus petit que).

* `AND Rd, Rn, <operand2>` réalise un ET logique bit à bit entre la valeur du registre `n` et `<operand2>` et l'enregistre dans le registre `d`

* `ORR Rd, Rn, <operand2>` réalise un OU logique bit à bit entre la valeur du registre `n` et `<operand2>` et l'enregistre dans le registre `d`

* `EOR Rd, Rn, <operand2>` réalise un OU exclusif (XOR) logique bit à bit entre la valeur du registre `n` et `<operand2>` et l'enregistre dans le registre `d`


* `MVN Rd, <operand2>` réalise un NON logique bit à bit de `<operand2>` et l'enregistre dans le registre `d`


* `LSL Rd, Rn, <operand2>` Réalise un décalage à gauche (logical shift left) de `<operand2>` bits sur la valeur du registre `n` et l'enregistre dans le registre `d`. **RQ** cela revient à multiplier par `2 ** <operand2>`


* `LSR Rd, Rn, <operand2>` Réalise un décalage à droite (logical shift right) de `<operand2>` bits sur la valeur du registre `n` et l'enregistre dans le registre `d`. **RQ** cela revient à faire la division entière par `2 ** <operand2>`

* `HALT` arrête le programme

* `<operand2>` peut être un nombre noté `#234` pour $234$ ou un registre, noté `Rd`.

* Les registres vont de `R0` à `R12`.


## Extensions INP et OUT

* `INP Rd, 2` lit un nombre depuis la zone de saisie et l'enregistre en registre `d`, `OUT Rd, 4` affiche un nombre.

    Changer le numéro `4` change le mode :

    * 4 : nombre signé
    * 5 : nombre non signé
    * 6 : hex
    * 7 : caractère


## Commentaire

Tout ce qui suit un `/` est un commentaire. J'ai partout utilisé `//` dont l'usage est fréquent dans les langages haut niveau.

## Suite

_beaucoup de commentaires trop techniques pour nous._

## boucle Récupérer et exécuter (Fetch / Execute cycle)

Elle est animée par des blocs qui se déplacent. Ainsi qu'on peut s'en douter, certains navigateurs ont des soucis avec les blocs de nombre trop grands.

## Sources

Auteur : [peterhigginson](www.peterhigginson.co.uk/LMC)

Traducteur : [qkzk](qkzk.xyz)
