#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define SIZE 0xFFFFFFFF
#define STEP 12861455

char* tape;


int execute(void);

int main(int argc, char** argv)
{

    tape = calloc(SIZE,1);
    if (!tape)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    printf("%d\n", execute());
    return 0;
}

int execute(void)
{
    long int sc, cu;
    char st = 0;
    cu = SIZE/2;
    for (sc=0;sc<STEP;sc++)
    {
        switch (tape[cu]+st*2)
        {
            case 0 : // A 0
                tape[cu] = 1;
                cu++;
                st = 1;
                break;
            case 1 : // A 1
                tape[cu] = 0;
                cu--;
                st = 1;
                break;
            case 2 : // B 0
                tape[cu] = 1;
                cu--;
                st = 2;
                break;
            case 3 : // B 1
                tape[cu] = 0;
                cu++;
                st = 4;
                break;
            case 4 : // C 0
                tape[cu] = 1;
                cu++;
                st = 4;
                break;
            case 5 : // C 1
                tape[cu] = 0;
                cu--;
                st = 3;
                break;
            case 6 : // D 0
                tape[cu] = 1;
                cu--;
                st = 0;
                break;
            case 7 : // D 1
                tape[cu] = 1;
                cu--;
                st = 0;
                break;
            case 8 : // E 0
                tape[cu] = 0;
                cu++;
                st = 0;
                break;
            case 9 : // E 1
                tape[cu] = 0;
                cu++;
                st = 5;
                break;
            case 10 : // F 0
                tape[cu] = 1;
                cu++;
                st = 4;
                break;
            case 11 : // F 1
                tape[cu] = 1;
                cu++;
                st = 0;
                break;
            default :
                fprintf(stderr, "Corrupted State: %d\n", st);
                break;
        }
        if (cu < 0 || cu == SIZE)
        {
            printf("Tape is finite.\n");
            exit(1);
        }
    }
    sc = 0;
    for (cu=0;cu<SIZE;cu++)
        sc += tape[cu];
    return sc;
}
