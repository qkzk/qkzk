---
author: qu3nt1n
date: 2016-07-02 08:40:29+00:00
draft: false
title: 4.02 Javascript, les variables
weight: 2
---



Notions abordées dans cette page



* introduction à javascript
* javascript ans une page HTML
* déclaration de variables en javascript
* affectation
* séquence d'instructions
* "debuggage", utilisation de la console de développement
* introduction à la portée de variables
* environnement







# Introduction à Javascript




Les navigateurs possèdent leur propre interprète Javascript. Il en
résulte qu'il existe différentes versions du langage, selon les
navigateurs mais aussi selon leurs versions... Un code
Javascript pourra donc être interprété différemment (voire pas du tout) selon le
navigateur utilisé. Il en est d'ailleurs de même pour l'interprétation
des feuilles de style.
Heureusement le noyau du langage ne change pas et les concepts encore
moins, et la plupart de ce qui sera présenté sera valide sur tous les
navigateurs. Cependant nous nous basons sur le javascript contenu
dans des versions de Firefox supérieures à la version 3.6.


Dans les exemples précédents nous n'avons pas à proprement parler
utilisé de langage de programmation. Nous avons exploité des
fonctionnalités offertes par des logiciels (tableur ou traitement de
textes) qui offrent dans un cadre limité et restreint à leur objectif
des possibilités de généricité et de traitement partiel sur des
contenus. Nous allons maintenant commencer l'étude d'un "vrai" langage
de programmation.

Nous utiliserons le langage **Javascript**. Il s'agit d'un langage
de programmation qui permet d'ajouter des traitements au sein d'une
page web (au format HTML).
L'utilisation de code dans le langage Javascript au sein d'une
page HTML permet d'obtenir une page dont le contenu (ou du moins une
partie de celui-ci) est **calculée** par le traitement réalisé en
Javascript. On peut ainsi produire des pages "**dynamiques**" et
dont le contenu peut par exemple s'adapter à un contexte particulier
qui peut être le résultat de choix de l'utilisateur de la page.

Le code Javascript est interprété par le navigateur, comme
celui-ci interprète le code HTML et la feuille de style CSS. Le
code Javascript doit être placé dans une balise HTML
particulière, la balise `script`. La balise ouvrante
contient une information supplémentaire précisant qu'il s'agit de
code Javascript. Une première manière de procéder consiste à placer
le code Javascript directement dans la page HTML, au sein de la
balise `script` comme ceci :


    ...du code HTML ici
       <script type="text/Javascript">//

         ... CODE JAVASCRIPT ICI ...

    </script> du code HTML ici


Cela a pour effet d'alourdir un peu le code HTML écrit mais tout à un
coût. De plus ce code n'est "visible" que pour le rédacteur de la page.

Une page HTML peut contenir plusieurs balises de script.


# Variables en Javascript


Comme cela a déjà été vu avec le code HTML, l'écriture de code
informatique nécessite le respect d'une syntaxe précise. Une partie du
travail d'apprentissage d'un langage de programmation consiste donc à
en connaître la syntaxe. La bonne utilisation de cette syntaxe afin de
produire des codes dont l'exécution aboutit au résultat souhaité est
évidemment une seconde partie essentielle de cet apprentissage.


## Déclaration


Pour définir (on utilise également le verbe _déclarer_) une
variable en Javascript il faut utiliser le mot-clé `var`
suivi de l'identificateur (le nom) de
la variable que l'on souhaite déclarer. Par exemple :


On peut remarquer ici le `;` qui
conclut l'instruction de déclaration. Il représente le caractère de
"fin de phrase". Même si cela n'est pas obligatoire il est très
vivement conseillé, et presque toujours observé, d'aller à la ligne
après chaque instruction.




    var uneVariable;



Les identificateurs doivent respecter certaines règles : ils sont
composés de lettres (il faut éviter les accents), de chiffres, du
caractère dollar ($) et de caractères de soulignement ('_'), sans
espace et ne doivent pas commencer par un chiffre. De plus certains
noms sont interdits car déjà utilisés par le langage, on parle
de _noms réservés_. C'est par exemple le cas du
mot `var` et on comprend bien pourquoi.

Les noms de variables suivants sont donc autorisés :

~~~javascript
x
y$
x1
laTemperature
une_autre_temperature
_duree_en_secondes
$nomArtiste
~~~




