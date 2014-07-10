#ifndef _CVOLUME_H_
#define _CVOLUME_H_

void fcomputeVolume( int ni, int nj, int nk, const float* mesh, float* vol);

void dcomputeVolume( int ni, int nj, int nk, const double* mesh, float* vol);

#endif
