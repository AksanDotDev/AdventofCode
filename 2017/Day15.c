#include <stdio.h>
#include <stdlib.h>

#define FACTOR_A    16807
#define FACTOR_B    48271
#define R_DIVIDER   2147483647
#define JUDGE_C     40000000

int runner(unsigned long long, unsigned long long);
int main(int argc, char** argv)
{
    unsigned long long a = strtol(argv[1], NULL, 10);
    unsigned long long b = strtol(argv[2], NULL, 10);
    printf("%d", runner(a, b));
    return 0;
}

int runner(unsigned long long a, unsigned long long b)
{
    int i, s;
    s = 0; 
    for (i=0;i<JUDGE_C;i++)
    {
        a = (a * FACTOR_A) % R_DIVIDER;
        b = (b * FACTOR_B) % R_DIVIDER;
        if ((a & 65535) == (b & 65535))
            s++;
    }
    return s;
}