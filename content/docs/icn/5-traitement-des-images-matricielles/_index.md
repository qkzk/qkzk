---
author: qu3nt1n
date: 2016-07-04 14:18:48+00:00
draft: false
title: 05. Traitement des images matricielles
weight: 5
---

Cette introduction est accompagnée d'un [tutoriel en Python](http://icnflandres.free.fr/docs_atspace/image_bitmap.zip). Téléchargez et décompressez le, toutes les instructions sont dans le code.

_Cette introduction technique n'a pas la prétention de faire de vous un graphiste._


## Rappels et introduction


Les images matricielles sont des tableaux dont chaque case est est un pixel rempli d'une couleur unie. Cette couleur peut-être un niveau de gris ou une couleur RVB (pour les formats affichés à l'écran). Nous allons nous intéresser aux opérations de base qu'on peut réaliser sur ces tableaux, pixel par pixel. Pour simplifier on ne considérera dans les exemples que des niveaux de gris, allant de 0 (noir) à 255 (blanc).

La couleur est obtenue en ajoutant les niveaux de rouge, de vert et de bleu. Eux même sont codés par un nombre entre 0 et 255. Le jaune vif est donc obtenu par (255,255,0) soit #FFFF00 en hexadécimal. L'impression papier est différente et ne sera pas abordée ici.

Notre image est donc un tableau rectangulaire où chaque case, repérée par ses coordonnées, contient un nombre entre 0 et 255.


## Les transformations les plus courantes




### Exemple : le masque


On dispose d'une image telle que celle-ci où nous gêne la présence de gris autour des pattes de l'araignée.

