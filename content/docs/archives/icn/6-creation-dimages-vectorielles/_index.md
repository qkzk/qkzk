---
author: qu3nt1n
date: 2016-07-07 09:09:18+00:00
draft: false
title: 06. Création d'images vectorielles
bookCollapseSection: true
weight: 6

---

# 1. Introduction, rappels


Pour suivre ces activités, il est nécessaire d'avoir des connaissances en HTML et en CSS.

Le svg d'après Wikipédia :

_Le Scalable Vector Graphics (en français « graphique vectoriel adaptable»), ou SVG, est un format de données conçu pour décrire des ensembles de graphiques vectoriels et basé sur XML._

En résumé, le svg est un format de données conçu pour décrire des graphiques vectoriels. Mais qu'est-ce qu'un graphique vectoriel ?

Ici aussi, consultons Wikipédia sur ce sujet :

_Une image vectorielle (ou image en mode trait), en informatique, est une image numérique composée d'objets géométriques individuels, des primitives géométriques (segments de droite, arcs de cercle, courbes de Bézier, polygones, etc.), définis chacun par différents attributs (forme, position, couleur, remplissage, visibilité, etc.) et auxquels on peut appliquer différentes transformations (homothéties, rotations, écrasement, mise à l'échelle, extrusion, inclinaison, effet miroir, dégradé de formes, morphage, etc.). Elle se différencie en cela des images matricielles (ou images bitmap), qui sont constituées de pixels._

Tout est expliqué ci-dessus, mais revenons sur l'essentiel :

il existe en informatique 2 types d'images :



 les images matricielles qui sont des suites de points (pixels)


 les images vectorielles qui sont composées d'objets géométriques (segments de droite, cercle, polygones)

Les images vectorielles ont un immense avantage par rapport aux images matricielles : il est possible de zoomer (ou dézoomer) comme bon vous semble avec une image vectorielle sans que cela ne dégrade la qualité de cette image.

Nous aurons l'occasion de revenir sur la différence entre les images vectorielles et les images matricielles, pour l'instant, concentrons-nous sur le svg.

Le HTML5 propose une balise svg. Cette balise svg permettra d'afficher sur votre page web une "zone de dessin".


#### À faire vous même 1.1


Créer un dossier "svg" dans votre espace de travail. Ceci étant fait, créer un fichier "index.html" et "style.css" dans ce dossier "svg".



---





#### À faire vous même 1.2


Compléter le fichier "index.html" comme suit :


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin"></svg>
    </body>
    </html>


Compléter le fichier "style.css" comme suit :


    #dessin {
        width:800px;
        height:600px;
        border : 1px solid black;
    }


Ouvrir le fichier index.html dans un navigateur



---



Comme vous pouvez le constater, une zone délimitée par une bordure apparait sur la page proposée par le navigateur. Cette zone sera notre zone de dessin. Pour ce qui est du code, rien de très compliqué, le html utilise le fichier "style.css". Ce fichier "style.css" permet de définir la largeur et la hauteur de notre zone de dessin ainsi que la bordure entourant cette même zone de dessin (zone de dessin qui aura été défini par la balise svg dans le code html). Dans la prochaine activité, nous commençerons à dessiner.


# 2. Cercles, disques : premières formes






Pour dessiner dans la zone créée dans l'activité précédente, nous allons utiliser des balises, voici quelques exemples :



 <circle/>
 <rect/>
 <line/>
 <path/>

Commençons par nous intéresser à la balise <circle/> qui, comme vous l'avez sans doute deviné, permet de dessiner un cercle !

Problème, un cercle à un rayon, où va-t-on renseigner cette information ?

Il est possible de rajouter des attributs dans les balises. Pour définir le rayon du cercle nous écrirons : <circle r="40"/>

Nous avons ajouté un attribut r à notre balise, le cercle aura donc un rayon de 40 pixels.

Il est aussi possible de renseigner les coordonnées du centre du cercle grâce aux attributs "cx" et "cy" : <circle r="40" cx="400" cy="300"/>

