---
author: qu3nt1n
date: 2016-07-02 10:05:25+00:00
draft: false
title: 4.07 Fonctions et environnement
weight: 7
---

Notions abordées dans cette page



* variables, environnements et _locals_
* portées







## Fonctions et environnement


Les manipulations réalisées avec nous ont permis de visualiser la séquence de
traitement du code exécuté. Il est également possible à tout moment
de visualiser le résultat de ces traitements et l'état de
l'environnement d'exécution et son évolution :


Les notions présentées ici ne sont sans doute pas si évidentes. Cela
vaut certainement la peine de faire les manipulations au vidéo-projecteur
avec toute la classe et de solliciter au fur et à mesure les réactions
des élèves afin d'engager la discussion sur ce qui est observé et en
dégager collectivement les règles de portée.








1. Activez, si besoin, Firebug et rechargez le document [version 2](/uploads/docs/doc04/doc/monuments-version2.html).
2. S'il n'y est plus replacez un point d'arrêt sur la première ligne de code du corps de la
fonction `afficheMonument`, et supprimez les éventuels autres.
3. Sélectionnez ensuite l'onglet **Espions** dans la zone
droite (à côté de l'onglet **Pile** déjà utilisé).
4. Rechargez la page et étudiez le contenu de cet onglet. Qu'y trouve-t-on (on laissera de côté les
éléments `this` et `Fenêtre`) ?
5. Tout en observant l'évolution du contenu de cet onglet, faites du
pas-à-pas de traitement jusqu'à affichage de la tour
Eiffel. Qu'avez-vous observé ?
6. Que représente la quantité **arguments** que vous avez pu observer ?
7. Quel lien existe entre les paramètres formels et les
paramètres effectifs ?




Vous avez pu constater que le contenu de cet onglet permettait de
consulter les valeurs des variables et des paramètres des
fonctions. On observe à chaque instant l'état des
couples _(identificateurs, valeurs)_, c'est-à-dire l'état de
l'environnement d'évaluation. On remarque que le contenu de
l'environnement évolue, tant dans sa composition que dans les valeurs
qu'il contient. L'environnemment avait initialement été présenté
comme l'ensemble des variables définies, on constate qu'il faut lui
ajouter les liaisons entre les paramètres formels et les paramètres
effectifs.


Faites une copie du
document `monuments-version2.html` et
du fichier de script `monuments-fonction.js`. Dans cet
exercice vous travaillez avec ces copies.



1. Modifiez la copie de `monuments-version2.html` pour
qu'elle utilise la copie du fichier de script.
2. En consultant le code des 3 fonctions définies dans le
fichier `monuments-fonction.js`, on peut remarquer que
dans le code de chacune d'entre elle on trouve la définition d'une
variable appelée `texte`. Recommencez le pas-à-pas
jusqu'à la Tour Eiffel en vous concentrant sur les valeurs prises
par ces différentes variables nommées `texte`
3. Si besoin
répétez votre observation avec l'affichage des images
suivantes.
4. Selon vous, si dans l'une de ces
fonctions, `texteMonument` par exemple, on renomme la
variable `texte` en `texteResultat`, cela
change-t-il quelque chose ?
Si oui, quoi ? Si non, pourquoi ?
Faites-le pour vérifier votre réponse (attention à bien renommer
toutes les occurrences de la variable).
5. Ajoutez à la fin de la portion `script` du
fichier `monuments-version2.html` la ligne

~~~javascript
document.writeln("valeur de texte = "+texte);
~~~



6. Chargez votre document et consultez la **Console** de Firebug.
Quelle conclusion en tirez-vous ?
7. Déduisez de ces dernières observations une règle sur la portée des
variables définies dans une fonction.




Nous venons de découvrir une autre règle de portée des
variables.


Les variables définies dans une fonction
sont locales à cette fonction. Elles ne
sont pas définies en dehors de cette fonction. On parle
de portée locale.


Et qu'en est-il des variables définies en dehors des fonctions ?


On poursuite la manipulation précédente :



1. Ajoutez au début de la portion `script` du
fichier `monuments-version2.html` la ligne


      var globale = "une valeur quelconque";



Cette variable est-elle définie dans la
fonction `afficheMonument` (et dans les autres) ?
Quelle est sa valeur ?

(Vous pouvez éventuellement demandez l'affichage de la valeur de
cette variable dans cette fonction, que se passe-t-il ?)
2. Déduisez-en une règle sur la portée des variables définies en
dehors des fonctions.






Les variables définies en dehors de toute
fonction sont globales. Elles sont
toujours définies et accessibles.


Il est légitime de se demander ce qui se passe lorsque l'on utilise le
même identificateur pour définir une variable globale et une
varibale locale. On crée un **conflit** de nom, comment est-il
géré par le langage ?




Reprenez le document [version 2](/uploads/docs/doc04/doc/monuments-version2.html) dans sa version initiale.



1. Ajoutez au début de la portion `script` du
fichier `monuments-version2.html` la ligne


      var texte = "une valeur quelconque";



et à la fin la ligne


     document.writeln("valeur de texte = "+texte);




2. Chargez le document, supprimez tous les points d'arrêt existant et
placez-en un nouveau sur la ligne ajoutée :


      var texte = "une valeur quelconque";




3. En procédant pas-à-pas observez
l'évolution du contenu de `texte` au cours du
traitement.
4. Dans la fonction `texteMonument` renommez la variable
locale `texte` en `resultat` (par
exemple).
Recommencez le pas-à-pas jusqu'à arriver au début du traitement
de cette fonction. La variable `texte` n'apparaît pas dans
la zone **Espions** qui n'affiche par défaut que les définitions
locales, mais il est possible de corriger cela :
dans cette zone cliquez sur "_Nouvelle expression
espion..._" et saisissez `texte` pour connaître la
valeur de cette variable.
5. Que constatez-vous ?
6. Pour vérification créez un "espion" pour une variale qui n'existe
pas, `truc` par exemple, quelle est sa valeur ?
7. Des observations précédentes établissez la règle qui résoud le
conflit de nom entre vairables globales et locales.




On constate qu'en cas de conflit de njom la variable locale prend le
pas sur la variable globale tant qu'elle est définie. Mais la variable
globale conserve et "retrouve" sa valeur une fois que l'on quittte la
portée de la définition locale.


Les définitions locales l'emportent sur les
définitions globales. On dit qu'il y
a masquage de la variable globale
par la variable locale de même nom.


Les bonnes pratiques de programmation recommandent de limiter au
maximum l'usage des variables globales. Il faut les réserver pour
définir des valeurs dont l'existence a un sens pour l'application
dans son ensemble.
L'utilisation de variables globales ne doit pas remplacer le rôle des
paramètres des fonctions.
