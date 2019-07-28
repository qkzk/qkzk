---
author: qu3nt1n
date: 2016-07-02 09:37:25+00:00
draft: false
title: 4.06 Création de fonctions
weight: 6
---

Notions abordées dans cette page



* utilisation de définitions javascript faites en dehors de la page
* écriture de fonctions
* (première) utilisation d'un debugger
* tests







# Création de fonctions




## Du code javascript en dehors de la page HTML




Télécharger sur le bureau les quatre fichiers : [monuments1.html](http://qkzk.xyz/docs/doc04/doc/monuments-version2.html), [monuments-fonction.js](http://qkzk.xyz/docs/doc04/doc/monuments-fonction.js), [monuments-version2.html](http://qkzk.xyz/docs/doc04/doc/monuments-version2.html) et [monuments-fonction2.js](http://qkzk.xyz/docs/doc04/doc/monuments-fonction2.js)
Les fonctions qu'ils contiennent sont susceptibles d'être bloquées par le serveur qui héberge les fichiers.
Dans la suite du document tous les liens mènent vers ces fichiers.








1. Consultez les 2 pages suivantes : [version 1](http://qkzk.xyz/docs/doc04/doc/monuments-version1.html), [version 2](http://qkzk.xyz/docs/doc04/doc/monuments-version2.html). Rafraîchir la page si les images ne se chargent pas.
2. Voyez-vous des différences entre ces 2 versions ?
3. Consultez les codes HTML de ces 2 pages.
4. Quelles différences constatez-vous ? Qu'en pensez-vous ? L'un des deux fichiers HTML est-il plus facile à comprendre ? Si oui, lequel ?
5. Le château de Chambord se trouve aux coordonnées (47.616141,1.517105). Ajoutez pour chacun des 2 documents HTML l'affichage de ce monument. Cela vous semble-t-il plus facile, ou plus naturel, dans un cas que dans l'autre ?




Le code de la version 2 est particulièrement épuré. On devine facilement que la responsabilité de l'affichage des monuments a été déléguée à la fonction `afficheMonument` que l'on voit apparaître dans le code source. On n'en connaît pas la spécification précise, mais on parvient néanmoins à l'utiliser par mimétisme pour ajouter le château de Chambord.


D'après le comportement observé dans le document version 2, donnez une spécification (probable) de la fonction `afficheMonument`.


Vous vous en doutez sûrement, la
fonction `afficheMonument` n'est pas une fonction prédéfinie en Javascript. Elle a été créée spécifiquement pour notre exemple. Mais alors où est-elle définie ? La réponse se situe dans la zone `head` du document version 2. Les plus attentifs ont peut-être constaté la ligne :

~~~javascript
<script src="monuments-fonction.js" type="text/javascript">// <![CDATA[
    // ]]></script>
~~~


Cette instruction indique que du code Javascript se trouve dans
un fichier précisé par l'attribut `src`,
ici `monuments-fonction.js` qui va être chargé et évalué
par le navigateur.

Dans la fenêtre contenant le code source de la
page `monuments-fonction.js` est un hyperlien qui lorsqu'on
le sélectionne permet de consulter le contenu du
fichier `monuments-fonction.js`.

On peut également définir des fonctions sans utiliser du
mot-clé `var` à l'aide de la syntaxe suivante :

~~~javascript
function afficheMonument (nomMonument, longitude, latitude) {
  var texte = texteMonument(nomMonument, longitude, latitude);
  document.writeln(texte);
}
~~~




Prenez quelques instants pour étudier attentivement le contenu de ce
fichier, en particulier  :



1. Quelles sont les 3 fonctions définies dans ce fichier ?
2. Etudiez chacun des commentaires qui précédent les définitions. La spécification que vous avez proposée pour `afficheMonument` correspond-elle ? Ces commentaires vous permettent-ils d'utiliser les fonctions sans étudier de manière plus poussée le code de leur définition ? Cela serait-il aussi facile sans ces commentaires ?
3. Quel mot-clé introduit la définition de ces fonctions ?
4. Quelles sont les 2 fonctions qui produisent un résultat ?
5. Dans ces fonctions, quel mot-clé, absent dans la troisème fonction, vous semble leur permettre de produire ce résultat ?
6. Dans cette définition :

~~~javascript
var afficheMonument = function (nomMonument, longitude, latitude) {
    var texte = texteMonument(nomMonument, longitude, latitude);
    document.writeln(texte);
}
~~~


désignez les paramètres formels, les paramètres effectifs et les variables.






## Définition de fonctions


Ce fichier `monuments-fonction.js` contient la
définition de 3 fonctions que ne proposent pas initialement le
langage Javascript. La définition de ces fonctions permet d'enrichir
le langage en fournissant de nouveaux outils (les 3
fonctions `afficheMonument`, `texteMonument` et
`imageGoogleMap`) mis à
la disposition du programmeur. Une fois définies celles-ci peuvent
être utilisées exactement comme l'est par exemple la
fonction prédéfinie `parseInt`. C'est ce qui est fait
dans le fichier `monuments-version2.html`.


Déduisez de ce qui précède la syntaxe de la définition d'une fonction en Javascript.




"_return_" peut se traduire par "_retourner_" ou aussi
"_renvoyer_" d'où l'usage des expressions "_valeur retournée/renvoyée
par une fonction_"
ou "_la fonction retourne/renvoie la valeur ..._".


Dans la définition on peut distinguer 2 parties :



* l'entête de la fonction qui
reprend le nom et la liste des paramètres entre parenthèses (on doit
noter `()` si aucun paramètre n'est requis),
* le corps de la fonction qui
contient le code exécuté lors de l'appel de la fonction.
Dans le corps de la fonction le mot-clé return permet
d'introduire une expression dont la valeur est résultat de l'appel
de fonction.

Le traitement d'une fonction se termine dès qu'une
expression `return` est rencontrée avec le résultat
associé. Si le corps la fonction ne contient pas une telle
expression, la fonction ne renverra aucun résultat et son traitement
se termine lorsque la dernière expression du corps a été évaluée.


## Au coeur du traitement




Cherchez l'origine du mot _bug_ en informatique et en
programmation en particulier.


Nous allons étudier en détail le fonctionnement de ces fonctions. Pour
cela nous utiliserons à nouveau Firebug et cette fois-ci ses fonctions
de debugger. Un debugger est un
programme informatique dont le but est de permettre l'étude en
détail du fonctionnement d'un code écrit dans un langage donné. Le
plus souvent cette étude est menée lorsque ce code n'a pas le
comportement attendu ("_il buggue_") et donc y trouver et
comprendre le problème afin de le corriger. Les fonctionnalités
habituelles d'un debugger sont de permettre :



* la mise en place de **points d'arrêt** dans le code
afin d'en interrompre l'exécution au moment précis ou cet endroit du
code est traité,
* l'**exécution pas-à-pas** du programme,
* d'**inspecter l'état des données** manipulées par le code,
notamment afin de vérifier s'il correspond à ce que l'on attendait.

Dans notre cas, notre programme ne comporte pas d'erreur dans son
fonctionnement, mais nous allons néanmoins expoiter ces possibilités pour
en examiner le fonctionnement en détail :






1. Activez Firebug et ouvrez le document dans
sa [version 2](http://qkzk.xyz/docs/doc04/doc/monuments-version2.html).
2. Ouvrez l'onglet script et choisissez le
fichier`monuments-fonction.js` contenant le code des
fonctions que nous voulons analyser.
![Firebug - code](http://qkzk.xyz/docs/doc04/doc/firebugDebugger1.png)

3. Placez un point d'arrêt sur la première ligne de code du corps de la
fonction `afficheMonument` en cliquant dans la marge du
code :
![Firebug - point arret](http://qkzk.xyz/docs/doc04/doc/firebugDebugger2.png)

4. Rechargez la page. Celle-ci commence à être évaluée, comme
l'indique l'affichage du contenu de la balise `h1` puis
le traitement s'arrête et dans la zone Firebug la ligne sur laquelle
nous avions mis un point d'arrêt est surlignée. Dans la marge un
curseur en forme de triangle nous indique que le traitement du code
est en attente avant l'évaluation de cette ligne.
5. Dans la zone de droite de Firebug, activez
l'onglet **Pile**. Celui-ci indique par quel chemin (qui se lit
de bas en haut) on est arrivé à ce point d'arrêt. Vous pouvez
cliquer sur les noms pour accéder directement aux codes impliqués.
![Firebug - pile exécution](http://qkzk.xyz/docs/doc04/doc/firebugDebugger3.png)

6. Dans l'image ci-dessus on peut apercevoir un groupe de
boutons, située au-dessus de la zone contenant le code
Javascript. Passez en laissant un peu votre souris au-dessus de
chacun d'entre eux pour voir apparaitre leur rôle.
7. Nous
allons commencer par utiliser le troisième appelé **Pas à pas
détaillé**.

Appuyez sur ce bouton jusqu'à la fin du traitement de l'appel de
la fonction `afficheMonument` en cours (c'est-à-dire
jusqu'à l'affichage de la tour eiffel par le navigateur). Soyez
attentif à la séquence d'opérations exécutées et notamment à ce qui
se passe lorsqu'une fonction en appelle une autre et lors du "_retour_"
de cette fonction. Surveillez notamment le contenu de la
zone **Pile** sur la droite.
8. Recommencez jusqu'à affichage du Mont Saint-Michel.
9. Appuyez cette fois sur le second bouton
(appelé **Continuer**).
10. Placez un point d'arrêt sur la première ligne de chacune des 2
autres fonctions puis, en observant ce qui se passe, utilisez le
bouton **Continuer** jusqu'à afficher le chateau de Chambord.
Donnez une description de l'action de ce bouton.




**Meilleure pratique.**
Dans les règles de bonne pratique de
code il est universellement admis qu'il est
préférable de ne pas utiliser de valeur littérale ("constante")
"directement" dans le code. Un exemple de telle valeur est
le `17` utilisé pour fixer le facteur de zoom dans le
texte de l'url de l'image à afficher.
La recommandation de tous les programmeurs expérimentés est de nommer les
valeurs utilisées et de faire référence aux noms (on peut même placer
ces définitions dans un fichier "à part").






1. Chargez le
fichier [monuments-fonction-meilleurePratique.js](http://qkzk.xyz/docs/doc04/doc/monuments-fonction-meilleurePratique.js)
et
étudiez-en le code.
2. Quelles sont les données qui ont été nommées ? Où sont-elles utilisées ?
3. Faites une copie du fichier `monuments-version2.html`
et modifiez la partie `head` de la copie pour utiliser
ce fichier Javascript. Vérifiez que le comportement n'a pas été
perturbé.
4. Reprenez l'exercice avec les modifications sur le document
d'affichage des monuments avec cette version et comparez avec ce que
vous aviez dû faire pour les 2 autres versions. Peut-être cela vous
donne-t-il l'idée de créer d'autres données globales pour ce
document ? Faites le.




Cette pratique facilite la modification du code et en facilite le
"paramétrage". Cela évite par exemple d'avoir à rechercher dans le
code toutes les apparitions de cette valeur lorsque l'on veut faire
une modification (cf. `tailleImage` que l'on n'a plus qu'à
modifier une seule fois).


Faites les modifications demandées pour les 2 versions précédentes et
comparez le travail à faire dans chacun des cas :



1. passez le facteur de zoom de 17 à 16
2. modifiez la taille d'affichage des images de 400 à 500
3. modifiez le titre qui précède chaque monument :

  1. remplacez le texte _Monument _ par _Voici :_
  2. créez une feuille de style qui définit une classe CSS pour un
texte blanc sur fond bleu et affectée cette classe aux
éléments `h2` de titre des monuments
  3. ajoutez après le nom du monument ses
coordonnées GPS, par exemple pour avoir _La tour Eiffel se trouve aux
coordonnées (48.85826,2.294591)_








Nous avons déjà indiqué l'importance du choix des identificateurs pour
les variables, le choix du nom d'une fonction est tout aussi important, voire
plus. Celui-ci doit permettre à celui qui l'utilise de se faire une
intuition de ce que fait la fonction. Si cela ne lui évitera pas
de lire la documentation-spécification de la fonction pour bien
l'utiliser, le nom permet certainement de retrouver parmi toutes
celles qui existent la fonction qui a de bonnes chances de
correspondre à ce que l'on
cherche. Ainsi les noms de fonction `charAt`
ou `getYear` nous aident à imaginer leur rôle.
De même le choix `fahrenheitEnCelsius` est
certainement plus pertinent que `f`
ou `fahrcels` par exemple.








1. Dans un fichier `temperature.js` écrivez le code une
fonction `fahrenheitEnCelsius` qui prend un paramètre
numérique représentant une température exprimée en degré Fahrenheit et
a pour résultat la même température exprimée en degré Celsius.
2. Avez-vous rédigé la partie documentation ? Si non, c'est un
tort elle fait partie de la fonction et est tout aussi
indispensable que le code lui-même. Pourquoi selon vous ?
3. Ecrivez une page HTML qui utilise la définition de cette fonction
dans ce fichier pour, après avoir demandé une température en
Fahrenheit affiche la valeur en Celsius correspondante.
4. Testez.
5. Définissez la fonction qui réalise la conversion inverse et
testez-la également.






**Calcul de la date de Pâques.**
Le calcul de la date de
Pâques est loin d'être une chose si facile. La définition
actuelle de la date de Pâques est celle définie en 325 lors du
concile de Nicée : "_Pâques est le dimanche qui suit le
quatorzième jour de la Lune qui atteint cet âge au 21 mars ou
immédiatement après_". Le quatorzième jour de la Lune étant le
jour de la pleine Lune et le 21 mars correspondant à la date de
l´équinoxe de printemps.
L'_algorithme de Oudin_ permet le calcul de la date de pâques
pour une année donnée. Il est présenté ci-dessous sous sa forme
non simplifiée donc utilisable pour toute année postérieure à 1583
(après l'apparition du calendrier grégorien).

Dans la suite, RESTE représente le reste dans la division entière et QUO le quotient entier



* G = _annee_ RESTE 19
* C = _annee_ QUO 100
* D = C - C QUO 4
* E = (8 x C + 13) QUO 25
* I = (19x G + 15) RESTE 30
* H = (D - E + 19xG + 15) RESTE 30
* K = H QUO 28
* P = 29 QUO (H + 1)
* Q = (21 - G) QUO 11
* I = H - K x (1 - K x P x Q)
* J=(_annee_+_annee_ QUO 4 + I + 2 -D) RESTE 7
* R = 28+I-

Le résultat R représente le nombre de jours après le 1er mars
correspondant au dimanche de Pâques.
En Javascript l'opérateur RESTE se note `%`. S'il n'existe
pas d'opérateur prédéfini correspondant à QUO, on peut sur les
nombres positifs composer l'opérateur de division avec la fonction
`Math.floor` qui fournit la valeur arrondie par
défaut. En exploitant les conversions de type implicites de
Javascript (ici de `Float` vers `String`) on
peut aussi utiliser de manière détournée la fonction `parseInt` :

~~~javascript
var n = 12;
n % 3            //  0        // reste de la division de n par 3
n % 5            //  2
n / 5            //  2.4      // division flottante
Math.floor(n/5)  //  2        // valeur arrondie par défaut de la division flottante
parseInt(n/5)    //  2        // permet d'obtenir le quotient
Math.floor(n/3)  //  4
~~~





1. Dans un fichier écrivez le code d'une fonction qui prend pour paramètre une année
et a pour résultat le nombre de jours après le 1er mars de cette
année correspondant au dimanche de Pâques.
2. Ecrivez un document HTML qui utilise cette fonction pour

  1. afficher le nombre de jours qui sépare le dimanche de Pâques du
1er mars pour l'année en cours (reprenez ce qui a été vue sur le
type `Date` !)
  2. demander à l'utilisateur de fournir une année et affiche la même
information pour l'année fournie


3. Faites plusieurs tests et utilisez Firebug pour suivre pas à pas
l'exécution de votre fonction.






## Tests




Contrairement à ce que l'on peut peut-être penser dans une première
intuition, l'activité de programmation ne se limite pas à l'écriture du
code informatique du programme.

Ecrire un programme c'est aussi le
commenter (le spécifier) et le tester.

En cela les projets
informatique ne diffèrent pas de ceux dans d'autres domaines :
lorsque l'on produit une voiture on commence par en établir le cahier
des charges et on n'imagine pas ne pas en tester chaque composant (le
moteur, les freins, l'airbag, etc.).


Dans les manipulations qui ont été proposées depuis le début de
l'apprentissage de la programmation, il était demandé (quasi)
systématiquement de **tester**. Il est temps de revenir sur
cette phase fondamentale de l'activité de programmation qui avait
été annoncée dès l'introduction : la phase
de test. Une règle simple à retenir
et appliquer :


Tout code informatique écrit doit être testé.


Cela doit finalement être une évidence. Il est en effet naturel de s'assurer
que ce qui a été produit fonctionne conformément à ce qui était
prévu. Il n'est pas concevable de réaliser le branchement d'une prise
électrique sans en vérifier le bon fonctionnement.

Les programmes informatiques sont cependant des systèmes complexes où
les différents composants (fonctions par exemple) interagissent entre
eux. Ces interactions rendent très difficiles la construction de tests
complets permettant de s'assurer de leur bon fonctionnement. La
notion de test de programme est d'ailleurs une thématique de recherche
à part entière de l'informatique. Vous avez sûrement eu l'occasion
d'être confronté, déjà à plusieurs reprises, au dysfonctionnement de
programmes. Pourtant on peut imaginer que, dans la plupart des cas du
moins, leurs concepteurs ont apporté toute leur attention à leur
réalisation et les avaient testés avant de les diffuser.

Néanmoins, une première étape consiste à tester indépendamment chacun des éléments
programmés, chacune des fonctions, afin de vérifier que son
comportement correspond à sa spécification. Une des difficultés
lors de tests est de s'assurer que l'on parvient à vérifier tous les
cas de figure, y compris, et surtout, les cas particuliers sources
des erreurs non prévues. Plusieurs essais s'avèrent donc nécessaires,
avec différentes valeurs de paramètres bien choisies.


Vous devez et devrez donc systématiquement
procéder au test de chacune des fonctions que vous programmez.
