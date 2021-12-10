#include <stdio.h>
#include <stdlib.h>

char b[64];

void runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    runner(f);
    fclose(f);
    printf("%s", b);
    return 0;
}


void runner(FILE* f)
{
    int i, j, k, l, d;
    char s[256][64];
    k = -1;
    while(!feof(f)){
        fgets(s[++k], 64, f);
        for(i = 0; i < k; i++) {
            d = 0;
            for(j = 0; s[i][j] && d < 2; j++){
                if (s[i][j] != s[k][j]){
                    d++;
                }
            }
            if (d == 1){
                for (j = l = 0; s[k][j]; j++){
                    if (s[i][j] == s[k][j]){
                        b[l++] = s[k][j];
                    }
                    b[l] = '\0';
                }
            }
        }
    }
}