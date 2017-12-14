#include <stdio.h>
#include <stdlib.h>

#define LOOPSIZE 256

int runner(char*, int, int*);
void reverse_section(int *, int , int , int);
int hash_count(int*, int);

int main(int argc, char **argv)
{
    int a[LOOPSIZE];
    int b[64];
    int wh, jl, i, j, k, n, s;
    s = 0;
    for(k=0;k<128;k++)
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
        s += hash_count(a,LOOPSIZE);
    }
    printf("%d\n", s);
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

int hash_count(int* a, int n)
{
    int i, j, s;
    int b[16];
    s = 0;
    for (i=0;i<n;i+=16)
    {
        b[i/16] = a[i] ^ a[i+1] ^ a[i+2] ^ a[i+3] ^ a[i+4] ^ a[i+5] ^ a[i+6] ^ a[i+7] \
            ^ a[i+8] ^ a[i+9] ^ a[i+10] ^ a[i+11] ^ a[i+12] ^ a[i+13] ^ a[i+14] ^ a[i+15];
    }
    for(i=0;i<16;i++)
        for (j=0;j<8;j++)
            s += (b[i]>>j) & 1;   
    return s;
}