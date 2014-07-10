#include <math.h>
#include <stdio.h>
#include "CVolume.h"

#define Mesh(l,i,j,k) mesh[(l*ni*nj*nk)+((i)+(j)*ni+(k)*ni*nj)]
void fcomputeVolume( int ni, int nj, int nk, const float* mesh, float* vol)
{
  int i,j,k;
  double bary[3], AB[3], AC[3], AD[3], AG[3];
  for (k = 0; k < nk-1; ++k) {
    for (j = 0; j < nj-1; ++j) {
      for (i = 0; i < ni-1; ++i) {
	double v;
	bary[0] = (Mesh(0,i,j,k)+Mesh(0,i+1,j,k)+Mesh(0,i+1,j+1,k)+Mesh(0,i,j+1,k)+
		   Mesh(0,i,j,k+1)+Mesh(0,i+1,j,k+1)+Mesh(0,i+1,j+1,k+1)+Mesh(0,i,j+1,k+1))
	  *0.125;
	bary[1] = (Mesh(1,i,j,k)+Mesh(1,i+1,j,k)+Mesh(1,i+1,j+1,k)+Mesh(1,i,j+1,k)+
		   Mesh(1,i,j,k+1)+Mesh(1,i+1,j,k+1)+Mesh(1,i+1,j+1,k+1)+Mesh(1,i,j+1,k+1))
	  *0.125;
	bary[2] = (Mesh(2,i,j,k)+Mesh(2,i+1,j,k)+Mesh(2,i+1,j+1,k)+Mesh(2,i,j+1,k)+
		   Mesh(2,i,j,k+1)+Mesh(2,i+1,j,k+1)+Mesh(2,i+1,j+1,k+1)+Mesh(2,i,j+1,k+1))
	  *0.125;
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j  ,k  ) - Mesh(0,i  ,j  ,k  );
	AB[1] = Mesh(1,i+1,j  ,k  ) - Mesh(1,i  ,j  ,k  );
	AB[2] = Mesh(2,i+1,j  ,k  ) - Mesh(2,i  ,j  ,k  );

	AC[0] = Mesh(0,i+1,j+1,k  ) - Mesh(0,i  ,j  ,k  );
	AC[1] = Mesh(1,i+1,j+1,k  ) - Mesh(1,i  ,j  ,k  );
	AC[2] = Mesh(2,i+1,j+1,k  ) - Mesh(2,i  ,j  ,k  );

	AD[0] = Mesh(0,i  ,j+1,k  ) - Mesh(0,i  ,j  ,k  );
	AD[1] = Mesh(1,i  ,j+1,k  ) - Mesh(1,i  ,j  ,k  );
	AD[2] = Mesh(2,i  ,j+1,k  ) - Mesh(2,i  ,j  ,k  );

	AG[0] = bary[0] - Mesh(0,i  ,j  ,k  );
	AG[1] = bary[1] - Mesh(1,i  ,j  ,k  );
	AG[2] = bary[2] - Mesh(2,i  ,j  ,k  );

	v  = fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i  ,j+1,k  ) - Mesh(0,i  ,j  ,k  );
	AB[1] = Mesh(1,i  ,j+1,k  ) - Mesh(1,i  ,j  ,k  );
	AB[2] = Mesh(2,i  ,j+1,k  ) - Mesh(2,i  ,j  ,k  );

	AC[0] = Mesh(0,i  ,j+1,k+1) - Mesh(0,i  ,j  ,k  );
	AC[1] = Mesh(1,i  ,j+1,k+1) - Mesh(1,i  ,j  ,k  );
	AC[2] = Mesh(2,i  ,j+1,k+1) - Mesh(2,i  ,j  ,k  );

	AD[0] = Mesh(0,i  ,j  ,k+1) - Mesh(0,i  ,j  ,k  );
	AD[1] = Mesh(1,i  ,j  ,k+1) - Mesh(1,i  ,j  ,k  );
	AD[2] = Mesh(2,i  ,j  ,k+1) - Mesh(2,i  ,j  ,k  );

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j  ,k  ) - Mesh(0,i  ,j  ,k  );
	AB[1] = Mesh(1,i+1,j  ,k  ) - Mesh(1,i  ,j  ,k  );
	AB[2] = Mesh(2,i+1,j  ,k  ) - Mesh(2,i  ,j  ,k  );

	AC[0] = Mesh(0,i+1,j  ,k+1) - Mesh(0,i  ,j  ,k  );
	AC[1] = Mesh(1,i+1,j  ,k+1) - Mesh(1,i  ,j  ,k  );
	AC[2] = Mesh(2,i+1,j  ,k+1) - Mesh(2,i  ,j  ,k  );

	AD[0] = Mesh(0,i  ,j  ,k+1) - Mesh(0,i  ,j  ,k  );
	AD[1] = Mesh(1,i  ,j  ,k+1) - Mesh(1,i  ,j  ,k  );
	AD[2] = Mesh(2,i  ,j  ,k+1) - Mesh(2,i  ,j  ,k  );

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j  ,k+1) - Mesh(0,i+1,j+1,k+1);
	AB[1] = Mesh(1,i+1,j  ,k+1) - Mesh(1,i+1,j+1,k+1);
	AB[2] = Mesh(2,i+1,j  ,k+1) - Mesh(2,i+1,j+1,k+1);

	AC[0] = Mesh(0,i  ,j  ,k+1) - Mesh(0,i+1,j+1,k+1);
	AC[1] = Mesh(1,i  ,j  ,k+1) - Mesh(1,i+1,j+1,k+1);
	AC[2] = Mesh(2,i  ,j  ,k+1) - Mesh(2,i+1,j+1,k+1);

	AD[0] = Mesh(0,i  ,j+1,k+1) - Mesh(0,i+1,j+1,k+1);
	AD[1] = Mesh(1,i  ,j+1,k+1) - Mesh(1,i+1,j+1,k+1);
	AD[2] = Mesh(2,i  ,j+1,k+1) - Mesh(2,i+1,j+1,k+1);

	AG[0] = bary[0] - Mesh(0,i+1,j+1,k+1);
	AG[1] = bary[1] - Mesh(1,i+1,j+1,k+1);
	AG[2] = bary[2] - Mesh(2,i+1,j+1,k+1);

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j+1,k  ) - Mesh(0,i+1,j+1,k+1);
	AB[1] = Mesh(1,i+1,j+1,k  ) - Mesh(1,i+1,j+1,k+1);
	AB[2] = Mesh(2,i+1,j+1,k  ) - Mesh(2,i+1,j+1,k+1);

	AC[0] = Mesh(0,i+1,j  ,k  ) - Mesh(0,i+1,j+1,k+1);
	AC[1] = Mesh(1,i+1,j  ,k  ) - Mesh(1,i+1,j+1,k+1);
	AC[2] = Mesh(2,i+1,j  ,k  ) - Mesh(2,i+1,j+1,k+1);

	AD[0] = Mesh(0,i+1,j+1,k+1) - Mesh(0,i+1,j+1,k+1);
	AD[1] = Mesh(1,i+1,j  ,k+1) - Mesh(1,i+1,j+1,k+1);
	AD[2] = Mesh(2,i+1,j  ,k+1) - Mesh(2,i+1,j+1,k+1);

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j+1,k  ) - Mesh(0,i+1,j+1,k+1);
	AB[1] = Mesh(1,i+1,j+1,k  ) - Mesh(1,i+1,j+1,k+1);
	AB[2] = Mesh(2,i+1,j+1,k  ) - Mesh(2,i+1,j+1,k+1);

	AC[0] = Mesh(0,i  ,j+1,k  ) - Mesh(0,i+1,j+1,k+1);
	AC[1] = Mesh(1,i  ,j+1,k  ) - Mesh(1,i+1,j+1,k+1);
	AC[2] = Mesh(2,i  ,j+1,k  ) - Mesh(2,i+1,j+1,k+1);

	AD[0] = Mesh(0,i  ,j+1,k+1) - Mesh(0,i+1,j+1,k+1);
	AD[1] = Mesh(1,i  ,j+1,k+1) - Mesh(1,i+1,j+1,k+1);
	AD[2] = Mesh(2,i  ,j+1,k+1) - Mesh(2,i+1,j+1,k+1);

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	vol[i+j*(ni-1)+k*(ni-1)*(nj-1)] = (float)(v/6.);
      }// End for (i
    }// End for (j
  }// End for (k
}

