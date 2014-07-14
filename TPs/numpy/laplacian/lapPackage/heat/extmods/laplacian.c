#include <stdio.h>

void laplacian2DinC(int nx, int ny, double *h, double *x, double *y){
  int i, j;
  double cx = -1./(h[0]*h[0]);
  double cy = -1./(h[1]*h[1]);
  double c2 = -2.*(cx + cy);
  double som;

  for(j=0; j<ny; j++)
    for(i=0; i<nx; i++){
      som = c2*x[j*nx + i];
      if (i > 0)
	som += cx*x[j*nx + i - 1];
      if (i < nx-1)
	som += cx*x[j*nx + i + 1];
      if (j > 0)
	som += cy*x[(j - 1)*nx + i];
      if (j < ny-1)
	som += cy*x[(j + 1)*nx + i];
      y[j*nx + i] = som;
    }

}
