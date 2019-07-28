---
author: qu3nt1n
date: 2016-07-02 00:05:21+00:00
draft: false
title: 3.4 Structure des pages HTML
weight: 4
---






Notions abordées


* compléments HTML : balises, caractères spéciaux








# Page HTML






Nous avons déjà complété un fichier HTML dont la structure était
donnée.  Nous allons maintenant découvrir différentes balises. Pour
mémoire, un fichier HTML est du texte dont les catégories de mise en
page et de mise en forme sont indiquées par des balises (appelées tag
en anglais). Un exemple de fichier HTML simple est donné (cf.
[ex_html1.html](http://qkzk.xyz/docs/doc03/ex_html1.html)).





La partie `<head>` contient, entre autre, les
informations destinées au navigateur pour qu'il affiche correctement
la page et pour faciliter le travail des moteurs de recherche.  La
partie `<body>` contient le contenu de la page qui
est affiché par le navigateur.






## Entêtes des fichiers HTML `<head>`






Une des informations donnée dans l'entête est le codage des caractères
utilisé pour écrire la page web, grâce à la balise ci-dessous.





    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"></meta>





Elle indique que le codage de caractères utilisé pour le fichier
est de l'UTF-8 dans cet exemple.







**Importance du codage.**



1. Ajoutez la balise de codage donnée précédemment dans le fichier exemple,
à l'intérieur de la balise `<head>`, en première
position.
2. Ouvrez le fichier dans votre navigateur. Est-ce que le texte
est lisible ?
3. Si non, pourquoi et comment faire pour qu'il s'affiche
correctement ?








## Caractères spéciaux






Nous venons de voir que le codage du fichier source HTML doit être le
même que celui utilisé par le navigateur pour lire les informations, sinon
l'affichage des lettres qui ne font pas partie du code ASCII n'est pas
correct.





Une façon de s'affranchir du codage est de ne pas utiliser ces
caractères spéciaux, mais leur codage à l'aide des entités HTML. Par
exemple, le 'é' est codé par `&eacute;` où eacute est
le nom du caractère précédé de `&` et suivi de
`;`.





Dans les tableaux de la page [http://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references](http://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references)
vous trouverez tous les noms des caractères spéciaux dans la colonne
"name". Il suffit de les entourer de `&` et
`;` pour les utiliser dans une page web. Dans les faits,
les entités ne sont pas utilisées pour représenter les caractères
accuentés, par contre d'autres caractères spéciaux doivient être
représentés à l'aide des entités comme les symboles `<`
et `>` qui sont les marqueurs des balises, mais qui
peuvent aussi être des caractères utilisés dans le texte d'une page
web.







**Utilisation des caractères spéciaux.**


En vous aidant des tableaux des entités HTML, faites en sorte que le
texte suivant aparaisse dans votre page, affichée par votre navigateur :
`5 € > 4 €`







## Les balises des éléments de bloc






De nombreuses balises permettent de spécifier dans quelle catégorie
de mise en page se trouve un texte (est-ce qu'il s'agit
d'un titre, d'un paragraphe ou d'une liste… ?). Ces balises délimitent les
éléments dit de bloc (ou boites). Tout texte ou élément présent dans une page HTML
doit être dans une balise d'élément de bloc. Ces balises doivent être
ouvertes et fermées. Les blocs ainsi générés par ces balises sont indépendants
et structurent les pages web. Il y a un saut de ligne avant et après leur
contenu. Par défaut, deux éléments de bloc sont l'un en dessous de l'autre.
Exemples de balises HTML délimitant des éléments de bloc :





~~~html
<h1>Ceci est un titre de niveau 1</h1>
<h2>Ceci est un titre de niveau 2</h2>
<h3>Ceci est un titre de niveau 3</h3>
<p>Ceci est un paragraphe</p>
<ul>
	<li>Ceci est un élément d'une liste non numérotée</li>
	<li>Ceci est un 2ème élément d'une liste non numérotée</li>
</ul>
<ol>
	<li>Ceci est un élément d'une liste numérotée</li>
	<li>Ceci est un 2ème élément d'une liste numérotée</li>
</ol>
~~~







**Découverte des balises des éléments de bloc**

Copiez-collez ce texte avec balises dans votre page web et observez
la mise en forme produite.







## Les balises des éléments en ligne






D'autres balises viennent compléter les éléments de bloc, celles des
éléments en ligne. Elles ont plusieurs fonctions comme préciser la mise
en forme de parties du texte (mise en gras, en italique, en couleur…) ;
la création de liens hypertextes ou encore l'insertion d'images. Leur contenu
est en continu avec le contenu qui les contient, sans séparation. Vous avez
pu constater lors de l'activité 1 que les images sont bien des éléments en ligne
puisqu'elles s'insèrent au milieu du texte, sans retour à la ligne. Un élément
en ligne est forcément inclu dans un élément en bloc. Exemples de balises HTML 
délimitant des éléments en ligne :






~~~html
<p>Ceci est un paragraphe avec des éléments en gras
ou en italique. Il y a un retour à la ligne à la fin de
cette phrase <br></br>. C'est une balise qui ne se ferme pas.
Il y a aussi un <a href="http://fr.wikipedia.org/wiki/URL">lien hypertexte</a>
vers un autre site et une image
<img src="http://upload.wikimedia.org/wikipedia/commons/4/4a/Commons-logo.svg"></img>.
</p>
~~~






**Découverte des balises des éléments en ligne**

Copiez-collez ce texte avec balises dans votre page web et observez
la mise en forme produite. Vous remarquerez que l'image apparait en
grand dans la page. Les attributs `height=""` et
`width=""` permettent de changer la taille d'une image, en
précisant les valeurs désirées en pixels. Essayez de donner à l'image
une taille raisonnable.








**Correction de fichier HTML.**



1. Affichez le fichier [ex_html2.html](http://qkzk.xyz/docs/doc03/ex_html2.html) dans
votre navigateur. Est-ce que l'affichage semble correct ?
2. Ouvrez le
fichier à l'aide de votre éditeur de texte et corrigez les erreurs de
syntaxe HTML.
3. Affichez de nouveau le fichier et vérifiez que
l'affichage est conforme à ce qui est attendu.
4. Une fois que vous
pensez avoir corrigé toutes les erreurs, testez votre fichier à l'aide
du validateur du consortium W3C : [http://validator.w3.org/](http://validator.w3.org/)
5. Au fur et à mesure de vos corrections, complétez la liste des conseils
pour avoir une page web valide. Votre enseignant collectera les différents
conseils ajoutés afin de constituer une liste la plus complète possible.
