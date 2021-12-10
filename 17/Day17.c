#include <stdio.h>
#include <stdlib.h>

#define UPPER   2017

int runner(int);
int main(int argc, char** argv)
{
    int a = strtol(argv[1],NULL,10);
    printf("%d", runner(a));
    return 0;
}

int runner(const int a)
{
    int* cbuff = malloc((UPPER+1)*sizeof(int));
    int i, j, p, s;
    for (i=0;i<=UPPER;i++)
        cbuff[i] = -1;
    cbuff[0] = p = 0;
    s = 1;
    for (i=1;i<=UPPER;i++)
    {
        p = (p + a) % s;
        p++;
        for (j=s;j>p;j--)
            cbuff[j] = cbuff[j-1];
        cbuff[p] = i;
        s++;
    }
    p = cbuff[(p+1)%s];
    free(cbuff);
    return p;
}