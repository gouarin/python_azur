import numpy as np

def positive_elements(x):
    return x[x>0]

x = np.arange(10) - 5
print x
pos_x = positive_elements(x)
print pos_x
