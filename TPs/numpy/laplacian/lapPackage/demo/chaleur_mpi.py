# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt
import mpi4py.MPI as mpi
import heat

def initSolPara(nx, ny, h, Lx=[0., 1.], Ly=[0., 1.]):
    """
    Initialisation d'une fonction pour tester le schéma en temps

    """
    # Calcul du nombre de points par processus en y sans les points fictifs
    # on coupe en bandes

    comm = mpi.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    counts = np.empty(size, dtype='i')
    counts[:] = ny/size
    counts[-1] += ny%size
    
    disps = np.cumsum(np.array([0] + [ny/size]*(size-1)))

    disps[1:] -= 1
    counts[1:-1] += 2
    counts[0] += 1
    counts[-1] += 1
    
    yloc = np.empty(counts[rank])
    x = np.linspace(Lx[0] + h[0], Lx[1] - h[0], nx)

    if rank == 0:
        y = np.linspace(Ly[0] + h[1], Ly[1] - h[1], ny)
        comm.Scatterv([y, (counts, disps), mpi.DOUBLE], [yloc, mpi.DOUBLE], 0)
    else:
        comm.Scatterv(None, [yloc, mpi.DOUBLE], 0)

    print yloc
    x = x[np.newaxis, :]
    yloc = yloc[:, np.newaxis]

    
    return 100.*np.exp(-100.*((x - .5)**2 + (yloc - .5)**2))


def initSol(nx, ny, h, Lx=[0., 1.], Ly=[0., 1.]):
    """
    Initialisation d'une fonction pour tester le schéma en temps

    """
    X, Y = np.meshgrid(np.linspace(Lx[0] + h[0], Lx[1] - h[0], nx), 
                       np.linspace(Ly[0] + h[1], Ly[1] - h[1], ny))
    return 100.*np.exp(-100.*((X - .5)**2 + (Y - .5)**2))

nx, ny = 100, 100
h = [1./(nx + 1), 1./(ny + 1)]
u = initSolPara(nx, ny, h)

comm = mpi.COMM_WORLD
rank = comm.Get_rank()
if rank == 0:
    umono = initSol(nx, ny, h)

dt = np.min(h)**2/4.
print "dt =", dt
nite = 10

def laplacian2D_mpi(u, h):
    heat.update_fictitious_point(u)
    return heat.laplacian2D(u, h)

for i in xrange(nite):
    u[:, :] = heat.euler(u, -dt, laplacian2D_mpi, fargs=(h,))

    if rank == 0:
        umono[:, :] = heat.euler(umono, -dt, heat.laplacian2D, fargs=(h,))

s = u.shape
heat.update_fictitious_point(u)
# on vérifie que la solution mpi est la meme que sans mpi
if rank == 0:
    print (u == umono[:s[0],:s[1]]).all()
