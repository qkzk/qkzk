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

## Fichiers

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

* La seule librairie dont vous ayez besoin est Flask, déjà présent sur vos postes au lycée. Sinon, `$ pip install flask` si vous êtes sous linux ou recherchez dans google "windows installer librairie python avec pip"...
* Sujet du projet pour les [terminales ISN](http://qkzk.xyz/docs/isn/sujets-des-projets/serveur-meteo/).

    * Ils ont plus de temps,
    * un seul groupe travaille dessus,
    * ils sont 3 et l'un d'eux a déjà fait des trucs complets en Python.
  * Donc inutile de comparer, les conditions sont très différentes.

* Toutes les sources pour réaliser votre projet sont données. Lisez bien le projet pour les terminales.
* L'objectif est de comprendre, pas de devenir un [développeur web full stack](https://www.indeed.fr/salaries/D%C3%A9veloppeur-Full-Stack-Salaries)...
* Je vous invite à créer votre propre clé API openweather map, mais
  vous pouvez m'en demander une. Bien sûr, je ne vais pas la publier sur mon site...

## Cahier des charges

1. Servir une page avec Flask
2. Lire une requête du formulaire
3. Répondre avec des données statiques (sans passer par openweathermap) et les intégrer à la page correctement
3. Transformer la requête du formulaire et envoyer une commande à l'api openweathermap
4. Lire le json en réponse via json load, renvoyer ce json
5. Extraire les infos du json et remplir un dictionnaire avec la requête
5. Remplir le template de reponse avec les vraies données
6. css, prévisions, ce que vous voulez...
