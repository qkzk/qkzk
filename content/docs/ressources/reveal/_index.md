+++
title = "revealjs"
slug = "revealjs"
description = "present content as a reveal.js slide"
+++

This shortcode will format the enclosed markdow to render it with [reveal.js](http://lab.hakim.se/reveal-js/) at runtime (client-side)

Read more on [revealjs github repo](https://github.com/hakimel/reveal.js/#markdown).

## Usage

`revealjs` can use the following named parameters :

* theme
* transition
* controls
* progress
* history
* center


{{% hint warning %}}Even if the enclosed content is a mardown, use `<` shortcode notation instead of the `%` notation {{% /hint %}}

### Content formating and slide delimiters


## Demo


{{<revealjs theme="moon" progress="true">}}

## Test everything

```python
def f(x):
    return x
a = 1
b = True
c = "abc"
```

inline `$\int_1^2x^2dx=\frac{3}{2}$`

`$$\int_1^2x^2dx=\frac{3}{2}$$`

| super | bof |
|-------|-----|
| cool  | cho |

![image](./0.png)

___

# Bottom slide

---

# Right slide

{{</revealjs>}}

