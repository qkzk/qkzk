---
author: qu3nt1n
date: 2016-07-02 09:26:42+00:00
draft: false
title: 4.04 Fonctions
weight: 4
---



Notions abordées dans cette page



 	  * les fonctions
 	  * spécification
 	  * paramètres (formels effectifs)
 	  * appel de fonction







# Fonctions




Sans rentrer dans des détails, dans d'autres langages, et parfois même en javascript,
on pourra rencontrer le terme de **méthode** "à la place" du terme
de fonction.


En plus de l'opérateur `+` rencontré, le
type `String` définit d'autres opérations qu'il est
possible d'appliquer sur ses valeurs. Il s'agit
de fonctions. Une fonction est une
entité qui accepte des données en entrée, réalise un traitement puis
fournit un résultat.


A quoi vous fait penser cette définition (informelle) sur les fonctions ?




La notion de fonction ne différe pas fondamentalement celle en
mathématique, ainsi la fonction _sin_ admet-elle un seul
paramètre de type nombre et fournit un résultat de type nombre.
Simplement nous utiliserons des fonctions qui auront plusieurs
paramètres (on utilise le terme de _variable_ en mathématique) et
ces paramètres ne seront pas nécessairement des nombres.


Les données (en entrée) d'une fonction sont appelées
paramètres. Il peut y avoir plusieurs
paramètres à une fonction et ce nombre est fixé à la définition de la
fonction. Il ne peut cependant y avoir qu'un résultat. Lorsque l'on
utilise une fonction, on parle d'appel de
fonction, il faut fournir des valeurs pour les paramètres. Le
traitement réalisé par la fonction, et en conséquence son résultat,
dépend des valeurs des paramètres.

Par habitude, on dit qu'une
fonction **renvoie** ou **retourne** un résultat, on parlera
donc de **valeur retournée** ou **renvoyée** par une fonction.


La notion de "_fonction qui ne renvoie pas de résultat_" peut
sembler en contradiction avec la notion mathématique et le terme
de procédure est parfois utilisée pour
désigner les fonctions sans résultat.


Dans certain cas particuliers, une fonction n'a pas besoin de
retourner un résultat, seul le traitement réalisé compte. C'est par
exemple le cas de la fonction `writeln`
de `document` que nous avons déjà rencontrée.

Les types des paramètres ne sont
pas quelconques. A nouveau ils sont fixés à la définition de la
fonction. Lorsque l'on appelle une fonction, il faut fournir des
valeurs dont le type correspond à celui attendu. Mais il faut bien
évidemment également connaiître la nature de la valeur attendue,
savoir qu'il faut un nombre ne suffit pas, il faut savoir si ce
nombre correspond à une température, à une somme d'argent, à la durée
en secondes d'un morceau de musique, etc.


En plus des informations en permettant la bon utilisation, le
commentaire décrivant la spécification d'une fonction peut indiquer le
nom de son créateur, la date de création ou un numéro de version. Il
constitue d'une certaine manière la carte d'identité de la fonction.


Pour pouvoir appeler une fonction il faut donc connaître les
informations concernant les paramètres : leur nombre, leurs
types, et à quoi ils correspondent. Pour pouvoir l'utiliser il faut
également savoir à quoi correspond son résultat et quel traitement
est réalisé. Toutes ces
informations sont décrites dans
la spécification de la fonction (qui
correspond à ce que nous avons vu pour l'opérateur d'addition en
renommant simplement _opérande_ en _paramètre_).

La donnée de la spécification doit suffire à l'utilisation d'une
fonction.

Lorsqu'une fonction est définie pour un type de donnée particulier,
l'utilisation de cette fonction,
son appel, sur une donnée de ce type
s'écrit en utilisant la notation pointée. Nous l'avons déjà
rencontrée avec `document.writeln` qui est en fait un
appel de la fonction `writeln` sur une donnée de
type `Document`, ce type de données correspondant à une
page chargée dans le navigateur. Evidemment le résultat dépend de la
donnée sur laquelle s'utilise ou **s'applique** la fonction, on
utilisera aussi par la suite l'expression "_donnée concernée_".

