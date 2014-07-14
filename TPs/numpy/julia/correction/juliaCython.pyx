import numpy as np
import cython
from cython.parallel import prange
from libc.stdlib cimport malloc, free 

cdef inline double cabs(double complex z) nogil:
    return (z.real*z.real + z.imag*z.imag)

@cython.boundscheck(False)
@cython.wraparound(False)
def juliasetCython_v1(double [:] x, double [:] y, double complex c, double lim, int maxit):
    cdef:
        int [:, ::1] julia = np.zeros((x.size, y.size), dtype = np.int32)
        double lim2 = lim*lim
        double complex z
        int ite, i, j, nx=x.size, ny=y.size

    for i in xrange(nx):
        for j in xrange(ny):
            z = x[i] + 1j*y[j]
            ite = 0
            while  cabs(z) < lim2 and ite < maxit:
                z = z**2 + c
                ite += 1
            julia[j, i] = ite

    return julia

@cython.boundscheck(False)
@cython.wraparound(False)
def juliasetCython_v2(double [:] x, double [:] y, double complex c, double lim, int maxit):
    cdef:
        int [:, ::1] julia = np.zeros((x.size, y.size), dtype = np.int32)
        double tmp, zr, zi, lim2 = lim*lim
        double cr = c.real, ci = c.imag
        int ite, i, j, nx=x.size, ny=y.size

    for i in xrange(nx):
        for j in xrange(ny):
            zr = x[i] 
            zi = y[j]
            ite = 0
            while (zr*zr + zi*zi) < lim2 and ite < maxit:
                zr, zi = zr*zr - zi*zi + cr, 2*zr*zi + ci
                ite += 1
            julia[j, i] = ite

    return julia


@cython.boundscheck(False)
@cython.wraparound(False)
def juliasetCython_openMP(double [:] x, double [:] y, double complex c, double lim, int maxit):
    cdef:
        int [:, ::1] julia = np.zeros((x.size, y.size), dtype = np.int32)
        double tmp, zr, zi, lim2 = lim*lim
        double cr = c.real, ci = c.imag
        int  i, j, nx=x.size, ny=y.size
        int *ite

    for j in prange(ny, nogil=True, schedule='dynamic'):
        ite = <int *> malloc(sizeof(int))
        for i in xrange(nx):
            zr = x[i] 
            zi = y[j]
            ite[0] = 0
            while (zr*zr + zi*zi) < lim2 and ite[0] < maxit:
                zr, zi = zr*zr - zi*zi + cr, 2*zr*zi + ci
                ite[0] += 1
            julia[j, i] = ite[0]
        free(ite)
        
    return julia