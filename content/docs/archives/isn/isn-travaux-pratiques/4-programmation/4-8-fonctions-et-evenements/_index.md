---
author: qu3nt1n
date: 2016-07-02 10:13:25+00:00
draft: false
title: 4.08 Fonctions et événements
bookCollapseSection: true
weight: 8
---



Prérequis



* l'attribut `ID` a-t-il déjà été évoqué, a priori oui
pour le CSS
* a-t-on parlé d'arbre DOM ? Dans ce cas on peut modifier un peu
le discours.

Notions abordées dans cette page



* le type de donnée des "éléments de page"
* la mise en place d'événement
* manipulations dynamique de la page







Les codes fournis ici ne fonctionneront sans doute pas avec Internet
Explorer. L'interprète Javascript de ce navigateur diffère un peu de
ce qui est présenté ici. Le nom des fonctions utilisées changent mais les principes restent exactement les
mêmes. Ainsi les fonctions `addEventlistener`
et `removeEventListener` qui sont introduites dans la suite
s'appellent `attachEvent` et `detachEvent` pour
Internet Explorer.

Il en sera de même avec des navigateurs "un peu anciens" (on
devient très vite "ancien" en informatique). Il faut donc continuer à
tester ces codes avec un navigateur Firefox "récent" (version > 6
par exemple).




# Des pages plus dynamiques




## Des données pour représenter les éléments d'une page


La langage Javascript offre la possibilité de manipuler une page
HTML. Il est possible par l'exécution de code Javascript d'agir
directement sur une page affichée par un navigateur et de la
modifier dynamiquement. Il s'agit en fait d'agir sur les données qui
représentent les contenus de la page. Vous savez maintenant qu'une
page HTML respecte une syntaxe précise et qu'elle est composée
d'éléments structurés par des balises. Chacun des éléments qui
apparaît dans la page peut être représenté par une donnée
Javascript. Nous avons déjà rencontré la
donnée `document` qui représente le document dans son
ensemble. Javascript propose le type `Element` qui
représente les éléments au sein d'une page HTML, c'est-à-dire les
blocs correspondant à des balises, et offre des fonctionnalités pour
les manipuler. On peut ainsi définir une variable représentant un
élément <img>, un titre <h2> ,
un paragraphe <p> , un bloc
<div> , etc., et manipuler ces
variables. Par exemple, il est possible de modifier l'apparence ou
le contenu d'un élément. Ces opérations permettent de créer des
effets dynamiques qui enrichissent les possibilités offertes par
l'usage du seul couple HTML/CSS .


A nouveau, la présentation faite ici est partielle. Les possibilités
offertes par Javascript pour l'accès et la manipulation des données
représentant les éléments d'une page HTML sont beaucoup plus larges.


La première méthode d'accès aux données représentant un élément de
la page HTML que nous allons utiliser consiste à exploiter la
possibilité de nommer en HTML un élément de la page grâce à
l'attribut `id` (on pourra parler d'_élément
identifié_). En effet la fonction `getElementById`
qui s'applique sur la donnée `document` permet de
récupérer la donnée de type `Element` dont
l'attribut `id` correspond à la valeur passée en
paramètre de l'appel de fonction.

Ainsi considérons la portion de code HTML suivante :


~~~javascript
<h1>Un exemple avec des id</h1>
<div>Un premier bloc div</div>



<div id="important">Ceci est un texte important.</div>

<img src="exemple.png" id="monImage" class="encadree"></img>
~~~


Il est possible d'associer une variable Javascript pour chacun des
 éléments identifiés par un attribut `id` de la manière
 suivante :


~~~javascript
var divImportant = document.getElementById("important");
var lImage = document.getElementById("monImage");
~~~


Les éléments qui ne possèdent pas d'attribut `id` ne sont
pas accessibles par cette méthode.


## Evénements




