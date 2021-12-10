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
    int n, m, d, i;
    char c;
    char p[BUFFERSIZE];
    m = BUFFERSIZE;
    for(i = 65; i < 91; i++){
        n = 0;
        while(!feof(f) && n < BUFFERSIZE){
            c = fgetc(f);
            if (c == i || c == i + 32){
                continue;
            }
            if (n && (abs(p[n-1] - c) == 32 || c == '\n')){ 
                n--;
            } else {
                p[n++] = c;
            }
        }
        if (n < m){
            m = n;
        }
        rewind(f);
    }
    return m - 1;
}