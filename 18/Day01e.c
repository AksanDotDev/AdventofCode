#include <stdio.h>
#include <stdlib.h>
#define BUFFERSIZE 262144

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
    int r, i, j, k;
    int a[BUFFERSIZE];
    char b[32];
    r = j = 0;
    while(j<BUFFERSIZE){
        while(!feof(f)){
            fgets(b, 32, f);
            i = strtol(b, NULL, 10);
            r += i;
            for(k = 0; k < j; k++){
                if (a[k] == r){
                    return r;
                }
            }
            a[j++] = r;
        }
        rewind(f);
    }
    return 0;
}