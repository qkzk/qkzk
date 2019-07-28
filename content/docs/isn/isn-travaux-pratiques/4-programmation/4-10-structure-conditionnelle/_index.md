---
author: qu3nt1n
date: 2016-07-02 10:37:38+00:00
draft: false
title: 4.10 Structure conditionnelle
weight: 10
---


Pré-requis On suppose qu'ont été vues les notions de :



  * le  calcul booléen et le type booléen (partie 3)


Notions abordées dans cette page



  * structure conditionnelle
  * booléens










#  Des traitements sous condition





Nous avons précédemment rencontré la **Manip'** suivante :






  1. Récupérez et étudiez ce [document HTML](http://qkzk.xyz/docs/doc04/exemples/temperature.html) et sa [feuille de style](http://qkzk.xyz/docs/doc04/exemples/styleTemperature.css).
  2. Un événement `change` est déclenché à chaque fois que la valeur d'un élément `input` est modifiée par l'utilisateur (l'événement est activé lorsque l'on "quitte" l'élément `input` - on dit qu'il perd le focus). En partant du travail lors la **Manip** sur conversion de température, ajoutez à ce document le code Javascript qui permet lors d'une saisie (numérique, **_on ne s'occupera pas pour l'instant de ce qui se passe dans un autre cas_**) dans un champ à la valeur correspondante pour l'autre unité de mesure de afficher dans l'autre champ.

  3. Testez évidemment...







Il avait alors été fait la remarque "_on ne
  s'occupera pas pour l'instant de ce qui se passe dans un autre
  cas_" n'était pas très satisfaisante et qu'il "_faudra bien un
  jour que l'on se penche sur ce problème et que l'on étudie comment
  on peut le résoudre_". Et bien disons que ce jour est arrivé.






Reprenez la solution que vous avez produite, ou utilisez [celle-ci](http://qkzk.xyz/docs/doc04/exemples/temperatureComplet.html) et son [code javascript](http://qkzk.xyz/docs/doc04/exemples/temperature.js),  pour la Manip' précédente et testez ce qu'il se passe avec une saisie non numérique.






Pour éviter ce dysfonctionnement, on ne peut pas simplement se
  rabattre sur l'utilisateur. Même si on peut (dans ce cas précis)
  s'attendre à qu'il fournisse a priori une valeur numérique, une
  faute de frappe est toujours possible et on peut rencontrer d'autres
  situations similaires où la nature de la valeur à saisir est moins
  évidente.






  C'est au programmeur de faire en sorte que son programme
  soit **robuste**, c'est-à-dire qu'il résiste à des conditions
  d'utilisation "anormales" (pour lesquelles il n'est pas a priori
  prévu). Dans notre cas, le cas "normal" est celui où l'on cherche à
  convertir une valeur numérique en degrés Fahrenheit ou Celsius. Un
  cas "anormal" est celui où on essaie de le faire avec une valeur non
  numérique et le programme doit alors être capable de réaliser un
  traitement qui prend en compte cette situation.






Dans notre cas on peut par exemple décider que si la saisie de
  l'utilisateur ne correspond pas à un nombre, la valeur 100 sera
  prise par défaut. L'énoncé de la question 2 devient alors :
  "_ajoutez à ce document le code Javascript qui permet que lors
  d'une saisie numérique dans un champ, la valeur correspondante pour
  l'autre unité de mesure s'affiche dans l'autre champ. Une saisie non
  numérique sera remplacée par défaut par la valeur 100 et la
  conversion sera réalisée.  _"






Considérons le code de la
  fonction `fahrenheitVersCelsius` déclenchée par
  l'événement `change` sur
  l'élément `tFahrenheit` :







    var fahrenheitVersCelsius = function() {
        var tFahrenheit =  document.getElementById("tFahrenheit");
        var tempF = parseInt(tFahrenheit.value);
        var tCelsius = document.getElementById("tCelsius");
        tCelsius.value = ((tempF - 32) *  5 / 9).toFixed(2);
    }






Que faudrait-il changer dans cette fonction pour pouvoir prendre en
  compte le nouveau cahier des charges et sa valeur par défaut en cas
  de saisie ? Une étude de ce code, que peut compléter un examen
  pas-à-pas de son exécution avec Firebug, permet de se rendre compte
  que si la saisie n'est pas numérique `tempF` prend,
  logiquement, la valeur `NaN`. Le résultat
  de `((tempF - 32) *  5 / 9)` ne peut donc à partir de ce
  moment là qu'être lui aussi `NaN`. Pour pouvoir obtenir le
  comportement souhaité, il faut donc remplacer la valeur
  de `tempF` par `100` lorsqu'elle
  vaut `NaN` et la laisser inchangée dans le cas contraire.






Nous sommes donc confrontés à la situation où la réalisation d'un
  traitement, ici fixer la valeur de `tempF`
  à `100`, ne doit être réalisée
  qu'à condition que sa valeur
  soit `NaN`.
  Une telle situation est très fréquente en programmation et
  Javascript, comme tous les langages de programmation, propose une
  structure de contrôle appelée structure
  conditionnelle qui permet de ne réaliser un traitement que si
  une certaine condition est vérifiée (on dit
  aussi _réalisée_). Sa syntaxe est la suivante :







    if (condition) {
      traitement à réaliser
    }






où _condition_ est une expression à valeur
  booléenne. Attention les parenthèses autour de _condition_
  font partie de la syntaxe et sont donc obligatoires.





Lors du traitement de cette expression, _condition_ est
  évaluée. Si elle vaut `true` alors le code
  de _traitement à réaliser_ est exécutée, sinon rien ne se
  passe.






Dans notre cas il nous suffit donc de trouver une expression qui
  ait pour résultat la valeur `true`
  si `tempF` vaut `NaN` et `false`
  sinon. La fonction `isNaN` est toute désignée :







  **nom** : isNaN

  **Paramètres** : 1

  ** val** : une valeur

  **Résultat** :

  ** type** : un booléen

  ** description** : true si et
  seulement val vaut la valeur NaN







Le traitement à réaliser quand `tempF`
  vaut `NaN` est de fixer la valeur de `tempF` à
  100, sans oublier de changer le contenu du champ de saisie. On
  obtient alors le nouveau code :







    var fahrenheitVersCelsius = function() {
        var tFahrenheit =  document.getElementById("tFahrenheit");
        var tempF = parseInt(tFahrenheit.value);
        if (isNaN(tempF)) {
           tempF = 100;
           tFahrenheit.value = 100;
        }
        var tCelsius = document.getElementById("tCelsius");
        tCelsius.value = ((tempF - 32) *  5 / 9).toFixed(2);
    }










  1. Faites la modification similaire pour l'autre fonction de
  conversion de températures.

  2. Testez.
  3. Combien de tests devez-vous faire au minimum pour vous assurer que votre programme fonctionne correctement (c'est-à-dire comme vous l'avez prévu) ?








Le choix qui a été fait de prendre la valeur 100 par défaut en cas de mauvaise saisie était arbitraire. On aurait pu en faire un autre, comme celui de ne pas faire de calcul dans ce cas mais effacer le contenu des deux zones de saisie des températures.



  1. Modifiez le travail précédent pour obtenir ce comportement.

  2.
Testez.









Observez la valeur de `image.width` pour
comprendre la nécessité de l'utilisation de la fonction `parseInt`.






Si la variable `image` a pour valeur un élément d'une page correspondant à une balise `img`, il est possible de connaître la largeur actuelle de cette image par l'expression `parseInt(image.width)` et de modifier la largeur d'affichage de cette même image par une expression telle que `image.style.width = "250px"`, par exemple.



  1. Créez une page html et sa feuille de style qui contiendra un élément de balise `img`.

  2.
  Ajoutez à cette page deux zones "bouton" telles que :

        * un clic sur la première diminue la taille de l'image de 20px si cette taille est supérieure à 100px, sinon rien ne se passe
        * un clic sur la seconde augmente la taille de l'image de 20px si cette taille est inférieure à 400px, sinon rien ne se passe








# Expression d'alternatives





Dans les situations rencontrées ci-dessus un traitement "particulier" est réalisé si une condition est vérifiée et dans le cas contraire on passe à loa suite sans aucun traitement   complémentaire. On rencontre cependant fréquemment la situation dans laquelle un autre traitement doit être réalisé lorsque la condition n'est pas vérifiée (càd vaut `false`). Il est possible de programmer un tel comportement en complétant la structure conditionnelle `if` par un bloc exprimant l'alternative et identifié par le mot-clé `else`. La syntaxe est alors :







    if (condition<)
      traitement_vrai (à réaliser si condition vaut true)
    }
    else {
      traitement_faut (à réaliser si condition vaut false)
    }






