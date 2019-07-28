---
author: qu3nt1n
date: 2016-07-02 11:40:10+00:00
draft: false
title: 6. Architecture
weight: 8

---










Il s'agit d'une fiche-enseignant et non d'une fiche-élève.







Notions abordées



* introduction au langage assembleur


[AMIL](http://www-lipn.univ-paris13.fr/~boudes/spip.php?rubrique27) (Assembleur Miniature pour l'Informatique de Licence) est un programme développé par Pierre Boudes
simulant l'exécution de programmes écrits en assembleur.



* La version Web est disponible [ici](http://www-lipn.univ-paris13.fr/~boudes/amilweb/)
* Didier Mailliet a enrichi le jeu d'instructions. Sa version est disponible [ici](http://www2.lifl.fr/~mailliet/isn/archi/amil)
* Il existe aussi une version [téléchargeable](http://www2.lifl.fr/~mailliet/isn/archi/amil/amilweb.zip) de cette version améliorée.


Jean-François Przydatek a rédigé un cours d'initiation à l'assembleur dont on a un aperçu ci-dessous

et que l'on peut télécharger :


* [au format powerpoint(pptx)](http://qkzk.xyz/docs/doc06/transparents/ARCHI.pptx)
* [au format libreOffice ou openOffice(odp)](http://qkzk.xyz/docs/doc06/transparents/ARCHI.odp)
* [au format pdf](http://qkzk.xyz/docs/doc06/transparents/ARCHI.pdf)

ainsi qu'une [série d'exercices](http://qkzk.xyz/docs/doc06/transparents/ARCHI_exos.pptx).
Ce document est conçu comme un accompagnement de cette série
d'exercices.









#  Exercice 1





Ecrire un programme qui lit un nombre en entrée et le restitue en sortie.






    lecture 4 r0
    ecriture r0 5
    stop
    12
    ?






##  Explications






Les cases mémoires sont numérotées à partir de 1.







* On lit le contenu de la case mémoire 4 (contenant la valeur 12), pour la ranger dans le registre r0.
* On écrit le contenu du registre r0 dans la case mémoire 5






# Exercice 2





Lire dans l'ordre les valeurs de a,b et x, calculer et ranger en mémoire y=ax+b







    lecture 10 r0
    lecture 8 r1
    mult r1 r0
    lecture 9 r1
    add r1 r0
    ecriture r0 11
    stop
    2
    5
    3
    ?






# Exercice 3








* Soit x une valeur écrite dans la case mémoire 12 (dans l'exemple : x=3).
* Lire le nombre rangé dans la case mémoire 10.
* Si ce nombre est plus grand ou égal à x, remplacer le contenu de la case 12 par ce nombre.







    lecture 10 r0
    lecture 12 r1
    soustr r0 r1
    sautpos r1 6
    ecriture r0 12
    stop
    ?
    ?
    ?
    4
    ?
    3








* On lit le contenu des cases mémoires 10 et 12, et on les range respectivement dans les registres r0 et r1.


la plupart des instructions vont chercher leurs opérandes dans les registres, et pas dans la mémoire : gain de temps (les accès mémoire
sont coûteux, et les instructions sont plus faciles à décoder par le système)
* On soustrait le contenu de r0 au contenu de r1, puis on range le résultat dans r1.
* Si le contenu de r1 est positif (i.e. x est plus grand que le nombre rangé à la case mémoire 10), on saute directement à la ligne 6,
et le programme s'arrête.
* Sinon (x est plus petit que le contenu de la case mémoire 10), on effectue l'instruction de la ligne 5, et dont le contenu de r0,
qui est le nombre rpésent à la ligne 10, est rangé à la ligne 12.





# Exercice 4_1





Même exercice que le précédent, mais maintenant, on écrit dans la case mémoire 12 :



* 0 si le contenu de la case 10 est inférieur à celui de la case mémoire 12
* 1 sinon.







    valeur 0 r2
    lecture 10 r0
    lecture 12 r1
    soustr r0 r1
    sautpos r1 7
    valeur 1 r2
    ecriture r2 12
    stop
    ?
    4
    ?
    3






Le programme ressemble très fort au programme précédent, mais celui n'est pas utilisable directement : le fait d'avoir introduit
une ligne supplémentaire au début nous oblige à changer, dans l'instruction sautpos, le 6 en 7. On rencontre souvent
ce problème en assembleur. On le résout en introduisant des étiquettes (ou labels), qui seront transformées en vrais
numéros de ligne par le programme qui interprétera l'assembleur,
lors d'une première lecture du code






Le registre r2 contient la valeur qui sera écrite dans la case 12. Cette écriture est faite à l'instruction de la ligne 7. Avant d'arriver à cette instruction, on effectue le même travail (soustraction et test) que dans l'exercice précédent.
On teste le signe de la soustraction, ce qui peut amener à changer le 0 en 1 dans r2 avant d'écrire le contenu de r2 en mémoire.






# Exercice 4_2







pas compris









    valeur 0 r2
    lecture 10 r0
    lecture 12 r1
    soustr r0 r1
    sautnul r1 7
    sautpos r1 8
    valeur 1 r2
    ecriture r2 12
    stop
    3
    ?
    3






# Exercice 5








* On fixe i, l'adresse mémoire du début d'un tableau. Ce tableau, de longueur inconnue,
contient une suite de nombres positifs terminée par un nombre négatif.
* Ecrire un programme qui recopie chaque valeur du tableau (sauf le nombre négatif) à un autre endroit de la mémoire.







    valeur 20 r0
    valeur 30 r1
    lecture *r0 r2
    sautpos r2 6
    saut 11
    lecture *r0 r3
    ecriture r3 *r1
    add 1 r0
    add 1 r1
    saut 3
    stop
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    12
    5
    15
    6
    85
    -1







Cet exercice illustre le fonctionnement de la boucle `tant que`: exécuter une instruction
tant que la condition d'arrêt n'est pas vérifiée (ici : lecture d'un nombre négatif), et sa traduction en assembleur. On montre ainsi
qu'une structure de contrôle basique de tout langage de programmation évolué se traduit en assembleur par une combinaison de
tests élémentaires (`sautpos` qui teste le signe du contenu d'un registre) et de sauts.




Point 2 : on voit ici une limite de ce programme : on ne sait pas à l'avance si notre tableau, commençant
à la ligne 20, contient plus ou moins de 10 éléments !




Point 5  : est-ce qu'on aurait pu raccourcir
un tout petit peu ce programme ?






1. Dans cet exemple, le tableau commence à la ligne (ou adresse mémoire) 20, et contient les valeurs
12,5,15,6,85.
2. Il sera recopié à partir de l'adresse 30.

3. Les deux premières instructions initialisent l'adresse de départ du tableau, et l'adresse de début de sa copie.
4. La ligne 3 est une instruction contenant un adressage indirect : ce n'est pas le contenu de r0 (20) qui est copié dans r2,
mais le contenu de l'adresse mémoire contenue dans r0, donc la valeur qui se trouve à la ligne 20 (12).
5. Si la valeur rangée dans r2 est positive, on passe à la ligne 6, où la valeur (12 au premier passage) est chargée
dans r3, puis, par l'intermédiaire d'un deuxième adressage indirect, est recopiée à la ligne 30 (on considère le contenu
de r1 comme une adresse mémoire)
6. On ajoute 1 à r0 et r1, qui représentent maintenant les adresses mémoire 21 et 31
7. On revient au début du programme pour traiter la case suivante du tableau.
8. La ligne 5 est exécutée quand la valeur lue est négative, et mène à la fin du programme, ligne 11.






# Exercice 6





Ecrire le même programme que dans l'exercice précédent, mais cette fois, l'indice de fin est connu.






    valeur 20 r0
    valeur 24 r4
    soustr r0 r4
    add 1 r4
    valeur 30 r1
    sautnul r4 13
    lecture *r0 r3
    ecriture r3 *r1
    add 1 r0
    add 1 r1
    soustr 1 r4
    saut 6
    stop
    ?
    ?
    ?
    ?
    ?
    ?
    12
    5
    15
    6
    85






# Exercice 7 : echange





mettre 2 valeurs dans r0 et r1 et échanger leur valeurs en se servant de r2 , puis  en se servant de la mémoire au lieu de r2, puis de la pile.
Echanger 2 valeurs en mémoire sans transférer ces valeurs dans les registres (r0 et r1) mais grâce à leurs adresses.
Refaire les mêmes exercices, mais n’échangez que si la première valeur est supérieure à la seconde.












# Exercice 8 : tri





Écrire un programme de tri à bulles effectuant le résultat suivant :






# Exercice 9 : modulo





Écrire un programme lisant deux nombres a et b, remplaçant a par b dans le cas où a < b et retournant a, b et a mod b (reste de la division entière de a par b).






# Exercice 10 : pgcd





Écrire un programme qui retourne le PGCD de 2 nombres (Algorithme d'Euclide).
![algorithme  d'Euclide](http://qkzk.xyz/docs/doc06/pgcd.png)







    lecture 15 r1
    lecture 16 r2
    sautnul r2 13
    lecture r1 r0
    lecture r2 r1
    lecture r0 r3
    div r1 r3
    mult r1 r3
    lecture r0 r2
    inverse r3
    add r3 r2
    saut 3
    ecriture r1 17
    stop
    168
    20
    ?






# Exercice 11 : ppcm


Sachant que PGCD(a,b)*PPCM(a,b)=a*b, écrire un programme (ou ajouter au pg précédent) qui rend le PPCM de 2 nbs a et b.









    lecture 20 r1
    lecture 21 r2
    sautnul r2 13
    lecture r1 r0
    lecture r2 r1
    lecture r0 r3
    div r1 r3
    mult r1 r3
    lecture r0 r2
    inverse r3
    add r3 r2
    saut 3
    ecriture r1 22
    lecture 20 r0
    div r0 r1
    lecture 21 r1
    mult r1 r0
    ecriture r0 23
    stop
    168
    20
    ?
    ?







# Exercice 12 : sous-programmes





Écrire un programme comprenant un sous programme capable de retourner y=2x+3. Essayez-le avec au moins 3 valeurs de x que vous lirez en intercalant une série aléatoire de « noop ».






# Exercice 13 : factorielle





Écrire un programme calculant n! (n étant donné en mémoire) par la méthode récursive.






    valeur 23 r7
    saut 9
    sautnonnul r0 5
    retour
    mult r0 r1
    soustr 1 r0
    appel 3
    retour
    lecture 14 r0
    valeur 1 r1
    appel 3
    ecriture r1 15
    stop
    5
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?






# Exercice 14 : remplissage mémoire (1)





Écrire un programme qui partant de trois données entrées en mémoire (v, d, l) va mettre v en mémoire à partir de l'adresse d et ce pour l adresses consécutives.






# Exercice 15 : remplissage mémoire(2)





Écrire un programme qui partant de trois données entrées en mémoire (v, d, l) va mettre 1 en mémoire à partir de l'adresse d et ce pour l adresses consécutives.
mettre 0 dans les adresses en d+2v,d+3v...d+iv.





# Exercice 16 : Eratostene





En se servant des 2 exercices précédents, programmer le crible d'Eratostène.
![algorithme Crible Eratostene](http://www.fil.univ-lille1.fr/~wegrzyno/portail/API1/Doc/TP/TP-Tableaux/New_Animation_Sieve_of_Eratosthenes.gif)

Le crible d’Eratosthene
Eratosthene , mathématicien grec du IIIème siècle avant JC, a établi une méthode connue sous le nom de crible d’Eratosthene permettant de déterminer par exclusion tous les nombres premiers.
Cette méthode consiste à lister tous les nombres entiers depuis 2 jusqu’à une valeur limite n que l’on se fixe, puis à barrer successivement ces nombres


L’algorithme procède par élimination : il s’agit de supprimer d’une table tous les multiples des entiers de 2 à n, n étant un entier que l’on se fixe.


On commence par les multiples de 2, puis à chaque fois on raye les multiples du plus petit entier restant jusqu’à ce que le carré de celui-ci soit supérieur au plus grand entier de la liste.


On peut s’arrêter lorsque le carré du plus petit entier est supérieur au plus grand entier, car dans ce cas, s’il existait des non-premiers, ils auraient déjà été rayés précédemment.


À la fin du processus, tous les entiers qui n’ont pas été rayés sont les nombres premiers inférieurs à n.







    lecture 28 r0 	# ad de début données : contient l'entier 0
    lecture 29 r1 	# nombres de valeurs à traiter : n (on traite les entiers de 0 à n)
    add 2 r0	# les entiers 0 et 1 sont déja traités ( 0 aux adresses 30 et 31), on commence à 2
    valeur 1 r2	# aucun entier entre 2 à n n'est encore barré
    ecriture r2 *r0	# on met 1 à l'adresse contenue dans r0
    add 1 r0	# on passe à l'entier suivant
    soustr 1 r1	# il y en a un de moins à traiter
    sautnonnul r1 5 # après cette boucle le tableau est rempli de 1
    valeur 0 r2	# pour "barrer" le multiple recopie de r2(=0) à l'adresse contenant un nombre à barrer
    valeur 0 r3	# on commence avec le nombre 0
    lecture 28 r0	# il est rangé à l'adresse que l'on copie dans r0
    lecture 29 r1	# indice du dernier nombre à traiter
    add 1 r0	# on passe à l'adresse suivante
    add 1 r3	# et donc au nombre suivant
    lecture *r0 r4 	# ce nombre est-il barré ?
    sautnul r4 13	# après cette boucle r0 contient l'adresse du prochain élé ment non barré
    ecriture r0 28	# on remplace à cette ad. le nombre précédemment traité par celui qu'on vient de trouver
    add r3 r0	# on va barrer ses multiples (mais pas lui)
    soustr r3 r1	# on décrémente d'autant le nombres de valeurs à traiter
    ecriture r2 *r0 # on barre la valeur contenue à l'adresse indexée par r0
    sautpos r1 18	# A-t-on tout traité les multiples?
    lecture 29 r5	# Est-on arrivé à la rac. carrée? dans le tab. de 0 à n, on vient de barrer les mult. de i
    div r3 r5	# au lieu de tester si i>racine(n)  on arrête
    div r3 r5	# on teste
    soustr 1 r5	# (n/i²-1)>=0
    sautpos r5 11	# et dans ce cas, on recommence
    stop
    30	# mémorise le dernier nombre dont on a barré les multiples
    20	# taille de la table
    0	# 0 n'est pas premier
    0	# 1 non plus
    ?	# i est en mémoire 30+i
    ?	# un réro à l'emplacement i indiquera que i n'est pas premier
    ?	# un 1 ==> i est premier
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?
    ?	# prévoir quelques adresses supplémentaires
    ?	# pour pouvoir déborder du tableau
    ?	# pouvoir déborder simplifie le code
    ?
