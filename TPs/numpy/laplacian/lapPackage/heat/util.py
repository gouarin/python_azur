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

    """
    return np.sum(x*y)