ATTENTION : ci-dessus, 400 et 300 correspondent aux coordonnées du centre du cercle sachant que l'origine du repère (le point de coordonnées (0,0)), se trouve dans le coin supérieur gauche de la zone de dessin définie grâce à la balise <svg>


#### À faire vous même 2.1


Compléter le fichier "index.html" comme suit :


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <circle r="40" cx="400" cy="300"/>
        </svg>
    </body>
    </html>


Le fichier "style.css" reste identique à celui vu dans l'activité 1.

Tester cet exemple en lançant le fichier "index.html".



---





#### À faire vous même 2.2


En repartant de l'exemple précédent, modifiez les attributs "r", "cx" et "cy" afin de modifier la taille et la position du cercle.

Tester vos modifications.



---



Il est possible de modifier la couleur du cercle à l'aide des attributs "stroke" et "fill" :



 "stroke" correspond à la couleur de contour
 "fill" correspond à la couleur de remplissage



#### À faire vous même 2.3


Compléter le fichier "index.html" comme suit :


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <circle r="40" cx="400" cy="300" fill="green" stroke="red"/>
        </svg>
    </body>
    </html>


Le fichier "style.css" reste identique à celui vu dans l'activité 1.

Tester cet exemple.



---



Au lieu de nommer les couleurs, il est possible de renseigner les canaux rouge, vert et bleu :

par exemple, fill="rgb(255,0,0)"  donnera une couleur de remplissage rouge.

Pour en savoir plus sur les canaux rouge, vert et bleu, n'hésitez pas à consulter [cette page](https://fr.wikipedia.org/wiki/Rouge_vert_bleu).


#### À faire vous même 2.4


En repartant de l'exemple précédent, modifier les couleurs de remplissage et de contour, en utilisant les canaux rouge, vert et bleu.



---



Il est possible de joueur sur l'opacité (transparence) avec les attributs "fill-opacity" et "stroke-opacity". Les valeurs de ces attributs varient entre 0 (totalement transparent) et 1 (totalement opaque).


#### À faire vous même 2.5


Modifiez l'exemple précédent en ajoutant les attributs "fill-opacity" et "stroke-opacity". Vous choisirez les valeurs de ces 2 attributs comme bon vous semble.



---



Il est possible de modifier l'épaisseur du trait de contour avec l'attribut "stroke-width", par exemple _stroke-width="5"_ permettra d'avoir un contour de 5 pixels.


#### À faire vous même 2.5


Reprenez l'exemple précédent en modifiant l'épaisseur du trait de contour en ajoutant l'attribut "stroke-width".



---








# 3. Rectangles et formes, premier dessin composé






Évidemment, le svg ne propose pas seulement de dessiner des cercles. Nous allons présenter d'autres figures géométriques.

Commençons par les rectangles :

Nous devons utiliser la balise <rect/>. Cette balise peut prendre pour attributs :



 x : coordonnée x du coin haut-gauche du rectangle, exemple <rect x="400"/>
 y : coordonnée y du coin haut-gauche du rectangle, exemple <rect x="400" y="300"/>
 width : la largeur du rectangle, exemple <rect x="400" y="300" width="100"/>
 height : la longueur du rectangle, exemple <rect x="400" y="300" width="100" height="50"/>

Il est possible d'utiliser les attributs vus dans l'activité précédente ("fill", "stroke", "fill-opacity", "stroke-opacity" et "stroke-width")


#### À faire vous même 3.1


Compléter le fichier "index.html" comme suit :


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <rect x="400" y="300" width="100" height="50" fill="rgb(255,125,0)" stroke="green" fill-opacity="0.4" stroke-width="5" />
        </svg>
    </body>
    </html>


Le fichier "style.css" reste identique à celui vu dans l'activité 1.

Tester cet exemple en effectuant un "double-clic" sur le fichier "index.html".



---



Il est possible de tracer un segment de droite avec la balise <line/>. Nous avons 4 attributs : x1, y1, x2 et y2. Le couple (x1,y1) correspond aux coordonnées du point de départ du segment de droite, le couple (x2,y2) correspond aux coordonnées du point d'arrivée du segment.

Les autres attributs restent valables.


#### À faire vous même 3.2


