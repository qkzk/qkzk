---
author: qu3nt1n
date: 2016-07-01 14:45:31+00:00
draft: false
title: 07. Cartographie
bookCollapseSection: true
weight: 7
---



Notions abordées



 google map
 editer une carte en ligne
 créer sa propre carte
 anamorphose







### La cartographie.




# Principe.


Une carte, un plan doit permettre au lecteur de se repérer dans l'espace et d'obtenir les infomations dont il a besoin pour se déplacer ou comprendre certaines notions.
Les cartes anciennes étaient principalement utilisées pour se déplacer (sur terre ou sur mer), planifier des constructions et faire la guerre.
Ces usages n'ont pas changé mais leur conception a énormément progressé depuis l'ordinateur. Inutile d'avoir, comme il y a 15 ans à peine, 20 cartes dans son véhicule. Le GPS nous guide bien gentillement jusqu'au camping et il suffit d'écouter sa douce voix (sans s'énerver).


## Comment les cartes sont-elles concues ?


On utilise à l'heure actuelle des photographies prises depuis un satellite (géo-satellite = satellite en orbite stationnaire par rapport à la terre ou satellite dont l'orbite survole régulièrement les mêmes points) d'une grande précision. Cela demande donc d'avoir, au dessus de nous, des satellites qui photographient la terre et transmettent leurs informations sur terre (photographie, position, date). Celles-ci sont alors recomposées en une image globale ou partielle de la terre et traitée pour en repérer les informations essentielles. On y intègre alors plus ou moins automatiquement toutes les informations nécessaires : routes, bâtiments, frontières etc.

Afin de pouvoir zoomer comme on l'entend dans la carte celles-ci sont vectorielles et chaque niveau de zoom apportera des précisions supplémentaires. Ce procédé est à l'origine des cartes telles que Google Map et Google Earth. Il a été repris afin de rendre les données libres de droits ([Open Street Map)](https://www.openstreetmap.org/#map=5/51.500/-0.100) ou par la concurrence (Microsoft, Apple, Mappy, Tomtom etc.)



---



**Et les cartes de géographie ?**

Sur le même procédé mais adapté au besoin du concepteur. Avant, il fallait dessiner les contours en décalquant un planisphère, colorier chaque partie à la main, apporter les informations supplémentaires à la main. C'est ce qu'on a longtemps fait sur un ordinateur et... c'est ce qu'on fait toujours !

Mais heureusement c'est plus rapide. On utilise maintenant des logiciels dédiés qui permettent de relier des données (population d'un département) à un contour (celui des départements) pour intégrer une information à l'aide d'une couleur par exemple.

**Le taux de chômage par département au 1er trimestre 2014**[![France_Dept_Chom](/uploads/uploads/2016/07/France_Dept_Chom.png)
](/uploads/uploads/2016/07/France_Dept_Chom.png)Le niveau de bleu indique le taux.


# Manipulation d'une carte vectorielle


