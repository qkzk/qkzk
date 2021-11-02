---
author: qu3nt1n
date: 2016-07-02 09:12:00+00:00
draft: false
title: 4.03 Types de données
bookCollapseSection: true
weight: 3
---

Notions abordées dans cette page  * types de données  * le type chaines de caractères  * spécification  * le type date

# Types

En Javascript, le type d'une variable peut changer, il suffit de lui affecter une valeur d'un type différent.
Dans un certain nombre de langages (C et java par exemple), les variables sont typées c'est-à-dire qu'au moment de sa déclaration on précise le type des valeurs autorisées pour cette variable et il n'est pas possible par la suite d'affecter à cette variable une valeur d'un autre type.
Ces langages sont qualifiés de **langage typé**.

Dans les exemples rencontrés jusque maintenant nous n'avons défini en Javascript que des variables dont la valeur était un nombre. Il est possible de manipuler des variables dont les valeurs sont autres que numériques : des textes, des images, des dates, des sons, etc. Comme cela a déjà été dit on parle alors de types des données. Les opérations qui peuvent être appliquées sur une variable diffèrent selon son type (c'est-à-dire, en Javascript, le type de la valeur à laquelle la variable est liée) .

Un type de données est défini par un ensemble de valeurs et les opérations qui s'appliquent sur ces valeurs.

## Les chaînes de caractères

**Codage** : faire/rappeler le lien entre caractères et nombres. Cf. table ASCII.

Un type de données fréquemment utilisé en programmation est le type chaîne de caractères car il permet la manipulation de données textuelles. Ce type est appelé `String` dans la quasi-totalité des langages de programmation, y compris Javascript. On abbréviera souvent la dénomination en **chaîne**.

La valeur d'une chaîne de caractères est constituée d'une séquence de caractères. Les valeurs sont représentées par la suite des caractères encadrée par des délimiteurs. Ces délimiteurs peuvent en Javascript être des apostrophes `'` ou des guillemets `"`, mais une chaîne commencée par un délimiteur se termine par le même. Les délimiteurs ne font pas partie de la chaîne.

Voici quelques exemples de valeurs possibles pour des chaînes de caractères :

    "ceci est une chaine de caractères"
    'ceci aussi'
    ""
    "0n peut !_Mettre_! d3s c@r@ctère5 quelc0nqueS !%$^"
    '1234'
    "Il faut le même délimiteur ' pour finir et commencer une chaîne "
    '   on peut avoir des espaces en début et en fin, l'espace est un caractère !   '

La **chaîne vide** est le cas particulier de la chaîne qui ne contient aucun caractère.

Certains langages distinguent le type _chaîne de caractères_ du type _caractère_ dont les valeurs se limitent à un seul caractère. Les opérations ne sont alors pas les mêmes sur les valeurs de type caractère ou celles de type chaînes de caractères.
En Javascript, comme dans d'autres langages, le type _caractère_ n'existe pas indépendamment. Pour représenter une telle valeur on utilise une chaîne dont la séquence ne contient qu'un seul caractère.

Définissez une page HTML qui définit une variable `langage` dont la valeur est la chaîne de caractères `"Javascript"` et qui contient le texte `J'apprends le javacript`. La modification de la valeur de la variable doit modifier le texte.

La présence dans la séquence des caractères qui constituent la chaîne d'un des caractères délimiteurs pose problème.
En définissant dans une page des variables de type chaine de caractères ayant les valeurs demandées et en les affichant, testez vos réponses aux questions suivantes :  1. Comment faire pour représenter une chaîne qui contient la séquence : _attention à l'apostrophe_ .  2. Comment faire pour représenter une chaîne qui contient la séquence : _attention égalemente aux "guillemets"_ .  3. Comment faire pour représenter une chaîne qui contient la séquence : _et s'il y a les deux "signes" dans le texte ?_ .

