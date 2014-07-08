import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import vtk
from vtk.util import numpy_support

def plotWithMatplotlib(u):
    n = u.shape
    if u.ndim == 1: 
        plt.plot(u)
    if u.ndim == 2:
        plt.imshow(u)
        plt.colorbar()
    if u.ndim == 3:
        G = gridspec.GridSpec(2, 3)

        plt.subplot(G[:, :2])
        plt.imshow(u[:, :, n[0]/2])
        plt.title("plan de coupe en x")
        plt.colorbar()

        plt.subplot(G[0, 2])
        plt.title("plan de coupe en y")
        plt.imshow(u[:, n[1]/2, :])
        plt.colorbar()

        plt.subplot(G[1, 2])
        plt.imshow(u[n[2]/2, :, :])
        plt.title("plan de coupe en z")
        plt.colorbar()

    plt.show()

def plotWithVTK(n, x, u):
    # Stockage des donnees au format VTK
    pts = vtk.vtkPoints()
    pts.SetData(numpy_support.numpy_to_vtk(x))

    uvtk = numpy_support.numpy_to_vtk(u)
    uvtk.SetName("u")

    data = vtk.vtkStructuredGrid()
    nn = n + [1]*(3 - len(n))
    data.SetDimensions(nn)
    data.SetPoints(pts)
    data.GetPointData().SetScalars(uvtk)
    data.Update()

    # Sortie fichier
    w = vtk.vtkXMLStructuredGridWriter()
    w.SetFileName("poisson.vts")
    w.SetInput(data)
    w.Write()
