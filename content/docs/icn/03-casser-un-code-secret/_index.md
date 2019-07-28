---
author: qu3nt1n
date: 2017-06-26 07:07:22+00:00
draft: false
title: 03. Casser un code secret

url: /
---



Pré-requis



 	  * [Cryptographie : codage simple](http://qkzk.xyz/?page_id=83)

Notions abordées



 	  * lexicométrie
 	  * cryptographie simple : casser le code







### Casser le codage simple.


Voilà qui ne semble pas très facile : il y a 26! = 4x1026 combinaisons possibles... Comment déterminer la bonne ? Même kéké connait la réponse : l'analyse fréquentielle.

On va simplement appliquer l'analyse des fréquences sur un texte crypté.

Le texte d'origine, pré formaté : [texte_clair](http://qkzk.xyz/?attachment_id=98)

Le texte crypté : [texte-crypt](http://qkzk.xyz/?attachment_id=99)

La tentative de décryptage : [texte-decrypt](http://qkzk.xyz/?attachment_id=100)

On peut remarquer que c'est loin d'être parfait... C'est tout à fait logique, les fréquences d'apparition des lettres fluctuent d'un texte à l'autre. Néanmoins une quinzaine de lettres sont justes et, pour déterminer les autres on procède en repérant des mots probables.

Voici quelques un script (moche) qui fait tout ça (il est tard).

    
    <code>
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    from string import ascii_lowercase     # ascii_lowercase =='abcdefghijklmnopqrstuvwxyz'
    #print ascii_lowercase
    print "mot code"
    with open('texte-crypt.txt') as f3:
        text3 = f3.read().lower().strip()
        dic3 = {}
        for x in ascii_lowercase:
            dic3[x] = text3.count(x)
    print dic3
    
    print "somme des values"
    total = 0
    for k, v in dic3.items():
        total += v
    
    print "frequences en pourcent"
    frequence = {}
    for k, v in dic3.items():
        frequence[k] = round(100*v/float(total),2)
    print frequence
    
    data = frequence
    cle = sorted(data, key=data.get, reverse=True)
    
    print cle
    
    cle = ''.join(cle)
    print cle
    print len(cle)
    code = text3
    
    ordre = 'eaistnrulodmpcvqgbfjhzxykw'
    
    dechiffre = ''
    for c in text3:
        if c in ascii_lowercase:
            p = cle.index(c)
            m = ordre[p]
        else:
            m = c
        dechiffre = dechiffre + m
    print dechiffre
    with open('texte-decrypt.txt', 'w') as decrypt:
        decrypt.write(dechiffre)
    </code>


Pour aller plus loin on s'intéressera à un chiffrement qui a longtemps résisté, celui de Vigénere. Il a tenu 300 ans avant d'être brisé, c'est encore un record absolu.

Son principe le protège de l'analyse fréquentielle simple... mais c'est par une variante un peu plus élaborée qu'il rendra les armes.


## A l'heure actuelle


La cryptographie moderne repose sur des algorithmes plus élaborés et le plus célèbre est appelé **RSA**. Il est très solide. Grosso modo, sa robustesse vient du fait qu'un ordinateur multiplie beaucoup plus vite qu'il ne divise. Partons d'une situation :

Un message est codé un mot avec une méthode qui nécessite deux clés, une publique et l'autre privée. Ce sont des nombres premiers, ce n'est pas un hasard. Prenons par exemple 29 et 31.

On fait alors le produit 31*29 = 899. Connaissant 29 (ma clé privée) et 899 (la clé publique) je n'ai aucun mal à obtenir 899/29 = 31 : l'autre clé. Les 2 clés étant nécessaires pour déchiffrer, cela ne me prend pas beaucoup de temps. Par contre si un pirate ne connait que 899 (la clé publique qu'il intercepte facilement), il doit chercher quels sont ses diviseurs pour trouver péniblement 29 et 31 après beaucoup d'essais. Il n'existe pas de démarches vraiment meilleures que celle là pour déterminer les clés privées à partir des clés publiques.
Bien sûr, me direz-vous, votre calculatrice trouverait très vite 899 = 29 * 31. Mais quand les clés sont des nombres premiers à 2048 bits (ce qui se converti en 617 chiffres en base 10) alors les combinaisons sont nombreuses et même les machines les plus puissantes mettent beaucoup de temps à obtenir les facteurs.


### Ordinateur quantique


On entend régulièrement parler de **l'ordinateur quantique**. Fondé sur un principe très différent de celui des machines qui nous entourent, il n'a aucun mal à réaliser d'énormes divisions. Il offre d'ailleurs d'immenses possibilités dans beaucoup d'autres domaines tant sa conception est révolutionnaire.
Le hic est que son développement est extrêmement coûteux et qu'il n'est pas envisagé d'en rendre l'usage public. En effet il repose sur des propriétés de la matière qui ne sont accessibles qu'à des températures extrêmement basses et très coûteuses en énergie.
Alors, certes, il permettrait de casser la sécurité de facebook et de lire les messages privées échangés par kéké et sa copine lulu... mais vu ce qu'il coûte on aura mieux à faire.


## Et mes passwords ?


Là c'est à la fois très simple et très compliqué. En vous identifiant quelque part vous créez un password qui est sauvegardé dans la base de donnée du serveur. Si le serveur est bien foutu, ces mots de passes sont HASHES. Ce qui signifie qu'ils sont encodés dès leur création en une version totalement illisible. Quand vous vous connectez, on compare le résultat du hashage de votre essai de mot de passe avec le hashage en mémoire. Le même : entrez ! Autre chose : recommencez.
Et il n'y a rien à faire pour contourner ce mur : le hachage ne pouvant être décrypté.
Les méthodes qui subsistent sont rudimentaires :
1. Tester tous les mots de passe dans un dictionnaire. En attaquant par les classiques "kekeballondor" sera découvert en quelques secondes... mais un mot de passe complexe (et surtout LONG) prendra plus de temps. On parle de _brute force_.
2. à l'obtenir directement auprès de l'utilisateur, soit en enregistrant ses actions sur l'ordinateur (avec un keylogguer) soit en s'arrangeant pour qu'il le tape ailleurs (sur une page détournée, c'est le _phishing_).
3. L'approche la plus courante repose néanmoins sur la confiance... Le pirate convainc quelqu'un de sa bonne foi et obtient un changement de mot passe auprès de la compagnie. Il s'arrange pour récupérer la nouvelle information (en fournissant un nouveau mail, par exemple). Ou alors, tout bêtement il demande ses identifiants à l'utilisateur... C'est le _social engenieering_. Pour en faire l'expérience, téléphonez à votre fournisseur d'accès ou votre opérateur téléphonique pour signaler un dysfonctionnement ou autre. Ils vous demanderont de répondre à quelques questions : "pouvez-vous me rappeler votre adresse ?" Le drame n'est pas très loin.

On peut aussi s'attaquer à un site plus fragile, récupérer login et password et les tenter ailleurs. Souvent les gens gardent le même mot de passe partout... aussi c'est plus facile.
Ah, et le mot de la fin, si le serveur est mal configuré, les mots de passe sont conservés en clair... Et là c'est le drame. La moindre de faille du serveur (et on en découvre tous les jours) peut compromettre toute la base de donnée et la rendre publique : kekeballondor:kekeballondor circule maintenant partout... Ce type de faille a fait "tomber" le PlayStationNetwork pendant plus d'un mois et coûté des milliards à Sony. Les mots de passe (et les numéros de cartes bleues...) circulent encore.
Soyez prudent !

**
Ajout de juin 2017.**

Je me sens obligé de vous rappeler quelques règles d'usages. Vos informations privées ont de la valeur et vous ne souhaitez pas qu'on les publie ou qu'on les utilise contre vous. En 2011, un compte World of Warcraft vide se vendait plus cher qu'un numéro de carte bleu valide. Un compte "top niveau" se vendait plus de 1000$. **En 2011...**



 	  * Changez régulièrement de mot de passe, ne les communiquez pas, ne les réemployez pas. Utilisez des mots de passe longs : _jevaismangerlavoituredemonbeaufrere_ est plus sûr que_ t4t459!. _N'utilisez pas celui là, il finira dans un dictionnaire maintenant que je l'ai publié.
 	  * Il existe des applications / extension de navigateur permettant de conserver vos mots de passe de vous identifier de manière sécurisée. Elles ne sont pas toutes de même qualité. [Comparatif en anglais](http://www.pcmag.com/article2/0,2817,2475964,00.asp) des solutions gratuites.
 	  * Méfiez-vous du phishing. Ne vous connectez jamais sur un site dont vous n'avez pas tapé l'adresse vous même. Votre banque vous envoie un mail pour vous signaler quelque chose, n'employez pas ce lien. Tapez l'adresse ou trouvez la dans google.
 	  * Adoptez une double authentification (password + confirmation par un code envoyé par SMS par exemple). C'est imparfait mais déjà mieux. Toutes les entreprises sérieuses proposent maintenant de la double authentification : Google, Apple, Microsoft, Facebook, Sony, Amazon, Twitter, Twitch, Steam, Blizzard, Paypal, Ebay...
Faîtes le au moins pour le compte de votre téléphone et votre messagerie principale.

 	  * Déconnectez-vous des machines et méfiez vous des réseaux publics (tel que celui du lycée ou le wifi du Macdo).

