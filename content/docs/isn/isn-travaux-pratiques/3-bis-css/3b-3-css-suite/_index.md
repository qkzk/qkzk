---
author: qu3nt1n
date: 2016-07-02 08:15:25+00:00
draft: false
title: 3b.3 CSS suite
weight: 3
---



Notions abordées dans cette page



 	  * classes et identités (`class` et `id`)
 	  * balises `div` et `span`







# Classes et identités








 	  1. Récupérez [cette archive](https://drive.google.com/open?id=0B4Mq2ZGzUQ3VTUtiVi14OWM2ak0) et après
l'avoir décompressée consultez le
code source du fichier html qu'elle contient puis affichez le dans le navigateur.
 	  2. Les images ont des tailles différentes ce qui rend la page peu
agréable. Créez une feuille de style qui fixe la largeur des images à
200px avec une marge de 10px et la
propriété `vertical-align` fixée à la valeur `text-top`.
 	  3. Ajoutez aux images une marge intérieure de 5px et une bordure fine pleine
noire.
 	  4. Pouvez-vous modifier la feuille de style pour que&nbsp:

 	    * les bordures autour des tableaux de Brueghel aient un
style `inset` et une épaissseur de 2px,
 	    * les bordures autour des tableaux de Monet aient une marge intérieure
de 10px et une couleur verte,
 	    * les bordures autour des tableaux de Matisse soient
en `blue` et d'une épaisseur de 8px et pas de marge intérieure,


 	  5. Choisissez parmi les neuf tableaux celui que vous préférez,
pouvez-vous modifier la feuille de style pour seul celui-là ait, en
plus des autres propriétés de style, une largeur de 300px et une
bordure rouge de 2px ?
 	  6. Pourquoi ne pouvez-vous pas apporter de réponse satisfaisante aux
deux dernières questions ?




Le problème posé par ces deux dernières questions est que l'on ne
sait pas comment proposer plusieurs styles pour une même
balise, `img` ici en l'occurrence.

Il existe heureusement une solution pour ce genre de situation. Il
est possible de définir des classes
différentes pour un même élément et d'attribuer des styles
différents pour chacune de ces classes. Cela se fait très simplement,
que ce soit au niveau du fichier html ou au niveau du fichier
CSS.

Reprenons la situation de la Manip' précédente. Nous pouvons définir
une classe pour les tableaux de Brueghel,
appelons-la `brueghel`. Dans le fichier html, il suffit de
marquer les éléments qui doivent apppartenir à cette classe en
ajoutant l'attribut `class="brueghel"` à l'élément
concerné. Dans le fichier CSS, on peut attribuer un style pour cette
classe en indiquant soit un style pour un
élément `img.brueghel` si l'on veut que le style ne
s'applique qu'aux images de cette classe soit un style pour un
élément `.brueghel` et dans ce cas le style s'appliquerait
à des éléments de la classe `brueghel` auutres que des images.

On aurait ainsi dans le fichier html :


    ...


Tableaux de Brueghel l'Ancien ![Brueghel Babel](brueghel-babel.jpg)
class="brueghel"> ![Brueghel Carnaval et Carême](brueghel-carnaval.jpg)
class="brueghel"> ![Brueghel noces paysannes](brueghel-noces.jpg)
class="brueghel">

...


On remarque qu'il n'y a pas de guillemets autour du nom de la classe
dans le fichier CSS et pas de point devant le nom de la classe dans le
fichier html.


et dans le fichier CSS, en plus des propriétés de style déjà
définies pour la balise `img` :


    img.brueghel {          /*  seules les balises img de classe brueghel sont impactées */
       border-width:2px;
    }
    .brueghel {             /*  toutes les balises de classe brueghel sont impactées */
       border-width:2px;
    }





Faites les modifications nécessaires pour que



 	  * les bordures autour des tableaux de Monet aient une marge intérieure
de 10px et une couleur verte,
 	  * les bordures autour des tableaux de Matisse soient
en `blue` et d'une épaisseur de 8px et pas de marge intérieure,




Reste le cas du tableau préféré. Il est possible d'attribuer
plusieurs classes à un même élément, il suffit d'énumérer dans son
attribut `class` les différentes classes voulues séparées
par des espaces. Une première solution serait donc de définir une
classe `prefere`, de donner à cette classe le style qui
fixe la largeur à 300px et une bordure rouge de 2px puis d'attribuer à
l'image retenue la classe `prefere` en plus de celle déjà
fixée.


Faites-le pour le tableau que vous avez sélectionné et vérifiez que
cela fonctionne.


Cette solution pose cependant un problème par rapport à ce qui était
demandé initialement. En effet il était précisé qu'une fois le tableau
préféré choisi, "_**seul celui-là** ait (...) une largeur de
300px et..._". Or il est possible d'attribuer la
classe `prefere` à n'importe quel élément. Rien n'empêche
donc a priori de choisir "plusieurs préférés".

Il existe cependant une possibilité pour garantir qu'un style
défini ne s'appliquera que sur au plus un seul élément d'une
page. Pour cela il faut attribuer
une identité à un élément. Pour cela il suffit
de définir un attribut `id` pour l'élément
sélection, dans notre cas `id="prefere"`. On peut
définir un style pour cette identité en utilisant dans le fichier
CSS la notation `#prefere`.


Faites les modifications permettant de définir votre tableau préféré
à l'aide d'une identité.


Un intérêt important des `id` est qu'il permet de
caractériser de manière unique une élément dans une page. Cette
possibilité sera particulièrement utilisée lorsque nous manipulerons
dynamiquement le contenu de nos pages avec la programmation.


Dans un document html on peut avoir plusieurs éléments d'une même
classe et plusieurs classes pour un même éléments mais on ne peut
pas avoir deux éléments avec la même identité ni un élément avec
deux identités. Un élément peut à la fois appartenir à une ou plusieurs
classes et avoir une identité.




# Deux nouvelles balises


En plus des balises déjà étudiées, le langage html offre deux
balises génériques :



 	  * la balise `div` qui correspond à un élément de bloc,
on les utilise donc plutôt pour structurer la page
 	  * la balise `span` qui correspond à un élément en ligne,
on les utilise donc de préférence sur une partie d'un élément,
typiquement une portion de texte

A la différence des autres balises déjà rencontrées ces balises
n'ont pas d'interprétation (de sémantique) particulière. Elle n'ont
pas d'effet visuel spécifique : `span` n'a aucun
effet du tout et `div` ne fait que créer un bloc
(comme `p`). Elles prennent tout leur intérêt lorsqu'on
les combinent avec les classes et les identités vues précédemment en
leur associant des styles propres. Ils permettent alors de
structurer la page en en caractérisant certains éléments ou en
marquant certaines portions de texte. On peut ainsi donner plus de
sens aux différents au sein de la page sans être limité par les
balises disponibles par défaut : les "titres" (`h?`)
ou paragraphe(`p`).

Dans le document précédent, on peut par exemple créer un élément
pour regrouper les différents tableaux d'un même peintre et
appliquer un type présentation à ces groupes. Cela pourrait par
exemple donner dans les fichiers html et css avec une
classe `tableaux` :


    ...










      <img src="http://qkzk.xyz/docs/doc03b/brueghel-babel.jpg" alt="Brueghel Babel" class="brueghel"></img>
      <img src="http://qkzk.xyz/docs/doc03b/brueghel-carnaval.jpg" alt="Brueghel Carnaval et Carême" class="brueghel"></img>
      <img src="http://qkzk.xyz/docs/doc03b/brueghel-noces.jpg" alt="Brueghel noces paysannes" class="brueghel"></img>







    ...





    .tableaux {
        background-color : #FFFFBB;
        text-align:center;
        margin:1% 10%;
    }



On peut également souhaiter que les noms des peintres soient mis en
évidence. Il faut alors définir une classe `peintre` que
l'on appliquera à un élément en ligne `span` et on
modifie les fichiers html et css ainsi :


    ...
    Tableaux de Brueghel l'Ancien
    ...





    .peintre {
        font-weight : bold;
        color : green;
    }





Appliquez les modifications ci-dessus aux autres groupes de tableaux
et non de peintre.








 	  1. On retrouve trois éléments de texte de la forme "_Tableaux de
..._". Créez une classe et un style pour ces éléments de texte
et appliquez le au document.
 	  2.

 	    * Créez une identité `piedDePage` à laquelle vous
associerez un style, par exemple en alignant à droite le texte de taille
petite et de couleur blanche sur fond `silver` après
avoir défini des marges.
 	    * Appliquez cette identité au texte en fin de document Textes
issus de wikipédia.
 	    * Pourquoi utiliser une identité et non une classe ?
 	    * L'élément `
` qui le précède est-il encore
nécessaire ?


 	  3. Vous pouvez finaliser la mise en page de ce document en ajoutant des
styles pour les autres éléments
(`h?`, `p`, `body`, etc.).
