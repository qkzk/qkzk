---
title: "Exercices"
author: "qkzk"
weight: 2
---

* Le simulateur [ARMLite](https://peterhigginson.co.uk/ARMlite/) et un [mirroir](https://www.iro.umontreal.ca/~mignotte/IFT1215/APPLETS/LM_ARM/)
* [documentation complète](https://peterhigginson.co.uk/ARMlite/Programming%20reference%20manual.pdf)

# Exercices de déroulé de code

Ces exercices se traitent _d'abord sur feuille_, ensuite dans l'assembleur pour vérifier.

À chaque fois, on veut connaître l'état de tous les registres modifiés durant le programme à la fin de celui ci.

Lorsque le registre n'est pas modifié, inutile de le préciser.

Exemple :

```java
MOV R0, #25
ADD R1, R0, #12
```

- `RO` contient 25
- `R1` contient $25+12=37$

## Ecrit 1 - Mnemonique

Remplacer chaque instruction suivante par son mnemonique puis dérouler le programme pas à pas.

```
    Charger la valeur 2 dans le registre 3
    Charger la valeur 5 dans le registre 1
    Ajouter les registres 3 et 1 et enregistrer dans le registre 2
    Soustraire 25 du registre 2 et enregistrer dans le registre 1
    Comparer les registres 3 et 1
    Si la comparaison est différente, sauter à FIN
    Charger la valeur 1 dans le registre 2
FIN:
    arrêter le programme
```

Quels sont les états des registres ?

## Ecrit 2 - Dérouler et traduire

Dérouler le programme suivant, noter les états finaux des variables `x, y, z` puis le traduire en assembleur
et recommencer.

```python
x = 8
y = 12
z = x + y
if z == x:
  x = y
else:
  x = z
```

## Ecrit 3 - Traduire et dérouler

Traduire le programme suivant en langage naturel et le dérouler ligne par ligne.

```
    MOV R1, #10
    MOV R2, #12
    ADD R3, R2, R1
    CMP R1, R2
    BNE Different
    SUB R3, R2, R1
    B Fin
Different:
    SUB R2, R1, R3
Fin:
    HALT
```

## Ecrit 4 - Traduire et dérouler (suite)

```java

       LDR R1, a
       LDR R2, b
       ADD R3, R2, R1
       STR R3, a
       LDR R1, a
       LDR R2, b
       SUB R3, R1, R2
       STR R3, a
       HALT
 a:    .WORD 42
 b:    .WORD 20
```

Dérouler le programme suivant, on notera l'état de la mémoire et des registres au fur et à mesure.

## Ecrit 5 - Boucle

Il existe de nombreuses manières d'écrire une boucle en assembleur.

Le principe consiste à renvoyer à la même adresse tant qu'une condition n'est
pas remplie.

```
    MOV R1, #0
    MOV R2, #1
    MOV R3, #4
Boucle:
    CMP R1, R3
    BEQ Fin
    ADD R1, R1, R2
    B Boucle
Fin:
    HALT
```

1. Dérouler le programme précédent pas à pas. Combien de fois les instructions
   entre `Boucle:` et `Fin:` seront-elles exécutées ?
2. Modifier le programme afin que 10 tours de boucle soient réalisés.
3. Modifier le programme afin que la boucle soit infinie.

## Ecrit 6 - Boucle en Python

Voici un programme Python qui utilise une boucle pour calculer
un montant après 10 ans sur un compte rapportant 150€ d'intérêts annuels.

```python
capital = 2000
for annee in range(10);
  capital += 150
```

1. Quel est le montant de `capital` après l'exécution du programme ?
2. Traduire ce programme en assembleur.

## Ecrit 7 - Compteur

Voici un programme qui compte le nombre d'années nécessaires pour doubler
un capital.

```python
capital = 3000
double = 2 * capital
annee = 0
while capital < double:
  capital += 150
  annee += 1
```

1. Combien d'années sont nécessaires ? Résoudre mathématiquement la question.
2. Faire tourner en Python en le programmant sur votre calculatrice.
   Ajouter les instructions nécessaires pour consulter le solde final
   et le nombre d'années.
3. Traduire ce programme en assembleur.

## Ecrit 8 - Multiplication

L'assembleur dont nous disposons ne contient aucune instruction permettant
de multiplier deux entiers.

Afin de réaliser une _multiplication_, il faut la programmer avec des additions.

Par exemple le produit de 3 par 12 peut être calculé par des additions de deux manières :

$3 \times 12 = 12 + 12 + 12$ ou $12 \times 3 = 3 + 3 + 3 + 3 + 3 + 3 + 3 + 3 + 3 + 3 + 3 + 3$

De toute évidence, une approche est meilleure que l'autre...

1. Sans se soucier d'optimiser.

Compléter le programme suivant afin qu'il réalise le produit $3 \times 12$

R1: 3, R2: 12, R3: résultat de la multiplication, R4: nombre d'additions déjà réalisées.

```
    MOV R1, #3
    MOV R2, #12
    MOV R3, #0
    MOV R4, #0
  Produit:
    CMP R4, R2
    BEQ Fin
    ADD R3, R3, R1
    ...
    B Produit
Fin:
    HALT
```

2. En cherchant à minimiser le nombre d'instruction

Il est préférable de réaliser $12 + 12 + 12$ que $3+ 3 + \cdots + 3$.

Afin d'améliorer le temps de calcul, nous allons comparer les nombres et utiliser
deux registres supplémentaires.

1. On charge dans R5 le plus petit de R1 et R2,
2. On charge dans R6 le plus grand de R1 et R2,
3. On réalise `R5 * R6`

Mémoire :

| Adresse | Valeur |
| ------- | ------ |
| 200     | 3      |
| 201     | 12     |

```
// R1: a
// R2: b
// R3: a * b
// R4: compteur de tour
// R5: temp
      LDR R1, a
      LDR R2, b
      MOV R3, #0
      MOV R4, #0
      CMP ...
      BLT Petit
      B Produit
Petit:
      ...
      ...
      ...
      B Produit
Produit:
      CMP R4, R2
      BEQ Fin
      ...
      ...
      B Produit
Fin:
      HALT
a:    .WORD 12
b:    .WORD 3
```

Compléter le programme suivant. Vérifier qu'il exécute bien l'opération optimale.

## Ecrit 9 - Division Euclidienne

Nous allons réaliser la division Euclidienne pour calculer le quotient et le
reste d'une division.

$20 = 7 \times 2 + 6$

La division Euclidienne de $20$ par $7$ a pour quotient $2$ et reste $6$.

Voici l'algorithme de la division Euclidienne de $a$ par $b$ utilisant des
soustractions successives :

```
Diviser(a: entier, b: entier)
  a et b deux entiers.
  q = 0

  Tant que a >= b faire
    a = a - b
    q = q + 1

  r = a

  renvoyer q et r
```

1. Traduire ce programme en assembleur.
2. Vérifier qu'il renvoie le résultat correct pour les divisions de $7$ par $2$ et de $21$ par $4$

## Ecrit 10 - Maximum d'une collection

Dans cette partie, plus délicate, on va s'intéresser à _l'adressage indirect._

Ce principe permet de réaliser des opérations sur les adresses. L'objectif est d'utiliser un tableau
de données enregistré en mémoire.

### Enregister les données.

1. On aligne d'abord la mémoire à une adresse spécifiée, assez grande pour pouvoir enregistrer le code avant.
2. On spécifie la taille totale des données, en nombre de mots,
3. On donne un nom à l'adresse de départ de la collection, ensuite on écrit les valeurs de cette collection.

### Le programme lui même

Dans le code, on va d'abord charger l'adresse du premier élément.
Pour accéder au suivant, on se déplace de la taille d'un mot (4 octets) dans la mémoire.
Et ainsi de suite.

### Un exemple

Le code suivant présente un parcours séquentiel afin de déterminer un maximum. C'est le plus simple que je parvienne à écrire, il y a sûrement mieux !

```java
  1|      MOV R1, #tableau  // adresse du début du tableau
  2|      LDR R2, longueur  // taille du tableau
  3|      LSL R2, R2, #2    // multiplier par 2**2 pour compter les octets (1 mot = 4 octets)
  4|      MOV R3, #0        // compteur de boucle
  5|      LDR R4, tableau   // maximum
  6|boucle:
  7|      LDR R5, [R1+R3]   // charger la valeur courante
  8|      ADD R3, R3, #4    // incrémenter le compteur de boucle
  9|      CMP R5, R4        // comparer la valeur courante au max
 10|      BGT nouveaumax    // on a un nouveau max !
 11|      B continuer       // doit-on continuer la boucle ?
 12|nouveaumax:
 13|      MOV R4, R5        // sauvegarder le nouveau max
 14|      B continuer       // doit on continuer la boucle ?
 15|continuer:
 16|      CMP R3, R2        // comparer l'indice de boucle au nombre d'éléments
 17|      BGT fin           // on dépasse, on s'arrête
 18|      B boucle          // on ne dépasse pas, encore un tour
 19|fin:
 20|      HALT
 21|      .ALIGN 0x00100
 22|longueur: 5             // taille du tableau
 23|tableau: 10             // 1er élément
 24|      11
 25|      5
 26|      8
 27|      4
```

L'étape importante est en trois temps :

- d'abord ligne 1, on charge une _adresse_,
- ensuite ligne 3 on mesure le nombre d'octets, vu qu'on doit donner une adresse dans cette unité,
- enfin ligne 7 `[R1+R3]` va nous donner la position du nombre courant.

1. Faire tourner ce programme à la main
2. Que changer pour un tableau de 20 éléments ?
3. L'adapter proprement pour déterminer :

   a. le minimum des éléments,
   b. la somme des éléments.

# Exercices de programmation

Tous ces exercices doivent se traiter dans le [simulateur ARMLite](https://peterhigginson.co.uk/ARMlite/)

Certains sont difficiles et demandent d'avoir bien reflechi avant de se lancer.

## Programmation 1. Hello Robert

Écrire un programme qui :

1. affiche le message : "Tapez votre nom : "
2. demande une saisie à l'utilisateur. (Par exemple "Robert")
3. Affiche le message "Bonjour $nom"

Exemple :

```
Tapez votre nom :
Robert
Bonjour Robert
```

En python :

```python
nom = input("tapez votre nom")
print("bonjour", nom)
```

## Programmation 2. Opérations courantes

1. Exécutez le code python suivant (Thonny, sublime text etc.)

   ```python
   a = 0b10011111
   b = 0b00110011

   print(a + b)
   print(a - b)
   print(a & b)
   print(a | b)
   print(a ^ b)
   print(a >> 2)
   print(b << 2)
   ```

2. Le traduire en ARMlite et vérifier les résultats obtenus.

## Programmation 3. Capital simple

On place 1000€ sur un compte.

Chaque années on dépose 250€.

Comptez à l'aide d'ARMlite le nombre d'années nécessaires pour doubler le capital initial.

On conservera la réponse finale dans un registre spécifique (au choix) et on l'affichera à l'écran.

_Je précise aux malins que la réponse est 4... et qu'on s'en moque. Faites le._

## Programmation 4. Afficher une table ASCII

Les [caractères imprimables à l'écran de la table ASCII](/docs/nsi/cours_premiere/donnees_simples/chaines_caracteres/1_cours/) sont encodés de 32 à 127.

1. Affichez les tous à l'écran sans retour à la ligne entre les caractères à l'aide d'une boucle.

   ```
    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
   ```

2. Affichez une ligne par caractère avec sa valeur numérique d'abord

   ```
   32
   33 !
   ...
   64 @
   65 A
   66 B
   67 C
   ...
   ```

## Programmation 5. Jeu à deux joueurs, le plus ou moins.

On suppose le déroulé d'une partie suivante entre A et B :

A choisit un nombre entre 1 et 100
B doit le trouver.

A choisit 42

- B propose une valeur, disons 50, A lui répond "C'est moins"
- B propose une valeur, disons 25, A lui répond "C'est plus"

etc.

- B propose une valeur, disons 42 (enfin...). A lui répond "gagné" et la partie s'arrête.

1. **Programmer ce jeu en ARMlite.**

   On supposera que A saisit sa valeur et qu'elle est inconnue de B (qui ne triche pas en lisant les valeurs à l'écran...)

   **Aide** On pourra s'aider de [ce point de départ](./guess_start.arm)

2. Améliorer le jeu en proposant de rejouer après une partie (`Taper 1 pour rejouer`).

3. **Bonus délicat** à l'aide de la documentation, remplacer le joueur A par le choix aléatoire d'un entier.
   Pour simplifier, on utilisera des nombres entre 1 et un puissance de 2 (entre 1 et 64, par exemple).