D'une manière générale vous pouvez considérer qu'il ne faut plus
utiliser `document.writeln` dès lors qu'il s'agira de
manipuler dynamiquement des éléments de la page.


L'interaction sur des éléments d'une page nécessite d'aborder des
manipulations un peu différentes de celles étudiées jusque
maintenant.
L'approche à adopter va différer de ce que nous faisions jusque
maintenant car nous agissions sur le contenu de la page **au moment
de son chargement**. Ainsi les `document.writeln` utilisées
étaient interprétées par la navigateur au fur et à mesure de la mise
en place de la construction des éléments comme nous avons
pu l'observer lors du chargement de la page affichant les
momuments. Cela ne convient plus pour ce que nous voulons faire maintenant.

Enfonçons les portes ouvertes : pour agir sur les éléments d'une
page il faut que ces éléments existent... Il faut donc que la page
ait été chargée complètement par le navigateur. Les traitements
agissent donc sur une page déjà "existante". Il faut donc trouver un
moyen pour déclencher ces traitements alors que la page a fini d'être
chargée. Cela est possible grâce à
la programmation événementielle.

On appelle événement :



* une action de
l'utilisateur sur un élément de la page via la souris ou le
clavier
* ou le chargement d'une donnée, page ou image par exemple.

Le principe est de permettre le déclenchement d'un traitement
lorsqu'un événement particulier se produit sur un élément de la page.

Il existe différents types d'événements. Ils caractérisent l'action
réalisée et dépendent de l'élément sur lequel porte l'action, tous les
types d'événements ne sont pas disponibles pour toutes les sortes
d'éléments. Chaque type d'événement à un nom :

* un événement `click` est déclenché lors d'un clic souris
* un événement `load` est déclenché à la fin du chargement
d'un élément
* un événement `mouseover` est déclenché lorsque la
souris passe au-dessus d'un élément
* un événement `keypress` est déclenché lors de l'appui
d'une touche
* un événement `change` est déclenché lorsque le
contenu d'un élément change,
* etc.



La programmation événementielle consiste à lier une
fonction à un type d'événement pour un élément donné.
La fonction est exécutée lorsque l'événement se produit sur cet objet.




La liaison d'une fonction à un événement pour un élément donnée se
réalise grâce à la fonction `addEventListener` du
type `Element` :



**type concerné :** Element

**nom** : addEventListener

**Paramètres** : 2

**typeEvenement** : (chaîne), le nom du type d'événement considéré

**fonctionDeclenchee** : (fonction),
la fonction déclenchée lorsque l'événement considéré se produit sur
l'élément concerné

**Résultat** : aucun

**Effet de bord** : appel la
fonction fonctionDeclenchee lorsque l'événement de
type typeEvenement se produit sur l'élément concerné.


La syntaxe d'un appel sur un élément ressemble donc à :


~~~javascript
    element.addEventListener(typeEvenement,fonctionDeclenchee)
~~~


On rencontrera (et utilisera) donc souvent le schéma typique de code
suivant, où `action` est une fonction supposée définie par
ailleurs :

~~~javascript
    var unElement = document.getElementById("lElementQueJeVeux");
    unElement.addEventListener("click",action);
~~~


qui aura pour conséquence que la méthode `action` sera
appelée à chaque fois que l'utilisateur cliquera sur l'élément de la
page dont l'`id` est `lElementQueJeVeux`.


Attention Il est important de noter que le second paramètre
de `addEventListener` est un nom de fonction
(identificateur) et pas une
chaîne de caractères représentant ce nom.


On utilise le terme d'**abonnement** de la fonction
à l'événement sur l'objet. La fonction est elle appelée _fonction
écouteur_, **listener** en anglais.


## Mise en place des abonnements


Il nous reste une petite difficulté technique à franchir pour
pouvoir exploiter ces événements sur les éléments de notre page mais
elle n'est pas très compliquée à comprendre et facile à résoudre
avec un peu de méthode. Et les exemples clarifieront tout cela.