Compléter le fichier "index.html" comme suit :


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <line x1="100" y1="100" x2="300" y2="500" stroke="red" stroke-width="4"/>
        </svg>
    </body>
    </html>


Le fichier "style.css" reste identique à celui vu dans l'activité 1.

Tester cet exemple en effectuant un "double-clic" sur le fichier "index.html".



---



Nous allons terminer avec ce tour d'horizon non exhaustif du svg par le tracé d'un "chemin" ("path" en anglais). L'idée est de reproduire le comportement du couple main+stylo.

Quand vous voulez dessiner une succession de segments de droite, vous commencez par placer votre stylo quelque part sur la feuille, vous dessinez ensuite le premier segment de droite puis le second et ainsi de suite.

Le principe est ici identique :

La balise a un attribut obligatoire : "d" (comme data). C'est grâce à cet attribut que vous allez définir le chemin à parcourir par votre "stylo".


#### À faire vous même 3.3


Compléter le fichier "index.html" comme suit :


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <path d="M 100,200 L 200,230 L 250,50 L 150,75" fill="none" stroke="black"/>
        </svg>
    </body>
    </html>


Le fichier "style.css" reste identique à celui vu dans l'activité 1.

Tester cet exemple en effectuant un "double-clic" sur le fichier "index.html".



---



Quelques commentaires sur le "À faire vous même 3.3" :

L'attribut "d" est égal à une série de lettres et de nombres. La lettre M permet d'amener votre "stylo" au point de coordonnées (100,200). La lettre "L" indique qu'il faut tracer un segment de droite de la position courante (100,200) jusqu'au point de coordonnées (200,230). Le "stylo" étant maintenant aux coordonnées (200,230), le deuxième "L" permet de tracer un second segment de droite entre le point de coordonnées (200,230) et le point de coordonnées (250,50). Le principe est le même pour les autres "L" de l'attribut "d".

Notez que le _fill="none"_ permet de ne pas avoir de couleur de remplissage. Vous pouvez d'ailleurs le supprimer pour voir ce qui se passe.

Il est possible de refermer automatiquement la figure en reliant le dernier et le premier point en ajoutant un "Z" à la fin de l'attribut "d"


#### À faire vous même 3.4


Reprenez l'exemple précédent en modifiant l'attribut "d" comme suit : _d="M 100,200 L 200,230 L 250,50 L 150,75 Z"_

Vérifiez le résultat.



---



Ici aussi, il est possible d'utiliser tous les attributs vus précédemment (("fill", "stroke", "fill-opacity", "stroke-opacity" et "stroke-width"))


#### À faire vous même 3.5


Essayez de reproduire (à peu près) ce dessin :





---



svg permet aussi d'afficher du texte à l'aide de la balise <text>


#### À faire vous même 3.6


Compléter le fichier "index.html" comme suit :


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
             <text x="200" y="300" font-family="Verdana" font-size="55">Hello World!</text>
        </svg>
    </body>
    </html>


Testez ce code



---








# 4. Les transformations géométriques






L'attribut _transform_ permet d'effectuer :



 des translations
 des rotations
 des mises à l'échelle (en gros, des zooms)

Il faut bien que vous compreniez que ces transformations agissent sur le système de coordonnées.

Commençons par la rotation qui permet de "tourner" le système de coordonnées d'un certain angle.

Au départ nous avons :

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/0.png)


après une rotation, nous obtenons ceci :

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/1.png)


Pour effectuer une rotation d'un angle α, il suffit de rajouter l'attribut _transform_(_transform="rotate(α)"_)

sans le _transform="rotate(α)"_

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/2.png)


avec le _transform="rotate(α)"_

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/3.png)



#### À faire vous-même 4.1


Saisissez et testez ce code


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <rect x="50" y="60" width="20" height="20" transform="rotate(30)"/>
        </svg>
    </body>
    </html>





---





#### À faire vous-même 4.2


Saisissez et testez ce code


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <rect x="100" y="100" width="20" height="20"/>
            <rect x="100" y="100" width="20" height="20" transform="rotate(30)"/>
        </svg>
    </body>
    </html>





---



"translate" permet de faire faire une translation au système de coordonnées :

avant

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/0.png)


