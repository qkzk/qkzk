---
author: qu3nt1n
date: 2016-07-02 10:32:51+00:00
draft: false
title: 4.09 L'api Google Map
weight: 9
---


**Remarque :** l'API Google Map a considérablement changé depuis la rédaction
de ce tutoriel. Il n'est plus possible de l'intégrer à une page web et d'y
faire des requêtes. Des alternatives gratuites et libres existent comme openStreetMap
mais ce tutoriel ne sera pas remis à jour pour autant.

Notions abordées dans cette page



* un exemple d'API : Google Map v3







# Bibliothèque de code


L'activité de programmation consite à produire un traitement dédié
à une tâche particulière. Pour cela le programmeur dispose d'outils
proposés par le langage qu'il utilise. Certains de ces outils sont
prédéfinis dans ce langage. C'est par exemple en Javascript le cas
de la fonction `parseInt` ou du type `String`
et de certaines de ses fonctions telle `charAt`. Si ce
n'est pas le cas, c'est à ce moment là que le programmeur utilise
ses compétences pour créer (programmer) à partir des éléments
existants un nouveau traitement, défini dans une fonction par
exemple. Dès lors cette fonction, telle `texteMonument`,
devient un nouvel outil à la disposition du programmeur et elle ne
se distingue plus particulièrement de celles prédéfinies. Si pour un
autre programme ce programmeur doit mettre en place le même
traitement il pourra reprende cette définition de fonction, sans
travail supplémentaire. Chaque définition de nouvelle fonction est
donc un nouvel outil, un nouveau mot à disposition du programmeur et
qui vient donc enrichir le langage. Ecrire un programme consiste donc
soit à utiliser des éléments existants soit à créer ceux qui font défaut
avant de les utiliser.

Certains programmeurs (ou groupes de programmeurs, ou sociétés)
choisissent de mettre à disposition des autres programmeurs les
fruits de leur travail. La communauté peut ainsi bénéficier du
travail réalisé sans effort supplémentaire, exceptée la lecture de la
documentation qui prend alors toute son importance.

Cette mise à disposition est d'autant plus intéressante et perinente
que la portée du travail mise à disposition est générale. Ainsi
mettre à disposition des autres nos fonctions de conversion de
Celsius en Fahrenheit intéressera certainement moins de programmeurs que
des fonctions qui permettent de crypter des messages ou de manipuler
des fichiers audio de différents formats.


Le succès d'un langage peut se mesurer au nombre d'API
proposées, et réciproquement les API proposées peuvent contribuer à ce
succès.

Cependant une difficulté est parfois de trouver l'outil que
l'on cherche dans la jungle des bibliothèques proposées. On peut
également parfois rencontrer des problèmes d'incompatibilité entre
plusieurs bibliothèques utilisées ensemble.


Lorsque le travail mis à disposition rassemble un certain nombre
d'outils cohérents sur un même thème on parle
de bibliothèque ou encore
de librairie et également
d'API pour "_Application
Programming Interface_". Une partie de l'activité du
programmeur consiste donc à assimiller et utiliser ces API. Nous
allons explorer, partiellement, l'API Google Map v3 proposée par Google.


# Quelques éléments de l'API Google Map v3


