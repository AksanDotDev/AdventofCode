#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int runner(int*, int);
int main(int argc, char** argv)
{
    int *a = (int *)calloc(argc-1,sizeof(int));
    int i;
    for(i=0;i<argc-1;i++)
    {
        a[i] = strtol(argv[i+1],NULL,10);
    }
    printf("%d\n", runner(a, argc - 1));
    return 0;
}

int runner(int* a, int n)
{
    int s, i, j, x, l, m;
    l = 256;
    int** r = (int**)malloc(sizeof(int**)*l);
    if (!r)
    {
        fprintf(stderr, "Error in malloc.\n");
        return 1;
    }
    for(i=0;i<l;i++)
    {
        r[i] = (int*)malloc(sizeof(int*)*n);
        if (!r[i])
        {
            fprintf(stderr, "Error in malloc.\n");
            return 1;
        }
    }
    m = x = 0;
    do
    {
        memcpy((void*)r[s++],(void*)a,n*sizeof(int));
        for(i=0;i<n;i++)
        {
            if (a[i] > x)
            {
                x = a[i];
                j = i;
            }
        }
        a[j++] = 0;
        if (j == n)
            j = 0;
        for(;x>0;x--)
        {
            a[j++]++;
            if (j == n)
                j = 0;
        }
        for(i=0;i<s;i++)
        {
            if (!memcmp((void*)r[i],(void*)a,n*sizeof(int)))
            {
                m++;
                break;
            }
        }
        if (s+1 == l)
        {
            l *= 2;
            r = (int**)realloc((void*)r,sizeof(int**)*l);
            if (!r)
            {
                fprintf(stderr, "Error in realloc.\n");
                return 1;
            }
            for(i=l/2;i<l;i++)
            {
                r[i] = (int*)malloc(sizeof(int*)*n);
                if (!r[i])
                {
                    fprintf(stderr, "Error in malloc.\n");
                    return 1;
                }
            }
        }
    }
    while(!m);
    for (i=0;i<l;i++)
        free(r[i]);
    free (r);
    return s;
}