# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from timeit import default_timer as timer
import juliaCython

def myTimer(fonction, fonction_args=(), nrep=10):
    t = timer()
    for i in xrange(nrep):
        fonction(*fonction_args)
    try:
        name = fonction.__name__
    except:
        name = fonction.py_func.func_name
    return [name, (timer() - t)/nrep]

def juliasetPurePython(x, y, c, lim, maxit):
    """ 
    Renvoie l'ensemble de Julia
    
    Paramètres
    ----------
    x: coordonnées des parties réelles regardées
    y: coordonnées des parties imaginaires regardées
    c: nombre complexe figurant dans z^2 + c
    lim: limite du module complexe à partir de laquelle la suite est dite divergente
    maxit: nombre d'itérés maximal
    
    """
    julia = np.zeros((x.size, y.size))

    for i in xrange(x.size):
        for j in xrange(y.size):
            z = x[i] + 1j*y[j]
            ite = 0
            while abs(z) < lim and ite < maxit:
                z = z**2 + c
                ite += 1
            julia[j, i] = ite

    return julia

def juliasetNumpy(x, y, c, lim, maxit):
    julia = np.zeros((x.size, y.size), dtype=np.int32)

    zx = x[np.newaxis, :]
    zy = y[:, np.newaxis]
    
    z = zx + zy*1j
    
    ite = 0
    while not np.all(julia) and ite < maxit:
        z = z**2 + c
        mask = np.logical_not(julia) & (np.abs(z) >= lim)
        ite += 1
        julia[mask] = ite

    return julia


if __name__ == '__main__':

    # taille de la grille
    #nx, ny = 64, 64
    nx, ny = 1024, 1024
    # limites indiquant quand la suite diverge
    lim, maxit = 400, 2000
    # valeurs à visualiser 
    vmin, vmax = 0, 200
    # définition de la grille
    x = np.linspace(-1.6, 1.6, nx)
    y = np.linspace(-1.6, 1.6, ny)
    c = -0.772691322542185 + 0.124281466072787j

    exec_time = []
    exec_time.append(myTimer(juliasetPurePython, (x, y, c, lim, maxit), 1))
    exec_time.append(myTimer(juliasetNumpy, (x, y, c, lim, maxit), 10))
    exec_time.append(myTimer(juliaCython.juliasetCython_v1, (x, y, c, lim, maxit), 100))
    exec_time.append(myTimer(juliaCython.juliasetCython_v2, (x, y, c, lim, maxit), 100))
    exec_time.append(myTimer(juliaCython.juliasetCython_openMP, (x, y, c, lim, maxit), 100))
    
    
    t = np.asarray([e[1] for e in exec_time])
    ti = np.argsort(t)

    for i in ti:
        print exec_time[i][0], '\t', exec_time[i][1], '\t', exec_time[i][1]/exec_time[ti[0]][1] 
