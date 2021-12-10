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
    char **a = malloc(SIZE*sizeof(char*));
    int r[8];
    char* b = (char*)malloc(128);
    int i, j, k, n, s, u;
    for (i=0;i<SIZE;i++)
    if (!a)
        exit(1);
    for (i=0;i<SIZE;i++)
    {
        a[i] = calloc(SIZE,sizeof(char));
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
            else 
                break;
        a[n][n] = 1;
    }
    u = 1;
    while(u)
    {
        u = 0;
        for (j=0;j<SIZE;j++)
        {
            if (!a[0][j])
                continue;
            for (k=0;k<SIZE;k++)
                if (a[j][k] && !a[0][k])
                {
                    u = 1;
                    a[0][k] = a[k][0] = 1;
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

