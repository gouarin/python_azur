void gen3d_(int* i, int* j, int*k, float* x, float* y, float* z)
{
  int ix, jx, kx;
  int n;
  for (ix = 0; ix < *i; ++ix) {
    for (jx = 0; jx < *j; ++jx) {
      for (kx = 0; kx < *k; ++kx) {
	n = kx + jx*(*k) + ix*(*k)*(*j);
	x[n] = ix;
	y[n] = jx;
	z[n] = kx;
      }
    }
  }
}
