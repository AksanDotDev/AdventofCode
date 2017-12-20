#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define GENS 1000

typedef struct vector {
    int x;
    int y;
    int z;
} vector;

typedef struct particle {
    vector pos;
    vector vel;
    vector acc;
    int alive;
} particle;

particle* graphic;
int pn;
int result;

void reader(FILE*);
void runner(void);

int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    reader(f);
    fclose(f);
    runner();
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
        graphic[i].alive = 1;
    }
    free(buffer);
}

void runner(void)
{
    int i, j, g;
    result = pn;
    for (g=0;g<GENS;g++)
    {
        for (i=0;i<pn;i++)
            if (graphic[i].alive)
            {
                graphic[i].vel.x += graphic[i].acc.x;
                graphic[i].vel.y += graphic[i].acc.y;
                graphic[i].vel.z += graphic[i].acc.z;
                graphic[i].pos.x += graphic[i].vel.x;
                graphic[i].pos.y += graphic[i].vel.y;
                graphic[i].pos.z += graphic[i].vel.z;
                for (j=0;j<i;j++)
                    if (graphic[j].alive && graphic[i].pos.x == graphic[j].pos.x \
                        && graphic[i].pos.y == graphic[j].pos.y && graphic[i].pos.z == graphic[j].pos.z)
                        graphic[i].alive = graphic[j].alive = -1;
            }
        for (i=0;i<pn;i++)
            if (graphic[i].alive == -1)
            {
                graphic[i].alive = 0;
                result--;
            }
    }
}