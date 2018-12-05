#include <stdio.h>
#include <stdlib.h>
#define BUFFERSIZE 16384

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
    int n, d, i;
    char c;
    char p[BUFFERSIZE];
    n = 0;
    while(!feof(f) && n < BUFFERSIZE){
        c = fgetc(f);
        if (n){
            d = (p[n-1] - c) > 0 ? (p[n-1] - c) : (c - p[n-1]);
            if (d == 32 || c == '\n'){ 
                n--;
            } else {
                p[n++] = c;
            }
        } else {
            p[n++] = c;
        }
    }
    return n - 1;
}