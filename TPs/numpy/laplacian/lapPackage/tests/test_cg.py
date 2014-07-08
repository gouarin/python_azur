import numpy as np
import heat
from heat.util import myMultSparse
import scipy.sparse.linalg as spspl

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

def init(dim):
    n = [9]*dim
    h = [1./(i + 1) for i in n]

    u = np.zeros(n)
    b = np.ones(n)

    A = heat.laplacianSparse(h, n)
    setDirichlet(b, h)

    u = u.flatten()
    b = b.flatten()
    
    return A, b, u

def solve(A, b, u):
    uscipy, info = spspl.cg(A, b, x0=u, tol=1.e-6, maxiter=500, M=None)
    heat.conjugateGradient(myMultSparse, b, u, extraMatMult=(A,))        
    return uscipy, u

def test_1D():
    A, b ,u = init(1)
    uscipy, u = solve(A, b, u)
    np.testing.assert_array_equal(uscipy, u)

def test_2D():
    A, b ,u = init(2)
    uscipy, u = solve(A, b, u)
    np.testing.assert_array_equal(uscipy, u)

def test_3D():
    A, b ,u = init(3)
    uscipy, u = solve(A, b, u)
    np.testing.assert_array_equal(uscipy, u)