Le choix de l'identificateur d'une variable est
important. Il faut notamment privilégier des noms qui aident à
comprendre ce que représente la variable. Il faut ainsi préférer des
identificateurs de variables tels
que `temperature`, `nomDuJour`
ou `couleurDAffichage` à `t`, `n`
ou `c`. Même si cela implique que le code à écrire est plus
long, tous les programmeurs s'accordent à dire que cela facilite
beaucoup la production et la lecture du code.


Enfin, le langage fait la distinction entre les majuscules et les
minuscules. Les variables d'identificateurs `temperature`
et `Temperature` sont donc différentes.

Utiliser une variable c'est utiliser son identificateur dans une
expression. Celui-ci est évalué à la valeur de la variable. Il faut
donc attribuer une valeur à la variable. On parle
d'initialisation de la variable.


## Attribuer une valeur


Une variable est un couple (identificateur, valeur). Nous avons pour
l'instant défini l'identificateur mais aucune valeur n'a été
associée. Pour attribuer, ou **affecter**, une valeur à une
variable on utilise l'opérateur
d'affectation `=`. Il s'agit d'un opérateur binaire,
l'opérande de gauche est l'identificateur de la variable dont on fixe
la valeur et l'opérande de droite est une expression dont la valeur
est affectée à la variable.


    identificateur = valeur;



Chaque affectation sur une variable modifie sa valeur, la valeur
précédente est oubliée.

Il est possible d'affecter une valeur à une variable en même temps que
sa déclaration.


Les portion de lignes situées après `//` désignent des
**commentaires**, le texte qui suit ces lignes est ignoré par le
langage. Les commentaires sont utilisés par le programmeur pour
laisser des "notes" dans le code qu'il a écrit. Ces informations sont
à destination des autres programmeurs (ou lui-même) et sont destinées
à faciliter la compréhension du code écrit. Un commentaire doit donc
être concis, précis et informatif.
Tout bon programmeur se doit de laisser des commentaires dans le
code qu'il produit.
Il est également possible de produire des commentaires sur plusieurs
lignes en les encadrant des signes `/*` et `*/`.



~~~javascript
var temperature;               // définit la variable temperature
temperature = 37;              // fixe la valeur de temperature à 37
var _duree_en_secondes = 324;  // définit la variable _duree_en_secondes et fixe sa valeur à 324
_duree_en_secondes = 238;      // modifie la valeur de _duree_en_secondes qui vaut maintenant 238
~~~


La partie droite d'une affectation peut en fait être une
expression. Cette expression sera évaluée (calculée) et c'est le
résultat de cette évaluation qui constituera la valeur affectée
à la variable.

~~~javascript
var n = 12+5;               // la variable n est créée avec la valeur 17
var numero = 10+n;          // la variable numero est créée avec la valeur 27
numero = numero+1;          // modifie la valeur de numero qui vaut maintenant 28
~~~




## Première utilisation dans une page web


Pour un premier exemple, nous allons faire très simple en créant et
initialisant 2 variables numériques et en affichant dans la page le
résultat de leur somme.


`document` est en fait une variable particulière créée par
le navigateur et dont la valeur est le contenu du document géré par
le navigateur.


Pour pouvoir réaliser l'affichage nous allons utiliser une
instruction particulière :

~~~javascript
document.writeln(expression);
~~~


dont l'exécution produit l'écriture du résultat de l'évaluation
de `_expression_` dans la page HTML à l'endroit où
cette instruction Javascript est placée. Ce code (devenu HTML) est
ensuite interprété par le navigateur pour son affichage.

Il faut donc créer une page HTML dans laquelle on va placer d'une part
le code de déclaration des variables :

~~~javascript
<script type="text/Javascript">

     var nombre1 = 12;
     var nombre2 = 20;

</script>
~~~

puis d'autre part le message qui affiche leur
somme :

Le résultat de la somme est


Le résultat obtenu n'est pas celui attendu ?
Attention aux fautes de frappe ! Assurez-vous de ne pas avoir
fait d'erreur de copie, en oubliant un ; ou un " par
exemple. Voir également plus bas.






Créez une telle page HTML que vous adapterez
pour afficher le résultat en rouge en utilisant après l'avoir
définie une feuille de style CSS.




Rien ne change  ?
Avez-vous sauvegardé après
avoir modifié ? Avez-vous rechargé la page ensuite ?




Modifiez le document précédent pour que le
texte affiché dans la page soit :


     Le résultat de la somme de 12 et 20 est 32.



