#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define GENS 18

typedef struct pattern2 {
    char map[2][3];
} pattern2;

typedef struct pattern3 {
    char map[3][4];
} pattern3;

typedef struct pattern4 {
    char map[4][5];
} pattern4;

typedef struct mapping2t3 {
    pattern2 from;
    pattern3 to;
} mapping2t3;

typedef struct mapping3t4 {
    pattern3 from;
    pattern4 to;
} mapping3t4;

pattern3 seed = {.map = {".#.","..#","###"}};

int size;
int mappingscount2;
int mappingscount3;
mapping2t3* map2;
mapping3t4* map3;
pattern2* buffer2;
pattern3* buffer3;
char** canvas;
int result;

void reader(FILE*);
void runner(void);
pattern2 read2(int, int);
pattern3 read3(int, int);
void write3(int, int, pattern3);
void write4(int, int, pattern4);
int match2(pattern2, pattern2);
void rotate2(pattern2*);
void flip2(pattern2*);
int match3(pattern3, pattern3);
void rotate3(pattern3*);
void flip3(pattern3*);

int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    reader(f);
    fclose(f);
    runner();
    free(map2);
    free(map3);
    printf("%d\n", result);
    return 0;
}


void reader(FILE* f)
{
    char* buffer = (char*)malloc(512);
    int i, j;
    i = j = 0;
    if (!buffer)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    while(!feof(f))
    {
        fgets(buffer,512,f);
        if (buffer[6] == '=')
            i++;
        else
            j++;
    }
    rewind(f);
    mappingscount2 = i;
    mappingscount3 = j;
    map2 = (mapping2t3*)malloc(mappingscount2*sizeof(mapping2t3));
    map3 = (mapping3t4*)malloc(mappingscount3*sizeof(mapping3t4));
    if (!map2 || !map3)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    i = j = 0;
    while(!feof(f))
    {
        fgets(buffer,512,f);
        if (buffer[6] == '=')
        {
            sscanf(buffer, "%[^/]/%s => %[^/]/%[^/]/%s", map2[i].from.map[0], map2[i].from.map[1], map2[i].to.map[0],\
                map2[i].to.map[1], map2[i].to.map[2]);
            i++;
        }
        else
        {
            sscanf(buffer, "%[^/]/%[^/]/%s => %[^/]/%[^/]/%[^/]/%s", map3[j].from.map[0], map3[j].from.map[1], map3[j].from.map[2],\
                map3[j].to.map[0], map3[j].to.map[1], map3[j].to.map[2], map3[j].to.map[3]);
            j++; 
        }
    }
    free(buffer);
}

void runner(void)
{
    int i, j, k, s, v, h;
    size = 3;
    canvas = (char**)malloc(size*sizeof(char*));
    if (!canvas)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    for (k=0;k<size;k++)
    {
        canvas[k] = (char*)malloc(size+1);
        if (!canvas[k])
        {
            fprintf(stderr, "Malloc failed\n");
            exit(1);
        }
        strcpy(canvas[k], seed.map[k]);
    } 
    for (i=0;i<GENS;i++)
    {
        v = h = 0;
        if (size % 2)
        {
            s = (size/3)*(size/3);
            buffer3 = (pattern3*)malloc(s*sizeof(pattern3));
            for (j=0;j<s;j++)
            {
                buffer3[j] = read3(v,h);
                if (!buffer3)
                {
                    fprintf(stderr, "Malloc failed\n");
                    exit(1);
                }
                h += 3;
                if (h == size)
                {
                    v += 3;
                    h = 0;
                }
            }
            free(canvas);
            size *= 4;
            size /= 3;
            canvas = (char**)malloc(size*sizeof(char*));
            if (!canvas)
            {
                fprintf(stderr, "Malloc failed\n");
                exit(1);
            }
            for (k=0;k<size;k++)
            {
                canvas[k] = (char*)malloc(size+1);
                if (!canvas[k])
                {
                    fprintf(stderr, "Malloc failed\n");
                    exit(1);
                }
            }
            v = h = 0;
            for (j=0;j<s;j++)
            {
                for (k=0;k<mappingscount3;k++)
                    if (match3(buffer3[j], map3[k].from))
                        break;
                write4(v, h, map3[k].to);
                h += 4;
                if (h == size)
                {
                    v += 4;
                    h = 0;
                }
            }
            free(buffer3);
        }
        else
        {
            s = (size/2)*(size/2);
            buffer2 = (pattern2*)malloc(s*sizeof(pattern2));
            for (j=0;j<s;j++)
            {
                buffer2[j] = read2(v,h);
                if (!buffer2)
                {
                    fprintf(stderr, "Malloc failed\n");
                    exit(1);
                }
                h += 2;
                if (h == size)
                {
                    v += 2;
                    h = 0;
                }
            }
            free(canvas);
            size *= 3;
            size /= 2;
            canvas = (char**)malloc(size*sizeof(char*));
            if (!canvas)
            {
                fprintf(stderr, "Malloc failed\n");
                exit(1);
            }
            for (k=0;k<size;k++)
            {
                canvas[k] = (char*)malloc(size+1);
                if (!canvas[k])
                {
                    fprintf(stderr, "Malloc failed\n");
                    exit(1);
                }
            }
            v = h = 0;
            for (j=0;j<s;j++)
            {
                for (k=0;k<mappingscount2;k++)
                    if (match2(buffer2[j], map2[k].from))
                        break;
                write3(v, h, map2[k].to);
                h += 3;
                if (h == size)
                {
                    v += 3;
                    h = 0;
                }
            }
            free(buffer2);
        } 
    }
    result = 0;
    for (i=0;i<size;i++)
        for (j=0;j<size;j++)
            if (canvas[i][j] == '#')
                result ++;
}

