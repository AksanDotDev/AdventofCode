#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct vector {
    int x;
    int y;
    int z;
} vector;

typedef struct particle {
    vector pos;
    vector vel;
    vector acc;
} particle;

particle* graphic;
int pn;
int result;

void reader(FILE*);

int main(int argc, char** argv)
{
    int i, n;
    FILE* f = fopen(argv[1], "r");
    reader(f);
    fclose(f);
    n = HUGE_VAL;
    for (i=0;i<pn;i++)
        if ((abs(graphic[i].acc.x) + abs(graphic[i].acc.y) + abs(graphic[i].acc.z)) < n)
        {
            n = (abs(graphic[i].acc.x) + abs(graphic[i].acc.y) + abs(graphic[i].acc.z));
            result = i;
        }
    free(graphic);
    printf("%d\n", result);
    return 0;
}


void reader(FILE* f)
{
    char* buffer = (char*)malloc(512);
    int i;
    i = 0;
    if (!buffer)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    while(!feof(f))
    {
        fgets(buffer,512,f);
        i++;
    }
    pn = i;
    rewind(f);
    graphic = malloc(pn*sizeof(particle));
    if (!graphic)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    for (i=0;i<pn;i++)
    {
        fgets(buffer,512,f);
        sscanf(buffer, "p=<%d,%d,%d>, v=<%d,%d,%d>, a=<%d,%d,%d>", &graphic[i].pos.x, &graphic[i].pos.y, &graphic[i].pos.z, \
            &graphic[i].vel.x, &graphic[i].vel.y, &graphic[i].vel.z, &graphic[i].acc.x, &graphic[i].acc.y, &graphic[i].acc.z);
    }
    free(buffer);
}