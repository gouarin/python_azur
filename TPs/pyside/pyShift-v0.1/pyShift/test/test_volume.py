# ----------------------------------------------------------------------------
# pyShift - Cartesian Mesh Volume computation
#         - see file license.txt
#
import pyShift.gengrid_stub as GGN
import pyShift.motion as MTN
import pyShift.volume as PSV
import pyShift.cyVolume as CSV
import math
import numpy
import copy
import time

def test_vol():
  """Test mesh generation"""
  n = 30
  trueVol = numpy.ones((n-1,n-1,n-1),dtype=numpy.float32)
  g  = GGN.cube(n)
  v  = PSV.volume(g)
  numpy.testing.assert_allclose(v, trueVol, rtol=1.e-6)
  alpha=45*(math.pi/180.)
  p0=(0.0,0.0,0.0)
  p1=(0.0,1.0,0.0)
  trans=(0.0,0.0,0.0)
  g1 = MTN.shift(g, p0,p1,alpha,trans)
  v1 = PSV.volume(g1)
  numpy.testing.assert_allclose(v1, trueVol, rtol=1.e-6)
  t1 = time.time()
  v2  = CSV.volume(g)
  t2 = time.time()
  totTime = t2-t1
  numpy.testing.assert_allclose(v2, trueVol, rtol=1.e-6)
  t1 = time.time()
  v3  = CSV.volume(g1)
  t2 = time.time()
  totTime += t2-t1
  numpy.testing.assert_allclose(v3, trueVol, rtol=1.e-6)
  print "Temps total version C-Cython : ", totTime

test_vol()