Ce "problème" concerne la mise en place des abonnements pour ces
événements. On retrouve un problème similaire à celui rencontré
précédemment : pour réaliser un abonnement il est nécessaire de
disposer de la donnée le représentant. Il faut donc que cet
élément existe. On ne peut donc pas réaliser l'abonnement tant que la
page n'a pas été chargée par le navigateur. Or le code Javascript
est a priori exécuté pendant le chargement de la page, pas après...

Pour résoudre ce paradoxe apparant nous allons utiliser le
mécanisme événementiel et un événement en particulier :
l'événement `load` qui permet de déclencher un appel de
fonction (donc un traitement) après qu'un élément ait été
complètement chargé.

Il faut créer une fonction qui réalise tous les
abonnements et abonner cette fonction à
l'élément `window`, qui est l'élément qui représente la
page dans son ensemble, pour l'événement `load`. Ainsi la
mise en place des abonnements sera réalisée après que la page ait
été chargée, on a donc l'assurance que les éléments impliqués existent.

Passons à la pratique, il "suffit" de suivre étape par étape la
démarche suivante :



1. créer un fichier dans lequel va être placé le code Javascript
correspondant à la gestion des événements, appelons-le pour
l'exemple `mesEvenements.js`,
2. ajouter dans la partie `head` du document HTML concerné
le lien vers ce fichier de script
3. définir dans ce fichier les fonctions _listeners_ dont on a
besoin, comme c'était la cas de la fonction `action`
précédemment,
4. en début de fichier, placer une fonction que nous
appellerons `setupEvents` qui aura pour responsabilité de
mettre en place les abonnements souhaités en respectant le schéma
type vu ci-dessus,
5. provoquer l'appel de cette fonction quand la page a fini son
chargement, ce qui est réaliser en abonnant cette fonction sur l'élément `window`
pour l'événement `load`

Le fichier `mesEvenements.js` ressemblera donc à ceci
:

~~~javascript
/* fonction de mise en place des abonnements
 */
var setupEvents = function ()  {

  // abonnement de la fonction action pour l'élément d'id lElementQueJeVeux en réaction à un click<
  var unElement = document.getElementById("lElementQueJeVeux");
  unElement.addEventListener("click",action);

  // ... on répète le même schéma ici si on veut mettre en place d'autres abonnements
}

// pour appeler la fonction ci-dessus quans la page est chargée
window.addEventListener("load",setupEvents);

// ----------------------------------------
/* Documentation de la fonction action
 */
var action = function () {
   ... // ce que action doit faire
}

// ... et d'autres définitions éventuellement
~~~


alors que le fichier HTML ressemble à :

~~~javascript
<script src="mesEvenements.js" type="text/javascript"></script>......
~~~


---


La méthode `alert` qui s'applique à la
donnée `window` permet l'affichage d'une
fenêtre _pop-up_ affichant le message passé en paramètre (de type
`String`).








1. Etudiez et testez [cet exemple](/uploads/docs/doc04/exemples/exemple_event1.html).
2. Complétez le code Javascript pour qu'une une fenêtre d'alerte
(utilisez `window.alert`) s'affiche dès que l'on passe la
souris sur l'image, le type de l'événement
est `mouseover`.
3. Testez !






A la suite de la manipulation précédente



1. Placez des points
d'arrêt :

  1. sur la première ligne de `setupEvents`
  2. sur la ligne `window.addEventListener("load",
setupEvents);`
  3. sur la première ligne de chacune des fonctions _listeners_
(`action1` et celle que vous avez créée).


2. Rechargez la page, "utilisez la" et observez à quel moment est
déclenché chacun des événements.




Sur un élément donné on peut avoir



* plusieurs abonnements pour différents types d'événements
* plusieurs abonnements pour un même type d'événement



