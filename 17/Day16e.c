#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define SIZE    16
#define ITER    1000000000


void runner(FILE*);
void spin(int);
void exchange(int,int);
void partner(char,char);



char* dancers;
 

int main(int argc, char** argv)
{
    int i, j;
    FILE* f = fopen(argv[1], "r");
    dancers = malloc(SIZE);
    for (i=0;i<SIZE;i++)
        dancers[i] = ('a' + i);
    for (i=0;j<SIZE;i++)
    {
        runner(f);
        for (j=0;j<SIZE;j++)
            if (dancers[j] != ('a' + j))
                break;
        rewind(f);
    }
    j = ITER % i;
    for (i=0;i<j;i++)
    {
        runner(f);
        rewind(f);
    }
    fclose(f);
    for (i=0;i<SIZE;i++)
        putchar(dancers[i]);
    putchar('\n');
    free(dancers);
    return 0;
}

void runner(FILE* f)
{
    int a, b;
    char c, d;
    while(!feof(f))
    {
        switch(fgetc(f))
        {
            case 's' :
                fscanf(f,"%d",&a);
                spin(a);
                break;
            case 'x' :
                fscanf(f,"%d/%d",&a,&b);
                exchange(a,b);
                break;
            case 'p' :
                fscanf(f,"%c/%c",&c,&d);
                partner(c,d);
                break;
            default :
                break;
        }
    }
    return;
}


void spin(int a)
{
    int i, j;
    char c;
    for (i=0;i<a;i++)
    {   
        c = dancers[SIZE-1];
        for (j=SIZE-1;j>=0;j--)
        {
            dancers[j] = dancers[j-1];
        }
        dancers[0] = c;
    }
}

void exchange(int a,int b)
{
    if (a == b)
        return;
    dancers[a] ^= dancers [b];
    dancers[b] ^= dancers [a];
    dancers[a] ^= dancers [b];
}

void partner(char a,char b)
{
    int i;
    for (i=0;i<SIZE;i++)
    {
        if (dancers[i] == a)
            dancers[i] = b;
        else if (dancers[i] == b)
            dancers[i] = a;
    }
}