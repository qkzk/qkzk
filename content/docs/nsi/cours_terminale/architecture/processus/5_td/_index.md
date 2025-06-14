---
title: "Processus - TD"
bookCollapseSection: false
weight: 5
---

[pdf](/uploads/docnsitale/processus/td_processus.pdf)

**Compétence :** Appliquer l'algorithme d'ordonnancement du plus court d'abord.

## Exercice 1

Les 3 processus doivent être exécutés simultanément sur un ordinateur à un
seul microprocesseur.

| Processus 1   | Processus 2   | Processus 3   |
| ------------- | ------------- | ------------- |
| instruction 1 | instruction 1 | instruction 1 |
| instruction 2 | instruction 2 | instruction 2 |
| instruction 3 | instruction 3 | instruction 3 |
| instruction 4 |               | instruction 4 |
| instruction 5 |               | instruction 5 |
| instruction 6 |               |               |
| instruction 7 |               |               |

L'ordonnanceur du système d'exploitation utilise la technique "du plus court
d'abord".

Schématiser l'ordre de traitement des instructions des 3 processus.

**Compétence :** Appliquer l'algorithme d'ordonnancement en tourniquet.

## Exercice 2

Schématiser l'ordre de traitement des instructions des 3 processus pour un
ordonnancement en tourniquet.

**Compétence :** _Appliquer l'ordonnancement premier entré, premier sorti_

## Exercice 3

Schématiser l'ordonnancement des tâches d'impression soumises par des
ordinateurs d'un réseau local sur une imprimante connectée et partagée
sur ce réseau.

- 5 ordinateurs (A, B, C, D et E) et une imprimante P sont raccordés à un même commutateur (switch)
- On suppose que la file d'impression est vide au départ. Tous les temps indiqués
  ci-dessous sont mesurés après le départ :

  | Ordinateur | nom du document | horaire d'envoi du document |
  | ---------- | --------------- | --------------------------- |
  | **A**      | cours1.pdf      | 01:30                       |
  | **A**      | cours2.pdf      | 01:45                       |
  | **B**      | image1.jpg      | 00:10                       |
  | **C**      | chanson.doc     | 01:00                       |
  | **C**      | roman.pdf       | 01:10                       |
  | **D**      | plan.jpg        | 00:45                       |
  | **D**      | formation.pdf   | 01:05                       |
  | **E**      | carte.pdf       | 00:30                       |
  | **E**      | metro.pdf       | 01:20                       |

**Compétence :** _Détecter une situation d'interblocage_

## Exercice 4

Sept processus Pi sont dans la situation suivante par rapport aux ressources Ri :

- P1 a obtenu R1 et demande R2
- P2 demande R3 et n’a obtenu aucune ressource tout comme P3 qui demande R2
- P4 a obtenu R2 et R4 puis demande R3
- P5 a obtenu R3 et demande R5
- P6 a obtenu R6 et demande R2
- P7 a obtenu R5 et demande R2.

On voudrait savoir s’il y a interblocage.

1. Construire un graphe orienté où les sommets sont les processus et les ressources, et où :

    La présence de l’arc $Ri\rightarrow Pj$ signifie que le processus Pj a obtenu la ressource Ri
    La présence de l’arc $Pj\rightarrow Ri$ signifie que le processus Pj demande la ressource Ri.

2. Y-a-t-il interblocage ? si oui précisez où.

## Exercice 5 - Ecrit 2025, Asie J2, Exercice 2, sur 6 points


_Cet exercice porte sur la programmation Python, la gestion des processus._

On souhaite élaborer un programme système permettant de gérer l’ordre d’exécution des processus sur le processeur.

1. Donner le nom de ce type de programme.

2. Donner les différents états possibles d’un processus.

Chaque processus dispose d’une valeur de priorité. Un processus est prioritaire sur un autre processus si sa valeur de priorité est plus petite. Ainsi pour rendre un processus moins prioritaire, il faut augmenter sa valeur de priorité, par exemple en la faisant passer de 2 à 3.

**Fonctionnement du programme gérant l’ordre d’exécution des processus :**