La carte suivante disponible [ici](https://upload.wikimedia.org/wikipedia/commons/4/43/France_cities.svg) est au format svg, elle est donc éditable à la volée... ce qui n'est pas une mince affaire.


Récupérer la carte ci-dessus et l'éditer dans Notepad++.


Le fichier est volumineux, il décrit très précisément les contours de la France... Plus le dessin est fin, plus le fichier est complexe.


Retrouver le code couleur du remplissage de la France et la colorier en Cyan.


Les chaines de montagne sont en allemand. Toujours dans Notepad, traduire les chaines de montagne en Français.

Faire de même pour les mers et les golfes.


Ouvrir votre fichier dans inkscape et selectionner la ville de Calais. Changer son nom en le remplaçant par votre bled et déplacer le point pour le postionner approximativement. Attention à ce que les noms ne se chevauchent pas !




# Google Maps




## Fonctionnement de base


Nous allons nous pencher sur l'application [de cartes](https://maps.google.com/) de Google. Cette-ci reprend les mêmes informations qu'elle soit utilisée dans votre navigateur ou dans un application mobile.

Les informations de l'utilisateur sont transmises à google maps par le biais de l'URL. entre @ et ? on trouve 3 nombres. Par exemple : `https://www.google.fr/maps/@50.7288981,2.5609289,13z?hl=en`. Si vous êtes allés à l'école vous devriez reconnaître les coordonnées GPS d'une ville très connue... Le troisième nombre indique une altitude et donc un niveau de zoom.




Commencez par repérer votre ville en cliquant dessus. Relever les coordonnées GPS qui apparaissent dans l'URL.

Faire apparaître le trajet que vous effectuez le matin pour venir au Lycée en employant le moyen de transport (voiture si vous venez en bus).




Il est possible d'afficher le trafic en temps réel et à certains horaires. Admettons qu'on quitte le lycée maintenant pour se rendre à Lille en voiture combien de temps mettrions-nous ? Et en partant à 7h le lundi matin ? Et maintenant faisant le contraire : A quelle heure quitter Lille pour arriver à l'heure au lycée ? Comment s'explique cette différence de durée de parcours ?



---





## L'api Google Maps


Google maps propose une API (interface de programmation) qui permet d'intégrer dans des logiciels et sites web une carte et des informations supplémentaires. On consultera [leur site](https://developers.google.com/maps/) pour quelques exemples.

Voici un très simple exemple qui présente le trafic en temps réel autour de Lille : [map_test_trafic](/uploads/uploads/2016/07/map_test_trafic.html) (C'est pénible d'activer Javascript dans une page wordpress aussi vous devrez l'ouvrir dans un autre onglet).

Examinons le code cette page :




    <!DOCTYPE html>
    <html>
      <head>
        <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
        <meta charset="utf-8">
        <title>Traffic layer</title>
        <style>
          html, body {
            height: 100%;
            margin: 0;
            padding: 0;
          }
          #map {
            height: 100%;
          }
        </style>
      </head>
      <body>
        <div id="map"></div>
        <script>
    function initMap() {
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: {lat: 50.65, lng: 3.05}
      });

      var trafficLayer = new google.maps.TrafficLayer();
      trafficLayer.setMap(map);
    }

        </script>
        <script src="https://maps.googleapis.com/maps/api/js?callback=initMap" async defer>
        </script>
      </body>
    </html>


C'est donc une page html classique qui comporte les balises usuelles (html, head, body). Le head comporte un élément de CSS (style) qui donne les dimensions de la page et de la carte.
Le body contient simplement 2 balises un div (qui présente la carte, laissé vide, nommé "map") et un script.

C'est ce script qui nous intéresse.

`new google.maps.Map(document.getElementById('map') ` défini une carte google map dont les paramètres sont donnés entre les accolades { ... }

Repérer dans le code le centre, qui est donné par ses coordonnées (latitude et longitude).

Une variable appelée trafficLayer est définie plus bas. Elle charge les informations de trafic sur la carte, une fois celle-ci chargée.

Une deuxième script est défini plus bas, il renvoie à l'url de l'api google map et demande de la charger dans l'élément identifié par "map" qui est le div laissé vide.
En bref, on ne fait que charger une carte, centrée sur Lille, affichant le trafic routier à l'instant présent.


Créer un fichier html appelé traffic-paris.html et y insérer ce code.
Remplacer les coordonnées de Lille par celles de Paris. On adaptera le niveau de zoom de façon à faire apparaître tout le périphérique parisien.
Recommencer avec New-York. La nouvelle carte doit être centrée sur Central-Park et faire apparaître l'aéroport de Teterboro à l'ouest et le Queens à l'est.




## Dessiner sur google map


Il est tout à fait possible d'ajouter des éléments à Google Maps. On dessiner alors une couche vectorielle, repérée par des coordonnées GPS et qui se représente au dessus de la carte.



Pour des questions de sécurité, google map n'autorise que deux approches :



 Ajouter les éléments depuis le fichier html directement.
Dans ce premier exemple : [test_googlemap_png](/uploads/uploads/2016/07/test_googlemap_png.html), on ajoute une image, transparente à des coordonnées précises. Cet objet ne s'affiche que si le zoom est compris entre certaines valeurs (dézoomer et rezoomer).
C'est commode pour dessiner une figure simple, ça l'est moins pour les objets complexes
 Ajouter des éléments depuis un fichier .kml. C'est un format de fichier assez simple, c'est en fait du XML (comme SVG). L'inconvénient est qu'il faut absolument que ce fichier soit hébergé quelque part sur internet. Il est impossible de charger un fichier kml depuis votre ordinateur en local. Il faut qu'il soit accessible via une url. [Par exemple](https://developers.google.com/maps/documentation/javascript/examples/layer-kml)

