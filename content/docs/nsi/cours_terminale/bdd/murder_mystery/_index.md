
---
title: "SQL Murder Mystery"
author: "Guillaume Connan"
weight: 1000

---


## [SQL Murder Mystery](https://github.com/NUKnightLab/sql-mysteries)
Un meurtre  a été commis.  Comme vous  ne prenez jamais  de notes, vous  ne vous
souvenez plus du nom du meurtrier. Vous  vous souvenez juste que le meurtre a eu
lieu le 15 janvier 2018 dans la ville de SQL City.
![e g robinson](./egr.webp)
Vous disposez ensuite de la base de données schématisée ici :
![bdd de sql murder mystery](./sqlmm.png)
À vous de jouer :
{{< sql title="Entrez ici vos requêtes pour mener l'enquête:" dbfile="sql-murder-mystery.db">}}
{{< /sql >}}
Vous rentrerez ensuite votre solution ici :
{{< sql title="Votre solution:" dbfile="sql-murder-mystery.db">}}
INSERT INTO solution VALUES (1, "Entrez ici le nom du meurtrier");

SELECT value FROM solution;
{{< /sql >}}
