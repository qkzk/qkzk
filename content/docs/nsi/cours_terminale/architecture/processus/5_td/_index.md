---
title: "Processus - TD"
bookCollapseSection: true
weight: 5
---

### PDF : [pour impression](/uploads/docnsitale/processus/td_processus.pdf)

**Compétence :** Appliquer l'algorithme d'ordonnancement du plus court d'abord.

# Exercice 1

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

# Exercice 2

Schématiser l'ordre de traitement des instructions des 3 processus pour un
ordonnancement en tourniquet.

**Compétence :** _Appliquer l'ordonnancement premier entré, premier sorti_

# Exercice 3

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

# Exercice 4

Écrire en Python un programme correspondant à l'ordonnancement effectué
dans l'exercice 2.

# Exercice 5 - Bilan

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
