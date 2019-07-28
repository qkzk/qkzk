---
author: qu3nt1n
date: 2016-07-09 07:44:59+00:00
draft: false
title: '00. Réseau : internet et protocole HTTP'
weight: -1
---



Que se passe-t-il lorsque vous tapez dans la barre d'adresse de votre navigateur «http://www.google.fr» ?

Votre ordinateur (que l'on appellera le client) va chercher à entrer en communication avec un autre ordinateur (que l'on appellera le serveur) se trouvant probablement à des milliers de kilomètres de chez vous. Pour pouvoir établir cette communication,
il faut bien sûr que les 2 ordinateurs, le client et le serveur, soient « reliés ». On dira que nos 2 ordinateurs sont en réseau.

Il existe énormément de réseaux (les ordinateurs de la salle sont tous en « réseau »), certains réseaux sont reliés à d'autres réseaux qui sont eux-mêmes reliés à d'autres réseaux........ce qui forme « des réseaux de réseaux de réseaux...... ».
Savez-vous comment on appelle cet assemblage multiple de réseaux ? Internet !

Mon but ici n'est pas de vous expliquez comment font les ordinateurs pour se trouver dans cet « amas de réseaux », si ce sujet vous intéresse,
vous rencontrerez certains termes, comme : «routeur », « routage ».......


#### Adresse IP


Tout ordinateur possède une adresse sur un réseau : son adresse IP.

C'est grâce à cette adresse que les différents ordinateurs peuvent s'identifier sur un réseau.

Une adresse IP est de la forme "74.125.133.94" (cette adresse IP correspond au serveur de google "google.fr")

Comme cette suite de nombres n'est pas très simple à retenir, des serveurs appelés serveurs DNS se chargent de la traduction des noms en adresses IP. Par exemple, un serveur DNS traduira "google.fr" en "74.125.133.94"


#### Notion de client-serveur


En tapant «http://www.google.fr», votre machine va chercher à entrer en communication avec le serveur portant le nom «www.google.fr» (en fait c'est plus compliqué, pour les puristes nous dirons donc que la communication va être établie avec le serveur www du domaine google.fr, mais bon, pour la suite nous pourrons nous contenter de l'explication « simplifiée »).

Une fois la liaison établie, le client et le serveur vont échanger des informations en dialoguant :

client : bonjour www.google.fr (ou bonjour www se trouvant dans le domaine google.fr), pourrait tu m'envoyer le code html contenu dans le fichier index.html

serveur : OK, voici le code html demandé

client : je constate que des images, du code css et du code JavaScript sont utilisés, peux-tu me les envoyer

serveur : OK, les voici

Évidemment ce dialogue est très imagé, mais il porte tout de même une part de « vérité ».

J'espère que vous commencez à comprendre les termes client (celui qui demande quelque chose) et serveur (celui qui fournit ce qui a été demandé).


#### et le HTTP ?


Nous venons de voir que les ordinateurs communiquent entre eux, pour assurer cette communication, ils utilisent ce que l'on appelle des protocoles.

Selon Wikipedia, dans le cas général, protocole :

_On nomme protocole les conventions qui facilitent une communication sans faire directement partie du sujet de la communication elle-même._

En électronique et en informatique (toujours selon Wikipedia) :

_un protocole de communication est un ensemble de contraintes permettant d'établir une communication entre deux entités (dans le cas qui nous intéresse 2 ordinateurs)_

Pour que la communication soit possible, le client et le serveur doivent avoir des règles communes, ces règles sont définies dans un protocole. Comme vous l'avez sans doute deviné, le protocole de communication employé ici se nomme HTTP.

