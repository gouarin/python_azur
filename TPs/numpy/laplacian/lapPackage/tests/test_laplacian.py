from heat.laplacian import laplacian2D
import numpy as np

def test_laplacian():
    nx, ny = 100, 100
    u = np.ones((ny, nx))
    lap = laplacian2D(u, [1, 1])

    sol = np.ones((ny, nx))
    sol[1:-1, 1: -1] = 0
    sol[0, 0] = sol[0, -1] = 2
    sol[-1, -1] = sol[-1, 0] = 2
    
    np.testing.assert_array_equal(lap, sol)
