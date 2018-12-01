#include <stdio.h>
#include <stdlib.h>

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
    int r, i;
    char b[32];
    r = 0;
    while(!feof(f)){
        fgets(b, 32, f);
        i = strtol(b, NULL, 10);
        r += i;
    }
    return r;
}