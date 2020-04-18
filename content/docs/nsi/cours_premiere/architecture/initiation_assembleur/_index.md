---
title: Initiation assembleur
author: David Roche
theme: metropolis
weight: 13
---



# Initiation à l'assembleur

Revenons sur ces instructions aussi appelées "instructions machines"
exécutées par l'unité de commande. Comme vous le savez déjà, un
ordinateur exécute des programmes qui sont des suites d'instructions.
Le CPU est incapable d'exécuter directement des programmes écrits, par
exemple, en Python. En effet, comme tous les autres constituants d'un
ordinateur, le CPU gère uniquement 2 états (toujours symbolisés par un
"1" et un "0"), les instructions exécutées au niveau du CPU sont
donc codées en binaire. L'ensemble des instructions exécutables
directement par le microprocesseur constitue ce que l'on appelle le
"langage machine".

Une instruction machine est une chaîne binaire composée principalement
de 2 parties :

-   le champ "code opération" qui indique au processeur le type de
    traitement à réaliser. Par exemple le code "00100110" donne
    l'ordre au CPU d'effectuer une multiplication.
-   le champ "opérandes" indique la nature des données sur lesquelles
    l'opération désignée par le "code opération" doit être effectuée.

![instruction machine](/uploads/docsnsi/architecture/aqa/img/instr_machine.png)

## Instruction machine

Les instructions machines sont relativement basiques (on parle
d'instructions de bas niveau), voici quelques exemples :

* Les instructions _arithmétiques_ (addition, soustraction,
    multiplication\...). Par exemple, on peut avoir une instruction qui
    ressemble à "additionne la valeur contenue dans le registre R1 et
    le nombre 789 et range le résultat dans le registre R0".

* Les instructions _de transfert de données_ qui permettent de
  transférer une donnée d'un registre du CPU vers la mémoire vive et
  vice versa. Par exemple, on peut avoir une instruction qui ressemble
  à "prendre la valeur située à l'adresse mémoire 487 et la placer
  dans la registre R2" ou encore "prendre la valeur située dans le
  registre R1 et la placer à l'adresse mémoire 512"

* Les instructions de rupture de séquence : les instructions machines
    sont situées en mémoire vive, si, par exemple, l'instruction n°1
    est située à l'adresse mémoire 343, l'instruction n°2 sera située
    à l'adresse mémoire 344, l'instruction n°3 sera située à
    l'adresse mémoire 345... Au cours de l'exécution d'un programme,
    le CPU passe d'une instruction à une autre en passant d'une
    adresse mémoire à l'adresse mémoire immédiatement supérieure :
    après avoir exécuté l'instruction n°2 (situé à l'adresse mémoire
    344), le CPU "va chercher" l'instruction suivante à l'adresse
    mémoire 344+1=345.

    Les instructions de rupture de séquence
    d'exécution encore appelées _instructions de saut ou de branchement_
    permettent d'interrompre l'ordre initial sous certaines conditions
    en passant à une instruction située une adresse mémoire donnée, par
    exemple, nous pouvons avoir une instruction qui ressemble à cela :
    imaginons qu'à l'adresse mémoire 354 nous avons l'instruction
    "si la valeur contenue dans le registre R1 est strictement
    supérieure à 0 alors exécuter l'instruction située à l'adresse
    mémoire 4521".

    Si la valeur contenue dans le registre R1 est
    strictement supérieure à 0 alors la prochaine instruction à exécuter
    est l'adresse mémoire 4521, dans le contraire, la prochaine
    instruction à exécuter est à l'adresse mémoire 355.

## Opérandes

Comme déjà dit, les opérandes désignent les données sur lesquelles le
code opération de l'instruction doit être réalisée. Un opérande peut
être de 3 natures différentes :

1.  l'opérande est une valeur immédiate : l'opération est effectuée
    directement sur la valeur donnée dans l'opérande
2.  l'opérande est un registre du CPU : l'opération est effectuée sur
    la valeur située dans un des registres (R0,R1, R2,\...), l'opérande
    indique de quel registre il s'agit
