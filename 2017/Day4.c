#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%d\n", runner(f));
    return 0;
}

int runner(FILE* f)
{
    char** a = (char**)malloc(256);
    char* b = (char*)malloc(1024);
    int i, j, k, l, s, w;
    if (a == NULL || b == NULL)
        exit(1);
    for (i=0;i<64;i++)
    {
        a[i] = (char*)malloc(64);
        if (a[i] == NULL)
            exit(1);
    }
    s = 0;
    while(!feof(f))
    {
        b = fgets(b,1024,f);
        i = j = k = 0;
        w = 1;
        while(w)
        {
            switch(b[k])
            {
                case ' ' :
                    a[i][j] = 0;
                    for (l=0;l<i;l++)
                    {
                        if (strcmp(a[l], a[i]) == 0)
                        {
                            w = 0;
                            break;
                        }
                    }
                    i++;
                    j = 0;
                    break;
                case '\n':
                    break;
                case 0:
                    a[i][j] = 0;
                    for (l=0;l<i;l++)
                    {
                        if (strcmp(a[l], a[i]) == 0)
                        {
                            w = 0;
                            break;
                        }
                    }
                    if (w)
                        s++;
                    w = 0;
                    break;
                default :
                    a[i][j] = b[k];
                    j++;
                    break;
            }
            k++;
        }
    }
    return(s);
}