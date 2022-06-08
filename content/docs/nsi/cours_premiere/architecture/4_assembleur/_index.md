---
title: Initiation assembleur
weight: 4

---

**PDF : [pour impression](./4_assembleur-Article.pdf), [diapos](./4_assembleur-Beamer.pdf)**


## Initiation à l'assembleur

### instructions machines

* Les instructions machines sont exécutées par l'unité de commande.

* Un programme est une suite d'instructions.

Le CPU est incapable d'exécuter directement des programmes écrits en Python
(ou C, java etc.).

Les instructions exécutées au niveau du CPU sont donc codées en binaire.


### Langage machine :

Ensemble des instructions exécutables par le microprocesseur

### Les instructions machines sont propres à chaque processeur

Chaque processeur possède son propre jeu d'instruction !

Heureusement, il existe de grandes familles (x86 PC, ARM téléphones etc.)

### Précisions

Une instruction machine est une chaîne binaire composée principalement
de 2 parties :

-   le champ "code opération" qui indique au processeur le type de
    traitement à réaliser. Par exemple le code "00100110" donne
    l'ordre au CPU d'effectuer une multiplication.
-   le champ "opérandes" indique la nature des données sur lesquelles
    l'opération désignée par le "code opération" doit être effectuée.

![instruction machine](../img/instr_machine.png)

## Familles Instruction machine

### Trois grandes familles

* arithmétiques
* transfert de données
* rupture de séquence

### Arithmétique

* Les instructions _arithmétiques_ (addition, soustraction,
    multiplication\...).

    "additionne la valeur contenue dans le registre R1 et
    le nombre 789 et range le résultat dans le registre R0".

### Transfert de données

* Les instructions _de transfert de données_

  "prendre la valeur située à l'adresse mémoire 487 et la placer
  dans la registre R2"

**Registre & Mémoire**

Un "mot" est un entier binaire sur $n$ bits. $n$ est une puissance de 2 correspondant à la classe du processeur.

Donc, un processeur 8 bits utilisera des mots de 8 bits (des octets) et un processeur 32 bits, des mots de 32 bits (4 octets).

L'assembleur dispose généralement de deux type de mémoires :

* Les registres : très petits, peu nombreux (8, 13, 17 rarement plus). Ils permettent de stocker un "mot",
* La mémoire vive (généralement abrégée en "Mémoire") : c'est la RAM, elle est plus vaste, moins rapide et chaque emplacement dispose d'une adresse numérique.

