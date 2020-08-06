---
title: "Github"
author: "qkzk"
date: "2020/08/04"
weight: 100

---


### pdf : [diaporama](/uploads/docnsitale/organisation/github.pdf)

# 0. L'outil

1. Nous allons utiliser Git et Github pour PUBLIER les énoncés.

. . .

2. JAMAIS POUR RENDRE UN TRAVAIL.

. . . 

3. git est un outil très puissant dont nous n'allons utiliser qu'une toute
    petite partie.

# 1. Git

## git

Git est un système de contrôle de version gratuit et open source conçu
pour gérer efficacement et rapidement tout type de projet.

Il a été crée dans les années 90 par Linus Torvald (le créateur de Linux).

Git est le système de contrôle de version le plus employé dans le monde.

## utilisation locale : installation

Git (le programme) est installé sur vos postes. Pour installer git chez-vous,
ce que je vous conseille de faire, il vous suffit de télécharger la bonne version
depuis [leur site](https://git-scm.com/downloads).

## utilisation locale : principe

`git` permet de synchroniser des fichiers entre un dépôt local et un distant.

1. On crée un dossier local et on exécute `git init`

. . .

2. On crée un dépôt distant portant le même nom.

. . .

3. On ajoute les fichiers à suivre avec `git add .`

. . .

4. Enregistrer localement : `git commit -m "message"`

. . .

5. On ajoute la référence au dépôt distant avec\
    `git remote add origin git@addresse.git`

. . .

6. Pousser : `git push -u origin master`

Là vos fichiers sont synchronisés.

. . .

Seules les étapes 3, 4 et 6 sont à refaire pour synchroniser à nouveau.

## utilisation distante et synchronisés d'un nouveau dépôt local

1. à l'adresse du dépôt on voit apparaître les changements

. . .

2. On peut récupérer le projet complet en copiant l'adresse du dépôt
    et en exécutant :\
    `git clone git@adresse.git`

. . .

3. Une fois le dépôt cloné, on récupère les mises à jour avec :\
    `git pull origin master`



# 2. Github

* [github.com](https://github.com) est un site qui héberge des dépôts git.
* C'est le site de dépôt le plus populaire.
* Github appartient à Microsoft (depuis 2018) qui l'a racheté pour 7.5 milliards de dollars.
* Github ajoute à git quelques outils (dont les organisations) simplifiant la collaboration.
* Github permet aussi d'ajouter et de modifier des fichiers sans utiliser de client local.


### Rendez vous sur [https://githbub.com](https://github.com)

# 3. Créer un compte

1. Utilisez vos identifiants **prenom.nom@ldf.fr** pour créer un compte.
2. Rendez-vous sur Gmail pour vérifier que vous recevez les messages de Github
3. Vous devriez avoir reçu (dès que je l'aurais envoyé !) une invitation à
    rejoindre une classe.

# 4. Rejoindre l'organisation

* Le nom de l'organisation dont vous allez faire partie est "NSI-T-2021".
    2021 pour la promotion 2020/2021. Les années devraient suivre, faites attention.

* Cette organisation contient un dépôt : [Tale_nsi_2021](https://github.com/NSI-T-2021/Tale_nsi_2021)

* En tant que membre, vous pouvez consulter les énoncés déposés.
* Vous ne POUVEZ PAS et NE DEVEZ PAS les modifier. Ces énoncés servent de référence.

# 5. Cloner le dépôt

1. Créez un dossier dans votre espace de travail `nsi_github_enonces` et ouvrez
    le dans un terminal. 

. . .

2. Clonez le dépôt :\
    `git clone https://github.com/NSI-T-2021/Tale_nsi_2021.git` (bouton vert, copier)

. . .

4. **NE MODIFIEZ JAMAIS DIRECTEMENT CE DOSSIER OU SON CONTENU**.\
    Vous ne ferez que récupérer les modifications `git pull origin master`

. . .

5. Vérifiez que vous avez récupéré les énoncés complets.

# 6. Traiter un sujet d'exemple

1. Créez un dossier `nsi_github_reponses` dans lequel vous allez travailler

. . .

2. Copier le dossier `prog/recursivite/td` depuis l'énoncé 
    depuis les énoncés vers les réponses (respectez l'arborescence par commodité).

. . .

3. Vous travaillez dans vos réponses normalement.

# 7. Rendre le travail correspondant sur classroom

1. Si un travail est à rendre sur classroom, vous aurez toujours un lien vers
    la page github correspondante.

2. Vous pouvez faire "rendre le travail" comme d'habitude et publier vos
    réponses.

3. En aucun cas vous ne devez tenter de modifier le dépôt des énoncés.

# 8. Résumé pour l'usage courant

1. On suppose que vous avez correctement inialisé un dépôt local des énoncés.

. . .

2. Ouvrir le dossier des énoncés dans un terminal,

. . .

3. Récupérer les modifications : `git pull origin master`

. . .

4. Copier le dossier qui vous intéresse dans le dossier réponse.

. . . 

5. Travailler (lol) dans le dossier réponse.

. . .

6. Rendre sur classroom si c'est demandé.

# 9. Références

1. Vidéo de présentation par [Graven](https://www.youtube.com/watch?v=gp_k0UVOYMw)
2. [Git](https://git-scm.com/)
3. [Github](https://github.com/)
4. [Tutoriel complet](https://perso.liris.cnrs.fr/pierre-antoine.champin/enseignement/intro-git/)
