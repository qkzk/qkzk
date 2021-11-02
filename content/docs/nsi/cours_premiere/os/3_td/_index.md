---
title: "Première NSI - Système d'exploitation Linux - TD"
bookCollapseSection: true
author: qkzk
weight: 3

---

### pdf [pour impression](/uploads/docsnsi/architecture/linux/linux_td.pdf)

# Se tester

## 1. BASH

1. Que fait la commande `ls -al` ?
2. Que fait la commande `mv` ?
3. La commande `ls -l toto.sh` affiche :

    ```
    -r-x-r--r-- 1   john    staff   128     18 mai 11:56 toto.sh
    ```

    a. À qui appartient ce fichier ?
    b. Qui peut écrire dans le fichier ?
    c. Qui peut le lire ?
    d. Qui peut l'exécuter ?

4. Logé sous Linux, dans un terminal on tape `cd` pour se placer dans HOME.
    Quelle commande doit-on ensuite taper pour déplacer dans le répertoire
    courant le fichier `exo1.py`que se trouve dans `Documents/python` sachant
    que `Documents` est dans HOME ?

## 2. Se déplacer dans le système de fichiers

Observer l'arborescence suivante :

$\;$![tree](/uploads/docsnsi/architecture/linux/tree.jpg)

1. Proposer une commande qui permette de se déplacer du répertoire HOME de 
    Alice à celui de Bob :
    a. en utilisant un chemin relatif ;
    b. en utilisant un chemin absolu.
2. Alice est à la racine `/`. Proposer trois commandes qui peuvent lui
    permettre de se déplace dans sont répertoire d'accueil (HOME).
3. Bob est dans son HOME. Aidez-le à :
    a. lister le contenu de son HOME ;
    b. lister le contenu de son HOME y compris les fichiers et répertoires cachés.
    c. lister le contenu du répertoire share sans quitter son HOME.

## 3. Créer une arborescence et se déplacer dedans

1. Créer dans le repertoire d'accueil l'arborescence ci-dessous dans laquelle
    A, B, C, D, E, F et G sont des répertoires :

    ```
    A
    +-- B
    |   |
    |   +-- D
    |   |
    |   +-- E
    +-- C
        |
        +-- F
        |
        +-- G
    ```

2. Quelle commande Unix permet de créer des fichiers vides ?
    Créer deux fichiers vides appelés "un" et "deux" dans votre
    répertoire d'accueil.
3. Quelle commande permet de copier des fichiers ou répertoires ? Colier le
    fichier "un" dans le répertoire "A" en lui donnant le nom "trois".
4. Comment réaliser la copie précédente en utilisant un chemin relatif si vous
    êtes ;
    a. dans le répertoire A ?
    b  dans le répertoire B ?
5. Si votre nom d'utilisateur est `alice`, comment réaliser cette copie
    en utilisant un chemin absolu ?
6. Comment renommer le fichier "trois" en "quatre" ?

## 4. Mettre en majuscule

1. Expliquer ce que fait la commande suivante (respecter les espaces) :

    ```bash
    echo 'bonjour' | tr [a-z] [A-Z]
    ```

   Remarque : Consultez la page de manuel (`man tr`) 
   [correspondante](http://www.linux-france.org/article/man-fr/man1/tr-1.html).

2. Écrire un script à un argument qui met en majuscule l'unique argument fourni.

## 5. Tester l'existence d'un fichier et en afficher le contenu

1. Quelle option de la commande `echo` faut-il utiliser pour rester sur la même
    ligne ?\
    [manuel d'echo](http://www.linux-france.org/article/man-fr/man1/echo-1.html)
2. Comment faut-il faire pour afficher un message sur plusieurs lignes avec
    cette même commande ?
3. Rappeler la commande permettant de lire au clavier et de stocker le résultat
    dans une variable bash.
4. Comment affiche-t-on le contenu d'un fichier sur le terminal ?
5. Pour tester l'existence d'un fichier, en BASH on utilise le test suivant :

    ```bash
    fic='monfic'
    if [ -f $fic ]
        then
            echo "Le fichier $fic existe"
        else
            echo "Le fichier $fic n\'existe pas !"
    fi
    ```

    Écrire un script qui demande à l'utilisateur de saisir un nom de fichier,
    teste si ce fichier existe, puis en affiche son contenu dans le terminal.

## 6. Lire les droits d'un fichier

Pour chacun des fichiers suivants, répondre aux deux questions :

```
-rwx------  1 alice     etu     43M     14 jui 11:55 fichier1
-rw-r--r--  1 roza      staff   54K     14 jui 11:56 fichier2
-rwx--x--x  1 bob       admin    3M     14 jui 11:57 fichier3
-r-xr-----  1 john      john     1B     14 jui 11:55 fichier4
```

1. Donner le nom de l'utilisateur auquel il appartient, les droits qu'il a
    sur le fichier, ceux du groupe et des autres
2. Quel est l'équivalent octal du droit correspondant ?

## 7. Rendre exécutable un fichier

1. Rappeler la commande qui permet de rendre exécutable un fichier pour tous
    les utilisateurs?
2. Rappeler la manière de tester l'existence d'un fichier.
3. Utiliser ces connaissances pour construire un script `rendExecutable` à un
    argument qui teste si cet argument désigne un fichier existant, et le
    rend exécutable si besoin.

    Pour tester si un fichier est exécutable, on peut utiliser le test
    similaire ;

    ```bash
    if [ -x $fic ]
        then
            echo "Le fichier $fic est exécutable"
        else
            echo "Le fichier $fic n'est pas exécutable !"
    fi
    ```

## 8. Rendre exécutable plusieurs fichiers

1. Rappeler comment on accède à la liste des arguments d'un script.
2. Ceomment parcourir cette liste dans un script ?
3. Utiliser ce parcours pour proposer un script `ajouteDroits.sh` qui attend
    en entrée une liste de fichiers et les rend tous exécutables (si besoin).


