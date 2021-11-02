---
author: qu3nt1n
date: 2016-07-02 11:07:28+00:00
draft: false
title: '4.bis : La programmation récursive'
bookCollapseSection: true
weight: 6
---

# 1. Principe et exemples


Les algorithmes récursifs et les fonctions récursives sont fondamentaux en informatique. Un algorithme est dit récursif s'il s'appelle lui-même.

On oppose généralement les algorithmes récursifs aux algorithmes dits impératifs ou itératifs qui s'exécutent sans invoquer ou appeler explicitement l'algorithme lui-même.

Prenons un exemple issu des mathématiques, celui de la factorielle. Celle-ci se définit intuitivement pour des entiers positifs par la fonction suivante :

$$n! = 1 \times 2 \times ... (n-1) \times n.$$

L'idée de la récursivité est d'utiliser une définition équivalente, à savoir une suite récurrente :

$n!=1$ si $n=0$ ou $1$, sinon $n!=n \times (n-1)!$






Vérifiez sur $n=1,2,3,4$ que les deux définitions sont équivalentes.


En récursif, la factorielle peut se traduire par le programme suivant en pseudo-code :


    factorielle(entier k) :
    si k=0
    alors renvoyer 1
    sinon renvoyer k * factorielle(k-1)
    finsi






Analysez les deux exemples qui suivent ligne par ligne puis testez les. Dans cet ordre !



**Exemple 1** :

~~~javascript
  function factorial(num)
  {
      // si le nombre est négatif, le rejeter.
      if (num < 0) {
          return -1;
        }
        // Si le nombre est 0 sa factorielle est 1.
        else if (num == 0) {
          return 1;
        }
        // Sinon n! = n * (n-1)!.

        var tmp = num;
        while (num-- > 2) {
          tmp *= num;
        }
        return tmp;
      }

      var result = factorial(8);
      document.write(result);

      // Sortie : 40320
~~~

**Exemple 2**. On peut transformer la fonction pour la rendre recursive très simplement. Au lieu d'utiliser une boucle while pour calculer la valeur, on peut se contenter d'appeler "factorial" à nouveau.


~~~javascript
function factorial(num)
{
    // si le nombre est négatif, le rejetter.
    if (num < 0) {
        return -1;
    }
    // Si le nombre est 0 sa factorielle est 1.
    else if (num == 0) {
        return 1;
    }
    // Sinon, appeler cette fonction recursive à nouveau.
    else {
        return (num * factorial(num - 1));
    }
}

var result = factorial(8);
document.write(result);

// Sortie : 40320
~~~





Testez ces fonctions sur quelques exemples : 0, 1, 2, 5, 12.

Attention : $2! = 479~001~600$




Il est important de remarquer qu'un algorithme récursif peut très bien ne pas s'arrêter.

Par exemple dans le calcul des factorielles, un mauvais argument en entrée renvoie une infinté de calculs !

$(-1)! = (-1)\times(-2)\times(-3)\times(-4)...$ et le calcul est infini !

Il est donc important de tester les fonctions récursives de manière précise avant de lancer la machine. Une mauvaise programmation entrainera toujours un plantage. Javascript n'affichera alors qu'une page blanche ou un espace vide à la place du calcul attendu.


# D'autres exemples simples.




## Calcul des puissances : $7^3 = 7 \times 7 \times 7 = 343$.


Le calcul des puissances d'un entier peut se traiter de manière récursive.

