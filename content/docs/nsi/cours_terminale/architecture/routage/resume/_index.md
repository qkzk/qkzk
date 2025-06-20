---
title: "Résumé"
author: "David Roche"
theme: "metropolis"
geometry: "margin=1.5cm"
weight: 1000

---

[pdf](./resume.pdf) -- Ce résumé a été écrit par [David Roche](https://pixees.fr/informatiquelycee/n_site/nsi_term_archi_routage.html)

## Protocoles de routage  

### Ce qu’il faut savoir  

- un routeur permet de relier ensemble plusieurs réseaux locaux.
- chaque routeur possède une table de routage. Une table de routage peut être vue  
  comme un tableau qui va contenir des informations permettant au routeur d'envoyer  
  le paquet de données dans la "bonne direction".  

- il existe 2 méthodes permettant de renseigner la table de routage d’un routeur :  
  - le routage statique : chaque ligne doit être renseignée "à la main". Cette  
    solution est seulement envisageable pour des très petits réseaux de réseaux  
  - le routage dynamique : tout se fait "automatiquement", on utilise des  
    protocoles qui vont permettre de "découvrir" les différentes routes  
    automatiquement afin de pouvoir remplir la table de routage tout aussi  
    automatiquement.  

- un réseau de réseaux comportant des routeurs peut être modélisé par un graphe (si  
  nécessaire revoir le cours sur les graphes) : chaque routeur est un sommet et chaque  
  liaison entre les routeurs ou entre un routeur et un switch est une arête. Les  
  algorithmes utilisés par les protocoles de routages sont donc des algorithmes issus  
  de la théorie de graphes.  

- les 2 protocoles au programme de terminale NSI sont les protocoles RIP (Routing  
  Information Protocol) et OSPF (Open Shortest Path First) :  

  - **protocole RIP** : le protocole RIP s'appuie sur l'algorithme de Bellman-Ford  
    (algorithme qui permet de calculer les plus courts chemins dans un graphe).  
    Le protocole RIP utilise le nombre de sauts comme métrique. Ce protocole  
    est aujourd'hui très rarement utilisé dans les grandes infrastructures.  

  - **protocole OSPF** : le protocole OSPF s'appuie sur l'algorithme de Dijkstra. Le  
    protocole OSPF utilise le “coût” comme métrique (la notion de coût est  
    directement liée au débit des liaisons entre les routeurs).  

### Ce qu’il faut savoir faire  

Vous devez être capable d’identifier la route empruntée par un paquet suivant le protocole  
de routage utilisé (RIP ou OSPF).