![spider](http://qkzk.xyz/wp-content/uploads/2016/07/spider.jpg)
On repère que les pattes sont très marquées, presque noire, le niveau de gris moyen est autour de 30. Le niveau du "bruit" autour des pattes est plus élevé, entre 150 et 255. On décide de filtrer tout le gris au dessus de 125.
Pour chaque pixel de l'image, s'il est supérieur à 125 on le remplace par 255. S'il est inférieur à 125 on n'y touche pas.
C'est ce qu'on appelle un masque et ce genre de procédé (plus élaboré on s'en doute) est couramment employé en graphisme.

![spider_mask](http://qkzk.xyz/wp-content/uploads/2016/07/spider_mask.jpg)
![spider_complet](http://qkzk.xyz/wp-content/uploads/2016/07/spider_complet.png)
Les logiciels de retouche d'image et la majorité des langages de programmation disposent d'outils pour réaliser de tels masque. On en rencontrera à la fin du tutoriel associé.
On peut se servir du masque pour laisser passer ou arrêter une couleur prédéfinie et donc faire apparaître une partie seulement d'une image.


### Le contraste d'une image.


Le contraste est la différence de luminosité ou de couleur qui rend un objet (ou sa représentation) distinguable.

![](https://upload.wikimedia.org/wikipedia/commons/2/20/Contrast_change_photoshop.jpg)

Différents niveaux de contrasteLe calcul du contraste d'une photographie est complexe et nécessite des méthodes statistiques avancées. Il est souvent visualisé par un histogramme permettant d'ajuster selon le résultat souhaité. Selon les contextes, les besoins changent.
<table border="0" >
<tbody >
<tr >

<td >![](http://cdn.cambridgeincolour.com/images/tutorials/hist_lowcont.jpg)

</td>

<td >![](http://cdn.cambridgeincolour.com/images/tutorials/hist_highcont.jpg)

</td>
</tr>
<tr >

<td >![](http://cdn.cambridgeincolour.com/images/tutorials/hist_lowcont_hist.png)

</td>

<td >![](http://cdn.cambridgeincolour.com/images/tutorials/hist_highcont_hist.png)

</td>
</tr>
<tr >

<td >![](http://cdn.cambridgeincolour.com/images/tutorials/gradient.jpg)

</td>

<td >![](http://cdn.cambridgeincolour.com/images/tutorials/gradient.jpg)

</td>
</tr>
</tbody>
</table>
Au sein d'une même image le contraste peut varier énormément !


 ![histo-exemple](http://qkzk.xyz/wp-content/uploads/2016/07/histo-exemple.png)



L'histogramme d'une image se comprend ainsi :
L'axe horizontal représente les intensités de 0 (noir) à 255 (blanc).
La hauteur de chaque bâton est donnée par l'effectif de chaque intensité dans le tableau des pixels.


##### Comment faire varier le contraste ?


Très simplement :
on considère le gris central comme référence. Son intensité est (0+255)/2 = 127.5 arrondi à 127 . On calcule l'écart entre l'intensité du pixel et ce centre.
Par exemple un gris clair d'intensité 180. On calcule l'écart avec le centre : (180-127) = 53
Si on augmente le contraste de 20%, on multiplie cet écart par 1.2 (augmenter de 20%...) et on obtient 53*1.2 = 63.6. On ajoute alors à 127 pour retrouver un gris plus clair : 127+63.6 = 190.6 arrondi à 191.

De façon analogue, un gris sombre, d'intensité 60 se trouvera encore assombri. Son écart à la valeur centrale ayant été amplifie. Il deviendra : 46.6, arrondi à 50.

C'est ce que font pour chaque pixel les logiciels qui changent le contraste d'une image.

En pratique, avec un coefficient de 0 l'image devient totalement grise, uniforme. Avec un contraste immense, on ne voit plus que du blanc et du noir.

Manip : Le tutoriel associé à la page présente une boucle qui fait varier le contraste d'une image prédéfinie. Testez la et changez les valeurs des coefficients.

**Remarque :** Ici, on a effectué le choix de couleur de référence indépendamment de l'image... Parfois on a besoin d'adapter la démarche à une image en particulier et on choisit comme référence l'intensité moyenne de l'image.

_Ah mais... manipuler une image c'est faire des maths avec un tableau de nombre ????_

Oui... et non.

Les transformations sont toutes mathématisées mais le choix de la bonne manipulation à effectuer est propre à chaque domaine et parfois à chaque image. L'imagerie médicale se moque des qualités artistiques de ce qu'elle représente. Elle cherche à faire apparaître des particularités aidant au diagnostic. Le photographe artistique cherche parfois à faire transparaître un message et le publicitaire à capter le regard d'un conducteur arrêté devant une affiche. Les traitements apportés à l'image changent alors considérablement... mais les outils sont souvent les mêmes.

Revenons au transformations courantes.


### La luminosité.


Assombrir ou éclaircir une image est très simple ! Il suffit d'ajouter ou d'enlever de l'intensité à chaque pixel. Bien sûr on est limité par 0 et 255.

Le tutoriel associé présente quelques manipulations de la luminosité. Les tester.


### Comment flouter une image, faire ressortir les détails ?


Flouter une image consiste à harmoniser les pixels d'une partie de l'image ou de toute l'image entière. On perd donc de l'information dans le processus et certains détails sont gommés.



Mais pourquoi vouloir perdre de l'information ? Pour embellir l'image pardi !

![](http://www.designyourway.net/diverse/portraitph/35330438349.jpg)

Un portraitiste gomme les défauts d'un visage.
Regardez le front pour vous en convaincre![](http://media.gettyimages.com/photos/paris-actor-jean-claude-van-damme-poses-at-a-portrait-session-in-on-picture-id81292328)

On cherche parfois à faire apparaître les particularités !![](http://sf.be.com/1/mode/bien-raisonnable/photo/6286628/16419738cd/bien-raisonnable-mullet_hairstyles-img.jpg)

Mais parfois on serait tenté d'effacer certains détails...On peut aussi donner de la profondeur de champ en floutant le fond :

![](http://static.wixstatic.com/media/263012_bf9784d6f9754e43aa4097be870fe82e.jpg/v1/fill/w_620,h_221/263012_bf9784d6f9754e43aa4097be870fe82e.jpg)
Ou créer un effet miniature :

![](http://img.zphoto.fr/data/photo/6c/89/512090.jpg)

Ce sont de vraies maisons !**Mais comment réaliser un flou ?**

Là, c'est tout de suite beaucoup plus compliqué. Il existe mille et une méthodes mais toutes ont un principe commun. Elles varient selon deux abords : la complexité du calcul (et donc le temps de calcul, les ressources machines nécessaires) et le résultat recherché.
Le procédé général consiste à calculer, pour chaque pixel, l'état de son environnement (les pixels qui l'entourent). On détermine alors une valeur moyenne qui remplacera l'intensité du pixel. La lourdeur du calcul provient alors de cet environnement (Un pixel d'écart, deux, trois ? Et les coins ? Pourquoi pas un disque autour du pixel ? etc.) et du calcul à proprement parler de cette valeur moyenne.
De nombreux procédés de calcul existent et ont leurs avantages (flou linéaire, quadratique, gaussien etc.)

On doit toujours prendre en compte les ressources (le temps de calcul et la mémoire dont on va disposer) et l'objectif à atteindre.

Le tutoriel comporte quelques exemples d'application de flou "blur" en anglais. Les repérer dans le code et les exécuter.


### L'acuité d'une photographie : le niveau de précision des contours.


Là aussi c'est compliqué... On cherche un traitement de l'image qui fasse ressortir un contour et le définisse précisément. On serait tenté d'augmenter le contraste mais ce n'est pas toujours optimal. Souvent on règle l'appareil photographique pour qu'il saisisse précisément les formes. C'est le principe de la photographie macro.

Mais une fois la photo prise... Retenons qu'on cherche les zones où la variation d'intensité est grande et le "bruit" important. Alors on règle le traitement selon le résultat souhaité.

![](http://cdn.cambridgeincolour.com/images/tutorials/sharpening_eagle2-original.jpg)
![](http://cdn.cambridgeincolour.com/images/tutorials/sharpening_eagle2-radius-small.jpg)
![](http://cdn.cambridgeincolour.com/images/tutorials/sharpening_eagle2-radius-large.jpg)
![](http://cdn.cambridgeincolour.com/images/tutorials/sharpening_eagle2-radius-optimal.jpg)
De gauche à droite, la photo originale, un réglage trop large, trop étroit et le "bon" réglage.

Le tutoriel présente une boucle affichant différents niveaux de réglages du "sharpness", l'acuité. A vous de le tester.

Augmenter la netteté d'une image ajoutera aussi du bruit dans les zones qui n'auraient pas dues être retouchées. On peut chercher, en effet à rendre bien dessiné un personnage et ne pas toucher au fond, délibérément flou. L'emploi d'un masque est alors nécessaire.

Nous n'entrerons pas plus loin dans les procédés mathématiques qui dépassent largement notre cadre.


## Le changement de dimension


AH, voilà qui est parait simple ! d'une image en 800 x 600 je fais une image en 640 x 480.

Mais comment ? Là aussi, des maths...

**Le principe :**

à nouveau, notre tableau de pixels a deux dimensions. Chaque pixel a son intensité. Si je passe d'une ligne comportant 800 pixels à une ligne en comportant 640, je pourrais être tenté d'en supprimer 160 pour n'en garder que le bon nombre. Mais lesquels ? Comment choisir ? Devrais-je adapter le procédé à chaque ligne de chaque image ?

Et cette méthode ne permettra pas d'augmenter les dimensions d'une image...

Aussi on procède par **interpolation.**

**Le principe de l'interpolation** : on utilise des données connues pour estimer des données en des points inconnus.

Si je souhaite connaître la température à midi mais ne l'ai mesurée qu'à 11h et 13h, je suis tenté d'employer l'interpolation linéaire :

![](http://cdn.cambridgeincolour.com/images/tutorials/interpolation_graph1.png)
Mais si j'ai d'autres mesures autour de midi, je peux faire mieux.

![](http://cdn.cambridgeincolour.com/images/tutorials/interpolation_graph2.png)
On remarque immédiatement qu'on obtient une estimation plus précise en tenant aussi compte de la donnée "11H30" dans le second exemple.

Interpoler des valeurs telles que celles-ci "semble" simple (Remarque du prof de maths : néanmoins ça ne l'est pas.) parce que ce sont des températures en fonction du temps : une variable en entrée, une variable en sortie.

Mais pour des couleurs (R, G, B) en fonction de deux coordonnées (x et y) : 2 données en entrée (x et y), 3 en sortie (R, G et B). aie aie aie.

Heureusement, des procédés existent. Ils permettent de calculer les niveaux estimés en d'autres pixels que ceux dont on dispose.

Par exemple, pour un agrandissement de 183% :


![](http://cdn.cambridgeincolour.com/images/tutorials/interpolation_2De.png)
![](http://cdn.cambridgeincolour.com/images/tutorials/interpolation_2D-lg.png)
![](http://cdn.cambridgeincolour.com/images/tutorials/interpolation_2D-interp.png)



_Original - Avant Interpolation - Après Interpolation _


Et ce qu'on obtient sans interpolation :

![](http://cdn.cambridgeincolour.com/images/tutorials/interpolation_nointerp.png)
Selon la qualité souhaitée et les ressources dont on dispose on emploiera un procédé ou un autre.


### ZOOM ZOOM !


Donc je peux zoomer une image comme dans [les experts](http://i.imgur.com/WuEff.jpg) ???

Non, c'est n'importe quoi. Même en disposant d'une image très détaillée au départ telle que :

![](http://cdn.cambridgeincolour.com/images/tutorials/digital_rainbow.jpg)
et en zoomant sur une partie avec des procédés numériques (digital zoom), voici ce qu'on obtient dans le meilleur des cas :

![](http://cdn.cambridgeincolour.com/images/tutorials/digital_rainbow_digital.jpg)
Une remarque toutefois... certains procédés très récents existent mais sont infiniment plus complexes. Un [exemple.](http://www.extremetech.com/extreme/132950-csi-style-super-resolution-image-enlargment-yeeaaaah) _Pour les anglophobes : Cela demande ÉNORMÉMENT de calculs très complexes - en 2012 les chercheurs n'ont pas précisé combien de temps par photographie, c'est mauvais signe. On touche ici à de l'informatique théorique très élaborée et encore loin des applications grand public._

Alors comment faire sans disposer des moyens de la Nasa ? Changer **l'objectif** de l'appareil photo ! C'est ce qu'on appelle un zoom optique.
Voici par contre ce qu'on obtient avec un zoom optique :

![](http://cdn.cambridgeincolour.com/images/tutorials/digital_rainbow_optical.jpg)


![](http://blogues.lapresse.ca/brault/files/2012/08/BB25153-420x279.jpg)

Un bel objectifEt, à plus de 600 mètres :

![](http://blogues.lapresse.ca/brault/files/2012/08/Canoe-Kayac-022.jpg)



### De l'interpolation partout


L'interpolation intervient aussi quand vous tournez une image ! Seules les rotations "simples" (90°, 180°, 270°) peuvent se faire sans perte (Pourquoi ????) Les autres angles engendrent tous une interpolation "lossy" !

Parmi les procédés de redimensionnement souvent employé on retiendra l'anti-aliasing bien connu des gamers.

Le tutoriel vous présente aussi différentes façons de transformer une image (déformations selon un axe, rotation prédéfinie, rotation libre etc.). Testez les.

Remarque :
Flouter une partie d'une image ou travailler son acuité peut servir à faire disparaître le "bruit", c'est à dire les pixels dont l'intensité est erronée par rapport à l'objet photographié. C'est très important en imagerie médicale ou en reconnaissance de caractères. C'est par un traitement complexe des images que Google parvient à lire les panneaux de circulation et à en intégrer le contenu dans ses logiciels. On procède de même pour automatiser les amendes : le logiciel détecte la plaque, en traite l'image et reconnait les caractères. Il interroge sa base de donnée, retrouve le véhicule correspondant et son propriétaire. L'amende lui est alors adressée.
D'où les articles amusants dans la presse : _"Papy Marcel en deux chevaux flashé à 200 km/h sur l'A7 ce lundi etc."_

![](https://s-media-cache-ak0.pinimg.com/736x/1d/46/1b/1d461b8fbe030453c0371d3a1175c6bf.jpg)



_On remarque que la plaque est difficilement lisible sur cette photographie !_


Une dernière remarque à ce propos :
Google s'est lancé il y a quelques années dans le projet [street view](https://www.google.fr/maps/@48.8740499,2.2939762,3a,75y,104.59h,96.63t/data=!3m6!1e1!3m4!1sdKOTWQWKKOQ58GBoQqjUPg!2e0!7i13312!8i6656?hl=fr). Il a alors rencontré d'immenses difficultés pour automatiser le repérage dans les rues. Souvent seules les maisons sont numérotées et il n'existe aucun autre moyen de connaître ce numéro qu'en lisant la plaque depuis la rue. Mais ces plaques ne respectent aucune convention et tout le monde est libre de la typographie, dimension, couleur...

Comment reconnaître un numéro de maison quand aucune convention typographique n'est respectée ?
L'idée géniale est venue avec les captchas, ces petits boutons où l'on vous demande de recopier une image pour démontrer que vous n'êtes pas un robot. En joignant à un vrai captcha une photographie de plaque de numéro de maison, on fait travailler gratuitement l'utilisateur à l'amélioration d'un service qu'il utilise. _Plus d'infos dans [cette source](https://techcrunch.com/2012/03/29/google-now-using-recaptcha-to-decode-street-view-addresses/) (en anglais)._


### L'exemple des textes : vers les images vectorielles


Les textes sont particulièrement soumis à des problèmes de redimensionnement. Les bords d'une lettre sont rarement verticaux ou horizontaux. Elles comportent beaucoup d'angles, de courbes... Et nos pixels carrés posent problème. Essayez d'écrire du texte avec des blocs de base dans minecraft ou en légo et vous comprendrez vite votre douleur.
Les lettres sont dessinées pour différentes tailles de caractères. Certaines polices bitmap (par exemple .bdf) contiennent toute une gamme de tailles pré dessinées et éventuellement retouchées.

![](https://upload.wikimedia.org/wikipedia/commons/2/29/Original_Mac_fonts.png)

Quelques fontes du premier système MacD'autres polices sont en vectoriel (Open Type, True Type, Meta Font (.otf, .ttf, .mf)). On ne retient que la description de la forme, pas l'état de chaque pixel ! C'est beaucoup mieux. Le rendu est alors toujours parfait.

_Un exemple d'utilisation de MetaFont :_


    %file name: beta.mf
    %mode_setup;
    % Define a beanlike shape for the character B
    beginchar("B",11pt#,11pt#,0);
      % Setup coordinates as an equation system
      y1=y2=y3=0;
      y4=y5=y6=h;
      x1=x4=0;
      x2=x5=w;
      x3=x6=2*w;

      % Define pen
      pickup pencircle xscaled 0.2w yscaled 0.04w rotated 45;

      % Draw the character curve
      draw z1..z3..z6{z2-z6}..z5..{z4-z2}z4..cycle;
    endchar;

    end


_Et le résultat :_
![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Metafont-example-output.svg/568px-Metafont-example-output.svg.png)



### C'est toujours aussi compliqué ?


Oui et non : nul besoin de maîtriser l'interpolation pour mettre en valeur la photo de tata qui pèche une sardine. C'est par contre indispensable pour automatiser le traitement d'une immense quantité d'images (flux vidéo, imagerie médicale etc.)

Dès que vous cherchez un rendu un peu meilleur alors il vaut mieux comprendre.

_Une grande partie de ce cours est inspiré des tutoriels de [Cambridge Colour](www.cambridgecolour.com)._
