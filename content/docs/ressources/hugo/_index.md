---
title: "Hugo"
bookCollapseSection: true
author: "qkzk"
weight: 2

---

# Hugo

[Hugo](https://gohugo.io/) est un concepteur de sites statiques.

Il permet de convertir automatiquement des documents markdown en html
et de créer l'arborescence du site.

Le principe est simple :

1. installer hugo
2. créer un site avec `hugo new site nom_du_site`
3. `hugo server` sert votre site localement.
4. `hugo deploy dossier_de_destination` crée les fichiers html automatiquement.

# Héberger le site

Github propose d'héberger un site statique. Ils proposent une solution
complète avec Jekyll mais j'ai préféré hugo qui me semblait mieux documenté
et plus rapide.

Le principe est de créer un dépôt public `mon_depot` et d'activer les **github pages**.

Ensuite on push les fichiers html sur `mon_depot`.

Et voilà, le site est en ligne.

[Tutoriel](https://developer.mozilla.org/fr/docs/Learn/Common_questions/Using_Github_pages) sur les github pages.

# Nom de domaine

Pour personnaliser une URL il faut un nom de domaine. Cela n'est pas onéreux
mais c'est la seule étape non gratuite. J'ai utilisé [Hostinger](https://www.hostinger.com/).

# Thème

Le thème que j'utilise s'appelle [Book](https://themes.gohugo.io/hugo-book/).

J'héberge _des cours_, je voulais donc une navigation aisée :

* au sein du site,
* dans le document lui même.

Ce thème est le seul que j'ai trouvé qui réunisse ces deux critères.

J'aurais pu en écrire un, mais pourquoi réinventer la roue ?

# Latex

Par défaut, hugo ne supporte pas latex. C'est qu'il existe des dizaines
de logiciels pour convertir du markdown en whatever mais qu'ils ont choisi
un moteur ne le faisant pas...

Il y a essentiellement deux options :

* [mathjax](https://geoffruddock.com/math-typesetting-in-hugo/)
* [katex](https://eankeen.github.io/blog/posts/render-latex-with-katex-in-hugo-blog/)

mathjax demande d'inclure un peu de Javascript, katex se configure 

# Dessiner des graphes

Le format courant pour représenter les graphes est `DOT` de la suite `GraphViz`.
C'est un format assez simple mais très riche.

Là encore, pas de support immédiat. Plusieurs approches :

* convertir les graphes à la main avec  `dot` : pénible
* convertir avec un filtre et joindre le fichier en ligne : un peu moins,
* utiliser [gravizo](https://www.gravizo.com/)

    <img src='https://g.gravizo.com/svg?
     digraph G {
       main -> parse -> execute;
       main -> init;
       main -> cleanup;
       execute -> make_string;
       execute -> printf
       init -> make_string;
       main -> printf;
       execute -> compare;
     }
    '/>

    Cela demande donc de changer deux lignes du document et d'enlever les lignes
    blanches, considérées comme de nouveaux paragraphes en markdown

L'autre format courant de graphes est mermaid. Voici [comment faire](https://codewithhugo.com/mermaid-js-hugo-shortcode/). 