La sémantique d'une expression est la suivante : lors du
  traitement de cette expression, `condition` est
  évaluée. Si elle vaut `true` alors le
  code `traitement_vrai` est exécutée, sinon, c'est-à-dire
  si `condition` est évaluée à `false`, c'est le
  code `traitement_faux` qui est exécutée.






On retrouve la forme de phrases du langage courant telles que "_Si
c'est pile je gagne sinon je perds_."







  La restriction d'accès à l'image est ici toute symbolique puisqu'il
  suffit de consulter le code Javascript source pour connaître le mot
  secret et même le nom, et donc l'URL, de l'image "cachée".





Considérons l'exemple fourni
  par [cette page](http://qkzk.xyz/docs/doc04/exemples/sesame.html). Une image est
  affichée **si** l'utilisateur fourni le mot demandé **sinon** un message
  d'alerte apparaît. Ce comportement est produit par la
  fonction `sesame` appelée au chargement de la page :






    var sesame = function() {
        var motDePasse = window.prompt("Indiquez le mot secret pour voir l'image");
        if (motDePasse == "secret") {
    	var imagePrivee =  document.getElementById("privee");
    	imagePrivee.src = "orionMessier.jpg";
        }
        else {
    	window.alert("Vous n'avez pas fourni le mot secret.");
        }
    }







  Vous pouvez "habiller" votre page en remplaçant les
  boutons _Pile_ et _Face_ par des images correspondant
  d'une pièce de monnaie.






  Ecrivez une page html qui comporte :

      1. 2 boutons _Pile_ et _Face_ tels que le clic sur l'un
  de ces boutons affiche le texte "_vous avez choisi pile/face_"
  dans une zone prévue à cet effet
      2. 1 bouton _Lancer_ qui simule un lancer pièce en provoquant
  un tirage aléatoire (`Math.random`) qui correspond
  à _Pile_ si la valeur inférieure à 0,5 et à _face_ sinon,
  le texte "_le résultat du lancer est pile/face_" est affiché
  dans la page
      3. le texte "_GAGNE/PERDU_" est affiché dans une zone résultat
  selon que le résultat du tirage correspond ou non au choix de
  l'utilisateur








# Attention





Il est important de noter et de prendre conscience que l'expression






    if (condition) {
       traitement_vrai
    }
    else {
       traitement_faux
    }






n'est pas
  équivalente à la séquence






    if (condition) {
       traitement_vrai
    };
    if (! condition) {
       traitement_faux
    }






contrairement à ce que l'on peut peut-être penser dans une première
  impulsion qui s'avère fausse. On est éventuellement d'autant plus
  susceptible de commettre cette erreur logique que dans certains cas
  le comportement de ces deux expressions sont identiques. Ainsi les résultats des deux codes
  suivants sont équivalents :






    var alea = Math.random();                      var alea = Math.random();
    var resultat;                                  var resultat;
    if (alea < 0.5) {                              if (alea < 0.5) {
      resultat = "pile";                              resultat = "pile";
    }                                              };
    else {				    	       if (alea >= 0.5) {
      resultat = "face";		    	          resultat = "face";
    }	               		    	       }






Ce n'est cependant pas toujours le cas.






La fonction de Collatz est à la base d'une conjecture
appelée [conjecture
    de Collat ou de Syracuse](http://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) qui malgré sa simplicité d'énoncé
résiste aux mathématiciens depuis près d'un siècle.






La fonction de Collatz est une fonction qui prend pour paramère un
  entier _n_ et dont le résultat dépend de la parité
  de _n_. Ce résultat est _3*n+1_ si _n_ est impair
  et _n/2_ si _n_ est pair.







  Ecrivez la spécification de la fonction de Collatz.






On propose les deux codes suivants pour cette fonction :






On rappelle que l'opérateur modulo `%` fournit le reste de
la division entière. On peut donc tester la parité d'un
entier _n_ par l'expression `n%2==0`
ou `n%2==1`.






    var n = parseInt(window.prompt("Fournissez un entier positif"));
    if (n%2 == 1) {
      n = 3*n +1;
    }
    else {
      n = n/2;
    }
    document.writeln("la valeur de Collatz pour l'entier fourni est "+n);




et




    var n = parseInt(window.prompt("Fournissez un entier positif"));
    if (n%2 == 1) {
      n = 3*n +1;
    }
    if (n%2 ==0) {
      n = n/2;
    }
    document.writeln("la valeur de Collatz pour l'entier fourni est "+n);










        1. Créez deux pages html qui contiennent ces portions de scripts et faites
    plusieurs tests avec les mêmes valeurs de _n_ pour les deux
    pages.
        2. Que constatez-vous ?
        3. Expliquez.








# Des conditions en cascade





Les expressions conditionnelles permettent donc de distinguer deux
  situations différentes et d'exécuter alors deux traitements
  différents. La composition de plusieurs expressions conditionnelles
  permet alors de traiter les situations où il existe plus de deux cas
  qui diffèrent.






  Prenons l'exemple de ce jeu dans lequel un joueur choisit
  secrètement un nombre
  que doit deviner un autre joueur. Pour cela ce dernier propose un
  nombre et le premier lui indiqué s'il a trouvé le nombre secret ou
  si sa proposition lui est supérieur ou inférieur. On le constate
  trois cas de figure sont possibles. Si on
  appelle `nombreSecret` la variable dont la valeur est le nombre
  secret choisi et `proposition` la variable dont la valeur
  est le nombre proposé, la portion de code suivante permet alors de
  fixer la valeur d'une variable `resultat` en fonction de
  chacune des trois situations :







    if (proposition == nombreSecret) {
       resultat = "trouve";
    }
    else {                      // proposition n'est pas égale à nombreSecret
      if (proposition < nombreSecret) {
         resultat = "trop petit";
      }
      else {
         resultat = "trop grand";
      }
    }







La solution consiste à considérer plusieurs fois des alternatives
entre deux situations. Ici, on teste d'abord si la
proposition est ou non égale au nombre secret, puis dans le second cas on
teste si elle est ou non plus petite. Comme on sait déjà qu'elle
n'est pas égale, le cas `false` correspond nécessairement à
une valeur trop grande.








Nous verrons plus tard comment faire pour que le jeu se répète tant
que le nombre secret n'a pas été trouvé.







  Ecrivez une page html qui :

    1. choisit aléatoirement un nombre secret  entre 0
  et 100,
    2. demande à l'utilisateur de faire une proposition,
    3. affiche les deux nombres et le résultat de la comparaison.







  Il existe différents modèles de machines à sous, aussi appelées
  bandits manchots.  Un modèle simple consiste en 3 rouleaux
  comportant 5 symboles (représentés ici par les chiffres de 1 à 5) et
  des espaces entre 2 symboles (représentés ici par le chiffre
  0). Pour commencer, nous allons programmer une version simple de ce
  jeu avec une seule mise. Les combinaisons gagnantes et les gains
  correspondants sont indiqués ci-dessous.


          * 1 1 1 : 250
          * 2 2 2 : 150
          * 3 3 3 : 80
          * 4 4 4 : 50
          * 5 5 5 : 20
          * deux 1 parmis les 3 rouleaux : 5
          * un seul 1 parmis les 3 rouleaux : 2



      1.
  Réalisez une fonction qui effectue trois tirages aléatoires de
  chiffres compris entre 0 et 5 inclus, affiche la combinaison
  correspondante et a pour résultat les gains selon la combinaison obtenue.

      2.
  Ecrivez une page html qui permet de jouer à ce jeu et d'afficher les
  gains.








  Le type `Date` dispose de la fonction suivante :



   **type concerné :** Date

  **nom** : getDay

  **Paramètres** : 0

  **Résultat** :

  ** type** : un nombre

  ** description** : un entier qui correspond au jour de
    la semaine :    0 pour dimanche,  1 pour lundi, etc.





        1. Spécifiez puis codez une fonction `nomDuJour` qui prend
pour pparamètre un nombre entre 0 et 6 et a pour
résultat la chaîne de caractères du nom du jour correspondant.
        2. Sachant que le type `Date` dispose d'une
  méthode `getMonth` similaire où 0 correspond à janvier, 1
  à férvier, etc., spécifiez puis codez sur le même principe une fonction `nomDuMois`

        3.
  Utilisez ces fonctions pour créer une
  fonction `aujourdHui` dont le résultat est une chaîne de
  caractères représentant la date d'aujourd'hui sous la forme
  "_mardi 25 décembre 2012_".

        4.
  Testez vos fonctions dans une page html.
