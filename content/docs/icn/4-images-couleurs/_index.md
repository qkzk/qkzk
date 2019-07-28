---
author: qu3nt1n
date: 2016-07-01 14:38:32+00:00
draft: false
title: 04. Images, couleurs
weight: 4

---



Notions abordées



* traitement des images : matriciel et vectoriel
* compression de données
* les cartes en  anamorphose







# Le traitement des images et les couleurs.




## Introduction : sauvegarder une image.


L'image est le procédé le plus courament employé pour transmettre une information. L'enfant dessine spontanement et longtemps avant de savoir écrire. L'art préhistorique remonte à environ 40 000 ans et l'écriture à 3300 ans. Les manuels Ikea ne comportent aucun texte seulement des pictogrammes et quelques chiffres. Il est donc inutile de les traduire pour exporter les meubles.

Comment numériser et sauvegarder une images dans un ordinateur ?


### Image matricielle et image vectorielle


Le procédé le plus naturel est celui de l'**image matricielle** : on se repère dans une image rectangulaire comme si elle était un tableau et chaque élément du tableau se voit attribuer une couleur.

![](https://upload.wikimedia.org/wikipedia/commons/1/16/DigitalPicture.jpg)
Selon la taille de l'image et la quantité de couleurs différentes qu'elle contient, ce procédé est vite couteux en espace. Un grand carré rouge uni de 1000x1000 comporte 1 million de pixels, tous de la même couleur enregistrés individuellement. Ce n'est pas très malin.

Et pourtant, grosso modo, c'est ce que font les appareils photo numériques et les scanners en haute résolution. Ne peut-on faire mieux ?

Si, bien-sûr, mais c'est vite complexe et cela demande des choix... que l'appareil photo numérique n'est pas toujours capable de faire seul.


#### **Quelques formats de compression.**




Vous devez avant tout savoir qu'il y a deux critères importants pour sauvegarder les images.

Premièrement, il y a deux façons de compresser : [Sans perte](http://en.wikipedia.org/wiki/Lossless_data_compression) et [à perte](http://en.wikipedia.org/wiki/Lossy_compression).



 **Sans perte** signifie que l'image est rendue plus petite (en espace disque), mais pas au détriment de la qualité.
 **A perte** signifie que que l'image est rendue (encore plus) petite, mais cela joue sur la qualité. Si vous enregistrez plusieurs fois une image dans un format à perte, la qualité de l'image va se dégrader de plus en plus.

Il y a aussi plusieurs façon de définir les couleurs (palettes): [Indexed color](http://en.wikipedia.org/wiki/Indexed_color) et [Direct color](http://en.wikipedia.org/wiki/Color_depth#Direct_color).



 **Indexed** signifie que l'image ne peut disposer que d'un petit nombre de couleur (généralement 256), définies par l'auteur, dans ce qu'on appelle une Carte de couleur.
 **Direct** signifie que l'on peut enregistrer des _milliers_ de couleurs qui n'auront pas été choisies une par une par l'auteur.




---





#### **Les formats d'image matricielle**





---



**BMP** - Lossless / Indexed et Direct

C'est un ancien format. Il est Lossless (aucune perte d'information en sauvegardant) mais il n'y a presque pas de compression, ce qui signifie que le fichier peut vite devenir TRES gros. Il peut disposer de palettes prédéfinies (Indexed) ou Directes, mais c'est une maigre consolation. L'espace disque est inutilement gaspillé ce qui fait que ce format est inemployé ou presque.

Bon pour : Rien. Il n'y a rien que le BMP fasse mieux que les autres.

![BMP vs GIF](http://i.stack.imgur.com/J1EEX.png)




---



**GIF** - Lossless / Indexed

GIF utilise une compression sans perte, ce qui signifie qu'en enregistrant plusieurs fois une image, on ne perd pas d'information. Le poids du fichier est bien plus petit que celui d'un BMP, l'algorithme de compression étant bien meilleur, mais il ne peut disposer que d'une palette de couleur indexée. Dans la majorité des cas, il ne peut y avoir plus de 256 couleurs dans le fichier. Cela parait peu et c'est le cas.

Les images GIF peuvent aussi être animées et être transparente.

Bon pour : les logos, les dessins avec des lignes et des formes géométriques simples. N'est réellement employé que pour de petites images sur les sites web.

![GIF vs JPEG](http://i.stack.imgur.com/F7VtM.png)




---



**JPEG (.jpeg, .jpg)** - Lossy / Direct

Les images JPEGs furent crées pour comprimer les photographies le plus possible en enlevant les détails que l’œil humain ne parvient pas à déceler. En conséquence c'est un format à perte et sauvegarder une image en jpg plusieurs fois va engendrer des pertes répétées. JPG dispose d'une palette de milliers de couleurs et est très bon pour la photo, mais la compression est mauvaise pour les logos et les dessins : non seulement ils seront rendus grossiers mais ils auront aussi une taille plus importante qu'en GIF !

Bon pour : Photographie. Aussi les dégradés (gradients).

![JPEG vs GIF](http://i.stack.imgur.com/aNqf7.png)




---



**PNG-8** - Lossless / Indexed

PNG est un format plus récent, et PNG-8 (la version indexée de PNG) succède parfaitement aux GIF. Hélas il a quelques inconvénients : d'abord il ne peut être animé comme le GIF (en fait si, mais peu de navigateurs hormis Firefox semblent l'implémenter, contrairement à GIF que tous les navigateurs supportent). Ensuite il s'affiche mal dans les anciens navigateurs comme IE6. Enfin certains logiciels très utilisés comme Photoshop ont une très mauvaise intégration du PNG. (C'est un choix délibéré d'Adobe qui cherche à promouvoir ses propres formats) PNG-8 ne contient que 256 couleurs, comme les GIF.

Bon pour : Ce que le PNG-8 fait mieux que les GIF est d'intégrer la transparence Alpha.

![PNG-8 vs GIF](http://i.stack.imgur.com/B09oZ.png)


**Remarque importante :** Photoshop ne gère pas encore la transparence Alpha pour les fichiers PNG-8. On peut contourner ce problème en utilisant un logiciel externe pour transformer l'image.



---



**PNG-24** - Lossless / Direct

PNG-24 est un excellent format qui combine l'encodage Lossless et les couleurs Directes (Milliers de couleurs, comme le JPEG). Il ressemble beaucoup au BMP dans ce sens, à ceci prêt qu'un PNG compresse l'image, aussi le poids du fichier est bien moindre. Hélas un fichier PNG-24 sera bien plus gros qu'un JPEG, un GIF ou un PNG-8, aussi il faut prendre ce critère en compte avant de s'en servir.

Bien que le PNG-24 comporte la compression sans perte et les milliers de couleur il n'est pas prévu pour remplacer le JPEG. Une photographie sauvegardée en PNG-24 sera environ 5 fois plus lourde qu'un JPEG pour une amélioration très médiocre de la qualité à l’œil nu. (Bien sur c'est un résultat appréciable si vous cherchez à conserver la meilleure qualité possible.)

PNG-24 gère aussi la transparence alpha.



---





#### **L'image vectorielle**


C'est le fait de décrire la construction, élément par élément, d'une figure à l'aide de commandes simples. Celle-ci est alors construite objet par objet quand on l'affiche. L'immense avantage est qu'on peut décrire exactement ce qu'on veut... et que le résultat restera totalement identique à tous les niveaux de zoom ! L'inconvénient est que décrire ainsi une photographie relève du travail de forçat et va demander un espace disque considérable... C'est un format qui a beaucoup d'emplois : polices de caractères, plans, cartes, logos, figures scientifiques, grandes affiches etc.

Le format d'image vectorielle le plus répandu est le SVG.



---



**SVG** - Lossless / Image vectorielle

C'est un format en pleine expansion (en particulier depuis la démocratisation des écrans Retina par apple). Il est donc différent de tous les précédents en son principe même : il est [vectoriel](https://fr.wikipedia.org/wiki/Image_vectorielle) et les précédents sont tous [matriciels](https://fr.wikipedia.org/wiki/Image_matricielle). Il est donc composé de lignes et de courbes remplies de couleurs au lieu de pixels. Zoomer sur une image vectorielle affiche toujours cette courbe. Quand on zoome sur une image matricielle on voit les pixels.

Par exemple :

[![PNG vs SVG](http://i.stack.imgur.com/Cnaf5.png)
](http://i.stack.imgur.com/Cnaf5.png)

[![SVG vs PNG](http://i.stack.imgur.com/UydAT.png)
](http://i.stack.imgur.com/UydAT.png)

SVG est donc idéal pour les logos et les icônes qui doivent garder leur précision à toutes les tailles et sur tous les écrans.

Ajoutons à cela que les fichiers SVG sont écrits en XML, format lisible par un éditeur de texte. Ils peuvent donc être édités à la main (il suffit de repérer la ligne de code qui colore l'oiseau de twitter pour le passer en rouge) et donc être manipulés PAR le navigateur ! Par exemple on peut écrire des scripts Javascript intégrés dans une page web qui changent la couleur d'un logo pour l'adapter à une page... comme du texte. Il est donc inutile de garder plusieurs versions de la même image selon les besoins.


### Et la video ?




OULA, c'est compliqué ! Elles sont encodées généralement image par image et le son est à part. Le tout est entremêlé pour que le son se ne trouve pas à la fin d'un énorme fichier. Beaucoup de procédés existent est le plus simple et courant est celui .divx : chaque image est en jpg, le son est en MP3. Si deux images successives sont identiques, on ne sauvegarde que la différence, le reste est transparent et on le colle par dessus... Il existe là aussi des milliers de variantes que nous n'aborderons pas vraiment.




AVI, par contre n'est qu'un conteneur qui n'indique en rien l'algorithme d'encodage de la vidéo qu'il contient...






---





# Quelques précisions sur les couleurs.


Comme on l'a vu, chaque couleur doit être sauvegardée dans le fichier et décrite précisément. Le procédé pour les afficher à l'écran est différent de celui employé pour les imprimer sur une page.

**L'écran** projette de la lumière (j'espère que je ne vous apprends pas que vous pouvez utiliser votre téléphone dans le noir...) et les couleurs obtenues le sont par synthèse additive. L'addition de ces trois lumières, généralement Rouge, Verte et Bleue (RVG en français, RGB en anglais) en proportions convenables donne la lumière blanche. L'absence de lumière donne donc le noir. Les écrans modernes disposent donc de trois pixels très proches, un rouge, un vert un bleu et les illuminent indépendamment.

Synthèse additive
![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Synthese%2B.svg/220px-Synthese%2B.svg.png)
**L'impression** utilise la synthèse soustractive (Magenta, Cyan, Jaune et souvent Noir). Chaque pigment ABSORBE une partie de la lumière qu'il reçoit et réfléchit le reste. Voilà pourquoi vos photographies changent quand on les éclaire différemment. D'ailleurs, vous ne pouvez pas les voir "dans le noir".

Synthèse soustractive
![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Synthese-.svg/220px-Synthese-.svg.png)



Un exemple de synthèse soustractive en mode CMJK (cyan, magenta, yellow, key = noir).

Autre question : combien de couleurs ? Pourquoi 256 ou "des milliers ?".
L'ordinateur fonctionne grâce à l’électronique. Le courant passe 1, ou non 0 : le binaire. 0 ou 1 : un bit. En binaire b10 désigne le nombre décimal 2.


<blockquote>

>
> “There are only 10 types of people in the world: those who understand binary and those who don't.”
>
> </blockquote>




On stocke généralement les données en des paquets de 23 = 8 bits = 1 octet (1 byte en anglais, c'est super l'anglais). Ensuite on choisit un format simple construit sur les octets afin de mieux comprendre.


On arrive à l'hexadécimal, comportant 16 chiffres : 0 1 2 3 4 5 6 7 7 8 9 A B C D E F.

Bon, disons que chaque couleur a 4 bits et qu'on a 4 niveaux de transparence on a alors :
4x4x4x4 = 256 couleurs possibles, celles du GIF et PNG-8.

Pour un chiffre hexadécimal par couleur et autant pour la transparence : 163 = 65 536 couleurs. Des milliers.

Maintenant on a 2 chiffres hexadécimaux par couleur et autant pour la transparence :
(162)3 = 16 777 216 couleurs possibles !
On arrive à plus de 4 milliards si on considères les 16x16 = 256 niveaux de transparence. Aie. Voilà pourquoi on intègre des palettes de couleurs dans les fichiers.

En html et presque partout ailleurs, on utilise le codage hexadécimal pour représenter une couleur :
#FF00AA va désiger : FF en rouge (le maximum), 00 en vert (pas de vert), AA en bleu (pas mal de bleu). Un [magenta](http://www.colorhexa.com/ff00aa) tirant sur le rouge donc.

#FF00AA
![](http://www.colorhexa.com/ff00aa.png)




---





# Les logiciels de dessin et de retouche, nos ambitions...


Il en existe des centaines et ils ont tous leurs spécificités. Les professionnels utilisent principalement ceux de la suite Adobe qui sont très complets mais très chers : Photoshop travaille sur les images matricielle et est l'outil de base du photographe professionnel qui retouche ses images ; Illustrator celui du designer qui construit des images vectorielles (polices de caractères, logos, plans).

GIMP est la meilleure alternative gratuite à la suite Adobe. Il traite le matriciel et le vectoriel, existe sur toutes les plateforme mais GIMP reste difficile d'accès. Aussi...

**Photofiltre (matriciel) et Inskcape (vectoriel)** seront les logiciels que nous allons employer. Ils sont gratuits, relativement simples et puissants.

Photofiltre permet l'application rapide de filtres sur une image pour en changer tout ou partie du rendu : la convertir en noir et blancs, changer son contraste, sa luminosité, la flouter etc.
On peut aussi dessiner des formes simples, y intégrer du texte, d'autres images, détourer une image etc.

Nous n'aurons pas d'ambition très poussée à ce propos, seulement celle de comprendre le principe des filtres et de ce qu'ils font à une image. Plus tard nous appliquerons ces procédés pixels par pixels sur de petites images.

Concernant l'image vectorielle nous verrons d'abord comment créer quelques images simples à la main afin d'être capable d'éditer, toujours à la main, le contenu d'un fichier SVG.

Nous construirons dans Inskcape un logo, le notre, et ce sera déjà bien !

Nous verrons plus longuement ce qu'il est possible de faire grâce au dessin vectoriel sur les cartes, comment celles-ci sont rendues à l'écran et comment créer nous même des cartes simples ou très complexes.
