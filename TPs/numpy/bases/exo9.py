import numpy as np

def differences(x):
    return x[:-1] - x[1:]

x = np.array([1., 2., -3., 0.])
print differences(x)
