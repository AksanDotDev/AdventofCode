#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define SIZE    26


typedef struct instruction{
    int opcode;
    long long int op1;
    long long int op2;
} instruction;


instruction* program;
long long int* registers;
// 01 snd val
// 02 snd reg
// 03 set reg, val
// 04 set reg, reg
// 05 add reg, val
// 06 add reg, reg
// 07 mul reg, val
// 08 mul reg, reg
// 09 mod reg, val
// 10 mod reg, reg
// 11 rcv val
// 12 rcv reg
// 13 jgz val, val 
// 14 jgz val, reg
// 15 jgz reg, val
// 16 jgz reg, reg


int runner(FILE*);
int execute(int l);

int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    if (!f)
    {
        fprintf(stderr, "File open failed\n");
        exit(1);
    }
    int l;
    registers = calloc(SIZE,sizeof(long long int));
    if (!registers)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    l = runner(f);
    fclose(f);
    printf("%d\n", execute(l));
}

int runner(FILE* f)
{
    int i, l, t;
    long int x, y;
    char a, b;
    char buffer[64];
    l = 0;
    while(!feof(f))
    {
        fgets(buffer,512,f);
        l++;
    }
    program = malloc(l*sizeof(instruction));
    if (!program)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    } 
    rewind(f);
    for (i=0;i<l;i++)
    {
        fgets(buffer,64,f);
        switch (buffer[0])
        {
            case 's' :
                t = sscanf(buffer,"snd %ld", &x);
                if (t == 1)
                {
                    program[i].opcode = 1;
                    program[i].op1 = x;
                    break;
                }
                t = sscanf(buffer,"snd %c", &a);
                if (t == 1)
                {
                    program[i].opcode = 2;
                    program[i].op1 = (int)(a - 'a');
                    break;
                }
                t = sscanf(buffer,"set %c %ld", &a, &y);
                if (t == 2)
                {
                    program[i].opcode = 3;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (y);
                    break;
                }
                t = sscanf(buffer,"set %c %c", &a, &b);
                if (t == 2)
                {
                    program[i].opcode = 4;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (int)(b - 'a');
                    break;
                }
                fprintf(stderr, "Unparsed Command 's': %s\n", buffer);
                break;
            case 'a' :
                t = sscanf(buffer,"add %c %ld", &a, &y);
                if (t == 2)
                {
                    program[i].opcode = 5;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (y);
                    break;
                }
                t = sscanf(buffer,"add %c %c", &a, &b);
                if (t == 2)
                {
                    program[i].opcode = 6;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (int)(b - 'a');
                    break;
                }
                fprintf(stderr,"Unparsed Command 'a': %s\n", buffer);
                break;
            case 'm' :
                t = sscanf(buffer,"mul %c %ld", &a, &y);
                if (t == 2)
                {
                    program[i].opcode = 7;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = y;
                    break;
                }
                t = sscanf(buffer,"mul %c %c", &a, &b);
                if (t == 2)
                {
                    program[i].opcode = 8;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (int)(b - 'a');
                    break;
                }
                t = sscanf(buffer,"mod %c %ld", &a, &y);
                if (t == 2)
                {
                    program[i].opcode = 9;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (y);
                    break;
                }
                t = sscanf(buffer,"mod %c %c", &a, &b);
                if (t == 2)
                {
                    program[i].opcode = 10;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (int)(b - 'a');
                    break;
                }
                fprintf(stderr, "Unparsed Command 'm': %s\n", buffer);
                break;
            case 'r' :
                t = sscanf(buffer,"rcv %ld", &x);
                if (t == 1)
                {
                    program[i].opcode = 11;
                    program[i].op1 = (x);
                    break;
                }
                t = sscanf(buffer,"rcv %c", &a);
                if (t == 1)
                {
                    program[i].opcode = 12;
                    program[i].op1 = (int)(a - 'a');
                    break;
                }
                fprintf(stderr,"Unparsed Command 'r': %s\n", buffer);
                break;
            case 'j' :
                t = sscanf(buffer,"jgz %ld %ld", &x, &y);
                if (t == 2)
                {
                    program[i].opcode = 13;
                    program[i].op1 = (x);
                    program[i].op2 = (y);
                    break;
                }
                t = sscanf(buffer,"jgz %ld %c", &x, &b);
                if (t == 2)
                {
                    program[i].opcode = 14;
                    program[i].op1 = (x);
                    program[i].op2 = (int)(b - 'a');
                    break;
                }
                t = sscanf(buffer,"jgz %c %ld", &a, &y);
                if (t == 2)
                {
                    program[i].opcode = 15;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (y);
                    break;
                }
                t = sscanf(buffer,"jgz %c %c", &a, &b);
                if (t == 2)
                {
                    program[i].opcode = 16;
                    program[i].op1 = (int)(a - 'a');
                    program[i].op2 = (int)(b - 'a');
                    break;
                }
                fprintf(stderr,"Unparsed Command 'j': %s\n", buffer);
                break;
            default :
                fprintf(stderr,"Unparsed Command '*': %s\n", buffer);
                break;
        }
    }
    return l;
}

int execute(int l)
{
    int pc, lp;
    lp = -1;
    pc = 0;
    while(1)
    {
        switch (program[pc].opcode)
        {
            case 1 : //snd val
                lp = program[pc].op1;
                break;
            case 2 : //snd reg
                lp = registers[program[pc].op1];
                break;
            case 3 : //set reg, val
                registers[program[pc].op1] = program[pc].op2;
                break;
            case 4 : //set reg, reg
                registers[program[pc].op1] = registers[program[pc].op2];
                break;
            case 5 : //add reg, val
                registers[program[pc].op1] += program[pc].op2;
                break;
            case 6 : //add reg, reg
                registers[program[pc].op1] += registers[program[pc].op2];
                break;
            case 7 : //mul reg, val
                registers[program[pc].op1] *= program[pc].op2;
                break;
            case 8 : //mul reg, reg
                registers[program[pc].op1] *= registers[program[pc].op2];
                break;
            case 9 : //mod reg, val
                registers[program[pc].op1] %= program[pc].op2;
                if (registers[program[pc].op1] * program[pc].op2 < 0)
                    registers[program[pc].op1] += program[pc].op2;
                break;
            case 10 : //mod reg, reg
                registers[program[pc].op1] %= registers[program[pc].op2];
                if (registers[program[pc].op1] * registers[program[pc].op2] < 0)
                    registers[program[pc].op1] += registers[program[pc].op2];
                break;
            case 11 : //rcv val
                if(program[pc].op1)
                    return(lp);
                break;
            case 12 : //rcv reg
                if(registers[program[pc].op1])
                    return(lp);
                break;
            case 13 : //jgz val, val
                if(program[pc].op1 > 0)
                    pc += (program[pc].op2 - 1);
                break;
            case 14 : //jgz val, reg
                if(program[pc].op1 > 0)
                    pc += (registers[program[pc].op2] - 1);
                break;
            case 15 : //jgz reg, val
                if(registers[program[pc].op1] > 0)
                    pc += (program[pc].op2 - 1);
                break;
            case 16 : //jgz reg, reg
                if(registers[program[pc].op1] > 0)
                    pc += (registers[program[pc].op2] - 1);
                break;
            default :
                fprintf(stderr, "Corrupted Command: %d\n", program[pc].opcode);
                break;
        }
        pc++;
    }
    return -1;
}
