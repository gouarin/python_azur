# -*- coding: utf-8 *-*
import numpy as np

def myMultSparse(x, A):
    """
    Produit matrice-vecteur du Laplacien à l'aide d'une matrice creuse A

    """
    return A*x

def myProdScal(x, y):
    """
    Produit scalaire pour 2 tableaux x et y de dimension 2.

    On les remet en 1D avant de faire le produit scalaire.

    """
    return np.sum(x*y)
