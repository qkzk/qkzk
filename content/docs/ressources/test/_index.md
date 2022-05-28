---
title: "Python shortcodes"
weight: 10000

---

## Pyodide shortcodes

{{< python title="IDE 1" init="init1.py" >}}None
{{< /python >}}


{{< python >}}False
{{< /python >}}


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
