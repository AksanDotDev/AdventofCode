#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char** argv)
{
    int n, o, s, i;
    n = strtol(argv[1], NULL, 10);
    s =  (int)sqrt(n);
    o = n - s*s;
    if (o != 0)
    {
        if (s % 2 != 0)
            s++;
        else 
            o--;
        i = s;
        o = o % s;
        o = abs(s/2 - o);
        i -= (s/2 - o);
    }
    else 
    {
        i = s - 1;
    }
    printf("%d\n", i);
    return 0;
}