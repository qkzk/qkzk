---
title: "cours: Les URL"
bookCollapseSection: true
author: David Roche
theme: metropolis
weight: 2

---

pdf : [pour impression](./nsi_prem_url.pdf)


# Les URL

Dans la barre d'adresse de votre navigateur web vous trouvez, quand
vous visitez un site, des choses du genre :
"`https://qkzk.xyz/docs/nsi/cours_premiere/programmation/comparaison/`".

La partie
"`/docs/nsi/cours_premiere/programmation/comparaison/`" s'appelle une URL.

Plus précisément :

| protocole  | domaine    | URL                                                   |
|------------|------------|-------------------------------------------------------|
| `https://` | `qkzk.xyz` | `/docs/nsi/cours_premiere/programmation/comparaison/` |


Une URL (Uniform Resource Locator) permet d'identifier une ressource
(par exemple un fichier) sur un réseau.

L'URL indique « l'endroit » où se trouve une ressource sur un
ordinateur. Un fichier peut se trouver dans un dossier qui peut lui-même
se trouver dans un autre dossier... On parle d'une structure en
arborescence, car elle ressemble à un arbre à l'envers :

![arbo](/uploads/docsnsi/ihm_web/img/url.jpg)


Comme vous pouvez le constater, la base de l'arbre s'appelle la _racine_ 
de l'arborescence et se représente par un `/`

## Chemin absolu ou chemin relatif ?

Il existe deux types de chemins dans une arborescence : **absolu** et **relatif**.

Le chemin absolu doit indiquer le chemin depuis la racine. 

Par exemple l'URL du fichier `fichier3.jpg` sera : `/dossier2/dossier3/fichier3.jpg`

Remarquez que nous démarrons bien de la racine `/` 

(attention les symboles de séparation sont aussi des `/`)

Imaginons maintenant que le fichier fichier1.css fasse appel au fichier
fichier3.jpg (comme un fichier HTML peut faire appel à un fichier CSS).
Il est possible d'indiquer le chemin non pas depuis la racine, mais
depuis le dossier (dossier2) qui accueille le fichier1.css, nous
parlerons alors de chemin relatif :

`dossier3/fichier3.jpg`

Remarquez l'absence du `/` au début du chemin (c'est cela qui nous
permettra de distinguer un chemin relatif et un chemin absolu).

Imaginons maintenant que nous désirions indiquer le chemin relatif du
fichier fichier1.css depuis l'intérieur du dossier dossier4.

Comment faire ?

Il faut « remonter » d'un « niveau » dans l'arborescence pour se
retrouver dans le dossier dossier2 et ainsi pouvoir repartir vers la
bonne « branche ». Pour ce faire il faut utiliser 2 points :`..` 

`../dossier2/fichier1.css`

Il est tout à fait possible de remonter de plusieurs « crans » :`../../` 
depuis le dossier dossier4 permet de « retourner » à la racine.

En résumé :

**Chemin absolu**

* débute par `/`
* indique l'adresse depuis la racine

**Chemin relatif**

* ne débute par par `/`
* indique l'adresse depuis la position actuelle
* `../` signifie un niveau plus haut dans l'arborescence

## À faire vous-même 1

Soit la structure en arborescence suivante:

![arbo](/uploads/docsnsi/ihm_web/img/url.jpg)

Le contenu du fichier "`fichier7.odp`" utilise le fichier
"`fichier5.svg`". Donnez le chemin relatif qui devra être renseigné
dans le fichier "`fichier7.odp`" afin d'atteindre le fichier
"`fichier5.svg`".

Donnez le chemin absolu permettant d'atteindre le fichier
"fichier6.html".

---

Remarque : la façon d'écrire les chemins (avec des slash (`/`) comme
séparateurs) est propre aux systèmes dits « UNIX », par exemple
GNU/Linux ou encore Mac OS. Sous Windows, ce n'est pas le slash qui est
utilisé, mais l'antislash (`\\`). Pour ce qui nous concerne ici, les
chemins réseau (et donc le web), pas de problème, c'est le slash qui
est utilisé.
