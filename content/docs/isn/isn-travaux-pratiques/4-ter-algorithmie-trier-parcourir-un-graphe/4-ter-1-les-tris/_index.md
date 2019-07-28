---
author: qu3nt1n
date: 2017-06-15 16:10:46+00:00
draft: false
title: '4.ter - 1 : Les tris'
weight: 1
---

## Trier une liste


Nous allons présenter deux méthodes classiques permettant de trier des listes. Il en existe beaucoup et celles-ci sont peut-être les plus simples. Le lecteur curieux trouvera aisément d'autres sources à ce sujet.

Comment trier efficacement une grande quantité de données ?

On suppose disposer d'une **liste de nombres désordonnés**. L'objectif est de **créer une fonction qui prenne cette liste et renvoie la liste ordonnée.**

Ex :

_liste1 = [1,3,2]_

_function tri(liste1):_
_# travail_
_return liste2 #la meme liste mais triée._

_print tri(liste1)_
_#[1,2,3]_
Avant de nous plonger dans les détails on peut envisager ce problème sous différents angles.
1. Déjà son intérêt est manifeste. Si on dispose d'une grande quantité d'informations, l'esprit humain n'est pas capable de les appréhender toutes en même temps.
Bon nombre d'indicateurs statistiques reposent sur l'ordre des données, les trier permet donc d'en dégager quelques informations assez simplement : valeurs extrêmes, quartiles etc.
Trier constitue donc une des premières étapes dans la réduction de l'information à des données essentielles.

2. Ensuite sa mise en pratique permet d'aborder l'optimisation des algorithmes. Chaque action que vous demandez à la machine a un coût et même plutôt deux :



* le temps d'exécution d'une opération lui même.
* l'espace en mémoire occupé par votre programme.

Selon les contextes l'un de ces coûts pourra totalement écraser l'autre.
Par exemple, si vous connaissez la suite de Fibonacci en mathématiques, il existe deux grands algorithmes pour en calculer les termes successifs.

Tous deux ont sensiblement le même coût en terme de temps d’exécution mais l'espace occupé par le premier est beaucoup beaucoup plus grand que celui occupé par le second. Ainsi, il est difficile de calculer des termes de rang élevé avec l'un tandis qu'il est aisé d'arriver beaucoup plus loin avec l'autre.

3. Enfin, ces problèmes de tris permettent de mettre en oeuvre la démarche naturelle de la programmation :
  1. analyse de l'énoncé et recherche de solution simple
  2. réalisation d'un algorithme papier
  3. développement pratique du programme dans un vrai langage
  4. tests et comparaison des méthodes.

Sans tarder davantage, intéressons nous aux algorithmes de tris.

Sachez d'abord qu'il en existe beaucoup ! C'est un problème fondamental et on a affiné leur développement. Certains algorithmes sont relativement bons en toute circonstance (que la liste soit totalement aléatoire ou presque ordonnée dès le départ), d'autres ont des champs d'application plus restreints, ils sont spécialisés (pour des listes aléatoires, des listes faiblement désordonnées etc.)

Nous n'en étudierons que deux mais de nombreuses sources en ligne les abordent tous.


### I. Le tri par sélection.


Son principe est très simple et il ressemble à une méthode qu'un humain pourrait appliquer naturellement :

**Principe** : _On détermine la position du plus petit élément, on le met en première position (en échangeant_
_avec le premier élément), et on itère le procédé sur le tableau restant._

Exemple sur l = [1,3,2]

1er tour :
On commencence avec x=1.
on parcourt le tableau en comparant 1 aux autres éléments.
1<3 et 1<2. Aucun échange 1 est le plus petit élément. Il est placé en premier.

On poursuit avec 3 (second élément).
On compare ensuite 3 et 2 : 3>2. 2 est plus petit que 3, on échange 2 et 3.

On termine avec le dernier élément qui est devenu 3.
Il n'y a personne avec qui le comparer, il reste en dernier.

La liste en sortie est donc l=[1,2,3].

**Consigne.**
Tester cet algorithme à la main sur la liste l = [4,1,3,2].
Compter le nombre C de comparaison et le nombre E d’échange que vous devez réaliser en tout.


### II. Le tri par fusion.