Nous verrons qu'il existe également des fonctions
dites _globales_ qui ne sont pas définies par un type
particulier. Dans ce cas leur appel se fait simplement en utilisant
le nom de la fonction, sans utiliser la notation pointée.


## Exemple


Il existe une fonction `getHours` sur le
type `Date`. De même que l'opérateur `+`
existe pour les nombres et pour les chaines de caractères, on peut
imaginer qu'une fonction de nom `getHours` puisse être
définie pour un autre type de donnée. Par exemple une
donnée `Spectacle` qui permetrait de gérer des spectacles, la
fonction `getHours` fournirait alors peut-être l'heure de début du
spectacle. Il est donc indispensable de préciser dans
la spécification pour quel type la fonction est spécifiée.

Voici une spécification de `getHours` du type `Date` :


**type concerné :** Date
**nom** : getHours
**Paramètres** : 0
**Résultat** :
**  type** : un nombre
**  description** : l'heure de la date concernée


Cette spécification nous suffit pour savoir comment utiliser cette
fonction sur une donnée de type `Date` :


    var maintenant = new Date();                                  // date a pour la valeur la date courante
    var nbHeures = maintenant.getHours();                         // heures a pour valeur le nombre d'heures de <b>Date</b>
    document.writeln("le nombre d'heures est " + nbHeures);       // on affiche ce nombre d'heures (on note l'utilisation de la concaténation)
    document.writeln("ou encore :" + maintenant.getHours());      // il n'est pas obligatoire de définir une variable pour utiliser le résultat
    document.writeln("ou encore :" + new Date().getHours());


Il existe de nombreuses autres méthodes similaires qui s'appliquent
sur et permettent la manipulation des données de
type `Date` : `getFullYear`, `getMinutes`, `getMonth`, `getSeconds`
et `getMilliseconds`.


Ecrivez une page qui affiche de manière détaillée à raison de une
par ligne les informations
de la date courante (au moment du chargement de la page). Utilisez
une feuille de style pour présenter l'information.




Un peu plus haut nous avons vu qu'il n'était pas indispensable de
définir une variable pour la date.
Expliquez néanmoins la différence qu'il y a entre les deux codes suivants :


        var maintenant = new Date();
        document.writeln(maintenant.getFullYear());
        document.writeln(maintenant.getFullYear());


et


        document.writeln(new Date().getFullYear());
        document.writeln(new Date().getFullYear());


Notamment que se passe-t-il si on remplace l'appel à la
fonction `getFullYear` par `getSeconds`
ou `getMilliseconds`  ?
Faites des tests pour appuyer votre réponse.




Les fonctions que nous venons de découvrir sont définies pour le
type `Date` et (a priori) uniquement pour ce type. En
tout cas il n'existe pas de fonction de même nom pour le
type `String`. Appeler une telle fonction sur une telle
donnée n'a donc aucun sens et est refusé par le langage.


On constate que le message d'erreur n'est pas totalement précis. Il faut comprendre
le message `chaine.getHours is not a function`
comme signifiant _`getHours` n'est pas une fonction définie pour `chaine`,donc
pour son type : `String`_




Ecrivez un code qui définit et initialise une
variable `chaine` de type chaîne de caractères puis
appelle la fonction `getHours` sur cette variable.
Chargez cette page puis utilisez Firebug pour constatez ce qui
se passe.




`getFullYear` a été créée pour pallier ce problème lié à
l'an 2000 et il est maintenant considéré que `getYear` ne
doit plus être utilisée. De telles évolutions dans les langages de
programmation arrivent régulièrement. Ce ne sont pas des langues
mortes !Les éléments qu'il ne faut plus utiliser sont
dits **désapprouvés** (**deprecated** en anglais).






