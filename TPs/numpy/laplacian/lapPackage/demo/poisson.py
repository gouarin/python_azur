import numpy as np
import heat
from heat.util import myMultSparse

def getCoords(n, h):
    dim = len(n)
    if dim == 1:
        x = np.arange(h[0], 1., h[0])
    elif dim == 2:
        x = np.arange(h[0], 1., h[0])
        x = x[np.newaxis, :]
        x = np.repeat(x, n[1], axis=0).flatten()

        y = np.arange(h[1], 1., h[1])
        y = y[:, np.newaxis]
        y = np.repeat(y, n[0], axis=1).flatten()
    elif dim == 3:
        x = np.arange(h[0], 1., h[0])
        x = x[np.newaxis, np.newaxis, :]
        x = np.repeat(x, n[1]*n[2], axis=0).flatten()

        y = np.arange(h[1], 1., h[1])
        y = y[np.newaxis, :, np.newaxis]
        y = np.repeat(np.repeat(y, n[0], axis=1), n[2], axis=0).flatten()

        z = np.arange(h[2], 1., h[2])
        z = np.repeat(z, n[0]*n[1]).flatten()

    coord = np.zeros((x.size, 3))
    coord[:, 0] = x
    if dim > 1:
        coord[:, 1] = y
    if dim == 3:
        coord[:, 2] = z
        
    return coord
    
def setDirichlet(b, h):
    """
    Conditions de Dirichlet avec 
        u = 1. en x=0 
        u = 0. sinon

    """
    if len(h) == 1:
        b[0] += 1./h[0]**2
    else:
        b[:, 0] += 1./h[0]**2

dim = 1
matplot = False

n = [9]*dim
h = [1./(i + 1) for i in n]

u = np.zeros(n)
b = np.ones(n)

A = heat.laplacianSparse(h, n)
setDirichlet(b, h)

u = u.flatten()
b = b.flatten()

heat.conjugateGradient(myMultSparse, b, u, extraMatMult=(A,))        

if matplot:
    heat.plotWithMatplotlib(u.reshape(n))
else:
    heat.plotWithVTK(n, getCoords(n, h), u)
