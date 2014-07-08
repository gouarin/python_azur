# -*- coding: utf-8 *-*
import numpy as np
import scipy.sparse as sps

def laplacian2D(u, h):
    """
    Produit matrice-vecteur du Laplacien sans assemblage de la matrice

    """
    cx = -1./h[0]**2
    cy = -1./h[1]**2
    c = -2.*(cx + cy)

    lap = c*u
    lap[:, :-1] += cx*u[:, 1:]
    lap[:, 1:] += cx*u[:, :-1]
    lap[1:, :] += cy*u[:-1, :]
    lap[:-1, :] += cy*u[1:, :]
    
    return lap

def laplacianSparse(h, n):
    dim = len(n)
    # 1D laplacian matrix
    if dim==1:
        return 1./h[0]**2*sps.spdiags([-np.ones(n[0]), 2*np.ones(n[0]), -np.ones(n[0])],[-1, 0, 1], n[0], n[0])
    # 2D laplacian matrix
    if dim==2:
        M1Dx = sps.spdiags([-np.ones(n[0]), 2*np.ones(n[0]), -np.ones(n[0])], [-1, 0, 1], n[0], n[0])
        I1x = sps.eye(n[1], n[1])
        M1Dy = sps.spdiags([-np.ones(n[1]), 2*np.ones(n[1]), -np.ones(n[1])], [-1, 0, 1], n[1], n[1])
        I1y = sps.eye(n[0], n[0])
        return 1./h[1]**2*sps.kron(M1Dy, I1y) + 1./h[0]**2*sps.kron(I1x, M1Dx)
    # 3D laplacian matrix
    if dim==3:
        M1Dx = sps.spdiags([-np.ones(n[0]), 2*np.ones(n[0]), -np.ones(n[0])],[-1, 0, 1], n[0], n[0]) 
        I1x = sps.eye(n[1], n[1])
        M1Dy = sps.spdiags([-np.ones(n[1]), 2*np.ones(n[1]), -np.ones(n[1])], [-1, 0, 1], n[1], n[1])
        I1y = sps.eye(n[2], n[2])
        M1Dz = sps.spdiags([-np.ones(n[2]), 2*np.ones(n[2]), -np.ones(n[2])], [-1, 0, 1], n[2], n[2])
        I1z = sps.eye(n[1], n[1])
        I2 = sps.eye(n[2]*n[1], n[2]*n[1])
        M2D = 1./h[2]**2*sps.kron(M1Dz, I1z) + 1./h[1]**2*sps.kron(I1y, M1Dy)  
        return sps.kron(M2D, I1z) + 1./h[0]**2*sps.kron(I2, M1Dx)
