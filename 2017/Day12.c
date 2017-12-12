#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define SIZE 2048


int runner(FILE*);

int main(int argc, char** argv)
{
    int s;
    FILE* f = fopen(argv[1], "r");
    if (!f)
        return 1;
    s = runner(f);
    printf("%d\n", s);
    fclose(f);
    return 0;
}

int runner(FILE* f)
{
    int **a = malloc(SIZE*sizeof(int*));
    int r[8];
    char* b = (char*)malloc(128);
    int i, j, k, n, s, u;
    for (i=0;i<SIZE;i++)
    if (!a)
        exit(1);
    for (i=0;i<SIZE;i++)
    {
        a[i] = calloc(SIZE,sizeof(int));
        if (!a[i])
            exit(1);
    }
    for (i=0;i<8;i++)
        r[i] = -1;
    while(!feof(f))
    {
        fgets(b, 128, f);
        sscanf(b,"%d <-> %d, %d, %d, %d, %d, %d, %d, %d", &n, &r[0], &r[1], &r[2], &r[3], &r[4], &r[5], &r[6], &r[7]);
        for (i=0;i<8;i++)
            if (r[i] >= 0)
            {
                a[n][r[i]] = a[r[i]][n] = 1;
                r[i] = -1;
            }
        a[n][n] = 1;
    }
    u = 1;
    while(u)
    {
        u = 0;
        for (i=0;i<SIZE;i++)
            for (j=0;j<SIZE;j++)
            {
                if (!a[i][j])
                    continue;
                for (k=0;k<SIZE;k++)
                    if (a[j][k] && !a[i][k])
                    {
                        u = 1;
                        a[i][k] = a[k][i] = 1;
                    }
            }
    }
    s = 0;
    for (i=0;i<SIZE;i++)
        if (a[0][i])
            s++;
    for (i=0;i<SIZE;i++)
        free(a[i]);
    free(a);
    free(b);
    return s;
}

