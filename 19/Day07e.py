from itertools import permutations


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

def em_output(code, index, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    else:
        arg_0 = directValue(code, index + 1)
    return index + 2, arg_0

def em_input(code, index, par_str, signal):
    writeReference(code, index + 1, signal)
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

def emulate_amp(amp_code, signal, code, index):
    init = (index == 0)
    index = index
    while (index != -1):
        op_str = str(code[index]).zfill(5)
        op = int(op_str[3:])
        par_str = op_str[2::-1]
        if (op == 99):
            index = holding_index = -1
        elif (op == 8):
            index = em_equals(code, index, par_str)
        elif (op == 7):
            index = em_less_than(code, index, par_str)
        elif (op == 6):
            index = em_jump_if_false(code, index, par_str)
        elif (op == 5):
            index = em_jump_if_true(code, index, par_str)
        elif (op == 4):
            holding_index, signal = em_output(code, index, par_str)
            index = -1
        elif (op == 3):
            index = em_input(code, index, par_str, amp_code if init else signal)
            init = False
        elif (op == 2):
            index = em_multiplication(code, index, par_str)
        elif (op == 1):
            index = em_addition(code, index, par_str)
        else:
            index = holding_index = -1
    return holding_index, code, signal

def emulate_system_with_data(perm):
    signal = 0
    codes = [ground_intcode[:],ground_intcode[:],ground_intcode[:],ground_intcode[:],ground_intcode[:]]
    indices = [0,0,0,0,0]
    while (-1 not in indices):
        for amp in range(0, 5):
            indices[amp], codes[amp], signal = emulate_amp(perm[amp], signal, codes[amp], indices[amp])
    return signal




raw_intcode = input()
str_intcode = raw_intcode.split(',')
ground_intcode = list(map(int, str_intcode))



perms = list(permutations(range(5, 10)))

max_output = 0

for perm in perms:
    max_output = max(max_output, emulate_system_with_data(perm))

print(max_output)