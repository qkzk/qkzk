---
author: qu3nt1n
date: 2016-07-01 14:20:49+00:00
draft: false
title: 01. Lexicométrie

url: /
---



Notions abordées



 	  * lexicométrie
 	  * extraction d'un texte à partir d'un pdf
 	  * encodage des caractères
 	  * python







### Projet : l'encodage d'un document et la lexicométrie (étude statistique d'un texte et interprétations).




# Introduction


L'informatique permet de traiter d'importantes quantités de données et renseigne de façon parfois surprenante sur les informations qui se dégagent d'un texte.
Quelle lettre est la plus fréquente dans un texte ? Est-ce lié à la langue dans laquelle il est écrit ? Peut-on déterminer la langue dans laquelle ce document est écrit à partir de ces informations ? Quel est le mot le plus fréquent dans un discours politique ? Une pièce de théâtre ? Peut-on déterminer la tendance d'un discours politique à partir d'une étude de ce genre ? Ces questions trouvent toutes une réponse dans la lexicométrie.
C'est un domaine actif de la recherche linguistique qui s'avère vite complexe. On réalisera bientôt pourquoi.
Notre ambition est, rassurez-vous, modeste.
Nous verrons, par la suite, quelles sont les applications concrètes de l'étude lexicométrique - nous en utilisons régulièrement.

Notre projet consistera à étudier le plus profondément possible un texte. Nous chercherons à rendre ces résultats compréhensible au commun des mortels et donc à illustrer le plus possible les informations obtenues.




# Première étape : importer et transformer un document


Il existe beaucoup de base de données d'ebooks et Altramentra est l'une d'entre-elles.




