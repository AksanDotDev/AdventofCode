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
    int x, y, i, j, s, n, m;
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
            m = 4*BUFFERSIZE;
            for(i = 0; i < n; i++){
                s = abs(x - c[i][0]) + abs(y - c[i][1]);
                if (s < m){
                    a[x][y] = i;
                    m = s;
                } else if (s == m){
                    a[x][y] = -1;
                }
            }
        }
    }
    m = 0;
    for(i = 0; i < n; i++){
        s = 0;
        for(j = 0; j < BUFFERSIZE; j++){
            if(a[j][0] == i || a[0][j] == i || a[j][BUFFERSIZE-1] == i || a[BUFFERSIZE-1][j] == i){
                s++;
                break;
            }
        }
        if (!s){
            for(x = 0; x < BUFFERSIZE; x++){
                for(y = 0; y < BUFFERSIZE; y++){
                    if (a[x][y] == i){
                        s++;
                    }
                }
            }
            if (s > m){
                m = s;
            }
        }
    }
    return m;
}