void dcomputeVolume( int ni, int nj, int nk, const double* mesh, float* vol)
{
  int i,j,k;
  double bary[3], AB[3], AC[3], AD[3], AG[3];
  for (k = 0; k < nk-1; ++k) {
    for (j = 0; j < nj-1; ++j) {
      for (i = 0; i < ni-1; ++i) {
	double v;
	bary[0] = (Mesh(0,i,j,k)+Mesh(0,i+1,j,k)+Mesh(0,i+1,j+1,k)+Mesh(0,i,j+1,k)+
		   Mesh(0,i,j,k+1)+Mesh(0,i+1,j,k+1)+Mesh(0,i+1,j+1,k+1)+Mesh(0,i,j+1,k+1))
	  *0.125;
	bary[1] = (Mesh(1,i,j,k)+Mesh(1,i+1,j,k)+Mesh(1,i+1,j+1,k)+Mesh(1,i,j+1,k)+
		   Mesh(1,i,j,k+1)+Mesh(1,i+1,j,k+1)+Mesh(1,i+1,j+1,k+1)+Mesh(1,i,j+1,k+1))
	  *0.125;
	bary[2] = (Mesh(2,i,j,k)+Mesh(2,i+1,j,k)+Mesh(2,i+1,j+1,k)+Mesh(2,i,j+1,k)+
		   Mesh(2,i,j,k+1)+Mesh(2,i+1,j,k+1)+Mesh(2,i+1,j+1,k+1)+Mesh(2,i,j+1,k+1))
	  *0.125;
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j  ,k  ) - Mesh(0,i  ,j  ,k  );
	AB[1] = Mesh(1,i+1,j  ,k  ) - Mesh(1,i  ,j  ,k  );
	AB[2] = Mesh(2,i+1,j  ,k  ) - Mesh(2,i  ,j  ,k  );

	AC[0] = Mesh(0,i+1,j+1,k  ) - Mesh(0,i  ,j  ,k  );
	AC[1] = Mesh(1,i+1,j+1,k  ) - Mesh(1,i  ,j  ,k  );
	AC[2] = Mesh(2,i+1,j+1,k  ) - Mesh(2,i  ,j  ,k  );

	AD[0] = Mesh(0,i  ,j+1,k  ) - Mesh(0,i  ,j  ,k  );
	AD[1] = Mesh(1,i  ,j+1,k  ) - Mesh(1,i  ,j  ,k  );
	AD[2] = Mesh(2,i  ,j+1,k  ) - Mesh(2,i  ,j  ,k  );

	AG[0] = bary[0] - Mesh(0,i  ,j  ,k  );
	AG[1] = bary[1] - Mesh(1,i  ,j  ,k  );
	AG[2] = bary[2] - Mesh(2,i  ,j  ,k  );

	v  = fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i  ,j+1,k  ) - Mesh(0,i  ,j  ,k  );
	AB[1] = Mesh(1,i  ,j+1,k  ) - Mesh(1,i  ,j  ,k  );
	AB[2] = Mesh(2,i  ,j+1,k  ) - Mesh(2,i  ,j  ,k  );

	AC[0] = Mesh(0,i  ,j+1,k+1) - Mesh(0,i  ,j  ,k  );
	AC[1] = Mesh(1,i  ,j+1,k+1) - Mesh(1,i  ,j  ,k  );
	AC[2] = Mesh(2,i  ,j+1,k+1) - Mesh(2,i  ,j  ,k  );

	AD[0] = Mesh(0,i  ,j  ,k+1) - Mesh(0,i  ,j  ,k  );
	AD[1] = Mesh(1,i  ,j  ,k+1) - Mesh(1,i  ,j  ,k  );
	AD[2] = Mesh(2,i  ,j  ,k+1) - Mesh(2,i  ,j  ,k  );

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j  ,k  ) - Mesh(0,i  ,j  ,k  );
	AB[1] = Mesh(1,i+1,j  ,k  ) - Mesh(1,i  ,j  ,k  );
	AB[2] = Mesh(2,i+1,j  ,k  ) - Mesh(2,i  ,j  ,k  );

	AC[0] = Mesh(0,i+1,j  ,k+1) - Mesh(0,i  ,j  ,k  );
	AC[1] = Mesh(1,i+1,j  ,k+1) - Mesh(1,i  ,j  ,k  );
	AC[2] = Mesh(2,i+1,j  ,k+1) - Mesh(2,i  ,j  ,k  );

	AD[0] = Mesh(0,i  ,j  ,k+1) - Mesh(0,i  ,j  ,k  );
	AD[1] = Mesh(1,i  ,j  ,k+1) - Mesh(1,i  ,j  ,k  );
	AD[2] = Mesh(2,i  ,j  ,k+1) - Mesh(2,i  ,j  ,k  );

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j  ,k+1) - Mesh(0,i+1,j+1,k+1);
	AB[1] = Mesh(1,i+1,j  ,k+1) - Mesh(1,i+1,j+1,k+1);
	AB[2] = Mesh(2,i+1,j  ,k+1) - Mesh(2,i+1,j+1,k+1);

	AC[0] = Mesh(0,i  ,j  ,k+1) - Mesh(0,i+1,j+1,k+1);
	AC[1] = Mesh(1,i  ,j  ,k+1) - Mesh(1,i+1,j+1,k+1);
	AC[2] = Mesh(2,i  ,j  ,k+1) - Mesh(2,i+1,j+1,k+1);

	AD[0] = Mesh(0,i  ,j+1,k+1) - Mesh(0,i+1,j+1,k+1);
	AD[1] = Mesh(1,i  ,j+1,k+1) - Mesh(1,i+1,j+1,k+1);
	AD[2] = Mesh(2,i  ,j+1,k+1) - Mesh(2,i+1,j+1,k+1);

	AG[0] = bary[0] - Mesh(0,i+1,j+1,k+1);
	AG[1] = bary[1] - Mesh(1,i+1,j+1,k+1);
	AG[2] = bary[2] - Mesh(2,i+1,j+1,k+1);

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j+1,k  ) - Mesh(0,i+1,j+1,k+1);
	AB[1] = Mesh(1,i+1,j+1,k  ) - Mesh(1,i+1,j+1,k+1);
	AB[2] = Mesh(2,i+1,j+1,k  ) - Mesh(2,i+1,j+1,k+1);

	AC[0] = Mesh(0,i+1,j  ,k  ) - Mesh(0,i+1,j+1,k+1);
	AC[1] = Mesh(1,i+1,j  ,k  ) - Mesh(1,i+1,j+1,k+1);
	AC[2] = Mesh(2,i+1,j  ,k  ) - Mesh(2,i+1,j+1,k+1);

	AD[0] = Mesh(0,i+1,j+1,k+1) - Mesh(0,i+1,j+1,k+1);
	AD[1] = Mesh(1,i+1,j  ,k+1) - Mesh(1,i+1,j+1,k+1);
	AD[2] = Mesh(2,i+1,j  ,k+1) - Mesh(2,i+1,j+1,k+1);

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	AB[0] = Mesh(0,i+1,j+1,k  ) - Mesh(0,i+1,j+1,k+1);
	AB[1] = Mesh(1,i+1,j+1,k  ) - Mesh(1,i+1,j+1,k+1);
	AB[2] = Mesh(2,i+1,j+1,k  ) - Mesh(2,i+1,j+1,k+1);

	AC[0] = Mesh(0,i  ,j+1,k  ) - Mesh(0,i+1,j+1,k+1);
	AC[1] = Mesh(1,i  ,j+1,k  ) - Mesh(1,i+1,j+1,k+1);
	AC[2] = Mesh(2,i  ,j+1,k  ) - Mesh(2,i+1,j+1,k+1);

	AD[0] = Mesh(0,i  ,j+1,k+1) - Mesh(0,i+1,j+1,k+1);
	AD[1] = Mesh(1,i  ,j+1,k+1) - Mesh(1,i+1,j+1,k+1);
	AD[2] = Mesh(2,i  ,j+1,k+1) - Mesh(2,i+1,j+1,k+1);

	v += fabs(AB[0]*AC[1]*AG[2]+AB[1]*AC[2]*AG[0]+AB[2]*AC[0]*AG[1]-
		  AG[0]*AC[1]*AB[2]-AG[1]*AC[2]*AB[0]-AG[2]*AC[0]*AB[1]);
	v += fabs(AC[0]*AD[1]*AG[2]+AC[1]*AD[2]*AG[0]+AC[2]*AD[0]*AG[1]-
		  AG[0]*AD[1]*AC[2]-AG[1]*AD[2]*AC[0]-AG[2]*AD[0]*AC[1]);
	/************************************************************************/
	vol[i+j*(ni-1)+k*(ni-1)*(nj-1)] = (float)(v/6.);
      }// End for (i
    }// End for (j
  }// End for (k
}
