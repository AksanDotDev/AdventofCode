#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%d\n", runner(f));
    close(f);
    return 0;
}

int runner(FILE* f)
{
    char b[32];
    char c;
    int x,n,i,j,s,t;
    s = i = 0;
    j = 1;
    while(!feof(f))
    {
        c = fgetc(f);
        switch(c)
        {            
            case '\t' :
            case ' ' :
                b[i] = 0;
                t = strtol(b, NULL, 10);
                if (j)
                {
                    n = x = t;
                    j = 0;
                }
                else if (t>x)
                    x = t;
                else if (t<n)
                    n = t;
                i = 0;
                break;
            case '\n' :
                b[i] = 0;
                t = strtol(b, NULL, 10);
                if (j)
                    n = x = t;
                else if (t>x)
                    x = t;
                else if (t<n)
                    n = t;
                i = 0;
                j = 1;
                s += x - n;
                break;
            default :
                b[i] = c;
                i++;
                break;
        }
    }
    b[i] = 0;
    t = strtol(b, NULL, 10);
    if (j)
        n = x = t;
    else if (t>x)
        x = t;
    else if (t<n)
        n = t;
    s += x - n;
    return s;
}