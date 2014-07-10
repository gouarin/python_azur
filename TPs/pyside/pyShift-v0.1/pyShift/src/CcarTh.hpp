#ifndef CCARTH_HPP
#define CCARTH_HPP
#include <cmath>

template<typename K>
void generateCarTh(int ni, int nj, int nk, K* mesh)
{
  K* xc = new K[ni];
  K* yc = new K[nj];
  K* zc = new K[nk];

  K hx=2/K(ni-1), hy=2/K(nj-1), hz=2/K(nk-1);

  xc[0] = -1;
  for (int i = 1; i< ni; ++i) xc[i] = xc[i-1] + tanh(abs(-1+i*hx));

  zc[0] = -1;
  for (int i = 1; i< nk; ++i) zc[i] = zc[i-1] + tanh(abs(-1+i*hz));

  yc[0] = -1;
  for (int i = 1; i < nj; ++i) {
    K y = -1 + i*hy;
    yc[i] = yc[i-1] + y/(y*y + 1);
  }

  int indi, indj;
  int njnk = nj*nk;
  int stride = ni*nj*nk;
  K* mesh_x = mesh;
  K* mesh_y = mesh+stride;
  K* mesh_z = mesh+2*stride;
  indi = 0;
  for (int i = 0; i < ni; ++i) {
    indj = indi;
    for (int j = 0; j < nj; ++j) {
      for (int k = 0; k < nk; ++k) {
	mesh_x[indj+k] = xc[i];
	mesh_y[indj+k] = yc[j];
	mesh_z[indj+k] = zc[k];
      }
      indj += nk;
    }
    indi += njnk;
  }
  delete [] xc;
  delete [] yc;
  delete [] zc;
}

#endif
