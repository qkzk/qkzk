---
author: qkzk
draft: false
title: Serveur méteo
bookCollapseSection: true
weight: 9
---


# Site météo

## Présentation d'un projet de serveur météo.

Le principe est de créer :

* une page web (html, css) avec 2 vues
* un serveur web en Python avec [Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/) qui sert cette page
* une application intégrée au serveur qui communique avec [openweathermap](https://openweathermap.org/api)


---

## Utilisation

* L'utilisateur se connecte via le navigateur sur votre site
* Il remplit un formulaire demandant précisant une ville et le type de requête (instantané, prévision)
* Votre serveur transforme ça en une requête API pour openweathermap et envoie la question
* openweathermap renvoie un json
* votre application en extraie les infos
* flask les formate dans la page et sert la page à l'utilisateur

---

Le projet se découpe naturellement en plusieurs parties :

## 1. Simple

1. Formater une requête pour l'API d'openweathermap,
2. envoyer la requête API,
3. ouvrir le fichier json reçu dans Python
4. intégrer ces étapes à deux fonctions "requete_api, lecture_reponse_api".
    La deuxième fonction renvoie les informations devant être présentées.
5. Créer une troisième fonction qui englobe les deux premières.


## 2. Simple

1. créer une page html + css avec 2 vues "meteo instantanée", "prévision sur qq jours". Le second étant optionnel et à garder pour une extension
2. formater votre page avec flask en fonction de données météo que vous SIMULEZ (fausses données mais de même format que les vraies)

En faisant comme ça, on peut développer cette partie avant que la première ne soit réalisée

La première étape de cette partie est d'obtenir une réponse json d'openweathermap et d'en extraire les infos que vous
souhaiterez présenter. Contentez-vous d'abord du minimum : quelques chaînes de caractères.

Assurez-vous de comprendre _comment_ flask intègre ces éléments à une page web. Ce n'est pas votre rôle que de servir
rééllement la page. Seulement d'intégrer les éléments.

## 3. Elaboré

Cette partie se concentre sur l'aspect client serveur. L'idéal et d'obtenir un code source facile à
lire et à améliorer pour intégrer d'autres pages.

1. créer le serveur
2. Servir une page statique
3. le faire tourner sur le réseau du lycée afin qu'un autre poste (de la même salle !) puisse l'atteindre
4. créer le formulaire html permettant de lire les infos de l'utilisateur (http request : GET, POST)
5. faire fonctionner les parties 1 et 2cd

Parmi les nombreuses extensions de cette partie on peut envisager une page
"base.html" qui sera intégrée à toutes les autres avec, par exemple, un menu,
un bas de page.

C'est aussi cet équipier qui pourra commencer les extensions "physiques" du
projet : remplacer les requêtes à openweathermap en une communication avec
un raspberry.


---

Prérequis

Je vous invite à tous réaliser les étapes suivantes avant de commencer ce projet

* Cours Python (qkzk > NSI > cours python)

  Parties 1 à 4 (bases, conditions, boucles, fonctions). Traitez les exos à une étoile

* Cours de première "IHM sur le web" (qkzk > NSI > première > IHM sur le web)
    La dernière étape est le même projet que vous, mais réalisé en beaucoup moins de temps et dirigé par mes soins. Inutile de comparer ça n'aurait aucun sens, les conditions changent
    trop.


---

# Sources :

* [tutoriel flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
* [requêtes, formulaire avec flask en NSI](http://qkzk.xyz/docs/nsi/cours_premiere/ihm_web/).
    Lisez rapidement les éléments dans l'ordre. La partie qui vous intéresse le plus et la
    [dernière](http://qkzk.xyz/docs/nsi/cours_premiere/ihm_web/flask/)
* [api d'openweather map](https://openweathermap.org/api)
* [Exemple d'utilisation de l'api OWM en Python](https://code-maven.com/openweathermap-api-using-python)

---

# Extensions

* Créer une carte de France et intégrer la météo de différentes villes
* Prévisions sur une semaine, formatage des images etc.
* Utilisation de capteurs pour récupérer la météo locale avec un raspberry
* Toute autre idée inspirée d'un site météo...

---

# Les étapes de la requête et le trajet de l'information


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
