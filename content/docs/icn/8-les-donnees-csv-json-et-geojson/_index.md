---
author: qu3nt1n
date: 2016-07-09 07:04:36+00:00
draft: false
title: 08. Les données CSV, JSON et GeoJSON

url: /
---




## Prérequis :


il est souhaitable (mais non indispensable) d'avoir quelques idées sur les notions de réseau et de client-serveur. Vous trouverez [ici](http://qkzk.xyz/?page_id=631) toutes les informations dont vous aurez besoin pour suivre cette série d'activités. Des connaissances en JavaScript sont aussi souhaitables.

Sur internet, il est possible de trouver un grand nombre d'informations. Ces informations sont, dans la plupart des cas, stockées sur des serveurs dans des bases de données.

Quand un client interroge un serveur afin de récupérer des données, le serveur effectue une requête auprès de la base de données et renvoie ensuite les informations demandées vers le client.

Sous quelle forme ces données transitent-elles entre le client et le serveur ?

Nous n'allons pas chercher à être exhaustifs et nous allons uniquement voir 3 exemples : le CSV, le JSON et le geoJSON.

Vous devez savoir qu'il existe d'autres formats de données, par exemple le XML (pour en savoir plus sur le XML, vous pouvez consulter le cours proposé par l'excellent site openclassrooms : [ici](https://openclassrooms.com/courses/structurez-vos-donnees-avec-xml)), mais j'ai choisi de me restreindre aux 3 formats évoqués ci-dessus.


## Le format CSV











Premier format que nous allons étudier, le CSV (Comma separated values). Sur de nombreux sites, il est possible de télécharger des fichiers au format csv (nom_du_fichier.csv).

Voici ce que nous dit Wikipédia sur le format CSV :

_Comma-separated values, connu sous le sigle CSV, est un format informatique ouvert représentant des données tabulaires sous forme de valeurs séparées par des virgules._

_Un fichier CSV est un fichier texte, par opposition aux formats dits « binaires ». Chaque ligne du texte correspond à une ligne du tableau et les virgules correspondent aux séparations entre les colonnes. Les portions de texte séparées par une virgule correspondent ainsi aux contenus des cellules du tableau._

Voici un exemple du contenu d'un fichier CSV:

    
    nom,prenom,date_naissance
    Durand,Jean-Pierre,23/05/1985
    Dupont,Christophe,15/12/1967
    Terta,Henry,12/06/1978


Je pense qu'il est évident pour vous que nous avons ici 3 personnes :



 	  * Jean-Pierre Durand qui est né le 23/05/1985
 	  * Christophe Dupont qui est né le 15/12/1967
 	  * Henry Terta qui est né le 12/06/1978

ATTENTION :

La virgule est un standard pour les données anglo-saxonnes, mais pas pour les données aux normes françaises. En effet, en français, la virgule est le séparateur des chiffres décimaux. Il serait impossible de différencier les virgules des décimaux et les virgules de séparation des informations. C’est pourquoi on utilise un autre séparateur : le point-virgule (;). Dans certains cas cela peut engendrer quelques problèmes, vous devrez donc rester vigilants sur le type de séparateur utilisé.

Les tableurs, tels que "Calc" (Libre Office), sont normalement capables de lire les fichiers au format CSV. J'ai précisé "normalement" car certains tableurs gèrent mal le séparateur CSV "point-virgule" et le séparateur des chiffres décimaux "virgule".


#### À faire vous-même 1.1


Après avoir téléchargé le fichier [ident_pointVirgule.csv](http://informatiquelycee.fr/asset/ident_pointVirgule.csv), ouvrez ce dernier à l'aide d'un tableur.

Si par hasard votre tableur ne gère pas correctement le fichier avec le séparateur "point-virgule", voici une version "séparateur virgule" du fichier : [ident_virgule.csv](http://informatiquelycee.fr/asset/ident_virgule.csv)

Dans la suite, gardez toujours cet éventuel problème à l'esprit (surtout avec des données "made in France")



* * *



Vous devriez obtenir ceci :

![](http://informatiquelycee.fr/img/procAnDo_a1_1.png)


Vous pouvez constater que les données sont bien "rangées" dans un tableau avec des lignes et des colonnes (voilà pourquoi on parle de données tabulaires.

Il est possible de trouver sur le web des données beaucoup plus intéressantes à traiter que celles contenues dans le fichier "ident_pointVirgule.csv" (ou "ident_virgule.csv"). Par exemple, le site [sql.sh](http://sql.sh/736-base-donnees-villes-francaises), propose un fichier csv contenant des informations sur l'ensemble des communes françaises.


#### À faire vous-même 1.2


Ouvrez le fichier [ville_point_virgule.csv](http://www.ac-grenoble.fr/disciplines/informatiquelycee/asset/ident_pointVirgule.csv) à l'aide d'un tableur (c’est une version légèrement modifiée de celle disponible sur le site sql.sh, j’y ai notamment ajouté des entêtes). En cas de problème avec votre tableur, voici une version "séparateur virgule" : [ville_virgule.csv](http://www.ac-grenoble.fr/disciplines/informatiquelycee/asset/ident_virgule.csv) (attention le séparateur "décimal" est ici le point)



* * *



Comme vous pouvez le constater, nous avons 12 colonnes (et 36700 lignes si on ne compte pas l'entête !), voici la signification de ces colonnes :



 	  * dep : numéro de département
 	  * nom : nom de la commune
 	  * cp : code postal
 	  * nb_hab_2010 : nombre d'habitants en 2010
 	  * nb_hab_1999 : nombre d'habitants en 1999
 	  * nb_hab_2012 : nombre d'habitants en 2012 (approximatif)
 	  * dens : densité de la population (habitants par kilomètre carré)
 	  * surf : superficie de la commune en kilomètre carré
 	  * long : longitude
 	  * lat : latitude
 	  * alt_min : altitude minimale de la commune (il manque des données pour certains territoires d'outre-mer)
 	  * alt_max : altitude maximale de la commune (il manque des données pour certains territoires d'outre-mer)

Vous trouverez un grand nombre de données, diverses et variées, au format CSV sur le site gouvernemental [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/?format=csv).

Il existe aussi un format très voisin du CSV, le TSV (Tab-separated values) où le séparateur est une tabulation (touche avec le symbole ↹)







* * *





## Le format JSON






Autre format de données très courant sur le "web", le JSON (JavaScript Object Notation). Le JSON fonctionne avec un système de paire clé/valeur. Le format JSON, comme son nom l'indique, est dérivé de la notation des objets du JavaScript.

Un objet JavaScript est encadré par des accolades :

    
    {cle_1 : val_1, cle_2 : val_2, cle_3 : val_3}


souvent, pour une question de lisibilité, on écriera :

    
    {
        cle_1 : val_1, 
        cle_2 : val_2, 
        cle_3 : val_3
    }
    


Un fichier au format JSON peut regrouper un grand nombre d'objets :

    
    [{
        "nom" : "Durand", 
        "prenom" : "Jean-Pierre", 
        "date_naissance" : "23/05/1985"
    },
    {
        "nom" : "Dupont", 
        "prenom" : "Christophe", 
        "date_naissance" : "15/12/1967"
    },
    {
        "nom" : "Terta", 
        "prenom" : "Henry", 
        "date_naissance" : "12/06/1978"
    }]


Ci-dessus, nous avons un tableau contenant des objets.

La "valeur" d'une paire "clé/valeur" peut être un tableau :

    
    {
        "nom" : "Durand", 
        "prenom" : "Jean-Pierre", 
        "date_naissance" : "23/05/1985"
        "sport" : ["tennis", "football", "pétanque"]
    }
    


ou même un autre objet :

    
    {
        "nom" : "Durand", 
        "prenom" : "Jean-Pierre", 
        "date_naissance" : "23/05/1985"
        "adresse" : {"num":6, "rue":"impasse du rossignol", "ville":"Nogent-le-Rotrou", "cp":"28400"}
    }


Comme vous pouvez le constater, il est possible d'obtenir des structures de données très complexes avec le format JSON.

Comment utiliser les données présentes dans le fichier JSON ?

Si le fichier JSON contient un seul objet (pour simplifier l'explication, nous "rangerons" cet objet dans une variable) :

    
    var data = {
        "nom" : "Durand", 
        "prenom" : "Jean-Pierre", 
        "date_naissance" : "23/05/1985"
        "adresse" : {"num":6, "rue":"impasse du rossignol",
        "ville":"Nogent-le-Rotrou", "cp":"28400"}
    }


Il suffit d'utiliser la "notation pointée" : "data.nom" permet de récupérer le nom (ici "Durand"), "data.prenom" permet de récupérer le prénom (ici "Jean-Pierre") ou plus compliqué, "data.adresse.rue" sera égal à "impasse du rossignol" dans l'exemple ci-dessus

Si le fichier JSON contient un tableau d'objet :

    
    var tabData=[{
        "nom" : "Durand", 
        "prenom" : "Jean-Pierre", 
        "date_naissance" : "23/05/1985"
    },
    {
        "nom" : "Dupont", 
        "prenom" : "Christophe", 
        "date_naissance" : "15/12/1967"
    },
    {
        "nom" : "Terta", 
        "prenom" : "Henry", 
        "date_naissance" : "12/06/1978"
    }]


Comme ici, nous avons un tableau contenant des objets, il faudra utiliser la notation habituelle pour les tableaux, suivit de la "notation pointée" :

"tabData[0].nom" renverra "Durand", "tabData[1].prenom" renverra "Christophe"...

Pour en savoir plus sur le JSON, vous pouvez lire l'article sur [Wikipédia](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation).


#### À faire vous-même 2.1


Téléchargez le fichier [ident.json](http://informatiquelycee.fr/asset/ident.json) et ouvrez-le à l'aide d'un éditeur de texte.



* * *



De nombreux sites web proposent des services basés sur des API (Application Programming Interface). Ces sites sont capables de fournir des données aux formats JSON sur "simple demande". Souvent, ces "demandes" sont effectuées par l'intermédiaire d'une url (si vous avez besoin de vous rafraichir la mémoire à propos de la notion d'url, n'hésitez pas à consulter ce [document](http://informatiquelycee.fr/reseau_a1.html)).

Nous allons illustrer ce propos en utilisant l'API d'un site qui fournit des informations météo au format JSON. Vous trouverez ce site à l'adresse suivante : [openweathermap.org/api](http://openweathermap.org/api)

Pour profiter de ce service, il est nécessaire de s'inscrire ([http://home.openweathermap.org/users/sign_up](http://home.openweathermap.org/users/sign_up)) afin de pouvoir récupérer une clé (API key). Notez bien cette clé quelque part, elle vous servira dès que vous voulez accéder au service.


#### À faire vous-même 2.2


Ouvrez votre navigateur préféré et copier-coller l'url suivante dans la barre d'url du navigateur :

    
    http://api.openweathermap.org/data/2.5/weather?q=hazebrouck,fr&lang=fr&units=metric&APPID=XXXXXXXXXXXXX


ATTENTION : il faut remplacer les "X" par la clé (API key) que vous aurez obtenue lors de votre inscription.



* * *



Au lieu d'obtenir, comme d'habitude, une page web, vous devriez obtenir uniquement quelque chose qui ressemblera à ceci :

    
    {"coord":{"lon":2.54,"lat":50.72},
    "weather":[{"id":501,"main":"Rain","description":"pluies modérées","icon":"10d"}],
    "base":"stations",
    "main":{"temp":17.46,"pressure":1020,"humidity":82,"temp_min":16,"temp_max":20.1},
    "visibility":10000,
    "wind":{"speed":4.1,"deg":240},
    "rain":{"1h":1.52},
    "clouds":{"all":75},
    "dt":1468048824,
    "sys":{"type":1,"id":5625,"message":0.0338,"country":"FR","sunrise":1468036100,"sunset":1468094487},
    "id":3013619,
    "name":"Hazebrouck",
    "cod":200}


Comme les données sont réactualisées relativement souvent, vous n'obtiendrez pas la même chose que moi !

Avec une simple url, le site open weather renvoie des informations météo sous forme de données JSON.

Détaillons l'url :

    
    http://api.openweathermap.org/data/2.5/weather


Cette partie de l'url ne changera pas (sauf si vous désirez autre chose que les conditions météo actuelles, à ce moment-là, il faudra remplacer "weather" par autre chose (consulter le site open weather pour plus d'informations)).

    
    ?q=hazebrouck,fr&lang=fr&units=metric&APPID=XXXXXXXXXXXXX


À partir du point d'interrogation, vous devez renseigner les différents paramètres qui permettront à open weather de vous renvoyer les bonnes informations. Ces paramètres sont séparés par le caractère "&".



 	  * "q=hazebrouck,fr" le paramètre "q" correspond au nom de la ville suivi du pays (fr dans notre cas)
 	  * "lang=fr" la langue utilisée sera le français
 	  * "units=metric" on désire avoir les longueurs en mètres (et les vitesses en mètre par seconde).
 	  * "APPID" correspond à l'API key

Il est possible de construire des requêtes beaucoup plus complexes, encore une fois, veuillez consulter le site open weather pour plus d'informations.

Intéressons-nous maintenant aux données JSON renvoyées (nous n'allons pas tout détailler) :

 	  * "coord":{"lon":2.54,"lat":50.72} latitude et longitude du lieu
 	  * "weather":[{"id":501,"main":"Rain","description":"pluies modérées","icon":"10d"}] "weather" correspond à un tableau qui contient un seul objet.
 	  * "main":{"temp":17.46,"pressure":1020,"humidity":82,"temp_min":16,"temp_max":20.1} "main" correspond à un objet qui contient différents types d'informations
 	  * "dt":1468048824 "dt" nous donne l'heure et la date de diffusion du bulletin au format "timestamp" (voir [ici](http://www.timestamp.fr/) pour plus d'informations sur la notion de timestamp). Nous utiliserons "dt" dans le prochain "À faire vous-même".
 	  * "sunrise":1468036100,"sunset":1468094487 : respectivement heure de lever et de coucher du soleil au format timestamp







* * *





## Les données GeoJSON






Le geoJSON est un format ([http://geojson.org/](http://geojson.org/)) qui permet d'encoder des données à "caractère géographiques". Voici ce que dit Wikipédia à propos de ce format :


<blockquote>GeoJSON (de l'anglais Geographic JSON, signifiant littéralement JSON géographique) est un format ouvert d'encodage d'ensemble de données géospatiales simples utilisant la norme JSON (JavaScript Object Notation). Il permet de décrire des données de type point, ligne, chaîne de caractères, polygone, ainsi que des ensembles et sous-ensembles de ces types de données et d'y ajouter des attributs d'information qui ne sont pas spatiale. Le format GeoJSON, contrairement à la majorité des standards de systèmes d'informations géographiques, n'est pas écrit par l'Open Geospatial Consortium, mais par un groupe de travail de développeurs au travers d'internet.</blockquote>


Comme indiqué dans Wikipédia, le geoJSON est avant tout du JSON et nous le traiterons comme tel.


#### À faire vous-même 3.1


Dans la barre d'adresse de votre navigateur, tapez l'adresse suivante :

    
    http://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson


Vous devriez obtenir quelque chose ressemblant à ceci :





* * *



Le site "earthquake.usgs.gov", comme le site "http://openweathermap.org/", propose une API qui renvoie des données à partir d'une simple url. Le site "earthquake.usgs.gov" renvoie des données au format geoJSON (c'est donc du JSON), ces données contiennent des informations sur les tremblements de terre détectés dans le monde sur une période de 30 jours. Le site vous propose différentes options pour la requête, vous trouverez une description complète de ces options [ici](http://earthquake.usgs.gov/fdsnws/event/1/)


#### À faire vous-même 3.2


En vous aidant de la documentation présente sur le site [http://earthquake.usgs.gov](http://earthquake.usgs.gov/fdsnws/event/1/), écrivez une requête sous forme d'url qui permettra d'obtenir des données (au format geoJSON) sur les tremblements de terre, d'une magnitude supérieure à 5, ayant eu lieu ces 30 derniers jours partout dans le monde.

Testez votre requête en la copiant dans la barre d'adresse de votre navigateur. Une fois les données obtenues, étudiez-les afin de comprendre la structure de ces données.



* * *





#### Approfondissement


Ces données incluant des coordonnées GPS il est possible de les intégrer dans une carte... Celle-ci peut être statique (Le tremblements de terre des 30 derniers jours à la date à laquelle vous l'aurez crée) ou dynamique (Les tremblements de terre des 30 derniers jours à la date du chargement de la page !)
C'est difficile cependant étant donné qu'il faut formater beaucoup de données et les lier à un objet très différent, la carte.
d3js est une librairie javascript permettant ce genre d'opération complexe.




_Sources : http://informatiquelycee.fr/_