3.  l'opérande est une donnée située en mémoire vive : l'opération est
    effectuée sur la valeur située en mémoire vive à l'adresse XXXXX.
    Cette adresse est indiquée dans l'opérande.

Quand on considère l'instruction machine : "additionne le nombre 125
et la valeur située dans le registre R2 , range le résultat dans le
registre R1", nous avons 2 valeurs : le "nombre 125" (qui est une
valeur immédiate, nous sommes dans le cas n°1) et "la valeur située
dans le registre R2" (nous sommes dans le cas n°2)

Quand on considère l'instruction machine : "prendre la valeur située
dans le registre R1 et la placer à l'adresse mémoire 512", nous avons
2 valeurs : "à l'adresse mémoire 512" (nous sommes dans le cas n°3)
et "la valeur située dans le registre R1" (nous sommes toujours dans
le cas n°2)

Évidemment le microprocesseur est incapable d'interpréter la phrase
"additionne le nombre 125 et la valeur située dans le registre R2 ,
range le résultat dans le registre R1" tout cela doit être codé sous
forme binaire.

## Programme en langage machine

Un programme en langage machine est donc une suite très très longue de
"1" et de "0" ! Programmer en langage machine est
extrêmement difficile, pour pallier cette difficulté, les informaticiens
ont remplacé les codes binaires abscons par des symboles mnémoniques.
Au lieu d'écrire "11100010100000100001000001111101", nous pourrons écrire "ADD
R1,R2,\#125". Dans les 2 cas, la signification est identique :
"additionne le nombre 125 et la valeur située dans le registre R2,
range le résultat dans le registre R1".

## Assembler

Le processeur est uniquement capable d'interpréter le langage machine,
un programme appelé "assembleur" assure donc le passage de "ADD
R1,R2,\#125" à "11100010100000100001000001111101". Par extension, on
dit que l'on programme en assembleur quand on écrit des programmes avec
ces symboles mnémoniques à la place de suites de "0" et de "1".
Aujourd'hui plus personne n'écrit de programme directement en langage
machine, en revanche l'écriture de programme en assembleur est encore
chose relativement courante.

## Présentation d'un langage assembleur

Il n'est pas question d'apprendre à programmer en assembleur dans ce
cours, vous devez par contre être capable de suivre une série d'instruction
en langage machine.  Voici une brève présentation d'un langage assembleur.

    LDR R1,78


Place la valeur stockée à l'adresse mémoire 78 dans le registre R1

    STR R3,125


Place la valeur stockée dans le registre R3 en mémoire vive à l'adresse
125

    ADD R1,R0,#128


