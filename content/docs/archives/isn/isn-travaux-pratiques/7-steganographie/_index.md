---
author: qu3nt1n
date: 2016-07-02 11:48:27+00:00
draft: false
title: 7. Stéganographie
bookCollapseSection: true
weight: 9

---


Pré-requis



* le codage des couleurs (voir partie 3
* le code ASCII (voir partie 3)


Notions abordées



* codage de l'information : application (codage des couleurs,
codage des caractères, codage binaire)
* représentation/codage des images, formats
* compression avec ou sans perte










#  Stéganographie





La stéganographie est l’étude des
procédés de dissimulation d’une information dans une
autre.






L'[article de wikipédia qui lui est consacré](http://fr.wikipedia.org/wiki/St%C3%A9ganographie) commence ainsi :"_Si la
cryptographie est l'«art du secret», la stéganographie est l'art
de la dissimulation : l'objet de la stéganographie est de faire
passer inaperçu un message dans un autre message et non de rendre un
message inintelligible à autre que qui-de-droit. Pour prendre une
métaphore, la stéganographie consisterait à enterrer son argent dans
son jardin là où la cryptographie consisterait à l'enfermer dans un
coffre-fort — cela dit, rien n'empêche de combiner les deux
techniques, de même que l'on peut enterrer un coffre dans son
jardin._".





Nous allons nous intéresser à un procédé élémentaire
de dissimulation d’information dans une image.






## Les pixels dans une image




Une image informatisée est discrétisée en pixels (_picture
  elements_), c’est-à-dire en (petites) zones carrées. Chaque
pixel possède une couleur (ou une nuance de gris). L’ensemble des
pixels est organisé sous forme d’un tableau bidimensionnel dans
lequel chacun d’eux peut-être repéré par un numéro de
lignes _x_ et un numéro de colonnes _y_. Le couple
(_x_,_y_) forme les coordonnées du pixel dans l’image.






Ce nombre de pixels est souvent mis en avant comme un critère de qualité d’un appareil photo numérique.







Le nombre de lignes et de colonnes donnent la dimension de l’image, et
le produit de ces deux nombres est égal au nombre de pixels contenus
dans l’image.






Les logiciels de traitement d’images numériques comme Photoshop ou
Gimp permettent par un fort agrandissement de mettre en évidence les
pixels d’une image.







Quelques éléments de la boîte à outils de Gimp que nous utiliserons :



![boite à outils de Gimp](/uploads/docs/doc07/doc/gimp-boite-outils-annotee.png)













  1. Récupérez [cette image](/uploads/docs/doc07/doc/img0.png), et visualisez-la avec le logiciel Gimp.
  2. Effectuez le grossissement maximal de l’image : utilisez l'outil "loupe" et cliquez sur l'image (un appui sur la touche "Ctrl" pendant le clic permet un zoom arrière).

Avec la version 2.6 de Gimp ce grossissement maximal est
   de 25600%, autrement dit un pixel est visualisé à l’écran comme un
   carré de dimensions 256x256, voici vues avec Gimp les images entière
   et avec grossissement maximal.




![](/uploads/docs/doc07/doc/gimp-img0-100.png)

![](/uploads/docs/doc07/doc/gimp-img0-25600.png)










## Couleur d’un pixel






La couleur d’un pixel peut être décrite de plusieurs façons par un ou
plusieurs nombres. Un codage courant que nous avons déjà rencontré est
le codage RVB.







 A l'aide de Gimp, déterminez la couleur du pixel de coordonnées
 (252,214) de l’image précédente : il suffit d'utiliser l’outil
 pipette et de cliquer sur le pixel voulu en maintenant la
 touche _Majuscules_ appuyée. Il peut être pratique de zoomer
 avant...


Quel est le code hexadécimal, celui utilisé en html, pour cette
 couleur ?






## Description du procédé stéganographique





Si on modifie la couleur d’un pixel en ajoutant ou retranchant un
  petit nombre à l’une ou l’autre des trois composantes, le changement
  de couleur du pixel est imperceptible pour l’oeil.







1. Vérifiez que les deux points de coordonnées (0,0) et (0,1)
(tout en haut à gauche de l’image) sont exactement de la même
couleur.
2. Modifiez la couleur du pixel de coordonnées (0,0) en ajoutant 1 à
la composante bleue de sa couleur : dans la "_Boîte à
outils_", après avoir sélectionnée la couleur du pixel avec la
pipette cliquez sur la couleur de premier plan, vous pouvez alors
modifier la composante bleue puis faites la modification à l'aide de
l'outil rayon que vous aurez réglé pour qu'il n'affecte qu'un seul
pixel.
3. Voyez-vous une
différence de couleur avec le pixel voisin ? N'hésitez pas à
zoomer au maximum.








On peut exploiter cette non perception de la modification d’une unité
d’une des trois composantes de la couleur d’un pixel pour cacher un
bit dans un pixel. Plus précisément si le bit à cacher vaut 0 on
modifie la composante de couleur de sorte que son écriture binaire se
termine par 0. Si le bit à cacher vaut 1 on modifie cette composante
de sorte que l’écriture binaire se termine par 1, tous les autres bits
restant inchangés.






Pour dissimuler dans une image un message composé de _n_ bits, on
  cache chacun de ses bits dans _n_ pixels convenus de l’image.






## Retrouver un message





Dans l’image que vous pouvez récupérer [ici](http://www.fil.univ-lille1.fr/~wegrzyno/ISN/Stegano/stega-img0.png), un message a été dissimulé en suivant le procédé précédent. Tous les bits dissimulés correspondent au bit de poids faible de la composante bleue de la   couleur des pixels.






Le nombre _l_ de caractères du message dissimulé dans l’image est codée par les huit premiers pixels de la première ligne (ligne d'ordonnée 0), chacun d’eux donnant un bit de l’écriture binaire de cette longueur.





Utilisez Gimp pour retrouver le nombre _l_ du message dissimulé.





Le message dissimulé est un (petit) texte codé en binaire en
utilisant le codage ASCII. Ce codage codant chaque caractère sur
huit bits, le nombre de pixels dissimulant un bit du message est
donc égal à 8x_l_. Ces pixels sont situés sur la deuxième ligne
(ligne d'ordonnée 1) de l’image en partant de la gauche.






Retrouvez le message dissimulé dans l'image :



1. commencez par noter les valeurs des composantes bleus,
2. puis déterminez les valeurs de leur bit de poids faible,
3. trouvez les codes binaires des caractères cachés,
4. enfin en vous aidant de la [table du codage
ASCII sur Wikipedia](http://fr.wikipedia.org/wiki/Code_ASCII) révélez le message.







## Dissimuler un message






À vous de dissimuler maintenant ! Cachez le message de votre choix
dans l’image d’origine. Afin de vérifier le succès de votre codage,
transmettez l’image que vous aurez produite à votre voisin qui se
chargera de retrouver le message que vous y avez mis.







#  Choix du format de sauvegarde du fichier





Il existe plusieurs formats de sauvegarde des images dans des
fichiers : bitmap (bmp), jpeg (jpg), portable network graphics
(png), ...









1. Reprenez l’image de laquelle vous avez extrait le message qui y
était dissimulé. En utilisant Gimp, enregistrez-la sur disque au
format jpg. Laissez inchangés les
paramètres par défaut.
2. Chargez cette image au format jpg
avec Gimp et tentez de retrouver l’information dissimulée. Que
constatez-vous ?
3. Comparez la taille des deux fichiers  aux
formats jpg
et png. Qu'en pensez-vous ?
4. Examinez d’autres formats possibles. Lesquels conviennent pour
notre procédé stéganographique ?
