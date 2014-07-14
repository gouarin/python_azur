import mpi4py.MPI as mpi

def update_fictitious_point(x):
    comm = mpi.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    down, up = rank - 1, rank + 1
    
    if down < 0:
        down = -1
    if up >= size:
        up = -1

    comm.Sendrecv([x[1, :], mpi.DOUBLE], down, 0,
                  [x[0, :], mpi.DOUBLE], down, 0)
    comm.Sendrecv([x[-2, :], mpi.DOUBLE], up, 0,
                  [x[-1, :], mpi.DOUBLE], up, 0)