Le protocole HTTP (HyperText Transfer Protocol) a été inventé par Tim Berners-Lee (1955-....) au début des années 1990. Tim Berners-Lee est aussi à l'origine du langage HTML et des « adresses web ». C'est la combinaison de ces 3 éléments (HTTP, HTML, « adresse web ») que l'on nomme aujourd'hui le « web » (« web » qu'il ne faut pas confondre avec l'internet (erreur ultra classique), même si le web utilise l'internet).

Le HTTP va permettre au client d'effectuer des requêtes à destination d'un serveur. En retour, le serveur va envoyer une réponse.

Voici une version simplifiée de la composition d'une requête :



 la méthode employée pour effectuer la requête
 l'URL de la ressource
 la version du protocole utilisé par le client (souvent HTTP 1.1)
 le navigateur employé (Firefox, Chrome) et sa version
 le type du document demandé (par exemple HTML)
 ...

Certaines de ces lignes sont optionnelles.

Voici un exemple de requête HTTP (la méthode, l'URL et la version du protocole se trouvent sur la première ligne) :


    GET /mondossier/monFichier.html HTTP/1.1
    User-Agent : Mozilla/5.0
    Accept : text/html


Revenons uniquement sur 2 aspects (si nécessaire nous reviendrons sur les autres plus tard) : la méthode employée et l'URL.


#### Les méthodes des requêtes HTTP


Une requête HTTP  utilise une méthode (c'est une commande qui demande au serveur d'effectuer une certaine action). Voici la liste des méthodes disponibles :

GET, HEAD, POST, OPTIONS, CONNECT, TRACE, PUT, PATCH, DELETE

Détaillons 4 de ces méthodes :



 GET : C'est la méthode la plus courante pour demander une ressource. Elle est sans effet sur la ressource.
 POST : Cette méthode est utilisée pour soumettre des données en vue d'un traitement (côté serveur). Typiquement c'est la méthode employée lorsque l'on envoie au serveur les données issues d'un formulaire ( avec une balise form, voir les activités sur HTML5 et CSS3).
 DELETE : Cette méthode permet de supprimer une ressource sur le serveur.
 PUT : Cette méthode permet de modifier une ressource sur le serveur



#### L'URL (et l'URI)


Une URI (Uniform Ressource Identifier) permet d'identifier une ressource sur un réseau, une URL est un cas particulier d'URI. Nous ne nous attarderons pas sur les subtiles différences entre une URI et une URL et à partir de maintenant je parlerai exclusivement d'URL (par souci de simplification).

L'URL indique « l'endroit » où se trouve une ressource sur le serveur. Un fichier peut se trouver dans un dossier qui peut lui-même se trouver dans un autre dossier.....on parle d'une structure en arborescence, car elle ressemble à un arbre à l'envers :

![arbo](http://informatiquelycee.fr/img/url.jpg)


Comme vous pouvez le constater, la base de l'arbre s'appelle la racine de l'arborescence et se représente par un /


#### Chemin absolu ou chemin relatif ?


Pour indiquer la position d'un fichier (ou d'un dossier) dans l'arborescence, il existe 2 méthodes : indiquer un chemin absolu ou indiquer un chemin relatif. Le chemin absolu doit indiquer « le chemin » depuis la racine. Par exemple l'URL du fichier fichier3.txt sera : /dossier2/dossier3/fichier3.jpg

Remarquez que nous démarrons bien de la racine / (attention les symboles de séparation sont aussi des /)

Imaginons maintenant que le fichier fichier1.css fasse appel au fichier fichier3.jpg (comme un fichier HTML peut faire appel à un fichier CSS ou JavaScript). Il est possible d'indiquer le chemin non pas depuis la racine, mais depuis le dossier (dossier2) qui accueille le fichier1.css, nous parlerons alors de chemin relatif :

dossier3/fichier3.jpg

Remarquez l’absence du / au début du chemin (c'est cela qui nous permettra de distinguer un chemin relatif et un chemin absolu).

Imaginons maintenant que nous désirions indiquer le chemin relatif du fichier fichier1.txt depuis le dossier dossier4.

Comment faire ?

Il faut « reculer » d'1 « cran » dans l'arborescence (pour se retrouver dans le dossier dossier2 et ainsi pouvoir repartir vers la bonne « branche ». Pour ce faire il faut utiliser 2 points : ..

../dossier2/fichier3.jpg

Il est tout à fait possible de remonter de plusieurs « crans » : ../../ depuis le dossier dossier4 permet de « retourner » à la racine.

Remarque : la façon d'écrire les chemins (avec des slash (/) comme séparateurs) est propre aux systèmes dits « UNIX », par exemple GNU/Linux ou encore Mac OS. Sous Windows, ce n'est pas le slash qui est utilisé, mais l'antislash (\). Pour ce qui nous concerne ici, les chemins réseau (et donc le web), pas de problème, c'est le slash qui est utilisé.


#### Réponse du serveur à une requête HTTP


Une fois la requête reçue, le serveur va renvoyer une réponse, voici un exemple de réponse du serveur :


    HTTP/1.1 200 OK
    Date: Thu, 15 feb 2013 12:02:32 GMT
    Server: Apache/2.0.54 (Debian GNU/Linux) DAV/2 SVN/1.1.4
    Connection: close
    Transfer-Encoding: chunked
    Content-Type: text/html; charset=ISO-8859-1
    <!doctype html>
    <html lang="fr">
    <head>
    <meta charset="utf-8">
    <title>Voici mon site</title>
    </head>
    <body>
     <h1>Hello World! Ceci est un titre</h1>
    <p>Ceci est un <strong>paragraphe</strong>. Avez-vous bien compris ?</p>
    </body>
    </html>


Nous n'allons pas détailler cette réponse, voici quelques explications sur les éléments qui nous seront indispensables par la suite :

Commençons par la fin : le serveur renvoie du code HTML, une fois ce code reçu par le client, il est interprété par le navigateur qui affiche le résultat à l'écran. Cette partie correspond au corps de la réponse.

La 1re ligne se nomme la ligne de statut :



 HTTP/1.1 : version de HTTP utilisé par le serveur
 200 : code indiquant que le document recherché par le client a bien été trouvé par le serveur. Il existe d'autres codes dont un que vous connaissez peut-être déjà : le code 404 (qui signifie  «Le document recherché n'a pu être trouvé»).

Les 5 lignes suivantes constituent l'en-tête de la réponse, une ligne nous intéresse plus particulièrement : «Server: Apache/2.0.54 (Debian GNU/Linux)».

Server: Apache/2.0.54 (Debian GNU/Linux) DAV/2 SVN/1.1.4


#### Les serveurs HTTP


Il existe différents types de serveur capable de répondre à des requêtes HTTP (on les appelle serveurs HTTP ou encore serveurs web). Que faut-il pour constituer un serveur web ?



 un ordinateur (souvent ce sont des machines spécialisées : elles sont conçues pour fonctionner 24h/24h mais il est possible d'utiliser un ordinateur « classique » surtout si votre but est uniquement de faire des tests).
 un système d'exploitation : Les distributions GNU/Linux sont, pour différentes raisons, à privilégier. Dans la réponse HTTP que nous avons étudiée ci-dessus, le serveur fonctionne sous une distribution GNU/Linux dénommée Debian (mais si vous êtes sous Windows, il est tout de même possible de mettre en place un serveur web).
 Un logiciel destiné à recevoir les requêtes HTTP et à fournir des réponses. Un des logiciels les plus « populaires » se nomme Apache (il équipe plus de la moitié de serveur web en activité dans le monde !), mais il en existe d'autres : nginx, lighttpd......(j'ai volontairement choisi d'évoquer uniquement les solutions « libres », mais vous devez savoir qu'il existe aussi des solutions « propriétaires », si c'est 2 termes vous sont inconnus, il serait bon de rechercher leur signification).



#### Les langages côté serveur


Il y a quelques années, le web était dit « statique » : le concepteur de site web écrivait son code HTML et ce code était simplement envoyé par le serveur au client. Les personnes qui consultaient le site avaient toutes le droit à la même page, le web était purement « consultatif » (nous étions encore très loin des « single page application » que nous verrons plus tard).

Les choses ont ensuite évolué : les serveurs sont aujourd'hui capables de générer eux même du code HTML. Les résultats qui s'afficheront à l'écran dépendront donc des demandes effectuées par l'utilisateur du site : le web est devenu dynamique.

Différents langages de programmation peuvent être utilisés « côté serveur » afin de permettre au serveur de générer lui même le code HTML à envoyer. Le plus utilisé encore aujourd'hui se nomme PHP (PHP Hypertext Preprocessor : c'est un acronyme récursif comme GNU qui signifie GNU's Not Unix). D'autres langages sont utilisables côté serveur (pour permettre la génération dynamique de code HTML), voici un liste non exhaustive : Java, Python, ASP....

Demander au serveur d'effectuer tous les calculs pour toutes les pages n'est pas toujours une bonne idée. En effet le client dispose aussi d'un ordinateur ! Il existe donc des langages qui font travailler le client, en particulier JavaScript. Une page contenant un script JavaScript sera donc traitée par le client. Ceci permet d'y intégrer des programmes parfois lourds et complexes (des jeux vidéos, du traitement de donnée) parfois très simples (vérification qu'un email saisi respecte bien le format souhaité, qu'un mot de passe contient assez caractères etc.). Pour d'évidentes questions de sécurité, ce code ne peut faire n'importe quoi : imaginons une page d'apparence anodine qui, sans vous l'afficher, efface le contenu de votre machine ! Le navigateur n'a pas la liberté de manipuler les fichiers de votre machine depuis du code javascript, par exemple. Tout n'est donc pas possible « côté client ».




_Sources : http://informatiquelycee.fr/_