$$7^3 = 7 \times (7^2) = 7 \times (7 \times (7^1) = 7 \times (7 \times (7 \times (7^0)))$$

Ce qui peut s'intérpréter par une fonction f prenant 2 variables n et p et renvoyant n^p.

$f(n, p)=1$ si $p=0$, sinon $f(n,p) = n \times f(n, p-1)$




Ecrire deux algorithmes en pseudo code sur le drive permettant de calculer n^p des façons suivantes :



1. Avec une boucle while.
2. En récursif.
3. Programmer les algorithme en JavaScript dans de nouveaux fichiers : puissance-while.html et puissance-recursive.html
4. Commenter toutes les lignes de votre code afin de le rendre lisible par un camarade. Cette question sera fortement évaluée !!!






## L'algorithme d'Euclide


Le PGCD (Plus Grand Commun Diviseur)

Exemple : cherchons le pgcd de 24 et 36

Les diviseurs de 24 sont : 1, 2, 3, 4, 6, 8, 12 et 24

Les diviseurs de 36 sont : 1, 2, 3, 4, 6, 9, 12, 18 et 36

24 et 36 ont pour diviseurs communs: 1, 2, 3, 4, 6 et 12

Le plus grand d'entre eux est 12

12 est le pgcd de 24 et de 36. On écrit pgcd(24, 36)=12
L'algorithme d' Euclide permet de déterminer le pgcd de la manière suivante :

* pgcd(a, a) = a,
* pgcd(a, b) = pgcd(a − b, b) si a > b ou pgcd(a, b − a) si a


Programmez l'algorithme d'Euclide de façon récursive en suivant les étapes respectées lors de la manip précédente : papier, drive, javascript.


NB : une autre méthode pour calculer l'algorithme d'Euclide est l'opérateur modulo "%" (le reste de la division euclidienne de a par b si b < a ou de b par a sinon.

pgcd (a,b) = b si a%b == 0 , ou sinon (a%b) % b ;

**Solution :**

~~~javascript
function pgcd(a,b){
return  a>b && pgcd(a-b, b)|| a< b && pgcd(a,b-a) || a===b && a ; } //Et avec l'opérateur modulo : function pgcd(a,b){ return a>b && a%b>0 && pgcd(b,a%b) || (b>a)&& pgcd(b,a) || a%b===0 && b ;
}
pgcd(2736,486144);//30
~~~


Ici on utilise volontairement les expressions javascript pour raccourcir l'écriture, ce qui n'est pas forcément toujours à conseiller.


# 2. Exercices


Ils sont presque tous corrigés ! Indispensable étant donné que je ne pourrais pas être partout à la fois et que les solutions sont très faciles d'accès sur internet. La tentation serait trop grande de toute manière.

Néanmoins il est indispensable de s'initier sérieusement à l'algorithmique afin d'être à l'aise dans vos projets.

Aussi, faîtes les sérieusement.

Voici une liste de quelques exercices illustrant la notion de fonction recursive. Presque tous sont faisables "directement", c'est à dire en n'employant que des boucles, des tests et des affectations.

Cependant la plupart d'entre eux seront plus faciles et plus concis en recursif.

Ces exercices illustrent aussi des pièges et des difficultés.




Les exercices ne sont pas obligatoires. Ils peuvent constituer un travail supplémentaire si vous le souhaitez. Si cela vous intéresse et que vous souhaitez le faire, écrivez-moi un mail après avoir déposé vos travaux dans votre dossier google drive.

