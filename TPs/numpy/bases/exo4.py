import numpy as np

def eratostene(n):
    A = np.ones(n, dtype=np.bool)
    for i in xrange(2, int(np.sqrt(n))):
        if A[i]:
            A[i**2::i] = False

    return np.where(A)[0]

print eratostene(1000)

