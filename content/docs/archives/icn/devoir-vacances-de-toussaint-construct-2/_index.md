---
author: qu3nt1n
date: 2016-09-25 20:07:36+00:00
draft: false
title: 'devoir : vacances de Toussaint - Construct 2'
weight: 100

---

# Créez votre propre jeu avec Construct 2





## Update : évaluation de vos jeux.


L'évaluation de vos travaux va être réalisés par les élèves eux-mêmes. Les élèves de première vont évaluer les jeux des secondes et inversement, les secondes évalueront les jeux des premières.
Les travaux devraient tous être récupérés avant la mi-novembre ce qui nous laissera 3 semaines pour les évaluer sereinement avant les vacances de Noël.
Chaque groupe (seconde, première) doit donc tester les jeux de l'autre groupe (la liste sera disponible ici sous peu) et voter pour le meilleur jeu selon 3 critères :



 La dimension artistique
 L'interactivité et la jouabilité
 L'originalité



###




## Introduction


Avant de vous lancer réellement dans la programmation vous allez découvrir qu'il est tout à fait possible de créer un jeu vidéo assez élaboré sans coder quoi que ce soit...

L'outil que vous allez employer est **Construct 2**. C'est un logiciel windows qui permet de créer rapidement un jeu vidéo 2D. Très pratique, il suffit d'une demi-heure environ pour disposer d'une version jouable !

Construct 2 permet d'exporter les jeux html5 (jouable directement dans le navigateur) ou sur la majorité des plateformes actuelles.

