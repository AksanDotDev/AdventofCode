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
    int d, t, df, tf, i, j;
    char a[64];
    char b[64];
    d = t = 0;
    while(!feof(f)){
        df = tf = 0;
        fgets(b, 64, f);
        for(i = 0; b[i]; i++){
            a[i] = 1;
            for(j = 0; j < i; j++){
                if (b[j] == b[i]){
                    a[i]++;
                    a[j]++;
                }
            }
        }
        for(j = 0; j < i; j++){
            if(a[j] == 2){
                df++;
            } else if (a[j] == 3){
                tf++;
            }
        }
        if (df){
            d++;
        }
        if (tf){
            t++;
        }
    }
    return d*t;
}