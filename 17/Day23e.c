#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_MAX 1000000

int main(int argc, char** argv)
{
    int i, l, r, c;
    int a[499999];
    int *p1, *p2, *pl;
    l = strtol(argv[1], NULL, 10);
    l *= 100;
    l += 100000;
    r = l;
    r += 17000;
    c = 0;
    pl = a+((r-1)>>1);
    for(p1 = a, i=3;(*p1=i)<r;i+=2,p1++);
    for(p1 = a;p1<pl;p1++)
    {
        if((*p1) != 0)
        {
            if((*p1) >= l && !((*p1 - l) % 17))
            {
                c++;
            }
            for(p2=p1+*p1;p2<pl;p2+=*p1)
                *p2 = 0;
        }
    }  
    printf("%d\n", 1001-c); 
    return 0;
}