Dans ce dernier cas, une fois que l'on a choisi l'un ou l'autre délimiteur, si l'on veut que la chaîne puisse contenir le caractère correspondant, il faut _protéger_ celui-ci en le précédant d'un _backslash_ `\`.

Donnez deux écritures pour représenter une chaîne qui contient la séquence : _et s'il y a "les deux" signes ?_ .
Testez vos propositions.

Dans la mesure où l'on peut espérer une certaine cohérence dans la définition du langage, devinez comment représenter une chaîne qui contient la séquence : _le signe \ protège le caractère correspondant au délimiteur_ et testez votre proposition.

On souhaite écrire une page qui reprend le poème de Jacques Prévert extrait de "_Paroles_" intitulé "_Les belles familles_" mais avec la possibilité de pouvoir facilement créer des variantes en changeant le prénom.  1. Faites une recherche pour trouver le texte du poème.  2. Ecrivez une page HTML de telle manière qu'une seule modification permette de modifier le prénom répété.  3. Testez votre solution.

[poème initial](/uploads/docs/doc04/corrections/louis.html) - [ 1ère version avec variable](/uploads/docs/doc04/corrections/louis2.html) - [2nde version avec variable](/uploads/docs/doc04/corrections/louis2Bis.html) - Comparer les 2 versions.

## Quelques manipulations

Les opérations qui s'appliquent sur une donnée dépendent de ce type. Ainsi il est possible de faire sur des chaînes de caractères des manipulation qui n'ont pas de sens avec des nombres. Par exemple les chaînes de caractères dispose d'une propriété `length` qui permet d'obtenir la longueur d'une chaîne, c'est-à-dire le nombre de caractères qui la compose.

On avait déjà aperçu la notation pointée dans l'expression `document.writeln`. Nous aurons l'occasion de la rencontrer de nombreuses fois encore.

La syntaxe d'utilisation s'appuie sur une notation pointée : si `chaine` est une chaîne de caractère `chaine.length` est une expression dont la valeur est la longueur de `chaine`

Cette propriété n'a cependant aucun sens pour une donnée de type numérique.

Créez une page HTML dans laquelle sont définies deux variables, l'une de type chaîne de caractères, l'autre numérique et qui tente d'afficher la valeur de la propriété `length` pour chacune de ces variables.
Ques constatez-vous ?

Par ailleurs certaines opérations qui ont un sens sur les nombres en ont un autre avec les chaînes de caractères. C'est le cas de l'opérateur `+` dont la **sémantique** change selon le type des données auxquelles on l'applique.  1. Créez une page HTML dans laquelle sont définies deux variables `chaine1` et `chaine2` de type chaîne de caractères que vous initialiserez et qui affiche le résultat de l'expression `chaine1 + chaine2`.  2. Affichez la page plusieurs fois en changeant les valeurs d'initialisation des deux chaines.  3. Décrivez l'opération réalisée par l'opérateur `+` lorsque les opérandes sont des chaines de caractères  ?  4. Si cela n'a pas encore été fait, faites un test avec des chaines qui ne sont composées que de caractères correspondant à des chiffres. Cela change-t-il la description que vous venez de rédiger ?  5. En fonction des connaissances acquises comment peut-on vérifier que le type du résultat est de type chaîne de caractères ?

5 : en testant que la propriété `length` est définie sur le résultat.

Pour pouvoir utiliser correctement un élément mis à disposition par le langage, comme l'opérateur `+`, il est donc nécessaire d'en avoir une description précise, on parle de spécification.

Une spécification doit présenter toutes les informations qui permettent une utilisation précise en non ambigüe d'un élément. Elle en constitue dans une certaine manière la documentation de référence. C'est au programmeur qui a créé l'élément de rédiger cette spécification et à celui qui l'utilise de la consulter pour l'utiliser correctement. On a ainsi deux statuts du programmeur, celui qui crée l'élément et celui qui l'utilise dans un programme.

Par exemple, une spécification de l'opérateur `+` pour les nombres pourrait prendre la forme :

