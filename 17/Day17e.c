#include <stdio.h>
#include <stdlib.h>

#define UPPER   50000000

int runner(int);
int main(int argc, char** argv)
{
    int a = strtol(argv[1],NULL,10);
    printf("%d", runner(a));
    return 0;
}

int runner(const int a)
{
    int i, n, p, s;
    s = 1;
    for (i=1;i<=UPPER;i++)
    {
        p = (p + a) % s;
        p++;
        if (p == 1)
            n = i;
        s++;
    }
    return n;
}