cimport numpy as cnp
import numpy as pnp
from libc.math cimport tanh, fabs
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def cartThCythonOB1(int nx, int ny, int nz):
  cdef:
    cnp.ndarray[cnp.float32_t, ndim=4, mode="c"] mesh = pnp.empty((3, nx, ny, nz), dtype=pnp.float32)
    float xc, yc, zc, y
    int i, j, k

  xc = -1.
  for i in xrange(nx):
    yc = -1.
    for j in xrange(ny):
      zc = -1.
      for k in xrange(nz):
        mesh[0, i, j, k] = xc
        mesh[1, i, j, k] = yc
        mesh[2, i, j, k] = zc
        zc += tanh(fabs(-1.+2.*k/(nz-1.)))
      y = -1+2*j/(ny - 1.)
      yc += y/(y*y + 1)
    xc += tanh(fabs(-1.+2.*i/(nx-1.)))
  return pnp.asarray(mesh)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def cartThCythonOB2(int nx, int ny, int nz):
  cdef:
    cnp.ndarray[cnp.float32_t, ndim=4, mode="c"] mesh = pnp.empty((3, nx, ny, nz), dtype=pnp.float32)
    float y
    float hx=2./(nx-1), hy=2./(ny-1), hz=2./(nz-1)
    int i, j, k
    cnp.ndarray[cnp.float32_t, ndim=1, mode="c"] xc = pnp.empty(nx, dtype=pnp.float32)
    cnp.ndarray[cnp.float32_t, ndim=1, mode="c"] yc = pnp.empty(nx, dtype=pnp.float32)
    cnp.ndarray[cnp.float32_t, ndim=1, mode="c"] zc = pnp.empty(nx, dtype=pnp.float32)

  xc[0] = -1.
  for i in xrange(nx-1):
      xc[i+1] = xc[i] + tanh(fabs(-1.+i*hx))

  zc[0] = -1.
  for i in xrange(nz-1):
      zc[i+1] = zc[i] + tanh(fabs(-1.+i*hz))

  yc[0] = -1.
  for i in xrange(ny-1):
    y = -1. + i*hy
    yc[i+1] = yc[i] + y/(y*y + 1)

  for i in xrange(nx):
    for j in xrange(ny):
      for k in xrange(nz):
        mesh[0, i, j, k] = xc[i]
        mesh[1, i, j, k] = yc[j]
        mesh[2, i, j, k] = zc[k]

  return pnp.asarray(mesh)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def cartThCythonMV1(int nx, int ny, int nz):
  cdef:
    float[:, :, :, ::1] mesh = pnp.empty((3, nx, ny, nz), dtype=pnp.float32)
    float xc, yc, zc, y
    int i, j, k

  xc = -1.
  for i in xrange(nx):
    yc = -1.
    for j in xrange(ny):
      zc = -1.
      for k in xrange(nz):
        mesh[0, i, j, k] = xc
        mesh[1, i, j, k] = yc
        mesh[2, i, j, k] = zc
        zc += tanh(fabs(-1.+2.*k/(nz-1.)))
      y = -1+2*j/(ny - 1.)
      yc += y/(y*y + 1)
    xc += tanh(fabs(-1.+2.*i/(nx-1.)))
  return pnp.asarray(mesh)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def cartThCythonMV2(int nx, int ny, int nz):
  cdef:
    float[:, :, :, ::1] mesh = pnp.empty((3, nx, ny, nz), dtype=pnp.float32)
    float y
    float hx=2./(nx-1), hy=2./(ny-1), hz=2./(nz-1)
    int i, j, k
    float [::1] xc = pnp.empty(nx, dtype=pnp.float32)
    float [::1] yc = pnp.empty(nx, dtype=pnp.float32)
    float [::1] zc = pnp.empty(nx, dtype=pnp.float32)

  xc[0] = -1.
  for i in xrange(nx-1):
      xc[i+1] = xc[i] + tanh(fabs(-1.+i*hx))

  zc[0] = -1.
  for i in xrange(nz-1):
      zc[i+1] = zc[i] + tanh(fabs(-1.+i*hz))

  yc[0] = -1.
  for i in xrange(ny-1):
    y = -1. + i*hy
    yc[i+1] = yc[i] + y/(y*y + 1)

  for i in xrange(nx):
    for j in xrange(ny):
      for k in xrange(nz):
        mesh[0, i, j, k] = xc[i]
        mesh[1, i, j, k] = yc[j]
        mesh[2, i, j, k] = zc[k]

  return pnp.asarray(mesh)