**nom** : +
**Opérandes** : 2
**  n1** : numérique
**  n2** : numérique
**Résultat**
**  type** : numérique
**  description** : la somme de n1 et n2

Une spécification bien rédigée doit permettre une utilisation sans surprise de l'élément spécifié.

Cherchez dans wikipedia la définition de **concaténation**, notamment en programmation puis proposez une spécification de l'opérateur `+` pour les chaînes.

La rédaction de spécification/documentation du travail qu'il réalise est une tâche importante et indispensable du travail du programmeur.
La lecture de spécifications/documentations écrites par d'autres programmeurs constitue une part importante du programmeur pour réaliser d'autres tâches.

## Identificateurs et chaines de caractères

Il est très important de bien faire la différence entre identificateurs des variables et chaînes de caractères. S'ils peuvent se ressembler dans leur forme  : une séquence de caractères, les chaînes de caractères se caractérisent par la présence des délimiteurs. Mais la différence principale réside dans ce que réprésente l'un ou l'autre et est notamment visible au niveau de leur évaluation. Ainsi une chaîne de caractères est une expression constante qui s'évalue en elle-même, sa valeur est donc... une chaîne de caractères. Alors qu'un identificateur de variable s'évalue en la valeur associée à la variable : un nombre, une couleur ou même une chaîne de caractères, mais de manière fortuite.

On considère la séquence de code suivante :

~~~javascript
var exemple = 42;

document.writeln("valeur de la variable exemple : ");
document.writeln(exemple);
document.writeln("<br></br>");

document.writeln('valeur de la chaine "exemple" : ');
document.writeln("exemple");
document.writeln("<br></br>");
~~~

1. Qu'affiche cette portion de code (si on la place dans la balise `script` au sein d'une page HTML).
2. Testez votre réponse en écrivant et visualisant une telle page.
3. Modifiez l'initialisation de la variable ainsi :

     var exemple = "un texte";

et reprenez les deux questions précédentes.

Attention, la confusion entre identificateur de variable et chaîne de caractères est une source d'erreur courante chez des débutants en programmation, en particulier lorsque la variable a une valeur de type chaîne.

## Le type Booleén

Nous avons eu l'occasion de découvrir le calcul booléen (TP 3). Les données à valeur booléennes jouent un rôle important en programmation, notamment pour les structures conditionnelles que nous découvrirons ultérieurement. Tous les langages de programmation proposent donc un type pour manipuler ces données.

On dit de l'opérateur de négation `!` qu'il est prefixe car il s'écrit avant son opérande. A l'inverse les opérateurs `&&` et `||` sont dits infixes car ils s'écrivent entre leurs deux opérandes. En mathématiques, l'opérateur de carré "²" est lui postfixe car il s'écrit après son opérande.

Cherchez d'autres exemples d'opérateurs préfixes ou postfixes, ne vous limitez pas aux mathématiques, il en existe en musique par exemple.

En javascript ce type s'appelle `Boolean` et les deux valeurs de ce type sont nommées `true` et `false`, et correspondent évidemment à VRAI et FALSE. Les opérateurs booléens NON, ET et OU se nomment `!`, `&&` et `||` en javascript.

Ainsi si _a_ et _b_ sont deux variables booléennes, les deux seules valeurs qu'elles peuvent prendre sont `true` ou `false` et les expressions suivantes sont valides :


~~~javascript
!a                  //  NON a, la négation de a
a && b              //  a ET b
a || b              //  a OU b
(a && b) || (!b)    //  (a ET b) OU (NON b)
~~~

Soient _a_ et _b_ sont deux variables booléennes, donnez une expression javascript permettant de calculer _a_ XOR _b_.

Ne compliquons pas mais sachez qu'il existe en javascript d'autres prédicats d'égalité, notamment pour prendre en compte le fait que le langage fait "automatiquement" certaines conversions.
Vous trouverez ainsi l'opérateur `===` (promis on s'arrête à 3 signes "="). Celui-ci vérifie en plus que le type des opérandes est le même et n'accepte donc pas les "conversions automatiques", contrairement à `==`.
Ainsi en javascript l'expression `1=="1"` a pour valeur `true` alors que `1==="1"` a pour valeur `false`.

