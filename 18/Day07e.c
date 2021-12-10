#include <stdio.h>
#include <stdlib.h>
#define WORKERS 5
#define BASETIME 61

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
    int i, j, k, n, t;
    char h, s;
    char b[64];
    int w[WORKERS];
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
        a[h][h] = h + BASETIME;
        a[s][s] = s + BASETIME;
        a[s][h] = 1;
    }
    for(i = 0; i < WORKERS; i++){
        w[i] = -1;
    }
    while(n){
        for(i = 0; i < WORKERS; i++){
            if (w[i] == -1){
                for(j = 0; j < 26; j++){
                    if(a[j][j]){
                        for(k = 0; k < 26; k++){
                            if(k != j && a[j][k]){
                                break;
                            }
                        }
                        if(k == 26){
                            for(k = 0; k < WORKERS; k++){
                                if(k != i && w[k] == j){
                                    break;
                                }
                            }
                            if(k == WORKERS){
                                w[i] = j;
                                break;
                            }
                        }
                    }
                }
            }
        }
        for(i = 0; i < WORKERS; i++){
            if(w[i] >= 0 && !--a[w[i]][w[i]]){
                for(k = 0; k < 26; k++){
                    a[k][w[i]] = 0;
                }
                w[i] = -1;
                n--;
            }
        }
        t++;
    }
    return t;
}