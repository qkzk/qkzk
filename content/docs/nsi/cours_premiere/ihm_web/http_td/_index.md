---
title: "TD : HTTP"
bookCollapseSection: true
weight: 17

---

### PDF : [pour impression](./TD_IHM_HTTP.pdf)


## Analyser une requête HTTP

Voici l'extrait d'une requête HTTP obtenue sur le site [httpie](https://httpie.io/run)

```bash
$ http -v GET https.qkzk.xyz
```


```html
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: qkzk.xyz
User-Agent: HTTPie/2.0.0
```

1. Quelle est la méthode employée par la requête HTTP ? Quelle URL est demandée ?

2. Complétons ensemble le tableau suivant :

  | Paramètre         | Contenu      | Rôle           |
  |-------------------|--------------|----------------|
  | `Host`            | \hspace{5cm} | $\hspace{5cm}$ |
  | `User-Agent`      |              |                |
  | `Accept`          |              |                |
  | `Accept-Encoding` |              |                |
  | `Connection`      |              |                |


Voici maintenant un extrait de la réponse du serveur :

```html
HTTP/1.1 200 OK
Accept-Ranges: bytes
Access-Control-Allow-Origin: *
Age: 0
Cache-Control: max-age=600
Connection: keep-alive
Content-Encoding: gzip
Content-Length: 836
Content-Type: text/html; charset=utf-8
Date: Wed, 26 May 2021 05:31:12 GMT
ETag: W/"60addaf4-71c"
Last-Modified: Wed, 26 May 2021 05:21:56 GMT
Server: GitHub.com
Vary: Accept-Encoding
Via: 1.1 varnish
X-Cache: MISS
X-Cache-Hits: 0
X-Fastly-Request-ID: 030a81aee4cd0d99f3de1a85e7c5083bc72ee960
X-GitHub-Request-Id: AAD4:4DE7:179655B:2171F65:60ADDCDF
X-Served-By: cache-ewr18171-EWR
X-Timer: S1622007073.955723,VS0,VE13
expires: Wed, 26 May 2021 05:40:07 GMT
x-proxy-cache: MISS

<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="generator" content="Hugo 0.83.1" />
  <meta http-equiv="refresh" content="0; URL=/docs" />
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>
...
</html>
```

3. Quelle est la version du protocole http ?

4. Complétons ensemble le tableau suivant :

    | Paramètre          | Contenu        | Rôle           |
    |--------------------|----------------|----------------|
    | Code réponse       | $\hspace{5cm}$ | $\hspace{5cm}$ |
    | `content-type`     |                |                |
    | `Content-Encoding` |                |                |
    | `Date`             |                |                |
    | `Server`           |                |                |

5. Le code 404 est un code d'erreur. Modifier la requête initiale afin de générer
  un tel code d'erreur.

## `GET` et `POST`

La requête suivante peut être lue dans la barre d'adresse d'un navigateur web,
après avoir cliqué sur le bouton **envoyer** d'un formulaire.

```
http://localhost/cible.html?prenom=Lola?Parfum1=Fraise?Parfum2=Fraise?Parfum3=Chocolat
```

1. S'agit-il d'une requête GET ou POST ? Justifier.
2. Identifier les paramètres envoyés par la requête, ainsi que les valeurs transmises
  correspondantes.
3. Que penser de la confidentialité des paramètres transmis dans la requête ?

