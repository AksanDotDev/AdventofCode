#include <stdio.h>
#include <stdlib.h>


char s[16];

char* runner(int);
int main(int argc, char** argv)
{
    int g;
    sscanf(argv[1], "%d", &g);
    printf("%s\n", runner(g));
    return 0;
}


char* runner(int g)
{
    int i, j, p, m, x, y;
    int a[300][300];
    int b[298][298];
    for(i = 0; i < 300; i++){
        for(j = 0; j < 300; j++){
            p = j + 11;
            p *= (i + 1);
            p += g;
            p *= (j + 11);
            p %= 1000;
            p -= (p % 100);
            p /= 100; 
            p -= 5;
            a[i][j] = p;
        }
    }
    
    for(i = 0; i < 298; i++){
        for(j = 0; j < 298; j++){
            b[i][j] = 0;
            b[i][j] += a[i][j];     
            b[i][j] += a[i+1][j];
            b[i][j] += a[i+2][j];
            b[i][j] += a[i][j+1];
            b[i][j] += a[i+1][j+1];
            b[i][j] += a[i+2][j+1];
            b[i][j] += a[i][j+2];
            b[i][j] += a[i+1][j+2];
            b[i][j] += a[i+2][j+2];
        }
    }
    m = 0;
    for(i = 0; i < 298; i++){
        for(j = 0; j < 298; j++){
            if (b[i][j] > m){
                m = b[i][j];
                x = j;
                y = i;
            }
        }
    }
    sprintf(s,"(%03d,%03d)", x + 1, y + 1);
    return s;
}