Il est fondé sur le principe suivant : il est plus facile de séparer un tas en deux parties que de réaliser des comparaisons et certaines comparaisons sont inutiles si on sait déjà qu'une partie est triée.

**Principe** : Il s’agit d’un exemple d’algorithme de type “diviser pour régner”. On procède par fusion
progressive de listes déjà triées.

La première fonction, appelée fusion, fusionne deux listes supposées triées en une seule.
Par exemple, fusion([1,2,4],[2,3,8]) renvoie [1,2,2,3,4,8].

La fonction de tri, récursive, consiste à couper en deux la liste initiale, à trier (par appels récursifs) les deux sous-listes, puis à les fusionner en faisant appel à la fonction fusion.

L’algorithme permettant la fusion de deux listes triées consiste à comparer les éléments de tête et à sélectionner le plus petit d’entre eux, à l’ajouter à la liste des éléments déjà sélectionnés, et à poursuivre sur les listes associées
aux autres éléments.

ouch.

regardons en détail ce que ça donne sur une liste de taille 4 :
l = [4,1,3,2]

On a donc 2 fonctions : _trifusion(liste)_ renvoie la liste triée.
_fusion(liste1, liste2)_ renvoie la fusion triée de ces listes QUI SONT ELLES MEMES SUPPOSEES TRIEES.

La clé est que _trifusion_ teste d'abord la longueur de la liste qu'elle a en paramètre. Tant qu'elle est supérieure à 1 (cette longueur), elle s'appelle elle même pour la fusion des deux sous listes.

C'est parti.

_trifusion([4,1,3,2])_

longueur = 4.
On découpe en 2 : [4,1] et [3,2]
On appelle _fusion( trifusion([4,1], trifusion([3,2]))_
2eme étape, a)
_trifusion([4,1])_ : taille = 2, on découpe [4] et [1]
On appelle _fusion( trifusion[4], trifusion[1])_
3eme étape a)
_trifusion([4])_ renvoie [4] car la liste est de taille 1.
3eme étape b)
_trifusion([1])_ renvoie [1] car la liste est de taille 1.
4eme étape c)
_fusion([4],[1])_.
On compare les deux listes jusqu'à épuisement :
4>1 donc on note [1,4]. Les listes étant épuisées on renvoie [1,4]
2eme étape a)
_trifusion([3,2])_ : taille 2 on découpe [3] et [2]
On appelle _fusion( trifusion[3], trifusion[2])_
3eme étape a)
_trifusion([3])_ renvoie [3] - la taille est 1
3eme étape b)
_trifusion([2])_ renvoie [2].
3eme étape c)
_fusion([3],[2])_
On compare jusqu'à épuisement :
3>2 on note [2,3]. Les listes étant épuisées on renvoie [2,3]
2eme étape c)
_fusion( [1,4], [2,3] )_
On compare : 1 et 2 on note [1].
On compare 4 et 2 : 2<4 ; donc 2 est le plus petit élément. On note [1,2].
On compare 4 et 3 : 3<4. Donc 3 est le plus petit élément. On note
[1,2,3].
La liste 2 est épuisée on note la fin de la liste 1 sans comparer :
[1,2,3,4]
_trifusion([4,1,3,2])_ renvoie enfin [1,2,3,4].

Cette démarche semble très fastidieuse ! Néanmoins regardons bien le nombre de comparaison effectuées, j'en compte 5 ! C'est bien inférieur à ce qu'on fait dans l'algorithme par sélection.
L'espace en mémoire peut sembler conséquent mais à chaque tour la taille des liste est divisée par 2. Il y a donc un espace total égal à la taille totale de la liste (environ) pour chaque tour.
On a conservé (approximativement) 3*4 = 12 données en mémoire durant tout le parcours.

On verra lors des tests que cet algorithme est bien meilleur que l'algorithme par selection.

Reprendre cet démarche en détail avec une liste de taille 3. Cela devrait aller vite.


### III . Programmation des deux algorithmes.




#### 1. SELECTION


On l'a vu, l'algorithme par sélection n'est constituée que de deux boucles imbriquées :
pour i un indice de la liste:
on note m = i
pour j un indice ultérieur à i:
on compare et on garde l'élément minimal, son indice est m.
On a trouvé le minimum on échange les éléments d'indice m et i.

Programmer cet algorithme (en Python ou en JavaScript selon votre parcours).

