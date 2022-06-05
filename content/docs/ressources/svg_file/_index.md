---
title: "svg from file"
weight: 101

---

## SVG from a file

<img
    src="kernel.svg"
    alt="Linux Kernel"
    height="100%"
    width="100%" />

## graphviz `a -> b`

<!--
```graphviz
digraph {
    rankdir="LR";
    a -> b
}
```
-->
![0.svg](./0.svg)

## graphviz `a -> b -> c -> d -> a`

<!--
```graphviz
digraph {
    rankdir="LR";
    a -> b
    b -> c
    c -> d
    d -> a
}
```
-->
![1.svg](./1.svg)

