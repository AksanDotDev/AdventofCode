#include <stdio.h>
#include <stdlib.h>

#define LOOPSIZE 256
#define GRIDSIZE 128

int s;
int g[GRIDSIZE][GRIDSIZE];

int runner(char*, int, int*);
void reverse_section(int *, int , int , int);
void hash_count(int*, int, int);
int grid_solve(void);
void grid_update(int, int);


int main(int argc, char **argv)
{
    int a[LOOPSIZE];
    int b[64];
    int wh, jl, i, j, k, n, gr;
    for (i=0;i<GRIDSIZE;i++)
        for (j=0;j<GRIDSIZE;j++)
            g[i][j] = 0;
    s = 0;
    for (k=0;k<GRIDSIZE;k++)
    {
        wh = jl = 0;
        for (i=0;i<LOOPSIZE;i++)
            a[i] = i;
        n = runner(argv[1], k, b);
        for (i=0;i<64;i++)
            for (j=0;j<n;j++)
            {
                reverse_section(a,wh,(int)b[j],LOOPSIZE);
                wh = (wh + b[j] + jl++)%LOOPSIZE;
            }
        hash_count(a,k,LOOPSIZE);
    }
    gr = grid_solve();
    printf("%d\n", gr);
}

int runner(char* v, int k, int* b)
{
    char s[64];
    int i = 0;
    sprintf(s,"%s-%d", v, k);
    while (s[i])
    {
        b[i] = s[i];
        i++;
    }
    b[i++] = 17;
    b[i++] = 31;
    b[i++] = 73;
    b[i++] = 47;
    b[i++] = 23;
    return i;
}

void reverse_section(int *a, int wh, int rl, int al)
{
    int i;
    for (i=0;i<rl/2;i++)
    {
        a[(wh+i)%al] ^= a[(wh+rl-i-1)%al];
        a[(wh+rl-i-1)%al] ^= a[(wh+i)%al];
        a[(wh+i)%al] ^= a[(wh+rl-i-1)%al];
    }
}

void hash_count(int* a, int k, int n)
{
    int i, j, s;
    int b[16];
    for (i=0;i<n;i+=16)
    {
        b[i/16] = a[i] ^ a[i+1] ^ a[i+2] ^ a[i+3] ^ a[i+4] ^ a[i+5] ^ a[i+6] ^ a[i+7] \
            ^ a[i+8] ^ a[i+9] ^ a[i+10] ^ a[i+11] ^ a[i+12] ^ a[i+13] ^ a[i+14] ^ a[i+15];
    }
    for(i=0;i<16;i++)
        for (j=7;j>=0;j--)
            if ((b[i]>>j) & 1)
            {   
                //printf("(%d,%d) = %d\n", k, (8*i) + (7-j), s);
                g[k][(8*i)+(7-j)] = ++s;       
            }
}

int grid_solve(void)
{
    int i, j, k, x;
    int f[GRIDSIZE*GRIDSIZE];
    for (i=0;i<GRIDSIZE;i++)
        for (j=0;j<GRIDSIZE;j++)
        {
            if (g[i][j])
            {
                if (((i-1) >= 0) && g[i-1][j] && (g[i-1][j] != g[i][j]))
                    grid_update(g[i-1][j],g[i][j]);
                if (((j-1) >= 0) && g[i][j-1] && (g[i][j-1] != g[i][j]))
                    grid_update(g[i][j-1],g[i][j]);
                if (((i+1) <128) && g[i+1][j] && (g[i+1][j] != g[i][j]))
                    grid_update(g[i][j],g[i+1][j]);
                if (((j+1) <128) && g[i][j+1] && (g[i][j+1] != g[i][j]))
                    grid_update(g[i][j],g[i][j+1]);
            }
        }
    x = 0;
    for (i=0;i<GRIDSIZE;i++)
        for (j=0;j<GRIDSIZE;j++)
            if (g[i][j])
            {
                for (k=0;k<x;k++)
                    if (g[i][j] == f[k])
                        break;
                if (x == k)
                    f[x++] = g[i][j];
            }
    return x;
}

void grid_update(int t, int f)
{
    int i, j;
    for (i=0;i<GRIDSIZE;i++)
        for (j=0;j<GRIDSIZE;j++)
            if (g[i][j] == f)
                g[i][j] = t;
}