Il existe également une fonction
`getYear` pour le type `Date`.



 	  1. Faites quelques tests d'appel de cette fonction avec des données
de type `Date` définies avec différentes années.
 	  2. Déduisez-en une spécification pour cette fonction.
 	  3. Avez-vous une idée de pourquoi cette fonction a été considérée comme
n'étant pas compatible avec le passage à l'an 2000 ?




Le nombre d'éléments définis dans un langage (types, fonctions,
etc.) est énorme et en perpétuelle augmentation puisque les programmeurs
viennent ajouter des nouvelles fonctionnalités en continu. Il est
donc sans espoir de vouloir tout connaître. Mais ce n'est pas grave
car cela n'est en fait pas nécessairement utile. Ce qu'il faut par contre
c'est savoir, et donc apprendre à, chercher des
informations. Ensuite l'expérience et la pratique font que l'on sait
plus ou moins de choses sur un langage... mais jamais tout.

Nous avons déjà eu l'occasion de dire que la lecture de
documentations et de spécifications était une activité
importante pour un programmeur. Essayons nous à sa pratique...


Une bonne source d'information est le **Mozilla Developper
Network**. Il contient des documentations de référence assez
détaillées et des exemples notamment pour Javascript mais aussi les
CSS ou HTML. Vous pouvez donc suivre avec confiance les liens
proposés lorsqu'ils vont vers ce site.
Plus concis mais très pratique pour retrouver une information
oubliée, vous pouvez également certainement compter sur le
site **w3schools** (malgré la pollution publicitaire).
Evidemment c'est le plus souvent en anglais.




Testez et recherchez de la documentation (ou recherchez et testez) sur
les fonctions du type `Date` :



 	  * `toLocaleString`
 	  * `toLocaleDateString`
 	  * `toLocaletimeString`

Ecrivez leur spécification.






## Fonctions pour le type `String`


Il existe par exemple en javascript une
fonction `charAt` pour les chaînes de caractères, en
voici la spécification :


On rencontre à nouveau la numérotation à partir de 0.




Le terme **_indice_** est utilisé pour désigner la position d'un
caractère dans une chaîne.




**type concerné :** String
**nom** : charAt
**Paramètres** : 1
**  pos** : (numérique) correspond à
l'indice du caractère demandé, le premier caractère a pour indice
0
**Résultat**
**  type** : une chaine de longueur 1 (on rappelle
qu'en javascript il n'y a pas de type spécifique pour les caractères)
**  description** : le caractère
d'indice pos dans la chaîne de caractères concernée




Soit `chaine` une variable initialisée à la
valeur `"timoleon"`, à partir de la spécification ci-dessus quel
appel de fonction permet de connaître :



 	  1. le premier caractère de `chaine`,
 	  2. le quatrième caractère de `chaine`,
 	  3. le dernier caractère de `chaine`.
 	  4. Reprenez vos réponses à ces trois questions en modifiant la valeur
de la variable `chaine` en `"javascript"`,
la dernière expression est-elle encore correcte ? Quelle
expression permet de la corriger ?
 	  5. Donnez en fonction de la propriété `length` une
expression qui permet d'obtenir le dernier caractère d'une
variable `chaine` indépendamment de sa valeur (supposée
différente de `""`).Vérifiez votre proposition avec les deux valeurs précédentes
puis avec quelques autres.






Dans la description de la fonction _sin_ que l'on nomme _x_
ou _u_ ce paramètre formel, la fonction est bien évidemment la
même : la fonction qui à _x_ associe _sin(x)_ est la
même que la fonction qui à _u_ associe _sin(u)_.
Cependant, faire le calcul avec pour paramètre
effectif `1` ou `0` n'est pas la même chose et
influe tout aussi évidemment sur le résultat.