On réutilise la version initiale de
l'[exemple précédent](/uploads/docs/doc04/exemples/exemple_event1.html).



1. L'événement `mousedown` est déclenché lorsque l'on
presse le bouton de la souris et l'événement `mouseup`
lorsqu'on le relâche. Complétez le code Javascript de l'exemple pour
afficher une alerte différente lorsque chacun de ces événements se
produit sur l'image.
2. Ajoutez un second abonnement pour l'événement `click`
sur l'élément d'`id` "`piedDePage`" qui
déclenchera la fonction suivante :

~~~javascript
var piedEnBleu = function() {
  var piedDePage = document.getElementById("piedDePage");
  piedDePage.style.backgroundColor = "blue";
  piedDePage.style.color = "white";
}
~~~









## Manipulation sur les éléments




Cette [page](/uploads/docs/doc04/doc/equivalences-css-javascript.html) propose
une table des équivalences de nom entre les propriétés CSS et Javascript.


La dernière _Manip_ a permis de mettre en œuvre une première
interaction avec la page : le clic sur la zone
appelée `piedDePage` a provoqué sont changement de
couleur. Le code est assez simple à comprendre : on constate que
les données de type `Element` dispose d'une
propriété `style` qui représente les informations sur
l'apparence de l'élément. Informations elles-mêmes caractérisées par
des propriétés telles que `backgroundColor`
et `color` qui ne sont pas sans rappeler celles des
feuilles CSS auxquelles elles ne sont bien sûr pas étrangères malgré
quelques différences de nommage.

On eut ainsi accéder ou modifier une valeur de style d'un élément
présent dans la page. Le navigateur interprétant en continu toute
modification de la page on obtient des effets dynamiques. Pour
modifier le style d’un élément ayant
comme `id` _monElement_ et donner la
valeur _laValeur_ à sa propriété _laPropriete_ il faut
utiliser la syntaxe suivante :


~~~javascript
var monElement = document.getElementById(monElement);
monElement.style.laPropriete = "laValeur";
~~~


On note que les valeurs des propriétés sont des chaînes de caractères.







1. Définissez une page HTML contenant un élément de
balise `div` d'identifiant `zoneTravail` et
une feuille CSS qui définit pour cette balise un texte de
couleur `red` et une couleur de
fond `#EEEEEE`.
2. Ecrivez un code Javascript qui permet lorsque l'on clique
dessus de modifier cet élément en lui attribuant la couleur de
texte `blue` et la couleur de
fond `yellow`.
3. Complétez le code HTML pour y ajouter un autre
élément `div` et ajoutez dans le code Javascript pour
qu'un clic sur ce nouvel élément permette de modifier
l'élément `zoneTravail` en lui attribuant la couleur de
texte `black`, la couleur de fond `#77FF77`
et une bordure d'épaisseur 2px, en trait plein et de
couleur `#00FF00`.
4. A nouveau complétez l'HTML avec une balise `div` et
le Javascript pour que cette fois, un clic sur l'élément ajouté
provoque l'inversion des couleurs de texte et de fond
de `zoneTravail`, quelles que soient ces couleurs.
5. Vous n'avez pas oublié de tester au fur et à
mesure, n'est-ce-pas ?
6. N'hésitez pas à utiliser Firebug pour exécuter pas-à-pas le
traitement de vos fonctions.




Essayer la
propriété css `border-radius:6px;` sur le style de vos éléments de type
bouton. Vous trouverez peut-être que cela accroit le "look bouton".





1. Modifiez la feuille de style pour donner une apparence plus "type bouton" aux 2 derniers
éléments ajoutés (largeur limitée, bordure, changement de couleur
lorsque la souris passe
au-dessus, etc.)










