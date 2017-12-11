#include <stdio.h>
#include <stdlib.h>

#define LOOPSIZE 256

void reverse_section(int *, int , int , int);
int main(int argc, char **argv)
{
    int a[LOOPSIZE];
    int wh, jl, rl, i;
    wh = jl = 0;
    for (i=0;i<LOOPSIZE;i++)
        a[i] = i;
    for (i=1;i<argc;i++)
    {
        rl = strtol(argv[i],NULL,10);
        reverse_section(a,wh,rl,LOOPSIZE);
        wh = (wh + rl + jl++)%LOOPSIZE;
    } 
    printf("%d\n", a[0]*a[1]);
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