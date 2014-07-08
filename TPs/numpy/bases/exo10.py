import numpy as np

def repeat_twice(a):
    np.repeat(np.repeat(a, 2, axis=0), 2, axis=1)

a = np.arange(1, 5, dtype = 'i').reshape((2, 2))
print repeat_twice(a)
