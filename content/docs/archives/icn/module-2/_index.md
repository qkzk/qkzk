---
author: qu3nt1n
date: 2016-07-01 12:40:21+00:00
draft: false
title: 'module 2 : web'
weight: -8

---

# Première partie :




## Objectifs de cette partie :


**Rédiger une première page html **




Pré-requis On suppose qu'ont été vues les notions de :



 tutoriel openclassrooms : [introduction à l'html partie 1](http://openclassrooms.com/courses/apprenez-a-creer-votre-site-web-avec-html5-et-css3/comment-fait-on-pour-creer-des-sites-web)

Notions abordées



 création d'une page html
 mise en ligne







## activités en classe :






 	    * Chaque groupe se voit attribué un des thèmes (de a à g) référencés plus bas. Il rédige un article de 4 paragraphes de quelques lignes dans notepad++ portant sur le thème attribué.
_N’hésitez pas à employer Wikipédia, notre objectif ici n’est pas de rédiger par vous même mais de citer de l’information fiable._
 	    * **Thèmes :
a) persistance de l’information, b) addiction aux nouvelles technologies, c) fracture numérique, d) big data, e) informatique dans les nuages, f) intelligence artificielle, g) cyber criminalité, h) cryptographie.**




 L’article est ensuite inséré paragraphe par paragraphe dans un fichier html très basique nommé **act1_a.html** ( act1_b.html etc.)
Il nous servira à créer la structure de la page :


    <html>
    <head>
    	<title> Votre thème </title>
    	</head>
    <body>
    	<h1 id="titre"> Votre thème </h1>
    		<h2> Sous titre 1 </h2>
    			<p> votre premier paragraphe </p>
    			<img src="l'adresse de votre première image">

    		<h2> Sous titre 2 </h2>
    			<p> votre second paragraphe </p>
    			<img src="l'adresse de votre seconde image">
    		etc.
    		<h2> Sources </h2>
    		<a href="./index.html"> Retour au sommaire</a>
    </body>
    </html>



 Des liens vers les sources et vers la racine du site de la classe :
`<a href="./index.html"> Retour au sommaire </a>` sont introduits et correctement référencés.
 Le fichier est alors testé localement de façon exhaustive (chaque mot, chaque image, chaque lien etc.).
Un problème apparait avec le lien ./index.html lors du test local.
L’expliquer dans un mail au professeur et proposer une solution avec le nom du groupe. Le premier groupe à fournir une réponse correcte gagnera des points.
 Le fichier et les images associées sont déposés sur le serveur ftp de free à l'aide de FileZilla
