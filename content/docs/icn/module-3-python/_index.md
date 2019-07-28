---
author: qu3nt1n
date: 2016-07-01 12:47:04+00:00
draft: false
title: 'module 3 : python'
weight: -7

---

# Découverte du Langage Python




## Remarque TRES IMPORTANTE.


Pendant plusieurs années la découverte de Python en ICN et ISN s'est déroulée ainsi : installation (si nécessaire), création d'un compte sur OpenClassRooms et suivi de certaines parties de leur tutoriel.

Cette méthode a fait ses preuves mais présente de nombreux désavantages. Déjà elle n'est pas très scolaire : peu d'exercices, beaucoup de lecture... et elle demande plusieurs semaines avant d'être autonome. J'ai donc décidé de chercher un meilleur cours : à la fois plus abordable pour les novices et aussi complet pour ceux qui en veulent...
Au bord du désespoir (à l'idée de devoir écrire 15 chapitres) j'ai découvert les supports de Fabrice Sincère. Ils me semblent très bons et - pour pouvoir me consacrer à autre chose - j'ai décidé de les incorporer.

Ils sont **DANS LES MENUS**, à partir de cette page.

Un autre point capital à réaliser est que Python nécessite une installation. Les logiciels installés sur les machines peuvent poser problème. D'une séance à l'autre les images peuvent être modifiées... Voilà pourquoi une certaine maîtrise de l'informatique est attendue (installation, désinstallation, navigation dans les dossiers, recherche sur internet de solutions simples etc.)


### Remarque sur les contenus.





 Comme tous les cours de programmation on suppose une certaine acquisition de l'autonomie au fur et à mesure de vos découvertes...
 Chapitres indispensables : de 0 à 4
 Chapitres indispensables pour développer de manière efficace et se lancer dans un long projet : 5 et 6
 Les chapitres 8 à 10 sont à envisager dans un contexte de projet
 Les derniers chapitres correspondent plus à une série de projets à développer dont ils posent les fondations. Le reste est à construire...






































## LES ANCIENS ENSEIGNEMENTS


Ce qui suit n'est plus d'actualité. Je l'ai laissé pour mémoire.

Pour tous les élèves commençant un enseignement après la rentrée 2018, **il faut travailler avec les supports du menu.**


#




# Première partie :




### Objectifs de cette partie : installer Python et le découvrir.






Notions abordées



 Premier programme
 découpage d'un programme en séquences
 tutoriel openclassrooms : [Python partie 1](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/qu-est-ce-que-python)







### activités en classe : Installer Python 2.7 et découvrir la programmation.


Avant de procéder à l'installation, verifier si une version de python est installée sur l’ordinateur (menu démarrer un dossier Python doit figurer quelque part.)

Si ce n'est pas le cas ou si vous n'avez pas la bonne version de Python (par exemple Python 3, qui nous posera des soucis plus tard) alors :



 	  1. la desinstaller
 	  2. Télécharger python 2.7.10 à [cette adresse](https://www.python.org/downloads/) (Windows x86 MSI installer Le deuxième bouton orange).
 	  3. Installer python 2.7.10

Sinon, vous pouvez commencer les tutoriels.
_Si vous ne pouvez pas installer python chez vous, comment faire ? Il existe des sites (comme [trinket.io](http://trinket.io/)) qui permettent de tester en ligne les programmes sans installer quoi que ce soit localement.
Problème, ils ne fonctionnent pas avec pygame (la librairie de fonctions dédiées aux jeux vidéos)._

Une fois l'installation réalisée, vos premiers pas en programmation se feront sur OpenClassrooms.

** Vous réaliserez la première partie de [ce tutoriel](http://openclassrooms.com/courses/apprenez-a-programmer-en-python).**

Remarquons qu'OpenClassrooms utilise Python 3. Certains travaux auront donc une syntaxe différente.

Autre remarque importante, la partie suivante étant un TP à réaliser en classe, je vous invite à bien vous concentrer sur le TP proposé par OpenClassrooms.



---






## Deuxième partie : un premier programme assez simple






Pré-requis On suppose qu'ont été vues les notions de :



 tutoriel openclassrooms : [Python partie 1](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/qu-est-ce-que-python)

Notions abordées



 Utilisation des fonctions de base de Python
 premiers travaux






### activités en classe : Réalisation du jeu du plus et du moins.


Le principe du jeu est de faire deviner un nombre tiré au hasard à un utilisateur en lui disant, après chacune de ses propositions s'il est trop haut ou trop bas.

**Les consignes :**
Votre programme joue contre vous.
Le programme choisit un nombre au hasard entre 1 et 1000 qu'il n'affiche pas.
Il demande à l'utilisateur de proposer une valeur.
Si elle est juste, il affiche "gagné" et le nombre de coups nécessaire.
Si elle est trop grande, il affiche : "c'est moins !"
Si elle est trop petite, il affiche : "c'est plus !"
Si l'utilisateur n'a pas gagné, il propose alors de recommencer.
Vous pouvez recommencer une partie en tapant 'o' ou vous arrêter en tapant 'n'.



**Consignes :**

Vous créerez ce programme en Python, il pourra s'exécuter en ligne de commande ou dans un fichier .py.
Une fois crée, vous le déposerez sur le drive dans votre dossier et m'enverrez un mail.
Trois critères seront pris en compte :



 Le respect des consignes énoncées plus haut.
 La qualité du code et les commentaires que vous y apporterez. J'insiste sur ce point.
 La gestion des erreurs : si l'utilisateur tape n'importe quoi, comment votre programme réagit-il ?
 Le temps qu'il vous faut pour le réaliser. Il faudra donc m'envoyer un mail signifiant la réalisation de votre programme et son dépôt sur le drive.

**Ce travail est un TP de groupe mais peut être individuel.** Son objectif est d'évaluer vos capacités, bien plus que de vous pénaliser si vous rencontrez des difficultés. Si vous êtes incapable de le réaliser, vous n'avancerez que très difficilement par la suite... Aussi n'hésitez pas à demander de l'aide.



**Quelques étapes**
Comme pour tous vos programmes futurs, vous DEVEZ commencer avec une feuille et un crayon.
Muni de vos outils, découpez votre programme en séquences. Voici un plan :



 Tirer un entier au hasard entre 1 et 10 et l'afficher.
_Durant la programmation, vous aurez besoin de connaitre le nombre choisi par la machine. Ce n'est qu'une fois terminé qu'il faut le cacher._
 Demander à l'utilisateur de proposer un nombre et afficher une réponse si celui-ci est juste.
 Réaliser les autres comparaisons (plus petit, plus grand).
 Réaliser une fonction contenant une boucle while. Celle-ci demande un nombre à l'utilisateur et l'affiche. Le critère d'arrêt de la boucle est que le nombre soit égal à une valeur prédéfinie.
 Recommencer en affichant "plus petit !", "plus grand !" selon les cas.
 Tous les éléments pour créer le jeu sont alors à votre disposition, il s'agit maintenant de les combiner.




---






## Troisième partie : les listes et tableaux avec Python






Pré-requis On suppose qu'ont été vues les notions de :



 tutoriel openclassrooms : [Python partie 1](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/qu-est-ce-que-python)
 Création d'un premier programme

Notions abordées



 Les listes, les tableaux






### activités en classe :


La consigne est de parvenir à la fin de la [ deuxième partie](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/notre-premier-objet-les-chaines-de-caracteres) du tutoriel d'OpenClassrooms AVANT le TP sur le pendu.



---



_Ici s'arrêtent les pré requis nécessaires à l'option facultative de première et terminale._



---



La poursuite de ce module vise à vous faire découvrir la conception de jeux vidéos simples avec Python. Python a bien d'autres emplois mais c'est un moyen efficace de progresser en programmation.

Retour sur OpenClassroom avec le TP sur le pendu. Il est beaucoup plus difficile que tout ce qui précède. Je vous invite à l'étudier 2 ou 3 séances si nécessaire mais surement pas plus. Signalez moi votre arrivée à cette étape et je vous transmettrai une adaptation de la solution fonctionnant en Python 2.7 si vous ne parvenez pas à le réaliser vous même.

La suite du tutoriel est très intéressante (enfin je trouve...) mais n'est absolument pas nécessaire pour que vous puissiez aborder vos premiers jeux vidéos un peu plus amusants. Nous allons donc changer de registre et aborder Pygame.




## Quatrième partie : Pygame




### Installer et découvrir Pygame, la librairie "jeux vidéos" la plus simple de Python.






Pré-requis On suppose qu'ont été vues les notions de :



 tutoriel openclassrooms : Python, les deux premières parties

Notions abordées



 Pygame




Pygame est disponible [ici.](http://www.pygame.org/download.shtml) Choisir la version correspondant à votre installation de Python : pygame-1.9.2a0.win32-py2.7.msi

Concernant votre apprentissage le tutoriel se trouve [ici.](https://openclassrooms.com/courses/interface-graphique-pygame-pour-python/presentation-de-pygame) Seule la première partie nous intéresse réellement.

Retenez que la deuxième partie aborde l'utilisation du son et l'installation d'une manette. Cela pourra nous servir pour créer une console de jeu en fin d'année.

Votre objectif est donc très simple, parvenir jusqu'au TP du tutoriel. Celui-ci est à mes yeux assez difficile mais comporte tous les éléments dont vous aurez besoin. Si vous n'y parvenez pas, la correction proposée ne fonctionne que sous Python 3. Une version pour Python 2.7 est disponible [ici](https://drive.google.com/open?id=0B4Mq2ZGzUQ3VTWctT0pTWkdEazg)



---








## Cinquième partie : premier jeu personnel avec Pygame




### Utiliser Pygame pour créer votre premier jeu vidéo.






Pré-requis On suppose qu'ont été vues les notions de :



 tutoriel openclassrooms : Python (les deux premières parties), pygame

Notions abordées



 Pygame : création d'un petit jeu-video






### Utiliser Pygame.


Voici le jeu que je vous propose de créer. Il est très simple et sans grand intérêt mais vous permettra d'apprendre les rudiments.


## Tête de pioche


Pourquoi ce nom ? Aucune idée et sans doute aucun rapport avec le jeu lui même, c'est le seul qui me soit passé par la tête...


##### Le but :


Marquer le plus de points en attrapant des bonus qui tombent de l'écran. Survivre le plus longtemps en évitant des malus qui tombent aussi de l'écran. Les seules actions sont d'aller à gauche et à droite, les bonus s'attrapent automatiquement.


##### Le joueur :


Votre personnage, Tête de pioche, est représenté par un sprite en 2D ayant 5 images. Il est tourné vers la gauche, la droite, regarde en l'air, frappe ou meurt.

Il repose au sol, sur un décor (herbe, sol martien, lune, ce qui vous chante).

Il peut se déplacer horizontalement sur cet axe, sans quitter l'écran.

Tête de pioche peut casser des briques (on les évoquera plus tard) ou mourir s'il heurte un champignon tombé du ciel.


##### **Les bonus et la mort**


Du ciel peuvent tomber 2 sortes d'objets : des briques et des champignons.

Si Tête de Pioche rencontre un champignon, il meurt.
Si Tête de Pioche rencontre une brique, il la frappe et gagne un point (aucune action n'est nécessaire).


##### **Apparition des bonus et enjeu**


Les objets (brique ou champignon) apparaissent à des positions aléatoires, en haut de l'écran. Deux objets ne peuvent apparaître en même temps, il s'écoule un temps (aléatoire) entre deux d'entre eux. Ils descendent ensuite l'écran de façon régulière. Ils disparaissent une fois arrivés en bas.

Tête de Pioche doit donc éviter les champignons, arriver jusqu'aux briques (avant qu'il ne soit trop tard).

Chaque brique cassée lui rapporte un point et chaque champignon le tue. Ce score doit apparaître à l'écran.


##### **Difficultés manifestes :**


**L'animation du personnage, des objets**

L'affichages de multiples bonus malus à l'écran et leurs animations (déplacement, contact avec le joueur, disparition).

La première étape est le personnage : On le fera se mouvoir horizontalement puis on s'assurera qu'il reste à l'écran.

On créera ensuite un objet, pouvant prendre deux sprites (bonus ou malus) et on le déplacera verticalement. Ensuite on s'assurera de sa disparition arrivé en bas de l'écran. Enfin que l'objet peut apparaître à une abscisse aléatoire.

On fera ensuite apparaître plusieurs objets à l'écran, à des intervalles réguliers. Ces objets respecteront le principe précédent. Enfin, on rendra l'intervalle entre l'apparition de deux objets aléatoire.

**Deuxième difficulté : les collisions.**

Il existe de multiples manières de gérer les collisions et pygame dispose de fonctions pour le faire. On les utilisera. Une fois les collisions détectées on se penchera sur la réaction : si c'est une brique, le personnage frappe un court instant, si c'est un champignon il meurt.

C'est l'occasion d'implémenter la fin de partie.


### Cahier des charges





 Créer les éléments premiers graphiques (joueur, bonus, malus, sol, ciel). On pourra utiliser [photofiltre](http://www.photofiltre-studio.com/pf7.htm).
 Afficher le personne sur le sol.
 Le déplacer au clavier (gauche, droite).
Tourner le personnage selon sa direction
 Afficher un bonus, le faire descendre verticalement (et disparaitre).
 Faire revenir le bonus en haut de l'écran.
 Choisir aléatoirement l'absisse du bonus quand il revient en haut de l'écran.
 Détecter la collision de Tête de Pioche et du bonus.
Il frappe alors la brique.
 Afficher un score
 Adapter ce travail au malus, choisir aléatoirement l'un ou l'autre quand l'objet arrive en bas. Gérer la défaite.
 Afficher 4 objets qui font la même chose (nature aléatoire, absisse aléatoire, descente, collision).
Le jeu est maitnenant jouable.
 L'étape suivante est la gestion d'une quantité quelconque de bonus/malus.




---








## Sixième partie : un jeu plus difficile




### Objectifs de cette partie : recréer un jeu déjà existant.






Pré-requis On suppose qu'ont été vues les notions de :



 Tête de pioche

Notions abordées



 Zigzag




_Le projet qui suit est clairement difficile pour un novice. C'est un projet de fin d'année de terminale à envisager si vous n'avez pas rencontré de difficulté jusque là et avez déjà épuisé ce que je vous ai proposé._


### Zigzag.


 ![zigzag](http://qkzk.xyz/wp-content/uploads/2016/07/zigzag-168x300.jpg)


L'objectif de ce projet est de réaliser le jeu complet en Python.
Essentiellement, le moteur du jeu crée une cellule (un losange) en haut de l'écran, partageant un bord avec la dernière cellule crée et fait défiler vers le bas l'ensemble. Cet ensemble crée l'impression de continuité. La bille se déplace horizontalement à vitesse constante et change de direction quand on agit (pression sur l'écran ou une touche du clavier). Chaque action rapporte un point (les bonus 2 points). Le joueur perd dès que la bille n'est plus sur une cellule.




Le jeu est considéré comme "jouable" dès que la défaite (chute de la bille) est correctement gérée et qu'on voit le score.







On créera dans cet ordre les éléments :



 une cellule
 le déplacement de cette cellule
 un "ruban" continu de cellule - c'est clairement la première étape cruciale
 la balle et son déplacement
 la défaite (tomber) - voici la deuxième étape importante
 le score
 le rebord vertical des cellules
 les bonus (les diamants mauves)
 le changement aléatoire de couleur






### Extensions





On pourra ajouter des fonctionnalités, voici quelques suggestions (liste non limitative et non triée par difficulté) :






 meilleur score dans un cookie
 la chute des cellules parvenues en bas de l'écran
 la chute de la balle qui tombe
 les menus : pause, restart etc.
 les autres statistiques du joueur : nombre de parties, de bonus etc.
 l'effet de lumière autour de la bille (regardez bien)
 des sons
 différentes résolutions
 rendre le jeu jouable avec une manette



#### D'autres idées de jeux ?


Si Zigzag ne vous branche pas ou si vous trouvez le principe difficile, vous pouvez essayer :



 **Pong**, à deux joueurs sur le même clavier
 **Démineur, **un grand tableau, une seule action possible (cliquer sur une case)
 **Un jeu de plateformes,** déjà plus difficile. En particulier les sauts.
 **Le jeu de la vie** (de Conway). Aussi difficile à réaliser que Zigzag, assez simple en Python (on verra pourquoi) et très intéressant d'un point de vue historique.
 Et sinon ? **Mastermind**, **Le compte est bon**, **Don't click the white tile...** Ou presque n'importe quel jeu simple...

Hormis Démineur et don't click the white tile (que j'ai prévu de préparer, un jour quand je n'aurais rien à faire) tous ces projets ont déjà été réalisés par des élèves et je suis donc certain qu'ils sont tous faisables. Ils peuvent être longs et demander quelques efforts...




#### Moi les jeux ça me fait #@%$£ ! Mais alors grave.


Ah. D'accord. Alors il faut se pencher sur des applications un peu plus sérieuses.

Avec un intérêt historique ? Le jeu de la vie est un bon début... Lisez la page wikipédia vous comprendrez en quoi ce n'est pas vraiment un jeu et regardez le projet proposé aux Terminales S spécialité ISN dans le menu.

En lien avec le raspberry ? J'ai beaucoup d'idées, me contacter.

Sinon la poursuite de votre apprentissage peut s'avérer plus approfondie soit en Python, soit en découvrant un autre langage de programmation : le javascript ou pour les plus motivés le PHP. Me contacter.

Non mais c'est de programmer qui me saoule en fait monsieur ! Alors venez me voir, j'ai d'autres pistes à explorer.
