---
title: "Documentation" 
author: "qkzk" 
weight: 1

---

## Introduction simplifiée

pdf : [cette fiche imprimable](./1NSI_4_fiche_assembleur.pdf)

ARMLite est _machine_ disposant d'une architecture de Von Neumann qui exécute du code saisi en mnémoniques.

* Elle dispose de 13 registres généraux : `R0 à R12`. On les notera `Rx, Ry` etc.
* Les nombres _littéraux_ sont notés `#val`, par exemple `#20` désigne le nombre 20, _vingt_.
* Sa mémoire est initialisée avec le code du programme.
* Les autres registres sont utilisés pour le fonctionnement interne, quelques bits indiquent l'état de la dernière opération


## Instructions

Les instructions les plus couramment employées sont les suivantes :


1. Déplacement de contenu
    * `MOV Rx, val` : déplace `val` dans le registre `Rx`. `val` peut-être un registre
      ou un littéral.
    * `LDR Rx, adresse` : charge dans le registre `Rx` le contenu de l'adresse mémoire indiquée,
    * `STR Rx, adresse` : écrit le contenu du registre `Rx` à l'adresse mémoire indiquée,

    Attention, seules les adresses multiples de 4 sont valides. En effet, ARMLite fonctionne avec des _mots_ de 4 octets et chaque octet dispose d'une adresse.

    Donc `LDR R0, 40` est valide mais `LDR R0, 41` est invalide, car 41 n'est pas multiple de 4.

2. Opérations arithmétiques et logiques

    * `ADD Rx, Ry, val` : effectue l'addition `Ry + val` et écrit le résultat dans `Rx`. `val` peut être un registre ou un littéral.
    * Les instructions `SUB`, `AND`, `ORR`, `EOR` (respectivement soustraire, ET logique, OU logique, OU EXCLUSIF) ont un fonctionnement similaire.

3. Rupture de séquence

    * `CMP Rx, Ry` : effectue la comparaison entre `Rx` et `Ry`
    * `BGT label` : saute vers l'instruction précédée du nom `label` SEULEMENT si
      la précédente comparaison était "plus grand que."\
      Par exemple : 

      * si on a comparé 4 et 2, alors `BGT label` va sauter en `label`,
      * si on a comparé 4 et 10, alors `BGT label` va passer à l'instruction suivante.

    * `BEQ label` : saute vers l'instruction précédée du nom `label` SEULEMENT si
      les valeurs comparées étaient égales,
    * `BLT label` : saute seulement si la dernière comparaison était "plus petit que",
    * `B label` : saute, _sans condition_ vers `label`,
    * `HALT` : arrête la machine.


## Exemple de programme

```java
 1|      MOV R1, #10            //         R1 contient 10
 2|      MOV R2, #5             //         R2 contient 5
 3|      ADD R3, R1, R2         //         R3 contient 5 + 10 = 15
 4|      CMP R3, R1             //         Comparaison de 15 et 5
 5|      BGT more               //         15 > 5 donc on va en "more", ligne 08.
 6|      HALT                   //         Fin du programme (ne sera pas exécuté dans l'exemple)
 7|                             //         Rien, on va à la ligne
 8|    more:                    //         pas de code après l'étiquette, on ne fait rien
 9|      ADD R3, R1, R3         //         R3 contient 15 + 10 = 25
10|      HALT                   //         Fin du programme
```

---

_Ci-dessous une documentation plus complète_

# ARMLite: Manuel de référence de programmation

