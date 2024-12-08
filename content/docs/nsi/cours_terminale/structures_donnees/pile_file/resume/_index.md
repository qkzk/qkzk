---
subtitle: "Résumé : files et piles"
author: qkzk
weight: 100

---


pdf : [pour impression](/uploads/docnsitale/pile_file/pile_file_resume.pdf)

## Les files et les piles


Les piles et les files sont des exemples de structures de données que faute de
mieux, nous appellerons des _sacs_. Un sac offre trois opérations élémentaires :

1. tester si le sac est vide,
2. ajouter un élément dans le sac,
3. retirer un élément du sac (tenter de retirer un élément d’un sac vide déclenche une erreur).


Le sac est une structure impérative : un sac se modifie au cours du temps.

## piles vs files



Piles et files se distinguent par la relation entre éléments ajoutés et
éléments retirés.

* Dans le cas des **piles**, c’est le **dernier** élément ajouté qui est retiré.
* Dans le cas d’une **file** c’est le **premier** élément ajouté qui est retiré.

On dit que

* la **pile** est une structure **LIFO** (last-in first-out),
* la **file** est une structure **FIFO** (first-in first-out).

Si on représente pile et file par des tas de cases, on voit que la pile possède
un sommet, où sont ajoutés et d’où sont retirés les éléments, tandis que la
file possède une entrée et une sortie.


{{< columns >}}
Pile
<--->
File
{{< /columns >}}
![pile_file](/uploads/docnsitale/pile_file/img/file_pile.png)


Il y a un peu de vocabulaire spécifique aux piles et aux files.
Traditionnellement, ajouter un élément dans une pile se dit empiler (`push`),
et l’enlever dépiler (`pop`), tandis qu’ajouter un élément dans une file se dit
enfiler (`enqueue`), et l’enlever défiler (`dequeue`).




### Python : modéliser une pile ou une file avec un objet `list`

```python

>>> pile = [ ]                            |       >>> file = [ ]
>>> pile.append(1)                        |       >>> file.append(1)
>>> pile.append(2)                        |       >>> file.append(2)
>>> pile.append(3)                        |       >>> file.append(3)
>>> pile.pop()                            |       >>> file.pop(0)
3                                         |       1
>>> pile.pop()                            |       >>> file.pop(0)
2                                         |       2
>>> pile.pop()                            |       >>> file.pop(0)
1                                         |       3
```

**Remarque:**

> Il est possible de créer une classe qui modélise une pile ou une file. (cf TP)

## Utilisation des piles et files en informatique

*   Les gestionnaires de messages, utilisent un "tampon" pour accumuler les
    messages à traiter. Si le traitement est long et qu'ils peuvent recevoir
    plusieurs messages simultanément, les messages sont rangés dans une file.

    Un serveur (de fichier, web ou autre) est généralement accompagné d'un
    gestionnaire de message qui enregistre les requêtes avant de les faire
    exécuter par le serveur lui même.

    Ainsi une machine peu puissante traite les requêtes à son rythme et cela
    évite que les requêtes soient perdues.

*   Les appels successifs d'une fonction récursive s'accumulent dans la pile
    de récursion. Le dernier appel retourne une valeur au précédent, qui
    retourne au précédent etc.