On modifiera la feuille de style pour que les valeurs des 2 nombres
soient affichées en vert.

Evidemment une modification de la valeur d'une variable au moment de
la déclaration doit suffire pour entrainer une modification du texte affiché
dans la page sans que l'on ait à modifier autre chose.

Validez ce point en remplaçant dans la déclaration de la variable
`nombre1` (et uniquement à cet endroit) 12 par 22.






## Séquence d'instructions


Une portion de code Javascript délimité par la
balise `script` peut contenir plusieurs expressions
Javascript. C'était le cas ci-dessus avec le bloc de déclaration des
deux variables `nombre1` et `nombre2`. On
parle alors de séquence
d'instructions et ces expressions sont évaluées les unes
après les autres dans leur ordre d'écriture.

Le `;` déjà évoqué est le séparateur entre les
expressions d'un séquence. On peut considérer qu'il joue le rôle des
adverbes de temps _puis_ ou _ensuite_ en
Français : _évaluer `var nombre1=10` **puis**
évaluer `var nombre2=12`_ ou _évaluer `var
nombre1=10` **ensuite** évaluer `var
nombre2=12`_.


## Des erreurs dans mon code...


La ***Console de Développement** est l'outil le plus important pour développer
en javascript. Dans votre navigateur Chrome, pressez F12 pour ouvrir la console
de développement.

Vous remarquez qu'une fenêtre s'ouvre à droite de la page. Elle contient de
nombreux outils utiles à différentes phases de la conception d'un site web.

Ceux qui vous nous intéresser le plus sont :

* la console (onglet _console_ en haut) où apparaissent les erreurs et certains messages
* l'icône carré contenant une flèche tout en haut à gauche. Elle permet de cliquer sur un élément de la page et de voir le code correspondant. On peut ainsi repérer et modifier les éléments ou leur style (CSS)
* les sources (onglet _source_ en haut) où le code des différents fichiers est présenté. On y trouve un _débuggueur_ qui nous permettra d'exécuter notre code étape par étape et de consulter l'état des variables au fur et à mesure.

Tous les navigateurs récents proposent une console de développement équivalente.




Nous commençons à écrire du code et risquons très vite d'être
confrontés au problème des erreurs dans le code, erreurs de syntaxe
notamment. Un des problèmes des programmeurs, en particulier les
débutants, est de savoir trouver ces erreurs.
Heureusement il existe des outils qui facilitent ce travail. Ceux-ci
disposent d'un **analyseur syntaxique** (comme les validateurs HTML
ou CSS déjà étudiés) capable de trouver les erreurs de syntaxe dans un
code et, le plus souvent, de transmettre un message indiquant où se
trouve l'erreur et quelle en est la cause probable.

Il est important et même indispensable de savoir retrouver les erreurs
et comprendre les messages d'erreur afin de pouvoir corriger le code
en autonomie.
En ce qui nous concerne nous allons utiliser l'outil la console de développement pour
retrouver ces erreurs.


Reprenez le document qui affiche la somme de 2 nombres et modifiez
la ligne qui affiche la somme **exactement** ainsi :

~~~javascript
<script type="text/Javascript">
document.wrteln(nombre+nombre2);
</script>
~~~






On peut constater que l'existence d'erreurs dans le code Javascript
dans la page n'empêche
pas le navigateur d'afficher un contenu.




Rechargez la page et constatez que le texte affiché ne correspond à ce
que l'on souhaitait obtenir initialement ce qui est naturellement dû
aux erreurs que nous avons introduites.






Activez la console de développement via la touche F12.




Une zone s'active en bas de la
fenêtre du navigateur. Pour ce premier contact avec la console de développement nous
allons nous contenter du premier onglet intitulé "Console". Dans cette
zone nous trouvons affichés la portion de code Javascript qui pose
problème, un message d'erreur en rouge, le nom du
fichier contenant l'erreur et le numéro de la ligne dans le fichier
qui contient l'erreur.

