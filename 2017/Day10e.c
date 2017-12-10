#include <stdio.h>
#include <stdlib.h>

#define LOOPSIZE 256

int runner(FILE*, int*);
void reverse_section(int *, int , int , int);
void hash_print(int*, int);

int main(int argc, char **argv)
{
    int a[LOOPSIZE];
    int b[64];
    int wh, jl, i, j, n;
    wh = jl = 0;
    for (i=0;i<LOOPSIZE;i++)
        a[i] = i;
    FILE* f = fopen(argv[1], "r");
    n = runner(f, b);
    for (i=0;i<64;i++)
        for (j=0;j<n;j++)
        {
            reverse_section(a,wh,(int)b[j],LOOPSIZE);
            wh = (wh + b[j] + jl++)%LOOPSIZE;
        }
    hash_print(a,LOOPSIZE);
}

int runner(FILE* f, int* b)
{
    char c;
    int i = 0;
    while (!feof(f) && (c = fgetc(f)) && c != '\n' && c > 0)
    {
        b[i++] = c;
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

void hash_print(int* a, int n)
{
    int i;
    int b[16];
    for (i=0;i<n;i+=16)
    {
        b[i/16] = a[i] ^ a[i+1] ^ a[i+2] ^ a[i+3] ^ a[i+4] ^ a[i+5] ^ a[i+6] ^ a[i+7] \
            ^ a[i+8] ^ a[i+9] ^ a[i+10] ^ a[i+11] ^ a[i+12] ^ a[i+13] ^ a[i+14] ^ a[i+15];
    }
    
    for(i=0;i<16;i++)
        printf("%02x", b[i]);
    printf("\n");
}