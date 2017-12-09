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
    int i, d, g, s;
    if (b == NULL)
        exit(1);
    i = d = g = s = 0;
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
                    if (g)
                        s++;
                    g = 1;
                    break;
                case '>':
                    g = 0;
                    break;
                default :
                    if (g)
                        s++;
                    break;
            }
            i++;
        }
    }
    free(b);
    return(s);
}