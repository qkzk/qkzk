---
title: 9. Titanic
subtitle: TP CSV
author: qkzk
date: 2026-02-13
theme: metropolis
weight: 10000000
bookCollapseSection: true
geometry: "margin=1.5cm"

---

Le fichier [Titanic.csv](./titanic.csv) contient les données _d'une partie_ des 2200 passagers du Titanic.

![Titanic](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/1280px-RMS_Titanic_3.jpg)

_Rappelons aux plus cultivés d'entre-vous que le Titanic est un bateau qui a fait nauffrage lors de sa première traversée de l'Atlantique._



On répondra à chaque question à l'aide d'un code Python.

1. Quels sont les descripteurs de ce fichier ?
2. Combien de passagers comportait le Titanic ?
3. Les valeurs possibles du champ `Survived` sont 0 si le passagers est décédé durant le naufrage et 1 s'il a survecu. 

    Combien de passagers ont survecu au naufrage ?
4. Le champ `Fare` indique le montant du voyage pour ce passager.

    Quel était le chiffre d'affaire du voyage (= la somme des recettes) ?

5. Le champ `Sex` indique le genre du passager. Comparer les taux de survie selon le genre.
6. Le champ `Pclass` indique la _classe_ dans laquelle les passagers ont séjourné. Quel est le tarif moyen pour chaque classe ? On construira un dictionnaire `{classe: tarif_moyen}`
7. Les plus fortunés ont-ils un meilleur taux de survie ? Quel est le taux de survie de chaque classe ?
8. Les ages. Quels sont les plus jeunes et plus agés des passagers ayant survécu ? Étant décédés ? On veut les noms et les ages respectifs.

    Attention : certains passagers n'ont pas d'age et d'autres ont un age à virgule...
9. Sachant que le salaire d’un employé en 1900 est de 2.10 €/semaine et que le SMIC en janvier 2026 est de 90 €/jour, extrapoler les valeurs que prendraient le tarif moyen et le tarif le plus élevé en 2026. 
