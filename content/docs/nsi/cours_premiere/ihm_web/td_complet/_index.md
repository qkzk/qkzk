---
title: "TD complet"
bookCollapseSection: true
weight: 120

---

pdf [pour impression](./TD_IHM.pdf)

## Exercice 1

Donner le protocole, le domaine et l'URL des adresses suivantes :

1. `https://qkzk.xyz`
2. `http://www.france-ioi.org/`
3. `ftp://192.168.1.2/docs/devoir.pdf`

## Exercice 2

Quelles sont les URL correctes ? Proposer une rectification des URL fausses.

1. `http:///jerome.fr`
2. `https://jerome.fr/base/index?r=toto`
3. `http://jerome.fr/base/index#ailleurs`
4. `http://ici.jerome.fr/base index ailleurs`
5. `http://jerome.fr/bla?r=toto&d=tata`

## Exercice 3

On considère l'arborescence de fichiers suivante :

```
/
+-- corr_2
|   +-- content
|   |   +-- index.html
|   |   +-- contenu.html
|   +-- view.py
+-- serveur
|   +-- essai
|   |   +-- resultat.html
|   +-- view.py
+-- templates
    +-- score.html

```


1. Donner l'adresse absolue de `contenu.html`
2. Donner l'adresse relative de `resultat.html` depuis `/templates`
3. Donner l'adresse relative de `index.html` depuis `/serveur/essai`

## Exercice 4

Voici un extrait de code html d'une page web ouverte dans le navigateur.

```html
<!DOCTYPE html>
<html>
<head>
  <title>
    Bowling 
  </title>

</head>
<body>
  <h1>
    Le bowling, ma passion
  </h1>
  <ul>
    <li>
      <a href="materiel.html">Le matériel que j'utilise</a>
    </li>
    <li>
      <a href="http://bowling_metropole.fr/club/index.html">Mon club</a>
    </li>
  </ul>
  <p>
    Compétitions les mardis et vendredis de 20h à minuit. Venez en famille.
  </p>
</body>
</html>
```

1. Quel est le titre de l'onglet de la page dans le navigateur ?
2. Écrire à la main le rendu de la page.
3. Proposer un fichier CSS afin de satisfaire les contraintes suivantes :

    * fond noir sur toute la page,
    * titres en jaune,
    * éléments de liste en rose
    * corps des paragraphes en taille de police 14.
4. Compléter le document html afin de charger votre fichier CSS. On suppose
  que les fichiers html et css sont dans le même dossier.



## Exercice 5

Donner le nom de la balise qui correspond à sa description

1. Paragraphe,
2. Sous-titre,
3. Titre de section,
4. Formulaire,
5. Élément de liste,
6. Liste numérotée.

## Exercice 6

On considère l'extrait de page HTML ci-dessous.

```html
<body>
  <p class="red">Salut la famille</p>
  <p>Comment-allez vous ?</p>
  <p>Ici c'est la grande forme !</p>
</body>
```


1. Donner le code CSS permettant de colorier le texte du premier paragraphe en rouge.
2. Ajouter une instruction CSS afin de colorier tous les paragraphes en vert sauf le
  premier qui doit reste rouge.