Vous répondrez donc à chaque exercice par un fichier individuel (ou avec le nom de chacun d'entre vous) sur le drive. Vous vous assurerez du partage de chacun de ces fichiers.






### Exercice 1 : Le nombre de chiffres.


L'objectif est de créer une fonction récursive en JavaScript qui calcule le nombre de chiffres d'un entier :

nchiffres(123456789) renvoie 9.






1. Etudier la fonction suivante qui répond au problème MAIS n'utilise pas de récursif :

~~~JavaScript
function nchiffres(n) {
var p=1
while(n>1){
  p++;
  n=Math.floor(n/10);
}
return p;
}

document.write(nchiffres(123456));
~~~



2. Créer une nouvelle fonction sur le même principe en utilisant le JavaScript.






### Exercice 2 : La liste des chiffres d'un nombre.


Dans javascript un nombre est un nombre et sa liste de chiffres demande un peu de travail pour être obtenue.

Partir d'un entier défini par n=123456789 et aboutir à la liste l=[1,2,3,4,5,6,7,8,9]

C'est un exercice indispensable pour la suite étant donné que les variables obtenues dans la pratique n'ont pas toujours le bon format.






1. Créer une fonction NON RECURSIVE à l'aide d'une boucle "for" en JavaScript qui prend un nombre en variable et renvoie sa liste de chiffre dans un tableau.
`chiffres(123456789)` renvoie `[1,2,3,4,5,6,7,8,9]`.
2. Tester le script suivant :

~~~javascript
var n =  123456789;
var digits = (123456789).toString(10).split("");
~~~


Il a pour inconvénient de renvoyer un tableau contenant des chaines de caractères et non des nombres. C'est facheux.
3. Voilà pourquoi je vous propose de tester cette fonction :

~~~javascript
var n =  123456789;
var digits2 = (123456789).toString(10).split("").map(function(t){return parseInt(t)});;
~~~


Testez ces deux fonctions et réalisez des calculs sur les éléments de la liste du type
 `digits[0] + digits[1]` qui renvoie la somme des deux premiers éléments de la liste.

Attention la liste est numérotée à partir de 0 en JavaScript !

Reprendre ce test avec la nouvelle fonction afin de comparer le résultat.

Que s'est il passé ?






### Exercice 3 : La somme de ces mêmes chiffres.






Créer une fonction récursive en JavaScript qui calcule la somme des chiffres d'un nombre entier et recommence jusqu'à obtenir un nombre entre 1 et 9.

sommechiffres( 685977856 ) donne 6+8+5+9+7+7+8+5+6 = 61 puis 6+1 = 7.

La fonction doit réaliser tous les calculs en une seule fois, en n'étant appelée qu'une seule fois.

Tester cette fonction sur de grandes valeurs.






# Exercice 4 : Les tours de Hanoi


![](http://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Tower_of_Hanoi.jpeg/300px-Tower_of_Hanoi.jpeg)


Voici (enfin) l'incontournable problème qui illustre la récursivité, ce problème a été inventé au début du siècle par un mathématicien français afin d'illustrer la résolution d'un problème par récursivité.

Attention, essayez de comprendre ce problème et sa solution... c'est un problème fondamental.

Dans un temple bouddhiste, à Hanoi 3 mâts sont disposés en ligne l'un à côté de l'autre. Sur le mât de gauche sont empilés des disques d'or très lourds, percés au centre, de diamètre variable, et ordonnés du plus grand au plus petit.

Un moine est chargé de transférer ces disques sur le troisième piquet à droite, avec cependant un impératif: il ne doit jamais déposer un disque d'un diamètre supérieur aux disques précédents sur un mât donné.

La légende dit que la fin du monde surviendra lorsque le moine aura terminé son travail...

Pouvez vous programmer un mode d'emploi pour aider notre moine dans sa tache interminable ? Il faut écrire un programme qui donne

hanoi( ndisques, "gauche", "droite", "milieu")

qui permet à notre moine de savoir de transférer ndisques de gauche à droite, en s'aidant du mât du milieu .


##### Résumé des règles du problème :


Le problème des tours de Hanoï consiste à déplacer des disques de diamètres différents d'une tour de « départ » à une tour d'« arrivée » en passant par une tour « intermédiaire », et ceci en un minimum de coups, tout en respectant les règles suivantes :



 	  * on ne peut déplacer plus d'un disque à la fois,
 	  * on ne peut placer un disque que sur un autre disque plus grand que lui ou sur un emplacement vide.

On suppose que cette dernière règle est également respectée dans la configuration de départ.

Réponse:

![](http://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Tower_of_Hanoi_4.gif/300px-Tower_of_Hanoi_4.gif)


Le principe de récurrence dit que si vous pouvez le faire pour 1 élément et si vous savez passer de l'élément n à n-1 alors vous savez résoudre le problème ! ....

Ainsi on suppose que vous savez passer une colonne de n-1 disques de gauche au milieu ou à droite.. comment passer une colonne de n disques de gauche à droite :

passer une colonne entière de n-1 disques de gauche au milieu, // vous prétendez que vous savez le faire
passer le disque large de la base de gauche à droite // vous savez le faire pour de bon !

puis repasser la colonne de n-1 disques du milieu à gauche... // vous prétendez savoir le faire






1. Réaliser un dessin papier des trois tours avec seulement 2 disques.Ecrire la liste des manipulation : Faire passer le disque de gauche à droite etc. conduisant à une solution
2. Reprendre la démarche avec 3 disques. On pourra s’entraîner avec [cette animation flash](http://proficio.free.fr/AP/tour%20de%20Hanoi.htm)
3. Programmer la solution en JavaScript.

C'est l'exercice le plus difficile.




[corrections](/uploads/docs/doc04b/corrections.zip)
