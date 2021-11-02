---
title: NN - partie 2
bookCollapseSection: true
author: qu3nt1n
date: 2019-05-04 11:17:30+00:00
draft: false
type: docs
weight: 1
---

# Englober notre neurone dans une classe

Dans la précédente partie nous avons crée un simple neurone qui prédit une
sortie et résout un problème très simple.

Avant d'aborder des problèmes plus délicats comme la classification d'images
nous allons rendre ce premier neurone un peu plus commode en l'englobant
dans une classe.

## Les classes

_Nous n'allons pas utiliser énormément de notions liées au classes, seulement
celles au programme de Terminale NSI._

On suppose que vous avez déjà travaillé avec les classes en Python, aussi les
notions ne seront pas rappelées au fur et à mesure.

## Définition et initialisation de la classe.

~~~python
import numpy as np


class NeuralNetwork():

    def __init__(self):
        # Racine du générateur de nombre
        np.random.seed(1)

        # On défini les poids synaptiques initiaux entre -1 et 1,
        # centrés sur 0, dans une matrice 3x1
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

~~~


## Simoid et sa dérivée

Nous allons les intégrer comme deux méthodes à la classe.
Ce n'est pas indispensable mais l'idée est d'englober les outils dans la classe
aussi... Ajoutez ces deux méthodes après `__init__`.

~~~python
class NeuralNetwork():

  ...


  def sigmoid(self, x):
      '''
      Sigmoid :  normalise les entrées
      @param x: (float)
      @return: float
      '''
      return 1 / (1 + np.exp(-x))

  def sigmoid_derivative(self, x):
      '''
      Calcule la dérivée de sigmoid
      @param x: (float) l'entrée est déjà une image par sigmoid
      @return: (float) la dérivée
      '''
      return x * (1 - x)
~~~

La seule différence avec les fonctions de la version 1 est qu'elle prenne aussi
`self` en paramètre.

## La méthode `think`

C'est la méthode qui permet au neurone de prédire une résultat en fonction
des poids synaptiques.

Je ne reviens pas sur la démarche, largement abordée dans la partie précédente.

Ajoutez la méthode suivante après les fonctions sigmoid.

~~~python
def think(self, inputs):
    """
    Renvoie las sorties du neurone pour les entrées fournies.
    @param inputs: (np.array) matrice des entrées
    @return: (np.array) vecteur de sortie
    """

    inputs = inputs.astype(float)
    output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
    return output
~~~

## L'entraînement

À nouveau une seule méthode va suffire, qui va simplement contenir notre
boucle de la première partie.

Ajoutez cette dernière méthode à la classe :

~~~python
    def train(self, training_inputs, training_outputs, training_iterations):
        """
        We train the model through trial and error, adjusting the
        synaptic weights each time to get a better result

        Entraine le modèle et ajuste les poids synaptiques au fur et à mesure
        des opérations.
        Modifie les valeurs des poids synaptiques.

        @param training_inputs: (np.array) matrice des entrées
        @param training_outputs: (np.array) matrice des sorties réelles
        @param training_iterations: (int) le nombre d'itérations à réaliser
        @return: (None)
        SE: modifie l'attribut self.synaptic_weights en place
        """
        for iteration in range(training_iterations):
            # On passe les données d'entrainement en paramètre au réseau
            output = self.think(training_inputs)

            # On calcule l'erreur
            error = training_outputs - output

            # L'erreur est multipliée aux entrées et à la dérivée de la fonction
            # sigmoid. Les poids les moins "confiants" sont ainsi les plus
            # ajustés
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            # On ajuste les poids synaptiques
            self.synaptic_weights += adjustments
~~~


La classe est maintenant terminée.

## La fonction `main`

Il reste à écrire une fonction qui crée les objets, réalise l'entrainement
et teste le résultat.

~~~python

def main():
    '''
    Fonction principale qui initialise le réseau de neurone, réalise
    l'entrainement et vérifie la qualité des prédictions sur les données
    d'essais.
    @return: (None)
    SE. Affiche dans les valeurs dans la console.
    '''
    # Initialise le réseau de neurone.
    neural_network = NeuralNetwork()

    print("Random starting synaptic weights: ")
    print(neural_network.synaptic_weights)

    # Les données d'entraînement avec 4 exemples de 3 entrées et une sortie
    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 0],
                                [0, 1, 0]])

    training_outputs = np.array([[0, 1, 1, 0]]).T

    # Entraîne le réseau
    neural_network.train(training_inputs, training_outputs, 10000)

    print("Synaptic weights after training: ")
    print(neural_network.synaptic_weights)

    test_inputs = np.array([[0, 1, 0],
                            [1, 0, 0]])

    actual_outputs = np.array([[0, 1]]).T

    test_outputs = neural_network.think(test_inputs)

    print("New situation: input data :")
    print(test_inputs)
    print("Output data: ")
    print(actual_outputs)
    print("Our network thinks :")
    print(test_outputs)
~~~

On réalise les mêmes calculs que dans la partie précédente.

D'abord on initialise la classe avec `neural_network = NeuralNetwork()`.
Cette variable est un objet de la classe `NeuralNetwork`.

À cette étape, seule la fonction `__init__` a été exécutée.
Ensuite on  crée les deux tableaux pour l'entraînement : `training_inputs` et
`training_outputs` comme précédemment.

On réalise l'entrainement en appelant la méthode `train`

Remarquons qu'il ne fait pas faire référence à `self` dans les paramètres
d'appel d'une méthode de classe.

L'entraînement est terminé et on peut tester le réseau avec la
méthode `think`. Pour cela on l'appelle avec les données de test.

Il ne reste plus qu'à afficher les résultats pour comparer.

## Conclusion

On a maintenant englobé notre réseau dans une classe.
Ce n'est toujours pas un réseau très ambitieux et, à ce point, vous pouvez
avoir remarqué son défaut majeur : les poids synaptiques obtenus ne sont
pas formidables...

En effet, on l'a entraîné avec bien trop peu de données pour qu'il soit
efficace !

Dans la partie suivante nous allons aborder un problème réel et nous allons
utiliser les méthode abordées ici pour le résoudre : la classification des
nombres.


## le code complet

{{< gist qkzk ce5677bb8d0561047b0d647e4293f8ac >}}