pattern2 read2(int v, int h)
{
    pattern2 read;
    read.map[0][0] = canvas[v][h];
    read.map[0][1] = canvas[v][h+1];
    read.map[1][0] = canvas[v+1][h];
    read.map[1][1] = canvas[v+1][h+1];
    return read;
}

pattern3 read3(int v, int h)
{
    pattern3 read;
    read.map[0][0] = canvas[v][h];
    read.map[0][1] = canvas[v][h+1];
    read.map[0][2] = canvas[v][h+2];
    read.map[1][0] = canvas[v+1][h];
    read.map[1][1] = canvas[v+1][h+1];
    read.map[1][2] = canvas[v+1][h+2];
    read.map[2][0] = canvas[v+2][h];
    read.map[2][1] = canvas[v+2][h+1];
    read.map[2][2] = canvas[v+2][h+2];
    return read;
}

void write3(int v, int h, pattern3 content)
{
    canvas[v][h] = content.map[0][0];
    canvas[v][h+1] = content.map[0][1];
    canvas[v][h+2] = content.map[0][2];
    canvas[v+1][h] = content.map[1][0];
    canvas[v+1][h+1] = content.map[1][1];
    canvas[v+1][h+2] = content.map[1][2];
    canvas[v+2][h] = content.map[2][0];
    canvas[v+2][h+1] = content.map[2][1];
    canvas[v+2][h+2] = content.map[2][2];
}

void write4(int v, int h, pattern4 content)
{
    canvas[v][h] = content.map[0][0];
    canvas[v][h+1] = content.map[0][1];
    canvas[v][h+2] = content.map[0][2];
    canvas[v][h+3] = content.map[0][3];
    canvas[v+1][h] = content.map[1][0];
    canvas[v+1][h+1] = content.map[1][1];
    canvas[v+1][h+2] = content.map[1][2];
    canvas[v+1][h+3] = content.map[1][3];
    canvas[v+2][h] = content.map[2][0];
    canvas[v+2][h+1] = content.map[2][1];
    canvas[v+2][h+2] = content.map[2][2];
    canvas[v+2][h+3] = content.map[2][3];
    canvas[v+3][h] = content.map[3][0];
    canvas[v+3][h+1] = content.map[3][1];
    canvas[v+3][h+2] = content.map[3][2];
    canvas[v+3][h+3] = content.map[3][3];
}

int match2(pattern2 buffer, pattern2 mapping)
{
    int i;    
    for (i=0;i<4;i++)
    {
        if (!strncmp(buffer.map[0],mapping.map[0], 2) && !strncmp(buffer.map[1],mapping.map[1], 2))
            return 1;
        rotate2(&buffer);
    }
    flip2(&buffer);
    for (i=0;i<4;i++)
    {
        if (!strncmp(buffer.map[0],mapping.map[0], 2) && !strncmp(buffer.map[1],mapping.map[1], 2))
            return 1;
        rotate2(&buffer);
    }
    return 0; 
}

void rotate2(pattern2* content)
{
    char t;
    t = (*content).map[0][0];
    (*content).map[0][0] = (*content).map[0][1];
    (*content).map[0][1] = (*content).map[1][1];
    (*content).map[1][1] = (*content).map[1][0];
    (*content).map[1][0] = t;
}

void flip2(pattern2* content)
{
    (*content).map[0][0] ^= (*content).map[0][1];
    (*content).map[0][1] ^= (*content).map[0][0];
    (*content).map[0][0] ^= (*content).map[0][1];
    (*content).map[1][0] ^= (*content).map[1][1];
    (*content).map[1][1] ^= (*content).map[1][0];
    (*content).map[1][0] ^= (*content).map[1][1];
}

int match3(pattern3 buffer, pattern3 mapping)
{
    int i;    
    for (i=0;i<4;i++)
    {
        if (!strncmp(buffer.map[0],mapping.map[0], 3) && !strncmp(buffer.map[1],mapping.map[1], 3)\
             && !strncmp(buffer.map[2],mapping.map[2], 3))
            return 1;
        rotate3(&buffer);
    }
    flip3(&buffer);
    for (i=0;i<4;i++)
    {
        if (!strncmp(buffer.map[0],mapping.map[0], 3) && !strncmp(buffer.map[1],mapping.map[1], 3)\
             && !strncmp(buffer.map[2],mapping.map[2], 3))
            return 1;
        rotate3(&buffer);
    }
    return 0; 
}

void rotate3(pattern3* content)
{
    char t1, t2;
    t1 = (*content).map[0][0];
    t2 = (*content).map[0][1];
    (*content).map[0][0] = (*content).map[0][2];
    (*content).map[0][1] = (*content).map[1][2];
    (*content).map[0][2] = (*content).map[2][2];
    (*content).map[1][2] = (*content).map[2][1];
    (*content).map[2][2] = (*content).map[2][0];
    (*content).map[2][1] = (*content).map[1][0];
    (*content).map[2][0] = t1;
    (*content).map[1][0] = t2;

}

void flip3(pattern3* content)
{
    (*content).map[0][0] ^= (*content).map[0][2];
    (*content).map[0][2] ^= (*content).map[0][0];
    (*content).map[0][0] ^= (*content).map[0][2];
    (*content).map[1][0] ^= (*content).map[1][2];
    (*content).map[1][2] ^= (*content).map[1][0];
    (*content).map[1][0] ^= (*content).map[1][2];
    (*content).map[2][0] ^= (*content).map[2][2];
    (*content).map[2][2] ^= (*content).map[2][0];
    (*content).map[2][0] ^= (*content).map[2][2];
}