après un _transform="translate(dx,dy)"_

on obtient ceci

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/5.png)



#### À faire vous-même 4.3


Saisissez et testez ce code


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <rect x="100" y="100" width="20" height="20"/>
            <rect x="100" y="100" width="20" height="20" transform="translate(250,150)"/>
        </svg>
    </body>
    </html>





---



sans le _transform="translate(dx,dy)"_

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/2.png)


avec le _transform="translate(dx,dy)"_

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/7.png)


"scale" ne devrait pas vous poser de difficultés :


#### À faire vous-même 4.4


Saisissez et testez ce code


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <rect x="100" y="100" width="20" height="20"/>
            <rect x="300" y="100" width="20" height="20" transform="scale(3,3)"/>
        </svg>
    </body>
    </html>





---



Attention, comme pour rotate ou translate, c'est le système de coordonnées qui se trouve affecté par l'application de scale. Scale permet donc de modifier les échelles : dilatation de l'échelle si l'argument est supérieur à 1, contraction de l'échelle si l'argument est compris entre 0 et 1.

Il est possible de combiner "rotate", "translate" et "scale" (attention l'ordre d'application à son importance) :

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/8.png)



#### À faire vous-même 4.5


Complétez le code suivant avec les couleurs (fill) correctes.

~~~html
    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <rect x="100" y="0" width="20" height="20" fill="????" stroke="none"/>
            <rect x="100" y="0" width="20" height="20" fill="????" stroke="none" transform="rotate(45)"/>
            <rect x="100" y="0" width="20" height="20" fill="????" stroke="none" transform="translate (0,50) rotate(45)"/>
            <rect x="100" y="0" width="20" height="20" fill="????" stroke="none" transform="translate (50,0) rotate(45)"/>
            <rect x="100" y="0" width="20" height="20" fill="????" stroke="none" transform="rotate(45) translate (50,0)/>
        </svg>
    </body>
    </html>
~~~

![repere](/docs/archives/icn/6-creation-dimages-vectorielles/img/9.png)




---



Il est possible, à l'aide de la balise <g> de regrouper vos dessins afin de leur faire subir des transformations (rotation, translation ou changement d'échelle de façon simultanée.


#### À faire vous-même 4.6


Saisissez et testez ce code


    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Dessiner avec svg</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <svg id="dessin">
            <g transform="rotate(45)">
                <rect x="100" y="0" width="20" height="20"/>
                <circle cx="140" cy="10" r="20" fill="red"/>
            </g>
        </svg>
    </body>
    </html>





---



Il suffit d'appliquer la transformation au groupe défini avec la balise <g> pour que le dessin dans son ensemble subisse la transformation.


#### À faire vous-même 4.7


En repartant de l'exemple que vous avez développé dans le "À faire vous même 3.5", essayez de reproduire (à peu près) ce dessin :








# 5. Dessiner avec des outils un peu plus agréables






Il existe de nombreux logiciels permettant de produire des dessins au format svg (dessin vectoriel). Inkscape ([https://inkscape.org/fr/](https://inkscape.org/fr/)) est l'un d'entre eux (logiciel de "qualité professionnel, gratuit et libre). Il existe, sur internet, de nombreux cours qui vous permettront de maitriser (au moins en partie) ce logiciel très complet.

Il existe aussi des outils en ligne, directement utilisables dans le navigateur, je vous conseille particulièrement l'application en ligne proposée par Framasoft : [http://framasoft.net/](http://framasoft.net/)


#### À faire vous-même 5.1


À l'aide de votre navigateur favori (par exemple Firefox), allez sur le site [http://framavectoriel.org/svg-editor.html](http://framavectoriel.org/svg-editor.html)

Faites le dessin de votre choix.

Une fois le dessin terminé, cliquez sur le bouton ![btn_svg](/docs/archives/icn/6-creation-dimages-vectorielles/img/10.png)
(en haut à gauche)

Vous devriez voir le code svg de votre image.

Modifiez le code comme bon vous semble et vérifiez que votre image a, elle aussi, été modifiée.








---



_Ce cours a été rédigé [par un collègue.](https://pixees.fr/informatiquelycee/)_
