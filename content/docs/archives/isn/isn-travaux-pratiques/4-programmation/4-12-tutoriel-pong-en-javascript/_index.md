---
author: qu3nt1n
date: 2016-07-01 12:34:25+00:00
draft: false
title: 4.12 Tutoriel pong en javascript
weight: 12

---



[![pong](/uploads/uploads/2016/07/pong.gif)
](/uploads/uploads/2016/07/pong.gif)




Pré-requis  : _HTML, CSS, JavaScript._

Notions abordées : _canvas, __boucle de rafraîchissement, __événements clavier, __déplacement__ d'un objet, collisions simples_







# Tutoriel : création du jeu Pong en html5 avec la balise canvas.




Durant tout le tutoriel, construire le code étape par étape. Il doit fonctionner à chaque étape intermédiaire et être régulièrement partagé avec votre enseignant via les procédés habituels (google drive). Cela peut sembler très long mais tout est décrit en détail.




### Pong


![](http://amigamuseum.emu-france.info/Fichiers/Biographie/images/pong/pong.gif)
Jeu historique où deux joueurs déplacent chacun une raquette permettant de faire rebondir une balle.
Si celle-ci parvient derrière une raquette, l'adversaire marque un point. La balle rebondit au sol et au plafond.
Contrainte supplémentaire : frapper la balle loin du centre de la raquette lui donne de l'effet

Jeu a deux joueur utilisant le clavier (Z et S pour le joueur 1, haut et bas pour le joueur 2).

Il sera donc réalisé dans une page html, elle même contenant un script javascript s'affichant dans une  balise canvas.


## Cahier des charges


Nous allons réaliser ensemble ce jeu afin de vous familiariser à canvas. L'idée ici n'est pas d'illustrer les propriétés graphiques de canvas mais plutôt de vous montrer comment créer très rapidement (2h) un jeu vidéo "jouable" (sa jouabilité est lamentable - remarquons le).



* Créer une page html contenant un canvas
* Créer la boucle de rafraîchissement
* Dessiner un rectangle donné par 4 sommets
* Evénements clavier : déplacer la raquette en question
* Les raquettes : dessin et animation
* La balle : une animation simple mais des contraintes multiples
* Rebonds, but : c'est gagné !



## Description pas à pas des éléments du code




### Elements généraux


On commence par créer un fichier html avec les balises usuelles.


~~~html
    <html>
    <head>
    	<title>Pong</title>
    	</head>
    <body>
    	<h1 id="titre">Pong</h1>

    </body>
    </html>
~~~



Ajouter les balises manquantes au début du fichier (doctype, meta etc.).


Dans le body on insère le canvas qui va dessiner le jeu ainsi qu'un message d'erreur permettant de comprendre ce qui se passe si rien n'arrive à l'écran.

~~~javascript
<div id='conteneur'>
	<canvas id="canvasElem" width="600" height="600">
		Canvas failed
	</canvas>
</div>
~~~

`<Canvas>` (Cannevas, en anglais...) est une balise html5 permettant de représenter une figure 2d ou 3d et de l'animer en javascript.

En 2D on dispose d'un repère orthonormé usuel en informatique. L'**origine en haut à gauche**, les x vers la droite et les y **vers le bas**.
Sa taille sera ici de 600x600 pixels.


Le contenu html ne changera plus et tout ce que nous allons ajouter sera dans le script. En utilisant les propriétés css, mettre un fond noir à la page, centrer le canvas à l'aide de son id et choisir une police et une taille de caractères pour le h1




## Le script et les premiers éléments graphiques


A l'aide d'un script on va utiliser les fonctions javascript associées à la balise canvas pour dessiner des objets.

** L'animation** est ensuite rendue possible en nettoyant le canvas et dessinant régulièrement les éléments à l'écran à la manière d'un dessin-animé.


### Récupération du canvas, écoute des événements, boucle de rafraichissement


Le principe est le suivant :
Une fois la page chargée par le navigateur, javascript execute à intervalle régulier la même fonction (la boucle de rafraichissement). Celle-ci dessine tous les éléments présents, calcule les états etc.

Avant d'insérer la boucle de rafraichissement il faut s'assurer que canvas est bien pris en charge par le navigateur.

On insère donc un "ecouteur d'événements" (window.addEventListener). Celui-ci servira tout d'abord à s'assurer que la page est bien chargée avant de lancer le canvas.

Il servira ensuite à détecter les pressions du clavier servant à animer les raquettes.

On insère dans le "head" le script suivant
**Une fois compris** il peut être repris pour n'importe quel jeu (ou animation) simple en 2D, la structure sera vraisemblablement la même.

~~~html
<script type="text/javascript">
		//à chaque reload
		window.addEventListener('load', function () {
		  // On récupère l'objet canvas
		  var elem = document.getElementById('canvasElem');
		  if (!elem || !elem.getContext) {
			return;
		  }
		  // On récupère le contexte 2D
		  context = elem.getContext('2d');
		  if (!context) {
			return;
		  }
		  // Boucle de rafraichissement du contexte 2D
		  boucleJeu = setInterval(refreshGame, intervalTemps); //refresh tous les x ms
		}, false);

		//variables
		intervalTemps = 2;//tous les 2 ms

		//boucle de rafraichissement
		//la boucle du jeu
				function refreshGame() {
				//ici on inscrira les appels succéssifs.
				}

		//fonctions : elles seront définies ici, appelées plus haut
</script>
~~~

** Traduction :**

On commence par "écouter" les "événements" de la page. `window.addEventListener(...)` : chargement de la page, action de l'utilisateur (clavier, souris etc.)

On charge une fonction javascript executée une seule fois (inutile donc de la nommer) **après** le reste du code html (load, ligne 3).

Celle-ci va s'arrêter si le code html ne contient aucun élément dont l'id est 'canvasElem'
`(if !elem){return;}` se traduit en : si tu ne trouves pas d'élément appelé 'canvasElem' tu sors de la fonction en ne faisant rien = tu t'arrêtes.
`return;` permet de quitter une fonction et de renvoyer ce qui est entre `return` et `;`. Ici : rien.
Elle s'arrêtera alors et on verra à l'écran "Canvas Failed" indiquant au programmeur d'où vient le problème.

Par exemple : `return 3;` aurait renvoyé la valeur 3 comme résultat, ce qui n'aurait aucun sens.

Si tout s'est bien passé jusque là (ça sera le cas !) on nomme `context` le canvas. (`context = elem.getContext('2d')`) dont le nom complet est : `document.getElementById('canvasElem').getContext('2d')` = le contexte 2d de l'élément canvasElem du document...

Ce nom étant bien trop pénible à employer, on l'a donc raccourci en `context`. C'est un nom assez usuel pour cet objet.

Chaque fois qu'on voudra dessiner dans le canvas ou y écrire du texte on utilisera cet objet. `context` comme on va rapidement le voir.


`context` n'est pas une variable mais un **objet**. Disons simplement qu'on traite context comme vous traiteriez une Ferrari durant un essai de 15 minutes : telle pédale fait ceci, tel bouton fait celà. On ne sait pas très bien de quoi c'est fait, ce n'est pas grave ; on fait confiance aux auteurs. Tant qu'on respecte les consignes, ça marche...


Toujours dans cet appel de fonction, on lance une autre fonction appelée `refreshGame`. Elle est définie plus bas et ne contient rien pour l'instant.

La syntaxe : `setInterval(refreshGame, intervalTemps)` permet de lancer cette fonction tous les 2 milisecondes. 2 ms parce que cette valeur rend le jeu très fluide. La valeur 2 est définie par `intervalTemps = 2;` définie plus bas.

OUF ! Vous êtes arrivés jusqu'ici... Rassurez-vous, ainsi que je l'ai dit plus haut, vous n'aurez pas besoin d'être capable de taper tout ça de mémoire, simplement comprendre les éléments principaux :



* Une fonction lance le canvas s'il est correctement défini
* Celui-ci est appelé à l'aide de la variable qu'on a appelé context
* Cette même fonction lance une autre fonction (vide...) qui servira à dessiner, animer, interpréter les événements (pression du clavier, clic souris etc.).

Aussi surprenant que cela puisse paraître, c'est le squelette de n'importe quel jeux vidéo 2d qui se déroule dans une seule fenêtre. Tout ce dont on a besoin y figure déjà !


## Variables et éléments initiaux


Le jeu est assez simple pour l'envisager intégralement dès le départ.

On se contentera à chaque rafraichissement de :



* Vider la fenêtre (sinon elle se remplit au fur et à mesure).
* Dessiner deux barres rectangulaires pour les raquettes.
* Dessiner la balle carré.
* Dessiner un filet constitué de rectangles.
* Détecter les collisions de la balle avec les objets (plafonds, buts, raquettes)
* Repérer si un des joueurs a pressé une touche.
* Calculer les positions futures des objets mobiles.
* Ecrire les deux scores

Quelles sont les variables dont on a besoin ?

* les dimensions du canvas, toujours utile pour se repérer
* les dimensions des raquettes, de la balle
* la position de chacun de ces objets
* les scores
* les "vitesses" de la balle, des raquettes

**Remarque importante concernant la vitesse**. Chaque déplacement se fait via un rafraichissement de l'écran. Toutes les positions sont donc calculées étape par étape. La vitesse de la balle est donc le nombre de pixels dont elle se déplace en abscisses, en ordonnées, entre deux rafraichissement.


### Comment déterminer les variables et leurs valeurs ?


En commençant le projet je ne savais pas quelle taille donner aux éléments. J'ai donc choisi des valeurs à tâtons.

Avant de progresser il faut reflechir aux collisions. Les objets étant tous des rectangles verticaux on va simplement résoudre des inéquations très simples... mais pénibles à écrire.


**Remarque :** une autre méthode est possible pour les collisions. Elle consiste à utiliser l'ordre dans lequel on dessine les éléments pour repérer si un pixel de la balle est dessiné sur un pixel d'une couleur particulière. Les collisions sont généralement des problèmes difficiles... Elles sont souvent résolues en entourant les objets de forme complexe d'une boite rectangulaire : c'est la "hit box" bien connue des joueurs de FPS... et on en revient à des inéquations à résoudre.


Il sera plus simple de traiter les collisions de la balle (=résoudre des inéquations) en utilisant le centre de chaque objet pour le repérer. Si la raquette fait 100 pixels de haut, son centre est à 50 en ordonnées du bord supérieur, 50 en ordonnées du bord inférieur.

Cette décision étant prise, les variables peuvent toutes être définies.

A nouveau, les valeurs retenues ont été obtenues en bidouillant, elles n'ont rien de particulier si ce n'est de rendre l'affichage "présentable".

Ce choix pose un autre problème (on n'a rien sans rien), canvas dessine les objets rectangulaires en partant de leur coin supérieur gauche...

Afin d'illustrer une méthode plus générale que celle du rectangle, on utilise ici le dessin d'un polygone qui sera rempli par une couleur. Il est défini par ses sommets et se remplit à l'aide d'une fonction.


Question niveau maternelle : si les coordonnées du centre d'un rectangle dont les côtés sont parallèles aux axes sont x et y, si l est sa demi-largeur et h sa demi-hauteur, quelles sont les coordonnées des quatre coins ?
Faire une figure en se souvenant que les ordonnées sont vers le bas.
Prendre une photo, l'insérer dans le drive au bon endroit et la renommer pour le dossier projet.




## Et maintenant les variables en elle même :


Elles iront en haut du script, avant la récupération du canvas. Elles sont toutes locales, certaines étant juste nommées sans valeur particulière à ce moment.

~~~javascript
//variables internes
var boucleJeu; //appelée pour refresh
var intervalTemps = 2; //temps entre 2 refresh en ms
var context; //le contexte 2d

// Constantes du jeu
var largeur_fenetre = 600; //taille du canvas
var hauteur_fenetre = 600; //hauteur du canvas
var avancer = 1; //on commence a gauche, en allant vers la droite

//positions des objets
//centre de la raquette de gauche
var abs_raquette1=60;
var ord_raquette1=300;
//centre de la raquette de droite
var abs_raquette2=540;
var ord_raquette2=300;
var barreStart=ord_raquette1; //l'ordonnee des barres apres les buts
//centre de la balle carre
var abs_balle=300;
var ord_balle=300;
var abs_depart=abs_balle;//on gare en mémoire la position initiale pour les remises en jeu
var ord_depart=ord_balle;
//largeur et hauteur des barres - ce sont en fait des demi-largeurs et hauteurs, comme on va le voir
var l=3;
var h=60;
//largeur et hauteur de la balle
var ll=6;
var hh=6;
//vitesse de deplacement des raquettes
var deplace = 18;
//vitesse horizontale et verticale de la balle
var horiz = 2;
var vertic = 0;
//les scores
var score1=0;
var score2=0;
~~~



Les noms ne sont pas clairs ! Ils ne le sont jamais, voilà pourquoi il faut ajouter des commentaires immédiatement afin de pouvoir relire son code.




Représenter l'ensemble de la fenêtre sur une autre figure. On doit y voir tous les éléments graphiques, leurs coordonnées à partir du point qui les repère noté en employant les variables que nous venons de définir.
Même traitement que pour la figure précédente : photo, drive, la classer correctement.




## Le contenu de refreshgame


Les variables étant choisies, on peut s'attaquer à la boucle de rafraichissement.

Les raquettes, la balle, les scores sont dessinés par des appels fonctions.
Par choix on dessine d'abord tous les éléments puis on calcule les états suivants.

~~~javascript
    function refreshGame() {
    	//nettoyage de l'ecran
    	context.clearRect(0,0,largeur_fenetre,hauteur_fenetre);

    	//dessin des éléments
    	dessinerBarre(abs_raquette1,ord_raquette1);
    	dessinerBarre(abs_raquette2,ord_raquette2);
    	dessinerBalle(abs_balle,ord_balle);

    	//deplacement des elements
       	deplaceBalle();

        //affichage des scores
        writescore(score1,1);
        writescore(score2,2);

        //ecoute des events claviers
        window.document.onkeydown = caBouge;
    }
~~~

Chacune des nouvelles fonctions doit être définie, on les laissera vide `function dessinerBarre(){}`, en dessous de ` refreshGame(){..}`. On ajoutera ensuite leurs actions entre les `{}` et leurs paramètres entre les `()`.

Commençons par décrire `context.clearRect(0,0,largeur_fenetre,hauteur_fenetre);` : dans le `context` (vous vous souvenez !?) execute `clearRect` (nettoyer le rectangle = effacer) en partant de (0,0) avec comme largeur et hauteur les deux autres paramètres.

Les suivantes sont assez évidentes. Remarquons simplement que certaines fonctions ont besoin de plusieurs paramètres et d'autres d'aucun. Cela dépend principalement du rôle qu'on leur donne : si elle ne servent qu'une fois, inutile de leur donner des paramètres. Remarquons aussi que `clearRect()` est une fonction qui existe déjà, tandis que `dessinerBalle()` est l'invention de votre professeur. Je vous laisse deviner laquelle est la mieux foutue...


D'autres événements que le clavier peuvent être écoutés... par exemple ceux relatifs au touchscreen pour les versions mobile. Ce Pong est certainement injouable sur mobile, mais certains jeux supportent très bien les deux versions.


Enfin, la dernière ligne est particulière : `window.document.onkeydown = caBouge;`. Si le focus est dans la fenêtre (la souris) et qu'une touche est enfoncée (on pouvait préciser `onkeyup` pour "relachée") alors execute la fonction `caBouge()`. Encore une fonction à définir.


Créer toutes les fonctions dont on va avoir besoin. Elles sont vides pour l'instant. Votre page doit se charger, afficher un canvas vide et aucun message d'erreur n'apparait dans la console.




La console (touche F12 dans chrome ou firefox, menu "console") vous affichera toutes les erreurs de syntaxe du code javascript et vous pouvez y faire apparaître des messages invisibles à l'utilisateur. Essayez d'ajouter `console.log("Where is brian ?")` dans la fonction `writescore()`.
A chaque boucle de rafraichissement, 2 messages sont affichés... Pourquoi ?
On découvrira bientôt un autre outil commode du panneau de développeurs.




## Dessin des raquettes


Ainsi qu'il a été dit plus haut il existe une méthode plus simple. Elle ne permet de dessiner que des rectangles (très similaire à clearRect). J'illustre ici un principe plus général.
Une seule fonction, appelée avec des variables différentes permet de dessiner les deux raquettes.


~~~javascript
//dessin de la balle, centree
function dessinerBalle(x,y){
	context.fillStyle = 'black';
	context.beginPath();
	context.moveTo(x-ll,y+hh); //bas gauche
	context.lineTo(x+ll, y+hh); //bas droite
	context.lineTo(x+ll, y-hh); //haut droit
	context.lineTo(x-ll, y-hh); //haut gauche
	context.closePath();
	context.fill();

}
~~~


Il faut d'abord choisir une couleur de remplissage: `context.fillStyle = 'black';`, sinon la précédente couleur sera utilisée. Sans problème ici, cela peut vite le devenir si vous avez plus de deux couleurs à l'écran...
On indique ensuite où placer le premier point `context.moveTo(x-ll,y+hh);`. On partira ici du coin inférieur gauche de la raquette. Puis :


~~~javascript
context.lineTo(x+ll, y+hh); //bas droite
context.lineTo(x+ll, y-hh); //haut droit
context.lineTo(x-ll, y-hh); //haut gauche
~~~


permet de tracer les côtés. Enfin


~~~javascript
context.closePath();
context.fill();
~~~

pour terminer la construction et la remplir. L'oubli de ` closePath()` est une source d'erreur majeure dont j'ai régulièrement fait les frais...


Ajouter cette fonction et tester votre script. Deux raquettes immobiles doivent apparaître.
C'est l'occasion de tester le menu "Sources" du panneau de développeurs (F12).
Double cliquez sur votre fichier html dans les sources (son code apparait à droite). Parmi tout ce qu'il est possible d'y faire retenons deux choses :



* L'édition en direct. Aucune modification n'est sauvegardée dans votre fichier réel, seulement dans le navigateur. On s'en servira peu, vos programmes restant assez courts.
* L'ajout d'un **breakpoint** : cliquez sur le **numero** de la ligne de l'appel à la fonction `dessinerBarre()` dans le panneau de développeur. Votre script s'arrête de s'executer au moment de l'appel de cette fonction.
Vous pouvez reprendre son execution en appuyant sur le bouton **pause** (triangle bleu, plus bas, à gauche) jusqu'au prochain appel de cette fonction.
En recliquant sur ce numero de ligne, vous enlevez ce breakpoint.

Après avoir ajouté un breakpoint à chaque appel de dessinerBarre et de dessinerBalle dans refreshGame, faites tourner pas à pas votre script en appuyant sur pause. Le navigateur vous affiche alors des informations supplémentaires (valeurs des variables définies juste avant, juste après etc.) et vous devriez voir apparaître une raquette puis l'autre et le canvas se vider. etc.
Voici, dans les grandes lignes, comment vous debugguerez vos programmes à l'avenir. Ces outils sont considérés par les webdeveloppeurs comme la révolution des années 2000.






Créer la fonction qui dessine la balle : dessinerBalle(x,y){...} en adaptant la précédente.




## Déplacement des raquettes


La dernière ligne de ` refreshGame() ` écoute les événements du clavier. Selon la touche pressée (z,s, haut et bas) la première ou la seconde raquette va bouger vers le haut ou vers le bas.

~~~javascript
function caBouge(e){
	//raquette de droite
	// Flêche du bas pressee
	if (e.keyCode == 38) {
		console.log("haut");
		if ( ord_raquette2 >= h){ ord_raquette2=ord_raquette2-deplace};
	}
	// Flêche du haut préssée

	//raquette de gauche
	//touche z pressee

	// touche s pressee


}
~~~



En fait : si l'événement `e` a un keyCode (c'est alors une touche du clavier) et que cellle-ci est 38 (vers le haut)...


Le paramètre `e` de `caBouge` est donc l'événément transmis par `window.document.onkeydown = caBouge;` de `refreshGame`.
`if (e.keyCode == 38)` s'interprète comme ceci : "si la touche enfoncée a pour keyCode 38" ... Alors deux actions effectuées :
`console.log()` permet d'afficher ce qu'on veut dans la console (accessible par la touche F12). On peut donc faire apparaître des informations masquées à l'utilisateur mais très commodes au développeur.
Enfin, première collision éventuelle, celle de la raquette et du sol : `if ( ord_raquette2 >= h){ ...};`. Il est atteint si son centre (sa référence) est supérieur ou égal à la moitié de la hauteur (variable h).
Si le centre est assez haut, on peut continuer à descendre : `{ ord_raquette2=ord_raquette2-deplace};` . Sinon, presser vers le bas ne fait rien.


Ajouter cette fonction et la tester. On doit pouvoir déplacer la raquette de droite jusqu'en bas de l'écran sans qu'elle n'en sorte.






Compléter cette fonction avec les autres événements possibles : touches haut, Z et S. Déterminer d'abord les keyCode relatifs à chaque touche puis compléter la fonction précédente. On utilisera trois `else if(){}`.

S'aider de la console et des outils développeurs si nécessaire.






### Résumé de la situation


On devrait maintenant avoir une fenêtre html contenant un canvas. Celui-ci fait apparaître deux raquettes mobiles (déplacées par les touches du clavier ; elles ne peuvent pas quitter l'écran) et une balle immobile au centre de l'écran.


## Déplacement de la balle


Réalisée en plusieurs étapes, on s'en doutait un peu.


### Trajectoire initiale


la balle va d'abord simplement se déplacer de gauche à droite et sortir de l'écran.

Deux nouvelles variables entrent en jeu : `var horiz = 1; var vertic = 0;`

Ce sont les vitesses horizontales et verticales de la balle au début du jeu.

`horiz` prendra les valeurs 1 et -1 tandis que `vertic` pourra changer énormément, augmentant la difficulté.


~~~javascript
function deplaceBalle(){

//on ajoutera ici, AVANT de déplacer la balle, tous les tests à effectuer
//pour changer sa trajectoire selon sa position = rebonds, buts, effet de la raquette etc.
x2=x2+horiz
y2=y2+vertic
}
~~~


A ce moment la balle doit quitter l'écran à droite et disparaitre.


Ajouter ces éléments en l'état. Quelle est la trajectoire de la balle ? De quelles variables dépend-elle ?
Proposer des valeurs de ces variables permettant de : déplacer la balle vers le bas, vers le haut, en diagonale haut gauche, bas gauche etc. Changer l'angle de la trajectoire pour la rendre presque verticale et expliquer ce qu'il faudrait faire pour gérer les rebonds sur le plafond et le sol.
Compléter votre diagramme papier avec ces éléments (photo, drive, classée au bon endroit...).




### Rebonds verticaux


On ajoute alors les tests de collision avec le haut et le bas.

~~~javascript
function deplaceBalle(){
	//tests de collision : plafond
	if(ord_balle-hh<=0){//on est arrivé en haut
		vertic=-vertic //la balle repart vers le bas
	}
	//autres tests à effectuer
	//...

	//deplacement de la balle
	x2=x2+horiz
	y2=y2+vertic
}
~~~



Compléter votre script avec les éléments nouveaux et tester la collision en donnant aux variables évoquées dans la manip précédente des valeurs permettant à la balle d'avoir une trajectoire verticale.
On testera les deux cas (vers le haut, vers le bas). Que se passe-t-il ? Expliquer.
La balle rebondit-elle quand son centre arrive au plafond ? Expliquer. Ajouter un breakpoint à la ligne `vertic=-vertic` si nécessaire.




Décrire ligne par ligne ces ajouts et les compléter avec les rebonds sur le sol. La balle peut quitter l'écran par la gauche et la droite mais plus par le sol ou le plafond.




### But !


Les raquettes et la balle sont recentrées à chaque point. Le score du joueur qui a marqué augmente de 1.
C'est là qu'intervient `ord_depart;` où on avait gardé en mémoire la position initiale de la raquette.

~~~javascript
if(abs_balle+ll>=largeur_fenetre){//a droite. but et on repart du centre
		horiz=-horiz;
		vertic=0;
		abs_balle=abs_depart;
		ord_balle=ord_depart;
		score1++;
		ord_raquette1=barreStart;
		ord_raquette2=barreStart;
	}
~~~

Insérer dans votre code (au bon endroit...) l'extrait précédent. Le décrire (pourquoi devoir modifier horiz et vertic ?) et écrire la partie correspondant au but de gauche.


## Etat des lieux après toutes ces étapes :


La balle ne peut plus quitter l'écran... mais sa trajectoire est définie par les valeurs initiales de horiz et vertic et elle ne "touche" pas encore les raquettes...

Vous devez être capable d'expliquer chacune des instructions, de l'illustrer. Sinon reprendre.


### Collision avec les raquettes


Les raquettes font rebondir la balle (comment ?) et ajoutent un effet vertical à la balle. Plus le contact est éloigné du centre, plus il est important.
D'autres versions sont possibles, l'idée est de vous en présenter une très simple.

On va tester si 4 inéquations sont résolues en même temps ! Auquel cas la trajectoire de la balle est modifiée... Elle rebondit sur la raquette.

L'opérateur && est un "Et booleen". Si les propositions A et B sont vraies, A&&B renvoie True (ou 1 dans certains langages). Dans tous les autres cas il vaut False (ou 0).
Il est MULTIPLICATIF. On peut enchainer plusieurs propositions et si elles sont toutes vraies (et seulement dans ce cas), il vaut True.

Un autre opérateur || (Ou booleen) permet de tester si (A ou B) est vrai (c'est le cas si A est vrai ou B est vrai ou si les deux le sont en même temps). Il est ADDITIF. Il faut donc respecter les priorités opératoires quand on emploie les deux en même temps.

~~~javascript
if(
abs_balle-ll <= abs_raquette1-l && abs_balle+ll >= abs_raquette1+l
&& ord_balle+hh <= ord_raquette1+h && ord_balle-hh >= ord_raquette1-h
)
{//elle a touche la raquette de gauche
	horiz=-horiz;//rebond
	vertic = vertic + 0.05*(ord_balle - ord_raquette1);//effet
}
~~~



On a écrit les conditions sur plusieurs lignes. C'est identique mais plus lisible.




Compléter votre code avec cet extrait et l'ajouter à votre script. La balle doit rebondir sur la raquette de gauche.
Expliquer ce que fait : `+ 0.05*(ord_balle - ord_raquette1); `




Compléter ce test avec celui de l'autre raquette et l'insérer dans votre code. La balle doit ENFIN rebondir sur les deux raquettes...




Bien que ce code fonctionne un bug subsiste ! Je ne m'en suis aperçu qu'en rédigeant ce tutoriel.
Saurez-vous le débusquer et le corriger ?
Indication : ajouter un breakpoint à horiz=-horiz.


Il reste deux étapes : les scores et le filet.

On peut faire plus simple mais j'ai cherché à ne créer qu'une seule fonction :


### Les scores




~~~JavaScript
//ecrit les scores
function writescore(s,j){
	context.fillStyle = 'black'
	context.font = "30px Arial";
	context.fillText(s,ZW/2 +200*j-300,50);
	}
~~~


Il faut, à nouveau, choisir une couleur de remplissage (plus prudent), une taille et une police de caractère et indiquer où écrire le message.


Que contient la variable s qui apparait à la dernière ligne ? writescore est appelée deux fois dans refreshgame, quelles sont les valeurs de `ZW/2 +200*j-300` dans chacun des appels ?




## Compléments


Le jeu est maintenant presque terminé, ne reste que le filet à ajouter. Vous ne devriez avoir aucun mal si vous êtes parvenus jusqu'ici.

D'autres idées :



* arrêter le jeu quand un joueur arrive à 10 pts. On utilisera : `clearInterval(boucleJeu);`.
* Changer alors le titre de la fenêtre pour l'indiquer au joueur. `document.getElementById("titre").innerHTML = "Game Over"`. RQ : on peut adapter ce message : "Joueur 1 a gagné".
