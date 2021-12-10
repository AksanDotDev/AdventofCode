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
    int i, j, k, d, p, m, c, x, y;
    int a[300][300];
    int b[300][300];
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
    m = 0;
    for(k = 0; k < 300; k++){
        for(i = 0; i < 300 - k; i++){
            for(j = 0; j < 300 - k; j++){
                if (k == 0){
                    b[i][j] = 0;
                }
                for(d = 0; d < k; d++){
                    b[i][j] += a[i+d][j+k];
                    b[i][j] += a[i+k][j+d];
                }
                b[i][j] += a[i+k][j+k];
            }
        }
        for(i = 0; i < 300 - k; i++){
            for(j = 0; j < 300 - k; j++){
                if (b[i][j] > m){
                    m = b[i][j];
                    x = j;
                    y = i;
                    c = k;
                }
            }
        }
    }
    sprintf(s,"(%03d,%03d,%03d)", x + 1, y + 1, c + 1);
    return s;
}