**Cahier des charges :**
1. Créer une fonction qui génère une liste désordonnée de taille n contenant des nombres entiers entre 1 et n.
Ex : [4,3,1,4] pour n=4. Les répétitions sont autorisées, on s'en moque.

2. Créer une fonction selection(liste) qui renvoie la liste triée par l'algorithme de sélection.

3. Tester abondamment. On affichera les listes avant et après pour s'assurer que tout fonctionne bien.

4. Calculer le temps moyen sur votre machine pour les tris par selection de 100 listes de taille 100. Tous les calculs doivent être faits par la machine. Elle n'affiche qu'un temps moyen final.


#### 2. FUSION


Rebelote avec l'algorithme par fusion.

La partie trifusion est la plus facile. On va la traiter en premier.
Hélas pour la réaliser il faut disposer au moins d'une sortie pour fusion(liste1, liste2).

On va donc commencer par créer un "faux" fusion(liste1, liste2) qui se contente de mettre bout à bout 2 listes sans rien faire. C'est faux, mais c'est facile.

**Consigne**
1. réaliser fausse_fusion(liste1, liste2) qui met bout à bout deux listes sans se soucier de l'ordre.

Ensuite programmons trifusion(liste).
Si la longueur de la liste est 1, l'algorithme renvoie la liste sans y toucher.
Sinon, il découpe en 2 parties et s'appelle lui même :
liste1 les premiers éléments, liste2 les seconds
Il renvoie fausse_fusion( trifusion(liste1), trifusion(liste2))

Remarque. attention aux listes de taille impaire. liste1 et liste2 n'auront pas la même taille. Débrouillez vous mais n'oubliez pas d'élément en route !