Voici un autre exemples simples tiré des exemples de l'api de google : [test_googlemap_dropmarkers](/uploads/uploads/2016/07/test_googlemap_dropmarkers.html). On fait apparaître des marqueurs qui tombent de façon animée.




Télécharger le code source de ce lien et changer les différentes coordonnées gps de façon à :



 Centre la carte sur Hazebrouck
 Faire tomber les marqueurs sur le Lycée
 Sur la Grand Place d'Hazebrouck
 Sur la gare d'Hazebrouck
 Sur l'Espace Flandres
 Adapter le niveau de zoom

Si vous n'aimez aucun de ces lieux (la gare, bon sang, elle est magnifique...) vous pouvez tout à fait repérer vos lieux favoris si ça vous chante. Le tout est de faire tenir les marqueurs dans une seule carte.






## Contribuer à la renommée de l'établissement en utilisant les outils de google maps


Nous allons dessiner un cabre surplombant le bâtiment B du lycée et l'afficher avec google map.


Commencer par relever précisément les coordonnées GPS des 4 coins du bâtiment B du Lycée qu'on assimile à un long rectangle.


L'exemple [test_googlemap_bermudes](/uploads/uploads/2016/07/test_googlemap_bermudes.html) dessine un triangle dans lequel on peut cliquer et qui affiche alors un tas d'informations passionnantes.


Télécharger le fichier source et l'éditer.
Modifier le centre de la carte vers le lycée, modifier les sommets du triangle pour en faire un quadrilatère surplombant le bâtiment B du lycée.
Changer la couleur de remplissage en cyan, la couleur du bord en magenta.Changer le contenu de la chaîne de caractère `contentString` pour que son contenu change quand on clique dessus et qu'il affiche :Bâtiment B
Lycée des Flandres


