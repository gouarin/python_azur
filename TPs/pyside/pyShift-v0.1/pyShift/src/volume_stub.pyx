"""Cython interface to C function volume

.. py:data:: E_ZERO_DIM

"""

import  numpy as PNPY
cimport numpy as CNPY

cdef extern from "CVolume.h":
   void fcomputeVolume( int ni, int nj, int nk, float* mesh, float* vol )
   void dcomputeVolume( int ni, int nj, int nk, double* mesh, float* vol )

def volume(CNPY.ndarray g):
    """Takes a Mesh as arg and return the volume of each cell of the mesh.
    Return is an array of size (nci,ncj,nck) where nci, ncj and nck are
    the number of cells per direction for the mesh.
    
    * Args
    
    - g : A mesh build by the pyShift grid generator
   
    * Return
    
    - a '''numpy''' array of size (nci,ncj,nck) with the volume of each cell

    * Exceptions

    - A message telling that this method is available only for 3D objects.
    """
    cdef CNPY.ndarray vol
    dims = g.shape
    if 1 == dims[3] :
        raise Exception, "Volume is available only for 3D objects !"
    vol = PNPY.empty((dims[1]-1,dims[2]-1,dims[3]-1), dtype=PNPY.float32)
    if g.descr.type_num == CNPY.NPY_DOUBLE:
        dcomputeVolume(<int>dims[1],<int>dims[2],<int>dims[3],<double*>g.data,<float*>vol.data)
    else:
        fcomputeVolume(<int>dims[1],<int>dims[2],<int>dims[3],<float*>g.data,<float*>vol.data)
    return vol
