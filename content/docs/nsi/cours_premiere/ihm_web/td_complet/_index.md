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
    <title>Bowling</title>
  </head>
  <body>
    <h1>Le bowling, ma passion</h1>
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

   - fond noir sur toute la page,
   - titres en jaune,
   - éléments de liste en rose
   - corps des paragraphes en taille de police 14.

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

## Exercice 7

Proposer le code html d'une page avec :

- le titre de l'onglet : _"Mon super site"_
- un lien vers un fichier css : _style.css_
- un titre dans la page _"Welcome!"_
- un paragraphe : "_développeur en devenir. Mes passions :_"
- une liste non numérotée :
  - "_les cartes magic_"
  - "_le tuning de trottinette électrique_"
  - "_les photos de train_"
- un lien vers google.com

Dans le fichier de style, déclarer

- une couleur de fond noire,
- une couleur de texte blanche,
- les liens en vert,

[page](./page.html_) et [css](./style.css)

## Exercice 8

JP a crée un chat avec Flask et il le présente à ses amis. Il analyse la console Python lorsque ceux-ci se connectent.

```sh
$ python server_JP_chat.py                                                                                                                                                           (master|✚1…1⚑2)
 * Serving Flask app 'serveur_JP_chat'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://10.10.10.10:8080
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-076-025
127.0.0.1 - - [08/Dec/2024 20:40:39] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Dec/2024 20:40:39] "GET /static/style.css HTTP/1.1" 200 -
127.0.0.1 - - [08/Dec/2024 20:40:39] "GET /favicon.ico HTTP/1.1" 404 -
```

1. Quelle adresse doivent utiliser ses amis pour se connecter ?
2. Frank a tenté de se connecter à 20h40 et affirme y être parvenu. Est-ce vrai ? Justifier. Combien de fichiers sont nécessaires pour lire la page ?
3. Que signifie le 404 dans la dernière ligne ?
4. Un peu plus tard, Frank envoie des messages sur le site de JP. Voici les enregistrements lus par JP dans la console Python.

   ```sh
   127.0.0.1 - - [08/Dec/2024 20:40:43] "POST / HTTP/1.1" 200 -
   127.0.0.1 - - [08/Dec/2024 20:40:43] "GET /static/style.css HTTP/1.1" 304 -
   127.0.0.1 - - [08/Dec/2024 20:44:26] "POST / HTTP/1.1" 200 -
   127.0.0.1 - - [08/Dec/2024 20:44:26] "GET /static/style.css HTTP/1.1" 304 -
   127.0.0.1 - - [08/Dec/2024 20:44:30] "POST / HTTP/1.1" 200 -
   127.0.0.1 - - [08/Dec/2024 20:44:30] "GET /static/style.css HTTP/1.1" 304 -
   ```

   - Combien de message ont-été envoyés ?
   - Quelle méthode HTTP est utilisée par JP pour transmettre le formulaire ?
   - Le code 304 signifie "Not Modified" : _Status Code 304, also known as “Not Modified,” is an HTTP response code indicating that the requested resource has not been modified since the client’s last request._

     Expliquez pourquoi le serveur répond 304 lors de ces requêtes. Quel intérêt ?

5. Frank affirme avoir exécuté ces requêtes à la main avec le module `requests` de Python. JP affirme qu'il ment et qu'elles ont été effectuées par un navigateur. Qu'en pensez-vous ?
