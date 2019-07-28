---
author: qu3nt1n
date: 2017-06-15 17:05:59+00:00
draft: false
title: '4.ter - 2 : parcourir un graphe'
weight: 2

---

## Introduction


Parce que c'est une partie difficile, **commençons par un jeu.**

Voici ce que vous allez faire :

Vous partez de la page d'accueil [wikipedia.fr](https://fr.wikipedia.org/)
Vous devez parvenir à [cette page](https://fr.wikipedia.org/wiki/Leonhard_Euler) en ne cliquant que sur des liens internes à wikipedia
Vous n'avez pas le droit d'en sortir, seulement de cliquer sur des liens de la page.
Vous n'avez pas le droit non plus de taper quoi que ce soit ni d'utiliser autre chose que des clics sur des liens internes.

En quelques essais vous parviendrez peut-être à votre destination. Peut-être est-elle impossible à atteindre ?

C'est possible en trois clics. Qui dit mieux ?

Pourrions nous trouver une méthode parcourant tous les chemins partant de la page de départ et qui réponde à la question : est-ce possible ?

La tâche parait complexe et l'est réellement. Différentes méthodes sont envisageables et nous allons en présenter deux.

**Commençons par introduire les bons outils.**

Un **graphe** est constitué de sommets et d'arc. Dans notre exemple les sommets sont les pages et les arcs les liens.
En l'occurence ils sont orientés, un lien part d'une page 1 vers une page 2.
Peut-être qu'aucun lien n'existe entre la page 2 et la page 1...

Un arbre est un graphe particulier, les arcs vont dans un sens précis et aucune boucle n'est possible.

Deux arbres identiques sont représentés ci-dessous. Remarquons que seule la numérotation change. A ce détail près ils sont identiques.

![graphes_figures (1)](http://qkzk.xyz/wp-content/uploads/2017/06/graphes_figures-1.png)


Imaginons partir du sommet 1 et chercher à parcourir tout l'arbre à la recherche d'un sommet particulier. On peut se représenter cette démarche comme le parcours d'un utilisateur cherchant un fichier particulier dans ses dossiers depuis la racine de son disque dur. Il pourrait lancer une recherche (qui fera peut-être la même chose - mais d'autres méthodes plus efficaces existent) mais il décide de chercher "à la main".

**Il parcourt les sommets dans l'ordre indiqué sur chacun des deux schémas : 1-2-3-4-5.**

**Dans le schéma de gauche il va d'abord parcourir tous les sommets d'un même niveau de profondeur.**
** Dans le schéma de droite, il va explorer toutes les branches jusqu'au bout avant d'en changer.**

On parle de **parcours en largeur** ou de **parcours en profondeur**.

Nous allons mettre en place des algorithmes de parcours en largeur et en profondeur dans les cas des arbres simples (sans cycles, sans retour, avec un seul sens) puis dans le cas de graphes ayant peut-être plusieurs connexions entre les sommets.

L'exemple ci-dessous (graphe3) présente un graphe avec des cycles possibles (1,2,3,1) ou (1,4,3,2,1) etc.

![graphes_figures (2)](http://qkzk.xyz/wp-content/uploads/2017/06/graphes_figures-2.png)


Le parcourir présentera une difficulté supplémentaire : il est possible de passer plusieurs fois par le même sommet. Nous verrons donc comment l'éviter.


## I. Parcours en largeur.


Fixons la situation.
Un arbre avec n sommets. On en choisit un sommet de départ et on parcourt tout l'arbre **en explorant tous les sommets de même profondeur d'abord**.
La profondeur du sommet B depuis le sommet A est le nombre d'arc qu'il faut emprunter pour rejoindre B depuis A.
Dans l'exemple 1, les sommets 2 et 3 ont une profondeur 1 depuis le sommet 1 et les sommets 4 et 5 ont une profondeur 2 depuis le sommet 1.
**Nous souhaitons donc que notre algorithme nous renvoie la liste des sommets qu'il parcourt et s'arrête une fois l'exploration terminée.**

parcoursLargeur(arbre1, 1) renvoie donc [1,2,3,4,5].

et parcoursLargeur(arbre2, 1) renvoie donc [1,2,4,3,5]

Pour l'exemple 4 ci-dessous, nous aurons donc :
parcoursLargeur(arbre4, 1) qui renvoie [1,2,3,4,5,6,7]

![graphes_figures (3)](http://qkzk.xyz/wp-content/uploads/2017/06/graphes_figures-3.png)



### 1. Représenter les arbres en Python.


Il existe mille et une manière de représenter les arbres en Python et nous allons en présenter une très simple. Elle consiste à noter un sommet, par exemple 1 et la liste des sommets avec qui il est lié.
Si les arcs sont orientés il faut faire attention mais si ce n'est pas le cas on peut se contenter de les noter de haut en bas.
Son avantage est qu'elle est simple, son inconvénient est qu'elle peut-être lourde.

Etant donné que nous n'allons travailler qu'avec des arbres simples, cela ne pose pas de problème.

On utilsera donc un object dictionnaire qui permet d'avoir un ensemble de clé, key en anglais, et de valeurs, values en anglais.

Pour l'arbre4 cela donne :

![graphes_figures (3)](http://qkzk.xyz/wp-content/uploads/2017/06/graphes_figures-3.png)


_arbre4 = {1:[2,3],2:[4,5],3:[6,7],4:[],5:[],6:[],7:[]}_
Remarquons qu'on note les arcs comme s'ils étaient orientés du haut vers le bas.

Pour le graphe3 :

![graphes_figures (2)](http://qkzk.xyz/wp-content/uploads/2017/06/graphes_figures-2.png)

_graphe3 = {1:[2,3,4],2:[3],3:[4],4:[]}_

A nouveau on n'a noté qu'une seule fois chaque arc.
On pourrait noter :
_graphe3 = {1:[2,3,4],2:[1,3],3:[1,2,4],4:[1,3]}_
qui est plus lourd mais représente bien le même graphe.


### Le parcours en largeur pour les arbres


Rappelons qu'on ne note qu'une fois les arcs et toujours en partant du haut de l'arbre.

_ParcoursLargeur(arbre B, Somme s):_
_ f = listevide_
_ ajouter s à f_
_ afficher s_
_ tant que la liste f est non vide:_
_ enlever le premier élément de f noté s_
_ pour tout voisin t de s dans B:_
_ on ajoute t à la fin de f_
_ on affiche t_
Tester à la main sur les arbres 1 et 4 et s'assurer que l'algorithme produit bien le résultat escompté.

Il ne reste plus qu'à écrire nos objets arbre1, arbre4 et à programmer l'algorithme.

_arbre1 = {1:[2,3],2:[4],3:[5],4:[],5:[]}_
_arbre4 = {1:[2,3],2:[4,5],3:[6,7],4:[],5:[],6:[],7:[]}_

Solution en Python :

~~~python
    def parcoursLargeur(arbre, sommet):
    f = []
    f.append(sommet) # ajoute à la fin de la liste
    print sommet
    while len(f)>0:
    s = f[0]
    f = f[1:]# notation qui prend tous les elements de f à partir de l'element 1
    print s
    for t in arbre[s]:
    print t
    f.append(t)
~~~

Tester cette fonction sur nos arbres1 et arbres4.


### Le parcours en largeur pour les graphes


On peut se convaincre (mais un essai est bienvenu) qu'elle ne fonctionne pas pour les graphes présentant un cycle. Elle va tourner indéfiniment sur graphe3 sans jamais s'arrêter.

Comment remédier à ce problème ?

Il suffit de noter régulièrement les sommets déjà parcourus et de s'interdire d'y retourner si on en rencontre un.

Proposer une version corrigée de _parcoursLargeur_, notée _parcoursLargeur2_ qui réponde à ce problème.


## II. Parcours en profondeur.


C'est l'autre méthode classique de parcours des graphes : on explore les chemins jusqu'au bout d'abord. Pour résoudre immédiatement le problème des cycles, on s'interdira de repasser par un sommet déjà visité.

Pour notre arbre4 cela donne : 1,2,4,5,3,6,7

![graphes_figures (3)](http://qkzk.xyz/wp-content/uploads/2017/06/graphes_figures-3.png)


Sa mise en oeuvre la plus simple nécessite **une récursion** : la fonction s'appelle elle même.
Si on oublie de noter régulièrement les sommets visités et qu'un cycle est présent (comme dans le graphe3) alors on va parcourir indéfiniment le même cycle :
Pour graphe3 : 1,2,3,1,2,3,1 etc.
Il est alors impossible d'atteindre le sommet 4.

L'algorithme se présente ainsi :

_explorer(graphe G, sommet s)_
_ marquer le sommet s_
_ pour tout sommet t voisin du sommet s_
_ si t n'est pas marqué alors_
_ explorer(G, t)_

**Consigne :** à vous de le programmer dans votre langage (Python ou JS) !
Testez le abondamment sur les exemples plus haut.


### III. Quelques compléments sur les graphes.


La théorie des graphes a été inventée par **Leonard Euler** pour résoudre le problèmes des 7 ponts de Königsberg.

_La ville de Königsberg (aujourd'hui Kaliningrad) est construite autour de deux îles situées sur le Pregel et reliées entre elles par un pont. Six autres ponts relient les rives de la rivière à l'une ou l'autre des deux îles, comme représentés sur le plan ci-dessus. Le problème consiste à déterminer s'il existe ou non une promenade dans les rues de Königsberg permettant, à partir d'un point de départ au choix, de passer une et une seule fois par chaque pont, et de revenir à son point de départ, étant entendu qu'on ne peut traverser le Pregel qu'en passant sur les ponts. _(cf wikipedia)

Euler démontre très simplement que la réponse est non. Il suffit de compter intelligemment (comme toujours avec Euler) les arcs et les sommets pour s'apercevoir qu'un tel cycle n'existe pas.

Ce problème a ouvert une autre branche des mathématiques, elle aussi très féconde : la **topologie** (l'étude des formes et de leurs propriétés).

Les graphes sont omniprésents en informatique et dans toute théorie de l'information.
Certains problèmes de théorie des graphes (par exemple [le voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce)) n'ont pas de solution simple et c'est encore de nos jours un problème majeur.

En spécialité mathématiques on étudie l'[algorithme de Djikstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) qui permet de déterminer le plus court chemin reliant deux sommets. On doit supposer que certains arcs ont des poids (pensez à la longueur totale d'une route ou à un temps de transport entre deux villes).
D'autres algorithmes plus efficaces sont employés couramment, par exemple google maps propose un trajet efficace qui n'est pas forcement le meilleur pour relier deux villes. Le célèbre [algorithme A*](https://fr.wikipedia.org/wiki/Algorithme_A*) est un bon exemple de recherche à la fois efficace (mais pas toujours optimale !) et simple à mettre en oeuvre.

S'il voulait trouver absolument le meilleur il devrait sans doute parcourir énormément de chemins possibles... mais s'il ne cherche qu'un très bon chemin alors il peut limiter son parcours à des trajets cohérents (= qui le font s'approcher du but).

La théorie des graphes est encore un domaine de recherche très actif en mathématique, et en informatique car elle est appliquée partout : intelligence artificielle, chimie, physique théorique, biologie, logistique, télécommunication, cartographie etc.

On peut citer le fameux **[théorème des 4 couleurs](https://www.youtube.com/watch?v=g_nTfZ9OgJs) :**
Le théorème des quatre couleurs indique qu'il est possible, en n'utilisant que quatre couleurs différentes, de colorier n'importe quelle carte découpée en régions connexes, de sorte que deux régions adjacentes (ou limitrophes), c'est-à-dire ayant toute une frontière (et non simplement un point) en commun reçoivent toujours deux couleurs distinctes.
cf Wikipédia

Conjecturé en 1852, toutes les démonstrations connues à ce jour est nécessitent la vérifications de milliers de cas critiques par un assistant de vérification de preuves (utilisant lui même la théorie des graphes !). Elle est loin de faire l'unanimité au sein de la communauté scientifique étant donné qu'aucun humain n'est capable de suivre une telle quantité de calculs.

Ce théorème a des applications surprenantes et que vous utilisez en permanence :



* Affecter des fréquences différentes à des cellules voisines dans un réseau de téléphone mobile GSM.
* Organiser un examen suivant les matières que doit passer chaque étudiant. Comment mettre en parallèle plusieurs épreuves sans léser un candidat ?
* Optimiser l'utilisation des machines de travail. Comment mettre en parallèle des fabrications utilisant plusieurs machines ?
* Problème d'incompatibilité. Comment faire cohabiter des personnes ou des animaux en tenant compte de leur incompatibilité ?
* La résolution du Sudoku peut se ramener à un problème de coloration de graphe.

[Solution des problèmes présentés plus haut](https://drive.google.com/open?id=0B4Mq2ZGzUQ3VNWN1NUo3T193TDQ)
