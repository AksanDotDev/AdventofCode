#include <stdio.h>
#include <stdlib.h>

char b[64];

char* runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%s\n", runner(f));
    fclose(f);
    return 0;
}


char* runner(FILE* f)
{
    int i, j, k, n;
    char h, s;
    int a[26][26];
    for(i = 0; i < 26; i++){
        for(j = 0; j < 26; j++){
            a[i][j] = 0;
        }
    }
    n = 0;
    while(!feof(f)){
        fgets(b, 64, f);
        sscanf(b, "Step %c must be finished before step %c can begin.", &h, &s);
        h -= 'A';
        s -= 'A';
        if(!a[h][h]){
            n++;
        }
        if(!a[s][s]){
            n++;
        }
        a[h][h] = a[s][s] = a[s][h] = 1;
    }
    for(i = 0; i < n; i++){
        for(j = 0; j < 26; j++){
            if(a[j][j]){
                for(k = 0; k < 26; k++){
                    if(k != j && a[j][k]){
                        break;
                    }
                }
                if(k == 26){
                    b[i] = j + 'A';
                    a[j][j] = 0;
                    for(k = 0; k < 26; k++){
                        a[k][j] = 0;
                    }
                    break;
                }
            }
        }
    }
    b[i] = 0;
    return b;
}