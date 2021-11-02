---
author: qu3nt1n
date: 2016-07-02 09:32:07+00:00
draft: false
title: 4.05 Exemples de Fonctions
bookCollapseSection: true
weight: 5
---

Notions abordées dans cette page



* interactivité
* "conversion" de types






# Exemples de fonctions




## Un peu d'interactivité


Voici la spécification de la fonction `prompt` qui
s'applique à la variable définie par le
navigateur `window`, de type `Window`.


La valeur `null` est une valeur particulière qui,
étrangement, peut être interprétée comme signifiant "_pas de
valeur_". Nous aurons l'occasion de revenir dessus ultérieurement.





**type concerné :** Window

**nom** : prompt

**Paramètres** : 2 (voir note)

**  message** : (chaîne), le message d'invite

**  val_init** : _(optionnel)_ (chaîne), la valeur par défaut

**Résultat** :

**type** : chaîne de caractères

**description** : la chaîne de caractères saisie
par l'utilisateur lorsqu'il clique sur Valider
ou `null` si il clique sur Annuler.

**Effet de bord** : fait apparaître une boîte de dialogue avec une zone de saisie
de texte et deux boutons Valider et Annuler.
message est affiché dans la fenêtre au-dessus de la zone
de saisie. Le champ de saisie est pré-rempli avec la valeur de `val_init`;
**note** : le second paramètre peut-être omis, dans ce cas
le champ de saisie est vide (ce qui revient à dire que la valeur
de `val_init` est `""`).


Cette spécification doit nous permettre l'utilisation de cette
fonction, testons-la :






1. Créez une page qui définit une variable `nom`,
initialise sa valeur à l'aide du résultat fourni par un appel à la
fonction `prompt` demandant à l'utilisateur de saisir
son nom, puis crée le contenu de la page avec le
message `Hello _xxx_` où `_xxx_`
est la valeur de la variable `nom` qui aura donc été
fournir lors de la saisie.
2. Testez la fonction `prompt` avec ou sans second paramètre.
3. Que se passe-t-il si l'utilisateur clique sur le bouton Annuler
de la boîte de dialogue ? Testez.




On le constate, l'utilisation de la fonction `prompt`
permet une certaine interactivité avec l'utilisateur de la
page. Elle permet d'interroger l'utilisateur et d'adapter le contenu
de la page affichée en fonction de sa réponse. Cette interactivité
n'est pas totalement satisfaisante notamment car la boîte de
dialogue bloque la page, de plus seules elle ne convient que pour
l'obtention d'une information textuelle (chaîne de caractères) et
enfin les utilisateurs n'apprécient pas forcément d'être
"interrompus" par de telles fenêtres "pop-up". Nous aurons
l'occasion d'étudier d'autre mode d'interaction par la suite.


Reprendre la manipulation sur le poème "_Paroles_" de Jacques Prévert,
cette fois le prénom répété sera obtenu par une saisie de
l'utilisateur.




Reprenons une autre manipulation que nous avons déjà rencontrée :



1. Créez une page HTML dans laquelle sont définies deux
variables `chaine1` et `chaine2` de type
chaîne de caractères que vous initialiserez à l'aide d'un appel à la
fonction `prompt` et qui affiche le
résultat de l'expression
`chaine1 + chaine2`.
2. Testez la page avec différentes valeurs pour `chaine1` et `chaine2`
3. Avez-vous fait le test avec des valeurs ne contenant que des
caractères-chiffres ? Essayez avec par exemple `12`
pour `chaine1` et `20`
pour `chaine2`.
4. Qu'affiche la page ?
5. Cela correspond-il au résultat auquel vous vous attendiez ?
Justifiez le résultat obtenu.




La spécification du résultat permettait d'anticiper le résultat
sans ambigüité. Il est cependant légitime de se demander comment
récupérer un nombre saisi par l'utilisateur.

La solution consiste en fait non pas à modifier la saisie
d'information, on va encore saisir une chaîne de caractères, mais il
s'agit de convertir la chaîne de caractères lue
en un nombre. Il faut bien évidemment que le contenu de chaîne
corresponde bien à l'écriture d'un nombre.


Cherchez la traduction en français du verbe _parse_.




Le type `Float` correspond aux nombres à virgule
flottante, généralement
appelés flottants.

La plupart des langages proposent un type différent pour
les entiers et les flottants. Ce n'est pas le cas de javascript qui ne le
différencie pas.





Selon vous pourquoi la plupart des langages
ont aussi choisi `Float` comme nom
pour ce type au lieu de `Real`, alors qu'ils nomment le
plus souvent `Integer` le type des entiers ?




## Conversion de types


Cette conversion se fait à l'aide de fonctions. Ainsi il existe la
fonction `parseInt` qui prend en paramètre une chaîne de
caractères et dont le résultat est l'entier correspondant au contenu
de cette chaîne de caractères, lorsque cela est possible. De manière
similaire il existe une fonction `parseFloat` qui permet
la conversion d'une chaîne en un nombre "à virgule flottante"
lorsque cela est possible.

Quelques précisions sont nécessaires quant au fonctionnement des
ces fonctions :



* seul le premier nombre dans la chaîne est retourné, les autres
caractères (y compris correspondant à des nombres) sont
ignorés,
* si le premier caractère ne peut être converti en un nombre, le
résultat sera `NaN`,
* les espaces en tête sont ignorés,
* avec `parseInt` il est possible de préciser un second paramètre
qui sera la base (8, 10, 16) à utiliser pour analyser la chaîne.

