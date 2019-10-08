---
title: Projet serveur méteo
author: qkzk
theme: metropolis
weight: 8
---
# Serveur méteo

L'objectif de ce mini projet est de mettre en oeuvre tout ce que vous
avez appris concernant les IHM sur le web, Flask et l'utilisation d'une api très simple.

Qui plus est nous allons aussi utiliser des dictionnaire (simples) pour
intégrer des informations à une page web.

Pour cela vous allez d'abord :

1. Lire et réaliser tout le cours IHM sur le web (qkzk, nsi, premiere, ihm sur le web)
2. Réaliser l'activité finale avec le formulaire.

  * Cette partie _peut_ se réaliser dans colab mais c'est sport. Un [exemple](https://stackoverflow.com/questions/54465816/how-to-use-flask-in-google-colaboratory-python-notebook). Ouvrez le lien de la première réponse pour découvrir un exemple.
  * Thonny gère Flask sans problème.
3. Apprendre à passer des requêtes openweathermap _directement dans le navigateur_
4. intégrer ces requêtes à Python
5. Combiner le tout pour créer une interface complète.

## Délais

Ce projet doit être terminé début décembre. Je vais rater beaucoup de séances alors prédire l'avenir est délicat mais cela me semble un délai raisonnable.

Le projet final est constitué des fichiers suivants :

~~~
.
├── readme.md
├── serveur.py
└── templates
    ├── index.html
    └── resultats.html
~~~

* `readme.md` est votre compte rendu (!). Vous le rédigerez en [markdown](https://openclassrooms.com/fr/courses/1304236-redigez-en-markdown). Un éditeur en [ligne](https://stackedit.io/)
* `serveur.py` : est l'unique fichier Python qui fait tout. Partez du résultat final de l'activité IHM sur le web "Flask" (le formulaire...) `views.py`
* `index.html` et `resultats.html` sont vos pages web servies par Flask

## D'autres informations sur le projet à cette page :

* La seule librairie à installer dont vous ayez besoin est Flask, déjà présent sur vos postes au lycée. Sinon, `$ pip install flask` si vous êtes sous linux ou recherchez dans google "windows installer librairie python avec pip"...
* Sujet du projet pour les [terminales ISN](http://qkzk.xyz/docs/isn/sujets-des-projets/serveur-meteo/).

    * Ils ont plus de temps, un seul groupe travaille dessus, ils sont 3 et l'un d'eux a déjà fait des trucs complets en Python. Donc inutile de comparer, les conditions sont très différentes.
    * Toutes les sources pour réaliser votre projet sont données.
    * L'objectif est de comprendre, pas de devenir un [développeur web full stack](https://www.indeed.fr/salaries/D%C3%A9veloppeur-Full-Stack-Salaries)...
    * Je vous invite à créer votre propre clé API openweather map, mais
      vous pouvez m'en demander une. Bien sûr, je ne vais pas la publier sur mon site...

## Cahier des charges

1. servir une page
2. lire une requête du formulaire
3. Répondre avec des données statiques (sans passer par openweathermap) et les intégrer à la page correctement
3. transformer la requête du formulaire et envoyer une commande à l'api openweathermap
4. lire le json en réponse via json load, renvoyer ce json
5. extraire les infos du json et remplir un dictionnaire avec la requête
5. remplir le template de reponse avec les vraies données
6. css, prévisions, ce que vous voulez.



# Les étapes d'une connexion client serveur


## Les éléments

Le client (navigateur web)

Le serveur web (Python + Flask)

Et le site Openweathermap

* ![Le client, le serveur flask et openweathermap](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask(9).svg)



## Le serveur se lance

Quand on exécute le script Python du serveur il attend qu'un client se connecte...

* ![Le serveur se lance et sert une page *index.html*](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask(8).svg)


## Le client se connecte sur le site

L'utilisateur a tapé l'adresse du site dans sa barre d'adresse...

* ![Le client se connecte sur le site](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask(7).svg)


## Le serveur web renvoie alors une page html

La page html est un formulaire à remplir (ville ?) avec un bouton _submit_

* ![première requête : *index.html*, réponse du serveur](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask(6).svg)


## Formulaire rempli, _submit_

L'utilisateur a rempli son formulaire avec _Lille_ et cliqué sur submit

* ![l'utilisateur remplit le formulaire (_Lille_) sur le client, clique *submit*](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask(4).svg)


## Le serveur reçoit et traite la requête

Le serveur Python récupère les données du formulaire et appelle une fonction...

* ![la requête est envoyée au serveur web, qui la traite...](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask(3).svg)


## Le serveur envoie à son tour une requête à OWM...

La requête est transmise à OWM via une URL (string...) qu'on formate

* ![le serveur envoie une requête à OMW avec leur API (_...weather lille..._)](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask(2).svg)


## OWM lit traite la requête et renvoie la météo dans un JSON

JSON (Javascript Object Notation) est le format le plus populaire pour échanger des données sur le web.
Les données ressemblent à un dictionnaire Python. Python manipule sans difficulté les JSON.

* ![OWM lit la requête et répond avec un JSON contenant la météo (*...temp 12.3...*)](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask(1).svg)


## Le serveur traite la réponse et injecte la météo dans une page _resultat.html_

Elle est envoyée au client

Qui l'affiche dans le navigateur.

L'utilisateur lit la météo de Lille : **il fait 12.3°C** !

* ![Le serveur traite la réponse JSON et sert une page au client (*`<p>12.3°C</p>`*)](/uploads/docsnsi/ihm_web/img/meteo_flask/meteo_flask.svg)
