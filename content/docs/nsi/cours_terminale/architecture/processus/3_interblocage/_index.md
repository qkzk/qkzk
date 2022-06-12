---
title: Interblocage
bookCollapseSection: true
weight: 3

---

[pdf](./3_interblocage.pdf)

## L'interblocage

Nous avons dits précédemment que des processus peuvent avoir besoin de la
même ressource.

Dans de nombreuses situations, deux processus (ou davantage) peuvent souhaiter
accéder à la même donnée sur le disque dur :

* Les deux processus ont uniquement besoin de lire la donnée : celle-ci est
    alors partagée, sans problème complexe.
* Les deux processus ont besoin de la donnée de manière exclusive, pour la
    modifier, par exemple.
* Les deux processus ont besoin de communiquer entre eux : l'un doit attendre
    un résultat de l'autre.

**Exemple 1**

Deux processus P1 et P2 ont tous les deux besoin de la même donnée D pour la
modifier, c'est-à-dire de manière exclusive. Le premier à y accéder est P1,
D lui est alloué par le système d'exploitation. Lorsque P2 souhaite accéder à
D, la ressource n'est pas disponible : P2 est alors bloqué jusqu'à la fin de
l'utilisation de D par P1.

**Exemple 2**

Deux processus P1 et P2 ont tous les besoin de deux données, D1 et D2.\
Chaque processus bloque une donnée et doit attendre d'avoir accès à la seconde
pour se terminer et les libérer.

Si la chronologie est la suivante :

* P1 bloque D1
* P2 bloque D2
* P1 attend D2
* P2 attend D1

Alors aucun des deux processus ne pourra avancer. C'est **l'interblocage**.
Sans une intervention extérieure, la situation est figée.

Face à cette problématique la plupart des systèmes d'exploitation ont choisi
de ne pas essayer d'éviter les interblocages mais de les détecter s'ils
surviennent et de les solutionner.


### Détecter une situation d'interblocage

Afin de résoudre _conceptuellement_ ce problème on peut utiliser un graphe orienté.

* On sépare les processus et les ressources : ce sont les noeuds du graphe.
* Lorsqu'un processus attend une ressource, un arc est tracé partant de ce
  processus vers la ressource,
* Lorsqu'un processus acquiert une ressource, un arc est tracé partant de la
  ressource vers le processus. On efface l'arc dans l'autre sens s'il existe.

**L'interblocage se produit lorsqu'il existe un cycle dans le graphe**

![graph_000.svg](graph_000.svg)


Ce graphe présente un cycle et les processus sont bloqués.

![graph_001.svg](graph_001.svg)


Ce graphe ne présente pas ce cycle, il n'y a pas d'interblocage.

En pratique, P1 possède les deux ressources dont il a besoin et va terminer en premier.
Ensuite P2 va acquérir les ressources et terminer.

---

Il existe d'autres situations critiques lorsqu'on exécute plusieurs processus
en même temps. En voici une :

## Race condition (_situation de compétition_) - HP

C'est une situation dans laquelle le résultat d'une série d'opération
dépend de _l'ordre_ dans lequel celles-ci sont effectuées.

Lorsque un processus principal crée plusieurs processus fils, il ne contrôle
pas l'ordre dans lequel ils sont exécutés. S'il a besoin des résultats de ceux
ci, il ne pourra pas prédire le résultat final.


### Un exemple

`hello` et `bonjour` sont deux processus indépendants qui partagent une même ressource.

Afin d'illustrer on se contente de les faire écrire dans la console. En pratique
ils écriraient dans le même fichier.

À l'aide de Python nous allons les lancer l'un après l'autre et attendre
qu'ils aient terminé tous les deux.

Le système d'exploitation se charge de leur exécution et leur donne la main
selon un ordre difficile (_quasi impossible_) à prédire.

Leur résultat commun est donc la sortie console.


```python
from multiprocessing import Process
from random import random
from time import sleep


def hello():
    for _ in range(5):
        print("hello")
        sleep(random())


def bonjour():
    for _ in range(5):
        print("bonjour")
        sleep(random())


p1 = Process(target=hello)
p2 = Process(target=bonjour)

p1.start()
p2.start()

p1.join()
p2.join()
```

Première exécution :

```bash
hello
bonjour
hello
bonjour
hello
hello
bonjour
bonjour
bonjour
hello
```

Seconde exécution :

```bash
hello
bonjour
bonjour
bonjour
hello
hello
hello
hello
bonjour
bonjour
```

