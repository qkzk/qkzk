---
author: qu3nt1n
date: 2016-07-01 23:33:50+00:00
draft: false
title: 3.2 Codage des caractères
weight: 2
---



Notions abordées



*  codag de caractères : le code ASCII, codage UTF-8
*  codage et HTML, URL









# Codage des caractères







## Codage ASCII




Un fichier contient une représentation de données. Par exemple un
fichier peut contenir une représentation d'un texte. Bien souvent on
dit plus simplement que le fichier contient le texte.






Un **caractère** peut être une lettre, un chiffre,
une ponctuation, tout autre symbole accessible via les touches de
votre clavier, etc.




Le contenu du fichier n'est lui-même qu'une suite de 0 et de 1, des
bits. On choisit donc de coder chacune des lettres, plus généralement
chacun des caractères, par une représentation binaire.

Ce choix d'utiliser un codage donné est arbitraire.

Historiquement, le codage ASCII
a été défini et utilisé pour écrire des textes en anglais.

La table ASCII fournit la correspondance entre 128 caractères et
leur représentation binaire. Les caractères sont numérotés de
0 à 127. A priori, 7 bits suffisent à coder ces caractères, en effet
128 = 27. En pratique, les ordinateurs travaillent presque
tous sur des multiples de 8 bits, ce que l'on nomme octet. Chacun des 128 caractères ASCII est
donc codé par un octet dont le 8ème bit est à 0.






Observez la [table ASCII](http://qkzk.xyz/docs/doc03/ascii.txt).
On remarque que certains caractères de la table ASCII sont des
caractères dits de contrôle, ils ne sont pas imprimables ou ne
peuvent pas être affichés.)

