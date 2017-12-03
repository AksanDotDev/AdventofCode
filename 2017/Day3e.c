#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(int argc, char** argv)
{
    int a[255][255];
    int i, j, b, c, r, s, l, d, k;
    l = strtol(argv[1], NULL, 10);
    for (i=0;i<255;i++)
        for (j=0;j<255;j++)
            a[i][j] = 0;
    i = j = 127;
    a[i][j] = 1;
    r = d = 1;
    k = 2;
    s = 0;
    i++;
    while (s < l)
    {
        s = 0;
        for(b=-1;b<2;b++)
            for (c=-1;c<2;c++)
                s+=a[i+b][j+c];
        a[i][j] = s;
        r--;
        if (r == 0)
        {
            k++;
            r = k/2;
            d--;
            if (d == -1)
                d = 3;
        }
        switch (d)
        {
            case 0 :
                j--;
                break;
            case 1 :
                i++;
                break;
            case 2 :
                j++;
                break;
            case 3 :
                i--;
                break;
            default :
                printf("help...");
                break;
        }
        printf("%d\n", s);
    }
    printf("%d\n", s);
    return 0;
}