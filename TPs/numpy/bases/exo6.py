import numpy as np

a = np.diag(np.arange(2, 7, dtype = 'f8'), -1)[:, :-1]
print a

a = np.ones((4, 4), dtype='i'); a[2, -1] = 2; a[-1, 1] = 6
print a
