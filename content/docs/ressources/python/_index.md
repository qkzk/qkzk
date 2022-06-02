---
title: "Python worker"
weight: 10000

---

## Pyodide shortcodes

{{< python title="IDE 1" init="init1.py" >}}for i in range(10 ** 6):
    print(i)
"Finished..."
{{< /python >}}


{{< python >}}print("Hello World!")
False
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

Inline code no color `class A():` with color {{< highlight python "linenos=inline" >}}a = "abc" + "def"{{< /highlight >}}

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
