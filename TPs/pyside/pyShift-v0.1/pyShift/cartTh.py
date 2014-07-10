import math
import numpy as np
import pyShift.cartThCy as CTHC

def cartThPurePython1(nx, ny, nz):
  mesh = np.empty((3, nx, ny, nz), dtype=np.float32)
  
  xc = -1.
  for i in xrange(nx):
    yc = -1.
    for j in xrange(ny):
      zc = -1.
      for k in xrange(nz):
        mesh[0, i, j, k] = xc
        mesh[1, i, j, k] = yc
        mesh[2, i, j, k] = zc
        zc += np.tanh(np.abs(-1+2*k/(nz - 1.)))
      y = -1+2*j/(ny - 1.)
      yc += y/(y**2 + 1)
    xc += np.tanh(np.abs(-1.+2*i/(nx - 1.)))
  return mesh

def cartThPurePython2(nx, ny, nz):
  mesh = np.empty((3, nx, ny, nz), dtype=np.float32)
  
  xc = -1.
  for i in xrange(nx):
    yc = -1.
    for j in xrange(ny):
      zc = -1.
      for k in xrange(nz):
        mesh[0, i, j, k] = xc
        mesh[1, i, j, k] = yc
        mesh[2, i, j, k] = zc
        zc += math.tanh(math.fabs(-1+2*k/(nz - 1.)))
      y = -1+2*j/(ny - 1.)
      yc += y/(y**2 + 1)
    xc += math.tanh(math.fabs(-1.+2*i/(nx - 1.)))
  return mesh

def cartThNumpy(nx, ny, nz):
  mesh = np.empty((3, nx, ny, nz), dtype=np.float32)

  x = np.linspace(-1, 1, nx)
  y = np.linspace(-1, 1, ny)
  z = np.linspace(-1, 1, nz)
  
  hx = np.empty(nx)
  hx[0] = -1.
  hx[1:] = np.tanh(np.fabs(x[:-1]))

  hz = np.empty(nz)
  hz[0] = -1.
  hz[1:] = np.tanh(np.fabs(z[:-1]))

  xc = np.add.accumulate(hx)
  zc = np.add.accumulate(hz)
  y[1:] = y[:-1]/(y[:-1]*y[:-1] + 1.)
  y[0] = -1
  yc = np.add.accumulate(y)

  mesh[0, :, :, :] = xc[:, np.newaxis, np.newaxis]
  mesh[1, :, :, :] = yc[np.newaxis, :, np.newaxis]
  mesh[2, :, :, :] = zc[np.newaxis, np.newaxis, :]
  return mesh

def cartThCythonOB1(nx, ny, nz):
  return CTHC.cartThCythonOB1(nx, ny, nz)

def cartThCythonOB2(nx, ny, nz):
  return CTHC.cartThCythonOB2(nx, ny, nz)

def cartThCythonMV1(nx, ny, nz):
  return CTHC.cartThCythonMV1(nx, ny, nz)

def cartThCythonMV2(nx, ny, nz):
  return CTHC.cartThCythonMV2(nx, ny, nz)

if __name__ == "__main__":
    import time
    nx = ny = nz = 50
    t = time.time()
    m1 = cartThPurePython2(nx, ny, nz)
    print time.time() - t

    t = time.time()
    m2 = cartThNumpy(nx, ny, nz)
    print time.time() - t

    print (m1[0]==m2[0]).all()

