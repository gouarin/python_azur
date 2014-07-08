# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt
import heat

def initSol(nx, ny, h, Lx=[0., 1.], Ly=[0., 1.]):
    """
    Initialisation d'une fonction pour tester le schéma en temps

    """
    X, Y = np.meshgrid(np.linspace(Lx[0] + h[0], Lx[1] - h[0], nx), 
                       np.linspace(Ly[0] + h[1], Ly[1] - h[1], ny))
    return 100.*np.exp(-100.*((X - .5)**2 + (Y - .5)**2))

nx, ny = 100, 100
h = [1./(nx + 1), 1./(ny + 1)]
u = initSol(nx, ny, h)

dt = np.min(h)**2/4.
print "dt =", dt
nite = 500

plt.ion()
plot = plt.imshow(u)
plt.colorbar()

for i in xrange(nite):
    u[:, :] = heat.euler(u, -dt, heat.laplacian2D, fargs=(h,))
    plot.set_data(u)
    plt.title("t = {0:5.5e}".format((i + 1)*dt))
    plt.draw()
    plt.pause(0.0001) 
