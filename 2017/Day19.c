#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char** map;
int xlim;
int ylim;
char* result;

void reader(FILE*);
void runner(void);

int main(int argc, char** argv)
{
    int i;
    FILE* f = fopen(argv[1], "r");
    reader(f);
    fclose(f);
    runner();
    printf("%s\n", result);
    free(result);
    for (i=0;i<ylim;i++)
        free(map[i]);
    free(map);
    return 0;
}


void reader(FILE* f)
{
    char* buffer = (char*)malloc(512);
    int i;
    i = 0;
    if (!buffer)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    while(!feof(f))
    {
        fgets(buffer,512,f);
        i++;
    }
    ylim = i;
    xlim = strlen(buffer);
    rewind(f);
    map = malloc(ylim*sizeof(char*));
    if (!map)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    for (i=0;i<ylim;i++)
    {
        map[i] = malloc((xlim+1)*sizeof(char));
        if (!map[i])
        {
            fprintf(stderr, "Malloc failed\n");
            exit(1);
        }
        fgets(buffer,512,f);
        strcpy(map[i],buffer);
    }
    free(buffer);
}

void runner(void)
{
    int x, y, i, d; // D = 0, L = 1, U = 2, R = 3
    result = (char*)malloc(27);
    i = y = d = 0;
    for (x=0;x<xlim;x++)
        if (map[0][x] == '|')
            break;
    while (1)
    {
        switch (d)
        {
            case 0 :
                y++;
                break;
            case 1 :
                x--;
                break;
            case 2 :
                y--;
                break;
            case 3 :
                x++;
                break;
            default :
                fprintf(stderr, "Corrupted direction.\n");
                break;
        }
        if (x < 0 || y < 0 || x >= xlim || y >= ylim || map[y][x] == ' ')
            break;
        switch (map[y][x])
        {
            case '|' :
            case '-' :
                break;
            case '+' :
                if (d % 2)
                {
                    if (y+1 < ylim && map[y+1][x] != ' ')
                        d = 0;
                    else 
                        d = 2;
                }
                else 
                {
                    if (x+1 < xlim && map[y][x+1] != ' ')
                        d = 3;
                    else 
                        d = 1;
                }
                break;
            default :
                result[i] = map[y][x];
                i++;
                break;
        }
    }
    result[i] = 0;
}