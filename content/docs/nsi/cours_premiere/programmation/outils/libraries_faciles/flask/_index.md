---
author: qkzk
date: 2019-12-10 07:08:58+00:00
draft: false
title: Flask
bookCollapseSection: true
weight: 7
---

_Brève introduction à la librairie Flask de Python qui permet de créer un site web_

# Flask

Il serait vain d'espérer vous présenter Flask en une page. Flask est utilisé
mondialement pour créer des sites web en Python.

Flask est un "micro framework", un cadre minimaliste qu'on peut étendre à l'infini.

Toute sortes de sites web peuvent être crées avec Flask : pages statiques, chat bot, réseaux sociaux etc.

## Documentation officielle

[L'accueil](http://flask.palletsprojects.com/) et [la prise en main](http://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)

## Tutoriel créant de A à Z un site de micro blogging (très très largement hors programme)

Le site de micro blogging de [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) (La grosse référence de Flask).

## Installation

Par défaut, Flask devrait être installé sur les machines du lycée.

Si ça n'est pas le cas :

sous linux

~~~bash
$ sudo pip3 install flask
~~~

sous windows

Lancer `cmd` en mode admin, demander à un adminstrateur de saisir ses identifiants et

~~~bash
> pip3 install flask
~~~

Si vous êtes derrière un proxy :

~~~bash
> pip3 install --proxy http://ip.proxy:port flask
~~~


## Servir une page statique avec un jeu P5JS, par exemple

[Dépôt du projet](https://github.com/qkzk/qkzk_flask_intro)

Dans **le même dossier**, créer deux dossiers : `templates` et `static`
et les fichiers suivants :

~~~
.
├── views.py
├── templates
|    ├── index.html
|    └── super_jeu.html
└── static
    ├── css
    │   └── style.css
    ├── img
    │   └── chewie.jpg
    └── js
        └── script.js
~~~

Cette structure est celle couramment employée dans un projet Flask.

Cet exemple n'aborde pas la transmission d'information depuis Python vers les pages web.
Pour un exemple de projet utilisant ces méthodes, se référer au cours de première NSI : IHM sur le web.

### `views.py`

~~~python
# coding=utf-8
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/super_jeu')
def hello():
    return render_template('super_jeu.html')


if __name__ == "__main__":
    app.run(port=2332, debug=True)
~~~

### `index.html`

~~~html
<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Mon site avec Flask</title>
    <link rel="stylesheet" href="/static/css/style.css">
  </head>
  <body>
    <div class="presentation">
      <h1>Bienvenue chez moi !</h1>
      <h2>Ma tête</h2>
      <img src="static/img/chewie.jpg " alt="chewie" width="200px" height="200px">
      <h2>Ma vie</h2>
        <p>
          <span>Né à Montevidéo en 1814, j'ai gravi une à une les étapes pour devenir :</span>
          <ol>
            <li>président des états unis,</li>
            <li>pro gamer,</li>
            <li>influenceur,</li>
            <li>avant centre du Réal Madrid !</li>
          </ol>
          <span>Qui peut en dire autant ?</span>
        </p>
      <h2>Mon oeuvre</h2>
        <p>Découvrez mon <a href="super_jeu">super jeu</a>, crée en P5JS</p>
    </div>
  </body>
</html>
~~~

### `super_jeu.html`

~~~
<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Jeu de la vie en P5JS</title>
  </head>
  <body>
    <p>Voici le jeu de la vie. <a href="https://p5js.org/examples/simulate-game-of-life.html">Source.</a></p>
    <script src="https://cdn.jsdelivr.net/npm/p5@0.10.2/lib/p5.js"></script>
    <script src="static/js/script.js" charset="utf-8"></script>
  </body>
</html>
~~~

### `style.css`

~~~css
h1 {
  color:red;
}

span {
  text-align: center;
}

h2 {
  background-color: green;
}
~~~

### `chewie.jpg`

Enregistrer cette image : ![chewie](./img/chewie.jpg) sous le nom `chewie.jpg`

### `script.js`

C'est le jeu de la vie en P5JS

~~~javascript
let w;
let columns;
let rows;
let board;
let next;

function setup() {
  createCanvas(720, 400);
  w = 20;
  // Calculate columns and rows
  columns = floor(width / w);
  rows = floor(height / w);
  // Wacky way to make a 2D array is JS
  board = new Array(columns);
  for (let i = 0; i < columns; i++) {
    board[i] = new Array(rows);
  }
  // Going to use multiple 2D arrays and swap them
  next = new Array(columns);
  for (i = 0; i < columns; i++) {
    next[i] = new Array(rows);
  }
  init();
}

function draw() {
  background(255);
  generate();
  for ( let i = 0; i < columns;i++) {
    for ( let j = 0; j < rows;j++) {
      if ((board[i][j] == 1)) fill(0);
      else fill(255);
      stroke(0);
      rect(i * w, j * w, w-1, w-1);
    }
  }

}

// reset board when mouse is pressed
function mousePressed() {
  init();
}

// Fill board randomly
function init() {
  for (let i = 0; i < columns; i++) {
    for (let j = 0; j < rows; j++) {
      // Lining the edges with 0s
      if (i == 0 || j == 0 || i == columns-1 || j == rows-1) board[i][j] = 0;
      // Filling the rest randomly
      else board[i][j] = floor(random(2));
      next[i][j] = 0;
    }
  }
}

// The process of creating the new generation
function generate() {

  // Loop through every spot in our 2D array and check spots neighbors
  for (let x = 1; x < columns - 1; x++) {
    for (let y = 1; y < rows - 1; y++) {
      // Add up all the states in a 3x3 surrounding grid
      let neighbors = 0;
      for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
          neighbors += board[x+i][y+j];
        }
      }

      // A little trick to subtract the current cell's state since
      // we added it in the above loop
      neighbors -= board[x][y];
      // Rules of Life
      if      ((board[x][y] == 1) && (neighbors <  2)) next[x][y] = 0;           // Loneliness
      else if ((board[x][y] == 1) && (neighbors >  3)) next[x][y] = 0;           // Overpopulation
      else if ((board[x][y] == 0) && (neighbors == 3)) next[x][y] = 1;           // Reproduction
      else                                             next[x][y] = board[x][y]; // Stasis
    }
  }

  // Swap!
  let temp = board;
  board = next;
  next = temp;
}
~~~

## utiliser le serveur

Lancer le serveur avec `$ python views.py`

Rendez-vous sur `http://localhost:2332` dans votre navigateur. Et voilà.
