#cython: boundscheck=False
#cython: wraparound=False
#cython: cdivision=True

import numpy as np

cdef extern from "extmods/laplacian.h":
     void laplacian2DinC(int nx, int ny, double *h, double *x, double *y)


def laplacian2DCython(double [:, ::1] u, double [:] h):
    cdef: 
      double cx = -1./(h[0]*h[0])
      double cy = -1./(h[1]*h[1])
      double c = -2.*(cx + cy)
      int ny = u.shape[0], nx = u.shape[1]
      double [:, ::1] lap = np.empty((ny, nx))
      int i, j
      double tmp

    for j in xrange(ny):
      for i in xrange(nx):
        tmp = c*u[j , i]
        if i > 0:
          tmp += cx*u[j, i - 1] 
        if i < nx - 1:
          tmp += cx*u[j, i + 1]
        if j > 0:
          tmp += cy*u[j - 1, i] 
        if j < ny - 1:
          tmp += cy*u[j + 1, i]
        lap[j, i] = tmp

    return lap

def laplacian2DCythonWithC(double [:, ::1] x, double[::1] h):
    """
    Produit matrice-vecteur du Laplacien sans assemblage de la matrice

    """
    cdef:
        int nx = x.shape[1]
        int ny = x.shape[0]
        double [:, ::1] y = np.empty((ny, nx))

    laplacian2DinC(nx, ny, &h[0], &x[0,0], &y[0,0])

    return y
