---
title: Mini Projet serveur méteo
author: qkzk
weight: 8
---


pdf : [pour impression](/uploads/docsnsi/ihm_web/nsi_prem_projet_flask_print.pdf)

# Serveur méteo

L'objectif de ce mini projet est de mettre en oeuvre ce que vous
avez appris concernant les IHM sur le web, Flask ainsi que l'utilisation d'une
api très simple.

## Présentation du projet


Le principe est de créer :

* une page web (html, css) avec 2 vues
* un serveur web en Python avec Flask qui sert deux pages (formulaire, résultat de la requête)
* Le serveur communique avec [openweathermap](https://openweathermap.org/city/2998324) et intègre la météo de la ville choisie au résultat

---


## Utilisation

* L'utilisateur se connecte via le navigateur sur votre site
* Il remplit un formulaire demandant une ville, par exemple : **Lille**
* Votre serveur redirige l'utilisateur vers une page contenant l'information : **Temp : 12.3°C etc.**

---

## Comparaison avec le formulaire obtenu à la fin du cours

Très peu de nouveautés !


* Votre serveur transforme la réponse au formulaire en une requête API pour openweathermap
* Il envoie la question
* openweathermap renvoie des données
* votre serveur en extraie les infos
* qu'il intègre à la page `resultat.html`

---

## Étapes

**Vous allez d'abord :**

1. Lire et réaliser tout le cours IHM sur le web (qkzk, nsi, premiere, ihm sur le web)
2. Réaliser l'activité finale avec le formulaire. _C'est le point de départ._

**De l'activité finale à la réalisation du projet**

3. Apprendre à passer des requêtes openweathermap _directement dans le navigateur_
4. Réaliser ces requêtes en Python, dans la console
5. Combiner le tout pour créer l'application complète.

---

## Outils

## IDE

* Thonny gère Flask sans problème.
* N'importe quel IDE installé sur votre machine (atom, sublime text...) pour
    écrire le code html (et éventuellement Python)
* On _peut_ servir un site depuis colab avec Flask mais c'est **sport.**
    Un [exemple](https://stackoverflow.com/questions/54465816/how-to-use-flask-in-google-colaboratory-python-notebook). Ouvrez le lien de la première réponse pour découvrir un exemple.

## Librairies

Flask est la seule librairie dont vous ayez besoin.
Elle est déjà présente sur votre machine.

---

## Délais

Ce projet doit être terminé **début décembre**.
J'attends de vous voir travailler pour fixer précisément le délai.
Je vais rater beaucoup de séances alors prédire l'avenir est délicat mais cela
me semble un délai raisonnable.

## Résultat attendu

Le projet final est constitué des fichiers suivants :

~~~
.
├── readme.md
├── serveur.py
└── templates
    ├── index.html
    └── resultats.html
~~~

* `readme.md` est votre compte rendu (!). Vous le rédigerez
  en [markdown](https://openclassrooms.com/fr/courses/1304236-redigez-en-markdown).
  Un éditeur en [ligne](https://stackedit.io/)
* `serveur.py` : est l'unique fichier Python qui fait tout. Partez du résultat
  final de l'activité IHM sur le web "Flask" (le formulaire...) `views.py`
* `index.html` et `resultats.html` sont vos pages web servies par Flask

## D'autres informations sur le projet à cette page :

* L'objectif est de comprendre, pas de devenir un
  [développeur web full stack](https://www.indeed.fr/salaries/D%C3%A9veloppeur-Full-Stack-Salaries)...
* Je vous invite à créer votre propre clé API openweather map, mais
  vous pouvez m'en demander une. Bien sûr, je ne vais pas la publier sur
  mon site...

## Cahier des charges détaillé

1. Servir une page (statique d'abord) avec flask
2. Lire une requête du formulaire
3. Répondre avec des données statiques (sans passer par openweathermap) et les intégrer à la page correctement
3. Transformer la requête du formulaire et envoyer une commande à l'api openweathermap
4. Lire le json en réponse via json load, renvoyer ce json
5. Extraire les infos du json et remplir un dictionnaire avec la requête
5. Remplir le template de reponse avec les vraies données
6. Extensions : css, prévisions, carte de France avec les villes, ce que vous voulez.

---

# Sources :

* [tutoriel flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
* [IHM sur le web; formulaire avec flask en NSI](http://qkzk.xyz/docs/nsi/cours_premiere/ihm_web/).
* [api d'openweather map](https://openweathermap.org/api)
* [Exemple d'utilisation de l'api OWM en Python](https://code-maven.com/openweathermap-api-using-python)

---

# Extensions

* Créer une carte de France et intégrer la météo de différentes villes
* Prévisions sur une semaine, formatage des images etc.
* Utilisation de capteurs pour récupérer la météo locale avec un raspberry
* Toute autre idée inspirée d'un site météo...

---


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
