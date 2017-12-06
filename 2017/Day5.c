#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int solver(int a[], int l);
int runner(FILE* f, int a[]);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    int a[2048];
    int l;
    l = runner(f, a);
    printf("%d\n", solver(a,l));
    return 0;
}

int runner(FILE* f, int a[])
{
    char* b = (char*)malloc(16);
    int l = 0;
    if (a == NULL || b == NULL)
        exit(1);
    while(!feof(f))
    {
        fgets(b,16,f);
        a[l] = strtol(b,NULL,10);
        l++;
    }
    free(b);
    return l;
}

int solver(int a[], int l)
{
    int i, s;
    i = s = 0;
    while (i >= 0 && i < l)
    {
        i += a[i]++;
        s++;
    }
    return s;
}