Récupérer les _Poèmes saturniens_ de VERLAINE au format pdf sur [Atramentra](http://www.atramenta.net/). Renommer ce fichier en 'verlaine.pdf' afin de le manipuler plus simplement. Il pèse 196 ko. Examinez le dans sumatraPDF (ou le lecteur installé sur votre machine) ; on y repère beaucoup de formatage.


PDF est un format de fichier développé par Adobe (Acrobat, Photoshop, Illustrator...) servant à la présentation des documents. Il est vite pénible d'éditer un PDF directement, mais c'est possible. C'est un format propriétaire mais utilisable par tous. Il est lisible sur presque toutes les machines modernes et assez simple (pour un ordinateur) à créer. Les fichiers PDF ont l'immense avantage d'obtenir le même rendu sur (presque) tous les lecteurs et s'impriment facilement. On a parfois des surprises...







**Poppler pour windows.**
Poppler permet **d'extraire du texte d'un pdf.** Vous me direz _"bah, j'ai qua l'ouvrir, tout sélectionner, copier, coller..."_ Sauf que la plupart du temps, ça ne fonctionne pas. Et que vous copierez aussi une tonne d'information inutile qu'il faudra éditer presque caractère par caractère. Pas très automatisé tout ça !
A noter que Poppler peut créer un fichier html prêt à l'affichage dans un navigateur, extraire du texte d'un ePub (format classique pour les ebooks), extraire une image d'un pdf (même au format vectoriel SVG) etc. C'est un outil très puissant mais difficile d'accès, il est souvent intégré dans des librairies de développement.
Il est disponible [ici :](http://blog.alivate.com.au/poppler-windows/)


**Télécharger le fichier "Latest binary : poppler..._x86.7z"**


Penchons-nous sur ce fichier avant de l'utiliser. Vous venez de récupérer le code source et les librairies d'une suite de petits logiciels.
Le code source est lisible sur n'importe quel système d'exploitation. Les exécutables et les librairies sont propres à chaque système : unix (linux, android, osx), windows, iOS etc.
Voilà pourquoi vos applications iPhone ne sont pas utilisables directement sous windows. Elles doivent être compilées (= traduites en langage machine) depuis leur code sources pour être rendues utilisables.
Ensuite, nous travaillons ici sous un environnement windows. Windows dispose de deux déclinaisons principales (32 bits et 64 bits) dans chaque version (10, 8, 7, xp, 2000 etc.). Les applications 32 bits sont utilisables sur toutes les versions de windows (en principe), les applications 64 bits nécessitent une version 64bits de windows et le processeur qui va avec. Ça se complique.
Nous avons récupéré la version x86 : cette version fonctionne avec les processeurs "x86 compatible" : pour les PC 32 bits. Elle devrait donc fonctionner sur tous les windows au delà de windows 7. Ce concept, appelé "compatibilité descendante" a fait la gloire du PC.
Ensuite le développeur a indiqué la version de son code (.45 au jour où j'écris cette page, le 27 juin 2016, 11h, il fait moche mais la France est en 1/4 de finale de l'euro, je suis content).
Enfin l'extension : ".7z". Elle nous indique que le fichier est compressé à l'aide de l'algorithme 7zip. Vous devriez l'avoir sur vos machines.


**Clic droit sur le fichier, 7zip, "extraire vers Poppler....". Copier ensuite le dossier Poppler sur le bureau.**


Dans ce dossier on trouve 4 sous dossiers : bin, include, lib et share.
bin contient les exécutables (généralement appelées binaries en anglais), include contient les morceaux de codes dont le développeur a eu besoin et qu'il a inclu dans son fichier. lib contient les sources et les librairies windows. La version originale de Poppler est prévue pour Unix et le développeur s'est contenté de le compiler pour windows. Share contient ce qui a été partagé des autres versions de Poppler, ici son manuel au format "man", une commande très pratique sous Unix.
Bref... un simple fichier qui semble très compliqué à utiliser.


**Rendez-vous dans bin. Déposer votre fichier verlaine.pdf dans ce dossier. Faîtes glisser 'verlaine.pdf' sur le fichier 'pdftotxt.exe'.**


Poppler s’exécute alors et crée un fichier 'verlaine.txt' dans le même dossier. OUF.
A l'avenir il vous suffira de faire de même pour extraire du texte d'un pdf.
Je réalise bien qu'il est fort possible qu'une des étapes précédentes échoue... auquel cas vous n'avancerez-plus. On trouvera donc ici le fichier texte : [verlaine.txt](http://qkzk.xyz/?attachment_id=93)

Une dernière remarque avant d'avancer. Ce que nous venons de faire, d'autres l'ont déjà fait !?! Et mieux. On trouvera [ici](http://pdftotext.com/) un site (en php je pense) prêt à l'emploi réalisant toute la démarche. Etant donné qu'il renvoie exactement le fichier que Poppler pour windows il y a fort à penser qu'il utilise une autre version de Poppler : poppler pour unix, compilée pour les systèmes unix généralement utilisées par les serveurs web.
_"Ah ouais c'est bien tout ça... mais au final j'ai simplement utilisé un .exe pour faire tout le travail ! Je pensais que j'allais apprendre à coder moi même un truc comme poppler !"_ Non... Premièrement ça nous (et je m'y inclus) dépasse totalement. Deuxièmement pourquoi réinventer la roue ? A la rigueur je peux comprendre le principe général et vous l'expliquer... mais ce qu'on trouve dans un fichier .pdf est beaucoup plus compliqué qu'il n'y parait. Le texte est entièrement formaté et ce formatage respecte des contraintes très élaborées. Un gentil développeur s'est épuisé à le faire et partage son travail, on l'en remercie.

**tl;dr** résumé :
dl poppler [ici :](http://blog.alivate.com.au/poppler-windows/) télécharger le fichier "Latest binary : poppler..._x86.7z"
décomprésser avec 7zip (clic droit) et naviguer jusque .../bin
glisser le fichier 'verlaine.pdf' sur pdftotext.exe : le texte apparait dans verlaine.txt (si ça veut pas : [verlaine.txt](http://qkzk.xyz/?attachment_id=93))
Remarquons que des sites prêts à l'emploi font de même : [par exemple](http://pdftotext.com/).


# Deuxième étape, un peu de lexicométrie


**Examen du fichier texte.**
Première remarque, il ne pèse plus que 53ko. 196 - 53 = 143ko de formatage divers... Grosso modo, le formatage occupe les 3/4 de l'espace disque. C'est énorme !


**Ouvrir 'verlaine.txt' dans notepad++**


On remarque en effet que tout le formatage a disparu. Subsistent quelques caractères étranges. On va faire le ménage.


Sélectionner un des caractères hors du commun à l’écran. Menu Recherche, Remplacer (Search, Replace) ou raccourci CTRL+H. Le caractère apparaît dans la barre de recherche (il arrive qu'il soit présenté autrement), laisser vide le deuxième champ, faire "tout remplacer" ("replace all"). Notepad++ dégage tous les caractères superflus. Recommencer avec les autres caractères étranges. Sympa Notepadd++, non ?





**L'encodage** d'un fichier indique au lecteur avec quel jeu de caractères il a été écrit. Il faut spécifier ici à Notepad++ de sauvegarder ce texte au format UTF8 (encoding UTF8), le plus couramment employé en informatique car il permet de gérer simplement la majorité des caractères d'une grande quantité de langues. Il existe des milliers (!) d'encodages possibles pour des centaines de langues...

**Courte remarque sur UTF-8. **_Ce jeu d'encodage de caractère a vu le jour dans les années 90. Il a pour objectif d'uniformiser l'encodage des documents écrits. Il existait alors des dizaines d'encodages possibles et ils n'étaient pas compatibles. Créer un document texte sur un mac et l'ouvrir sur un PC nécessitait un changement d'encodage. Les "retours à la ligne" n'étaient même pas gérés correctement. Une vraie galère. Je ne parle même pas des accents... _
_L'encodage est un problème important pour nous qui écrivons en français. Développée en anglais, l'informatique s'est longtemps peu souciée des jeux de caractères des autres langues. A l'heure des réseaux mondiaux ce n'est plus possible de l'ignorer. Si vous n'êtes pas vigilant, vous rencontrerez très souvent des problèmes d'encodage. Retenez que, dans le doute, utf8 fait l'affaire._

A la fin du ficher vous trouverez une note de l'éditeur, qu'on va dégager aussi. **Arrêtez vous à 54 FIN et virez tout ce qui suit.**


**Sauvegardez votre travail.**


Il est maintenant prêt à l'emploi !



* * *





**Créer un dossier pour le projet et y déplacer le dossier de Popper et vos deux fichiers verlaine.txt et verlaine.pdf**







**Compter dans le document : quelle est la fréquence de chaque lettre ?**
Les premiers imprimeurs l'ont vite remarqué, certaines lettres sont plus fréquentes que d'autres en français. Hormis mon nom, je ne connais que peu de [mots comportant 2 k](http://www.listesdemots.fr/c/k/2/motscontenantkk.htm). Ils sont tous importés d'une autre langue ! Hormis kéké qui est un pur import du provencal cacou (pour votre culture, vous me remercierez quand vous serez président, miss france ou ballon d'or).
Nous allons ici utiliser le langage Python pour compter les lettres de chaque mot.




Récupérer le script [count_letter.py](http://qkzk.xyz/docs/count_letter.py) et l'ouvrir dans IDLE.



    
    <code>
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    '''
    
    '''
    
    from string import ascii_lowercase     # ascii_lowercase =='abcdefghijklmnopqrstuvwxyz'
    print "Nom du fichier"
    with open('votrefichier.txt') as f:
        text = f.read().lower().strip()
        dic = {}
        for x in ascii_lowercase:
            dic[x] = text.count(x)
    print dic
    </code>


Les deux premières lignes indiquent à Python que c'est un code source Python écrit en utf8. Entre les ''' et ''' on peut écrire autant de commentaire qu'on veut, ils ne seront pas interprétés.


Ascii est un ancien encodage, la base de tous les encodages modernes. Il ne comporte que 127 caractères, bien trop peu pour toutes les langues. Tous les autres, comme utf8 (qui fait partie d'Unicode) sont construits en ajoutant (plus ou moins bien) d'autres caractères. Il en existe d'autre déclinés par régions, par exemple ISO-latin-1 qui est utilisé en France sous Windows.


La première ligne interprétée est donc `from string import ascii_lowercase` et son commentaire commençant après le symbole #
depuis (from...) la librairie string (les chaines de caractères) on importe `ascii_lowercase` (les minuscules de la table ascii). Le commentaire nous explique ce qu'on va trouver dans ascii_lowercase.
Il est nécessaire d'importer cette variable car Python ne charge pas TOUTES ses librairies au démarrage. Il ne se lance qu'avec le strict minimum et c'est au développeur d'indiquer ce dont il a besoin.
La méthode `with` permet de créer une variable temporaire, le temps de manipuler le fichier. Elle le note simplement `f`.
On note ensuite `text` le résultat de `f.read().lower().strip()` : on lit le fichier f avec .read(), on converti tout en minscule avec .lower() et on vire le début et la fin (il subsiste toujours des caractères invisibles) avec strip().
On crée un dictionnaire vide notée `dic`
On boucle ensuite dans la chaine ascii_lowercase et, pour chaque élément noté `x` de cette chaîne on ajoute un élément à dic : `dic[x]`. Ce tableau dic sera donc indexé par la lettre en question. Cet élément du tableau est le résultat de `text.count(x)` : le comptage de la lettre x dans texte = combien de fois cette lettre est elle apparue !
La boucle est terminée, l'utilisation du fichier aussi, on désindente jusqu'à la gauche et on affiche dic

En 10 lignes de code (volontairement détaillées, on peut écrire ça en 2 ou 3 lignes), on compte tous les caractères d'un fichier texte.


**Editer le fichier source** en remplaçant 'votrefichier.txt' par 'verlaine.txt' et "Nom du fichier" par "Verlaine". Exécuter alors ce script. Quel est le résultat ?







Votre programme pose problème, ascii_lowercase ne tient pas compte des accents ! Dommage pour nos é è à ù et autres... Verlaine en utilise pourtant et ils devraient figurer.
Créer un fichier 'verlaine_sansaccent.txt' avec notepad++ contenant le même texte mais dans lequel tous les accents ont été remplacés par leur lettre sans accent : à -> a, é -> e etc. (Pas à la main kéké, réfléchis un petit peu...)
**Recommencer le comptage avec ce nouveau fichier.** Obtient-on les mêmes résultats ?




On aimerait maintenant afficher aussi le nombre de caractères accentués individuellement. Dans 'count_letter.py' ajouter une deuxième partie en copiant les lignes de `from` à `dic`.
Modifier votre code de façon à faire apparaître sur le même écran les contenus des deux tableaux : dic qui contient les comptages des lettres sans tenir compte des accents et dic_accents qui contient les lettres en les distinguant de leurs versions accentuées.





**Fréquence des lettres**
On n'affiche ici que le nombre d'occurence d'une lettre, pas sa fréquence. A l'issue de la boucle, dic contient toutes les informations dont on a besoin pour le faire.


Ajouter à votre programme une partie supplémentaire dans laquelle une nouvelle variable `total` contient la somme de toutes les occurrences contenues dans dic. On pourra créer une boucle `for k in dic: `




Créer ensuite un nouveau dictionnaire `frequences` qui contient la fréquence de chaque élément (fréquence du f = nombre d'occurence du f / nombre total de lettres).
Attention, en Python 2.7 la division est ENTIERE, comme celle que vous aviez appris à l'école (en 6eme ?). 3/2 renvoie 1 et pas 1,5...




Pour forcer une division à virgule on utilise 3/float(2) qui renvoie 1,5. (float = nombre à virgule flottante).




Comparer les résultats de Verlaine à ceux de la [langue française](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres_en_fran%C3%A7ais). Verlaine écrit-il en Français ?







Reprendre ce travail avec une oeuvre du corpus de Français étudiée cette année. On se contentera d'une oeuvre assez ancienne pour être libre de droits.
Recommencer avec _La disparition_ de GEORGES PEREC [(here)](http://www.oasisfle.com/ebook_oasisfle/georges_perec_la_disparition.pdf). Rien d'anormal ? Que dire de _Les revenentes_ du même auteur ?


Nous n'irons pas plus loin pour l'instant dans l'analyse fréquentielle. On laisse les procédés de comptage en suspend pour l'instant... Nous allons utiliser ce programme pour la cryptographie et, en particulier, le cassage des codes secrets !
**Une dernière remarque.**
Tout ce qu'on vient de faire : récupérer un fichier .pdf à une certaine adresse, en extraire le texte, compter les fréquences de chaque caractère etc. Python peut le faire seul... mais c'est un peu difficile pour vous. Et je ne suis même pas certain que tout soit possible sur les PC du lycée compte tenu de certains réglages (intégrer Poppler à Python en particulier). A l'origine, c'est ce que je voulais vous faire faire et, si j'en ai le temps, je l'aurais fait pour la rentrée et pourrais vous montrer ce que ça donne. Rien de bien méchant, juste 40h à trouver les bonnes librairies et les installer.
Si vous êtes chaud chaud chaud et trouvez tout ça bidon, libre à vous d'essayer ! :)
