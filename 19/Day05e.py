
def em_equals(code, index, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    else:
        arg_0 = directValue(code, index + 1)
    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    else:
        arg_1 = directValue(code, index + 2)
    writeReference(code, index + 3, 1 if arg_0 == arg_1 else 0)
    return (index + 4)

def em_less_than(code, index, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    else:
        arg_0 = directValue(code, index + 1)
    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    else:
        arg_1 = directValue(code, index + 2)
    writeReference(code, index + 3, 1 if arg_0 < arg_1 else 0)
    return (index + 4)

def em_jump_if_false(code, index, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    else:
        arg_0 = directValue(code, index + 1)
    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    else:
        arg_1 = directValue(code, index + 2)
    return arg_1 if arg_0 == 0 else index + 3

def em_jump_if_true(code, index, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    else:
        arg_0 = directValue(code, index + 1)
    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    else:
        arg_1 = directValue(code, index + 2)
    return arg_1 if arg_0 != 0 else index + 3

def em_output(code, index, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    else:
        arg_0 = directValue(code, index + 1)
    print(arg_0)
    return (index + 2)

def em_input(code, index, par_str):
    writeReference(code, index + 1, input())
    return (index + 2)

def em_multiplication(code, index, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    else:
        arg_0 = directValue(code, index + 1)
    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    else:
        arg_1 = directValue(code, index + 2)
    writeReference(code, index + 3, arg_0*arg_1)
    return (index + 4)

def em_addition(code, index, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    else:
        arg_0 = directValue(code, index + 1)
    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    else:
        arg_1 = directValue(code, index + 2)
    writeReference(code, index + 3, arg_0 + arg_1)
    return (index + 4)

def directValue(code, index):
    return int(code[index])

def referencedValue(code, index):
    return int(code[code[index]])

def writeReference(code, index, value):
    code[code[index]] = value

def emulate(code, index):
    op_str = str(code[index]).zfill(5)
    op = int(op_str[3:])
    par_str = op_str[2::-1]
    if (op == 99):
        index = -1
    elif (op == 8):
        index = em_equals(code, index, par_str)
    elif (op == 7):
        index = em_less_than(code, index, par_str)
    elif (op == 6):
        index = em_jump_if_false(code, index, par_str)
    elif (op == 5):
        index = em_jump_if_true(code, index, par_str)
    elif (op == 4):
        index = em_output(code, index, par_str)
    elif (op == 3):
        index = em_input(code, index, par_str)
    elif (op == 2):
        index = em_multiplication(code, index, par_str)
    elif (op == 1):
        index = em_addition(code, index, par_str)
    else:
        index = -1
    return index

raw_intcode = input()
str_intcode = raw_intcode.split(',')
intcode = list(map(int, str_intcode))

i = 0

while (i != -1):
    i = emulate(intcode, i)
