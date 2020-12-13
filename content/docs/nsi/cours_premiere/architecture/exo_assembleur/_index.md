---
title: "Exercice - modèle de Von Neumann, assembleur"
weight: 100

---

## Cours sur le modèle de Von Neumann

1. Dessiner _de mémoire_ le schéma du modèle de Von Neumann. Nommer correctement tous les éléments.
2. Attribuer à chaque élément les descriptions suivantes :

    * Ensemble de cellules où sont conservées les données. Elles sont accessibles par des adresses.
    * Liaisions physiques servant à la circulation des informations.
    * Unité servant à choisir les instructions réalisées et réalisant les embranchements qui correspondent à ces instructions.
    * Unité où sont réalisés les différents calculs mathématiques.
3. Un processeur moderne travaille par cycles qui comportent trois étapes. Lesquelles ?
4. On classe les mémoires d'un ordinateur par vitesse croissante. Triez les exemples suivants :

    RAM, Disque dur, registre, mémoire cache.
5. Parmi les exemples précédents, quelles sont les mémoires _volatiles_ (dont le contenu est perdu une fois la machine éteinte) ?
6. Citez en une phrase la loi de Moore. Est-elle toujours d'actualité ?


## Assembleur et modèle de Von Neumann

**Attention !** La machine présentée ci-dessous n'est pas la machine AQA avec laquelle nous avons travaillé !!!

Soit une machine basée sur une architecture de Von Neumann, disposant d'un Accumulateur et du jeu d'instructions suivant :

_Remarque_ : `//` désigne un commentaire, tous les nombres sont écrits en décimaux.

Dans cette machine il n'y a qu'un registre : l'accumulateur.
Tous les résultats des opérations arithmétiques (addition, soustraction) sont
conservés dans l'accumulateur.

~~~
LDA xx  //LoaD address (xx) in Accumulator
        //charge le contenu de la mémoire (xx) dans l'accumulateur
STA xx  //STore Accumulator value at address xx
        //enregistre la valeur de l'accumulateur en mémoire
ADD xx  //ADD (xx) to accumulator value
        //ajouter (xx) à la valeur de l'accumulateur
SUB xx  //SUBstract (xx) from accumulator value
        //soustraie (xx) à la valeur de l'accumulateur
BRZ xx  //BRanch to the instruction at address xx if Accumulator value equal Zero
        //Saute à l'instruction à l'adresse xx si l'accumulateur vaut 0
BRP xx  //BRanch to the instruction at address xx if Accumulator value is Positive (or zero)
        //Saute à l'instruction à l'adresse xx si l'accumulateur est positif ou nul
BRA xx  //BRanch Always to the instruction at address xx
        //Saute toujours à l'instruction à l'adresse xx
END     //Stop program
        //Arrête le programme
~~~

où xx représente une adresse mémoire et (xx) son contenu.

**Programme 1 : exemple**

~~~
01 LDA 07
02 SUB 08
03 LDA 08
04 ADD 07
05 SUB 09
06 END
07 1
08 10
09 2
~~~

Le tableau ci-dessous présente les valeurs de l'accumulateur à chaque étape.

1. Suivre le déroulé de l'exemple ci-dessous. Le refaire à partir d'un tableau vide.
2. Recommencer en remplaçant les valeurs respectives des lignes 07, 08 et 09 par 5, 2 et 9.


| Ligne 	| Accumulateur 	| Remarque                                                 	|
|-------	|:------------:	|----------------------------------------------------------	|
| 1     	| 1            	| On charge le nombre 1 dans l'Acc.                        	|
| 2     	| -9           	| On soustraie le nombre 10 à la valeur de l'Acc.          	|
| 3     	| 10           	| On charge le nombre 10 (la précédente valeur est perdue) 	|
| 4     	| 11           	| On ajoute le nombre 1 à l'Acc.                           	|
| 5     	| 9            	| On soustraie le nombre 2 à l'Acc.                        	|
| 6     	| 9            	| END : fin du programme, l'accumulateur contient 9        	|

**Programme 2 : test de parité**

1. Que contient l'accumulateur une fois le programme ci-dessous exécuté ?
2. Remplacer le contenu de la mémoire 11 par le nombre 6 et recommencer le programme.
3. Expliquer en quoi ce programme est un test _de parité_.

~~~
01 LDA 11
02 BRZ 09
03 SUB 12
04 BRP 02
05 B 09
06 END
07 LDA 13
08 END
09 LDA 14
10 END
11 7
12 2
13 0
14 1
~~~

\newpage

**Programme 2 : maximum**

1. Compléter le programme ci-dessous pour qu'il se termine en ayant dans
  l'accumulateur le plus grand des
  deux nombres enregistrés aux lignes 08 et 09 de la mémoire.

2. Faire tourner votre programme dans un tableau similaire à celui présenté pour le programme 1.

<!--
~~~
01 LDA 08
02 SUB 09
03 BRP 06
04 LDA 09
05 END
06 LDA 07
07 END
08 7
09 5
~~~
-->

~~~
01
02
03
04
05
06
07
08 7
09 5
~~~