On dispose d'une liste dont les éléments sont des files de processus. La première file contient les processus ayant la valeur de priorité la plus élevée 0, la seconde ceux ayant la valeur de priorité 1, etc.

À l'arrivée d'un nouveau processus :

* Attribuer au nouveau processus la valeur de priorité la plus élevée 0 ;
* Placer le nouveau processus dans la file d'attente correspondant à sa valeur de priorité (c’est-à-dire la première file de la liste).

À chaque cycle d'horloge :

* S'il n'y a pas de processus en cours d'exécution et s'il reste des processus en attente :

  * Sélectionner un processus avec la priorité la plus élevée dans l'une des files d'attente non vides ;
  * Élire ce processus comme nouveau processus en cours d'exécution ;
* Sinon si un processus est en cours d'exécution :

  * Si le processus a terminé son exécution, le retirer du processeur ;
  * Sinon,

    * incrémenter le temps d'utilisation du processus ;
    * Si des processus de priorité supérieure ou égale attendent :

      * Retirer le processus en cours d'exécution du processeur ;
      * Réduire sa priorité de 1 et le mettre dans la file d'attente correspondant à sa priorité ;
      * Élire un processus dont la priorité est la plus élevée parmi les processus des files d'attente non vides ;
    * Sinon, réduire sa priorité de 1 et continuer à exécuter le processus en cours d'exécution.

3. Parmi les propositions suivantes, donner la structure la plus adaptée pour stocker les processus d’une même priorité :

   * Proposition 1 : Liste
   * Proposition 2 : File
   * Proposition 3 : Pile

Pour représenter le processus, on utilise une classe `Processus` qui possède les variables d’instances `PID` (l’identifiant du processus), `priorite` (la priorité du processus), `temps_utilisation` sur le CPU et le temps nécessaire à son exécution `temps_CPU`.

4. Compléter le constructeur de la classe `Processus` :

   ```python
   class Processus:
       ...(self, ..., priorite, temps_CPU):
           ... priorite = priorite
           ... PID = ...
           self.temps_utilisation = 0
           self.temps_CPU = temps_CPU
   ```

5. On considère les trois processus suivants :

   ```python
   P1 = Processus(PID=1,priorite=0,temps_CPU=10)
   P2 = Processus(PID=2,priorite=0,temps_CPU=7)
   P3 = Processus(PID=3,priorite=0,temps_CPU=5)
   ```

   On a donc `liste_files = [[P3, P2, P1], [], []]`.

   Compléter la simulation suivante, dans laquelle la variable `CPU` contient le processus en cours d’exécution :

   ```
   Cycle 1: CPU=P1  liste_files=[[P3, P2], [], []]

   Cycle 2: CPU=P2  liste_files=[[P3],[P1],[]]

   Cycle 3: CPU=P3  liste_files=[[], [...],[]]

   Cycle 4: CPU=P3  liste_files=[[], [...], [...]]

   Cycle 5: CPU=... liste_files=[[], [...], [...]]
   ```

Dans les questions 6 et 7, on dispose :

* d’un processus qui nécessite un temps d’utilisation de 1000 pour terminer ;
* d’un nombre important de processus dont le temps d’utilisation pour terminer est de 4 où l’on suppose de plus que chaque processus terminé est remplacé par un nouveau processus similaire.

6. Expliquer pourquoi le processus qui nécessite un long temps d’utilisation du CPU risque de ne jamais terminer avec le programme de gestion de l’ordre des processus ci-dessus (indiquer notamment la priorité du processus long au bout de quelques temps).

Pour régler ce phénomène, on décide d’ajouter la variable d’instance `temps_d_attente` au processus, et on définit une constante appelée `Max_Temps` qui correspond au temps maximum qu’un processus attend avant de remonter sa priorité. L’idée est qu’à chaque cycle, le `temps_d_attente` augmente. Ainsi, si sa valeur dépasse `Max_Temps`, alors sa priorité augmente.

7. Expliquer pourquoi le processus qui nécessite un temps long d’utilisation du CPU ne risque plus de ne jamais terminer avec ce nouveau programme de gestion de l’ordre des processus.

