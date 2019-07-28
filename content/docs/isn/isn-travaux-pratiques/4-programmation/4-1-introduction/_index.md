---
author: qu3nt1n
date: 2016-07-02 08:27:54+00:00
draft: false
title: 4.01 Introduction
weight: 1
---



Pré-requis On suppose qu'ont été vues les notions de :



 	  * **logiciel/programme** : navigateur,
traitement de textes, tableur, etc.
 	  * **langage**  : HTML, CSS. Donc
les notions de _vocabulaire_ : _syntaxe_, _sémantique_ (interprétation par
navigateur) ont été abordées.

Notions abordées



 	  * la notion de variable
 	  * traitement de données







# Programmation




Nous allons commencer l'apprentissage de la programmation. Il va
falloir faire preuve d'un peu de patience avant d'être en mesure de
programmer des traitements "un peu complexe". La présentation et
surtout la compréhension d'un
certains de concepts de base, universels en programmation, est
indispensable afin de pouvoir progresser. Vous avez mis plusieurs
années à apprendre à lire, à compter, à parler Anglais, vous pouvez
bien admettre qu'il faut quelques semaines pour faire ses premiers pas
dans la programmation. Il faut aussi accepter qu'il ne sera pas
possible cette année d'aborder tout ce que la programmation propose.




La programmation est le processus dont le résultat est la production
d'un programme informatique.

