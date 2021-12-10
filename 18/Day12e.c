#include <stdio.h>
#include <stdlib.h>
#define GENERATIONS 50000000000
#define BUFFERSIZE 8192




long long int runner(FILE*);
int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%lld\n", runner(f));
    fclose(f);
    return 0;
}


long long int runner(FILE* f)
{
    int i, j, c, d;
    long long int a;
    int e[32];
    char b[128];
    char o[128];
    int s[BUFFERSIZE];
    char u;
    int l[BUFFERSIZE];
    int r[BUFFERSIZE];
    int * p;
    int * n;
    
    for(i = 0; i < BUFFERSIZE; i++){
        l[i] = 0;
    }
    for(i = 0; i < 32; i++){
        e[i] = 0;
    }
    fgets(b, 128, f);
    sscanf(b, "initial state: %s", &o);
    for(i = 0; o[i]; i++){
        if (o[i] == '#'){
            l[i + BUFFERSIZE/8] = 1; 
        } 
    }
    fgets(b, 128, f);
    for(i = 0; i < 32; i++){
        fgets(b, 128, f);
        sscanf(b, "%s => %c", &o, &u);
        if (u == '#'){
            c = 0;
            for (j = 0; j < 5; j++) {
                if (o[j] == '#'){
                    c += (16 >> j);
                }
            }
            e[c] = 1;
        } 
    }
    for (i = 0; i < GENERATIONS; i++){
        if (i & 1){
            p = r;
            n = l;
        } else {
            p = l;
            n = r;
        }
        c = (p[0] << 1) + p[1];
        for (j = 0; j < BUFFERSIZE; j++){
            c <<= 1;
            c &= 31;
            if (j + 2 < BUFFERSIZE){
                c += p[j+2];
            }
            n[j] = e[c];
        }
        s[i] = 0;
        for (j = 0; j < BUFFERSIZE; j++){
            if (n[j]){
                s[i] += j - BUFFERSIZE/8;
            }
        } 
        d = s[i] - s[i-1];
        for (j = i - 2; j >= 0; j--){
            if (s[j] != s[i] - (d * (i-j))){
                break;
            }
        }
        if (j < i/2 && j > 0){
            a = GENERATIONS - 1 - i;
            a *= d;
            a += s[i];
            break;
        }
    } 
    return a;
}