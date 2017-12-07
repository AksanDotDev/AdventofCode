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
    int i,j,k,s,l;
    int a[32]; 
    s = i = j = 0;
    l = 1;
    while(!feof(f))
    {
        c = fgetc(f);
        switch(c)
        {            
            case '\t' :
            case ' ' :
                if (!l)
                    break;
                b[i] = 0;
                a[j] = strtol(b, NULL, 10);
                printf("a[j] = %d, ", a[j]);
                i = 0;
                for(k=0;k<j;k++)
                {
                    if (a[k]%a[j] == 0)
                    {
                        s += a[k]/a[j];
                        l = 0;
                        j = -1;
                        break;
                    }
                    else if (a[j]%a[k] == 0)
                    {
                        s += a[j]/a[k];
                        l = 0;
                        j = -1;
                        break;
                    }
                }
                j++;
                break;
            case '\n' :
                if (!l)
                {
                    j = 0;
                    l = 1;
                    break;
                }
                b[i] = 0;
                a[j] = strtol(b, NULL, 10);
                printf("a[j] = %d, ", a[j]);
                i = 0;
                for(k=0;k<j;k++)
                {
                    if (a[k]%a[j] == 0)
                    {
                        s += a[k]/a[j];
                        l = 0;
                        j = 0;
                        break;
                    }
                    else if (a[j]%a[k] == 0)
                    {
                        s += a[j]/a[k];
                        l = 0;
                        j = 0;
                        break;
                    }
                }
                l = 1;
                break;
            default :
                if (!l)
                    break;
                b[i] = c;
                i++;
                break;
        }
        printf("i = %d, j = %d, s = %d, l = %d\n", i, j, s, l);
    }
    printf("i = %d, j = %d, s = %d, l = %d\n", i, j, s, l);
    if (l)
    {
        b[i] = 0;
        a[j] = strtol(b, NULL, 10);
        for(k=0;k<j;k++)
        {
            if (a[k]%a[j] == 0)
            {
                s += a[k]/a[j];
                break;
            }
            else if (a[j]%a[k] == 0)
            {
                s += a[j]/a[k];
                break;
            }
        }
    }
    printf("i = %d, j = %d, s = %d, l = %d\n", i, j, s, l);
    return s;
}