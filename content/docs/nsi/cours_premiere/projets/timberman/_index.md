---
title: "Timberman"
draft: false
---


# Timberman

L'objectif de ce mini projet est de mettre en pratique vos connaissances
sur les outils de base de Python (affectation, condition, boucles, fonctions,
listes) pour terminer une version très simple du jeu [_timberman_](http://www.jeux.fr/jeu/timberman).

![timberman](https://img.utdstc.com/screen/13/timberman.jpg)

Nous allons négliger tout l'aspect graphique pour nous concentrer sur les
dernières étapes : les fonctions qui font évoluer le jeu.

## Le jeu complet que vous devez obtenir

Dans la version "finale" de cette version, timberman est représenté par un
rectangle bleu à l'écran et l'arbre est représenté par un tronc et des branches
oranges.

Une barre de temps bleue diminue progressivement. Arrivée à 0 timberman meurt.

Pour gagner du temps (et des points) il tape le tronc. Les branches descendent.

S'il est heurté par une branche il meurt.

Il doit donc si situer du bon côté de la branche pour éviter de mourir.

Tout ce que le joueur peut faire est d'appuyer sur _Escape_ pour quitter,
_gauche_ pour taper à gauche et _droite_ pour taper à droite.

## État du projet que vous récupérez.

Le fichier [`timber_0.py`](/uploads/docsnsi/projets/timberman/timber_0.py) est déjà assez avancé. ([version sur github](https://github.com/qkzk/data_colab/blob/master/timber_0.py)).

En fait, pas tant que ça. Quand on débute un jeu, on part rarement de zéro.
On récupère souvent une version "précoce" d'un jeu précédent qu'on adapte.
Ce n'est pas toujours la meilleure pratique mais cela permet de commencer
rapidement.

Vous récupérez donc une version à "70%" du jeu.

Seules quelques fonctions sont à compléter.

Avant de vous décrire votre travail, examinons les éléments :

Le code est constitué d'un seul fichier constitué de plusieurs parties.

Chaque partie est découpée par des commentaires visibles, par exemple :

~~~python
###############################################################################
####################            IMPORTS                      ##################
###############################################################################
~~~

Le code se découpe ainsi :

## Description des éléments du fichier `timber_0.py`


### Imports

Les seuls imports dont on aura besoin sont :

* la fonction `choice` pour choisir au hasard un côté pour les branches qui
réapparaissent
* `pygame`

_Ils sont déjà faits_

### Constantes

Il est préférable de stocker dans des variables faciles à repérer les constantes
du jeu.

Python ne permet pas de créer de variable "constante", on peut toujours les
modifier plus tard si on veut !

Pour éviter de changer par erreur une constante (cela ferait certainement
planter le jeu) on donne aux constantes des noms en majuscule.

_Elles sont toutes déjà définies_

### Fonctions

Toutes les fonctions sont présentes.
Toutes les fonctions ont une description complète de ce qu'elles font.

Par contre, la majorité sont à compléter.

* Certaines sont totalement écrites (les plus difficiles),
* Certaines sont à compléter,
* Certaines sont à écrire complètement (les plus faciles).

Elles n'interviennent que plus tard, dans la boucle du jeu.

_Les fonctions sont votre travail_

Nous allons donc examiner le déroulement du jeu avant de parler de vos
consignes.

### initialisation du jeu

Pour que `pygame` puisse dessiner les éléments et faire avancer le jeu,
il faut créer quelques objets.

* On crée ici un objet `rect` qui servira à dessiner le tronc.
* Ensuite la liste des branches (toujours 3 à l'écran)
* Ensuite les coordonnées de timber. Seule son abscisse peut changer
* Ensuite quelques paramètres pour timber (le temps qu'il lui reste,
    est-il mort ou vivant ?, a-t-il bougé ?, son score)
* Enfin on initialise pygame.

_Cette partie est complète_

### Boucle infinie

Chaque tour du jeu se découpe en 3 / 4 parties (selon les jeux)

* récupérer les événements du vrai joueur (a-t-il enfoncé une touche ?),
* dessiner,
* calculer et mettre à jour.

#### Événements du joueur.

Seuls trois sont possibles, ce sont des événements clavier.

* **Escape** : quitte le jeu
* **Gauche** : tape depuis la gauche,
* **Droite** : tape depuis la droite.

_rien à coder ici_

#### Dessins

Tous les éléments sont dessinés un par un :

* le fond qu'on remplit de noir (pour effacer l'image précédente)
* le score
* le tronc
* les branches une par une à l'aide d'une boucle
* le bûcheron
* le chrono (afin qu'il soit devant les branches)

_Rien à coder ici_

#### Update

Dans cette partie on met à jour les derniers éléments :

* le score augmente régulièrement
* si le bûcheron à mis à coup,

    * on calcule la position des nouvelles branches
    * et on s'assure qu'il n'est pas mort (collision timber / branche du bas)
    * enfin, on lui donne du temps

* s'il est mort on arrête la boucle
* Enfin on met pygame à jour avec tous les nouveaux éléments. Tous les dessins
    apparaissent à l'écran à cette étape.
* et on fait avancer le temps.

_Rien à coder ici_

### Sortie du jeu

Pour sortir proprement, on affiche une dernière information : le score atteint.
Et on ferme le jeu en arrêtant pygame. A priori c'est inutile mais c'est
une bonne pratique.

## Cahier des charges

Ce que vous devez faire est simple :
**compléter les fonctions qui doivent l'être.**

* Chaque fonction est déjà définie
* Ses paramètres d'entrée sont complets, rien à ajouter
* Sa description est complète
* Ce qui manque est indiqué par un commentaire.


J'ai choisi de vous faire travailler sur différents aspects du jeu.

**Il faut donc que compreniez les étapes avant de vous lancer dans du code.**

### Fonction `drawText`

_Complète._

Tout ce qu'on fait est dessiner une chaîne de caractère dans une position
donnée.

### Fonction `chrono_dessiner`

_À écrire complètement_

Elle dessine un chronomètre sous la forme d'une barre bleue à l'écran.

La longueur de la barre est proportionnelle à la durée. Il faut d'abord la
calculer (pensez à un produit en croix...).

### Fonction `timber_deplacer`

_À compléter_

Il manque la nouvelle position et le nouvel objet `rect` du bûcheron.
La position dépend de la direction (`"gauche"` ou `"droite"`) et le `rect`
dépend de la position.

La suite est complète.

### Fonction `timber collision`

_À Compléter_

C'est, je pense, la fonction la plus difficile. Nous devons tester la collision
entre timber et la branche la plus basse. Les autres ne peuvent le toucher.

S'il y a collision, timber meurt (variable `timber_vivant`).

Pour éviter de planter le jeu, j'ai mis `timber_vivant = True`. Il faudra
bien sûr le modifier.

Pour tester la collision on va utiliser la méthode
[`colliderect`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect).
Cliquez sur ce mot pour atteindre les références.

C'est une méthode qui renvoit "True" si n'importe quelle partie de deux
rectangles se rencontrent.

Par exemple si `rect1` et `rect2` se touchent :

`rect1.colliderect(rect2)` vaut `True`

Sinon, cela vaut `False`.

### Fonction `timber_bonus_temps`

_À écrire presque complètement_

Pas grand chose à faire ici. Si le bucheron tape, il gagne du temps.
Son "chrono" est limité à une valeur maximale. Cela augmente un peu la
difficulté.

### Fonction `timber_diminuer_chrono`

_Donnée complétement_.

Pas très intéressante, donc je l'ai donnée. Timber perd du temps à chaque tour
et meurt si le temps arrive à 0.

**Petite question :** dans le code on teste :

~~~python
if timber_chrono <= 0:
  ...
~~~

Pourquoi `<= 0` et pas `== 0` ?

### Fonction `arbre_dessiner`:

_Donnée complétement_

On dessine bêtement le tronc et chaque branche. Pas intéressante.

### Fonction `arbre_deplacer`

_Une partie à compléter_

Toutes les branches doivent descendre d'un pas.

Détaillons le tableau des branches :

C'est une **liste à deux dimensions :**

des liste DANS une liste.

* Chaque branche est représentée par son coin supérieur gauche. `[abs, ord]`
* La première est forcement la plus basse.

Pour les faire descendre, on _augmente_ les ordonnées

Vous devrez donc faire une boucle qui parcourt le tableau et augmenter les
ordonnées.

_La fin est déjà traitée :_

si la branche du bas quitte l'écran, elle est enlevée du tableau et une
nouvelle apparaît en haut. Sa position est aléatoire.

## Extensions

Deux grands aspects sont négligés : les graphismes et l'animation.

* Pour les graphismes on peut utiliser des images (des sprites) pour le fond,
    timber, le tronc et les branches.
* Les animations sont plus délicates. Il faudrait modifier la boucle
  afin de dessiner les étapes du mouvement du bucheron et les branches qui
  quittent l'écran à l'opposé de sa frappe.


## Environnement de travail

Deux possibilités pour faire ce projet :

### Edition locale

Vous pouvez travailler sur un fichier source local que vous partagez avec
votre binôme via google drive.

Vous utilisez `Thonny` au lycée, ce que vous voulez chez vous.
Assurez-vous d'avoir installé la librairie `pygame` chez vous.

Installer une libaririe Python n'est pas difficile si Python est installé
correctement.
Une [référence](https://docs.python.org/fr/3.6/installing/index.html#basic-usage)

Vous pensez à partager manuellement le fichier après chaque session de travail
etc.

### Edition dans le cloud avec [repl.it](https://repl.it)

1. Rendez-vous sur [repl.it](https://repl.it) et connectez-vous.
2. "New repl", tapez "**pygame**".
3. Ensuite collez le code, assurez-vous qu'il tourne (RUN)
4. Activez le **multiplayer** (icone avec 2 bonhommes à gauche)
4. **Partagez ce repl avec moi (via mon adresse @lyceedesflandres habituelle)
    et avec votre binôme**.
5. Développez dedans. (Les deux élèves dans le même repl.) On doit voir
    apparaître deux curseurs avec les noms.

### Dans TOUS LES CAS

Vous envoyez un mail chaque semaine avec :

* votre avancée (terminé, ça bug là etc.)
* votre nom, le nom du binôme
* un lien vers le fichier (local ou dans le cloud)


## Quelques conseils

* Commencez par survoler le code afin de repérer les étapes
* Apprenez le fonctionnement voulu du jeu (en testant quelques cas dans le vrai jeu)
* Faîtes un schéma très rapide des différents éléments
* Relisez bien la description des éléments du cahier des charges et de ce que
    les fonctions doivent faire.
* Si vous pensez avoir compris, vous pouvez commencer à programmer.
