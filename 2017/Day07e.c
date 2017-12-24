#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TOWERMAX 2048

typedef struct Program
{
    char name[8];
    struct Program* below;
    struct Program* above[8];
    int weight;
    int weightabove;
    int balanced;
}
Program;


void nandw(Program**,FILE*);
void aandb(Program**,FILE*);
Program* root(Program*);
void correctimbalance(Program*);
int balanced(Program*);
void printtower(Program**);

int main(int argc, char** argv)
{
    int i;
    Program** tower = (Program**)malloc(TOWERMAX*sizeof(Program*));
    if (!tower)
    {
        fprintf(stderr, "Error, malloc failed.\n");
        return 1;
    }
    for (i=0;i<TOWERMAX;i++)
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
    correctimbalance(root(tower[0]));
    for (i=0;i>TOWERMAX;i++)
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
            for (k=0;k<TOWERMAX;k++)
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
    free(target);
}

void printtower(Program** tower)
{
    int i, j;
    for (i=0;i<TOWERMAX;i++)
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

void correctimbalance(Program* root)
{
    int i, j, w, l;
    int a[8],b[8];
    for (i=0;i<8;i++)
        b[i] = 0;
    if (root -> above[0] == NULL)
    {
        root -> weightabove = 0;
        root -> balanced = 1;
        return;
    }
    for (i=0;i<8;i++)
    {
        if (root -> above[i])
        {
            correctimbalance(root -> above[i]);
        }
        else 
            break;
        a[i] = (root -> above[i] -> weight) + (root -> above[i] -> weightabove);
        for (j=0;j<i;j++)
            if (a[j]==a[i])
                b[j] = b[i] = 1;
    }
    l = i;
    for (i=0;i<l;i++)
        if (b[i] == 0)
        {
            if (i == 0)
                j = i + 1;
            else
                j = i -1;
            w = (root -> above[j] -> weight + root -> above[j] -> weightabove) - root -> above[i] -> weightabove;
            printf ("%s: %d\n", root -> above[i] -> name, w);
            root -> above[i] -> weight = w;
            a[i] = root -> above[i] -> weight + root -> above[i] -> weightabove;
        }
    root -> balanced = 1;
    for (i=0;i<l;i++)
        root -> weightabove += a[i];
    return;
}



Program* root(Program* node)
{
    if (node -> below == NULL)
        return node;
    return root(node -> below);
}