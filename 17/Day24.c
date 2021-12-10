#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct Component
{
    int left;
    int right;
    char inuse;
}
Component;

Component* heap;
int l;
int result;

void reader(FILE* f);
void bridge(int p, int s);

int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    if (!f)
    {
        fprintf(stderr, "Error, file open failed.\n");
        return 1;
    }
    reader(f);
    fclose(f);
    result = d = 0;
    bridge(0, 0);
    printf("%d\n", result);
    return 0;
}

void reader(FILE* f)
{
    char* buffer = (char*)malloc(512);
    int i;
    if (!buffer)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    l = 0;
    while(!feof(f))
    {
        fgets(buffer,512,f);
        l++;
    }
    rewind(f);
    heap = (Component*)malloc(l*sizeof(Component));
    if (!heap)
    {
        fprintf(stderr, "Error, malloc failed.\n");
        exit(1);
    }
    for (i=0;i<l;i++)
    {
        fgets(buffer,512,f);
        sscanf(buffer, "%d/%d", &heap[i].left, &heap[i].right);
        heap[i].inuse = 0;
    }
    return;
}

void bridge(int p, int s)
{
    int i;
    for (i=0;i<l;i++)
    {
        if (!heap[i].inuse && heap[i].left == p)
        {
            heap[i].inuse = 1;
            bridge(heap[i].right, (s + heap[i].left + heap[i].right));
            heap[i].inuse = 0;
        }
        if (!heap[i].inuse && heap[i].right == p)
        {
            heap[i].inuse = 1;
            bridge(heap[i].left, (s + heap[i].left + heap[i].right));
            heap[i].inuse = 0;
        }
    }
    if (s > result)
        result = s;
    return;
}