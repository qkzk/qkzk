---
title: Architecture
author: qkzk
theme: metropolis
# mainfont: Noto Sans CJK JP
---

# Diapos du cours

1. [intro](/uploads/docsnsi/architecture/diapos/1_intro-Beamer.pdf)
2. [composants](/uploads/docsnsi/architecture/diapos/2_composants-Beamer.pdf)
3. [performances](/uploads/docsnsi/architecture/diapos/3_performances-Beamer.pdf)
4. [assembleur](/uploads/docsnsi/architecture/diapos/4_assembleur-Beamer.pdf)

# Videos

1. la [video Comparaison](/uploads/docsnsi/architecture/videos/Comparing.mp4) et les [soustitres](/uploads/docsnsi/architecture/videos/Comparing.srt)
2. la [video Breadboard](/uploads/docsnsi/architecture/videos/breadboard.mp4) et les [soustitres](/uploads/docsnsi/architecture/videos/breadboard.srt)

# Historique de la machine

## Préhistoire informatique

* Compter : les doigts, les orteils et des outils.
* Concevoir des machines pour réaliser des calculs (_calculi_ mot latin qui signifie "cailloux").
    **Exemple** : Le _boulier_, découvert indépendamment par de nombreuses civilisations




![Boulier](/uploads/docsnsi/architecture/img/boulier3.jpg)

## Antiquité : naviguer

