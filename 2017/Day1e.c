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
    int l = 0;
    int h, i;
    char* anchor = point;
    while(*point)
    {
        point++;
        l++;
    }
    h = l/2;
    for(i=0;i<l;i++)
    {
        if(anchor[i]==anchor[((i+h)%l)])
            s += anchor[i] - 48;
    }    
    return s;
}