#include <stdio.h>
#include <stdlib.h>
#define BUFFERSIZE 524288


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
    int i, j, t, a; 
    short int c[BUFFERSIZE];
    c[0] = 3;
    c[1] = 7;
    i = 0;
    j = 1;
    t = 2;
    while ( t < g + 10 ){
        a = c[i] + c[j];
        if ( a >= 10 ){
            c[t++] = a / 10;
        }
        c[t++] = a % 10;
        i = (i + 1 + c[i]) % t;
        j = (j + 1 + c[j]) % t;
    }
    for ( i = g, j = 0; j < 10; i++, j++){
        s[j] = c[i] + 48;
    }
    s[j] = 0;
    return s;
}







