---
author: qu3nt1n
date: 2016-07-02 13:48:12+00:00
draft: false
title: Wolfram Alpha like


---




# WolframAlpha-Like







### Projet de base





WolframAlpha est un service internet capable, entre autres, d'effectuer du calcul formel, de donner diverses représentations d'un problème posé ainsi que
les étapes de calculs détaillées amenant à la réponse (version pro). Voici, par exemple, comment WolframAlpha traite une équation du 
second degré :




[![doc00019_1](/uploads/uploads/2016/07/doc00019_1.jpeg)
](/uploads/uploads/2016/07/doc00019_1.jpeg)




Le projet consiste à réaliser en javascript le même type de service pour la résolution des équations du premier et du second degré.
Comme sur le site WolframAlpha, l'utilisateur entrera une équation, le programme devra identifier s'il s'agit d'une équation du premier ou du second degré et
ensuite il résoudra le problème. Pour le second degré on traitera également le cas des solutions complexes.



On se limitera à des coefficients entiers.



L'affichage des formules mathématiques pourra être réalisé en utilisant la bibliothèque MathJax ou simplement mathml.



Il faudra également implémenter la rédaction automatique détaillée des étapes de calculs pour la résolution des équations (qui ne figure pas sur la copie
d'écran ci-dessus).



L'ensemble sera intégré dans une page web fournissant les explications nécessaires à l'utilisation du logiciel.





### Extensions





On pourra ajouter des fonctionnalités, voici quelques suggestions (liste non limitative) :






* recherche des solutions réelles approchées pour un polynôme de degré supérieur ou égal à 3,
* dérivation des fonctions polynômes de n'importe quel degré,
* tableau de variation avec valeurs exactes pour une fonction polynôme de degré inférieur ou égal à 3,
* tableau de variation avec valeurs approchées pour une fonction polynôme de degré supérieur ou égal à 4.


