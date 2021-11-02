---
author: qu3nt1n
date: 2016-07-01 23:51:59+00:00
draft: false
title: 3.3 Codage des couleurs
bookCollapseSection: true
weight: 3
---



Notions abordées



* codage des couleurs : RVB
* des couleurs dans du HTML








# Codage des couleurs







### Nommer les couleurs






Nous pouvons désigner une couleur par son nom. En HTML, seize couleurs de base sont ainsi définies. Par exemple « black », « white >», « red », ou « green ». HTML et CSS définissent une autre liste de 130 couleurs supplémentaires. On peut les utiliser ainsi :




~~~html
<html>
<body style="background-color:black;">

<p style="color:red;">
Un paragrphe en rouge</p>

<p style="color:green;">
Un paragraphe en vert</p>

</body>
</html>
~~~








On pourra utiliser l’éditeur/visionneuse HTML en ligne de [http://www.w3schools.com/html/](http://www.w3schools.com/html/)
(point d’entrée direct [http://www.w3schools.com/html/tryit.asp?filename=tryhtml_paragraphs1](http://www.w3schools.com/html/tryit.asp?filename=tryhtml_paragraphs1))
pour avoir un rendu des fichiers HTML.










## Codage RVB des couleurs






Une couleur peut aussi être désignée par un triplet RVB (rouge, vert, bleu ; on utilise RGB en anglais). On précise une intensité, de 0 % à 100 % pour chacune des composantes. La couleur résultante est obtenue par synthèse additive des trois composantes.





Pour une intensité nulle des trois composantes, on obtient du noir. Pour une intensité maximale des trois composantes, on obtient du blanc.





L’intensité de chacune des composantes peut être exprimée sur une échelle qui va de 0 à 255. Huit bits, soit un octet, sont nécessaires pour représenter une telle valeur : 256 = 28. On utilise donc commodément une notation héxadécimale de deux chiffres entre ’00’ et ’FF’.





Une couleur est désignée par la concaténation de trois valeurs hexadécimales de deux chiffres, une pour chacune des trois composantes, dans l’ordre rouge, vert, bleu. Cette notation est
précédé en HTML par le signe ’#’. On pourra donc écrire ’#000000’ pour noir, ’#FFFFFF’ pour blanc, ou ’#FF0000’ pour rouge.





Remplacez les noms des couleurs dans le fichier HTML précédent par leur triplet hexadécimal correspondant. Vérifiez le rendu de la page HTML.









Combien de couleurs a priori distinctes peuvent être désignées par cette notation RVB ?





Éléments de solution. 2563=16 777 216, soit environ 16 millions de couleurs. On peut aussi parvenir au résultat en considérant que le codage d’une couleur est sur 24 bits :
224=16 777 216.









## Conversion en RVB






À partir de la valeur de l’intensité d’une composante, il s’agit par une règle de trois de produire une valeur entre 0 et 255.





Cette valeur doit ensuite être exprimée en hexadécimal. Le premier chiffre hexadécimal est obtenu par division entière par 16 de cette valeur. Le second chiffre est le reste de cette division entière.





Soit une intensité de 75 %. Cela correspond à une valeur de 256 × 75 / 100 = 192 sur notre échelle 0-255. Comme 192 = 12×16 + 0, on écrira ’C0’ en hexadécimal.





Il est nécessaire de répéter cette opération pour chacune des composantes.





La couleur ’#C0C0C0’ correspond à un gris.






On désire produire une couleur « gris vert ». Il s’agit d’un gris dans lequel la composante verte sera un peu plus importante que dans un gris. Essayez avec des composantes à 75 % et une composante verte à 80 %.
