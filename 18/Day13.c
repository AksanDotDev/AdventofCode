#include <stdio.h>
#include <stdlib.h>
#define BUFFERSIZE 256

char b[BUFFERSIZE];

typedef struct cart{
    short int x;
    short int y;
    short int d;
    short int t;
} cart;

int compareCarts(cart * a, cart * b);
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
    int i, j, n, s;
    short int a[BUFFERSIZE][BUFFERSIZE];
    cart c[BUFFERSIZE];
    i = n = 0;
    while(!feof(f)){
        fgets(b,255,f);
        /*
        *   World
        *   0 - Nothing
        *   1 - Vertical
        *   2 - Horizontal
        *   3 - TL Corner
        *   4 - TR Corner
        *   5 - BL Corner
        *   6 - BR Corner
        *   7 - Intersection 
        *   Carts d
        *   0 - Up
        *   1 - Right
        *   2 - Down
        *   3 - Left
        *   Carts t
        *   0 - Left
        *   1 - Straight
        *   2 - Right
        */
        for(j = 0; b[j]; j++){
            switch(b[j]){
                case ' ':
                    a[j][i] = 0;
                    break;
                case '|':
                    a[j][i] = 1;
                    break;
                case '-':
                    a[j][i] = 2;
                    break;
                case '/':
                    if(i > 1 && (a[j][i-1] == 1 || a[j][i-1] == 7)){
                        a[j][i] = 5;
                    } else {
                        a[j][i] = 3;
                    }
                    break;
                case '\\':
                    if(i > 1 && (a[j][i-1] == 1 || a[j][i-1] == 7)){
                        a[j][i] = 6;
                    } else {
                        a[j][i] = 4;
                    }
                    break;
                case '+':
                    a[j][i] = 7;
                    break;
                case '^':
                    a[j][i] = 1;
                    c[n].x = j;
                    c[n].y = i;
                    c[n].d = 0;
                    c[n].t = 0;
                    n++;
                    break;
                case 'v':
                    a[j][i] = 1;
                    c[n].x = j;
                    c[n].y = i;
                    c[n].d = 2;
                    c[n].t = 0;
                    n++;
                    break;
                case '>':
                    a[j][i] = 2;
                    c[n].x = j;
                    c[n].y = i;
                    c[n].d = 1;
                    c[n].t = 0;
                    n++;
                    break;
                case '<':
                    a[j][i] = 2;
                    c[n].x = j;
                    c[n].y = i;
                    c[n].d = 3;
                    c[n].t = 0;
                    n++;
                    break;
           }
       }
       i++;
    }
    s = 1;
    while(s){
        qsort( c, n, sizeof(cart), compareCarts);
        for(i = 0; i < n && s; i++){
            switch(c[i].d){
                case 0:
                    c[i].y--;
                    break;
                case 1:
                    c[i].x++;
                    break;
                case 2:
                    c[i].y++;
                    break;
                case 3:
                    c[i].x--;
                    break;
            }
            switch(a[c[i].x][c[i].y]){
                case 0:
                    printf("Map panic!\n %d %d \n", c[i].x, c[i].y);
                    exit(1);
                case 1:
                case 2:
                    break;
                case 3:
                    if(c[i].d == 0){
                        c[i].d = 1;
                    } else {
                        c[i].d = 2;
                    }
                    break;
                case 4:
                    if(c[i].d == 0){
                        c[i].d = 3;
                    } else {
                        c[i].d = 2;
                    }
                    break;
                case 5:
                    if(c[i].d == 2){
                        c[i].d = 3;
                    } else {
                        c[i].d = 0;
                    }
                    break;
                case 6:
                    if(c[i].d == 2){
                        c[i].d = 1;
                    } else {
                        c[i].d = 0;
                    }
                    break;
                case 7:
                    if(c[i].t == 1){
                        c[i].t++;
                    } else if (c[i].t == 2){
                        c[i].t = 0;
                        if(c[i].d < 3){
                            c[i].d++;
                        }else{
                            c[i].d = 0;
                        }
                    } else {
                        c[i].t++;
                        if(c[i].d){
                            c[i].d--;
                        }else{
                            c[i].d = 3;
                        }
                    }
                    break;                
            }
            for(j = 0; j < n; j++){
                if (j != i && c[i].y == c[j].y &&  c[i].x == c[j].x){
                    s = 0;
                    break;
                }
            }
        }

    }
    sprintf(b,"(%03d,%03d)", c[j].x, c[j].y);
    return b;
}

int compareCarts(cart * a, cart * b){
    if(a->x - b->x){
        return a->x - b->x;
    } else {
        return a->y - b->y;
    }
}