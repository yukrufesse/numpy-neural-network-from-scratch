Markdown
# Réseau de Neurones Artificiels (From Scratch)

Implémentation complète d'un Perceptron Multicouche (MLP) en Python, utilisant uniquement la bibliothèque **NumPy** pour comprendre l'algèbre linéaire sous-jacente des réseaux de neurones.

## Architecture du Réseau
* **Couche d'entrée :** 3 entrées ($x_1 = 1, x_2 = 2, x_3 = 3$)
* **Couche cachée :** 2 neurones avec la fonction d'activation **ReLU**
* **Couche de sortie :** 1 neurone avec la fonction d'activation **Sigmoïde** (pour obtenir une probabilité entre 0 et 1)

## Validation Mathématique (Fait main)
Pour m'assurer que la logique de mon code Python correspondait parfaitement aux équations mathématiques de la propagation avant (*forward propagation*), j'ai résolu l'intégralité des calculs (produit matriciel, ajout du biais, ReLU et Sigmoïde) à la main sur papier.

Le code et les calculs théoriques tombent tous les deux sur le même résultat ultra-précis : **0.99999774**.

### Ma feuille de calcul :
![Feuille de calcul](https://github.com/yukrufesse/numpy-neural-network-from-scratch/blob/main/prouf%20of%20work.jpg?raw=true)

## 🚀 Comment lancer le projet
```bash
pip install numpy
python network.py
