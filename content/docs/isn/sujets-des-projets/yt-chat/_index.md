---
author: qu3nt1n
date: 2017-12-28 14:41:40+00:00
draft: false
title: YT Chat
weight: 13
---

# YT Chat




### Objectif


L'objectif de ce projet est de réaliser un chat accessible dans le navigateur qui gère les pseudonymes et joue automatiquement et pour tous les utilisateurs en même temps une video youtube dont on copie colle le lien dans le chat.

C'est un projet qui mêle différentes technologies : html, css, js et node.js

Parmi tous les projets "javascript" c'est de loin le plus abouti.

![YTchat](http://qkzk.xyz/wp-content/uploads/2017/12/YTchat.gif)





## Principe


Votre programme se compose de deux fichiers : index.js et index.html



* **index.js** est une application node.js qui sert le fichier index.html à tous les utilisateurs connectés à l'adresse que vous fournirez. Ce fichier déploie les informations (connexion, déconnexion, messages, lien youtube joué automatiquement) à tous les utilisateurs.
* **index.html** est un fichier html contenant du css (pour la mise en page) et du javascript (pour la récupération des informations saisies (nom d'utilisateur, messages envoyés) et reçues par le serveur (connexion, déconnexion, message reçu, vidéo lancée). De plus il contiendra une fenêtre permettant de jouer automatiquement la vidéo.



### Cahier des charges





1. Créer une application node.js envoyant une information à tous ses utilisateurs. Celle-ci est affichée à l'écran.
2. Version simple du chat (un simple formulaire). Les informations saisies sont affichées dans la console de node.js
3. Publier automatiquement les informations saisies via le serveur dans une fenêtre d'utilisateur à tous les utilisateurs.
4. Mettre en page le site - version simple. Les messages s'affichent à la suite les uns des autres, sans grand effort de style.
5. Ajouter un cadre jouant automatiquement une vidéo youtube prédéfinie.
6. Rendre ce cadre dynamique depuis le serveur (changer son adresse quand on détecte un message particulier).
7. Repérer dans node.js les liens youtube, les formater et envoyer l'adresse au client. Celui-ci change l'adresse dans la fenêtre et joue la vidéo automatiquement.
8. Gestion des utilisateurs. Un nouvel utilisateur doit d'abord saisir son pseudonyme avant d'accéder au chat. Les autres utilisateurs sont informés de son arrivée, de son départ.
9. Hébergement en ligne sur un site gratuit.
10. Mise en forme du chat plus aboutie.



### Extensions


Elles sont infinies.


##### **Côté serveur :**


Ce sont les plus délicates, elles demandent à chaque fois une intégration côté client.



* Gestion des chat rooms : sur plusieurs onglets, dans le même onglet.
* Sauvegarde des informations publiées dans une bdd (format à définir)
* Changement de pseudonyme
* Timestamp des messages
* Ajout d'une image pour chaque utilisateur (aléatoire ou à uploader)
* Messages directs vers un utilisateur dans une autre fenêtre.
* youtube : gestion des playlists. Passage automatique à la vidéo suivante
* Etablissement d'une playlist dans laquelle on peut ajouter, retirer une video
* Mode admin protégé par mot de passe. Seul l'admin peut changer de video. Kick du chat. Ban du chat (reconnaissance par IP ou information du cookie).



##### **Côté client :**


Elles sont parfois plus simples, ne demandant pas d'évolution du serveur



* Mise en page précise du code html, du code css
* Ajout de menus, de boutons pour se reconnecter en cas d'erreur, forcer le redémarrage d'une vidéo
* Mise en page très aboutie : responsive design avec bootstrap
* Intégration de menu dynamiques pour chaque fonction
