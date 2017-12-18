#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <windows.h>
#include <process.h> 

#define SIZE    26
#define QUEUESIZE   2048


typedef struct instruction{
    int opcode;
    long long int op1;
    long long int op2;
} instruction;

typedef struct setup{
    long long int* r;
    long long int* qsnd;
    long long int* qrcv;
    int l;    
} setup;

instruction* program;
long long int* registersp0;
long long int* registersp1;
long long int* queuetop0;
long long int* queuetop1;
HANDLE  hReceiving;   //rcv Mutex
HANDLE  hEdit; //edt Mutex
int killswitch = 0;
int totsnd = 0;



int runner(FILE*);
void execute(void* r);
void sndr(long long int, long long int*);
long long int rcvr(long long int*);

int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    setup init0, init1;
    if (!f)
    {
        fprintf(stderr, "File open failed\n");
        exit(1);
    }
    registersp0 = calloc(SIZE,sizeof(long long int));
    registersp1 = calloc(SIZE,sizeof(long long int));
    queuetop0 = malloc(QUEUESIZE*sizeof(long long int));
    queuetop1 = malloc(QUEUESIZE*sizeof(long long int));
    if (!registersp0 || !registersp1 || !queuetop0 || !queuetop1)
    {
        fprintf(stderr, "Malloc failed\n");
        exit(1);
    }
    registersp1[15] = 1;
    init0.r = registersp0;
    init1.r = registersp1;
    init0.qsnd = init1.qrcv = queuetop1;
    init1.qsnd = init0.qrcv = queuetop0;
    queuetop0[0] = queuetop1[0] = 0;
    hReceiving = CreateMutex (NULL, FALSE, NULL);
    hEdit = CreateMutex (NULL, FALSE, NULL);
    init0.l = init1.l = runner(f);
    fclose(f);
    _beginthread(execute, 0, &init0);
    _beginthread(execute, 0, &init1);
    while(!killswitch);
    printf("%d\n", totsnd);
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

void execute(void* init)
{
    int pc, t, l;
    pc = 0;
    long long int* registers = ((setup*)init) -> r;
    long long int* snd = ((setup*)init) -> qsnd;
    long long int* rcv = ((setup*)init) -> qrcv;
    l = (((setup*)init) -> l - 1);
    while(1)
    {
        switch (program[pc].opcode)
        {
            case 1 : //snd val
                //totsnd++;
                sndr(program[pc].op1, snd);
                break;
            case 2 : //snd reg
                //totsnd++;
                sndr(registers[program[pc].op1], snd);
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
                t = (int)WaitForSingleObject(hReceiving,1000);
                if (t == WAIT_TIMEOUT)
                {
                    killswitch = 1;
                    _endthread();
                }
                registers[program[pc].op1] = rcvr(rcv);
                ReleaseMutex(hReceiving);
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
        if (pc < 0 || pc > l)
        {
            killswitch = 1;
            _endthread();
        }
        if (killswitch)
            _endthread();
    }
    return;
}

void sndr(long long int pkg, long long int* qts)
{
    if (qts == queuetop0)
        totsnd++;
    WaitForSingleObject(hEdit,INFINITE);
    qts[0]++;
    qts[qts[0]] = pkg;
    ReleaseMutex(hEdit);
    return;
}

long long int rcvr(long long int* qtr)
{
    int i;
    long long int pkg;
    while (1)
    {
        if (qtr[0])
            break;
        Sleep(10);
    } 
    WaitForSingleObject(hEdit,INFINITE);  
    pkg = qtr[1];
    for (i=1;i<qtr[0];i++)
        qtr[i] = qtr[i+1];
    qtr[0]--;
    ReleaseMutex(hEdit);
    return pkg;
}