Dans la spécification de la fonction, les noms donnés aux paramètres
n'ont pas de réelle importance. On peut changer le nom utilisé sans
changer la fonction, on parle de
paramètres formels. Dans la
spécification précédente
de la fonction `charAt`, appeler `pos`
ou `indice` ou `numero` le paramètre (formel) ne modifie en
rien la fonction elle-même.

A l'inverse lors
de l'appel d'une fonction, la valeur transmise à la fonction n'est
évidemment pas anodine et on parle alors de
paramètres effectifs. Demander le
caractère à l'indice `0`, `2`
ou `5` d'une chaîne ne fournit a priori pas la même
valeur, et en tout cas pas le même caractère.


Afin de pouvoir en écrire les spécifications, faites des recherches
sur les
fonctions `slice`, `substring`, `toUpperCase`
et `toLowerCase`.
Testez ces fonctions et écrivez leurs spécifications.




Ecrivez un portion de code qui permet de transformer la valeur d'une variable
de type chaine de caractères appelée `mot` et représentant un mot (par
hypothèse) en un nom propre. Cela consiste à mettre la première lettre
en majuscule et les autres en minuscules.Ainsi si la valeur de `mot` dans l'environnement est
initialement `"timoleon"`, après exécution de cette portion
de code l'environnement associe la valeur `"Timoleon"` à la
variable `mot`. Ou encore si la valeur initiale
est `"jaVaScripT"`, la valeur finale
est `"Javascript"`.
Testez votre portion de code.




Comme vous l'avez sans doute aperçu au cours de vos recherches, il
existe de nombreux autres fonctions pour le
type `String`. Nous aurons peut-être l'occasion d'en
découvrir et utiliser certaines...


## Retour sur les dates




On rencontre les termes de **accesseur** et **modificateur**
(ou **getter** et **setter** en anglais) pour désigner les fonctions
d'accès et de modifications des informations et dont les noms respectent
la forme `getXXX` et `setXXX`.


En plus des fonctions telles que `getHours` qui
permettent d'accéder aux différentes informations qui composent une
date, on dispose des fonctions correspondantes de
modification. Ainsi la fonction `setHours` permet de
modifier le nombre des heures d'une variable de
type `Date`. Ces fonctions ont la particularité, déjà
évoquée, de ne pas avoir de résultat. Leur intérêt réside donc dans
le traitement qu'elles réalisent. Dans leurs cas ce traitement a un
effet sur l'environnement en modifiant la variable de
type `Date` concernée. On
qualifie d'effet de bord de telles
actions "en dehors" de la fonction.

Leur spécification doit faire mention de cet effet. Ainsi
pour `setHours` :


**type concerné :** Date
**nom** : setHours
**Paramètres** : 1
**  h** : (numérique) correspond à
la nouvelle valeur des heures pour la date concernée
**Résultat** : aucun
**Effet de bord** : modifie les heures pour la date
concernée, la nouvelle valeur est h




Nous avons déjà mentionné le terme **procédure**. Ce sont les
fonctions à effet de bord que l'on appelle ainsi.


Nous avons déjà rencontré une fonction à effet de bord : la
fonction `writeln` qui s'applique aux valeurs de
type `Document`. Pour cette fonction l'effet de bord de
modification de l'environnement concerne la
variable `document` qui correspond à la page et dont le
contenu (en quelque sorte la valeur) est impacté par l'exécution de
la fonction.


Le paramètre de `writeln` est interpété par la navigateur
pour son affichage dans la page. Il peut et doit donc
correspondre à tout texte à la syntaxe HTML. Il peut notamment
contenir des balises et des informations _CSS_ sur ces balises.
Ainsi on peut vouloir écrire `document.writeln('<div
class="exemple"> un petit texte </div>');` et le
style précisé sera appliqué.




Proposez une spécification pour la fonction `writeln`


On peut également rencontrer des formules "mixtes", c'est-à-dire
des fonctions qui à la fois retournent un résultat et réalisent un effet de bord.
