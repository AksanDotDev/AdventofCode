#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define SIZE 2048


int runner(FILE*);

int main(int argc, char** argv)
{
    int s;
    FILE* f = fopen(argv[1], "r");
    if (!f)
        return 1;
    s = runner(f);
    printf("%d\n", s);
    fclose(f);
    return 0;
}

int runner(FILE* f)
{
    char* b = (char*)malloc(128);
    int d, r, s, t;
    t = -1;
    do
    {
        t++;
        s = 0;
        while(!feof(f))
        {
            fgets(b, 128, f);
            sscanf(b,"%d: %d", &d, &r);
            if ((d + t) % ((r-1)*2) == 0)
            {
                s = 1;
                break;
            }
        }
        rewind(f);
    }
    while(s);
    free(b);
    return t;
}

