---
author: qu3nt1n
date: 2016-07-02 08:01:25+00:00
draft: false
title: 3b.1 Séparation contenu / forme
weight: 1
---



Notions abordées dans cette page



  * feuilles de style et traitement de textes
  * séparation de la forme et du contenu










#  Un peu de style






Ouvrez [ce fichier](http://qkzk.xyz/docs/doc03b/exemples/gestionStyles.odt) avec le
logiciel LibreOffice. Vous découvrez un fichier dont le contenu est
structuré avec des titres et des paragraphes.








Les logiciels de traitement de textes tel que LibreOffice permettent
la mise en place de styles. Un style définit les différentes
propriétés qui régissent l'apparence d'un élément du document telles
que la police, la couleur, les marges, etc.







![liste de gestion des
						    styles](http://qkzk.xyz/docs/doc03b/zoneStylList.png)







Dans LibreOffice le nom du style appliqué à un élément est visible
  dans la zone de gestion des styles qui se trouve généralement à
  gauche au-dessus du texte, comme présenté sur l'image ci-contre. Un
  style peut être **appliqué** à un élément de texte dont
  l'apparence adopte alors toutes les propriétés définies par le
  style. Un même style peut être appliqué à plusieurs éléments d'un
  même document.








  Placez votre curseur à différents endroits du texte de la page et repérez
  les différents noms des styles utilisés ainsi que les différents
  pour lequel le style est le même.






L'utilisation des styles permet de gérer efficacement l'apparence
  d'un document en agissant sur les propriétés du style plutôt que sur
  les propriétés du contenu. Un premier intérêt est part que la gestion
  de la cohérence de l'apparence du document est facilitée car toute
  modfication est
  "automatiquement" appliquée à tous les éléments concernés.









  1. Placez le curseur sur le texte _Voici un premier titre_, dont
  le style à pour nom _Titre 1_.

  2. Faites un clic droit puis choisissez dans le menu _Editer le
    style de paragraphe..._.

  3. Faites différentes manipulations à l'aide de la fenêtre qui
  apparaît. Par exemple, à partir de l'onglet _Police_ modifiez
  la famille, le style et la taille de la police et cliquez sur le
  bouton _Appliquer_ en bas de la fenêtre.

  4. Que constatez-vous pour le texte _Voici un premier
    titre_ ? Et pour les autres éléments de texte auxquels
    s'applique le style _Titre 1_ ?

  5. Vous pouvez faire d'autres manipulations sur le style par exemple
  changer la couleur (_Effets de caractères_), l'alignement ou
  les retraits. Validez le tout à l'aide du bouton _OK_.







Un second intérêt est qu'il est facile de modifier fortement
  l'apparence d'un document sans "toucher à"
  celui-ci. Une feuille de style peut
  être définie indépendamment d'un document et appliqué à un tout
  document. Cela permet par exemple de définir une charte graphique
  commune à un ensemble de documents.










  1. Récupérez les fichiers de définition des feuilles de style (LibreOffice utilise le
  terme _modèle_) `[modele1.ott](http://qkzk.xyz/docs/doc03b/exemples/modele1.ott)`
  et `[modele2.ott](http://qkzk.xyz/docs/doc03b/exemples/modele2.ott)` et
  sauvegardez-lessur votre disque.




  2. ![zone boutons de
  gestion des styles](http://qkzk.xyz/docs/doc03b/boutonsStyles.png)

A partir du document précédent, cliquez sur le bouton à gauche de
  la liste des styles (cf. imgae ci-dessus) ou appuyez sur la
  touche. Cela fait apparaître une fenêtre nommée _Styles et
  formatage_.

Cliquez sur le bouton  le plus à droite et choisissez _Chargez les styles..._.



  3. ![fenêtre Chargez les styles](http://qkzk.xyz/docs/doc03b/chargerLesStyles.png)


Dans la fenêtre qui s'ouvre cochez la case _Ecraser_ puis cliquez
  sur le bouton _A partir d'un fichier..._. Dans la fenêtre de
  choix de fichier qui apparaître sélectionnez _Modèle de texte
  ODF_ dans la liste déroulante en bas à droite puis recherchez le
  dossier dans lequel vous avez enregistrer le
  fichier `modele1.ott` et sélectionnez-le avant de valider.


  4. Que constatez-vous dans le document ?

  5. Recommencez la manipulation précedente en choisissant cette fois
  la feuille de style définie par le fichier `modele2.ott`.













  1. Créez un nouveau document texte avec LibreOffice et créez du
  contenu en attribuant les
  styles _Titre_, _Titre 1_, _Titre 2_
  et _Corps de Texte à différentes parties du document.
  2. Appliquez à ce document le style défini par `modele1.ott`_








Pour créez vos propres feuilles de style (ou modèles) sous
LibreOffice, définissez les propriétés des styles des différents
éléments d'un document comme cela a été fait à la Manip' 3 puis
dans le menu _Fichier_ faites le choix _Modèles_
puis _Enregistrer..._. Il vous suffit alors de donner un nom à
votre feuille de style. Le fichier correspondant est stocké sur le
disque dans un répertoire géré par LibreOffice mais vous trouverez
dans la fenêtre de chargement de styles vue à la Manip' 4.






Un style permet donc de gérer l'apparence, la
forme d'un document indépendamment du
 contenu de la page autrement dit son
fond. Ces deux aspects d'un document
peuvent donc être gérés de manières totalement dissociées.  On dit que
l'on réalise ainsi la séparation du fond et
de la forme. Ce principe important dans toutes les tâches de
publication s'applique également aux pages web.
