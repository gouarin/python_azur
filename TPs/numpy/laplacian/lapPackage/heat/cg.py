# -*- coding: utf-8 *-*
import numpy as np

def conjugateGradient(matMult, b, x, prodScal = None, extraMatMult=(), maxite = 500, tol = 1e-6):
    """
    Gradient conjugué

    Parameters :
    ------------
    matMult: fonction indiquant comment faire le produit matrice vecteur qui prend 
             au moins comme paramètre un vecteur

    b: second membre

    x: solution recherchée

    prodScal: fonction indiquant comment faire le produit scalaire
              defaut: None prend numpy.dot

    extraMatMult: paramètres optionnels dans la fonction matMult

    maxite: nombre maximal d'itérations 

    tol: tolérance recherchée

    """
    if prodScal is None:
        prodScal = np.dot

    r = b - matMult(x, *extraMatMult)
    p = r.copy()

    r0 = np.linalg.norm(r)
    if r0 == 0:
        r0 = 1.
    residual = 1.

    ps1 = prodScal(r, r) 

    ite = 1

    while residual > tol and ite < maxite:
        Ap = matMult(p, *extraMatMult)

        alpha = ps1/prodScal(Ap, p)
        x[:] = x + alpha*p
        r[:] = r - alpha*Ap
        residual = np.linalg.norm(r)/r0

        ps2 = prodScal(r, r)
        beta = ps2/ps1
        p[:] = r + beta*p
        ps1 = ps2
        print "conjugate gradient: ite ", ite, "residual", residual
                
        ite += 1
