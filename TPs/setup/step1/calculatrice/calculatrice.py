# -*- coding: utf-8 -*-
import parser
import operateur 

op = {'+': operateur.addition,
      '-': operateur.soustraction,
      '*': operateur.multiplication,
      '/': operateur.division}

class Calculatrice:
    """
    classe Calculatrice

    calcule de façon rudimentaire une expression composée 
    de nombres et d'opérations simples (+, -, *, /). 

    Ne regarde pas l'ordre des opérateurs mais réalise 
    les opérations de gauche à droite.

    attributs

    :attribute numList: liste des nombres constituant l'expression
    :attribute opList: liste des opérateurs constituant l'expression

    :param s: l'expression à calculer

    """
    def __init__(self, s):
        self.numList, self.opList = parser.parser(s)

    def nombre_op(self):
        """
        retourne le nombre d'opérateur dans l'expression à calculer.
        """
        return len(self.opList) - 1
        
    def calcul(self):
        """
        calcul du résultat de l'expression
        """
        res = 0
        for o, num in zip(self.opList, self.numList):
            res = op[o](res, num)
        
        print res


if __name__ == '__main__':
    s = '3 + 4 * 6 / 5'
    c = Calculatrice(s)

    c.calcul()
    print c.nombre_op()
