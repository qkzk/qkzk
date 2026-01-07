---
title: TP Shell
author: qkzk
bookCollapseSection: true
date: 2026-01-07
theme: metropolis
weight: 10000
geometry: "margin=1.5cm"

---

Point de départ : une machine bootée sous linux. Machine virtuelle, clé live, OS principal... toutes les solutions sont bonnes.

# Shell 

## Exercice 1 : manipuler l'arborescence

Commandes employées : `pwd, cd, mkdir, touch, cat, echo, rm, rmdir, tree`

1. Si ce n'est pas déjà le cas, ouvrez un émulateur de terminal.
2. Lire rapidement la documentation de chacune de ces commandes ainsi que quelques exemples. Par exemple `man pwd`.
3. Dans quel dossier vous situez-vous ?
4. Quels sont les fichiers et dossiers, cachés ou non qu'il contient ?
5. En n'employant que des commandes du shell, reproduire l'arborescence dans le dossier courant.

    ```
    `-- a
        |-- b
        |   |-- c.txt
        |   `-- d
        |       `-- e.txt
        `-- f
            |-- g
            |   `-- h.txt
            |-- i.txt
            `-- j
                |-- k.txt
                `-- z.txt
    ```

    Afin de disintguer facilement les fichiers normaux des dossiers, tous les fichiers ont la même extension : `.txt`

    On trouvera sur mon site de la documentation sur ces commandes.
6. Écrire dans un fichier.

    Il est courant de devoir accéder à une machine distante sans disposer d'interface graphique. Alors on doit pouvoir écrire dans un fichier sans employer d'éditeur de texte comme sublime text.

    Deux approches sont possibles : 

    1. Envoyer un contenu depuis une commande shell. Par exemple :

        ```sh 
        echo "bonjour" > hello.txt
        ```

        Va écrire "bonjour" dans hello.txt.

        On peut ensuite consuler le contenu avec `cat hello.txt`

    2. Utiliser un éditeur en mode texte, comme `nano`. De nombreuses alternatives existent : `vi, vim, nvim` sont des éditeurs puissants, `vim` et `nvim` autant que sublime text ou vscode.

    Consignes :

    1. Écrire "l'info c'est cool" dans `info.txt`
    2. Éditer ce fichier avec `nano info.txt` et y ajouter votre recette préférée. Sauvegarder le fichier.

## Exercice 2 : exécuter et arrêter un programme

Nous allons simuler une situation courante : vous devez arrêter et relancer un programme qui a planté.

Voici un script python qui ne fait pas grand chose mais tourne indéfiniment :

```python 
#!/usr/bin/python3

from time import sleep

while True:
    sleep(3)
```

1. Que fait-il ? Documentez-vous sur le _shebang_ : `#!/usr/bin/python3` si nécessaire.
2. Créez un fichier `boucle_infinie.py` et taper le script précédent.
3. Quitter l'éditeur et rendre le fichier exécutable avec `chmod +x boucle_infinie.py`
4. Exécutez le fichier avec `./boucle_infinie.py`.
    Le shebang permet au shell de savoir quel programme choisir pour lancer le script, ici `/usr/bin/python3` qui est l'adresse courante de Python sous linux.
5. Arrêter le script avec `Ctrl+c`. Vous devriez récupérer la main sur la machine.
6. Exécuter le script en fond de tâche avec `setsid python3 ./boucle_infinie.py`. Si tout se passe bien, votre programme s'exécute indéfiniment et vous récupérez la main sur le terminal. Vous pouvez à nouveau taper des commandes !

    C'est exactement la situation présentée dans l'introduction : un programme s'exécute indéfiniment et vous devez l'arrêter.

7.  - Documentez-vous sur `kill` 

    - Qu'est-ce que le `PID` d'un processus ? Et le `PPID` ? Il n'est pas évident d'accéder au pid d'un processus. Un des moyen de retrouver le processus est la commande `top`. Que fait-elle ?

    
    - Avec `ps -ef | grep python` déterminer le PID du processus lancé plus tôt.
    - L'arrêter avec `kill`

    
