#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define BUFFERSIZE 4096

int runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%d\n", runner(f));
    fclose(f);
    return 0;
}


int runner(FILE* f)
{
    int n, i, j, g, l, w, r, m;
    int a[BUFFERSIZE][60];
    char e[BUFFERSIZE][64];
    char s[8];
    n = 0;
    while(!feof(f)){
        fgets(e[n++], 64, f);
    }
    qsort(e,n,64, strcmp);
    for(i = 0; i < BUFFERSIZE; i++){
        for(j = 0; j < 60; j++){
            a[i][j] = 0;
        }
    }
    for(i = 0; i < n; i++){
        r = sscanf(e[i], "[1518-%*d-%*d %*d:%d] %s #%d", &w, s, &g);
        if (r == 2 && s[0] == 'w'){
            for (j = l; j < w; j++){
                a[g][j]++;
            }
        } else if (r == 2) {
            l = w;
        }
    }
    m = 0;
    for(i = 0; i < BUFFERSIZE; i++){
        for(j = 0; j < 60; j++){
            if (a[i][j] > m){
                m = a[i][j];
                g = i;
                l = j;
            }
        }
    }
    r = g * l;
    return r;
}