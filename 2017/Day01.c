#include <stdio.h>

int runner(char*);
int main(int argc, char** argv)
{
    int a = runner(argv[1]);
    printf("%d", a);
    return 0;
}

int runner(char* point)
{
    int s = 0;
    char h = *point;
    while(point[1])
    {
        if (point[0] == point[1])
            s += (*point-48);
        point++;
    }
    if (*point == h)
        s += (*point-48);
    return s;
}