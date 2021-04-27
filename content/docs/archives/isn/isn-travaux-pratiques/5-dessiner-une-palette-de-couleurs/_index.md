---
author: qu3nt1n
date: 2016-07-02 11:33:20+00:00
draft: false
title: 5. Dessiner une palette de couleurs
weight: 7
---





Notions abordées / pré-requis



* le codage des couleurs
* propriétés CSS modifiant les couleurs
* programmation évènementielle
* fonctions


Nouvelles notions



* boucle pour








Toujours en cours de rédaction







L'objectif de cette séance est d'écrire le code nécessaire à
l'affichage d'une palette de couleurs. Pour aller plus loin on pourra
même imaginer transformer cette palette en palette interactive pour
modifier dynamiquement les couleurs des éléments d'une page HTML.






# Codage des couleurs





## Rappels






Vous avez déjà discuté de la manière dont on codait des
couleurs. Chaque couleur est codée en un nombre qui représente le
niveau, c'est-à-dire l'intensité, de rouge, de vert et de bleu qui,
une fois mélangés feront la couleur. On se souvient aussi qu'au noir
on fait correspondre le nombre 0 et qu'au blanc on fait correspondre
le nombre 256^3-1. Lorsque le nombre est représenté de manière
hexadécimale, chaque composante est représentée par 2 digits, variant
de 00 à FF (en décimale de 0 à 255). Ainsi le noir correspond à 000000 et le blanc à FFFFFF.







Sachant que la couleur jaune est un mélange de rouge et de vert,
quel sera le nombre qui représentera le jaune (en codage
héxadécimal).







En HTML/CSS on peut modifier les couleurs des éléments de la page. La
propriété permettant d'ajuster la couleur du texte
est `color` alors que la propriété permettant d'ajuster la
couleur de fond est `background-color`. On se rappelle aussi qu'en HTML le code couleur hexadécimal doit être précédé par #.







Ecrire une page HTML avec un texte en rouge sur fond jaune. Vous définirez un style CSS nommé `rougesurjaune`.






## Changer la couleur de manière aléatoire






On souhaite maintenant créer un carré de couleur qui, lorsqu'on clique dessus, voit sa couleur modifiée. On donne ci-dessous le code d'une page HTML permettant de créer un carré qui au départ est rouge.






~~~html
    <html>

      <head>

        <meta charset="utf-8"></meta>
        <style type="text/css">

          .carre {
          display: inline-block; /* sert à ne pas avoir de retour à la ligne apres un div */
          margin : 5;
          width  : 20;
          height : 20;
          border : thin solid black;
          background-color : #FF0000;
          }

        </style>

      </head>

      <body>

        <div class="carre" id="monCarre">
        </div>
    </body>
    </html>
~~~html






Ce carré est nommé `monCarre`, nous pourrons donc modifier
sa propriété CSS de couleur de fond et réaliser cela dynamiquement en
utilisant la programmation événementielle. Le code pour modifier la
propriété CSS est le suivant.





~~~javascript
    document.getElementById("monCarre").style.background = "#00FF00";
~~~







Reprendre le code de la page HTML donné plus haut et ajouter le code
JavaScript permettant de modifier le couleur.







La propriété de couleur doit être donnée sous la forme d'une chaîne de
caratères débutant par `#` représentant un nombre
hexadécimal sur 6 digits. On fournit la fonction JavaScript suivante
qui permet de transformer un nombre décimal en un nombre bien formatté
pour les propriétés de couleur CSS.





~~~javascript
// transforme le nombre d exprimé en décimal
// en une chaîne de caratères représentant le nombre
// en hexadécimal sur 6 digits
function decimalToHex (d) {
  var hex = Number(d).toString(16);
  var padding = 6 - hex.length;
  // ajoute des 0 en tête de la chaîne pour obtenir 6 digits
  for (var i = 0; i < padding; i++) {
    hex = "0" + hex;
  }
  // enfin, ajoute # devant la chaîne de caractères
  return "#"+hex;
}
~~~







Ajouter dans votre page ce code JavaScript puis créer une
fonction `couleurAleatoire` qui retourne une couleur
aléatoire sous forme d'une chaîne de caratère formattée pour les
propriétés de couleur CSS.