8. Écrire une fonction `meilleur_priorite` qui renvoie `None` s’il n’y a plus de processus et la priorité de l’un des processus les plus prioritaires de la liste des files d’attente dans le cas contraire.

   ```python
   def meilleur_priorite(liste_files):
       ...
   ```

   **Exemple :**

   ```python
   # p1, p2 et p3 sont des instances de la classe 'Processus'
   >>> liste_files = [[], [p2], [p3, p1]]
   >>> meilleur_priorite(liste_files)
   1
   ```

9. Écrire une fonction `prioritaire` qui renvoie `None` si aucune des files d’attente de la liste ne contient un processus et qui renvoie l’un des processus parmi les plus prioritaires sinon (dans ce cas la fonction `prioritaire` supprimera le processus choisi de la file d’attente dans laquelle il se trouvait).

   ```python
   def prioritaire(liste_files):
       ...
   ```

   On pourra utiliser `liste.pop(i)` pour renvoyer l’élément de la liste à la position `i`, tout en le supprimant de la liste.

10. Écrire une fonction `gerer` qui récupère le processus en cours d’exécution `p` ainsi que la liste des files d’attente `liste_files` et qui implémente le programme donné en début d’énoncé pour gérer les processus.

   ```python
   def gerer(p, liste_files):
       ...
   ```


## Exercice 6 - Bilan

Trois commerciaux (Audrey, Enzo et Louis) d'une société de vente à distance
travaillent en réseau sur un même serveur, sur lequel ils stockent des fichiers
qu'ils partagent : _fichier_produit_ et _fichier_clients_.

1. Schématiser ce contexte.
2. À certaines heures de travail, les 3 commerciaux effectuent des accès nombreux
   aux deux fichiers.

   Voici la liste de leurs accès aux fichiers entre 9h et 9h30 :

   | Heure de début | Durée    | Utilisateur | Fichier           | Tâche effectuée |
   | -------------- | -------- | ----------- | ----------------- | --------------- |
   | 09:01:00       | 00:01:00 | Louis       | _fichier_produit_ | Impression      |
   | 09:02:00       | 00:01:00 | Louis       | _fichier_clients_ | Impression      |
   | 09:05:00       | 00:04:00 | Audrey      | _fichier_clients_ | Lecture         |
   | 09:07:00       | 00:02:00 | Enzo        | _fichier_clients_ | Modification    |
   | 09:12:00       | 00:09:00 | Audrey      | _fichier_produit_ | Modification    |
   | 09:18:00       | 00:02:00 | Enzo        | _fichier_produit_ | Modification    |

   Schématiser la chronologie des accès qui sont faits sur cette période.

3. Compléter le schéma du 2. avec les accès suivants :

   | Heure de début | Durée    | Utilisateur | Fichier           | Tâche effectuée |
   | -------------- | -------- | ----------- | ----------------- | --------------- |
   | 09:24:00       | 00:10:00 | Louis       | _fichier_produit_ | Mise à jour     |
   | 09:28:00       | 00:10:00 | Audrey      | _fichier_clients_ | Mise à jour     |
   | 09:32:00       | 00:06:00 | Audrey      | _fichier_produit_ | Mise à jour     |
   | 09:36:00       | 00:06:00 | Louis       | _fichier_clients_ | Mise à jour     |

4. Quel est le problème qui survient sur cette période ?

   | Heure de début | Durée    | Utilisateur | Fichier                                  | Tâche effectuée |
   | -------------- | -------- | ----------- | ---------------------------------------- | --------------- |
   | 09:44:00       | 00:05:00 | Louis       | _fichier_produit_                        | Mise à jour     |
   | 09:46:00       | 00:05:00 | Audrey      | _fichier_clients_                        | Mise à jour     |
   | 09:49:00       | 00:04:00 | Louis       | _fichier_produit_ et \ _fichier_produit_ | Mise à jour     |
   | 09:51:00       | 00:04:00 | Audrey      | _fichier_clients_ et \ _fichier_produit_ | Mise à jour     |

**Remarque** : vous pouvez construire une chronologie minute par minute des utilisations
de chaque fichier (dans un seul tableau). Utiliser un code couleur "vert : accès non bloquant", "rouge : accès bloquant".