![La machine d'Anticythère](/uploads/docsnsi/architecture/img/anticythere_4.jpg)
![Reconstituée](/uploads/docsnsi/architecture/img/anticythere_5.png)

--------------------------

La machine d'Anticythère, découverte en 1900 et datant de -87 avant J.-C.  servait à calculer les positions astronomiques et donc à **naviguer**

Elle démontre que :

* Calculer a toujours été une entreprise importante
* L'homme s'est toujours montré d'une très grande ingéniosité pour y parvenir

## Renaissance : Blaise Pascal

**Blaise Pascal**. Scientifique et penseur français du XVIIe siècle

* En physique : le _théorème de Pascal_ qui exprime les variations de pression dans un fluide
* En mathématiques : _calcul infinitésimal_, _raisonnement par récurrence_ etc.
* En philosophie et littérature : les _Pensées_ (1669)
* En ingénierie : la _Pascaline_. Première machine à calculer. Inventée à 19 ans pour aider son père devant remettre en ordre les recettes fiscales d'une province.

##  La pascaline

### ![La Pascaline](/uploads/docsnsi/architecture/img/pascaline_2.jpg)

## Gottfried Wilhelm Leibniz

**Leibniz** (1646 - 1716) est un penseur allemand fait progresser la philosophie, les mathématiques, la physique et l'ingénierie autant que Pascal.

Il améliore la Pascaline et redécouvre le système **binaire**.

Néanmoins on n'utilisera réellement le binaire qu'après 1945.

## Premières machines programmables : métiers à tisser

**Joseph Marie Jacquard** (1752-1834) améliore des principes déjà existants pour concevoir une machine à tisser utilisant les cartes perforées de **Jean-Baptiste Falcon.**

### ON S'EN FOUT C'EST VIEUX !

Les métiers Jacquard sont encore utilisés dans le médical pour réaliser des coudières, genouillères et prothèses d'artères. Et c'est produit en France.

![Cartes perforées](/uploads/docsnsi/architecture/img/cartes_perforees_2.jpg)

## Machine à calculer programmable

**Charles Babbage** constatant que les erreurs de calculs dans les tables conduisent à de nombreuses catastrophes invente en 1833 le concept de _machine (Difference Engine 1)_ permettant d'automatiser le calcul.

Il correspond ensuite avec **Ada Lovelace** (comtesse et fille du poète Lord Byron). Elle conçoit les premiers programmes pour cette machine. Elle est vue comme la première programmeuse du monde.

Trop complexe, trop coûteuse la machine de Babbage ne verra jamais le jour.

## Ada Lovelace

![Nombres de Bernoulli](/uploads/docsnsi/architecture/img/lovelace_bernoulli_2.jpg)

![Ada Lovelace](/uploads/docsnsi/architecture/img/ada_lovelace_2.jpg)

## Électricité

La révolution industrielle de la fin du XIXe siècle conduit à l'apparition de l'électricité et des moteurs qui améliorent les machines à calculer.

Par exemple, aux USA, **Herman Hollerith**, conçoit une machine qui divise par deux le temps nécessaire au recensement de la population. Sa société fusionnera pour devenir IBM.

## XXe siècle : un essor fulgurant

* Avant 1936 : première machine capable de _parallélisme_
* 1936 : **Alonzo Church** et **Kurt Gödel** fournissent un cadre théorique et Alan Turing propose un concept théorique de machine qui est encore utilisé.
* Seconde guerre mondiale. L'information est chiffrée et circule alors massivement via les ondes radio et le télégraphe. Le déchiffrement devient un enjeu mondial.
Citons Enigma, utilisée par les allemands, déchiffrée par Turing grâce à _la bombe_.

## Enigma et la bombe

![Enigma](/uploads/docsnsi/architecture/img/enigma_2.jpg)

![La Bombe](/uploads/docsnsi/architecture/img/bombe_2.jpg)

## ENIAC

Les machines sont encore colossales !

* ENIAC : 30 tonnes, 167 m$^2$, 160 kW pour 100 kHz et 100 000 additions par secondes.

* Programme sur cartes perforées, entièrement électronique. Servant au calcul balistique. Programmé par six femmes.

* Calcul d'une trajectoire d'une table de tir. Comparatif :

~~~
      Moyen                         Temps
      Homme à la main               2,6 j
      Avec une machine à calculer    12 h
      Model 5 (concurrent ENIAC)     40 min
      ENIAC                           3 s
      PC ~2000                       30 µs
~~~

## l'ENIAC : un monstre

###![l'Eniac](/uploads/docsnsi/architecture/img/eniac_2.jpg)

# Modèle de Von Neumann

## Un esprit universel
**John Von Neumann** : ingénierie, logique, mathématiques... Participa au projet Manhattan (première bombe atomique) et à l'ENIAC

Il propose en 1944 un modèle _d'architecture_ novateur qui sert toujours de base à nos architectures actuelles.

### ![Von Neumann](/uploads/docsnsi/architecture/img/timbre_2.jpg)

## Présentation du modèle de Von Neumann

### ![Modèle original](/uploads/docsnsi/architecture/img/modele-originel2.gif)

* **Unité de commande** : contrôle la séquence d'instruction
* **Unité arithmétique** : exécution de ces instruction
* **Processeur** : réalise les calculs
* **Mémoire** : contient les données et **les programmes**
* **Entrées** : clavier, cartes perforées, etc.
* **Sorties** : affichages, imprimantes, écran

## Aujourd'hui : évolutions du modèle de Von Neumann

### ![Modèle actuel](/uploads/docsnsi/architecture/img/modele-actuel.gif)

* **Entrée-sorties** : contrôlées par des processeurs autonomes
* **Multiprocesseur** : unités séparés ou multiples coeurs dans une même puce. Augmentation de la puissance sans augmenter la vitesse des processeurs, limitée par les capacités d'évacuation de chaleur
* **La mémoire au coeur du système** et de plus en plus de **parallélisme**.

## L'assembleur, le C, Python

* 1954 : premier langage **assembleur** par IBM. Il sert d'intermédiaire entre le programme (_pour i allant de ..._) et le langage machine (_...01011001..._).
    Cela reste une langage très bas niveau (proche du métal)
* 1972 : Dennis Ritchie et Ken Thompson développent **le langage C** pour programmer le système d'exploitation **UNIX**. Rapide, à la syntaxe lisible, il est rapidement adopté.
* 1989 : Guido van Rossum crée Python qui deviendra le langage de script de référence.

## Séquencement d'une instruction : Python, C, assembleur
Partons d'un programme simple et regardons sa traduction en langage machine

Les premiers nombres de la suite de Fibonacci en Python

~~~Python
x = 0
y = 1
while x < 255:
  print(x)
  x, y = y, y + x
~~~

----------------------------

Et en C

~~~C
      # include <stdio.h>
      int main(void){
        int x, y, z;
        while(1){
          x = 0;
          y = 1;
          do{
            printf("%d\n", x);
            z = y + x;
            x = y;
            y = z;
          } while (x < 255);
        }
      }
~~~

---

En assembleur

* google drive : /dev/nsi/architecture matérielle : Vidéo avec soustitres fr
* La [video](https://www.youtube.com/watch?v=yOyaJXpAYZQ) de Bean Eater

# Systèmes d'exploitation

## Présentation

![système d'exploitation](/uploads/docsnsi/architecture/img/os.png)
Le système d'exploitation est un intermédiaire entre les logiciels d'application et le matériel

## Fonctionnalités

l'OS permet l'utilisation des applications utilisant les ressources de la machine.

* **Exécuter des programmes**
* **Partager les ressources** entre usagers, entre programmes
* Ressources :
    * **Périphériques** : chaque périph. a ses propres instructions
        Évite au programme de devoir écrire les siennes
    * **Fichiers** : tient compte du format de chaque fichier, protège les fichiers (droits d'utilisateurs)
    * **Détection, récupération d'erreurs**
    * **Contrôle** : surveillance des performances, des ressources etc.

## UNIX vs Windows

On distingue deux grandes familles de systèmes d'exploitation : UNIX et windows.

Parmi UNIX on trouve, en particulier :

* macOS,
* GNU/Linux
* Android
* iOS
* FreeBSD, NetBSD etc.

---

### Répartition

* **Ordinateurs personnels** : Windows (90% de part depuis 15 ans)
* **Mainframes et serveurs** : Linux, UNIX. (beaucoup de virtualisation depuis 10 ans)
* **Mobile** : Android (90% des smartphones)

## UNIX et le Libre

Développé au Bell Labs dans les années 1960, UNIX s'est rapidement séparé en de nombreuses variantes (BSD, Solaris etc.) et de nombreux procès de propriété intellectuelle ont compliqué son développement dans les années 80/90.

Dès les années 80 **Richard Stallman** commence le développement de GNU.

En 1991 **Linus Torvald** crée le premier noyau linux à partir de GNU. Le succès est immédiat.

* GNU/Linux est un logiciel **open source** : le code source est consultable, éditable, utilisable etc. Des dizaines de milliers de développeurs ont participé à ce projet via [internet](https://github.com/torvalds/linux)

Cela s'oppose aux **sources fermées**, généralement propriété des entreprises.

## Linux : Kernel et distribution

* Le noyau (**kernel**) d'un système UNIX comporte les fonctions de base du système d'exploitation. Il fournit aux logiciels l'interface de programmation pour utiliser le matériel
* le kernel est multitâche et multi-utilisateur. Il respecte les normes POSIX et ses programmes peuvent (ou devraient) fonctionner sur tous les systèmes UNIX
* La **distribution** est l'ensemble des logiciels qui s'ajoutent au noyau et rendent l'ordinateur utilisable. Par exemple : Ubuntu (PC), Raspbian (Raspberry Pi) ou Android (mobile)

## Utilisation courante : CLI vs GUI

### Command Line Interface

L'utilisateur tape dans un terminal ses commandes directement. Courante en informatique embarquée, administration de serveurs ou à distance

### Graphical User Interface

Les fenêtre auxquelles nous sommes habitués. Le gestionnaire de fenêtre n'est qu'un programme qu'on peut changer rendant l'expérience utilisateur totalement différente.

## Quelques préjugés

* _Linux c'est galère._

    Au début. Ensuite c'est difficile de faire machine arrière. Chez moi personne ne le remarque. Essayez une machine virtuelle !

* _C'est impossible de jouer ou d'utiliser tel logiciel sous linux._

    Impossible non, compliqué oui. Certains programmes (la suite adobe, solidworks) n'existent simplement pas sous linux mais ont des alternatives.
    Mon conseil est de garder un dualboot avec windows.

* _Linux c'est moche._

    Là c'est faux, vous en faites ce que vous voulez.
* _Ça ne sert à rien._

    Faux encore, ça sert à apprendre et pour programmer c'est bien mieux. Ensuite, et plus important, ça vous rend le contrôle de **votre** machine.


<!-- Poursuivre l'historique SEULEMENT des réseaux, cours sur les réseaux sans aspect historique -->
# Réseaux

## Préhistoire des réseaux : Arpanet

## TCP / IP

## Internet

## Wifi, bluetooth

## Objets embarqués

# I/O

## Périphériques d'entrée et de sortie

## Interface Homme Machine
