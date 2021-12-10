#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define SIZE 2047
#define ITER 10000000

int main(int argc, char** argv)
{
    char** m;
    int v, h, d, i, j;
    FILE* f = fopen(argv[1], "r");
    char* buffer = (char*)malloc(512);
    if (!(m = (char**)malloc(SIZE*sizeof(char*))) || !buffer)
    {
        printf("Malloc failed.\n");
        return 1;
    }
    for (i=0;i<SIZE;i++)
        if (!(m[i] = (char*)malloc(SIZE)))
        {
            printf("Malloc failed.\n");
            return 1;
        }   
    for (v=0;v<SIZE;v++)
        for (h=0;h<SIZE;h++)
            m[v][h] = '.';
    fgets(buffer, 512, f);
    d = (strlen(buffer)-1)/2;
    v = h = (SIZE/2) - d;
    i = j = 0;
    while (!feof(f))
    {
        while (buffer[i] != '\n' && buffer[i])
        {
            if (buffer[i] == '#')
                m[v+j][h+i] = '#';
            i++;
        }
        j++;
        i=0;
        fgets(buffer, 512, f);
    }
    while (buffer[i] != '\n' && buffer[i])
    {
        if (buffer[i] == '#')
            m[v+j][h+i] = '#';
        i++;
    }
    fclose(f);
    v = h = (SIZE/2);
    d = j = 0;
    for (i=0;i<ITER;i++)
    {
        switch (m[v][h])
        {
            case '#':
                d++;
                m[v][h] = 'F';
                break;
            case '.':
                d--;
                m[v][h] = 'W';
                break;
            case 'W':
                m[v][h] = '#';
                j++;
                break;
            case 'F':
                d += 2;
                m[v][h] = '.';
                break;
            default :
                printf("Memory corrupted\n");
                break;
        }
        d %= 4;
        if (d*4 < 0)
            d += 4;
        
        switch (d)
        {
            case 0 :
                v--;
                break;
            case 1 :
                h++;
                break;
            case 2 :
                v++;
                break;
            case 3 :
                h--;
                break;
            default :
                printf("Direction corrupted\n");
                break;
        }
        if (!h || !v || h == SIZE || v == SIZE)
        {
            printf("Out of bounds\n");
            return 1;
        }
    }
    printf("%d\n", j);
    free(buffer);
    for (i=0;i<SIZE;i++)
        free(m[i]);
    free(m);
    return 0;
}