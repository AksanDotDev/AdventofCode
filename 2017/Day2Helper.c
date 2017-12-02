#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void runner(FILE*, FILE*);
int main(int argc, char** argv)
{
    FILE *input = fopen("Day2Input", "r");
    FILE *output = fopen("Day2InputClean", "w");    
    runner(output, input);
    fclose(input);
    fclose(output);
    return 0;
}
void runner(FILE* output, FILE* input)
{
    char c;
    while(!feof(input))
    {
        c = fgetc(input);
        if(c == '\t' || c=='\n')
            fputc(' ',output);
        else
            fputc(c,output);
    }
}