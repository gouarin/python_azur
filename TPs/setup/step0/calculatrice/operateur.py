# -*- coding: utf-8 -*-
"""
Module définissant l'ensemble des opérateurs de notre calculatrice.

"""
from __future__ import division

def addition(a, b):
    """
    réalise l'addition de deux nombres.

    :param a: premier nombre à additionner
    :param b: deuxième nombre à additionner
    :return: addition 

    """
    return a + b

def multiplication(a, b):
    """
    réalise la multiplication de deux nombres.

    :param a: premier nombre à multiplier
    :param b: deuxième nombre à multiplier
    :return: multiplication

    """
    return a*b

def soustraction(a, b):
    """
    réalise la soustraction de deux nombres.

    :param a: premier nombre à soustraire
    :param b: deuxième nombre à soustraire
    :return: addition 

    """
    return a - b

def division(a, b):
    """
    réalise la division réelle de deux nombres.

    :param a: premier nombre à diviser
    :param b: deuxième nombre à diviser
    :return: addition 

    .. warning:: Attention à la division par zéro !!

    """
    return a/b

if __name__ == "__main__":
    print addition(3, 2)
