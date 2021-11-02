---
author: qu3nt1n
date: 2016-07-01 14:00:11+00:00
draft: false
title: 02. Cryptographie
bookCollapseSection: true
weight: 2

---



Notions abordées



lexicométrie
cryptographie simple : le code césar







### Utiliser la lexicométrie pour casser un code secret.




# Introduction


Le principe de la cryptographie est aussi vieux que l'histoire : transmettre un message succeptible d'être intercepté à une personne particulière en s'assurant qu'elle seule peut le lire.
Elle fait maintenant partie prenante de nos vie et, chaque fois que nous nous identifions sur un site sécurisé, elle entre en jeu pour s'assurer que nos données ne puissent être comprises par des pirates qui les intercepteraient.

![](https://s-media-cache-ak0.pinimg.com/736x/a5/e7/b3/a5e7b392129104c982149a73f7d33480.jpg)

La cryptographie est l'étude de ces procédés. Le procédé le plus connu est le code César utilisé par Jules César en personne. Il consiste à numéroter les lettres de l'alphabet (A=1,B=2,...) et à décaler chaque lettre d'un message. Par exemple si je décale de 5 le message ROBERT j'obtiens : WTGJWY. Si nécessaire on revient à A après Z.
Ce procédé, vieux comme le monde, ne résiste pas longtemps. Il n'y a, après tout que 26 possibilités. Et si le message contient une information cruciale alors il est surement pertinent d'y consacrer le temps nécessaire.
D'autres procédés furent inventés au fil du temps pour rendre le cryptage plus robuste. En voici un, il a résisté jusqu'à l'invention de la lexicométrie.

_Remarquons que la cryptographie est beaucoup plus ancienne ! Le plus ancien document chiffré est une recette secrète de poterie qui date du xvie siècle av. J.-C., qui a été découverte dans l'actuelle Irak. _


# Codage simple par inversion


On écrit un tableau de 2 lignes et 26 colonnes. Première ligne : les 26 lettres. 2ème ligne, une lettre parmi l'alphabet. La seule contrainte est de ne l'employer qu'une fois...
<table width="90%" border="" >
<tbody >
<tr bgcolor="#33CCFF" align="center" >

<td >Texte clair
</td>

<td >A
</td>

<td >B
</td>

<td >C
</td>

<td >D
</td>

<td >E
</td>

<td >F
</td>

<td >G
</td>

<td >H
</td>

<td >I
</td>

<td >J
</td>

<td >K
</td>

<td >L
</td>

<td >M
</td>

<td >N
</td>

<td >O
</td>

<td >P
</td>

<td >Q
</td>

<td >R
</td>

<td >S
</td>

<td >T
</td>

<td >U
</td>

<td >V
</td>

<td >W
</td>

<td >X
</td>

<td >Y
</td>

<td >Z
</td>
</tr>
<tr bgcolor="#FFFF99" align="center" >

<td >Texte codé
</td>

<td >W
</td>

<td >X
</td>

<td >E
</td>

<td >H
</td>

<td >Y
</td>

<td >Z
</td>

<td >T
</td>

<td >K
</td>

<td >C
</td>

<td >P
</td>

<td >J
</td>

<td >I
</td>

<td >U
</td>

<td >A
</td>

<td >D
</td>

<td >G
</td>

<td >L
</td>

<td >Q
</td>

<td >M
</td>

<td >N
</td>

<td >R
</td>

<td >S
</td>

<td >F
</td>

<td >V
</td>

<td >B
</td>

<td >O
</td>
</tr>
</tbody>
</table>


Ensuite coder le message est un jeu d'enfant, il suffit de remplacer chaque lettre du message par celle du code. On aura souvent tendance à enlever la ponctuation, coller tous les mots et découper de manière régulière.

Imaginons qu'on souhaite chiffrer ce texte :

UN PETIT ROSEAU M'A SUFFI POUR FAIRE FREMIR L'HERBE HAUTE ET TOUT LE PRE ET LES DOUX SAULES ET LE RUISSEAU QUI CHANTE AUSSI.

On obtient alors :
RA GYNCN QDMYWR U'W MRZZCN GDRQ ZWCQY ZQYUCQ I'KYQXY KWRNY YN NDRN IY GQY YN IYM HDRV MWRIYM LRC EKWANYAN WRMMC

Si notre destinataire connait la table il n'aura aucun mal à le déchiffrer. J'ose espérer que vous aviez deviné.

Le nombre de combinaison dépasse l'entendement : 26 pour la première lettre x 25 pour la 2eme x 24 pour la troisième etc. = 26 * 25 * 24 *...* 3 *2 *1. On note ce nombre 26! (26 factorielle) et il vaut environ 4*10^26. (4 suivi de 26 zéros). _Remarquons qu'on estime (grossièrement) qu'il y a entre 10^22 et 10^24 étoiles dans l'univers soit entre 100 et 10000 fois moins que de combinaisons possibles à notre codage._

Voilà une complexité qui semble inaccessible. Aucune machine ne pourrait les tester toutes ! C'est que cette approche n'est pas la bonne petit Kéké.

Ce code ne résiste pas longtemps à la lexicométrie... A condition que le message soit assez long. Nous allons voir plus bas que deux lignes suffisent pour le casser.


# Un petit peu de Python




## Chiffrer le message à l'aide du code César


Bien qu'il soit aisé de coder le message à la main nous allons créer un script qui code et décode en connaissant la clé.


Créer un nouveau script python. On n'oubliera pas de lui préciser d'encoder en utf8.
Créer une variable `message` contenant un message secret en clair (entourer votre chaîne de ' ' pour qu'elle soit comprise en tant que telle par Python).
Choisir une clé (entre 1 et 26)
Préparer votre message en enlevant la casse (tout en minuscule), la ponctuation, les espaces et les accents (à la main ça ira très bien, via une commande Python si vous en êtes capable). Nous traiterons ces cas plus tard. Le stocker dans une nouvelle variable `message_prepare`.
Afficher ce message.


**Deuxième étape : la table ascii.**
Ainsi qu'on l'a vu plus tôt, le codage ascii des caractère est le premier a avoir été développé. Il est facile à obtenir et ne comporte que 2^7-1 = 127 caractères. Il fut inventé AVANT les ordinateurs et sa promotion est due à Bell, entreprise pionnière des télécommunications.


Obtenir une table ascii sur internet et la garder au chaud dans un autre onglet de votre navigateur.


On remarquera que la table fait apparaître des caractères de contrôle (fin de ligne, fin de message, tabulation verticale etc.) Ce principe est encore employé à l'heure actuelle.

Les lettres minuscules sont encodées de 97 à 122 (en décimal, 61 jusque 7A en hexadécimal). Les lettres majuscules de 65 à 90 (41 jusque 5A en hexadécimal).


Hexadécimal ? C'est autre façon de représenter les entiers naturels : avec 16 chiffres, le plus souvent notés 0 1 2 3 4 5 6 7 8 9 A B C D E F. On utilise moins de place et, 16 étant une puissance de 2, c'est beaucoup plus commode pour les machines qui ne travaillent en fait qu'en binaire (0 et 1). Transposer un nombre de l'hexadécimal au binaire ne demande qu'une opération, la division Euclidienne par 2, répétée 4 fois.




**Remarque : **Vous_ rencontrerez souvent des caractères hexadécimaux en informatique. Par exemple on encode souvent les couleurs RGB (red-green-blue) ainsi : #FF00AA. [Le rouge à fond, pas de vert, la moitié de bleu.](https://www.w3schools.com/colors/colors_picker.asp?color=ff00aa)_




Nous allons maintenant reprendre votre script. On va, tout d'abord, créer une boucle qui transforme chaque lettre de votre message en clair par son équivalent en majuscule. 'a' -> 'A', 'b'-> 'B' etc.


Combien soustraire au code ascii du 'a' pour obtenir un 'A' ? Est-ce différent pour 'b'-> 'B' ?






Python dispose d'une fonction toute faite appelée `ord()`. Tester cette fonction sur des chaînes de caractères d'une seule lettre `print ord('a')` Que fait-elle ?

Utiliser cette fonction pour remplacer votre message en clair par une liste contenant les codes ascii de chaque caractère correspondant. L'afficher.






Créer une nouvelle fonction qui affiche la liste des codes ascii du message en clair, mais cette fois en majuscule.




Que fait la fonction `chr()` de Python ? La tester avec des nombres, par exemple `print chr(65)`.


Vous disposez maintenant de tous les éléments pour transposer votre message des minuscules vers les majuscules. Il faut faire une boucle se baladant dans la chaîne de caractères et pour chaque lettre combiner ord et chr.




Ecrire un script qui, à partir d'un message en clair et en minuscule, renvoie le message en clair mais en majuscule à l'aide des éléments listés plus haut.


Remarquons qu'une fonction préexistante de Python réalise tout ça. Néanmoins nous aurons besoin de ces étapes dans la suite aussi vous ne pouvez l'utiliser.








**Le code César.**

On suppose maintenant que vous disposez d'un message en clair en minuscule, sans ponctuation, sans accent, ni apostrophe et sans espace.

On pourrait croire qu'il suffit maintenant d'ajouter à chaque numéro de caractère la valeur de la clé. a valant 97, si ma clé est 3 je le code par 97 + 3 et j'affiche la réponse :



    message_majuscule = 'a'
    cle = 3
    print chr(ord(message)+cle)





Pourquoi ce script est-il faux ? Il affiche pourtant E, ce qui est bien la réponse attendue !?


Oui, c'était facile... si la clé est 3 alors x, y et z sont codés par les premières lettres de l'alphabet... Notre code renverra des caractères qui ne sont pas des lettres pour X, Y et Z. Vous pouvez tester.

Reprenons ! Si la clé est 3, qu'on numérote a = 0 (ce sera plus facile), b=1, c=2, ..., z=25 (on numérote à partir de 0 kéké) et qu'on ajoute 3 à tout le monde... alors il faut revenir à 0 à partir de 26.
27 donnera 1 (donc b), 28 donnera 2 (donc c).
**C'est le principe du reste dans la division par 26.**
Aussi on pourrait être tenté d'ajouter 3 à tous les codes ascii et prendre le reste par 26. Mais ça ne marchera pas... NON.
Flûte.

On va plutôt commencer par soustraire 97 à tous les codes. a -> 97 - 97 = 0,... z -> 122 - 97 = 25. Jusqu'ici tout va bien.
Ensuite on ajoute 3 à tout le monde et on prend le reste de la division par 26. Ce qu'on appelle le MODULO 26. C'est une fonction de base de tous les langages de programmation.
On obtient a -> 3, b->4,...,w->25,x->0,y->1,z->2. Et le tour est (presque) joué.

Résumé : On prend le code ascii de la lettre en clair, on soustrait 97, on ajoute la clé, on prend le reste modulo 26... et ?! et Kéké et ?! On ajoute à nouveau 97 pour retrouver le code ascii de la lettre codée. Faut suivre un petit peu kéké j'en ai marre.

En Python le modulo est codé par % : `28 % 26` renvoie 2.

Voici ce que ça donne pour la lettre 'z' et la clé 3 : `print chr( (ord('z')-97+3)%26 + 65 )`. Python renvoie c.


Adapter votre petit extrait de code pour qu'il renvoie une lettre codée par la clé 3 (on va commencer par une seule lettre).
Améliorer votre script pour qu'il code avec la variable `cle` dont vous pouvez changer la valeur. Ajouter une boucle à votre script, parcourant le message en clair, en majuscule et qui code le mot complet. Affichez le.


Et ça marche enfin... Arrivé ici il vous reste écrire le tout en une seule étape : le message en clair en minuscule, son codage, l'affichage du message codé en majuscule.


Reprendre le principe précédent pour le décodage. Etape par étape si nécessaire. C'est plus compliqué d'employer les modulos ici et je n'exige rien. Une correction vous sera transmise si vous buttez trop longtemps.




# L'analyse fréquentielle d'un message


Souvenons nous que le code César n'a que 26 combinaisons possibles... _"A quoi bon s’enquiquiner la vie avec l'analyse fréquentielle, je n'ai qu'à tester les 26 combinaisons sur quelques lettres et j'aurais rapidement décodé un message..."_ Ah kéké, tu me fatigues.

L'analyse fréquentielle nous permettra, si le message est assez long, de trouver immédiatement comme le E est codé. Et surtout elle s'appliquera à un code beaucoup plus difficile : l'échange simple que nous avons vu en introduction...

Reprendre le programme de la partie précédente.

Voici un message codé par le code césar :


<blockquote>txdwuh ylqjw gla plooh hpsorlv ydfdqwv gdqv oh vhfwhxu gx qxphultxh g lfl ghxa plooh ylqjw dxmrxug kxl ghmd ohv hqwuhsulvhv irqw sduw gh ehvrlqv hq uhfuxwhphqw qrq vdwlvidlwv fhv gliilfxowhv d o hpedxfkh vh yhulilh fkhc ohv lqjhqlhxuv lqirupdwltxhv hw gdqv xqh prlqguh phvxuh fkhc ohv whfkqlflhqv</blockquote>




Vous allez chercher à le décrypter à l'aide du programme d'analyse des fréquences de la partie précédente.
En l'appliquant au message crypté, il devrait vous donner la lettre la plus fréquente du code. Vous connaîtrez alors la lettre qui code le e, la lettre la plus fréquente de la langue française. Quelle est la lettre la plus fréquente du message ? Et son pourcentage d'apparition ? Quelle est la clé que j'ai utilisé pour encoder ce message ? Que dit-il ?


Cette étape était simple, vous n'aviez qu'à trouver la clé et le tour était joué !

C'est plus délicat concernant le codage simple... mais ça reste faisable. Le principe ayant été exposé au début de cette partie, entrons directement dans le vif du sujet.

Notre objectif est maintenant de coder un message par l’échange simple à l'aide d'une clé, de le décoder et, surtout de casser le code.

Rien que ça.

Concernant cette partie, je vais vous expliquer la démarche en détail et nous allons traiter ensemble chacune des étapes.


## Cahier des charges :


**Codage**



 Comprendre le principe de l'échange simple. Cette fois la clé est l'ordre dans lequel chacune des lettres de l'alphabet apparaît. Pour notre exemple, on travaillera avec `cle = 'zyxwvutsrqponmlkjihgfedcba'` : l'ordre inverse.
Cela n'a aucune importance, n'importe quel ordre fera l'affaire.
 Pour coder le message on va parcourir la chaîne de caractère et relever le code ascii du message en clair.
Les lettres étant des minuscules, c'est un nombre entre 97 (a) et 122 (z). On soustrait à nouveau 97 à ce nombre et on aura le numéro de la lettre en clair dans le message. Disons qu'on l'appelle n, comme numéro.
 A ce nombre on fait correspondre l'élément de position n de la liste notée clé.
 On obtient alors le message codé en regroupant lettre par lettre sans oublier les espaces.

**Décodage**
Inutile de réinventer la roue, direz-vous ! On a la clé, on l'inverse et on refait pareil. C'est ce qu'un humain ferait, je vous le concède. Pour une machine, c'est plus délicat. Notre clé n'a pas le bon format pour se prêter à ce genre d'exercice. On va plutôt employer une nouvelle fonction de Python qui renvoie l'indice d'un élément dans une chaîne de caractère.


    #!/usr/bin/python

    str1 = "c'est mon exemple";
    str2 = "mon";

    print str1.index(str2)



Et Python renvoie 6. La chaîne de caractères "mon" apparaît dans str1 à partir de la position d'indice 6, c'est à dire en 7eme place. Souvenez-vous qu'on compte à partir de 0.
Si Python ne trouve pas la lettre, il va simplement s’abstenir de répondre.

Pour nous, si le message crypté est note `code`, et sa première lettre 'w' on cherche la position de w dans la liste. On va alors trouver le w à l'indice 3 de notre clé. Ajoutons 97 à ce nombre : 97+3 = 100 (pas mal kéké) et on aura le code ascii de la lettre de départ : le d.

On recompose le mot et le tour est joué.


A vous de le faire, étape par étape en affichant les informations nécessaires au fur et à mesure.




La solution est dans le code source de la page héhé.
* [xvie]: 16ᵉ siècle
* [av. J.-C.]: avant Jésus-Christ