On appelle prédicat les fonctions dont le résultat est un booléen. On trouve par exemple les prédicats d'égalité `==` et de comparaison `<` ou `>`. Ces opérateurs s'appliquent sur les nombres et les chaînes de caractères. Ainsi par exemple la spécification de `<` pour les chaînes de caractères est

**nom** : <

**Opérandes** : 2

**c1** : String

**c2** : String

**Résultat**

**type** : booléen

**description** : true si la chaîne c1 est avant la chaîne c2 dans l'ordre lexicographique (comme "alphabétique" mais élargi à tous les caractères) et false sinon

Soient _n_ un nombre, donnez une expression javascript qui vaille `true` si et seulement si  1. _n ≥ 42_ (proposez deux expressions équivalentes)  2. _n ≤ 0_
(_les prédicats `>=` et `<=` (≤) sont définis en javascript, vous pouvez les utiliser pour la suite de l'exercice._)  3. _n_ appartient à l'intervalle [5,12]  4. _n_ n'appartient pas à l'intervalle [5,12] (proposez deux expressions équivalentes)  5. _n_ appartient à l'intervalle [5,12]∪[24,44]

Attention à ne pas confondre l'opérateur d'affectation `=` et l'opérateur d'égalité `==`.

## Un autre type de données : les dates

Le type `Date` constitue un autre type de données. Dans les deux premiers types rencontrés, les nombres et les chaînes de caractères, les valeurs étaient définies par des constantes du langage : une suite de chiffres pour les premiers (`42`) ou une séquence de caractères entre délimiteurs pour les seconds (`"timoleon"`). Pour les valeurs du type `Date` comme pour beaucoup d'autes, il est nécessaire de _construire_ les valeurs. Cela s'explique par le fait que les dates sont des données _complexes_ au sens où elles sont elles-mêmes composées de plusieurs données : le jour, l'année, l'heure, etc.

Il existe plusieurs manières de construire une donnée `Date`. La première permet de récupérer la valeur de la date (et l'heure) de l'ordinateur sur lequel fonctionne le navigateur, ainsi :

     var maintenant = new Date();


Après l'avoir définie, affichez la valeur de la variable `maintenant`.

Recherchez le pourquoi de ce _1er janvier 1970_.
Cherchez des informations sur "_le bug de l'année 2038_".
Ce problème se posera-t-il pour Javascript et votre navigateur ?

Si l'on souhaite obtenir une date spécifique, il "suffit" de préciser le nombre de millisecondes écoulées depuis le 1er janvier 1970 à 12h00mn00sec :

    var uneDate = new Date(1339000000000);

1. Après l'avoir définie, affichez la valeur de la variable `uneDate`.
2. Définissez par cette méthode la date correspondant au début de la séance d'aujourd'hui puis affichez-la pour vérification.

En informatique, il est habituel de commencer les numérotations à 0.

Une autre façon de procéder, sans doute plus pratique, consiste à communiquer à la construction de la date, sous la forme de nombres, les informations suivantes : année, mois (de 0 à 11), jour, heures, minutes et secondes (et même millisecondes). Les quatre dernières données sont facultatives.

    var bonneAnnee = new Date(2012,11,31,23,59,59,999);
    var dateReveillon = new Date(2012,11,31);

  1. Définissez par cette méthode la date correspondant au début de la séance d'aujourd'hui puis affichez-la pour vérification.
  2. Définissez et affichez votre date anniversaire.

## Autres manipulations : les fonctions

Un type de données est défini par un ensemble de valeurs et les opérations qui s'appliquent sur ces valeurs. Nous avons vu les opérations sur les nombres mais peu de manipulations sur les chaînes et aucune sur les dates. Nous allons corriger ce point grâce à la notion de fonction.
