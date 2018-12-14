#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define BUFFERSIZE 134217728


int runner(char*);
int main(int argc, char** argv)
{
    int g;
    printf("%d\n", runner(argv[1]));
    return 0;
}


int runner(char * e)
{
    int i, j, k, t, n, a; 
    short int * c = malloc(BUFFERSIZE * sizeof(short int));
    n = strlen(e);
    c[0] = 3;
    c[1] = 7;
    i = 0;
    j = 1;
    t = 2;
    while (t < BUFFERSIZE - 2){
        a = c[i] + c[j];
        if ( a >= 10 ){
            c[t++] = a / 10;
            for( k = 0; k <= n && t > n; k++){
                if (c[t-n+k] + 48 != e[k]){
                    break;
                }
            }
            if (k == n){
                break;
            }
        }
        c[t++] = a % 10;
        for( k = 0; k <= n && t > n; k++){
            if (c[t-n+k] + 48 != e[k]){
                break;
            }
        }
        if (k == n){
            break;
        }
        i = (i + 1 + c[i]) % t;
        j = (j + 1 + c[j]) % t;
    }
    free(c);
    return t - n;
}







