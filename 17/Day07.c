#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Program
{
    char name[8];
    struct Program* below;
    struct Program* above[8];
    int weight;
}
Program;


void nandw(Program**,FILE*);
void aandb(Program**,FILE*);
Program* root(Program*);
void printtower(Program**);

int main(int argc, char** argv)
{
    int i;
    Program** tower = (Program**)malloc(2048*sizeof(Program*));
    if (!tower)
    {
        fprintf(stderr, "Error, malloc failed.\n");
        return 1;
    }
    for (i=0;i<2048;i++)
    {
        tower[i] = (Program*)calloc(1,sizeof(Program));
        if (!tower[i])
        {
            fprintf(stderr, "Error, calloc failed.\n");
            return 1;
        }
    }
    FILE* f = fopen(argv[1], "r");
    if (!f)
    {
        fprintf(stderr, "Error, file open failed.\n");
        return 1;
    }
    nandw(tower,f);
    aandb(tower,f);
    fclose(f);
    printf("%s\n", root(tower[0])->name);
    for (i=0;i>2048;i++)
        free(tower[i]);
    free(tower);
    return 0;
}

void nandw(Program** tower,FILE* f)
{
    char* buffer = (char*)malloc(128);
    if (!buffer)
    {
        fprintf(stderr, "Error, malloc failed.\n");
        exit(1);
    }
    int i, j;
    i = 0;
    while (!feof(f))
    {
        fgets(buffer,128,f);
        j = 0;
        while(buffer[j] != ' ')
        {
            tower[i] -> name[j] = buffer[j];
            j++;
        }
        tower[i] -> name[j] = 0;
        j += 2;
        tower[i] -> weight = strtol(buffer+j, NULL, 10);
        i++;
    }
    free(buffer);
}

void aandb(Program** tower,FILE* f)
{
    char* buffer = (char*)malloc(128);
    char* target = (char*)malloc(8);
    if (!buffer || !target)
    {
        fprintf(stderr, "Error, malloc failed.\n");
        exit(1);
    }
    int i, j, k, l;
    i = 0;
    rewind(f);
    while (!feof(f))
    {
        fgets(buffer,128,f);
        j = 0;
        while(buffer[j] != '>' && buffer[j] != '\n' && buffer[j] != 0)
            j++;
        l = 0;
        while (buffer[j] != '\n' && buffer[j] != 0) 
        {
            j += 2;
            k = 0;
            while (buffer[j] != ',' && buffer[j] != '\n' && buffer[j] != '\0')
            {
                target[k] = buffer[j];
                j++;
                k++;
            }
            target[k] = 0;
            for (k=0;k<2048;k++)
            {
                if(!strcmp(target,tower[k]->name))
                {
                    tower[i] -> above[l] = tower[k];
                    tower[k] -> below = tower [i];
                    break;
                }
            }
            l++;
        }
        i++;
    }
    free(buffer);
}
void printtower(Program** tower)
{
    int i, j;
    for (i=0;i<2048;i++)
    {
        if (tower[i] -> name[0] == 0)
            break;
        printf("%s\t(%d)", tower[i] -> name, tower[i] -> weight);
        printf("\tBelow: ");
        if (tower[i] -> below != NULL)
            printf("%s", tower[i] -> below -> name);
        else
            printf("\t");
        printf("\tAbove: ");
        for(j=0;j<8;j++)
        {
            if (tower[i] -> above[j] == NULL)
                break;
            printf("\t%s", (tower[i] -> above[j]) -> name);
        }
        printf("\n");
    }
    
}

Program* root(Program* node)
{
    if (node -> below == NULL)
        return node;
    return root(node -> below);
}