On est prêt maintenant pour ajouter une action de changement de
couleur sur l'élément `monCarre`.







On rappelle que le code suivant :






~~~javascript
document.getElementById('monCarre').addEventListener("click",changeCouleurMonCarre);
~~~






a pour effet d'abonner la fonction `changeCouleurMonCarre` à un
l'évènement `click` sur l'objet `monCarre`.







Ajouter au code JavaScript de votre page une
fonction `changeCouleurAleatoire` qui prend en paramètre
l'identifiant d'un élément de la page et qui a pour effet
d'attribuer une couleur aléatoire à cet élément.







Ajouter au code JavaScript de votre page une
fonction `changeCouleurMonCarre` qui aura pour effet
d'attribuer une couleur aléatoire à
l'objet `monCarre`. Puis ajouter le code JavaScript
d'abonnement de cette fonction. Tester, vous devriez pouvoir
modifier la couleur du carré en cliquant dessus.








# Répéter ... sans répéter






Dans les programmes que nous avons écrits dans les activités
précédentes, les instructions étaient le plus souvent executés une
seule fois, comme par exemple dans le code ci-dessous :






~~~javascript
x = 1;
y = x * x;
document.write(x + " * " + x + " = " + y);
~~~



où les instructions 1 et 2 sont exéutées une seule fois. Si nous
voulons calculer le carré de 1 et le carré de 2 on sera alors obligé
d'écrire :






~~~javascript
x = 1;
y = x * x;
document.write(x + " * " + x + " = " + y);
x = 2;
y = x * x;
document.write(x + " * " + x + " = " + y);
~~~






Notez l'opérateur `+` sur les chaînes de caractères qui permet de concaténer des chaînes entre-elles, c'est-à-dire de coller des chaînes de caractères les unes derrière les autres. Lorsqu'on concatène un entier à une chaîne, celui-ci est automatiquement transformé en une chaîne.







Nous avons vu que pour éviter la recopie du code et faciliter sa
réutilisabilité (et sa maintenance), nous pouvions utiliser des
fonctions. On peut donc imaginer une fonction `carre`, qui
réalise le calcul du carré, et une
fonction `imprimer_carre`, qui utilise la
fonction `carre` et réalise l'affichage. Cela permettra
une meilleure écriture du code ci-dessus.





~~~javascript
function carre (x) {
  return x * x;
}

function imprimer_carre (x) {
  var y = x * x;
  document.write(x + " * " + x + " = " + y);
}

x = 1;
imprimer_carre (x);
x = 2;
imprimer_carre (x);

~~~







Les instructions des fonctions sont exécutées plusieurs fois. Mais
celles-ci ne produisent pas le même résultat qui dépend des
paramètres de la fonction.







Mais nous n'avons fait que repousser le problème. Imaginons maintenant
vouloir imprimer tous les carrés de 1 à 10, cela nécessitera de
répéter les instructions ci-dessus 10 fois.





~~~javascript
for (i = 1; i <= 10; i++) {
  document.write("x = " + i + ";</br>");
  document.write(imprime_carre(x)+"</br>");
}
~~~






## La boucle pour






Il arrive bien souvent, comme dans l'exemple ci-dessus, qu'on
veuille répéter un ensemble
d'instructions un nombre fini de fois :
écrire des tables de multiplications, écrire un calendrier, calculer
les termes d'une suite, etc.







Bien entendu, nous préférerions pouvoir écrire une seule instruction,
et indiquer au programme qu'elle doit s'exécuter plusieurs fois plutôt
que de l'écrire à la main.







Nous allons donc découvrir une nouvelle instruction,
la boucle, qui va nous permettre de
réaliser cela. Plus précisément nous allons introduire un type de
boucle qui s'appelle la boucle pour. La
boucle pour a pour particularité de permettre la répétion d'un
ensemble d'instructions un nombre fini de fois, connu à l'avance.







En Javascrit, répéter 52 fois l'affichage du mot semaine s'écrira :






~~~javascript
for (var i = 1; i <= 52; i++) {
  document.write("semaine");
}
~~~






