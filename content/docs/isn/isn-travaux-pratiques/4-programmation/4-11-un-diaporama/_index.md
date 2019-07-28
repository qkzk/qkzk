---
author: qu3nt1n
date: 2016-07-02 10:49:32+00:00
draft: false
title: 4.11 Un diaporama
weight: 11

---



Notions abordées dans cette page



* applications de différentes notions abordées auparavant
* provoquer le besoin de la structure tableau
* javascript : "timer"








# Un premier diaporama





## Version 1





Récupérez les 4 images suivantes :

![](http://qkzk.xyz/docs/doc04/images/ballade-des-oliviers.jpg)

![](http://qkzk.xyz/docs/doc04/images/vallon-pont-darc.jpg)

![](http://qkzk.xyz/docs/doc04/images/pont-du-gard.jpg)

![](http://qkzk.xyz/docs/doc04/images/fontenay.jpg)



On souhaite disposer d'une page html qui permettent d'afficher ces
images les unes après les autres dans cet ordre.



Cette page comportera deux "zones boutons" et un élément `img`. Le premier pour afficher à l'image précédente à
l'image courante, sauf si c'est la première et dans ce cas il ne se
passe rien. Le second pour afficher l'image suivante de l'image
actuelle, sauf si c'est la dernière et dans ce cas il ne se passe
rien.




Réalisez une telle page html et sa feuille de style.


Pour cela il faut qu'un clic sur une "zone bouton"
provoque la modification du contenu de la source
(attribut `src`) de l'élément `img` en le
  remplaçant par le texte correspondnat à l'image suivante ou précédente.










## Version 2 : modifions les images






Récupérez l'image supplémentaire suivante :

![](http://qkzk.xyz/docs/doc04/images/colisee-rome.jpg)






1. Faites les modifications permettant de remplacer l'image de
l'abbaye de Fontenay pas cette image.
2. Testez votre solution.
3. Faites les modifications permettant d'ajouter cette image à la fin
dans le diaporama initial.
4. Testez votre solution.
5. Faites les modifications permettant d'insérer cette image dans le diaporama initial entre
la seconde et la troisième image.
6. Testez votre solution.
7. Faites les modifications permettant de supprimer la dernière des images du  diaporama.

8. Testez  votre solution.
9. Faites les modifications nécessaires pour que les images
apparaissent désormais dans cet ordre :

![](http://qkzk.xyz/docs/doc04/images/vallon-pont-darc.jpg)

![](http://qkzk.xyz/docs/doc04/images/pont-du-gard.jpg)

![](http://qkzk.xyz/docs/doc04/images/colisee-rome.jpg)

![](http://qkzk.xyz/docs/doc04/images/ballade-des-oliviers.jpg)


10. Testez votre solution.
11. Que pensez-vous de la facilité d'ajout, de suppression ou
de  modification d'ordre des images ?


Qu'en serait-il si nous avions 20 images à afficher et que l'on
souhaitait :
* en changer l'ordre ?
* en supprimer 4 au hasard ?
* en ajouter cinq autres à des
positions quelconques ?
* tout cela à la fois ?
* et pour 100 images ? 1000 ?








## Version 3












1. Créez 4
variables `image1Src`, `image2Src`, `image3Src`
et `image4Src` que vous initialiserez respectivement avec
les chaînes de caractères correspondant aux
attributs `src` des 4 images du diaporama.

2. Reprenez le diaporama de la première **Manip'** en utilisant
ces 4 variables (plutôt que les chemins explicites  des
images).


Il peut être utile de disposer d'une variable supplémentaire
qui mémorise le "numéro" de la source de l'image courante.
3. Testez.
4. Faites et testez successivement les modifications suivantes :

  1. remplacer l'image de l'abbaye de Fontenay par celle  du Colisée de Rome.
  2. ajouter l'image du Colisée de Rome en
fin de ce "nouveau" diaporama.
  3. insérer l'image du Colisée de Rome entre la deuxième et la
troisième image du diaporama initial.
  4. changer l'ordre d'apparition des images.


5. Que pensez-vous de la facilité de ces modifications en comparaison
de la situation de la **Manip'2** ?
6. Qu'est-ce qui rend les choses plus faciles ?
7. Qu'en serait-il avec 20 images ? 100 ? 1000 ?







L'utilisation de variables facilite les modifications puisqu'il suffit
de changer la valeur de la variable sans modifier le code des
fonctions pour modifier le diaporama.





Cependant cette approche n'est pas satisfaisante si l'on doit
manipuler beaucoup d'images car elle nécessite la création de
nombreuses variables. De plus, la modification du nombre d'images
prises en compte n'est pas pratique. En cas de diminution de ce nombre
on se trouve avec des variables inutiles et en cas d'augmentation il
faut en créer des nouvelles.






Pour corriger ces problèmes et éviter la création d'un nombre
  important de variables représentant des données similaires, ici les
  chemins sources des images, on peut utiliser une donnée de type tableau.




# Les tableaux






De fait javascript accepte que les éléments d'un tableau soient de
types différents. On peut ainsi placer un booléen dans la première
case et un entier dans la seconde. Cependant dans la plupart des
langages, les éléments d'un tableau sont obligatoirement d'un même
type. Nous respecterons donc cette approche.






Les tableaux sont des structures de données permettant de stocker et
manipuler un nombre déterminé de données toutes de même
type. Plusieurs structures de données permettent un tel stockage. Ce
qui caractérise les tableaux, c'est que chacun de leurs éléments
possède une adresse qui permet l'accès direct à cet élément dans la
structure. Cette adresse est constituée d'un ou
plusieurs indices.





Lorsque l'accès à un
élément s'effectue à l'aide d'un seul indice, on dit que le tableau
est à une dimension.  On parle alors
parfois aussi nommés _vecteurs_. Les tableaux à une dimension
sont représentés de manière classique sous forme de cases contigües
contenant les valeurs des éléments du tableau. On parle donc ainsi
assez facilement de "cases" pour évoquer les éléments d'un tableau.






Un échiquier est un exemple de
tableaux à deux dimensions et les joueurs d'échec utilisent un système
d'indices pour désigner une classe : des lettres pour les
colonnes et des chiffres pour les lignes. On démarre la
numérotation en bas à gauche de l'échiquier. La case **B3** est ainsi
la case de la deuxième colonne et troisième ligne






S'il faut deux indices, le tableau est à deux dimensions et est
également appelé _matrices_. On le représente classiquement par
une grille rectangulaire, l'un des indices représentent alors les
colonnes et le second les lignes.






## Manipulations de base en javascript






Ce n'est pas le cas dans tous les langages, mais en javascript la
taille des tableaux peut varier en fonction de l'indice des éléments
que l'on définit. Ainsi si pour la variable `unTableau`
ci-contre on définit l'élément d'indice
7 `unTableau[7]=12`, alors le nombre d'éléments passent
automatiquement à 8. On n'est donc pas contraint en javascript de
préciser la taille du tableau à la création,  `new
  Array()` suffit. La taille du tableau sera
définie implicitement par les manipulations.





En javascript le type tableau est nommé `Array`. Pour
définir un tableau il faut le créer et on peut préciser à la création
le nombre d'éléments que contiendra le tableau :






    var unTableau = new Array(5);   // crée un tableau à 5 éléments







La variable tableau ainsi créée comporte dont 5 éléments. L'adresse
de ces éléments est donc identifiée par leur indice qui est leur numéro
d'ordre dans le tableau, le premier ayant le numéro 0. Le dernier
élément a donc toujours pour numéro "_nombre d'éléments du tableau
moins 1_". La référence à un élément du tableau se fait en utilisant
la notation indicée :






~~~javascript
    unTableau[0] = 3;                 // le premier élément du tableau prend la valeur 3
    document.writeln(unTableau[0]));  // affiche la valeur du 1er élément du tableau
    unTableau[3] = 5;                 // fixe à 5 la valeur du quatrième élément du tableau
    var i = 2;
    unTableau[i] = -4;                // fixe la valeur du 3ème élément
    document.writeln(unTableau[i+1]); // affiche la valeur du 4ème élément
~~~






Un tableau de taille _n_ peut donc être considéré comme le
regroupement de _n_ variables dont les identificateurs sont
formés par le nom du tableau suivi d'un entier entre 0 et _n-1_
noté entre crochets. Chaque élément du tableau peut donc être
utilisé et manipulé comme une variable "habituelle".  En
particulier, un élément du tableau dont la valeur n'aura pas été
initialisée vaut `undefined`.





La propriété `length` d'un tableau permet de connaître
le nombre d'éléments d'un tableau. L'indice du dernier élément (la
"dernière case") du tableau est donc
toujours `unTableau.length-1`.






On peut également créer un tableau et définir ses éléments par
énumération explicite. Ainsi la déclaration :





~~~javascript
var arcEnCiel = ["rouge","orange","jaune","vert","bleu","indigo","violet";];
~~~




définit une variable tableau `arcEnCiel` de taille 7
dont le premier élément (`arcEnCiel[0]`)
vaut `"rouge"`, le second vaut `"orange"`, etc.







## Application : diaporama version 4







1. Définissez une variable tableau `tableauSrcImage` par énumération des chaînes de caractères représentant les chemins sources des 4 images du diaporama initial.
2. Définissez une variable `indiceImage` qui représentera l'indice de l'image courante. Initialement cette variable vaut 0.
3. Définissez une fonction `afficheImage` qui fixe la source de l'élément image de la page à la valeur de l'élément d'indice `indiceImage` du tableau `tableauSrcImage`.
4. Définissez une fonction `imageSuivante` qui :

    1. augmente de 1 (incrémente) la valeur de `indiceImage` si celle-ci reste strictement inférieure au nombre d'éléments de `tableauSrcImage`, sinon laisse `indiceImage` inchangé
    2. affiche l'image correspondant à la nouvelle valeur de `indiceImage`.


5. Réalisez une fonction similaire `imagePrecedente`.
6. Réalisez la version 4 du diaporama utilisant ces differentes définitions.
7. Testez.
8. Faites des modifications :

  * ajoutez le colisée en modifiant la définition par énumération du tableau
  * supprimez une image
  * modifiez l'ordre des images


9. Que pensez-vous de la facilité (ou non) de ces modifications ? Le problème serait-il différent pour 20, 100, 1000 images ? (à part les textes à saisir bie sûr mais on ne peut faire moins).








## Un "vrai" diaporama...





Nous avons mis en place les outils pour visualiser une séquence
d'images par des clics successifs. Mais avec le terme diaporama on
sous-entend généralement souvent que les images s'enchainent
"automatiquement". Pour aller un peu plus loin et compléter notre
diaporama nous allons voir comment ajouter cette fontionnalité.






On peut aussi utiliser des timers pour exécuter une seule fois une
fonction après un délai fixé par la méthode `window.setTimeOut(_fonction_,_delai_)`.






Il nous faut pour cela utiliser un _timer_. Un timer permet de
declencher à intervalles réguliers l'exécution d'une fonction. On
crée et démarre un timer grâce à la
fonction `window.setInterval` à laquelle on passe en
paramètre la fonction à exécuter et sa périodicité (en nombre de ms). En retour cette
méthode fournit le timer créé. Ainsi






    var monTimer = window.setInterval(uneFonction,1000);





provoque l'exécution de la
fonction `_uneFonction_` toutes les secondes et
initialise `monTimer` avec le timer responsable de cette
exécution.





On eut arrêter l'exécution périodique d'un timer à l'aide de la
méthode `window.clearInterval` en lui passant en
paramètre le timer que l'on veut interrompre. Par exemple :






    window.clearInterval(monTimer);





interrompt le timer précédent.






Testez [cette page](http://qkzk.xyz/docs/doc04/exemples/exemple_timer.html) et étudiez le [code javascript](http://qkzk.xyz/docs/doc04/exemples/exemple_timer.js) qui l'accompagne, notamment les fonctions `start` et `stop` et leur usage.







Inspirez-vous de ce code pour compléter le diaporama :

* ajoutez la possibilité de démarrer et arrêter le diaporama et
passer d'une image à la suivante à intervalle régulier. modifiez le
comportement des versions précédentes pour qu'une fois arrivé à la
dernière image on recommence à la première.
* ajoutez une zone de saisie dans laquelle on peut fixer le nombre
de secondes de pause entre chaque image du diaporama
* ajouter une zone qui affiche le numéro de l'image affichée (par
exemple _3/5_ pour la 3ème image sur 5 images possibles)
* modifiez le comportement pour que l'image suivante soit choisie
aléatoirement (ce choix aléatoire ou non pourrait-être activé par
un clic...)
* peut-être aurez-vous d'autres idées de modifications ?
* Testez !
