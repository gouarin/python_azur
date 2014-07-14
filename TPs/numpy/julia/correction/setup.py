from distutils.core import setup, Extension
from Cython.Distutils import build_ext

PATH_INCLUDES=[]
PATH_LIBRARIES=[]
LINK_LIBRARIES=[]

julia_ext = Extension("juliaCython", 
                      ["juliaCython.pyx"],
                      include_dirs = PATH_INCLUDES,
                      library_dirs = PATH_LIBRARIES,
                      libraries    = LINK_LIBRARIES,
                      extra_compile_args=['-fopenmp'],
                      extra_link_args=['-fopenmp'],
                  )

setup(name="juliaCython",
      ext_modules = [julia_ext],
      cmdclass = {'build_ext': build_ext},
)
