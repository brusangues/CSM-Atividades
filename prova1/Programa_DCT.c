#include	<stdio.h>
#include	<math.h>
#define	PI	3.1415926535897
#define	w	2
#define	h	2

int	main(void)
{
int	x,y,u,v;

float	in[h][w]=	{{10.4,12.4},
                     {14.9,20.4},};
float	out[h][w],sum,Cu,Cv;

	for (u=0;u<w;u++)
	{
		for (v=0;v<h;v++)
		{
			sum=0;
			for (x=0;x<w;x++)
				for (y=0;y<h;y++)
				{
					sum=sum+in[x][y]*cos(((2.0*x+1)*u*PI)/16.0)*
						cos(((2.0*y+1)*v*PI)/16.0);
				}
			if (u==0) Cu=1/sqrt(2); else Cu=1;
			if (v==0) Cv=1/sqrt(2); else Cv=1;

			out[u][v]=1/4.0*Cu*Cv*sum;
			printf("%8.2f ",out[u][v]);
		}
		printf("\n");
	}
	printf("\n");
	return(0);
}
