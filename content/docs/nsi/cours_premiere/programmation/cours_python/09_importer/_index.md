---
title: "9 - Importer"
author: "qkzk"
date: "2021/04/27"
weight: 10

---

### pdf: [pour impression](./importer.pdf)


Il est courant de devoir utiliser des morceaux de programmes déjà écrits.

On connait les deux syntaxes :

```python
import math

print(math.pi)
```

et on peut accéder à toutes les fonctions de la librairie `math` avec
`dir(math)` ou l'aide `help(math)`

Il est aussi possible de n'importer qu'une fonction particulière avec :

```python
from math import pi

print(pi)
```

Cette fois, on n'a accès qu'à ce qu'on a importé.

C'est plus simple pour écrire le code et cela évite d'avoir beaucoup d'objets
inutiles en mémoire.

Enfin, on peut renommer des modules en les important :

```python
import matplotlib.plot as plot


plot([0, 1, 2], [5, 4, 3])
plot.show()
```

![fig](./fig.png)