La découverte sera très partielle car cette API est riche. Un coup
d'oeil sur [cette
page](https://developers.google.com/maps/documentation/javascript/reference?hl=fr) permet de s'en faire une idée. On comprend que le temps
d'appropriation d'une API peut être long. Il faut exploiter les
documentations proposées par le créateur de l'API, comme sur le lien
précédent en suivant les rubriques _Developer's Guide_
ou _Code Sample_ du menu sur la gauche, ou rechercher des
informations sur le web.

Nous nous contenterons de présenter quelques fonctionnalités les plus
simples. Ce sera à vous d'explorer et de mener des recherches si
vous voulez aller plus loin.

La première chose à faire est de déclarer l'utilisation de l'API
utilisée. Dans notre cas cela se fait en ajoutant la ligne suivante
dans la partie `head` de la page HTML, avant la
déclaration de nos propres scripts :

~~~javascript
<script src="http://maps.google.com/maps/api/js?sensor=false" type="text/javascript"></script>
~~~

Il faudra également que notre page HTML contienne un élément
identifié qui accueillera l'image de la carte désirée. Donc quelque
chose comme :


On peut bien sûr ajouter des informations CSS telle `class="..."`




~~~javascript
<div id="maCarte"></div>
~~~


Le chargement de cette API nous permet d'en utiliser les
 définitions. En particulier nous avons maintenant accès à un nouveau
 type de données représentant les
 cartes : `google.maps.Map`.

Pour créer une telle donnée, il faut donner deux informations. La
 première est l'élément HTML de la page qui contiendra la carte, le
 second est une donnée représentant des propriétés de cette
 carte. L'API définit la structure de ces propriétés représentées par le
 type `google.map.MapOptions`. Ces _options_
 définissent en particulier :



Les valeurs définies par le type `google.maps.MapTypeId`
 sont : `ROADMAP`, `SATELLITE`,
 `HYBRID` et `TERRAIN`.





* les coordonnées (latitude, longitude) du centre de la carte :
 option `center`, de type `google.maps.LatLng`
* le facteur de zoom : option `zoom`, un entier
* le type de carte utilisée :
 option `mapTypeId`, de
 type `google.maps.MapTypeId`


Pour créer une carte, il faut donc définir ces données ce qui donne
 quelque chose comme :


~~~javascript
var lElement  = document.getElementById("maCarte");
var leCentre = new google.maps.LatLng(50.609731,3.137511);
var lesOptions = {
	center: leCentre,
	zoom: 17,
	mapTypeId: google.maps.MapTypeId.ROADMAP
};

var laCarte = new google.maps.Map(lElement, lesOptions);
~~~


Les scripts Google Map et les informations sur les images sont
obtenus à partir d'information récupérer par le réseau. Pour éviter
des problèmes d'affichage de la page, il est donc préférable des
déclencher la création de la carte après le chargement complet de la
page. On utilisera comme précédemment un événement `load`
sur l'élément `window` qui appellera une fonction dont le
traitement correspondra au code ci-dessus.


Rassemblez les différentes informations pour construire une page
contenant votre première carte Google Map non statique.
Vous devriez obtenir [ ce résultat](http://qkzk.xyz/docs/doc04/exemples/googleMap1.html).




L'API propose sur les données de type carte les
fonctions `setCenter`, `setZoom`
et `setMapTypeId` qui ont pour effet de modifier les
options correspondantes pour la carte concernée. Ainsi


    laCarte.setZoom(15);



fixe le facteur de zoom de la donnée `laCarte` à 15.


Pour obtenir les coordonnées d'un point particulier, rendez-vous sur
le site [http://maps.google.fr/](http://maps.google.fr/),
affichez une carte contenant ce point, cliquez-droit dessus et
choisissez _Plus d'infos sur cet endroit_. Les coordonnées
s'affichent alors dans la zone de texte en haut.








1. Adaptez l'exercice précédent pour centrer la carte sur votre lycée.
2. Ajoutez aux options déjà gérées celle-ci :


    disableDefaultUI: true



et testez.
3. Idem pour celle-ci


    scrollwheel:false




4. Pour faciliter le travail qui suit, nous allons gérer dans une variable globale
pour représenter la donnée de type `google.maps.Map`
manipulée.
Faites la modification nécessaire qui consiste à placer la déclaration


    var laCarte



en dehors de toute fonction et à ne pas la masquer par une déclaration
locale au sein d'une fonction.
5. Ajoutez à votre page un champ de saisie (`input`) dans
lequel l'utilisateur peut fournir un entier. A chaque changement de
valeur, le facteur de zoom de la carte est changé.
6. Ajoutez deux nouveaux champs de saisie, un pour la
latitude, un pour la longitude, à chaque changement de l'un ou
l'autre on change le centre de la carte en conséquence.
7. Ajoutez un "bouton" qui permet de basculer entre les affichages en
mode "_satellite_" et "_route_", sachant qu'initialement
le mode est "_route_".




Parmi les possibilités offertes par l'API on trouve aussi la
gestion des "_marqueurs_" que l'on place sur une carte. Ce sont
des données de type `google.maps.Marker`. Pour créer un
marqueur il faut préciser sa position (les coordonnées où il se
trouve) et la carte où on le place. Ces informations sont cette fois
définies par des données `google.maps.MarkerOptions` :


    var point = new google.maps.LatLng(50.609731,3.137511);
    var marqueurOption = {
                          position: point,
    		      map: laCarte
    	             }
    var punaise = new google.maps.Marker(marqueurOption);



On peut aussi préférer écrire ainsi :


    var punaise = new google.maps.Marker({
    		position: new google.maps.LatLng(50.609731,3.137511),
    		map: laCarte
    	      });









1. Ajoutez ce code à la page créée lors de la **Manip' 1** pour en
constater le résultat.
2. Ajoutez deux nouveaux champs de saisie, un pour la
latitude, un pour la longitude, plus un "bouton" **Ajouter**. Un
clic sur ce bouton provoque l'ajout sur la carte d'un marqueur aux
coordonnées fournies par les deux champs de saisie.




Une API bien construite doit être cohérente. Cela facilite son
apprentissage. C'est le cas de l'API Google Map. Ainsi il existe un
type `google.maps.InfoWindow` qui dispose des mêmes
options que les marqueurs, avec en plus une
option `content` dont la valeur est une chaîne de
caractères contenant du code HTML.






1. Ajoutez une "_info window_" à la place de la punaise
précédente. Mettez pour `content` la valeur `"un
**premier** exemple d'info"`.
2. Testez
3. Modifiez pour centrer la carte sur votre lycée et afficher
une fenêtre d'information qui reprend le nom de votre lycée et une
photo de celui-ci (pas trop grande !)
4. Reprenez la **Manip'** sur les monuments et affichez dans une
page la carte de France (cherchez le bon zoom initial) avec
une _info window_ par monument.










1. Reprenez le travail produit à la **Manip' 1** et ajoutez le
code suivant à la fin de la fonction de création de la carte :


        laCarte.setZoom(16);
        laCarte.setCenter(50.610716,3.140007);

        var pointsTrajetRU = [
    	new google.maps.LatLng(50.609731,3.137511),
    	new google.maps.LatLng(50.610233,3.137721),
    	new google.maps.LatLng(50.609682,3.139406),
    	new google.maps.LatLng(50.610757,3.140103),
    	new google.maps.LatLng(50.610716,3.140318),
    	new google.maps.LatLng(50.61103,3.141294),
    	new google.maps.LatLng(50.611459,3.142131),
    	new google.maps.LatLng(50.611642,3.142646),
    	new google.maps.LatLng(50.612037,3.143225)
        ];

        var lignesTrajetRU = new google.maps.Polyline({
    	path: pointsTrajetRU,         // le chemin du tracé
    	strokeColor: "#AAAAFF",       // la couleur du tracé
            map: laCarte
        });



Il vous permet de visualiser le trajet entre le bâtiment M3 qui
héberge le Laboratoire d'Informatique de Lille ([LIFL](http://www.lifl.fr)) et le
Restaurant Universitaire sur le campus de Lille 1.
2. Testez le résultat et analysez ce code pour comprendre son
fonctionnement
3. En vous en inspirant, créez une page sur laquelle vous afficherez
une carte avec un marqueur pour votre domicile et un pour votre
lycée et vous tracerez le trajet que vous empruntez chaque matin
pour vous rendre au lycée (adaptez le facteur de zoom si nécessaire).
