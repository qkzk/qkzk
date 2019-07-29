---
author: qu3nt1n
date: 2016-07-01 18:59:10+00:00
draft: false
title: 2. Réseaux
weight: 2
---




# Réseaux et Protocoles.





## Références


On pourra lire les documents suivants qui sont très complets.

Le chapitre 16 [Les réseaux](/uploads/docs/16-reseaux.pdf) du manuel ["Une introduction à la science informatique pour les enseignants de la discipline en lycée"](https://wiki.inria.fr/sciencinfolycee/Une_introduction_%C3%A0_la_science_informatique_pour_les_enseignants_de_la_discipline_en_lyc%C3%A9e).

Le [tutoriel](/uploads/docs/346829-comprendre-les-reseaux-tcp-ip-et-le-fonctionnement-d-internet.pdf) d'[OpenClassrooms](http://www.openclassrooms.com/) sur le fonctionnement d'internet et TCP/IP.

Ces deux références sont plutôt complètes et serviront de références sur le thème du réseau.


## Activités menées en classe


L'objectif de cette activité est d'acquérir une comprehension globale
des questions se posant dans un réseau de communication comme Internet
ainsi que des mécanismes mis en oeuvre pour les résoudre.

Le principe est de proposer collectivement de tels mécanismes après
avoir expérimenté plusieurs situations d'échange de messages inscrits
sur papier au sein de la classe.

Aucune connaissance préalable sur les réseaux n'est nécessaire pour
participer à cette activité.






## Matériel






* un paquet de (petites) feuilles de papier identiques
* un paquet d'enveloppes identiques
* textes assez courts et facilement décomposables (poème, chanson etc)




## Couches physique, lien et réseau







**À vous de jouer ! **Vous devez échanger des messages courts
avec d'autres éléments du réseau plus ou moins distant de vous. Ces
messages peuvent être des affirmations n'attendant pas de réponse ou
au contraire des questions précises aux réponses courtes.


Qu'est ce qu'un **routeur** ?


Vous devez respecter des contraintes dans la transmission des
messages :



* n'échanger qu'avec vos voisins directs (ex : devant, derrière, gauche, droite),
* ne pas stocker de message qui ne vous soit pas adressé.




Suite à ces échanges, réfléchissez aux questions suivantes :



* Quels éléments vous semblent nécessaires pour que l'acheminement des messages se déroule bien ?
* Comment définir la notion de _protocole_ ? Donnez des exemples de protocoles tirés de la vie quotidienne.
* Quel protocole avez vous adopté pour la transmission des messages dans la classe ?
* Comment déterminez-vous à quel voisin vous devez transmettre un message pour qu'il arrive à la bonne personne ?







**Routage. **Pour déterminer à quel voisin transmettre (routage) un message, on
impose maintenant d'utiliser uniquement des informations obtenues dans
le réseau.



* Elaborez une stratégie au sein de la classe.
* Que se passe-t-il lorsqu'une ou plusieurs personnes cessent de participer au réseau ?
* Quelle(s) propriété(s) la stratégie choisie pour le routage doit possèder pour fonctionner dans un réseau dont la topologie peut évoluer ?
* Réfléchir aux problèmes de sécurité qui peuvent être rencontrés dans le réseau lorsqu'un ou plusieurs routeurs/éléves cessent de suivre le protocole choisi par tout le groupe à des fins plus ou moins malveillantes.




Nous allons maintenant essayer de formaliser un peu nos observations
et regarder dans les réseaux réels comme tout celà se passe.





**Structuration en couches. **Les expériences précédentes vous ont en réalité permis de mettre en
évidence trois des _couches protocolaires_ les plus basses d'un réseau.

Dans un premier temps faites des recherches pour expliquer ce
qu'est la structuration en couches et son intérêt pour de déploiement
des réseaux. Vous allez certainement entendre parler du
modèle **OSI** ... Mais qu'est-ce que c'est ?

Approfondissez vos recherches pour comprendre le rôle de chacune
des couches suivantes et identifier dans les protocoles que vous avez
mis en oeuvre ce qui appartient à chacune de ces couches.



1. **couche physique**
2. **couche lien ou liaison de données**
3. **couche réseau**

A quelle couche appartient le protocole **IP** ? D'ailleur comment fonctionne-t-il ?







## Couche transport








**Séquences.**Remettez le réseau formé par la classe en marche. Vous allez vous
échanger des messages longs, comme des poèmes ou des paroles de
chansons. Mais attention, maintenant la taille de chaque message est
limitée, un seul vers est autorisé par message !

Que dire sur l'arrivée des messages composant un poème ?
Élaborez une stratégie pour pouvoir lire correctement un poème que
vous recevez.









**Dans la réalité ...**Vous venez probablement d'expérimenter quelques difficultés dont la
gestion est affectée à la _couche transport_ dans un réseau
réel. Expliquez le rôle de cette couche et identifiez les éléments de
votre propre réseau appartenant à cette couche.

Penchez-vous plus précisément sur le cas de deux protocoles
célèbres, **TCP** et **UDP**, dont vous
expliquerez les principes respectifs.







## Couche applications







**Adressage ?**L'usage des noms est maintenant remplacé par celui d'_adresses
réseau_, chacun connaît la sienne, donnée par votre enseignant,
mais pas celle des autres, du moins au début.

On impose de plus que les adresses du destinataire et de l'expéditeur
soient clairement inscrites sur le message, mais pas leurs noms !

Vous devez continuer à faire fonctionner le réseau, mais avant
élaborez une stratégie pour connaître les adresses auxquelles vous
souhaitez écrire.


**DNS** ça vous dit quelque chose ?


Votre stratégie est elle applicable dans un réseau de grande ou
très grande échelle ? Si ce n'est pas le cas proposez un nouveau
protocole intégrant cette contrainte d'échelle.









**Dynamicité**Certains d'entre vous vont maintenant "tomber en panne" puis
"redémarrer" avec de nouvelles adresses pour simuler l'arrivée de
nouveaux composants dans le réseau comme cela se produit en permanence
dans le réseau mondial.

Modifiez éventuellement votre stratégie pour faire face aux
changements d'adresse.

Pouvez-vous envisager une manière de détourner votre protocoles
à des fins malveillantes ? Proposez éventuellement des modifications
pour éviter ces détournements.









**Attribution des adresses**On impose maintenant un format d'adresse. Combien d'adresses distinctes sont disponibles avec le nouveau
format ? Y en a-t-il suffisamment pour tous dans la salle ?


Et **DHCP** ?


Comment attribuer les adresses à chacun ? Proposez plusieurs
stratégies et comparez les.


D'où vient l'adresse MAC ?


Qu'est ce qu'une adresse MAC ? Dans le réseau de la classe que
pourrait être une adresse MAC et une adresse IP ?




Une fois les couches réseau et transport établies on peut utiliser ces
mécanimes pour envoyer différents types de messages, comme des
requêtes pour les DNS mais aussi HTTP, SMTP, FTP etc.


## Réseau planétaire et normalisation


Vous aurez compris que la définition de protocoles communs est
nécessaire pour pouvoir communiquer d'un bout à l'autre de la planète
et impose donc des accords internationaux.


IAB, IESG IETF, IRTF, IEEE, ISOC, IANA, ICANN,
ART, ETSI, UIT, W3C etc


Effectuez des recherches sur les instances de normalisation,
d'administration et de régulation des réseaux et
télécommunications.
