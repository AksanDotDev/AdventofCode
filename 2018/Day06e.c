#include <stdio.h>
#include <stdlib.h>
#define BUFFERSIZE 512

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
    int x, y, i, s, n;
    int **a = malloc(BUFFERSIZE*sizeof(int*));
    int c[64][2];
    char b[32];
    for (i = 0;i < BUFFERSIZE; i++){
        a[i] = calloc(BUFFERSIZE,sizeof(int));
    }
    n = 0;
    while(!feof(f)){
        fgets(b, 32, f);
        sscanf(b, "%d, %d", &x, &y);
        c[n][0] = x + (BUFFERSIZE/8);
        c[n++][1] = y + (BUFFERSIZE/8);
    }
    for(x = 0; x < BUFFERSIZE; x++){
        for(y = 0; y < BUFFERSIZE; y++){
            for(i = 0; i < n; i++){
                a[x][y] += abs(x - c[i][0]) + abs(y - c[i][1]);
            }
        }
    }
    s = 0;
    for(x = 0; x < BUFFERSIZE; x++){
        for(y = 0; y < BUFFERSIZE; y++){
            if (a[x][y] < 10000){
                s++;
            }
        }
    }
    return s;
}