8. D'autres programmes Python sont-ils en cours d'éxécution ? Lesquels ?

9. Lors de l'exécution de `ps -ef | grep python` on a employé une redirection de la sortie d'une commande `ps -ef` vers une autres `grep python` avec la redirection `|` _pipe_, tuyau en français.

    `ps -ef` affiche tous les processus en cours d'exécution, dans un tableau assez complet. Il présente le PID et PPID, PID du parent.

    `grep python` filtre les lignes et ne garde que celles qui contiennent le mot `python`.

    1. Quel est le PPID du processus `boucle_infinie.py` crée plus tôt ?

    2. Ouvrir un second terminal. _Cela n'est possible que si vous avez accès à l'interface graphique sinon zappez la question._ 

        Déplacez vous jusqu'au script `boucle_infinie.py` et exécutez le normalement `./boucle_infinie.py`

        Dans **l'autre terminal** retrouver le PID et PPID. 

        À quoi correspond le PPID du script que vous venez d'exécuter ?

        Expliquer la différence entre les deux.

        Arrêtez tous les scripts Python que vous avez lancé avec `kill`.
 

En résumé :

Lors du démarrage du système, le noyau linux crée un premier processus appelé `init` et de `PID` 1. Il n'a pas de parent. Tous les processus exécutés sont des "enfants" d'init. Lorsqu'on exécute une commande, elle devient un processus dont le parent est le processus du terminal en cours.
Avec `setsid` on crée un processus dont le parent est `init` lui même. Cela permet de garder la main sur le terminal. `ps` permet de retrouver les processus et `kill` de les arrêter. Ce ne sont pas les seuls usages de ces commandes.

## Exercice 3 - droits d'utilisation et propriétaire

La commande `ls -lah` affiche notamment les droits d'utilisation `drwxrwxrwx` et le propriétaire `premierensi` des fichiers qu'elle présente.

- Le propriétaire c'est simple : à qui appartient le fichier ?
- Le groupe, c'est déjà plus délicat. Les groupes permettent de donner des droits d'accès à de multiples utilisateurs, par exemple, l'accès au bluetooth ou aux disques peut-être donné en incluant un utilisateur dans un groupe particulier.
- Les droits d'utilisateur ou _permissions_ sont présentées par une chaîne (ou un entier souvent noté en octal...) et indiquent :

    - `d` ou `-` : que c'est un dossier ou un fichier normal. Des variantes existent `c`, `p`, `b` etc. on n'en parlera pas dans ce TP 
    - `r` ou `-` : peut-on (qui est on ?) lire le fichier ?
    - `w` ou `-` : peut-on écrire dans le fichier ?
    - `x` ou `-` : peut-on exécuter ce fichier ? ou peut-on traverser ce dossier ?

    La chaîne `rwx` est répétée trois fois pour : le propriétaire, le groupe et tous les utilisateurs.

    Ainsi : `-rwxrw-r--` indique :

    - un fichier normal,
    - que le propriétaire peut lire, modifier et exécuter,
    - que son groupe peut lire et modifier,
    - que tous les utilisateurs peuvent lire.

1. Retirer les droits d'exécution de `boucle_infinie.py` avec `chmod -x ./boucle_infinie.py`. Exécuter le directement avec `./boucle_infinie.py`. Que se passe-t-il ?

    Et avec `python3 boucle_infinie.py` ? Expliquer la différence de comportement.

2. Créer un fichier avec `touch exemple.txt`. Ecrire quelque chose dedans. Retirer les droits d'écriture et recommencer. Rendre les droits d'écriture.

3. Créer un fichier, écrire dedans lire, retirer les droits de lecture et tenter de lire à nouveau. Puis rendre les droits de lecture.

4. Que fait la commande `chmod a+x ./boucle_infinie.py` ? Comparer `ls -lah` avant et après l'exécution de la commande. Retirer ces nouveaux droits.

