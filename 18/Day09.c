#include <stdio.h>
#include <stdlib.h>


typedef struct node {
    struct node* clockwise;
    struct node* counterClockwise;
    unsigned long long int value;
} node;

node * newNode(unsigned long long int);
unsigned long long int runner(int, unsigned long long int);
int main(int argc, char** argv)
{
    int p;
    unsigned long long int l;
    sscanf(argv[1], "%ld", &p);
    sscanf(argv[2], "%ld", &l);
    printf("%lld\n", runner(p, l));
    return 0;
}


unsigned long long int runner(int p, unsigned long long int l)
{
    unsigned long long int s[512];
    node* c;
    node* u;
    node* k;
    int i;
    unsigned long long int m, x, t;
    t = m = 0;
    for(i = 0; i < p; i++){
        s[i] = 0;
    }
    c = newNode(0);
    c->clockwise = c;
    c->counterClockwise = c; 
    for(m = 1; m <= l; m++){
        if(m % 23){
            u = c->clockwise;
            k = u->clockwise;
            c = newNode(m);
            u->clockwise = c;
            c->counterClockwise = u;
            c->clockwise = k;
            k->counterClockwise = c;
        } else {
            for(i = 0; i < 6; i++){
                c = c->counterClockwise;
            }
            u = c->counterClockwise;
            t = u->value + m;
            c->counterClockwise = u->counterClockwise;
            c->counterClockwise->clockwise = c;
            free(u);
            s[m % p] += t; 
        }
    }
    x = 0;
    for(i = 0; i < p; i++){
        if(s[i] > x){
            x = s[i];
        }
    }
    return x;
}

node * newNode(unsigned long long int d){
    node * r;
    if(r = malloc(sizeof(node))){
        r->value = d;
        return r;
    } else {
        printf("Out of memory?\n");
    }
}





