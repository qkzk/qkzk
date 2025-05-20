---
title: "Boucles non bornées"
bookCollapseSection: true
author: "qkzk"
weight: 3

---

## Boucles non bornées : `while`

`while`, qui signifie _tant que_, permet de répéter un bloc tant qu'une condition est respectée :


```python
while condition:
    bloc_repete_tant_que_condition_est_vrai

bloc_execute_apres
```

On emploie `while` lorsqu'on ne sait pas à l'avance combien de fois il sera nécessaire
de répéter un bloc d'instruction.

Par exemple : "tant que je n'ai pas bon à l'exercice, je recommence".

Ou, "tant qu'il reste du pain je mange :"

{{< python title="petit déjeuner" >}}tartine = 50
while tartine > 0:
    print("Je mange une tartine wesh !")
    tartine = tartine - 1
{{< /python >}}

Autre exemple, le casino :

Jean-Martin a 10€, il joue aux machines à sous (un vrai pigeon). Chaque mise lui coûte 1€ et il a une chance sur 100 de gagner 10€ (quand je vous disais)...

Le programme suivant simule cette situation dramatique :

```python
import random                     # fonctions simulant le hasard

capital = 10
while capital > 0:
    capital = capital - 1         # il mise 1 €
    if random.random() < 0.01:    # une chance sur cent
        capital = capital + 10    # il récupère 10 €
        print("waouh...")
    else:
        print("encore perdu...")

print("Jean-Martin a perdu tout son argent.")
```

Le prof de maths qui sommeille en moi vous signale que :

1. Ce programme termine toujours :
2. Les étapes intermédiaires varient mais l'issue est toujours la même : Jean-Martin perd tout son argent.
3. Le seul moyen de gagner régulièrement aux jeux d'argent est de les organiser.      Ce privilège est reservé à l'État.


{{< python title="Casino">}}import random                     # fonctions simulant le hasard

capital = 10
while capital > 0:
    capital = capital - 1         # il mise 1 €
    if random.random() < 0.01:    # une chance sur cent
        capital = capital + 10    # il récupère 10 €
        print("waouh...")
    else:
        print("encore perdu...")

print("Jean-Martin a perdu tout son argent.")
{{< /python >}}

Regardez bien la manière de simuler un événement aléatoire de probabilité $\dfrac{1}{100}$ : 

```python
if random.random() < 0.01:
    # si l'événément se réalise...
else:
    # si l'événément ne se réalise pas...
```

### Exercice 1

Modifier le programme précédent :

1. Créer une variable `compteur` valant 0 avant la boucle,
2. Augmenter `compteur` de 1 à chaque tour de la boucle,
3. Affichez la valeur de `compteur` une fois la boucle terminée.
4. _Bonus difficile_ Affichez à la fin du programme le _maximum_ atteint par Jean-Martin avec un
    phrase un peu rageante.

## Boucle infinie

On emploie régulièrement des boucles infinies. Il suffit d'écrire la condition `while True`
pour qu'une boucle soit répétée indéfiniment.

Afin de ne pas saturer complètement votre processeur on va introduire un délai d'une seconde
entre deux affichages :

**DANS THONNY**

```python
from time import sleep

while True:
  print("NSI")
  sleep(1)
```

* On importe la fonction `sleep` qui va mettre l'exécution en pause une seconde avec `sleep(1)`
* On répète indéfiniment l'affichage "NSI" toutes les secondes.

{{< hint danger >}}
**Attention** : Impossible d'exécuter ces exemples sur mon site, il faut utiliser un programme externe.

La fonction `sleep` n'est pas traitée correctement ici pour des questions techniques.
{{< /hint >}}


Pour arrêter le programme vous pouvez utiliser le raccourci clavier "Ctrl + C"

À quoi cela peut-il bien servir ?

Et bien c'est ce qu'on fait dans TOUS les logiciels... Pensez un instant à un jeu vidéo.

Lorsque vous arrêtez de jouer, ne serait-ce qu'une seconde, le programme ne s'arrête pas de tourner.

On peut résumer un jeu vidéo à ce schéma :


```python
while True:
  lire_les_actions_du_joueur()
  mettre_le_jeu_a_jour()
  afficher_le_jeu_a_l_ecran()
```