Additionne le nombre 128 (une valeur immédiate est identifiée grâce au
symbole \#) et la valeur stockée dans le registre R0, place le résultat
dans le registre R1

    ADD R0,R1,R2


Additionne la valeur stockée dans le registre R1 et la valeur stockée
dans le registre R2, place le résultat dans le registre R0

    SUB R1,R0,#128


Soustrait le nombre 128 de la valeur stockée dans le registre R0, place
le résultat dans le registre R1

    SUB R0,R1,R2


Soustrait la valeur stockée dans le registre R2 de la valeur stockée
dans le registre R1, place le résultat dans le registre R0

    MOV R1, #23


Place le nombre 23 dans le registre R1

    MOV R0, R3


Place la valeur stockée dans le registre R3 dans le registre R0

    B 45


Nous avons une structure de rupture de séquence, la prochaine
instruction à exécuter se situe en mémoire vive à l'adresse 45

    CMP R0, #23


Compare la valeur stockée dans le registre R0 et le nombre 23. Cette
instruction CMP doit précéder une instruction de branchement
conditionnel BEQ, BNE, BGT, BLT (voir ci-dessous)

    CMP R0, R1


Compare la valeur stockée dans le registre R0 et la valeur stockée dans
le registre R1.

    CMP R0, #23
    BEQ 78


La prochaine instruction à exécuter se situe à l'adresse mémoire 78 si
la valeur stockée dans le registre R0 est égale à 23

    CMP R0, #23
    BNE 78


La prochaine instruction à exécuter se situe à l'adresse mémoire 78 si
la valeur stockée dans le registre R0 n'est pas égale à 23

    CMP R0, #23
    BGT 78


La prochaine instruction à exécuter se situe à l'adresse mémoire 78 si
la valeur stockée dans le registre R0 est plus grand que 23

    CMP R0, #23
    BLT 78


La prochaine instruction à exécuter se situe à l'adresse mémoire 78 si
la valeur stockée dans le registre R0 est plus petit que 23

    HALT


Arrête l'exécution du programme

---

### À faire vous-même 2

Expliquez brièvement (sur le même modèle que les exemples ci-dessus),
les instructions suivantes :

    ADD R0, R1, #42


    LDR R5,98


    CMP R4, #18
    BGT 77


    STR R0,15


    B 100


------------------------------------------------------------------------

### À faire vous-même 3

Écrire les instructions en assembleur correspondant aux phrases
suivantes :

-   Additionne la valeur stockée dans le registre R0 et la valeur
    stockée dans le registre R1, le résultat est stocké dans le registre
    R5
-   Place la valeur stockée à l'adresse mémoire 878 dans le registre R0
-   Place le contenu du registre R0 en mémoire vive à l'adresse 124
-   la prochaine instruction à exécuter se situe en mémoire vive à
    l'adresse 478
-   Si la valeur stockée dans le registre R0 est égale 42 alors la
    prochaine instruction à exécuter se situe à l'adresse mémoire 85

------------------------------------------------------------------------

En faite, les instructions assembleur B, BEQ, BNE, BGT et BLT
n'utilisent pas directement l'adresse mémoire de la prochaine
instruction à exécuter, mais des "labels". Un label correspond à une
adresse en mémoire vive (c'est l'assembleur qui fera la traduction
"label"-\>"adresse mémoire"). L'utilisation d'un label évite donc
d'avoir à manipuler des adresses mémoires en binaire ou en
hexadécimale. Voici un exemple qui montre comment utiliser un label :

       CMP R4, #18
       BGT monLabel
       MOV R0,#14
       HALT
    monLabel:
       MOV R0,#18
       HALT


Dans l'exemple ci-dessus, nous avons choisi "monLabel" comme nom de
label. La ligne "MOV R0,\#18" a pour label "monLabel" car elle est
située juste après la ligne "monLabel:". Concrètement, voici ce qui se
passe avec ce programme : si la valeur stockée dans le registre R4 est
supérieure à 18 on place le nombre 18 dans le registre R0 sinon on place
le nombre 14 dans le registre R0. ATTENTION : la présence du "HALT"
juste après la ligne "MOV R0,\#14" est indispensable, car sinon, la
ligne "MOV R0,\#18" sera aussi exécutée (même si la valeur stockée
dans le registre R4 est inférieure à 18 )

### À faire vous-même 4

Voici un programme Python très simple :

    x = 4
    y = 8
    if x == 10:
        y = 9
    else :
        x=x+1
    z=6


et voici maintenant voici son équivalent en assembleur :

       MOV R0, #4
       STR R0,30
       MOV R0, #8
       STR R0,75
       LDR R0,30
       CMP R0, #10
       BNE else
       MOV R0, #9
       STR R0,75
       B endif
    else:
       LDR R0,30
       ADD R0, R0, #1
       STR R0,30
    endif:
       MOV R0, #6
       STR R0,23
       HALT


Après avoir analysé très attentivement le programme en assembleur
ci-dessus, vous essaierez d'établir une correspondance entre les lignes
du programme en Python et les lignes du programme en assembleur. À quoi
sert la ligne "B endif" ? À quoi correspondent les adresses mémoires
23, 75 et 30 ?

## Architecture de von Neumann : la mémoire partagée

Comme vous avez pu le constater dans les exemples ci-dessus, les données
et les instructions sont stockées en mémoire vive (il n'y a pas une mémoire
pour les instructions et une mémoire différente pour les données).

C'est John von Neumann (mathématicien et physicien américano-hongrois
1903-1957) qui a eu l'idée en 1945 d'utiliser une structure de
stockage unique pour les données et les instructions, voilà pourquoi on
parle d'architecture de von Neumann. Encore aujourd'hui, tous les
ordinateurs fonctionnent sur ce principe défini par von Neumann.
