# ----------------------------------------------------------------------------
# pyShift - Cartesian Mesh Rigid Motion
#         - see file license.txt
#
import re,os,sys
from distutils.core import setup,Extension
from distutils.command.clean import clean as _clean
from distutils.dir_util import remove_tree

try:
  from Cython.Distutils import build_ext
except:
  raise 'Cannot build pyShift without cython'
  sys.exit()

try:
  import numpy
except:
  raise 'Cannot build pyShift without numpy'
  sys.exit()

# --------------------------------------------------------------------
# Clean target redefinition - force clean everything
relist=['^.*~$','^core\.*$','^#.*#$','^.*\.aux$','^.*\.pyc$','^.*\.o$']
reclean=[]

for restring in relist:
  reclean.append(re.compile(restring))

def wselect(args,dirname,names):
  for n in names:
    for rev in reclean:
      if (rev.match(n)):
        os.remove("%s/%s"%(dirname,n))
        break

class clean(_clean):
  def walkAndClean(self):
    os.path.walk("..",wselect,[])
  def run(self):
    if (os.path.exists('./build')): remove_tree('./build')
    self.walkAndClean()

PATH_INCLUDES=[numpy.get_include()]
PATH_LIBRARIES=['build']
LINK_LIBRARIES=[]

setup(
name         = "pyShift",
version      = "0.1",
description  = "Rigid Motion for 2D grids",
author       = "ONERA/DSNA/CS2A Marc Poinot",
author_email = "marc.poinot@onera.fr",
packages     = ['pyShift','pyShift.test'],
ext_modules  = [Extension("pyShift.gengrid_stub",
                          ["pyShift/src/gengrid_stub.pyx",
                           "pyShift/src/gengrid.c",
                           "pyShift/src/gen3d.c"],
                          include_dirs = PATH_INCLUDES,
                          library_dirs = PATH_LIBRARIES,
                          libraries    = LINK_LIBRARIES,
                          ),
                Extension("pyShift.cartThCy",
                          ["pyShift/src/cartTh.pyx",],
                          include_dirs = PATH_INCLUDES,
                          library_dirs = PATH_LIBRARIES,
                          libraries    = LINK_LIBRARIES,
                          ),
                Extension("pyShift.cartThCpp",
                          ["pyShift/src/cartTh_stub.cpp",],
                          include_dirs = PATH_INCLUDES,
                          library_dirs = PATH_LIBRARIES,
                          libraries    = LINK_LIBRARIES,
                          ),
                Extension("pyShift.cyVolume",
                          ["pyShift/src/volume_stub.pyx",
                           "pyShift/src/CVolume.c"],
                          include_dirs = PATH_INCLUDES,
                          library_dirs = PATH_LIBRARIES,
                          libraries    = LINK_LIBRARIES,
                          )],
cmdclass     = {'build_ext':build_ext,'clean':clean},
)