Exemples :

~~~javascript
parseFloat("1.24");                //   1.24
parseInt("42");                    //   42
parseInt("42 est la réponse");     //   42
parseInt("    42 est la réponse"); //   42
parseInt("1.24");                  //   1
parseInt("42estlaréponse");        //   42
parseInt("42 43 44");              //   42
parseInt("réponse = 42");          //   NaN
parseInt("10",16);                 //   16
parseInt("AA",16)                  //   170
~~~




Vous avez sûrement remarqué que la
fonction `parseInt` s'appelle "directement" sans
utilisation de la notation pointée. Il s'agit d'un exemple de _fonctions
globales_ que nous avons déjà évoquées précédemment. Ces
fonctions sont définies indépendamment d'un type de donnée particulier.




Expliquez les 2 derniers résultats.




Ecrivez la spécification de `parseInt`.


La fonction `parseInt` peut donc être appliquée au
résultat d'un appel à la fonction `prompt` pour produire
un nombre, lorsque cela a un sens :

~~~javascript
var texteSaisi = prompt("Donnez une valeur entière");
var unEntier = parseInt(texteSaisi);
~~~


Mais dans la mesure ou la fonction `parseInt` prend pour
paramètre une chaîne de caractères et que la
fonction `prompt` a pour résultat une chaîne de caractères,
on peut également "enchainer" les appels de fonction sans passer par
une variable intermédiaire :

~~~javascript
var unEntier = parseInt(prompt("Donnez une valeur entière"));
~~~


On obtient ainsi le moyen d'obtenir une valeur entière saisie par l'utilisateur.


Il s'agit exactement de la notion mathématique de composition, lorsque
l'on écrit _ln(sin(x))_ il s'agit bien de calculer la valeur
de _sin(x)_ avant d'appliquer à cette valeur _ln_. On
retouve également cette composition en Sciences Physiques
avec _cos(ωt+φ)_ qui compose la fonction qui à _t_
associe _ωt+φ_ avec la fonction _cos_.


On réalise dans ce cas une composition
d'appels de fonction.


Créez une page HTML qui demande à l'utilisateur de saisir deux entiers
et dont le contenu produit sera :


     Le résultat de la somme de xx et yy est res.



où `_xx_` et `_yy_` sont les nombres
saisis et `_res_` leur somme.

Faites plusieurs tests. Pensez à tester des saisies non valides (non
numériques) et à étudier ce qu'il se passe.






L'opérateur `+` lorsqu'il est utilisée avec une opérande de
type `String` et une autre numérique considère aussi une
conversion implicite de l'opérande numérique en
chaîne. `4+"you"` est donc évaluée en la
chaîne `"4you"`. On aurait dû
écrire `(4).toString()+"you"` (les parenthèses sont nécessaires avec
des constantes numériques).
On trouve assez régulièrement l'exploitation par des programmeurs de
cette conversion implicite lorsqu'ils ont besoin d'une conversion
(explicite) d'un nombre en chaîne. Il écrivent alors par
exemple `""+4` qui revient à `(4).toString()`.




Certaines conversions de type sont réalisées "automatiquement" par le
langage : le langage applique implicitement une conversion,
c'est-à-dire sans que le programmeur ait à "demander" cette
manipulation. C'est ce qui se passe par exemple avec la
fonction `writeln` que nous avons déjà beaucoup
utilisée. Le paramètre de cette fonction doit être de
type `String` or nous avons pu écrire :

~~~javascript
var x = 12;
document.writeln(x);
~~~


Cela est possible car Javascript réalise automatiquement l'appel d'un
traitement qui convertit la donnée numérique `12` en la
chaîne `"12"` avant d'exécuter le traitement
du `writeln`. Si le langage ne réalisait pas à notre place
cette conversion il faudrait écrire :

~~~javascript
document.writeln(x.toString());
~~~

Ce qui alourdit le code pour une fonction assez souvent utilisée. Les
concepteurs du langage ont ici voulu faciliter le travail des
programmeurs.


On souhaite créer une page qui permet la conversion d'une température
exprimée en Fahrenheit en Celsius puis l'inverse.



1. Recherchez sur internet les formules de conversion entre ces
unités de mesure.
2. Écrivez le code qui demande la saisie d'une température en Fahrenheit et affiche la température Celsius équivalente.
3. Écrivez le code qui demande la saisie d'une température en Celsius
et affiche la température Fahrenheit équivalente.
4. Testez la page créée.










 	  1. Réalisez un page HTML qui après avoir demandé la saisie de 2 valeurs
correspondant à une latitude et une longitude sous forme de nombres à virgule affiche la "_google
map_" centrée sur ces coordonnées.

**Rappel** : le code pour afficher une image _google
map_ ressemble à ceci :
`<img
src="http://maps.googleapis.com/maps/api/staticmap?center=50.609731,3.137511&zoom=17&size=400x400&sensor=false"
/>`
.
 	  2. Avez-vous transformé les données lues en données de
type _float_ ? Si oui, fallait-il absolument le faire ? Si non,
pourquoi n'était-ce pas indispensable ?
 	  3. Modifiez la page afin que l'utilisateur ait à fournir en plus la
valeur du facteur de zoom et la taille d'affichage (on pourra
conserver une image carrée) avant l'affichage.
 	  4. Testez !