1. Cherchez des informations sur la fonction `Math.random`,
écrivez sa spécification.
2. Même question pour la fonction `Math.floor`.
3. En déduire une fonction qui prend en paramètre un entier
positif _n_ et a pour résultat un entier aléatoire compris en
0 inclus et _n_ exclu.
4. Utilisez cette fonction et un codagergb des couleurs pour
programmer le changement aléatoire de la couleur de fond d'un
élément que vous choisirez (reprenez une page existante ou créez-en
une nouvelle) lorsque la souris le survole. Un
événement `mouseover` est déclenché dans un tel cas.
5. Testez.




D'autres propriétés existent sur les données de type `Element`,
leur présentation exhaustive serait fastidieuse. Nous les présenterons au fur
et à mesure des besoins. Elles correspondent pour une
bonne partie d'entre elles aux propriétés des éléments HTML qu'elles
représentent.

Prenons l'exemple des images, en HTML la balise `img` dispose
d'un attribut `src` qui désigne le fichier contenant la définition
de l'image à afficher. Et bien, si une donnée Javascript représente un
élément `img`, il dispose alors d'une propriété `src`
et il est possible de modifier cette valeur ce qui entraine une modification
de l'image dans la page !

Ainsi si dans une page une balise `img` a pour
identifiant `monImage`, le code Javascript
suivant :

~~~javascript
var elementImg = document.getElementById("monImage");
elementImg.src = "isn.png";
~~~


aura pour conséquence que dans la page HTML, l'image correspondant au
fichier `isn.png` sera affichée dans
l'élément `monImage`, quelle que soit l'image initialement présente
(éventuellement aucune).


Choisissez trois fichiers images et créez un document HTML avec une
zone `img` et trois éléments "cliquables" ("boutons"),
telle qu'initialement aucune image ne soit affichée. On associe
un fichier image à chaque "bouton" et le clic sur un bouton
provoque l'affichage de l'image dans la zone `img` de
la page.
Vous définirez une feuille CSS pour accompagner cette page afin de
représenter les boutons comme il convient et de forcer la largeur
de l'image à `300px` (par exemple).




Autre exemple, les éléments de type `input` dispose
d'une propriété `value` qui correspond au texte (de
type `String`) contenu dans ce champ de saisie. Il est
donc possible de lire ou de modifier le contenu de ce champ.


Des remarques comme "_on ne s'occupera pas pour l'instant de ce qui
se passe dans un autre cas_" sont un peu énervantes... Il faudra
bien un jour que l'on se penche sur ce problème et que l'on étudie
comment on peut le résoudre... Il faut que le programme soit
capable de gérer ces situations où la saisie de l'utilisateur ne
correspond pas à ce qui est attendu... Nous aborderons donc ce point
un peu plus tard...








1. Récupérez et étudiez ce [document
HTML](/uploads/docs/doc04/exemples/temperature.html) et sa [feuille de
style](/uploads/docs/doc04/exemples/styleTemperature.css).
2. Un événement `change` est déclenché à chaque fois que
la valeur d'un élément `input` est modifiée par
l'utilisateur (l'événement est activé lorsque l'on "quitte"
l'élément `input` - on dit qu'il perd le focus). En
partant du travail réalisé lors la **Manip** sur la conversion de
température, ajoutez à ce document le code Javascript qui permet,
lors d'une saisie (numérique, on ne s'occupera pas pour
l'instant de ce qui se passe dans un autre cas) dans un champ, à la
valeur correspondante pour l'autre unité de mesure de s'afficher dans
l'autre champ.
3. Testez évidemment...




Il est également possible de manipuler le contenu "complet" d'un
élément, c'est-à-dire le code HTML qui se trouve entre les balises
ouvrante et fermante de cet élément. Ce contenu est identifié par la
propriété `innerHTML`. En changeant sa valeur, on modifie
la portion de la page correspondante. La valeur de cette propriété est
une chaîne de caractères représentant du code HTML. On peut donc y
placer des balises, elles seront interprétées.






1. Créez une page HTML avec un élément identifié et un autre élément
type "bouton".
2. ![Alan Turing](/uploads/docs/doc04/exemples/alan-turing.jpeg)