![la console de développement](http://qkzk.xyz/docs/doc04/doc/firebug1.png)



Et oui, le message d'erreur est en anglais... Mais l'anglais est la
langue de l'informatique si vous en doutiez ou l'ignoriez encore, et il
s'agit d'anglais "technique" généralement assez simple une fois le
vocabulaire spécifique assimilé.


Le message d'erreur, `"nombre is not defined"`, nous indique que l'on
utilise une variable `nombre` qui n'est pas définie, et en
effet puisque c'est `nombre1` que nous voulions utiliser à
cet endroit.




Corrigez l'erreur, sauvegardez et rechargez la page.

Que constate-t-on ?

Utilisez la console de développement pour localiser la nouvelle erreur, quel est le message ?

L'erreur de frappe provoque cette fois la non reconnaissance d'une
fonction (`writeln`). Corrigez et vérifiez que tout est
correct maintenant.




Les messages d'erreur sont hélas parfois moins explicites, c'est
pourquoi il faut apprendre à analyser le code... Parfois une seule
erreur peut par propagation en générer plusieurs au niveau de
l'interprète.


Toujours à partir du même fichier, modifiez la déclaration
de `nombre2` en la remplaçant par :


     va nombre2 = 20;






1. Consultez la console de la console de développement.
2. Combien d'erreurs sont mentionnées ?
3. A quelles lignes sont-elles signalées ?
4. Que pensez-vous du premier message d'erreur ?
5. Que signifient les autres messages d'erreur ? Comment les expliquer ?
6. Corrigez cette première erreur et consultez à nouveau la console.






## Valeurs non initialisées




Modifiez à nouveau le code dans le document en supprimant la valeur de
l'initialisation de `nombre1` :

~~~javascript
<script type="text/Javascript">

  var nombre1;
</script>
~~~

Rechargez la page, que constate-t-on ?

Des erreurs sont-elles signalées par la console de développement ?




L'affichage de la valeur de `nombre1` montre que celle-ci à
une valeur **indéfinie** (`undefined`) ce qui est différent
d'une variable **non définie**, comme c'était le cas
de `nombre` précédemment. C'est subtil mais différent
malgré tout...

On constate que l'affichage de l'évaluation de la somme des
deux nombres produit une valeur particulière `NaN` (pour
"_Not a Number_"). Ce résultat indique que l'opération
d'addition n'a pu être réalisée car la variable `nombre1` n'était
pas liée à une valeur numérique.


Toute variable doit être définie pour pouvoir être utilisée et il faut
lui avoir attribué une valeur.




Définissez deux variables en les initialisant avec des valeurs
numériques, affichez leurs valeurs, puis écrivez un code Javascript
qui réalise l'échange des valeurs contenues par les deux variables puis
affiche à nouveau les valeurs des variables mais après l'échange.
Testez ce code avec plusieurs valeurs initiales des variables.




## Notion de portée


Les variables, une fois définies, n'existent pour autant pas "partout". Vérifions-le rapidement :


Créez une première page définissant et initialisant une
variable `nombre1` et qui en affiche la valeur (afin de
vérifier que la variable est définie).
Créez une seconde page
qui tente d'afficher la valeur d'une variable `nombre1`
mais **sans la définir (déclarer) auparavant**.
Dans votre
navigateur chargez la première page puis dans un autre onglet
chargez la seconde. Que remarque-t-on ?


La variable `nombre1` est bien définie dans la première
page, mais pas dans la seconde. On dit que
la portée de sa définition est limitée
à la page dans laquelle elle est définie. On dit que sa définition
reste locale à la page qui la définit.

La notion de règles de portée sur les variables existe dans tous
les langages, même si elles peuvent varier dans leur forme. Nous
aurons l'occasion de voir d'autres règles de portée appliquées par
Javascript.


## Environnement


Sans surprise, comme on a pu le constater dans les différentes
activités précédentes, le résultat d'une expression telle
que `nombre1+nombre2` par exemple, dépend de la valeur
des variables `nombre1` et `nombre2` au moment
où l'expression est évaluée.

De même pour qu'une expression ait une valeur, donc du sens, il
faut que les variables qui y apparaissent aient été préalablement
définies. L'absence de valeur (non initialisation) d'une variable,
même définie, pose également problème.

Il est donc indispensable d'avoir en permanence la connaissance des variables
définies et de leurs valeurs afin d'écrire des expressions d'une part
qui ont un sens et d'autre part qui ont la valeur attendue. On appelle
environnement le contexte dans lequel
on réalise une évaluation.


Un **environnement** est l'ensemble des variables, c'est-à-dire
des couples (identificateur, valeur) tels qu'ils sont définis à un
instant donné. Le résultat de l'évaluation d'une expression dépend de
l'environnement dans lequel elle est effectuée.


Certaines variables ont une portée locale, la valeur d'un
environnement est donc définie localement.