2. programmer cet algorithme "tricheur".
Il ne renvoie pas encore la liste triée mais vous devriez pouvoir débugguer facilement la partie récursive (quand il s'appelle lui même.)
A cette étape votre programme doit "tourner" et renvoyer la liste non triée sans rien faire d'autre que la découper et la recoller.

3. le vrai "fusion(liste1, liste2)"
C'est la partie délicate.
On va mettre dans liste3 les éléments successifs dont on est certain qu'ils sont les plus petits restants.

liste3 = []

on donne 2 compteurs i et j valant d'abord 0


Tant que i < longueur(liste1) et j < longueur(liste2):
si liste1[i] < liste2[i], on sait que liste1[i] est l'élément le plus petit donc
on ajoute liste1[i] à la fin de liste3
i augmente de 1.

Sinon on sait que liste2[j] est l'élément le plus petit donc
on ajoute liste2[j] à la fin de liste3
j augmente de 1.
Quand cette boucle est terminée on a parcouru entièrement une des deux listes.

Si c'est la première, on ajoute tous les éléments de liste2 (qui sont déjà triés et tous supérieurs à ceux de liste3) à la fin de liste3

Sinon c'est la seconde et on ajoute les éléments de liste1 (idem) à la fin de liste3.

On renvoie liste3.

Programmer cet algorithme fusion( liste1, liste2 ) et le tester sur des cas simples :
fusion([1],[2]) = [1,2] ; fusion([1,3],[2]) = [1,2,3] etc.

Corriger votre précédente fonction trifusion en lui faisant appeler fusion(liste1, liste2) au lieu de fausse_fusion(liste1, liste2)
Tester abondamment...

On reprendra les calculs de moyenne dans les mêmes conditions (100 listes de taille 100) pour comparer les 2 algorithmes. Le tri par fusion est bien meilleur.

Voilà pour cette première approche de l'algorithmie.


### IV. Quelques références :


**Les tris en action en vidéo.**

Rq : En anglais le tri par fusion s'appelle "merge sort" et le tri par selection "selection sort".

déjà, parce qu'[il faut bien rire un peu](https://www.youtube.com/watch?v=kPRA0W1kECg). Attention à la crise d'épilepsie. **- Écouteurs obligatoires -**

Ensuite pour se convaincre que [les différences de vitesses sont majeures](https://www.youtube.com/watch?v=ZZuD6iUe3Pc). Notons que l'efficacité des algorithmes dépend beaucoup du "désordre" initial dans la liste de départ.

Regardez bien cette vidéo et retenez que le tri par sélection n'est pas le plus mauvais mais est très lent par rapport au tri par sélection. Remarquez aussi qu'il y a toujours mieux !

**Les cours d'openclassrooms :**
[tri selection](https://openclassrooms.com/courses/le-tri-par-selection).
[tri fusion](https://openclassrooms.com/courses/le-tri-fusion).

Les deux sont intéressants, surtout si vous vous sentez perdu.

**La complexité de ces algorithmes.**

Revenons sur nos coûts.
La complexité d'un algorithme est le nombre d'opération à effectuer par la machine. On ne s'intéresse donc ici qu'aux calculs, pas aux accès mémoire.
Un problème à la fois donc.

Pour le tri par sélection :
2 boucles imbriquées, une de taille n contenant une de taille n-i
Ce qui donne
n-1 +(n-1)+(n-2)+...+1 comparaisons et échanges éventuels.
Vous reconnaissez la somme des entiers qui vaut (n-1)n/2
La complexité est donc un polynôme de degré 2 en la variable n
On dit que c'est un problème en O(n^2) (pas plus grand qu'un polynôme de degré 2).

Pour le tri par fusion :
Je vous renvoie au cours d'openclassrooms pour les détails (qui sont accessibles avec un niveau fin de terminale mais n'ont pas grand intérêt pour vous).
Retenez simplement que la complexité est O(n log n)

Grossièrement, on passe de n^2 (en gros, très gros) à n log n

Le ratio entre les deux est de l'ordre de log n / n

log n tend bien vers + infini en + infini... mais beaucoup beaucoup BEAUCOUP moins vite que n.

Par exemple ln(1000) = 7 à l'entier près. et 7/1000 n'est pas très grand.

Voilà pourquoi l'algorithme par fusion est beaucoup beaucoup plus rapide.

Quelques mots sur la complexité en général.



* On ne s'est penché que sur l'efficacité (nombre d'opération) et on a omis l'espace en mémoire. Souvent l'un des deux est négligeable devant l'autre... mais pas toujours !
* On range souvent les problèmes dans des catégories bien distinctes :
ceux pour lesquels on dispose d'un algorithme au pire polynômial et les autres.
Exemple : les tris ! Le tri par sélection est polynomial d'ordre 2 dans tous les cas. Le tri par fusion est même bien meilleur.

Est-ce le cas de tous les algorithmes ?
Et bien la réponse est qu'on n'en sait rien.
Si vous le démontrez vous pouvez gagner 1 million de dollars (Really).

Cette question est souvent référencée ainsi : a-t-on P = NP ?

P : la classe des problèmes disposant d'un algorithme polynomial.
NP : les autres.

Par exemple, pour la factorisation en produits de nombres premiers depuis un entier (15 = 5*3) (mais avec des tailles IMMENSES, exemple : 982.451.653), on ne connait pas d'algorithme polynomial.
Peut-être en existe-t-il ? On ne sait pas.

Peut-être même que P=NP et alors ce serait une révolution terrible en informatique. Si vous démontrez que P=NP (banco, un million) ET que vous proposez un algorithme polynomial pour ces problèmes (là vous devenez immédiatement aussi célèbre que Newton ou Einstein) alors toutes les transactions financières (TOUTES) deviendraient immédiatement NON SÉCURISEES car une machine standard pourrait les décrypter assez rapidement pour pirater et intercepter l'argent.

Et avec un peu de recul, un million de dollars pour démontrer que les transactions financières de toute la planète sont sécurisées n'est pas un montant si extraordinaire.

Peut-être que P!=NP et alors certains problèmes concrets deviennent irréalistes même en améliorant considérablement les machines...
Les mathématiciens et informaticiens théoriques pensent majoritairement que P!=NP.

Cette présentation très simplifiée (et fausse par endroit) ne saurait être une introduction à ce problème. Elle vise juste à vous présenter un concept théorique lourd de conséquences et vous justifier la nécessité de familiariser la jeunesse à ses enjeux.

[Solution des problèmes présentés plus haut.](https://drive.google.com/open?id=0B4Mq2ZGzUQ3VdE9QQkUzNFJZS00)

2 solutions sont proposées, équivalentes mais programmées en Python (qkzk_tris.py) ou Javascript (qkzk_tris.html et qkzk_tris.js). On trouvera aussi un pdf d'approfondissement accompagné d'un script python présentant d'autres algorithmes de tris.
