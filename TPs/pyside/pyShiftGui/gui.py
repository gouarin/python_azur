import sys
from PySide import QtGui, QtCore, QtUiTools
import numpy as np
import vtk

from QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkPlot import VtkPlot
from model import pyShiftModel, ParamNotValid

class MeshWindow(QtGui.QDialog):
    check = QtCore.Signal(str)

    def __init__(self, parent = None):
        super(MeshWindow, self).__init__(parent)
        loader = QtUiTools.QUiLoader()
        loader.registerCustomWidget(QVTKRenderWindowInteractor)
        self.ui = loader.load("./forms/meshWindow.ui")

        self.ui.tabWidget.clear()

        self.model = pyShiftModel()
        self.vtkPlot = VtkPlot()

        # VTK window init
        self.vtk_ = self.ui.display
        self.vtk_.Initialize()
        self.vtk_.Start()
        self.vtk_.GetRenderWindow().AddRenderer(self.vtkPlot.ren)

        self.ui.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.check.connect(self.error)

    @QtCore.Slot(int)
    def closeTab(self, index):
        """
        This slot remove the tab of the given index.
        In the same time, the grid entry for the model
        and the vtkPlot are removed for this given index.
        
        index: the index to remove  
        
        """
        self.model.pop(index)
        self.vtkPlot.removeGrid(index)
        self.ui.tabWidget.removeTab(index)
        self.vtkPlot.redraw()
        self.vtk_.repaint()

    def createTableWidget(self):
        """
        Create the table view of the last inserted mesh.

        """
        size = np.prod(self.model[-1].shape[1:])
        self.uiTabMesh.tableWidget.setRowCount(size)
        self.uiTabMesh.tableWidget.setColumnCount(3)
        self.uiTabMesh.tableWidget.setHorizontalHeaderLabels(['x', 'y', 'z'])
        shape = self.model[-1].shape 
        self.model[-1].shape = (3, size)
        for i in xrange(size):
            for j in xrange(3):
                self.uiTabMesh.tableWidget.setItem(i, j, QtGui.QTableWidgetItem("%s"%self.model[-1][j, i]))
        self.model[-1].shape = shape
        self.uiTabMesh.tableWidget.resizeColumnsToContents()

    def show(self):
        """
        shows the MeshWindow widget
        """
        self.ui.show()

    def addMesh(self, method, nx, ny, nz):
        """
        adds a mesh in the MeshWindow.
        
        method: how to create the mesh (square, rectangle, ...)
        nx: number of points in x direction
        ny: number of points in x direction
        nz: number of points in x direction

        """
        try:
            self.model.append(method, nx, ny, nz)
            loader = QtUiTools.QUiLoader()
            self.uiTabMesh = loader.load("./forms/tabMesh.ui")
            self.ui.tabWidget.addTab(self.uiTabMesh, "%s(%d,%d,%d)"%(method, nx, ny, nz))
            self.createTableWidget()
            self.vtkPlot.addGrid(self.model[-1])
            self.vtkPlot.redraw()
            self.vtk_.repaint()

            index = self.ui.tabWidget.count() - 1
            self.ui.tabWidget.setCurrentIndex(index)
            self.ui.tabWidget.widget(index).checkBox.setCheckState(QtCore.Qt.Checked)
            self.ui.tabWidget.widget(index).checkBox.stateChanged.connect(self.display)
            self.ui.tabWidget.widget(index).tableWidget.cellChanged.connect(self.moveCoords)
        except ParamNotValid, value:
            self.check.emit(value.param)

    @QtCore.Slot(int)
    def display(self, value):
        """
        This slot is used to display or not a mesh when the checkbox
        in the tab view is checked or unchecked.

        """
        index = self.ui.tabWidget.currentIndex()

        if self.ui.tabWidget.widget(index).checkBox.checkState() == QtCore.Qt.Unchecked:
            self.vtkPlot.hideActor(index)
        else:
            self.vtkPlot.showActor(index)

        self.vtkPlot.redraw()
        self.vtk_.repaint()

    @QtCore.Slot(int, int)
    def moveCoords(self, row, column):
        index = self.ui.tabWidget.currentIndex()

        x = float(self.ui.tabWidget.widget(index).tableWidget.item(row, 0).text())
        y = float(self.ui.tabWidget.widget(index).tableWidget.item(row, 1).text())
        z = float(self.ui.tabWidget.widget(index).tableWidget.item(row, 2).text())

        self.vtkPlot.movePoint(index, row, x, y, z)
        print "move point ", index, row, x, y, z

        size = np.prod(self.model[index].shape[1:])
        shape = self.model[index].shape
        self.model[index].shape = (3, size)
        self.model[index][:, row] = [x, y, z]
        self.model[index].shape = shape
        self.vtkPlot.redraw()
        self.vtk_.repaint()

    @QtCore.Slot(str)
    def error(self, s):
        QtGui.QErrorMessage(self).showMessage("%s doit etre plus grand que 0"%s)
    
class MainDialog(QtGui.QWidget):
    def __init__(self, parent = None):
        super(MainDialog, self).__init__(parent)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load("./forms/dialog.ui")
        self.ui.finished.connect(self.exit)
        self.ui.btn.clicked.connect(self.addMesh)

        self.meshWindow = MeshWindow()
        self.meshWindow.show()

    @QtCore.Slot()
    def exit(self):
        sys.exit()

    def show(self):
        self.ui.show()

    @QtCore.Slot()
    def addMesh(self):
        nx = self.ui.nx.value()
        ny = self.ui.ny.value()
        nz = self.ui.nz.value()
        method = self.ui.comboBox.currentText()
        self.meshWindow.addMesh(method, nx, ny, nz)

    def keyPressEvent(self, event):
        print event.key()
        super(MainDialog, self).keyPressEvent(event)
        
if __name__ =="__main__":
    app = QtGui.QApplication(sys.argv)
    
    form = MainDialog()
    form.show()

    app.exec_()
