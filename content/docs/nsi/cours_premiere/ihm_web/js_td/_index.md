---
title: 'TD : JavaScript'
bookCollapseSection: true
author: qkzk
weight: 10

---

### pdf : [pour impression](./TD_IHM_2_js.pdf)

# HTML

![HTML 5](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/240px-HTML5_logo_and_wordmark.svg.png)

## 1. Ecrire la structure d'une page depuis un modèle

Imaginons que le document devant vous (cet énoncé) soit une page web.

Écrire la structure de la page en question (on peut ignorer les phrases, seules
les balises importent) jusqu'à la fin de l'exercice 1.

Inclure les éléments de style (centrage, taille des polices) dans un fichier 
CSS séparé.

## 2. Dessiner la page depuis un code,

Écrire la page qui sera rendu par le navigateur à partir du code suivant :

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
<ul>
    <li>Hello</li>
    <li>World</li>
</ul>
</body>
</html>
```

# JavaScript

## 1. Éléments de syntaxe

Voici quelques éléments de comparaison entre Python et Javascript :

| Instruction            | Python                     | JavaScript                          |
|------------------------|----------------------------|-------------------------------------|
| Exécuté par            | le programme Python        | le navigateur (généralement)        |
| Code contenu dans      | un fichier .py             | une balise script d'une page html   |
| Créer une variable     | `a = 2`                    | `var a = 2;`                        |
| Fin d'instruction      | retour à la ligne          | point virugle `;`                   |
| indentation            | définit la structure       | optionnelle                         |
| fonction               | `def f(x): ...`            | `function f(x) { expr }`            |
| condition              | `if condition: expression` | `if (condition) { expr }`           |
| boucle for             | `for i in range(10): ...`  | `for (var i=0; i<10; i++) { expr }` |
| boucle while           | `while condition: expr`    | `while (condition) { expr }`        |
| commentaire            | `# un commentaire`         | `// un commentaire`                 |
| écrire dans la console | `print( expr1, expr2 )`    | `console.log( expr1, expr2 );`      |


1. Voici un script Python. Le traduire en JavaScript.

    ```python

    def calculer_imc(taille, masse):
        return masse / taille ** 2


    nom = "Duchmol"
    prenom = "Robert"       # Deuxième prénom Aldo
    taille_robert = 1.8
    masse_robert = 280
    imc_robert = calculer_imc(taille_robert, masse_robert)
    capital = 0
    nombre_mois = 0

    while capital < 1000:
        capital = capital * 1.05 + 100
        nombre_mois = nombre_mois + 1

    print("Il m'a fallu", nombre_mois, "pour accumuler 1000€")

    for i in range(10):
        print(3, "*", i, "=", 3 * i)
    ```


## 2. Modifier le contenu d'une page web avec JavaScript

L'usage courant de JavaScript permet de rendre une page dynamique.

Sans entrer dans le détail, on peut sélectionner un élément de la page (soit
on s'y répérant comme dans un arbre, soit à partir d'une classe ou d'une
indentification) et modifier cet élément (en donnant / changeant les attributs)
ou le contenu html.

Par exemple :

```html
<html>
...
    <body>
        <h1 id="titre">Mon titre</h1>

        <p class="para">Bonjour!</p>
        <p> Comment allez vous ?</p>
        <p class="para">Moi ça va super !</p>
        <ol class="listes">
        </ol>

        <script>
            // du code javascript dans une page html
            document.getElementById("titre").innerHTML = "Mon super titre";
            document.getElementsByClassName("para")[0].innerHTML = "Hello !";
        </script>
    </body>
</html>
```

Dans cet exemple, le contenu html des deux premières balises (h1 et p) est
remplacé.

* `document ` : le document = la page complète
* `getQuelqueChose` : méthode permettant de récupérer des éléments (des balises html) dans l'objet précédent
* `getElementById` : récupère un élément par son `id`
* `.innerHTML = ` : remplace l'attribut `innerHTML` par ce qui suit le signe égal.

1. Que signifie le `[0]` apres `...getElementsByClassName("para")` ?
2. Quels types d'objets retournent les méthodes `getElementsByClassName` et `getElementById` ?
2. Représenter la page qui sera affichée par le navigateur.
2. Ajouter une ligne pour modifier le contenu du dernier paragraphe en 
    "Mes films préférés".
3. On a oublié de remplir la liste des films préférés. En utilisant le même
    procédé, ajouter la liste des trois films préférés de
    Robert (Rambo 1, Rambo 2, Rambo 3) :

    a. À la main directement dans le code html,

    b. Un par un en JavaScript

    c. À l'aide d'une boucle `for`.


## 3. Réagir à un événement

JavaScript permet de réagir à des événements déclenchés par l'utilisateur.
L'exemple le plus simple est peut-être un bouton sur lequel on clique.

Le clic provoque l'appel d'une fonction JavaScript qui modifie alors le 
contenu de la page.

Voici un exemple tiré de w3Schools :

```html
<!DOCTYPE html>
<html>
<body>

<h1>The onclick Event</h1>

<p>The onclick event is used to trigger a function when an element is clicked on.</p>

<p>Click the button to trigger a function that will output "Hello World"
   in a p element with id="demo".</p>

<button onclick="myFunction()">Click me</button>

<p id="demo"></p>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Hello World";
}
</script>

</body>
</html>
```

1. Reprendre l'exemple de l'exercice 2 et ajouter :

    1. Un paragraphe vide,
    2. Un bouton dont le clic déclenche l'appel à une fonction,
    3. Cette fonction affiche la date de naissance de Robert : le premier
        janvier 1964.
2. Modifier la fonction précédente pour qu'elle efface tout le contenu de la
    page.

    _On pourra ajouter une `id` à l'élément `<body>`_
