---
author: qu3nt1n
date: 2016-07-02 08:08:27+00:00
draft: false
title: 3b.2 CSS intro
weight: 2
---


Pré-requis



* les bases d'html


Notions abordées dans cette page



* style css










#  Des pages html qui ont du style









1. Rendez-vous sur la page du [CSS Zen garden](http://www.csszengarden.com/) (ou sur la [page de la version française](http://www.csszengarden.com/tr/francais/), mais dont la traduction automatique est parfois étrange...).
2. A partir de cette page visitez quelques pages référencées dans la rubrique _select a design_ (ou _choisissez une conception_) dans le bandeau de droite. Après en avoir consulté quelques-unes vous devriez avoir rencontré des styles **très** différents.

3. Sélectionnez et ouvrez deux de ces pages dans des onglets séparés et pour chacune d'entre elles consultez-en  le code source. Rappelons qu'il suffit d'un clic droit sur la page puis de choisir _Code source de la page_.

4. Comparez les codes source de ces deux pages.
5. Que constatez-vous ? Quelle(s) différence(s) entre les deux ? Si vous n'en trouvez aucun, cherchez le contenu des balises `<style>` dans les parties `head`.








Vous venez de le constater l'application de feuilles de style à un document html permet d'en modifier sensiblement l'apparence. La séparation du fond et de la forme est à nouveau respectée. Le fond se trouve dans le document au format html et la forme est définie
dans un fichier écrit dans un format appelé css, pour _Cascading Style Sheets_ : _feuilles de style en cascade_.







Le principe de fonctionnement est exactement le même que celui que nous avons rencontré avec le traitement de textes. Un style est défini par un ensemble de propriétés qui caractérisent l'apparence que prendront les éléments auxquels il s'applique. Tout comme avec les styles LibreOffice, il va être possible d'agir sur les styles des caractères, les tailles d'affichage, les marges, etc.







##  Les bases







La structure et les éléments d'une page html sont définis par les balises. C'est donc
sur ces éléments balises que porte un style défini par un ensemble de couples _(propriété,valeur)_. Le langage CSS définit la syntaxe d'écriture de ces styles. Celle-ci est simple : on précise le type d'élément concerné, puis on énumère entre accolade et séparés par des `;` les couples sous le forme `_propriété : valeur_`. Il "suffit" donc de    connaître les propriétés qui s'appliquent à l'élément concerné et les valeurs possibles.






Voici un premier exemple de style qui s'applique aux éléments marqués par les balises `h2`





~~~css
h2 {
   font-size: 16pt;
   color: yellow;
   background-color: #6A0888;
}
~~~






On comprend sans difficulté les propriétés utilisées et leur~~~s valeurs : la taille de la police fixée à 16pt, la couleur d'écriture fixée à la constante prédéfinie `yellow` et la couleur d'arrière-plan fixée à `#6A0888`.






Pour appliquer ce style à un document html, il faut d'abord créer un fichier contenant ce code.






Sauvegardez ce texte dans un fichier que vous   appellerez `styleCSS1.css` .






On peut également utiliser la syntaxe


```css
<style type="text/css">
  @import url('styleCSS1.css');
</style>
```








Il faut ensuite préciser dans le document que l'on souhaite utiliser cette feuille de style. Une manière de procéder qui permet l'application du principe de séparation du contenu et de la forme est d'ajouter dans la partie `head` de la page html la ligne :





~~~css
<link href="styleCSS1.css" type="text/css" rel="stylesheet"></link>
~~~






Reprenez le
document [ex_html2.html](/uploads/docs/doc03b/ex_html2.html)
que vous avez corrigé, appliquez-lui la feuille de style du
fichier `styleCSS1.css` (que vous aurez placé dans le même
dossier) et visualisez le résultat.







L'essentiel est là. Il faut maintenant connaître les propriétés et
leurs valeurs et sans doute avoir un peu de sens créatif pour
obtenir des pages plus esthétiques.







Vous avez pu constater que les valeurs de couleur s'expriment de trois
façons : par des valeurs nommées prédéfinies (`yellow`),
par le triplet RVB en utilisant la notation hexadécimale
(`#FFFF00`) ou la notation décimale
(`rgb(255,255,0)`).







  Voici des définitions de style complémentaires :



    h1 {
      font-size: 20pt;
      font-family: sans-serif;
      font-weight: bold;
    }

    p {
      color:rgb(63,63,63);
    }

    h1 {
      color:white;
      background-color:#4C0B5F
    }

    h2 {
      font-size:12pt;
    }






  1.
Ajoutez-les à la suite des précédentes dans le
fichier `styleCSS1.css` et visualisez le résultat obtenu
pour le document `ex_html2.html`.

  2. Déduisez-en quelques règles d'écriture sur les propriétés :

    * Que se passe-t-il si les propriétés d'un élément sont définies en "plusieursblocs"
    * Que se passe-t-il si une même propriété est définie plusieurs
  fois pour un même élément.











Vous avez certainement remarqué que lors de l'application de la
feuille de style actuellement, la couleur des textes des
éléments `ul` diffère de celle des éléments `p`.
Ce qui est bien évidemment cohérent avec les déclarations qui ont été
faites. Si nous souhaitons leur attribuer la même couleur une première
solution serait d'ajouter la définition :






    ul {
      color:rgb(63,63,63);
    }







Cette solution a cependant le défaut que si l'on souhaite que les
éléments `p` et `ul` aient toujours la même
couleur et que l'on est ammené à  modifier leur couleur, il faudra
faire deux modifications en prenant soin de ne pas faire d'erreur. De
plus si en plus de la couleur on souhaite que ces éléments aient
d'autres propriétés en commun, comme la taille de la police par
exemple, on sera amené à dupliquer toutes les définitions communes ce
qui à nouveau est source d'erreur dans la gestion de la
cohérence. Pour éviter ce problème il est possible de définir des
propriétés pour plusieurs éléments simultanément, il suffit d'énumérer
ces éléments avant les propriétés comme ceci :







    p , ul {                      /* les éléments p et ul                         */
      color:rgb(63,63,63);      /*   auront la même couleur                     */
      font-size : 12pt;         /*   et la même taille de police                */
    }






Comme on a vu que les propriétés d'un élément pouvaient être
  définies en plusieurs fois, rien n'empêche d'avoir en plus de ces
  définitions communes des propriétés dont les valeurs sont propres à
  chacun de ces deux éléments.






### Apprentissage par l'exemple et auto-documentation





Une bonne partie de l'apprentissage du langage CSS peut se faire
progressivement et par l'exemple. Vous avez certainement deviné assez
  facilement la sémantique des différentes propriétés et valeurs
  utilisées ci-dessus.


 Il faut aussi très largement bénéficier des ressources sur le web à
l'aide de recherche pertinente.







Recherchez les valeurs possibles de la
propriété `font-weight`.


Les mots-clés "_css font-weight_" devrait suffire et le
site [w3schools](http://www.w3schools.com/cssref/) convient
le plus souvent pour une première description.







Recherchez les valeurs possibles de la
propriété `font-size`.  Remarquez les différentes manières
de noter les valeurs.








De même qu'il existe un validateur permettant de vérifier la correction
  html d'un document, le W3C fournit
  un [validateur pour les
  fichiers CSS](http://jigsaw.w3.org/css-validator/) qui permet de vérifier la syntaxe d'un fichier CSS et,
  en cas d'erreur, d'en être informé.







  Vérifiez que le fichier `styleCSS1.css` est valide.








En utilisant les quelques propriétés découvertes jusqu'à maintenant,
ajoutez des styles particuliers pour les éléments marqués par les
balises `code` et vérifiez la validité du
fichier que vous avez créé.



 Visualisez le résultat de l'application de ce style au
document `ex_html2.html` puis testez-le avec un autre fichier html
dont vous disposez.








## Quelques autres propriétés





### Les hyperliens




Les hyperliens sont marqués dans une page html par une
  balise `a`. Comme toute balise on peut lui appliquer un
  style, par exemple :







    a {
      color : red;
      text-decoration : underline ;
    }







  Ajoutez cette définition à votre feuille de style et testez.







`a:hover` doit toujours être placé après `a:link`
et `a:visited` dans la feuille de style quand ceux-ci sont présents.






Notons que la pseudo-classe `:hover` n'est pas limitée aux
éléments `a`.





Vous avez cependant certainement déjà constaté que l'apparence des
  hyperliens varie selon qu'ils ont été ou non visités et parfois lorsque
  le pointeur de la souris survole le lien.  Ces modifications d'apparence
  sont également définies par la feuille de stype. On les définit par les
  éléments (appelés _pseudo-classes_) tels
  que `a:link`, `a:visited`
  ou `a:hover`.







Essayez par exemple le résultat après avoir complété la feuille de style
  actuelle avec :



    a:visited {
      color : #680000;
    }
    a:hover {
      background-color : red;
      color : white;
      text-decoration:none;
      font-style : italic;
    }









### Alignements





Comme l'indique son nom la propriété `text-align` permet de
  fixer l'alignement du texte d'un élément.









  1. Recherchez les différentes valeurs que peut prendre cette propriété.
  2. Testez ces différentes valeurs sur les styles des
  éléments `h1`, `h2` et `p` de la
  feuille `styleCSS1.css`







###  Arrière-plan





Vous avez déjà pu observer le comportement de la
  propriété `background-color`. Il est également possible
  de placer une image en arrière plan d'un élément (pas uniquement de
  la page).









  1. Cherchez de la documentation sur la
  propriété `background-image`.

  2. testez-en le fonctionnement en plaçant une image de fond pour les
  éléments `body` et `p` de votre page
  3. Cherchez de la documentation sur la
  propriété `background-repeat`.
  4. Testez le comportement des différentes valeurs que peut prendre
  cette propriété.








## Boites : tailles, bordures et marges



![CSS : boite
						    englobante, bordure et
						    marges](/uploads/docs/doc03b/css-box.png)




Chaque élément d'une page html occupe une place délimitée par
  une _boîte englobante_. Un certain nombre de propriétés permettent
  d'agir sur cette boîte :






  * sa **taille**, avec les propriétés `width`
  et `height`, la valeur associée est est une
  longueur. La longueur peut être exprimée dans différentes unités.
  Nous nous limiterons à l'utilisation d'une unité de mesure absolue :
  le pixel, `px` et à une unité de mesure relative :
  le pourcentage, `%`, relatif aux dimensions du bloc
  qui contient l'élément.





    height : 200px;    // la hauteur de l'élement sera fixée à 200 pixels
    width  : 80%;      // la largeur de l'élément est fixée à 80% de la largeur du bloc qui le contient
    width : auto;      // la largeur est calculée par le navigateur, c'est la valeur par défaut








  * ses **marges extérieures** avec la famille des
 propriétés `margin`, elles définissent
 les tailles de l'espace autour de la bordure par rapport
 au reste de la page,
  * ses **marges intérieures** avec la famille des
 propriétés `padding`, elles définissent les tailles de
 l'espace à l'intérieur de la bordure, c'est-à-dire entre la boîte
 englobante et la bordure.





On parle de "famille" de propriétés car
pour `margin` ou `padding`
on peut avoir une valeur différente pour les parties au-dessus,
au-dessous, à gauche ou à droite de l'élément. On dispose de fait de
propriétés spécifiques dont le nom s'obtient en ajoutant respectivement les
suffixes `-top`, `-bottom`, `-left`
ou `-right`.


Par défaut les marges intérieures ou extérieures sont nulles.






Les différentes syntaxes suivantes permettent de définir les
  marges (on a exactement les mêmes possibilités avec les marges
  intérieures `padding`) :






    margin : 15px;                  // la marge extérieure vaut 15px dans les quatre directions
    margin : auto;                  // les marges sont calculées par le navigateur
    margin-right : 10%;             // seule la marge extérieure droite est fixée à 10%
    margin-left : 20px;             // seule la marge extérieure gauche vaut 20px
    margin : 100px 40px 10px 70px;  // fixe dans l'ordre top(=100px), right, bottom, left
    margin : 100px 20px;            // fixe top=bottom=100px, right=left=40px







Il existe bien d'autres possibilités avec les bordures. A vous de les
découvrir si vous êtes curieux. Il suffit de rechercher l'information. Essayez par
exemple la propriété `border-radius : 4px`.







  * sa **bordure** avec la famille des
 propriétés `border`.  A nouveau on peut séparer les quatre
 bordures : dessus, dessous, gauche et droite avec les mêmes
 suffixes que les marges. Et on peut en plus dans chaque cas préciser
 une couleur, un style et une épaisseur d'encadrement en ajoutant les
 suffixes `-color`, `-style`
 ou `-width`.





    border-style : solid;           // les 4 côtés de la bordures seront en trait plein \\
    border-color : blue;            // les 4 côtés de la bordures seront blue \\
    border-width : thin;            // les 4 côtés de la bordures seront "fines" \\
    border-top-style : none ;       // pas de bordure au-dessus
    border-bottom-style : dotted ;  // seule la bordure au-dessous est en pointillés
    border : 1px solid red;         // fixe dans l'ordre width, style, color pour les 4 bordures \\







Le terme _Cascade_ de l'acronyme _CSS_ signifie que certaines
propriétés d'un élément s'appliquent sur les autres éléments qu'il
contient (on rencontre le terme d'_héritage_ de propriété pour
évoquer cette notion).

Ainsi si on attribue une valeur à  la
propriété `background-color` de l'élément `body`
cette valeur est "automatiquement" reprise par les éléments
(`h1` ou `p` par exemple) contenu dans cet
élément, c'est-à-dire écrits entre les
balises `<body>` et `</body>`.
A moins bien sûr que cette propriété ne soit explicitement redéfinie
pour un de ces éléments.

Vous serez peut-être amenés dans les documentations que vous
lirez à rencontrer le terme d'_élément parent_. Ce terme désigne
l'élément dans lequel est contenu l'élément
considéré : `body` est l'élément parent des
balises `h1` dans votre document.









  1.  Ajoutez à votre feuille initiale les styles :



    html {
       background-color:#F7F7F7;
    }
    body {
      background-color: white;
      width : 90%;
      margin: auto;
      border-left : 2px solid #EEEEEE;
      border-right : 2px solid #EEEEEE;
    }
    h1 {
    padding : 10px;
    }
    h2 {
    padding : 5px;
    }



Testez.

  2. Ajoutez une marge **extérieure** gauche de 10 pixels aux
  éléments `p`. Testez.
  3. Ajoutez une brodure gauche de 2 pixels d'épaisseur, en trait plein et de
  couleur `#E0E0E0` aux
  éléments `p`. Testez.
  4. Ajoutez une marge **intérieure** gauche de 10 pixels aux
  éléments `p`. Testez.







Ceux intéressés pour en apprendre plus et s'initier sur les stratégies de positionnement
d'éléments par CSS dans une page peuvent consulter [cette référence](http://openweb.eu.org/articles/initiation_flux/).






Le langage CSS offre d'autres possibilités, notamment en terme de
"finesse" de portée des définitions et il existe bien d'autres
propriétés CSS intéressantes qui permettent d'obtenir de nombreux
effets. Le langage CSS est riche et parfois complexe. Le processus de
traitement du flux des éléments d'une page n'est par exemple pas si
simple. On peut ainsi citer sans les aborder les
propriétés `float`, `display`, `clear`, `position`
qu'un élève curieux pourra découvrir seul.