Vos travaux sur Google Map s'achèvent. Vous devriez maintenant être capable d'afficher une carte, de dessiner sommairement dessus des formes très simples. Approfondir nécessiterait des connaissances poussées en Javascript dont vous ne disposez pas aussi... ça attendra. Néanmoins, le [site pour les développeurs](https://developers.google.com/maps/) de Google est très complet, je vous invite à l'explorer si le sujet vous intéresse.


# Créer ses propres cartes. Travail à la maison.


Bon... le VRAI logiciel qui permet de créer des cartes est gratuit et son fonctionnement est complexe mais tout à fait abordable. Son inconvénient majeur est son poids, assez conséquent.

J'avais un petite manip en ~10 étapes à vous faire faire... Je ne la considère donc pas comme indispensable et la laisse (sans les détails qui vont avec et les traductions en français) pour le lecteur intéressé. Vous pouvez envisager ça comme **un travail à la maison**. Optionnel donc.

Voici le logiciel (gratuit et libre) : [QGIS](https://www.qgis.org/fr/site/forusers/download.html) - _Le fichier faisant 320 MB il n'est pas possible de le télécharger au lycée. C'est dommage mais c'est la vie._



 récupérer le fond de la carte de france au format SHP, découpée en département
 récupérer les taux de chomage par département au format xls, en faire un fichier dbf dans calc (le tableur de libre office)
Ne garder que : numero de département, nom du département, taux dans un seul fichier, d'une seule page
 joindre les taux de chomage par departement en suivant la démarche indiquée [ici](https://www.mapbox.com/tilemill/docs/guides/joining-data/#using-quantum-gis-to-join-your-data)
 trier : couleur selon taux de chomage en choisissant un dégradé
 exporter en png
 Exporter au format shp

Le résultat que vous obtiendrez est celui déjà affiché en début de partie :

**Le taux de chômage par département au 1er trimestre 2014**[![France_Dept_Chom](/uploads/uploads/2016/07/France_Dept_Chom.png)](/uploads/uploads/2016/07/test_googlemap_bermudes.html)
Le niveau de bleu indique le taux.Pour la suite, seul le résultat m'intéresse : la carte de France avec les données statistiques de la population de chaque département au format SHP


# Les cartes en Anamorphose


en voici quelques une assez parlantes :

[![vignettes_4](http://www.datamix.fr/wp-content/uploads/2014/12/vignettes_4-1024x486.png)
](http://www.datamix.fr/wp-content/uploads/2014/12/vignettes_4.png)

Celles tournant autour du sport sont disponibles sur [slate.](http://www.slate.fr/story/93121/cartes-france-sport)

J'aime bien "Bowling et sport de quilles" ...

Elles ont été réalisées en javascript grâce à [d3.js](https://d3js.org/). Je vous laisse explorer, cliquer n'importe où sur le grand bandeau... Vous devriez en revenir impressionné. Par [exemple](http://bl.ocks.org/mbostock/3057239) ou bien [ceci](http://www.koalastothemax.com/).

Plutôt que de réinventer la roue et parce que, mine de rien, c'est très long de préparer vos T.P. je vous invite à découvrir par vous même le principe et l'outil retenu pour créer ces cartes en suivant [ce pdf](https://www.academia.edu/attachments/39162337/download_file?st=MTQ2NzM4NTExMSw3OC4yNDIuNTQuMjQsMzc5NzM0MTQ%3D&s=swp-toolbar&ct=MTQ2NzM4NTExMSwxNCwzNzk3MzQxNA==). Certaines connaissances peuvent vous manquer et nous n'irons pas jusqu'au bout.
Ce qui m'intéresse est que vous compreniez bien ce que font les cartes en anamorphose et comment en créer une avec Scapetoad.

Le principe en est le suivant : modifier la superficie d'une zone (comme un département) pour qu'elle devienne proportionnelle à sa population. La population Française n'est pas répartie de façon homogène : Paris est dense et la Creuse dépeuplée. Paris parait énorme sur une anamorphose suivant la population, la Creuse très petite. Afin de comprendre la carte il est souvent utile de la colorer (Cf partie précédente)

Si vous avez suivi avec attention les slides du PDF de présentation, vous n'aurez aucun mal à réaliser une anamorphose.




Télécharger [ScapeToad](http://scapetoad.choros.ch/download.php). Décompressez [l'archive](http://icnflandres.free.fr/france_dept.zip)  que j'ai adapté pour vous. Elle contient le fichier SHP qu'il vous faut. Ne vous reste plus qu'à charger le layer SHP de la france et créer le cartogramme.
Revenir au PDF si ce n'est pas clair.

Exporter votre carte en SVG (sans la grille (grid)) et elle devrait être lisible dans inkscape.






**Optionnel : ** Exporter votre carte au format SHP et l'intégrer dans QGIS. Colorier la carte selon la population.


J'espère que vous avez bien suivi cette partie car nous aurons l'occasion d'y revenir. En effet on se servira de données géolocalisées dans une partie ultérieure...

Pour finir j'aurais besoin de quelques conseils de votre part, qu'est-ce que vous pensez de [ma déco ?](https://www.google.fr/maps/place/Palace+of+Versailles/@48.8049739,2.1214015,3a,75y,271h,90t/data=!3m7!1e1!3m5!1sK4tE8-hoUIk_Utx4bxAyBg!2e0!6s%2F%2Fgeo0.ggpht.com%2Fcbk%3Fpanoid%3DK4tE8-hoUIk_Utx4bxAyBg%26output%3Dthumbnail%26cb_client%3Dsearch.TACTILE.gps%26thumb%3D2%26w%3D129%26h%3D106%26yaw%3D271%26pitch%3D-6.17!7i13312!8i6656!4m5!3m4!1s0x47e67d94d7b14c75:0x538fcc15f59ce8f!8m2!3d48.8048649!4d2.1203554!6m1!1e1) Un peu trop chargée ?
Sinon j'ai acheté [deux trois ordis](https://www.google.com/maps/@35.8981776,-81.5481622,3a,75y,351.08h,88.27t/data=!3m6!1e1!3m4!1suMLibmsgdnXf2_bCctYEMw!2e0!7i13312!8i6656) pour faire tourner mon site mais la facture d’électricité est salée...
