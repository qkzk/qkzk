---
title: "Résumé des commandes bash"
author: qkzk
theme: metropolis
weight: 3
---

### pdf [pour impression](/uploads/docsnsi/architecture/linux/correction_linux_debian_intro.pdf)

# TP Linux "débian".

# Correction : liste des commandes rencontrées :


## Naviguer
* `ls` : liste les fichiers du dossier courant
* `ls -lah` : affiche aussi les fichiers cachés, avec les détails et les tailles dans des unités compréhensibles
* `cd` : change le dossier courant. `cd ~` vous envoie dans votre dossier. `cd ..` remonte d'un étage. `cd \` vous mène à la racine.
* `pwd` : (print working directory) : affiche l'addresse du dossier courant.

## Créer, effacer
* `cp` : Copie un fichier de départ vers une nouvelle destination `cp cassoulet.txt /home/robert/recettes/` va ajouter le fichier cassoulet.txt au dossier recettes.
* `mv` : Déplace un fichier. On peut le déplacer dans un dossier, ou lui attribuer un nouveau nom au passage.
* `touch` : Accède aux propriétés d'un fichier. Si un fichier existant est fourni, sa date d'édition est mise à jour. S'il n'existe pas il est crée.
* `mkdir` : "MaKe DIRrectory". Crée un dossier. `mkdir -p dir1/dir2/dir3` pour créer les dossiers intermédiaires si nécessaire.
* `rm` : Efface un dossier. Avec `rm -r` on efface récursivement et avec l'option `f` on "force". Danger : pas de confirmation sous UNIX.

## Utilitaires
* `clear` : Descend la console d'une centaine de lignes (vide le terminal...).
* `cat` : Concaténer. Nombreux usages, le plus courant est d'afficher le contenu d'un fichier dans la console.
* `top` : Gestinnaire de tâches. Il en existe de nombreux. Les plus connus sont `htop` et `glances`. On peut faire la même chose que dans celui de windows, mais en utilisant des racourcis clavier.
* `less` : Permet de "pagigner" un contenu. `less longfichier.txt` vous l'affichera en plusieurs pages.

## Processus
* `ps` : Affiche une vue _instantannée_ des processus (!= programme) en cours. Un programme c'est du texte. Un processus est un programme en cours d'exécution.
* `ps -ef` : affiche tous les processus (Every) Formatés dans une table. Renvoie trop de lignes pour qu'on lise facilement. On peut tuyauter vers less : `ps -ef | less` ou ...
* `grep` : filtre un contenu. Utilise des expressions régulières (bac +3 mais vous en verrez partout) ou de simples textes.
* `ps -ef | grep bidule` : affiche tous les processus qui tournent et dont une info (l'adresse, le nom, un paramètre...) contient le mot bidule.
* `kill` : Arrête un processus avec son numéro (PID : Processus IDentifiant). Si la commande ci-dessus vous indique que le PID de bidule est 1234, on fait `kill 1234`


## Réseau et accès distant
* `ip a` : Affiche toute la configuration réseau actuelle. On voit toutes les interfaces réseau et les adresses IP et mac
* `ping` : Envoie une requête (ICMP pour les curieux) à une adresse. On peut lui passer une adresse IP ou un nom de domaine.

    On voit apparaître un temps mesurant la durée de trajet.
* `ssh` : Ouvre un terminal sécurisé vers une machine distante. On doit alors s'authentifier (avec login/mdp ou automatiquement) et on peut taper des commandes directement sur la machine.
* `ssh pi@192.168.1.1` : Ouvre un terminal sur la machine 192.168.1.1 avec l'utilisateur pi

## Permissions, utilisateurs
* `chmod` : change les permissions d'un fichier. Elles sont déclinées pour le propriétaire, son groupe et les autres. Trois attributs : lire, écrire, exécuter.
* `chmod +x` : rend un fichier exécutable (ça n'empeche pas de planter si c'est une image, par exemple) POUR SON PROPRIÉTAIRE.
* `chmod 755` : 7 = 4 + 2 + 1 = tous les droits, 5 = 4 + 1 (lire, exécuter). Le propriétaire peut tout faire, les autres peuvent lire et exécuter.
* `su` : Passe en mode super utilisateur (root). Généralement il faut s'authentifier.
* `sudo commande` : Exécute une commande en mode super utilisateur. C'est possible si l'utilisateur courant est dans le groupe "sudo"
* `chown` : Change le propriétaire d'un fichier.


## Correction : exercice sur les redirections

1. J'aimerais afficher la liste des fichiers de /bin... mais je sais qu'il en a 4374 sur mon système actuel... Utiliser une rediction pour les afficher page par page. On pourra relire la documentation de less

~~~shell
$ ls /bin | less
~~~
2. Ecrire une commande d'une ligne qui envoie cette liste de fichiers (tout d'un coup) dans le fichier /home/pi/contenu_dossier.txt

~~~shell
$ ls /bin >> /home/pi/contenu_dossier.txt
~~~
3. Utiliser une redirection pour écraser ce contenu en le remplaçant par celui du dossier /dev
Toujours avec une redirection, ajouter le contenu de /lib à la fin du même fichier.
Utiliser cat, grep et une redirection pour trouver dans le fichier, les lignes contenant la chaîne ls

~~~shell
$ ls /dev > /home/pi/contenu_dossier.txt
$ ls /lib >> /home/pi/contenu_dossier.txt
$ cat /home/pi/contenu_dossier.txt | grep ls
~~~
