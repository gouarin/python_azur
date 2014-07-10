from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy 

PATH_INCLUDES=[numpy.get_include()]
PATH_LIBRARIES=[]
LINK_LIBRARIES=[]

setup(name = "heat",
      ext_modules  = [Extension("heat.laplacianCy",
                                ["heat/laplacianCython.pyx"],
                                include_dirs = PATH_INCLUDES,
                                library_dirs = PATH_LIBRARIES,
                                libraries    = LINK_LIBRARIES,
                            ),
                      ],
      packages = ['heat'],
      cmdclass = {'build_ext': build_ext},
)
