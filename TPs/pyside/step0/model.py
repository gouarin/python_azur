import pyShift.gengrid_stub as GGN
import pyShift.cartTh as CTH

GGNMethod = ['square', 'rectangle', 'cube', 'parallelepiped', 'cartTh']

class ParamNotValid(Exception):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return repr(self.param)

class pyShiftModel(list):
    def __init__(self):
        super(pyShiftModel, self).__init__()

    def append(self, method, nx, ny=1, nz=1):
        self.checkParam(method, nx, ny, nz)
        if method == "square":
            super(pyShiftModel, self).append(GGN.square(nx))
        elif method == "rectangle":
            super(pyShiftModel, self).append(GGN.rectangle(nx, ny))
        elif method == "cube":
            super(pyShiftModel, self).append(GGN.cube(nx))
        elif method == "parallelepiped":
            super(pyShiftModel, self).append(GGN.parallelepiped(nx, ny, nz))
        elif method == "cartTh":
            super(pyShiftModel, self).append(CTH.cartThCythonMV2(nx, ny, nz))

    def checkParam(self, method, nx, ny, nz):
        if method not in GGNMethod:
            raise ParamNotValid(method)
        if nx <= 0:
            raise ParamNotValid("nx")
        if ny <= 0 and method in ["rectangle", "parallelepiped", "cartTh"]:
            raise ParamNotValid("ny")
        if nz <= 0 and method == ["parallelepiped", "cartTh"]:
            raise ParamNotValid("nz")

 
if __name__ == '__main__':
    m = pyShiftModel()
    
    meth = ['toto', 'square', 'square']
    n = [2, -2, 2]
    for i in xrange(len(n)):
        try:
            m.append(meth[i], n[i])
        except ParamNotValid, value:
            print "ParamNotValid: " + str(value)
    print m
    m.pop()
