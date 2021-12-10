#include <stdio.h>
#include <stdlib.h>
#define BUFFERSIZE 512
#define VIEWPORTSIZE 256

char b[64];

void runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    runner(f);
    fclose(f);
    return 0;
}


void runner(FILE* f)
{
    int i, j, n, v, s, l;
    long long int g;
    int a[VIEWPORTSIZE*2][VIEWPORTSIZE*2];
    int p[BUFFERSIZE][4];
    char b[64];
    for(i = 0; i < VIEWPORTSIZE * 2; i++){
        for(j = 0; j < VIEWPORTSIZE * 2; j++){
            a[i][j] = 0;
        }
    }
    n = 0;
    while(!feof(f)){
        fgets(b, 64, f);
        sscanf(b, "position=< %d, %d> velocity=< %d, %d>", &p[n][1], &p[n][0], &p[n][3], &p[n][2]);
        n++;
    }
    l = 1;
    v = 0;
    g = 1;
    for(i = 0; i < n; i++){
        if(abs(p[i][0]) < VIEWPORTSIZE && abs(p[i][1]) < VIEWPORTSIZE){
            a[p[i][0] + VIEWPORTSIZE][p[i][1] + VIEWPORTSIZE] = 1;
            v++;
        }
    }
    while(l || v == n){
        for(i = 0; i < n; i++){
            if(abs(p[i][0]) < VIEWPORTSIZE && abs(p[i][1]) < VIEWPORTSIZE){
                a[p[i][0] + VIEWPORTSIZE][p[i][1] + VIEWPORTSIZE] = 0;
                v--;
            }
            p[i][0] += p[i][2];
            p[i][1] += p[i][3];
            if(abs(p[i][0]) < VIEWPORTSIZE && abs(p[i][1]) < VIEWPORTSIZE){
                a[p[i][0] + VIEWPORTSIZE][p[i][1] + VIEWPORTSIZE] = 1;
                v++;
            }
        }
        if (v == n){
            l = 0;
            for(i = 0; i < VIEWPORTSIZE * 2; i++){
                for(j = 0; j < VIEWPORTSIZE * 2; j++){
                    if (a[i][j]){
                        putchar(' ');
                    } else {
                        putchar ('#');
                    }
                }
                putchar('\n');
            }
            printf("%lld", g);
            putchar('\n');
        } 
        g++;
    }
}