ce qui se lit : _pour i allant de 1 à 52 exécuter
l'instruction `document.write("semaine")`_.







La variable `i` est appelée
la variable de boucle.







Détaillons la syntaxe. Après le mot-clé `for` on trouve
trois instructions entre les parenthèses :






* la première instruction détermine l'action
faite avant la première exécution du
bloc d'instructions entre les accolades : on y initialise la variable
de boucle
* la seconde instruction est le test
d'arrêt de la boucle, ce test est
réalisé avant l'exécution du bloc
d'instructions, dès qu'il est faux alors le bloc d'instructions n'est
pas réalisé et on sort de la boucle : on y indique la valeur maximale que peut atteindre la variable de boucle
* la troisième instruction est l'action
exécutée après l'exécution du bloc
d'instructions : on y modifie la variable de boucle




Les instructions mises entre les parenthèses d'une boucle pour peuvent être n'importe lesquelles. Cependant, on respectera scrupuleusement la règle qu'elles ne servent qu'à initialiser la variable de boucle, régler son incrément, déterminer la valeur maximale de la variable de boucle.








Ainsi, dans l'exemple, on commence par déclarer et initialiser la
variable `i` à 1, puis, tant que la valeur
de `i` est inférieure ou égale à 52, on incrémente la
variable `i`.







La variable de boucle ne doit pas être
modifiée dans le bloc d'instructions de la boucle, mais elle
peut bien sûr être utilisée, comme c'est fait dans l'exemple
ci-dessous.





~~~javascript
for (var i = 1; i <= 52; i++) {
  document.write("semaine " + i);
}
~~~







Recopiez le code Javascript ci-dessus dans une page et observez son exécution.







Modifiez maintenant le code pour que chaque semaine soit écrite sur une ligne.







Ecrire maintenant une page et le code Javascript permettant d'afficher
la table de multiplication de 8.







La valeur initiale donnée à la variable de boucle, l'incrément ainsi
que la valeur maximale atteinte par la variable de boucle peuvent être
définie dans des variables. Par exemple, si on souhaite énumérer les
nombres multiple à la fois de 3 et de 5 entre 0 et 100 on pourra
écrire :



Pour savoir si un nombre p est multiple de q, il suffit de savoir si
le reste de la division entière de p par q vaut 0. Par exemple, le
reste de la division entière de 17 par 5 est 2 (17 = 3*5+2) et donc 17
n'est pas divisible par 5. L'opérateur `%` fournit le reste
de la division entière.









~~~javascript
var i = 0;
for (i = 0; i < 100; i++) {
  if ((i % 3 == 0) && (i % 5 == 0)) {
    document.write(i + " ");
  }
}
~~~





mais il serait préférable d'écrire :






~~~javascript
var i = 0;
var max = 100;
for (i = 0; i < max; i++) {
  if ((i % 3 == 0) && (i % 5 == 0)) {
    document.write(i + " ");
  }
}
~~~






Il faut faire attention en écrivant la condition. En effet, celle-ci est évaluée à chaque tour de boucle, et donc si la variable `max` de notre exemple était modifiée dans le bloc d'instructions de la boucle, le nombre d'itérations de cette dernière serait modifié. Pire, si `max` était incrémenté de 1 à chaque tour, on aboutirait à une boucle infinie. C'est pourquoi on s'interdit de modifier les variables sur lesquels le test est réalisé dans le bloc d'instructions de la boucle : il faut toujours pouvoir prédire à l'avance combien d'itérations sont effectuées.






et on pourrait même en faire une fonction :






~~~javascript
function imprimer_multiples_de_2_et_3 (max) {
  var i = 0;
  for (i = 0; i < max; i++) {
    if ((i % 3 == 0) && (i % 5 == 0)) {
      document.write(i + " ");
    }
  }
}
~~~





## Retour aux couleurs






Nous allons mettre en oeuvre cette nouvelle notion de boucle pour afin
de construire la palette de couleurs annoncée au début de cette
activité.







Dans un premier temps, nous allons commencer par créer des carrés de
couleur aléatoire.







Reprendre la page HTML dans laquelle nous avions dessiné des carrés de
couleur aléatoire. Ecrire le code JavaScript permettant l'affichage de
64 carrés grâce à l'utilisation de la boucle pour. Cela revient à
créer 64 balises `

`.







