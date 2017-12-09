#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%d\n", runner(f));
    fclose(f);
    return 0;
}

int runner(FILE* f)
{
    char* b = (char*)malloc(1024);
    int i, d, g, n, s;
    if (b == NULL)
        exit(1);
    i = d = g = n = s = 0;
    while(!feof(f))
    {
        fgets(b,1024,f);
        i = 0;
        while(b[i]!=0)
        {
            if(d)
            {
                d = 0;
                i++;
                continue;
            }
            switch(b[i])
            {
                case '!' :
                    d = 1;
                    break;
                case '<':
                    g = 1;
                    break;
                case '>':
                    g = 0;
                    break;
                case '{':
                    if (g)
                        break;
                    n ++;
                    break;
                case '}':
                    if (g)
                        break;
                    s += n--;
                    break;
                default :
                    break;
            }
            i++;
        }
    }
    free(b);
    return(s);
}