Un tel programme est écrit dans un langage de programmation. Il existe
de **très** (!) nombreux langages informatiques. Pour s'en
convaincre on peut examiner
cette [liste](http://fr.wikipedia.org/wiki/Liste_des_langages_de_programmation).
Ils différent par leurs vocabulaires et leurs syntaxes. Il existe
également différents styles (on parle de _paradigmes_) de
programmation et en fonction du programme à écrire tel ou tel langage
peut s'avérer plus approprié.

Programmer consiste à écrire dans un langage informatique un code
réalisant un **traitement de données**. On utilise pour cela
des **instructions** écrites dans un langage de programmation
pour à partir du vocabulaire et en respectant la syntaxe de ce
langage. Il est indispensable d'être rigoureux dans la rédaction du
texte décrivant le traitement à réaliser sous peine de n'avoir aucun
résultat ou un résultat différent de ce qui était souhaité.




Lorsque l'on souhaite réaliser un traitement, il faut respecter plusieurs phases :



 	  1. identifier, décrire précisément le traitement à réaliser, on parle de spécification
 	  2. définir les algorithmes (voir cette [définition](http://fr.wikipedia.org/wiki/Algorithme))
permettant d'accomplir ce traitement puis en réaliser
le codage et documenter ce codage (ou documenter puis coder)
 	  3. tester la réalisation, il s'agit d'une phase indispensable
et primordiale




On représente souvent un programme comme un processus exploitant
des données fournies en **entrée** et produisant un résultat
(en "**sortie**").

Le plus souvent le résultat (en sortie) dépend de la
valeur des données (en entrée). Ces données et résultat peuvent être de
différentes natures : des nombres, des caractères ou chaines de caractères, des images,
etc. On parle de types des données.

Le type d'une donnée définit les opérations possibles sur cette
donnée :



 	  * on peut additionner 2 données de type numérique. exemple
 	  * on peut calculer la longueur d'un texte. [exemple](http://qkzk.xyz/docs/doc04/exemples/exemple_longueurChaine.html)
 	  * on peut modifier la taille d'affichage d'une image. [exemple](http://qkzk.xyz/docs/doc04/exemples/exemple_changeTailleImage.html)



# Premiers exemples




## Tableur


Un tableur constitue un environnement dans lequel des traitements
peuvent être réalisés en écrivant des formules de calcul dans un
langage défini.


Ouvrez une feuille de calcul dans libreoffice et dans la cellule A1
saisissez le code de traitement ` = 12+20`. Dans la cellule
on visualise alors le résultat de la réalisation du traitement en
"sortie" (ici 32).


L'intérêt de cette manière d'opérer est que l'on laisse le langage
(ici celui de libreoffice) faire le calcul (le traitement) à notre
place (même s'il était trivial ici). Les programmes sont là pour
cela : réaliser de manière automatique des traitements plus ou
moins complexes.

Pour obtenir un nouveau calcul on doit néanmoins modifier le code
saisi dans la cellule A1.

On aurait cependant pu opérer différemment et placer un nombre dans la case A1, par
exemple `12`, un autre dans la case A2, par
exemple `20` et obtenir le résultat de leur somme dans la case A3 en y
inscrivant le code du traitement à réaliser cette fois sous la forme : `=
A1+A2`.


Ouvrez une nouvelle feuille de calcul (en utilisant le second onglet
par exemple) et réalisez ces manipulations.


L'intérêt de cette seconde manière d'opérer est évidemment qu'une modification de la
valeur saisie dans A1, par exemple `22`, a une répercussion
immédiate sur la case A3 avec la mise à jour de la valeur.


Modifiez la valeur saisie dans la case A1.


Ce résultat n'a pu être rendu possible que parce que le traitement
codé dans la cellule A3 n'utilise pas directement les données
effectives du calcul à réaliser, ici 12 et 20 initialement, mais
utilisent des références,
ou adresses, vers ces valeurs, ici les
références des cellules A1 et A2. Une modification de la valeur dans
A1 ne modifie pas la validité du traitement à réaliser qui est inscrit
dans A3.

L'utilisation de ces références est cependant **fragile**. En
effet si la structure de la feuille de calcul est modifiée, cela
peut entrainer une modification des références/adresses des valeurs
et donc une corruption de la formule du traitement.






 	  1. Insérez une nouvelle colonne avant la colonne A (il faut cliquer sur
le _A_ en entête de colone, cliquez droit puis
choisir _Insérer une colonne_).
 	  2. Quelles sont les nouvelles références de nos valeurs ?
 	  3. Qu'est devenu la formule de traitement ?




Nous avons "de la chance" car le logiciel de tableur gère la
cohérence des formules lors des modifications des références comme
cela a été le cas ici avec l'insertion d'une colonne. Le traitement
réalisé dans la case d'adresse `B3` a été modifié
en `=B1+B2`. Cependant on constate qu'il ne correspond
plus à la formule que nous avions initialement
prévue : `=A1+A2`.

Il est possible d'opérer différemment et d'obtenir une formule de
traitement **robuste**. Pour cela il
faut nommer les données. Ainsi si
nous appelons `points` la première valeur
(`10`) et `bonus` la seconde
(`12`). La formule de traitement devient
alors `=points+bonus`. On peut remarquer qu'elle ne
dépend plus des références mais uniquement des noms. Testons cette version :

![zone nommage de donnée dans libreOffice](http://qkzk.xyz/docs/doc04/doc/zoneNommageTableur.png)







 	  1. Ouvrez une feuille de calcul et placez la valeur `10`
dans la case `A1` et `12` dans la
case `A2`.
 	  2. Pour nommer une valeur, il faut sélectionner la case,
`A1` par exemple, puis allez dans la _zone des noms_
en haut à gauche et y saisir le nom que l'on souhaite attribuer à la
donnée, `points` par exemple.
 	  3. Recommencez avec la donnée en `A2` en
l'appelant `bonus`, puis indiquez la formule de traitement
voulu `=points+bonus` en `A3`.
 	  4. Insérez une nouvelle colonne avant la colonne _A_.
 	  5. Que devient la formule dans la cellule `B3` ?
 	  6. Insérez cette formule dans une autre case, `F10` par
exemple, elle est encore valide.




Les valeurs à utiliser ont
été **nommées** et le calcul est exprimé de
manière **abstraite** à partir de ces noms : `=
points+bonus`. A la différence dans la toute première situation, le
traitement utilisé explicitement les valeurs **concrètes** du
calcul, il était alors nécessaire de modifier le code du traitement
pour obtenir un nouveau calcul. De plus l'utilisation de noms a pu
ajouter une relative sémantique aux données grâce au choix des noms,
il semblerait que le traitement réalisé ic additionne un nombre de points et un bonus.


Ce principe de nommage de données puis d'écriture d'un traitement
"abstrait" utilisant les noms de ces données est central en programmation.




## Traitement de textes


Nous allons voir une autre situation dans laquelle le nommage de
données et un traitement sur ces données, bien que simple, s'avère
utile.

Le scénario que nous considérons est le suivant. Pour une kermesse
d'école nous souhaitons créer des billets pour une tombola. Sur ces
billets apparaissent les informations suivantes :



 	  * le numéro du billet
 	  * la description du gros lot
 	  * la date du tirage



Ouvrez le traitement de texte de libreoffice et créez, rapidement, le
billet numéro 1 pour cette tombola dont le tirage se déroulera le 16
juin 2012 et dont le gros lot est une console
PS3. [exemple de billet](http://qkzk.xyz/docs/doc04/doc/billet-tombola1.odt)


On souhaite éditer 1000 billets pour cette tombola. Comment
feriez-vous ? Comment faire pour ne pas saisir "à la main" les 1000
numéros ?

D'autre part, cette tombola ce déroule chaque année mais la date de
tirage et le gros lot change chaque année. Comment faire pour ne
pas modifier "à la main" les 1000 billets ?

A nouveau la solution-réponse à toutes ces questions passe par la définition de données, leur
nommage et le codage d'un traitement.

Dans notre situation on peut identifier 3 données : le numéro du
billet, la date de tirage et la description du gros lot. La première
est une donnée numérique, les 2 autres sont des données
textuelles. Donnons un nom à ces données, il ne s'agit pas d'être
original mais au contraire explicite. Dans la mesure du possible les
noms choisis pour nommer une donnée doivent aider à cerner au mieux
le rôle de cette donnée. Nous les appelerons donc respectivement :



 	  * `numero`
 	  * `grosLot`
 	  * `dateTirage`

Nous allons maintenant définir dans le traitement de texte de
libreoffice des données avec ces noms en commençant par les 2
données textuelles.






 	  1. Placez-vous dans le document avec le billet, tout au début par
exemple, avant le billet (passez quelques lignes pour faire de la
place). Par la suite, nous appellerons cette zone, la "zone de définition".
 	  2. Faites les actions suivantes :

 	    1. choisissez dans le menu _Insertion_ puis _Champs_ puis _Autres_ puis
onglet _Variables_.
 	    2. choisissez maintenant _Définir une variable_
 	    3. dans la zone de texte _Nom_ (en bas à gauche) indiquez le
nom de la **variable** à définir, `grosLot` par
exemple.
 	    4. indiquez dans la zone _Valeur_ la valeur de cette
donnée `une console PS3` par exemple.
 	    5. enfin dans la
zone _Format_ sélectionnez _Texte_ pour préciser le type
des données
 	    6. terminez la définition de cette variable en cliquant
surle bouton _Insérer_.



Ca y est ! Ouf ! Nous venons de définir la
variable `grosLot`. Sa valeur apparaît avec un fond gris.

Il est maintenant facile de modifier la valeur de la variable, il suffit de
double-cliquer sur la valeur puis dans la fenêtre qui apparaît
modifier la zone _Valeur_ puis _OK_. La modification est répercutée.






Définir une variable consiste à nommer une donnée. On appelle aussi
identificateur le nom de la varialbe. Une variable est donc un
couple (identificateur, valeur). La valeur d'une variable peut être modifiée.





De la même manière définissez une
variable `dateTirage` dont la valeur sera `le 16
juin 2012`.


L'utilisation d'une variable, c'est-à-dire de la **valeur liée à
l'identificateur** est plus simple.


Dans le billet
existant sélectionnez le texte correspondant au lot et
effacez-le.
A la place nous allons insérer la valeur de la
variable `grosLot`.
Pour cela, choisissez dans le
menu _Insertion_ puis _Champs_ puis _Autres_ puis
onglet _Variables_. Il faut cette fois
choisir _Afficher la variable_ et dans _Sélection_
choisir _grosLot_ puis cliquer sur le
bouton _Insérer_.
La valeur de la variable apparaît alors dans le document.




Procédez de la même manière pour utiliser la
valeur de la variable `dateTirage` dans le texte du
billet de tombola.




Maintenant modifiez la valeur de ces variables
en double-cliquant sur leur zone de définition (attention pas dans
le billet qui n'est qu'une zone d'affichage).Que remarquez-vous dans le billet ?




Sélectionnez toute la portion de texte
correspondant au billet (attention de ne pas sélectionner la zone des
définitions des variables). Copiez-la puis collez-la plusieurs fois
pour créer plusieurs billets (5 suffiront) qui auront tous pour
l'instant le numéro 1.Modifiez les valeurs des variables : le gros lot devient une
`télé LED 40"` et la date du tirage sera le `11 janvier 2013`.Que constatez-vous ?

Qu'a-t-on gagné à utiliser des variables ?






Il nous reste à gérer nos numéros de
billet. Créez une variable d'identificateur `numero` et
de valeur `1`. Attention cette fois lors de la
définition, pour le format sélectionnez _Standard_ à la place
de _Texte_ car il s'agit d'une donnée numérique.




Supprimez les 5 billets créés en surplus pour ne
garder que le premier et utilisez la variable pour afficher
le numéro du billet.(Re)Créez à nouveau 5 billets et modifiez la valeur de la
variable `numero`, à 5 par exemple.Quel est le problème  ?




Et oui, la valeur est évidemment modifiée pour tous les billets. Car
**une variable ne peut avoir qu'une seule valeur à la
fois**... Il faut donc opérer un peu différemment.

La solution est qu'il faut exécuter un traitement qui modifie la
valeur de `numero` à chaque nouveau billet (c'est-à-dire
pour nous à chaque copier-coller du billet). Le traitement que l'on
veut réaliser consiste simplement à dire qu'à chaque fois la valeur
de `numero` est augmentée de 1, sa nouvelle valeur est
donc obtenue par le traitement (la formule) `numero+1`.

Il faut mettre en place ce traitement dans le billet. Effacez
donc l'actuel affichage de la variable `numero` dans le
billet.

On va remplacer cet affichage en appliquant la procédure de définition
d'une variable, en fait il s'agit de la redéfinition de la
variable `numero` avec pour _Valeur_ la formule de
traitement `numero+1` (voir image).

![saisie formule pour numéro](http://qkzk.xyz/docs/doc04/doc/saisie_formule_numero.png)



Sélectionnez toute la portion de texte
correspondant au billet (attention à nouveau de ne pas sélectionner la zone de
définition des variables). Copiez-la puis collez-la plusieurs fois
pour créer plusieurs billets (5 ou 10 suffiront).Que constate-t-on ?On peut maintenant modifier la valeur du numéro "initial" (à 0) par
exemple et les numéros de tous les billets devrient être modifés en
conséquence... Testez !






Remarque : Il n'y a d'une manière générale et
même le plus souvent en programmation pas obligation de redéfinir
une variable pour en changer la valeur même si c'est ce que fait le
traitement de texte de libreoffice, ou du moins ce qu'il nous laisse croire
par l'utilisation de la commande _Définir une variable_


A chaque nouveau billet une nouvelle variable de
nom `numero` va être créée, sa valeur est le résultat du
traitement de `numero+1`. La valeur d'un billet est à
chaque fois déterminée par rapport à la valeur du billet précédent
d'où le résultat obtenu.


[résultat final](http://qkzk.xyz/docs/doc04/doc/billet-tombola2.odt)
