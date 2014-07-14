#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calculatrice.calculatrice import Calculatrice
import sys

if len(sys.argv) != 2:
   print """
usage
=====

./calc.py s

où s est une chaine de caractères représentant l'expression à 
calculer.
"""
   sys.exit()

c = Calculatrice(sys.argv[1])
c.calcul()