_A l'heure actuelle, les connexions FTP depuis le lycée vers un serveur situé à l'extérieur sont bloquées et je ne peux rien y faire. Cette partie est donc à terminer chez vous !
Je proposerai une résolution partielle du problème avec des tests LOCAUX, sur ma machine._**hôte :** ftpperso.free.fr **login :** icnflandres **mdp :** flandresicn
**Dossier : ** icn-2018-2nde/module2/
Comment utiliser FileZilla ? [Ici](http://www.youtube.com/watch?v=NI_j1SVedG8)
 Tester les pages [ en ligne.](http://icnflandres.free.fr/icn-2017-2nde/)
Si vos fichiers sont déposés au bon endroit et nommés correctement les liens de la page précédente doivent fonctionner.
 Tous les fichiers sont déposés sur google drive dans le sous-dossier de votre dossier ICN intitulé “module2” partagé avec le camarade. Si les partages sont réalisés correctement, je devrais aussi y avoir accès.
 Aider les autres groupes dans leur travail
 Poursuivre le tutoriel openclassrooms : [css](http://openclassrooms.com/courses/apprenez-a-creer-votre-site-web-avec-html5-et-css3/mettre-en-place-le-css)




# Deuxième partie :




## Objectifs de ce module : écrire le fichier de style associé à votre première page.






Pré-requis On suppose qu'ont été vues les notions de :



 tutoriel openclassrooms : [partie 2 : CSS](http://openclassrooms.com/courses/apprenez-a-creer-votre-site-web-avec-html5-et-css3/comment-fait-on-pour-creer-des-sites-web)

Notions abordées



 mise en page avec css






## activités en classe :


Les groupes sont identiques à ceux du module précédent.
Chaque groupe récupère les fichiers html et les images associées crées lors du dernier module.



 Créer un fichier act1_a.css (décliner en act1_b.css etc.) et l’ouvrir dans notepad++
 Appeler le fichier de style dans le fichier html : act1_a.html crée précédemment.
 Dans votre fichier de style, ajouter les styles suivants :
_Tous les changements de style doivent se faire uniquement en manipulant le CSS, le code HTML ne doit pas changer !_

 	    1. h1 : rouge très foncé, taille triple de la normale, souligné, police arial, centré
 	    2. h2 : rouge plus clair, taille 1.5x la normale, gras, police arial, aligné à gauche
 	    3. p : noire, taille normale, corps de police normal, police verdana, aligné à gauche.
 	    4. liens : en vert
 	    5. la couleur du fond : gris très clair
 	    6. Dans chaque paragraphe, un mot sera surligné dans la couleur de votre choix
 	    7. Positionner les 4 images ainsi : la première flotte à gauche, la deuxième flotte à droite, la troisième est en dessous du texte et la 4ème au dessus.
 	    8. Redimensionner les images pour qu’elles occupent toutes environ la même surface


 Comme la dernière fois, tester localement toutes les propriétés introduites.
 Le fichier et les images associées sont déposés sur le serveur ftp de free dans le même dossier que votre fichier. Même remarque que précédemment, il est possible que l'accès au FTP de free soit bloqué, je proposerai une solution locale.
 Tester les ajouts online.
 Tous les fichiers sont déposés et partagés sur google drive dans le dossier “module 2” crée lors de l’activité précédente.
 Aider les autres groupes dans leur travail
 Tutoriel openclassrooms : css, partie 3 : structure



# Troisème partie :




## Objectifs de ce module : écrire la structure de votre page.






Pré-requis On suppose qu'ont été vues les notions de :

 	    * tutoriel openclassrooms : [partie 3 : Structure](http://openclassrooms.com/courses/apprenez-a-creer-votre-site-web-avec-html5-et-css3/comment-fait-on-pour-creer-des-sites-web)

Notions abordées

 	    * Structurer une page avec css






## activités en classe :


Les groupes sont identiques à ceux du module précédent.

Arrivé ici, vous devriez avoir compris que vous êtes en train de réaliser le site qui servira de vitrine à la classe.
Vous remarquerez que l'accueil est un peu tristounet. Cette partie a pour objectif de révéler vos talents créatifs.

L’entête sera évaluée selon 2 critères : qualité esthétique, qualité du code.
**C'est un travail sérieux qui va demander un peu plus de temps ; voilà pourquoi vous aurez environ 2 semaines pour le terminer chez vous.**



**les entêtes doivent comporter :**

 	    * le logo du Lycée des Flandres (à vous de le récupérer)
 	    * Une description de l’enseignement. Hors de question d’y citer mon nom.
 	    * Une image de fond occupant toute la largeur dont le choix est laissé libre (pitrerie = armageddon)
 	    * 2 couleurs dominantes (fond et titres) assez contrastées pour du texte.
 	    * Tout autre élément laissé à la liberté du groupe (dois-je me répéter concernant les pitreries ?)
 	    * Vous adapterez le CSS de la page elle-même pour faire apparaître une couleur de fond en lien avec l'image choisie plus haut.
 	    * Vous adapterez aussi les titres, sous-titres et les paragraphes (balise p) du fichier de style à votre convenance.

**Contrairement à ce que vous avez fait jusqu'ici, vous n'uploaderez pas directement vos travaux (votre fichier de style et vos images).
Elles seront seulement déposées sur le drive et testée localement. Les procédures sont les mêmes que précédemment.**
La version en ligne doit donc rester la même que lors de la précédente partie.