Maintenant nous allons modifier la couleur de chacun des carrés pour
obtenir 64 carrés alétoires.







Modifier le code précédent pour donner un `id` différent à
chaque carré. Par exemple, le premier carré pourra avoir
l'identifiant `carre1`, le second
l'identifiant `carre2`, ... , et le dernier
l'identidiant `carre64` (il suffit d'utiliser la concaténation de chaînes comme vu plus haut).







On peut aussi mettre les deux instructions, celle qui crée le div et celle qui modifie sa propriété de background dans une seule boucle. Il faut juste que l'élément soit déclaré, et donc présent dans l'arbre DOM, avant de pourvoir le modifier. Ce qui paraît logique.






Ajouter maintenant le code permettant d'affecter une couleur aléatoire
à chacun des carré. Cela nécessite l'écriture d'une autre boucle
pour. Etant donné un identifiant d'un carré, il suffit d'appeler la
fonction `changeCouleurAleatoire` écrite lors d'une
précédente manip.






## La palette






Maintenant nous aimerions contrôler la couleur affecter à chacun des
carrés pour avoir une palette de 64 couleurs équitablement réparties
sur l'ensemble des 256*256*256 couleurs possibles.







Nous allons tenter d'utiliser une boucle pour avec un incrément plus
grand que 1 pour réaliser cela.







Quel est l'incrément qu'il va falloir choisir pour obtenir 64 nombres
entre 0 et 256^3 ? Ecrire une boucle pour imprimer ces nombres afin de
vérifier la valeur d'incrément retenue.








Désormais nous avons le codage décimal des couleurs. Il reste à
afficher les carrés de couleur et à associer la bonne couleur à chaque
carré.







Créer une fonction `changeCouleur` qui prend en paramètre
l'identifiant d'un élément de la page et le code décimal d'une couleur
et modifie la propriété de couleur de fond de l'élément.







Reprendre le code qui avait permis l'affichage des 64 carrés de
couleur aléatoire puis le modifier pour obtenir 64 carrés de couleurs
uniformément réparties. Qu'observez-vous ?







En fait, lorsqu'on procède de la sorte, on réalise une variation sur
une couleur de base, dans une seule composante. En effet, si on
affiche le code hexadécimal des couleurs envisagées, on obtient :







    #000000 #040000 #080000 #0c0000 #100000 #140000 #180000 ...







Or nous souhaitons avoir une variation sur les 3 composantes à la
fois, c'est-à-dire 4 variations de rouge, 4 variations de vert, 4
variations de bleu (4 * 4 * 4 = 64). Il faut donc s'y prendre autrement.








On propose la solution suivante, qui permettra d'obtenir une palette
de 4*4 = 16 couleurs. Cette solution utilise deux boucles pour imbriquées.






~~~javascript
var i = 0, j = 0;
for (i = 0; i < 256; i = i + 85) {
  for (j = 0; j < 256; j = j + 85) {
    var couleur = 256 * i + j;
    document.write("<div class="carre" id="carre" + couleur + ""></div>");
    changeCouleur("carre"+couleur,couleur);
  }
}
~~~






Créer une nouvelle page HTML avec le code JavaScript ci-dessous (dans
oublier la fonction `decimalToHex`) et observer si le
résultat est conforme à celui attendu.







Déterminer combien de fois la seconde boucle est réalisée.







Déterminer combien de fois la première boucle est réalisée.







Déterminer combien de fois la fonction `changeCouleur` est appelée.







Pourquoi la variable couleur est-elle calculée en multipliant la
valeur de `i` par 256 ?  Lister toutes les valeurs prises
par la variable `couleur`.






### A vous de jouer






Maintenant que vous avez vu une solution permettant d'avoir 16
variations de couleur sur 2 composantes, proposez une solution
permettant d'avoir 64 variations de couleurs sur 3 composantes.








Pour aller plus loin, vous pourriez demander à l'utilisateur de donner
le nombre de variations par couleur qu'il souhaite, puis calculer
l'incrément nécessaire par composante, et afficher la palette.