Vous pouvez télécharger Construct 2 à [cette adresse](https://www.scirra.com/) et tester, pendant le téléchargement, le résultat du premier tutoriel que vous allez suivre [ici](http://icnflandres.free.fr/c2/tuto/)

Le résultat de ce tutoriel est donc un jeu de tir en 2D où vous vous déplacez à l'aide des flèches du clavier, tirez à la souris sur monstres ayant 5 points de vie. Ils vous tuent en vous touchant et apparaissent toutes les trois secondes à une position aléatoire. C'est loin d'être élaboré mais d'autres tutoriels vous emmèneront plus loin si vous le souhaitez.




##### Activité 1 : Prise en main de Construct 2


**Durant la séance.**

Téléchargez Construct 2 depuis [leur site](https://www.scirra.com/). Si cela ne fonctionne pas, je dispose du fichier d'installation sur clé (et j'envisage de l'héberger au lycée, pour éviter de saturer le réseau).

Commencez et réalisez le tutoriel en français disponible directement dans leur liste ; celui [pour les débutants](https://www.scirra.com/tutorials/37/beginners-guide-to-construct-2/fr/page-1).


##### Activité 2 : travaux de vacances.


**Chez vous. **

**Réalisez votre propre jeu. Uploadez le sur le site de l'enseignement.**

Vous allez réaliser un jeu vidéo à l'aide du logiciel Construct 2. Une fois terminé, **vous l'exporterez en HTML5** et l'uploaderez sur le site de la spécialité. Pas de panique, d'autres tutoriels sont disponibles sur le site de Construct 2 !


###### Cahier des charges.





 	  1. Date limite : séance de la rentrée dernier délais. Une fois uploadé, envoyez moi un mail avec l'adresse afin que j'examine.
 	  2. Il doit être jouable... mais si des bugs persistent, ce n'est pas grave.
 	  3. Il doit être simple (pensez pong, bomberman... pas league of legends)
 	  4. Il doit être léger (vous devrez l'uploader depuis chez vous et l'espace disque est limité sur le ftp de free)
 	  5. bonus : amusant !

**Précisions :**



 **Vous pouvez tout à fait reproduire un tutoriel déjà existant.** Dans ce cas, dîtes le moi par mail. Si vous ne le faites pas et me faites croire que c'est un travail personnel, c'est 0 si je découvre la même chose ou presque sur le net.
 **Vous devez l'uploader sur le ftp de l'enseignement** (logiciel : filezilla client, adresse : ftpperso.free.fr / login : icnflandres / mdp : flandresicn ).
Choisissez le dossier correspondant à votre enseignement (icn-2018-1ere ou icn-2018-2nde) et le sous dossier **construct2. **Créez alors un dossier selon votre nom de famille, par exemple "Obama" et déposez vos fichiers dans ce dossier.
Si vous avez exporté votre jeu en html5, il sera jouable à cette adresse : **http://icnflandres.free.fr/_icn-2017-2nde_/construct2/_obama. _**Il faut adapter le dossier selon votre classe et votre nom, bien sûr...
Si votre jeu prend beaucoup d'espace, indiquez le moi, je trouverai une solution pour l'héberger ailleurs
 **Il est possible de réaliser un travail en groupe.** 3 personnes maximum, indiquez le moi dès le début et, si possible, indiquez dans le mail qui s'est chargé de quoi, comment vous avez procédé etc.




##### Quelques remarques sur la création de jeu vidéos.


Construct 2 peut donner l'illusion qu'il est très simple de créer des jeux... N'espérez pas être capable de créer un jeu tel que le tutoriel de débutant aussi rapidement en Python ou en Javascript !

Bien que ce soit tout à fait possible et sans doute réaliste dans le cadre d'un projet, cela demanderait d'abord de maîtriser les bases de la programmation.
Tous les événements crées durant le tutoriel doivent être programmés à la main, chaque erreur de syntaxe, erreur dans l'algorithmique du programme entraînera un bug et vous n'aurez que les outils de base du développeur pour le résoudre.

Alors pourquoi Construct 2 ? Déjà pour vous le faire découvrir, j'espère que cela vous a amusé. Ensuite pour vous exposer les grands principes : la frame qui s'efface et se redessine à intervalle régulier ; les sprites, leurs actions, les conditions, les événements (clavier, souris, collisions, destruction), les variables etc.

La création des jeux en 2D repose presque toujours sur ces notions. Construct 2 permet sans doute de recréer tous les jeux 2D disponibles sur les consoles antérieures à la PlayStation 1... Mais Javascript + p5js ou Python + Pygame aussi ! Et cette fois, c'est vous qui programmerez.

**Dernière remarque** : pourquoi les créateurs de jeux-vidéo professionnels n'utilisent pas de tels outils ?
Deux choses à comprendre : **l'optimisation** et la **répartition des tâches**.
Construct2 n'est optimisé pour aucun jeu en particulier. C'est un moteur de jeu capable de les créer tous les jeux 2D... Un jeu vidéo 3D demande beaucoup plus de calculs à la machine et repose sur l'utilisation intelligente des fonctions de la carte graphique. Il faut donc déjà s'intéresser à la 3D avant d'envisager de programmer un jeu. L'équivalent de construct2 en 3D existe peut-être mais demandera une tonne d'effort supplémentaire dans sa prise en main.
Ensuite concevoir un jeu immense et disposant d'un univers artistique cohérent, d'une ou plusieurs progressions, d'une histoire, de personnages est un travail immense. Il faut donc le découper et le réaliser en équipe. Dans une équipe tous n'ont pas le même rôle. Certains écrivent un scénario, d'autres font du graphisme, les sons, les musiques... Seuls les développeurs écrivent du code. Généralement ils commencent par créer un moteur de jeu (ou s'en procurent un déjà existant et fonctionnel) et proposent à leurs collaborateurs un SDK (kit de développement logiciel) plus ou moins facile à prendre en main. Parfois leur travail est d'intégrer les créations artistiques dans le jeu. Ce travail d'équipe est à la fois difficile et coûteux. Il est donc délicat d'envisager de publier gratuitement de tels travaux.



---





### Liste des jeux réalisés cette année et les précédentes :


_Si votre jeu n'apparaît pas dans la liste assurez-vous d'avoir bien exporté en .html5 et uploadé tous les fichiers - la sauvegarde en .capx n'est pas jouable dans le navigateur. Le tutoriel de présentation vous explique la démarche à accomplir. Pensez à me signaler vos mises à jour._


#### Année scolaire 2016-2017




##### Secondes





 [Poissonnet](http://icnflandres.free.fr/icn-2017-2nde/construct2/Poissonnet/) : Mario
 [Flandrinck, Poissonnet](http://icnflandres.free.fr/icn-2017-2nde/construct2/Flandrinck/) : Tower Defense
 [Adorni](http://icnflandres.free.fr/icn-2017-2nde/construct2/Adorni/index.html) : Reprise du tuto (_pour tester les différents niveaux sans avoir a les finir : __1,2,3,4,5,6 du pavé numérique __et la touche " * " pour obtenir une arme plus puissante pour passer les niveaux difficiles._)
 [Duchateau](http://icnflandres.free.fr/icn-2017-2nde/construct2/Duchateau/) : Shoot'Em Up
 [Vanhaecke](http://icnflandres.free.fr/icn-2017-2nde/construct2/Vanhaecke/) : Alien Warrior



##### premieres





 [Carpentier](http://icnflandres.free.fr/icn-2017-1ere/construct2/Carpentier/1S1_Carpentier_Elie/index.html) : space invaders
 [Baranek](http://icnflandres.free.fr/icn-2017-1ere/construct2/baranek-domino-jaune/) : domino jaune
 [Seynave & Gregoire](http://icnflandres.free.fr/icn-2017-1ere/construct2/SEYNAVE_GREGOIRE/) : jeu mystère
 [Lefevre](http://icnflandres.free.fr/icn-2017-1ere/construct2/lefevre/) : flappy blue

_Merci à mon collègue M. Le Gallou de m'avoir fait découvrir Construct2 !_
