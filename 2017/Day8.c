#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define INITSIZE 128

typedef struct VirtRegister
{
    char name[4];
    int value;
}
VirtRegister;

VirtRegister *init_registers(int*);
void expand_registers(VirtRegister*, int*);
int find_register(VirtRegister*, char*, int*);
int test_register(VirtRegister*, char*, int, int);
int runner(FILE*);

int main(int argc, char** argv)
{
    FILE* f = fopen(argv[1], "r");
    printf("%d\n", runner(f));
    fclose(f);
    return 0;
}

int runner(FILE* f)
{
    char reg[8];
    char op[8];
    int opn, con, lim, regi, cori, max, i;
    char coreg[8];
    char cond[8];
    char* b = (char*)malloc(128);
    VirtRegister *regbank = init_registers(&lim);
    while(!feof(f))
    {
        fgets(b, 128, f);
        sscanf(b,"%s %s %d if %s %s %d", reg, op, &opn, coreg, cond, &con);
        cori = find_register(regbank, coreg, &lim);
        if (test_register(regbank, cond, cori, con))
        {
            regi = find_register(regbank, reg, &lim);
            if (!strcmp(op,"inc"))
                regbank[regi].value += opn;
            else 
                regbank[regi].value -= opn;
        }
    }
    for (i=0,max=0;i<lim;i++)
        if (regbank[i].value>max)
            max = regbank[i].value;
    free(regbank);
    free (b);
    return max;
}

VirtRegister *init_registers(int *lim)
{
    int i;
    VirtRegister *regbank = (VirtRegister*)malloc(INITSIZE*sizeof(VirtRegister));
    *lim = INITSIZE;
    if (!regbank)
    {
        fprintf(stderr, "Error in malloc.\n");
        exit(1);
    }
    for (i=0;i<*lim;i++)
    {
        strcpy(regbank[i].name,"");
        regbank[i].value = 0;
    }
    return regbank;
}

void expand_registers(VirtRegister *regbank, int *lim)
{
    int i;
    *lim *= 2;
    regbank = (VirtRegister*)realloc(regbank, (*lim)*sizeof(VirtRegister));
    if (!regbank)
    {
        fprintf(stderr, "Error in realloc.\n");
        exit(1);
    }
    for (i=*lim/2;i<*lim;i++)
    {
        strcpy(regbank[i].name,"");
        regbank[i].value = 0;
    }
}

int find_register(VirtRegister *regbank, char *target, int *lim)
{
    int i = 0;
    while (strcmp(regbank[i].name,"") && i<*lim)
    {
        if (!strcmp(regbank[i].name,target))
            return i;
        i++;
    }
    if (i==*lim)
        expand_registers(regbank, lim);
    strcpy(regbank[i].name,target);
    return i;
}

int test_register(VirtRegister* regbank, char* cond, int cori, int con)
{
    if (!strcmp(cond,">"))
        return (regbank[cori].value > con);
    if (!strcmp(cond,"<"))
        return (regbank[cori].value < con);
    if (!strcmp(cond,">="))
        return (regbank[cori].value >= con);
    if (!strcmp(cond,"<="))
        return (regbank[cori].value <= con);
    if (!strcmp(cond,"=="))
        return (regbank[cori].value == con);
    return (regbank[cori].value != con);
}