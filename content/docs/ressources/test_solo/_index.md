---
title: "Python solo"
weight: 10000

---

### Objectifs pour pyodide

1. plusieurs cellules de code
2. fonctionne le plus comme un script qu'on exécute : on voit print et la valeur finale séparé
3. permettre d'interrompre
4. pas bouffer toutes les ressources, launch que si demandé

## Plan pour pyodide

1. envoyer une redirection du stdout à python, lui permettre de choisir le bon élément pour son print
2. interrompre correctement
3. empêcher de load plusieurs fois... ??? flag qq part ???
4. écrire en mémoire qui est pyodide (window.pyodide instead of self.pyodide dans une fonction)
5. déplacer ce qui est statique dans un fichier qui soit pas un module (pas de namespace ? check la différence)
6. ???
7. profit

## Pyodide shortcodes

{{< python_solo title="IDE 1" init="init1.py" >}}for i in range(10 ** 1):
    print(i)
"Finished..."
{{< /python_solo >}}


{{< python_solo >}}print("Hello World!")
False
{{< /python_solo >}}


## Test everything


### LaTex

Inline math : $\int_1^2 x^2dx = \dfrac{3}{2}$

$$\sum_{k=1}^n k = \frac{n(n+1)}{2}$$

### Code

**Python**

```python
def f(x):
    return x ** 2

s = "bonjour"
t = "❤️"
a = 1234
b = 456.789
d = [1, 2]
# comment
```

**SQL**

```sql
SELECT * FROM table
WHERE age > 18;
```

Du code en ligne `self.pyodide = await load();`

### Tableau

| a | b |
|---|---|
| 1 | 2 |

### Liens

[mon site](https://qkzk.xyz)

### Images

Depuis l'extérieur :

![exterieure](/docs/ressources/test/img/0)


Depuis mon site :

![locale](/uploads/docnsitale/arbres/fig/expression-tree.svg)