Ajoutez un abonnement sur le "bouton" pour qu'un clic modifie le
contenu de l'élément identifié en attribuant à sa
propriété `innerHTML` la valeur :


le contenu a été changé. On peut placer dans innerHTML de l'HTML
qui est interprété. Du gras ou une image par  exemple :

~~~javascript
<img src="/uploads/docs/doc04/alan-turing.jpeg" alt="Alan Turing"></img>
~~~


3. Testez.










1. Reprenez et complétez la Manip' sur les conversions d'unités de
mesure de température pour que lors d'un calcul de conversion, la
page affiche un texte de la forme `la température _ccc_ en
Celsius vaut _fff_ en Fahrenheit`.
2. Mettez en forme (CSS) ce message affiché.






## Quelques compléments


Une même fonction peut être utilisée pour plusieurs abonnements.


Créez une page HTML qui affiche 2 images positionnées côte à côte
telle qu'un clic sur l'une des deux images provoque l'échange des 2
images.








1. Créez un document HTML avec deux éléments `div`
identifiés.
2. Créez une feuille CSS utilisée par cette page qui "donne du
style" à chacun de ces éléments.
3. Complétez la feuille de style en ajoutant pour le premier élément
le couple propriété/valeur :

~~~javascript
display: none;
~~~

et pour le second le couple

~~~javascript
display: block;
~~~

(cette seconde valeur est la valeur par défaut pour les
blocs `div`)
4. Rechargez la page. Que constatez-vous ?
5. Ajoutez 2 autres éléments `div` identifiés et cette
fois attribuez au premier la propriété :

~~~javascript
visibility: hidden;
~~~

et au second


    visibility: visible;


(cette seconde valeur est la valeur par défaut pour les éléments).
6. Rechargez la page. Que constatez-vous ?
7. Déduisez-en le sens de ces couples propriétés/valeurs, quelles
différences faites-vous entre les proprités `display`
et `visibility` ?
8. Etudiez ce [document HTML](/uploads/docs/doc04/exemples/mystere.html) et
sa [feuille de style](/uploads/docs/doc04/exemples/styleMystere.css)
9. Ajoutez le code Javascript qui permet d'afficher le contenu de
l'élément identifié `txtcache` lorsque l'on clique sur
le "bouton" _Montrer_ et de le masquer avec le
bouton _Cacher_. Faites une première version en jouant sur
l'attribut `display` et une seconde pour
l'attribut `visibility`.
10. Faites des modifications afin que seul le bouton utile (ou
pertinent) soit affiché.




Il est possible de désabonner une fonction d'un événement. Cela se
réalise à l'aide de la
fonction `removeEventListener`. Dans la mesure où il peut
y avoir plusieurs abonnements pour une même fonction et plusieurs
fonctions pour un même abonnement il est nécessaire de préciser à la
fois le type de l'événement et la fonction désabonnée. La
syntaxe d'un désabonnement est donc :

~~~javascript
element.removeEventListener(typeEvenement,fonctionDeclenchee)
~~~




En s'appuyant sur les travaux précédents, créez une page HTML avec
un bloc `div` identifié, telle que



1. un clic sur cet élément lui attribue une couleur de fond
aléatoire et la couleur de texte "complémentaire",
2. le second clic ne modifie plus les couleurs mais produit une
alerte annonçant "Cela ne marche qu'une
fois !",
3. les autres clics restent sans effet.






![eclipse](/uploads/docs/doc04/exemples/eclipse.jpg)

![soleil](/uploads/docs/doc04/exemples/soleil.jpg)


Récupérez les deux images sur la droite et, en utilisant les possibilités d'abonnement/désabonnement, créez une page HTML qui contient **un seul** élément `img` dont le contenu passe à chaque fois que l'on clique dessus d'une image à l'autre.
