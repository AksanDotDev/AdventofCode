#include <stdio.h>
#include <stdlib.h>


typedef struct node{
    int childCount;
    int metaCount;
    int metaData[64];
    struct node* children[64];
} node;

int calcNode(node*);
node * createNode(FILE*);
void freeNode(node*);
int runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%d\n", runner(f));
    fclose(f);
    return 0;
}


int runner(FILE* f)
{
    int s;
    node * o;
    o = createNode(f);
    s = calcNode(o);
    return s;
}

node* createNode(FILE* f){
    int i;
    node * w;
    w = malloc(sizeof(node));
    fscanf(f, "%d %d", &(w->childCount), &(w->metaCount));
    for(i = 0; i < w->childCount; i++){
        w->children[i] = createNode(f);
    }
    for(i = 0; i < w->metaCount; i++){
        fscanf(f, "%d", &(w->metaData[i]));
    }
    return w;
}

int calcNode(node* w){
    int s, i;
    s = 0;
    for(i = 0; i < w->childCount; i++){
        s += calcNode(w->children[i]);
    }
    for(i = 0; i < w->metaCount; i++){
        s += w->metaData[i];
    }
    return s;
}

void freeNode(node* w){
    int i;
    for(i = 0; i < w->childCount; i++){
        freeNode(w->children[i]);
    }
    free(w);
}