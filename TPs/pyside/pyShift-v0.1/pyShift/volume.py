# ------------------------------------------------------------------------
# pyShift - Compute the volume of each cells of a structured mesh
#         - see file license.txt
#
import math
import numpy

def volume(g):
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
   dims = g.shape
   if 1 == dims[3] :
       raise Exception, "Volume is available only for 3D objects !"
   vol = numpy.empty((dims[1]-1,dims[2]-1,dims[3]-1), dtype=numpy.float32)
   for k in xrange(dims[3]-1):
       for j in xrange(dims[2]-1):
           for i in xrange(dims[1]-1):
               # Compute barycenter of the hexahedra :
               bary = (g[:,i,j,k]+g[:,i+1,j,k]+g[:,i+1,j+1,k]+g[:,i,j+1,k]+
                       g[:,i,j,k+1]+g[:,i+1,j,k+1]+g[:,i+1,j+1,k+1]+g[:,i,j+1,k+1])*0.125
               # ----------------------------------------------
               # For each face (A,B,C,D) of the hexahedra :
               #
               # Splitting the face as two triangles and create two tetraedra
               # (A,B,C,G) and (A,C,D,G) where G is the barycenter of the cell
               #
               # Volume of a tetraedra : V = 1/6|det(AB,AC,AG)|
               # ----------------------
               #
               # First face :
               #============
               # Compute vectors
               #
               AB = g[:,i+1,j  ,k]-g[:,i,j,k]
               AC = g[:,i+1,j+1,k]-g[:,i,j,k]
               AD = g[:,i  ,j+1,k]-g[:,i,j,k]
               AG = bary[:] - g[:,i,j,k]
               # Compute 6 x volume of the both tetrahedra
               v1  = abs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
                         AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1])
               v1 += abs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
                         AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1])
               # Second face :
               #============
               # Compute vectors
               #
               AB = g[:,i,j+1,k  ]-g[:,i,j,k]
               AC = g[:,i,j+1,k+1]-g[:,i,j,k]
               AD = g[:,i,j  ,k+1]-g[:,i,j,k]
               #AG = bary[:] - g[:,i,j,k]
               # Compute 6 x volume of the both tetrahedra
               v1 += abs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
                         AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1])
               v1 += abs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]
                         -AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1])
               # Third face :
               #============
               # Compute vectors
               #
               AB = g[:,i+1,j,k  ]-g[:,i,j,k]
               AC = g[:,i+1,j,k+1]-g[:,i,j,k]
               AD = g[:,i  ,j,k+1]-g[:,i,j,k]
               #AG = bary[:] - g[:,i,j,k]
               # Compute 6 x volume of the both tetrahedra
               v1 += abs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
                         AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1])
               v1 += abs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
                         AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1])
               # Fourth face :
               #============
               # Compute vectors
               #
               AB = g[:,i+1,j  ,k+1]- g[:,i+1,j+1,k+1]
               AC = g[:,i  ,j  ,k+1]- g[:,i+1,j+1,k+1]
               AD = g[:,i  ,j+1,k+1]- g[:,i+1,j+1,k+1]
               AG = bary[:]         - g[:,i+1,j+1,k+1]
               # Compute 6 x volume of the both tetrahedra
               v1 += abs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
                         AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1])
               v1 += abs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
                         AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1])
               # Fifth face :
               #============
               # Compute vectors
               #
               AB = g[:,i+1,j+1,k  ]- g[:,i+1,j+1,k+1]
               AC = g[:,i+1,j  ,k  ]- g[:,i+1,j+1,k+1]
               AD = g[:,i+1,j  ,k+1]- g[:,i+1,j+1,k+1]
               #AG = bary[:]         - g[:,i+1,j+1,k+1]
               # Compute 6 x volume of the both tetrahedra
               v1 += abs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
                         AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1])
               v1 += abs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
                         AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1])
               # Sixth face :
               #============
               # Compute vectors
               #
               AB = g[:,i+1,j+1,k  ]- g[:,i+1,j+1,k+1]
               AC = g[:,i  ,j+1,k  ]- g[:,i+1,j+1,k+1]
               AD = g[:,i  ,j+1,k+1]- g[:,i+1,j+1,k+1]
               #AG = bary[:]         - g[:,i+1,j+1,k+1]
               # Compute 6 x volume of the both tetrahedra
               v1 += abs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
                         AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1])
               v1 += abs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
                         AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1])
               
               vol[i,j,k] = v1/6.
   return vol
