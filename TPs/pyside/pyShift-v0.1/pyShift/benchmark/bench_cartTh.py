import pyShift.cartTh as CTH
import pyShift.cartThCpp as CTHPP
import time

def timeit(method, args=(), nrep=100):
    t = time.time()
    for i in xrange(nrep):
        method(*args)
    return method.__name__, (time.time() - t)/nrep

nx = ny = nz = 100
nrep = 10

#print timeit(CTH.cartThPurePython1, (nx, ny, nz), nrep)
print timeit(CTH.cartThPurePython2, (nx, ny, nz), nrep)
print timeit(CTH.cartThNumpy, (nx, ny, nz), nrep)
print timeit(CTH.cartThCythonMV1, (nx, ny, nz), nrep)
print timeit(CTH.cartThCythonMV2, (nx, ny, nz), nrep)
print timeit(CTH.cartThCythonOB1, (nx, ny, nz), nrep)
print timeit(CTH.cartThCythonOB2, (nx, ny, nz), nrep)
print timeit(CTHPP.cartThCythonWrap, (nx, ny, nz), nrep)