* Les opérations courantes se font depuis un registre vers un registre.
* On _lit_ depuis la mémoire vers un registre, 
* on _écrit_ depuis un registre vers la mémoire.
* On _déplace_ vers un registre (soit une valeur littérale, soit la valeur d'un autre registre).

### Rupture de séquence

**Séquence d'instruction**


les instructions machines sont situées en mémoire vive.
Au cours de l'exécution, le CPU passe d'une instruction à une autre

* l'instruction n°1 située à l'adresse mémoire 343,
* l'instruction n°2 située à l'adresse mémoire 344 etc.

Ce déroulé se poursuit jusqu'à :

* rencontrer un bug,
* rencontrer `HALT`,
* rencontrer une **rupture de séquence**,


Rupture de séquence (ou _saut, branchement_) :

> interrompre l'ordre initial sous certaines conditions
> en passant à une instruction située une adresse mémoire donnée

Par exemple, :

> Si la valeur contenue dans le registre R1 est >0,\
> alors la prochaine instruction à exécuter est l'adresse mémoire 4521,\
> sinon, la prochaine instruction à exécuter est à l'adresse mémoire 355.

### Sauts conditionnels ou inconditionnels

* Un saut _inconditionnel_ se déroulera toujours. On passe de tel emplacement à tel emplacement.
* Un saut _conditionnel_ doit suivre une comparaison. Selon le résultat de cette comparaison on sautera ou on passera à l'emplacement suivant.

## Programme en langage machine

Suite très très longue de "1" et de "0".

Extrêmement difficile de lire ou d'écrire ainsi :  on remplace les codes binaires par des symboles _mnémoniques_.

`11100010100000100001000001111101 <--> ADD R1,R2,#125`

En fait :


| Inscrution | Operande 1 | Operande 2 | Operande 3 |
|------------|------------|------------|------------|
| 11100010   | 10000010   | 00010000   | 01111101   |
| `ADD`      | `R1`       | `R2`       | `#125`     |


### Assembler :

> Transformer ces codes mnémoniques en langage machine.\
> `ADD R1,R2,#125` ---> `11100010100000100001000001111101`

"Programmer en assembleur" revient donc à écrire du code en "mnemonique" pour un processeur particulier.

Encore aujourd'hui, programmer en assembleur est une activité courante.

## Présentation d'un langage assembleur par l'exemple

### Déplacements

| Mnemonique                | Exemple          | Description                                                                 |
|---------------------------|------------------|-----------------------------------------------------------------------------|
| Charger                   | `LDR R1,78`      | Place la valeur stockée à l'adresse mémoire 78 dans le registre R1          |
| Stocker                   | `STR R3,125`     | Place la valeur stockée dans le registre R3 en mémoire vive à l'adresse 125 |
| Déplacer                  | `MOV R1, #23`    | Place 23 dans R0                                                            |

### Opérations arithmétiques

| Mnemonique                | Exemple          | Description                                                                 |
|---------------------------|------------------|-----------------------------------------------------------------------------|
| Ajouter                   | `ADD R1,R0,#128` | Additionne 128 à la valeur du registre R0, place dans R1                    |
| Ajouter deux registres    | `ADD R0,R1,R2`   | Additionne R1 à R2, place dans R0                                           |
| Soustraire                | `SUB R1,R0,#128` | Soustrait 128 de R0, place dans R1                                          |
| Soustraire deux registres | `SUB R0,R1,R2`   | Soustrait R2 de R1, place dans R0                                           |

### Rupture de séquence

| Mnemonique                | Exemple          | Description                                                                 |
|---------------------------|------------------|-----------------------------------------------------------------------------|
| Arrêter la machine        | `HALT`           | Arrête l'exécution du programme                                             |
| Saut inconditionnel       | `B 45`           | La prochaine instruction se situe en mémoire à l'adresse 45                 |
| Comparer                  | `CMP R0, #23`    | Compare R0 et le nombre 23                                                  |
|                           |                  | CMP doit précéder                                                           |
|                           |                  | un branchement conditionnel                                                 |
| Saut "Égal"               | `BEQ 78`         | Si le dernier CMP est égal, saute à l'adresse 78                            |
| Saut "Différent"          | `BNE 78`         | Si le dernier CMP est différent, saute à l'adresse 78                       |
| Saut "Plus grand"         | `BGT 78`         | Si le dernier CMP est plus grand, saute à l'adresse 78                      |
| Saut "Plus petit"         | `BLT 78`         | Si le dernier CMP est plus petit, saute à l'adresse 78                      |


### Exemple

Expliquez brièvement :

    ADD R0, R1, #42

    LDR R5,98

    CMP R4, #18
    BGT 77

    STR R0,15

    B 100



### Exemple

Écrire les instructions en assembleur correspondant à :

-   Additionne la valeur stockée dans le registre R0 et la valeur
    stockée dans le registre R1, le résultat est stocké dans le registre
    R5
-   Place la valeur stockée à l'adresse mémoire 878 dans le registre R0
-   Place le contenu du registre R0 en mémoire vive à l'adresse 124
-   la prochaine instruction à exécuter se situe en mémoire vive à
    l'adresse 478
-   Si la valeur stockée dans le registre R0 est égale 42 alors la
    prochaine instruction à exécuter se situe à l'adresse mémoire 85

### Labels


Les instructions assembleur B, BEQ, BNE, BGT et BLT
n'utilisent pas directement l'adresse mémoire de la prochaine
instruction à exécuter, mais des "labels".

Un label correspond à une adresse en mémoire vive

       CMP R4, #18
       BGT monLabel
       MOV R0,#14
       HALT
    monLabel:
       MOV R0,#18
       HALT

### Python --> assembleur


~~~python
x = 4
y = 8
if x == 10:
    y = 9
else:
    x = x+1
z = 6
~~~

### Python --> assembleur

       MOV R0, #4       
       MOV R1, #8       
       CMP R0, #10      
       BNE else         
       MOV R1, #9       
       B endif          
    else: 
       ADD R0, R0, #1
       B endif
    endif:
       MOV R0, #6
       HALT


