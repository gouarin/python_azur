import vtk.util.numpy_support as vtknp
import vtk
import numpy as np

class VtkPlot:
    def __init__(self):
        self.grids = []
        self.actors = []
        self.display = []
        self.axis = False
        self.bounds = np.zeros(6)
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground(1.,1.,1.)
        self.cam = self.ren.GetActiveCamera()

    def setBounds(self):
        tmp = np.empty((6, self.display.count(True)))
        for i in xrange(len(self.display)):
            if self.display[i]:
                tmp[:, i] = self.grids[i].GetBounds()
        self.bounds[::2] = np.min(tmp, axis=1)[::2]
        self.bounds[1::2] = np.max(tmp, axis=1)[1::2]

    def setDisplay(self, index, cond):
        self.display[index] = cond

    def addGrid(self, grid):
        nx, ny, nz = grid.shape[1:]

        self.display.append(True)

        self.grids.append(vtk.vtkStructuredGrid())

        self.grids[-1].SetExtent(0, nz-1, 0, ny-1, 0, nx-1)
        p = vtk.vtkPoints()

        shp = grid.shape
        grid.shape = (3, nx*ny*nz)
        p.SetData(vtknp.numpy_to_vtk(np.ascontiguousarray(grid.T), deep=True, array_type=vtknp.get_vtk_array_type(grid.dtype)))
        grid.shape = shp
        self.grids[-1].SetPoints(p)

        #Couleur
        color = np.random.rand(3)
        #Create a vtkOutlineFilter to draw the bounding box of the data set.
        ol = vtk.vtkOutlineFilter()
        if (vtk.vtkVersion().GetVTKMajorVersion()>=6):
          ol.SetInputData(self.grids[-1])
        else:
          ol.SetInput(self.grids[-1])      
        olm = vtk.vtkPolyDataMapper()
        olm.SetInputConnection(ol.GetOutputPort())
        ola = vtk.vtkActor()
        ola.SetMapper(olm)
        ola.GetProperty().SetColor(color)

        s=vtk.vtkShrinkFilter()
        if (vtk.vtkVersion().GetVTKMajorVersion()>=6):
          s.SetInputData(self.grids[-1])
        else:
          s.SetInput(self.grids[-1])      
        s.SetShrinkFactor(0.8)
        #
        mapper = vtk.vtkDataSetMapper()
        #map.SetInputData(data)
        mapper.SetInputConnection(s.GetOutputPort())
        act = vtk.vtkLODActor()
        act.SetMapper(mapper)
        #act.GetProperty().SetRepresentationToWireframe()
        #act.GetProperty().SetRepresentationToPoints()	
        act.GetProperty().SetColor(color)
        act.GetProperty().SetEdgeColor(color)
        act.GetProperty().EdgeVisibilityOff()	
        self.actors.append(act)
        self.setBounds()
        self.ren.SetActiveCamera(self.cam)

    def moveCamera(self, Ox = 1.0, Oy = 0.0, Oz = 0.0):
        xmin, xmax, ymin, ymax, zmin, zmax = self.bounds[:]
        xc=0.5*(xmax+xmin)
        yc=0.5*(ymax+ymin)
        zc=0.5*(zmax+zmin)
        self.cam.SetFocalPoint(xc, yc, zc)
        if (Ox == 1.0):
            self.cam.SetViewUp(0.0, 0.0, 1.0)
            self.cam.SetPosition(xc+np.pi*(zmax-zmin),yc,zc)
        elif (Ox == -1.0):
            self.cam.SetViewUp(0.0, 0.0, 1.0)
            self.cam.SetPosition(xc-np.pi*(zmax-zmin),yc,zc)  
        if (Oy == 1.0):
            self.cam.SetViewUp(0.0, 0.0, 1.0)
            self.cam.SetPosition(xc,yc+np.pi*(zmax-zmin),zc)
        elif (Oy == -1.0):
            self.cam.SetViewUp(0.0, 0.0, 1.0)
            self.cam.SetPosition(xc,yc-np.pi*(zmax-zmin),zc)  
        if (Oz == 1.0):
            self.cam.SetViewUp(0.0, 1.0, 0.0)
            self.cam.SetPosition(xc,yc,zc+np.pi*(ymax-ymin))
        elif (Oz == -1.0):
            self.cam.SetViewUp(0.0, 1.0, 0.0)
            self.cam.SetPosition(xc,yc,zc-np.pi*(ymax-ymin))  

    def movePoint(self, gridIndex, pointIndex, x, y, z):
        self.actors[gridIndex].GetMapper().Update()
        print self.actors[gridIndex].GetMapper().GetInput().GetPoints()
        print self.actors[gridIndex].GetMapper().GetInput().GetPoints().GetPoint(pointIndex)
        self.actors[gridIndex].GetMapper().GetInput().GetPoints().SetPoint(pointIndex, x, y, z)


    def removeGrid(self, index):
        self.grids.pop(index)
        self.actors.pop(index)
        self.display.pop(index)

    def hideActor(self, index):
        self.display[index] = False

    def showActor(self, index):
        self.display[index] = True

    def redraw(self):
        self.ren.RemoveAllViewProps()
        for i in xrange(len(self.display)):
            if self.display[i]:
                self.ren.AddActor(self.actors[i])
        self.showAxis()
        self.moveCamera(0, 0, 1)
        self.ren.SetActiveCamera(self.cam)

    def showAxis(self):
        if self.axis:
            xmin, xmax, ymin, ymax, zmin, zmax = self.bounds[:]
            axes=vtk.vtkAxes()
            axes.SetOrigin(0.0,0.0,0.0)
            axes.SetScaleFactor(0.1*max([xmax-xmin,ymax-ymin,zmax-zmin]))
            axesTubes=vtk.vtkTubeFilter()
            axesTubes.SetInputConnection(axes.GetOutputPort())
            axesTubes.SetRadius(0.2)
            axesTubes.SetNumberOfSides(6)
            axesMapper=vtk.vtkPolyDataMapper() 
            axesMapper.SetInputConnection(axesTubes.GetOutputPort())
            axesActor=vtk.vtkActor() 
            axesActor.SetMapper(axesMapper)
            XText=vtk.vtkVectorText()    
            XText.SetText("X")
            XTextMapper=vtk.vtkPolyDataMapper() 
            XTextMapper.SetInputConnection(XText.GetOutputPort())
            XActor=vtk.vtkFollower()
            XActor.SetMapper(XTextMapper)
            XActor.SetScale(2.0, 2.0, 2.0)
            XActor.SetPosition(1.11*xmax, ymin, zmin)
            XActor.GetProperty().SetColor(0,0,0)
            XActor.SetCamera(self.cam)
            YText=vtk.vtkVectorText()    
            YText.SetText("Y")
            YTextMapper=vtk.vtkPolyDataMapper() 
            YTextMapper.SetInputConnection(YText.GetOutputPort())
            YActor=vtk.vtkFollower()
            YActor.SetMapper(YTextMapper)
            YActor.SetScale(2.0, 2.0, 2.0)
            YActor.SetPosition(xmin, 1.11*ymax, zmin)
            YActor.GetProperty().SetColor(0,0,0)
            YActor.SetCamera(self.cam)
            ZText=vtk.vtkVectorText()    
            ZText.SetText("Z")
            ZTextMapper=vtk.vtkPolyDataMapper() 
            ZTextMapper.SetInputConnection(ZText.GetOutputPort())
            ZActor=vtk.vtkFollower()
            ZActor.SetMapper(ZTextMapper)
            ZActor.SetScale(2.0, 2.0, 2.0)
            ZActor.SetPosition(xmin, ymin, 1.11*zmax)
            ZActor.GetProperty().SetColor(0,0,0)
            ZActor.SetCamera(self.cam)
            self.ren.AddActor(axesActor)
            self.ren.AddActor(XActor)
            self.ren.AddActor(YActor)
            self.ren.AddActor(ZActor)

    def show(self):
        fenetre = vtk.vtkRenderWindow()
        fenetre.AddRenderer(self.ren)
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(fenetre) 
        fenetre.SetPosition(50,50) 
        fenetre.SetSize(512,512)
        fenetre.SetWindowName("pyShift")
        iren.GetInteractorStyle().SetCurrentStyleToTrackballActor()
        iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()
        self.redraw()
        iren.Initialize()
        fenetre.Render()
        iren.Start()

if __name__ == "__main__":
    import pyShift.gengrid_stub as GGN

    wVtk = VtkPlot()
    case = 1 #2
    if case == 1:
        g = GGN.square(4)
        wVtk.addGrid(g)
        g = GGN.cube(4)
        wVtk.addGrid(g)
        g = GGN.rectangle(4, 50)
        wVtk.addGrid(g)
        wVtk.hideActor(0)
        wVtk.show()
        wVtk.showActor(0)
        wVtk.show()
        wVtk.hideActor(1)
        wVtk.hideActor(2)
        wVtk.movePoint(0, 0, 0., 2., 0.)
        wVtk.show()
    else:
        g = GGN.square(4)
        wVtk.addGrid(g)
        wVtk.movePoint(0, 0, 0., 2., 0.)
        wVtk.show()
        

