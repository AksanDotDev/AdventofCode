#include <stdio.h>
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
    int c, i, j, x, y, v, h;
    int **a = malloc(BUFFERSIZE*sizeof(int*));
    char b[64];
    c = 0;
    for (i=0;i<BUFFERSIZE;i++){
        a[i] = calloc(BUFFERSIZE,sizeof(int));
    }
    while(!feof(f)){
        fgets(b, 64, f);
        sscanf(b,"#%*d @ %d,%d: %dx%d", &x, &y, &v, &h);
        for(i = x; i < (x+v); i++){
            for(j = y; j < (y+h); j++){
                a[i][j]++;
            }
        }
    }
    for(i = 0; i < BUFFERSIZE; i++){
        for(j = 0; j < BUFFERSIZE; j++){
            if (a[i][j] > 1){
                c++;
            }
        }
    }
    for (i=0;i<BUFFERSIZE;i++){
        free(a[i]);
    }
    free(a);
    return c;
}