On peut arguer que ces programmes ne font rien d'essentiel, mais s'ils doivent
écrire dans le même fichier, c'est plus génant.

Il est délicat d'illustrer simplement les bugs engendrés par les situations
de compétition.

En voilà une avec une notion hors programme, les `threads` (_processus légers_) :

```python
import threading


def increment_global():
    global x
    x += 1


def task():
    for _ in range(500000):
        increment_global()


def race(nb: int):
    global x
    x = 0
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"after race number {nb}, x = {x}")


def main():
    for i in range(5):
        race(i)


if __name__ == "__main__":
    main()
```


Ce programme est supposé compter jusqu'à 1 million.

Que fait-il ?

* dans `race` on crée une variable globale `x` valant 0.
* On lance deux threads exécutant `task` qui incrémentent le même `x` 500000 fois chacun.

  On devrait trouver $x = 500000 + 500000 = 1000000$ à la fin...

Mais en fait :

```bash
$ python competition.py
after race number 0, x = 712104
after race number 1, x = 850346
after race number 2, x = 893592
after race number 3, x = 813423
after race number 4, x = 761881

```

D'où vient le problème ? `x += 1` réalise plusieurs opérations :

* lire la valeur de `x`
* lui ajouter 1
* écrire le résultat dans `x`

Imaginons un déroulé :

* thread1 lit quand `x` vaut 123,
* thread2 lit quand `x` vaut 123,
* thread1 ajoute 1 : 124
* thread2 ajoute 1 : 124
* thread1 écrit : `x = 124`
* thread2 écrit : `x = 124`

Deux incrémentations ont eu lieu, `x` devrait valoir 125... mais la valeur en mémoire
est 124...


Ce problème est _majeur_ et demande beaucoup de rigueur pour être évité.

Il existe de nombreuses approches mais la plus courante est d'employer des `mutex`
ou des `lock` qui vérouillent une exécution tant que le `mutex` n'est pas acquis.

C'est la raison pour laquelle on ne travaille pas avec des threads en NSI,
vous verrez ça plus tard :) !


## Threads vs Processus

Lorsqu'on exécute un programme simple, il se déroule sur un seul coeur de processeur.
Or... ajouter des coeurs de processeurs est la seule solution réaliste qu'on ait trouvé
pour accélérer les machines depuis 15 ans.

Un programme devant s'exécuter vite n'a pas le choix, il doit utiliser au maximum les ressources
de la machine et donc _le parallélisme_.

On a donc crée deux manières d'exécuter plusieurs séquences d'instructions en parallèle : les _threads_ (fils d'exécutions) et les _processus_.

Ce sont des séquences d'instructions indépendantes.

* Un thread s'exécute dans le même processus que le processus parent, il partage la mémoire du processus.
* Un processus fils est un autre processus, dépendant du parent, qui dispose de sa propre mémoire.

Un processus est plus _lourd_ pour le système qu'un thread... mais peut facilement être isolé
et son exécution est déléguée à l'OS, d'autre part un processus dispose de son propre expace
mémoire et ses erreurs ne risquent pas de compromettre l'ensemble du programme.

D'autres nuances existent et selon les besoins on choisira l'un ou l'autre.

Ces thèmes étant largement hors programme, je vous laisse vous documenter [ici en anglais](https://www.geeksforgeeks.org/difference-between-process-and-thread/).

D'autres précisions plus formelles sur la nuance _thead vs process_ :

> A process is an address space with some open files and other resources, plus some number of threads.
> 
> A thread is a set of registers and a stack and a program counter, that runs in an address space.
> 
> Threads in the same process share the address space, and the threads have a consistent (coherent) view of the contents of memory, subject to memory ordering rules.
> 
> So in current processors, you can run the threads of a process on any core, because modern machines all have coherent memory.
> 
> It wasn’t always so. There were multiprocessors in the 80’s and 90’s where the different cores did not necessarily have coherent views of memory. On those systems, including some built by Silicon Graphics I think, you could not have multiple threads from the same process running on different cores.
> 
> I am not sure those machines even had threads, but if they did, all the threads for a process would have to be scheduled on the same core.
> 
> Threads like that would still be useful, because threads are useful as programming conveniences as well as for parallel execution. Programmers often use threads to call synchronous I/O functions where they block waiting for events. Programmers think this is easier than using event driven programming with a single thread or using asynchronous I/O. I am not sure I agree, but that’s what folks do.
> 
> [source quora](https://www.quora.com/Could-process-threads-always-be-shared-between-cores)