Vous trouverez un tel découpage dans le code de _tous_ les logiciels. Par exemple, voici la boucle principale de [DOOM](https://github.com/id-Software/DOOM/blob/a77dfb96cb91780ca334d0d4cfd86957558007e0/linuxdoom-1.10/d_main.c#L354-L407).

## L'instruction `break`


L'instruction `break` provoque une sortie immédiate d'une boucle `while` ou
d'une boucle `for`.

Dans l'exemple suivant, l'expression `True` est toujours ... vraie : on a
une boucle sans fin.

L'instruction `break` est donc le seul moyen de sortir de la boucle.

{{< python title="break" >}}a = 0
while True:
    print(f"a vaut {a}")
    if a == 10:
        break
    a = a + 1
print("pas de boucle infinie !")
{{< /python >}}


### Affichage de l'heure courante

{{< hint danger >}}
**Doit être traité à l'extérieur, dans Thonny par exemple**
{{< /hint >}}



```python
import time     # importation du module time

while True:
    # strftime() est une fonction du module time
    print('Heure courante ', time.strftime('%H:%M:%S'))
    quitter = input('Voulez-vous quitter le programme (o/n) ? ')
    if quitter == 'o':
        break
print("A bientôt")
```



    >>>
    Heure courante  14:25:12
    Voulez-vous quitter le programme (o/n) ? n
    Heure courante  14:25:20
    Voulez-vous quitter le programme (o/n) ? o
    A bientôt

### Exercice 2 - Le plus ou moins

{{< hint danger >}}
**Doit être traité à l'extérieur, dans Thonny par exemple**
{{< /hint >}}

1. Se documenter sur la fonction `randint` du module `random`

    ```python
    import random
    help(random.randint)
    ```
2. Écrire une boucle qui affiche 10 nombres aléatoires entre 1 et 100

La fonction `input(message)` affiche un message à l'écran pour l'utilisateur,
  celui-ci saisit au clavier une valeur et cette valeur est renvoyée par `input`.

`input` renvoie toujours une chaîne de caractère.

Pour convertir une chaîne de caractère en un entier on peut utiliser :

```python
nombre = int(input("votre nombre : "))
```

Si l'utilisateur tape une valeur pouvant être transformée en entier comme "123",
`nombre` vaudra 123.

Si l'utilsateur tape une valeur _ne pouvant pas être transformée en entier_ comme "Marcel",
Python va générer une erreur.

3.  Écrire le script du jeu du plus ou moins suivant :

    ```
    >>>
    Le jeu consiste à deviner un nombre entre 1 et 100 :

    --->   50
    trop petit !
    --->   75
    trop petit !
    --->   87
    trop grand !
    --->   81
    trop petit !
    --->   84
    trop petit !
    --->   85
    Gagné !
    ```

4. Améliorer le jeu pour indiquer combien de coups ont été necessaires pour gagner.


### Exercice 3 - Intérêts

Lorsqu'on place un capital avec intérêt, on perçoit à intervalle régulier un montant qui vient
s'ajouter à ce capital.

{{< expand "Calcul des intérêts" "...">}}
Il existe deux manières de calculer les intérêts :

* intérêts **simples** : le montant des intérêts est fixe dans le temps, généralement proportionnel au montant
  du capital initial
* intérêts **composés** : les intérêts sont recalculés après chaque période et sont généralement proportionnels
  au capital courant, après versement des intérêts de la précédente période.

Considérons 100€ de capital initial, placés avec 10% d'intérêts :

* Intérêts simples

  Les intérêts sont constants et valent 10€

  | Capital initial | Fin 1ère période | Fin 2nde période | Fin 3eme période |
  |-----------------|------------------|------------------|------------------|
  | 100             | 110              | 120              | 130              |

  Par exemple : $120 + 10 = 130$

* Intérêts composés

  Les intérêts sont variables et valent 10% du dernier capital

  | Capital initial | Fin 1ere période | Fin 2nde période | Fin 3eme période |
  |-----------------|------------------|------------------|------------------|
  | 100             | 110              | 121              | 133.1            |

  Par exemple : 

  On utilise un _coefficient multiplicateur_ de $1.1$ :
  
  $120 \times 1.1 = 133.1$

{{< /expand >}}

_Questions_

1. On place 50000 avec intérêts simples de 5% par période. À l'aide d'une boucle, calculez le montant du capital après 10 périodes.
2. Proposez une formule explicite donnant ce montant, retrouvez votre résultat en posant un calcul à la main.
3. Posez une équation vous donnant le nombre de période avant de doubler le capital en fonction du taux d'intérêt.
3. Même montant initial et même taux d'intérêt mais cette fois composé. Calculez le montant du capital après 10 périodes.
4. À l'aide d'une boucle, déterminez le nombre de période pour doubler le capital.

Corsons un peu le contexte. Cette fois on ajoute aussi un dépôt régulier de 2000€. À chaque période l'épargnant
ajoute 2000€ à son capital. Selon le système d'intérêt, ils seront pris en compte ou non dans les intérêts
suivants.

6. Calculez à l'aide d'une boucle le montant après 10 périodes pour les deux systèmes d'intérêts
7. Calculez à l'aide d'une boucle le nombre de périodes pour doubler le capital dans les deux systèmes d'intérêts.

{{< python title="Intérêts">}}capital = 50000
{{< /python >}}



### Exercice 4 - Mini challenge

_À traiter à l'extérieur_

Le jeu du plus ou moins.

1. Générer un nombre entier aléatoire entre 1 et 100 à l'aide de `random.randint`
2. L'ordinateur choisit, on demande une saisie à l'utilisateur et s'il a bon, on lui dit bravo, sinon qu'il est nul.
3. Intégrer ça dans une boucle `while` et indiquer une fois la partie terminée combien de coups furent nécessaire
    _Remarque : on peut toujours trouver en 7 coups ou moins... pourquoi ?_
4. Intégrer tout ça dans une autre boucle while qui demande (Oui/non) à l'utilisateur s'il veut rejouer après une partie. 

    Faire en sorte qu'on ne lui demande rien quand la partie commence.
