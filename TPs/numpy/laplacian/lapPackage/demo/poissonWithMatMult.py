import numpy as np
import heat
from heat.util import myProdScal

def getCoords(n, h):
    x = np.arange(h[0], 1., h[0])
    x = x[np.newaxis, :]
    x = np.repeat(x, n[1], axis=0).flatten()

    y = np.arange(h[1], 1., h[1])
    y = y[:, np.newaxis]
    y = np.repeat(y, n[0], axis=1).flatten()

    coord = np.zeros((x.size, 3))
    coord[:, 0] = x
    coord[:, 1] = y
        
    return coord
    
def setDirichlet(b, h):
    """
    Conditions de Dirichlet avec 
        u = 1. en x=0 
        u = 0. sinon

    """
    b[:, 0] += 1./h[0]**2

dim = 2
matplot = False

n = [99]*dim
h = [1./(i + 1) for i in n]

u = np.zeros(n)
b = np.ones(n)

setDirichlet(b, h)

heat.conjugateGradient(heat.laplacian2D, b, u, myProdScal, extraMatMult=(h,))        

if matplot:
    heat.plotWithMatplotlib(u)
else:
    heat.plotWithVTK(n, getCoords(n, h), u.flatten())