* Le simulateur [ARMLite](https://peterhigginson.co.uk/ARMlite/) et un [mirroir](https://www.iro.umontreal.ca/~mignotte/IFT1215/APPLETS/LM_ARM/)
* [documentation complète](https://peterhigginson.co.uk/ARMlite/Programming%20reference%20manual.pdf)

## Fenêtre

![ARMlite](/docs/nsi/cours_premiere/architecture/6_armlite/livre_from_metal/armlite.png)

### Code

Grande fenêtre de gauche.

* On l'_edit_, puis _submit_.
* on peut l'exporter (_save_) vers `myprog.txt` ou le charger (_load_) depuis un fichier texte.

Une fois soumis, on peut ajouter un _breakpoint_ (point d'arrêt) en cliquant sur une ligne.
Si la soumission engendre une erreur, elle est affichée en rose.

Lorsque l'exécution est terminée (ou interrompue), la ligne courante est en orange.

### Processeur

La colonne centrale remplie de boutons

#### Ses registres.

Ceux dans lesquels on va écrire sont `R0, ..., R12`

`PC` indique l'instruction courante (le nombre est multiplié par 4)

#### Boutons

* play (plein) pour exécuter tout d'un coup,
* pause, stop : je vous laisser deviner
* step & slow : exécuter une instruction ou pas à pas.
* la molette tourne lors de l'exécution

#### Le reste

* count : incrémenté à chaque instruction exécutée
* current instruction : le numéro de l'instruction courante,
* status bits : 0 ou 1 selon le dernier calcul ou la dernière comparaison.

    * N (Negative) : 1 si la dernière comparaison est négative,
    * Z (Zero) : 1 si la dernière comparaison est égale
    * C (Carry) : 1 si la dernière instruction a entrainé une retenue,
    * V (oVerflow) : 1 si la dernière instruction a engendré un dépassement de capacité (oubliez pour l'instant)

### Mémoire

La mémoire est rangée dans un tableau `ligne x colonne`.

Chaque adresse est notée en hexadécimal en concaténant les nombres :

`ligne 0x0006 | colonne 0x4 -> 0x00064`

Il y a 1 Mo de mémoire (environ 8 millions de bits).

Chaque _mot_ (case visible) peut être présenté en binaire, **hexa** ou décimal (signé ou non).

Le décimal signé utilise le _complément à deux_ sur 32 bits.

Lorsqu'on soumet un code :

1. les instructions sont traduites en langage machine,
2. elles sont stockées en mémoire,
3. s'il y a des données, elles sont stockées à la fin.

Depuis le programme (ou à la main en cliquant) on peut écrire dans la mémoire.


## Formatage du code

Le code (fenêtre de gauche) est formaté lorsqu'il est envoyé à ARMLite. Cela ajoute des numéros
de ligne à gauche.

Lorsqu'on édite le code, on peut ignorer ces numéros et il n'est pas nécessaire de se soucier
de l'ordre des lignes. ARMLite va les recalculer.


### Commentaires

Les commentaires sont précédés d'une double barre oblique `//` ou `;` ou `/`.

### Étiquettes - _Labels_

Une _etiquette_ est un mot faisant référence à un emplacement mémoire.

Elles servent à deux occasions :

* branchement. `B loop` va "brancher" vers la ligne `loop:` 
* données : on peut enregistrer des données, un peu comme des variables, en les nommant


### Mémoire  

ARMlite  dispose  d'un  total  de  1  Mo  de  mémoire  soit  1048567  (8  bits)
octets  dans  la  plage  `0x00000`  à  `0xfffff`. Un mot mémoire est composé de
quatre octets successifs soit 32 bits.

Toutes les adresses spécifiées dans le code ARMlite sont des adresses
d'_octets_. Lorsqu'un mot mémoire doit être chargé ou enregistré (`LDR` ou
`STR`), l'adresse doit correspondre à une limite de mot, c'est-à-dire qu'elle
doit être divisible par 4 - sinon vous obtiendrez une erreur "accès non
aligné...".

### Registres

ARMlite  a  seize  registres  32  bits.  Il  existe  treize  registres  à
usage  général  -  `R0`  à  `R12`  - et  trois  registres  qui  ont  également
des  buts  spéciaux  SP  (Stack  Pointer),  LR  (Link  Register)  et  PC
(Compteur de programme). 

Le `PC` est initialisé à 0 et contient l'adresse de la prochaine instruction à
exécuter. Il est incrémenté de 4 à chaque nouvelle instruction extraite de la
mémoire passer à l'instruction suivante.

En première nous n'utiliserons pas les autres registres spéciaux.

## Instructions  et  directives

ARMlite  implémente  ces  instructions  (classées  par  ordre  alphabétique  ici):

```java
ADD, ADDS, AND, B, BCS, BEQ, BGT, BL, BLT, BMI, BNE, BVS, CMP, EOR, HALT, LDR, 
LDRB, LSL, LSR, MOV, MVN, ORR, POP, PUSH, RET, RFE, STR, STRB, SUB, SUBS, SVC 
```

Les  mots-clés  suivants  ne  sont  pas  des  'instructions' (ils  ne  sont
pas  traduits  en  opérations  de  processeur)  mais  sont  des  'directives'
à  l'assembleur  (par  ordre  alphabétique) :

```
.ALIGN, .ASCII, .ASCIZ, .BLOCK, .BYTE, .DATA, .WORD
```

Pour  faciliter  la  programmation  et  pour  s'aligner  sur  les  mnémoniques
largement  utilisés  ailleurs,  les  synonymes  suivants  sont  acceptés :

```
BIS  (=ORR),  XOR  (=EOR),  OR  (=ORR),  JMS  (=BL),  HLT  (=HALT)
```

### `HALT`

Interrompt l'exécution de la machine. Tous les programmes doivent se terminer par `HALT`.

`HALT` n'est pas forcément en bas du code, généralement ce n'est pas le cas.

Cette instruction empêche le processeur de continuer à lire et exécuter le code.

### `MOV`

`MOV`  ('Move')  est  utilisé  pour  placer  une  valeur  spécifique  (une  'valeur  immédiate')  dans  un  registre  spécifié,  ou  pour  
copier  une  valeur  d'un  registre  à  un  autre.  `MOV`  ne  peut  pas  référencer  les  adresses  mémoire.  Le  format  est :

```
MOV  Rd,  <opérande2>
```

Où  Rd  spécifie  le  registre  de  destination,  et  `<opérande2>`  peut  être  un  registre  source  ou  une  valeur  immédiate  

* `MOV  R0, #25` déplace  la  valeur  décimale  "immédiate"  25  dans  R0
* `MOV  R5, R3` copie  la  valeur  de  R3  dans  R5
* `MOV  R4, SP` copie  la  valeur  du  registre  SP  dans  R4

Les  valeurs  immédiates  peuvent  être  spécifiées  au  format  décimal,  hexadécimal  ou  binaire  (par  exemple  `#0x3f`,  `#0b1101`) .

Avec  MOV  sur  ARMlite  les valeurs immédiates vont de $-2^{25}$ à $2^{35}$ ($\pm 33554432$). C'est assez vaste pour
que  n'importe  quelle  valeur  ou  étiquette  d'E/S  (ou  couleur  HTML)  puisse  être  donné  à  un  MOV.  

### `LDR, STR`

`LDR` (‘Load Register’) copie une valeur d'un emplacement mémoire dans un registre. 

`STR` (‘Store Register) fait le contraire : il copie une valeur d'un registre dans un emplacement mémoire. 

`LDR` et `STR` _ne peuvent être utilisés avec des valeurs immédiates_, seulement des registres.


Pour  `LDR`  et  `STR` ,  la  valeur  copiée  est  un  mot  de  32  bits.  Pour  cette  raison,  l'adresse  mémoire  spécifie  le  premier  des  quatre  octets  
successifs  où  le  mot  est  stocké  -  **l'adresse  doit  donc  être  divisible  par  quatre.**

Les  deux  instructions  prennent  deux  opérandes,  le  premier  spécifie  le
registre  et  le  second  spécifie  l'adresse  mémoire.  Dans  sa  forme  la
plus  simple,  appelée  "adressage  direct",  la  référence  d'adresse  mémoire
prend  la  forme  d'une  étiquette  ou  d'un  nombre  (spécifié  en  décimal,
hexadécimal  ou  binaire).  Exemples  d'adressage  direct :

`LDR R0,0xfc`  charge le contenu d'un mot débutant à l'adresse mémoire `0x000fc` into R0. 

`STR R1,120`   charge le contenu de `R1` dans le mot débutat à l'adresse mémoire (décimale) 120. 

`LDR  R3,0x81`  est  une  instruction  invalide  car  l'adresse  `0x00081`  n'est  pas  une  adresse  de  mot  valide  (elle  n'est  
pas  divisible  par  quatre).  

`STR  R3,myLabel`  stocke  le  contenu  de  `R3`  dans  le  mot  défini  par  l'étiquette  `myLabel`.

`LDR  R4,#0xfc`  est  une  instruction  invalide  car  `LDR`  ne  fonctionne  pas  avec  une  valeur  immédiate.

Nous ne devrions pas souvent utiliser LDRB et STRB,

Nous n'utiliserons pas l'adressage _indirect_.


## Opérations arithmétiques

Deux opérations sont implantées : l'addition et la soustration. Les autres doivent être programmées.

### `ADD` & `SUB`

`ADD R0, R1, R2` : ajoute `R1` et `R2` et enregistre dans `R0` : En python, on écrirait : `R0 = R1 + R2`

`SUB R0, R1, R2` : soustraie `R2` à `R1` et enregistre dans `R0`. En python, on écrirait : `R0 = R1 - R2`

Si on veut ajouter un _nombre littéral_, comme le nombre 5 (cinq), il faut le précéder d'un dièze: `#` et il doit être spécifié en dernier.

`ADD R0, R1, #5` : `R0 = R1 + 5`

Il n'est pas possible de spécifier deux nombres littéraux. Le premier opérande doit être un registre.

## Opérations bits à bits

Elles suivent les mêmes règles que les opérations arithmétiques

### `AND, ORR (OR), EOR (XOR), LSL, LSR`

* `AND` : et logique bit à bit,
* `ORR` ou `OR` : ou logique bit à bit,
* `EOR` ou `XOR` : ou exclusif bit à bit,
* `LSL` et `LSR` : décalages à gauche / à droite

Il existe aussi `MVN` pour `Move Not`, déplace et inverse tous les bits.

```java
MOV R0 #0b11111000
MOV R1 #0b10001100
AND R2, R0, R1
// R2  0b10001000 
```



## Comparaisons et branchements

### Branchement inconditionnel

L'instruction `B`, suivie d'une adresse, généralement donnée sous la forme d'un label, saute à cette ligne.

```java
    MOV R0, #42
    B la_bas
    MOV R0, #14
    HALT
la_bas:
    HALT
// R0 contient #42, pas 14.
```

### Comparaison

L'instruction `CMP Rx, RY` fait deux choses :

* la soustraction des opérandes : `Rx - Ry`
* affecte aux bits d'état `N` et `Z` ("Status bits") les valeurs.

    * `N` pour Negative. Si `Rx - Ry < 0` alors `N` vaut 1.

    * `Z` pour Zero. Il vaut 1 si `Rx - Ry = 0`

Les comparaisons doivent précédent les branchement _conditionnels_.

Une seule comparaison peut servir à plusieurs branchements.

### Branchement conditionnels

Ils fonctionennt tous de la même manière et correspondent à un `if condition, alors`

* `BEQ` : branche si "égaux",
* `BNE` : branche is "pas égaux",
* `BGT` : branche si "plus grand",
* `BLT` : branche si "plus petit", etc.

Il en existe d'autres, en particulier permettant de travailler avec des "subroutines", l'équivalent
de fonctions, que nous n'utiliserons pas.

```java
    MOV R0, #25
    MOV R1, #33
    CMP R0, R1
    BEQ equal
    BLT plus_petit
    BGT plus_grand
equal:
    MOV R0, #10
    HALT
plus_petit:
    MOV R0, #20
    HALT
plus_grand:
    MOV R0, #30
    HALT

// 25 < 33 donc R0 contient 20
```

## Entrées / Sorties : I/O

Sous le processeur vous avez 3 fenêtres blanches :

* la console d'affichage (message d'erreur et sorties)
* la fenêtre de saisie,
* la fenêtre graphique.

Nous allons simplement écrire du texte (châines, caractères, nombres) et lire du texte.
Nous ne dessinerons pas sur dans la fenêtre graphique.

### Adressage mémoire

ARMlite utilise un principe assez courant : **Memory-mapped I/O**

Cela signifie que certaines adresses mémoires sont reservées aux entrées et sorties.

On utilise donc les instructions `LDR` et `STR` pour lire et écrire avec les périphériques (clavier ecran etc.)

L'autre approche courante est appelée _Port-mapped I/O_ et nécessite d'avoir des instructions spécifiques pour lire et écrire.

Quelques exemples simples :

### Écrire un nombre

```java
   MOV R0, #42
   STR R0, .WriteUnsignedNum
```

Va charger le nombre 42 (quarante deux) dans `R0` et l'écrire dans la console, comme un nombre décimal positif. On verra `42`.

On peut utiliser `.WriteSignedNum` pour écrire des nombres négatifs.

### Écrire une chaîne de caractères

```java
    MOV R1, #msg1
    STR R1, .WriteString
msg1: .ASCIZ "Hello World\n"
```

* `msg1` contient une chaîne ASCIZ (Ascii terminée par l'octet `0`) avec le texte `Hello World` suivi d'un retour à la ligne (`\n`)
* on charge dans le registre `R1` cette chaîne,
* on l'écrit comme du texte en précisant _l'adresse_ `.WriteString`


### Écrire un seul caractère

_Ceci n'a pas d'analogue en Python. Python n'a pas de type particulier pour les caractères ASCII_.

On peut afficher un seul caractère ASCII avec l'adresse `WriteChar`

Par exemple le `A` est encodé par le nombre 65 dans la table ASCII et donc :

```java
    MOV R0, #65
    STRB R0, .WriteChar
    HALT
```

va :

* stocker dans R0 la valeur 65,
* l'afficher comme un caractère ASCII (attention, l'instruction est `STRB`)



### Lire un nombre

```java
    LDR R2, .InputNum
```

Va demander à l'utilisateur de saisir un nombre décimal et le charger dans `R2`.

### Lire une chaîne ASCII

```java
    LDR R0, #myString
    STR R0, .ReadString
    HALT
myString: 
```

1. `myString:` réserve un emplacement mémoire pour la chaîne à venir,
2. `LDR R0, #myString`: on prépare un registre pour la chaîne à venir,
3. `STR R0, .InputNum`: on lit une chaîne ASCII et on l'enregistre dans l'emplacement réservé.


Autre exemple :

lire et afficher une chaîne tapée par l'utilisateur :

```java
      MOV R0, #myWord
      STR R0, .ReadString
      MOV R1, #myWord
      STR R1, .WriteString
      HALT
myWord:
```

1. `myWord:` réserve un emplacement mémoire avec l'étiquette `myWord`
2. `MOV R0, #myWord` est indispensable... cela prépare simplement le registre.
3. `STR R0, .ReadString`, lit le contenu à l'adresse `.ReadString`, cette adresse correspond à du texte tapé dans la fenêtre de saisie, et `myWord` va contenir ce mot.
4. `MOV R1, #myWord`, déplace le contenu de `myWord` dans le registre 1,
5. `STR R1, .WriteString`, écrit le contenu de `R1` comme une chaîne ASCII à l'écran,


## Exemples de programmes

### Opérations basiques

```python
a = 14
b = 3
c = a - b
d = a + b
e = a & b # ET  bit à bit entre a et b
f = a | b # OU  bit à bit entre a et b
g = a ^ b # XOR bit à bit entre a et b
```

```java
MOV R0, #14
MOV R1, #3
ADD R2, R0, R1
SUB R3, R0, R1
AND R4, R0, R1
ORR R5, R0, R1
XOR R6, R0, R1
HALT
```

### `if else`

```python
a = 5
b = 7
if a == b:
    c = 4
else:
    c = 5

# donc c = 5
```

```java
    MOV R0, #5
    MOV R1, #7
    CMP R0, R1
    BEQ equal
    MOV R2, #5
    HALT
equal:
    MOV R2, #4
    HALT
```

### Boucle

```python
a = 0
while a < 8:
    print("bonjour")
    a = a + 1
```

```java
    MOV R0, #0
loop:
    CMP R0, #8
    BGT end
    MOV R1, #msg
    STR R1, .WriteString
    ADD R0, R0, #1
    B loop
end:
    HALT
msg: .ASCIZ "bonjour\n"
```

### Multiplier

```python
a = 3
b = 6
c = a * b

# à la main sans le produit
# a * b = a + a + a + ... + a
p = 0
c = 0
while c < b:
    p = p + a
    c = c + 1

# p = 18
```

```java
// R0: a
// R1: b
// R2: a * b
// R3: compteur de boucle
    MOV R0, #3
    MOV R1, #6
    MOV R2, #0
    MOV R3, #0

loop:
    CMP R3, R1
    BEQ end
    ADD R2, R2, R0
    ADD R3, R3, #1
    B loop

end:
    HALT
```

### Division entière

Pas non plus de division dans ARMLite mais on peut 
utiliser les soustractions successives :

**diviser 21 par 4**

* $q = 0, r = 21$. $21 > 4$ donc on continue
* $q = 1, r = 21 - 4 = 15$. $15 \ge 4$ donc on continue
* $q = 2, r = 15 - 4 = 9$. $9 \ge 4$ donc on continue
* $q = 3, r = 9 - 4 = 5$. $5 \ge 4$ donc on continue
* $q = 4, r = 5 - 4 = 1$. $1 < 4$ donc on a fini.
* $21 = 4 \times 5 + 1$


```python
a = 21
b = 4

# a = 5 * b + 1
c = a // b # 5
d = a %  b # 1

# soustractions successives
q = 0
r = a
while r >= b:
    q += 1
    r = r - b

print(q)
print(r)
# q = 5
# r = 1
```

```java
// R0: a
// R1: b
// R2: a // b
// R3: a % b

    MOV R0, #21
    MOV R1, #4
    MOV R2, #0
    MOV R3, R0

loop:
    CMP R3, R1
    BLT end
    ADD R2, R2, #1
    SUB R3, R3, R1
    B loop

end:
    STR R2, .WriteUnsignedNum
    STR R3, .WriteUnsignedNum
    HALT

```


---

Il existe de nombreuses autres instructions présentées dans la documentation (lien tout en haut).

