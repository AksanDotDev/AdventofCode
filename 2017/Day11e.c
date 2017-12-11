#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int runner(FILE*);
void add_step(char*, int*, int*);

int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%d\n", runner(f));
    fclose(f);
    return 0;
}

int runner(FILE* f)
{
    char* b = (char*)calloc(1,4);
    int i, x, y, s, m;
    char c;
    if (b == NULL)
        exit(1);
    x = y = s = i = 0;
    while(!feof(f))
    {
        c = fgetc(f);
        switch(c)
        {
            case ',' :
                b[i] = 0;
                add_step(b,&x,&y);
                if (abs(y) < (abs(y) + abs((abs(x)-abs(y)))/2))
                    s = abs(y);
                else
                    s = abs(y) + abs((abs(x)-abs(y)))/2;
                if (s > m)
                    m = s;
                i = 0;
                break;
            default :
                b[i++] = c;
                break;
        }
    }
    b[i] = 0;
    add_step(b,&x,&y);
    free(b);
    return(m);
}

void add_step(char* b, int* x, int* y)
{
    switch (b[0])
    {
        case 'n' :
            *x += 1;
            break;
        case 's' :
            *x -= 1;
            break;
        default :
            fprintf(stderr, "Error\n");
            break;
    }
    switch (b[1])
    {
        case 'e' :
            *y += 1;
            break;
        case 'w' :
            *y -= 1;
            break;
        default :
            switch (b[0])
        {
            case 'n' :
                *x += 1;
                break;
            case 's' :
                *x -= 1;
                break;
            default :
                fprintf(stderr, "Error2\n");
                break;
        }
    }
}