On pourra aussi consulter [http://fr.wikipedia.org/wiki/ASCII](http://fr.wikipedia.org/wiki/ASCII).




La représentation binaire du caractère 'a' est '0110_0001'. Cette
valeur binaire correspond à 97 en décimal. On dit que le code ASCII de
'a' est 97. De même, 'z' est représenté par '0111_1010', qui
correspond à 122 en décimal. Le code ASCII de 'z' est 122.

On remarque aussi que les chiffres sont présents dans la table
ASCII, ce sont des caractères "comme les autres", la représentation
binaire du caractère '1' est par exemple '0011_0001', le code ASCII de
'1' est donc 49.






Donnez la représentation binaire ASCII du texte suivant :


    Je code en binaire !



On utilise la table ASCII. C'est laborieux... Vous pouvez
vérifier que vous trouvez bien le
[résultat suivant](http://qkzk.xyz/docs/doc03/je-code-en-binaire.txt).









Quel est le nombre de caractères du texte dont la repésentation
binaire ASCII est la suivante :




    0100110001100101 0010000001100010 0110100101101110 0110000101101001
    0111001001100101 0010110000100000 0110001100100111 0110010101110011
    0111010000100000 0110100101101110 0110100001110101 0110110101100001
    0110100101101110 00101110



Quel est ce texte ?




Il est mal commode, pour un humain, de manipuler des représentations
binaires. Pour faciliter les choses on regroupe les séquences de
4 bits en une valeur hexadécimale. En effet, les valeurs binaires de
'0000' à '1111' correspondent aux 16 valeurs hexadécimales '0', '1',
... '9', 'A', 'B', 'C', 'D', 'E', et 'F'. Par la suite, ces chiffres
et lettres seront appelés chiffres hexadécimaux.






Complétez la table suivante


    0 - 0000        4 - 0100        8 - 1000        C -
    1 - 0001        5 -             9 -             D -
    2 -             6 -             A -             E -
    3 -             7 -             B -             F - 1111






Les caractères ASCII sont représentés sur 8 bits. Tout caractère
ASCII peut donc être représenté par deux chiffres hexadécimaux. Notre
caractère 'a' sera représenté par la valeur hexadécimale '61', alors
que 'z' sera représenté par la valeur hexadécimale '7A'. Comme nous
ne sommes pas dans le système décimal, nous ne pouvons pas parler de
dizaine et d'unité, les termes de poids fort et faible sont utilisés
(7 est le poids fort et A le poids faible pour 'z').




Une autre vue de la table ASCII. Les entêtes des lignes
représentent les poids forts et ceux des colonnes sont les
poids faibles. Une case donne donc la lettre correspondant
à la valeur hexadécimale représentée par les poids des lignes
et colonnes. Cf [http://en.wikipedia.org/wiki/File:ASCII_Code_Chart.svg](http://en.wikipedia.org/wiki/File:ASCII_Code_Chart.svg)





On pourra utiliser un éditeur hexadécimal (mode hexl d'emacs ou
Online hexeditor, [http://www.onlinehexeditor.com/](http://www.onlinehexeditor.com/)) pour observer
le contenu du fichier [az.txt](http://qkzk.xyz/docs/doc03/az.txt) qui
contient les seuls deux caractères 'a' et 'z'.







Reprennons notre texte


    Je code en binaire !



Donnez le codage en ASCII hexadécimal de ce texte. On peut
commencer par une transcription manuelle puis terminer ou vérifier
à l'aide de l'éditeur hexadécimal.







## Codage ASCII étendu




La nécessité de représenter des textes comportant des caractères non
présents dans la table ASCII tels ceux de l'alphabet latin utilisés en
français comme le 'à', le 'é' ou le 'ç' impose l'utilisation d'un
autre codage que l'ASCII.

Plusieurs propositions de codage coexistent.

Afin de faciliter les choses, ces propositions sont des extensions du
codage ASCII :



*  le codage des caractères présents dans la table ASCII est conservé ;
*  le principe du codage de chacun des caractères sur un octet est conservé.

Mais les 8 bits de l'octet vont être utilisés. Cela permet de coder
28 = 256 caractères, soit 128 caractères
supplémentaires.

L'ISO, organisation internationale de normalisation,
propose de son côté plusieurs variantes de codages adaptées aux
différentes langues. La plus utilisée concerne les langues européennes
occidentales. Il s'agit de l'ISO-8859-1, aussi nommé ISO-Latin1.

Microsoft propose le codage dit Windows-1252 (encore appelé ANSI,
bien que cela puisse paraître abusif, l'ANSI, American National
Standards Institute, n'ayant jamais validé cette table !). Ce codage
ne diffère de l'ISO-8859-1 que pour quelques caractères tels le signe
euro, €, la ligature o-e, œ, ou certains guillemets qui
utilisent des codes réservés par ISO-Latin-1 pour des caractères de
contrôle.


Les tables Windows-1252 (cf [http://fr.wikipedia.org/wiki/Windows-1252](http://fr.wikipedia.org/wiki/Windows-1252))
et ISO-Latin1 (cf [http://fr.wikipedia.org/wiki/ISO_latin_1](http://fr.wikipedia.org/wiki/ISO_latin_1)).





## Plus loin avec les codages UTF




À l'évidence, 256 caractères ne suffisant pas pour représenter les
lettres de tous les alphabets utilisés (pensons au russe, à l'hébreu,
etc.), un nouveau standard a été introduit : Unicode. La table Unicode
comporte la définition de près de cent cinquante mille caractères.

Le codage de cette table est multiple. Le codage le plus couramment
utilisé se nomme UTF-8. Son principe est le suivant : une première
série de caractères sont codés sur un octet. D'autres caractères sont
codés sur deux octets, le premier octet débute par '110' pour
l'indiquer, l'octet suivant débute par '10'. De même des codages sur
3 ou 4 octets sont utilisés pour d'autres caractères. (Cette rapide
introduction à UTF-8 est volontairement simplifiée.)

Les 128 premiers caractères de la table UTF-8 sont compatibles avec
le codage ASCII. Ainsi le codage UTF-8 d'un texte ne comportant que
des caractères présents dans la table ASCII sera le même que le codage
ASCII de ce texte.

Ce ne sera pas vrai pour un texte ISO-Latin-1.

Il importe donc, quand on veut décoder un texte, de savoir quel est
le codage utilisé sous peine de décoder improprement les
caractères.


Dire que le codage UTF-8 de 'é' est 'C3~A9' est un raccourci qui fait
l'impasse sur la notion de point de code.Plus précisément, un codage intermédiaire, nommé point de code est
associé à chaque caractère. On parle de codage Unicode (et non UTF-8).
Pour 'é' il s'agit de '00 E9'. En binaire cela correspond
à '11101001'.Les chiffres binaires du point de code sont rangés aux positions 'x'
dans le schéma suivant de codage sur deux octets
'110x_xxxx 10xx_xxxx'. On obtient donc '1100_0011 1010_1001'. C'est
bien la valeur hexadécimale 'C3 A9' annoncée.








On lit dans une table UTF-8 que le caractère 'é' est codé sur deux
octets par les valeurs hexadécimales 'C3 A9' et le caractère '€'
sur 3 octets par les valeurs hexadécimales 'E2 82 AC'.

Soit un fichier contenant le texte "J'écris € en UTF-8"
codé en UTF-8. Quel sera le texte affiché si un logiciel décode ce
texte en supposant que le codage utilisé est Latin-1 ?

Les caractères ASCII seront décodés correctement. Le caractère 'é'
codé 'C3 A9' sera décodé comme deux caractères Latin-1, respectivement
'Ã' de code 'C3' et '©' de code 'A9'. Le caractère '€' sera
décodé comme trois caractères Latin-1, respectivement 'â' de code
'E2', un caractère de contrôle de code '82', et 'Ì' de code 'AC'. Le
caractère de contrôle s'affichera par exemple sous la forme
'¿'.

Le texte sera donc rendu "J'Ã©cris â¿Ì en UTF-8".






Donner la représentation binaire et/ou hexadécimale d'un texte et
demander quel est le codage utilisé.





# Codage des caractères et HTML







## Jeu de caractères




La norme HTML/CSS prévoit la possibilité d'indiquer le codage
utilisé pour les caractères d'un fichier donné. Le codage utilisé est
précisé par une valeur du tag `<meta>`, comme dans
l'exemple :



~~~html
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
</head>

<body>

<p>J'écris € en UTF-8.</p>

</body>
</html>
~~~





Expérimentez par exemple avec
[http://www.w3schools.com](http://www.w3schools.com), en
particulier [http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_charsets](http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_charsets).




Dans le code HTML précédent, changez le "UTF-8" en "ISO-8859-1" et
observez ce qu'il se passe lors de l'affichage du fichier dans votre
navigateur.


Lors de la définition d'une page HTML, il est important de préciser
l'encodage des caractères utilisés. À défaut, le navigateur web
utilisera un encodage par défaut qui ne correspondra pas
nécessairement à l'encodage utilisé pour écrire le fichier.




## Entités de caractère HTML




Pour certains caractères difficiles à saisir ou pour éviter les
problèmes de codage des caractères, il est possible, en HTML, de coder
les caractères par des suites de caractères ASCII, appelées entités
HTML. Par exemple, ’&eacute;’ pour ’é’ ou ’&euro;’ pour ’€’.


Modifiez le code HTML précédent pour utiliser uniquement l'encodage
ASCII et produire notre phrase habituelle "J'écris € en UTF-8".


On évitera d'abuser de ce codage ASCII des caractères, son usage
intempestif rend le code source HTML peu lisible.


La table [http://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references](http://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references)
liste l'ensemble des codes HTML de caractères.





## Codage des URL




Une URL est l'adresse d'une page web. Par exemple [http://fr.wikipedia.org/wiki/URL](http://fr.wikipedia.org/wiki/URL).

En particulier lors de la circulation des URL sur l’Internet, seuls
les caractères ASCII sont a priori autorisés dans une URL. L’usage de
certains caractères spéciaux tels le ’/’ ou le ’:’ est également
proscrit dans le chemin car ils ont une signification particulière.

Cependant, tous les caractères peuvent être utilisés s’ils sont
codés à l’aide de caractères ASCII. Le codage d’un caractère
correspond à deux chiffres hexadécimaux de son codage Unicode (Unicode
et non UTF-8) précédé du caractère ’%’.






On se souvient que le codage Unicode de ’é’ est ’E9’. Celui de
’:’ est ’3A’.

Fournissez une URL équivalente à [http://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search=url&fulltext=Search](http://fr.wikipedia.org/w/index.php?title=Spécial:Recherche&search=url&fulltext=Search)
qui utilise uniquement des caractères ASCII. Vérifiez votre
résultat en tentant l’accès à cette URL dans votre navigateur
web.
