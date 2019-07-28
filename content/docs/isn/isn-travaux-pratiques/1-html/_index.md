---
author: qu3nt1n
date: 2016-07-01 18:06:16+00:00
draft: false
title: 1. html
weight: 1
---




# Informatique et sciences du numérique.




Ce premier atelier conduit à une recherche documentaire sur un concept ou une personne en relation avec l'informatique.

Une restitution sous la forme de page web permettra de partager les résultats de ces recherches.




## Définissons l'informatique et les sciences du numérique







**À vos moteurs de recherche !**


Chaque binôme s'empare d'un sujet parmi les propositions suivantes :



1. Qui est **Alan Turing** ?
2. Qui est **John von Neumann** ?
3. Quelle est la **place du numérique** dans les objets de la vie quotidienne ?
4. Qu'est-ce qu'un **système d'exploitation** ?
5. Qu'est ce qu'un **logiciel** ?
6. Qu'est-ce qu'un **algorithme** ? Un **langage de programmation** ? Pourquoi y a-t-il tant de langages ?
7. Comment fonctionne **Wikipédia** ?
8. Qu'est-ce qu'un fichier, un **fichier texte** ? Éditeur de texte et traitement de texte, quelle différence ?






**Approfondissons.**On traitera une des questions précédentes.



* On s'aidera bien entendu de recherches sur le web. Il n'est cependant pas interdit de fréquenter une bibliothèque !
* On pourra consulter directement [Wikipédia](http://fr.wikipedia.org/).
* On profitera des articles [d')i(nterstices](http://interstices.info/)
* On ne manquera pas de  citer ses sources en fournissant par exemple leur [URL](http://fr.wikipedia.org/wiki/Uniform_Resource_Locator).






Recherche sur le web ? [Pourquoi ne dit-on pas recherches sur l'Internet](http://interstices.info/idee-recue-informatique-10) ? Cette question est l'une de celles auxquelles nous allons répondre ici !





## Une page HTML de restitution




Il s'agit de présenter une synthèse du travail de recherche réalisé sur une des questions précédentes. Pour produire un tel document, un format adapté doit être choisi. Il faut pouvoir structurer le document : indiquer son titre, le titre de parties ou de chapitres. Il faut pouvoir mettre en évidence certains mots, par exemple en gras ou en italique. Des tableaux, des schémas, des images doivent pouvoir être insérés dans le document. De multiples formats sont utilisés. Parmi l'ensemble des formats possibles, nous retiendrons le HTML (Hypertext Markup Language).

Le format HTML est particulièrement utilisé pour produire les pages web. Un fichier HTML est un simple fichier texte. Il est donc possible de le produire ou modifier à l'aide d'un éditeur de textes.




Un logiciel de **traitement de texte** n'est pas un **éditeur de textes**. Cette question fait l'objet d'une des recherches menées ici !

Quel éditeur de textes utiliser ? Selon l'environnement de travail, on pourra choisir [Notepad++](http://fr.wikipedia.org/wiki/Notepad%2B%2B) (qui ne fonctionne que sous Windows), [SublimeText](https://www.sublimetext.com/) sur toutes les plateformes.

Ce fichier HTML qui n'est qu'un simple fichier texte va être **interprété** par un **navigateur web** qui rendra les titres sous une certaine forme, affichera en gras ou en italique les caractères devant l'être, permettra de suivre des liens sur d'autres pages web ou d'autres sites web, etc.






Nous utiliserons exclusivement [Chrome](http://www.google.com/chrome/) ou firefox.




### HTML : 2 "aspects" - source et rendu







**Voir le code source d'une page**.
Dans le menu du bouton droit de la souris, sélectionner "_Code source de la page_" (sous Firefox) ouvre une fenêtre qui affiche le code HTML de la page. Comparez le code source de votre future page et celui de la page en cours..




Soit le code HTML suivant :

~~~html
<!-- Ceci est mon premier fichier HTML -->
<!DOCTYPE html>
<html>
<head>
    <title>Mon premier fichier HTML</title>
</head>

<body>
<h1>Section une</h1>  <!-- titre de la 1re section -->

<p>Mon premier paragraphe. Ces <b>deux mots</b> sont en gras.</p>

<p>Ce second paragraphe termine la section une.</p>

<h1>Section          deux</h1>

<p>Que pensez-vous du paragraphe suivant.</p>
<p>Martinus agens illas provincias pro praefectis aerumnas innocentium
malivolus tandem desineret

quieti coalitos homines in aperta pericula
proiectare.</p>

</body>
</html>
~~~

Ce contenu a été sauvegardé dans un fichier nommé `premier-html.html`. Vous pouvez en visualiser le rendu en cliquant sur le lien suivant : [premier-html](http://qkzk.xyz/wp-content/uploads/2016/07/premier-html.html) .






**Rendu de mon premier fichier HTML.**
Observez attentivement le rendu dans votre navigateur du fichier **premier-html.html**


en parallèle du code HTML de ce fichier.



* Comment le titre de la page est-il rendu ?
* Comment les caractères entre `<!--` et `-->` sont-ils rendus ?
* Les caractères espaces sont-ils significatifs ?







## Le format HTML




Détaillons le code HTML.

En premier lieu, remarquons que le code HTML est structuré à l'aide de balises.



* Les balises sont encadrées par les caractères `<` et `>` ou `<` et `/>`.
* Les balises s'utilisent comme des parenthèses : à la balise ouvrante `<h1>` correspond la balise fermante `</h1>`.
* Les balises peuvent être imbriquées, par exemple les balises `<b>`–`</b>` des deux mots rendus
en gras au sein des balises `<p>`–`</p>` du premier paragraphe.

Notre exemple débute par une ligne `<!DOCTYPE html>
`
qui indique que le fichier respecte la norme HTML basique, norme de 1991. Nous préférerons utiliser une norme plus récente telle XHTML 1.0 et préciser dans notre document :

~~~html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
~~~




Les balises utilisées dans l'exemple précédent sont :




* Les balises `<html>`-`</html>` délimitent le code HTML qui comporte deux grandes parties, l'entête et le corps.
* Les balises `<head>`-`</head>` délimitent l'entête du document. Cet entête permet de préciser des informations générales sur le document tel que le titre comme nous le faisons ici. L'entête contient éventuellement d'autres informations tels qu'une brève description du document, des mots-clés, le nom du ou des auteurs du document, etc.


Quelle est l'utilité des informations fournies dans l'entête d'un document HTML ? À quoi peuvent servir les mots-clés ou la description fournis ? Nous avons déjà vu comment le titre du document
pouvait être rendu. Toutes les informations contenues dans l'entête sont elles exploitées par le navigateur web ?




* Les balises `<body>`-`</body>` définissent le corps du document. C'est dans ce corps que nous allons trouver le contenu du document : texte, images, etc.
* Les balises `<h1>`-`</h1>` indiquent le titre d'une section de premier niveau. Des titres de niveaux inférieurs peuvent être définis, par exemple `<h2>`-`</h2>`, puis `<h3>`-`</h3>`, etc.Les titres de sections sont des éléments importants d'un document HTML. Deux aspects sont à considérer :

* le rendu par le navigateur web, par exemple en gras, avec une taille de caractères plus importante, permet au lecteur humain d'identifier le titre ;
* les titres de section mettent en évidence la **structure** du document. Cette structure est indispensable. Elle permet par exemple d'indexer automatiquement les pages web, de créer automatiquement des sommaires, etc.
* Les balises `<p>`-`</p>` délimitent les paragraphes du texte. Les balises `<b>`-`</b>` demandent au navigateur web de produire un **rendu en gras **d'une partie du texte. Il est également possible d'utiliser les balises `<i>`-`</i>` pour demander un _rendu en italique_.Ces deux rendus permettent de mettre en évidence des parties du texte.



Deux autres balises vont nous être utiles. L'une pour insérer des liens hypertextes, l'autre pour insérer des images dans une page HTML.

Un **lien hypertexte** est une référence sur un document, une référence sur une page web ou un site web. En cliquant sur un lien hypertexte, on atteint la page ou le site référencé.




Un **site web** est généralement composé de plusieurs **pages web**. L'adresse d'un site web est l'adresse
de sa page d'accueil. La page web est identifiée par son adresse, on parle
d'**adresse web**, ou d'URL (Uniform Resource Locator). C'est l'adresse qui apparaît dans la barre d'adresses de votre navigateur. Par exemple, l'adresse du site web Wikipédia est   **http://wikipedia.fr/**



l'adresse de la page de Wikipédia de l'article à propos de URL est :    **http://fr.wikipedia.org/wiki/URL**



Dans une page HTML, ces liens vont pouvoir être associés à un texte qui sera rendu d'une manière particulière (par exemple souligné en bleu) pour marquer qu'il s'agit d'un lien hypertexte.

En HTML, on utilise la balise `<a>`-`</a>` avec l'attribut `href="_adresse_web_"` ajouté à
l'intérieur de la balise. Par exemple

~~~html
<a href="http://wikipedia.fr" >Wikipedia</a>
~~~


va produire le texte "Wikipedia" à partir duquel on pourra atteindre le site `http://wikipedia.fr`. À partir de

~~~html
<a href="http://fr.wikipedia.org/wiki/URL" >Qu'est-ce qu'une URL ?</a>
~~~


on atteindra la page web de Wikipédia consacrée au terme URL.




Consultez la page [que voici](http://qkzk.xyz/wp-content/uploads/2016/07/lien.html). Elle contient deux liens hypertextes. Consultez le code HTML de la page pour vérifier que les textes associés aux liens hypertextes présentés sont cohérents.





**Attention !**
Consultez la [page suivante](http://qkzk.xyz/wp-content/uploads/2016/07/lien-escroc.html). Que cache-t-elle ? Des images peuvent être insérées dans des documents HTML : Connaissez-vous [Wikimedia Commons](http://commons.wikimedia.org/wiki/Accueil?uselang=fr), la médiathèque libre des projets Wikimedia ? Son logo
est le suivant :





![logo de wikimedia](http://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/89px-Commons-logo.svg.png)



Wikimedia Commons est un dépôt de millions d'images que vous pouvez utiliser. Le logo de Wikimedia Commons est disponible à l'adresse


    [http://upload.wikimedia.org/wikipedia/commons/4/4a/Commons-logo.svg](http://upload.wikimedia.org/wikipedia/commons/4/4a/Commons-logo.svg)



On utilise la balise `<img>` pour insérer cette image dans un document HTML. L'adresse web de l'image est précisée à l'aide de l'attribut `src="_adresse_de_l_image_" ` ajouté à l'intérieur de la balise :

~~~html
<img src="http://upload.wikimedia.org/wikipedia/commons/4/4a/Commons-logo.svg" />
~~~


Nous remarquons que la balise `img` s'utilise seule, sans balise fermante correspondante. Dans ce cas particulier on remarque que la fin de balise se note `/>`




D'autres utilisations de cette balise `img` sont illustrées sur la [page dédiée](http://qkzk.xyz/?attachment_id=178), visualisez le code HTML pour vous en inspirer. Observez les changements de mise en page quand vous agrandissez ou diminuez la largeur de la fenêtre. Créez une page html affichant les images suivantes :








1. `<img src="http://maps.googleapis.com/maps/api/staticmap?center=50.609731,3.137511&zoom=17&size=400x400&sensor=false">` et `<img src="http://maps.googleapis.com/maps/api/staticmap?center=50.609731,3.137511&zoom=18&maptype=satellite&size=400x400&sensor=false">`
2. Recherchez les coordonnées GPS de votre lycée et modifiez le code html précédent pour afficher une page contenant la carte de votre lycée.







## Votre première page HTML







Créer une page reprenant la structure vue en exemple et y intégrer chacune des manipulations réalisées.


Rappel de la structure proposée :

~~~html
<h1>Section une</h1> <!-- titre de la 1re section -->
< p > Mon premier paragraphe. Ces <b>deux mots</b> sont en gras. < /p >

< p > Ce second paragraphe termine la section une.< /p >
<h1>Section deux</h1>
< p > Un autre paragraphe< /p >
~~~
