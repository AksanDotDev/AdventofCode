from collections import defaultdict, Counter
from time import sleep
from random import randint

def em_adjust_base(code, index, base, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)

    return (index + 2), (base + arg_0)

def em_equals(code, index, base, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)
    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    elif (par_str[1] == '2'):
        arg_1 = relativeValue(code, index + 2, base)
    else:
        arg_1 = directValue(code, index + 2)

    if (par_str[2] =='0'):
        writeReference(code, index + 3, 1 if arg_0 == arg_1 else 0)
    else:
        writeRelative(code, index + 3, base, 1 if arg_0 == arg_1 else 0)

    return (index + 4), base

def em_less_than(code, index, base, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)
    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    elif (par_str[1] == '2'):
        arg_1 = relativeValue(code, index + 2, base)
    else:
        arg_1 = directValue(code, index + 2)

    if (par_str[2] =='0'):
        writeReference(code, index + 3, 1 if arg_0 < arg_1 else 0)
    else:
        writeRelative(code, index + 3, base, 1 if arg_0 < arg_1 else 0)

    return (index + 4), base

def em_jump_if_false(code, index, base, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)

    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    elif (par_str[1] == '2'):
        arg_1 = relativeValue(code, index + 2, base)
    else:
        arg_1 = directValue(code, index + 2)
    return (arg_1 if arg_0 == 0 else index + 3), base

def em_jump_if_true(code, index, base, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)

    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    elif (par_str[1] == '2'):
        arg_1 = relativeValue(code, index + 2, base)
    else:
        arg_1 = directValue(code, index + 2)

    return (arg_1 if arg_0 != 0 else index + 3), base

def em_output(code, index, base, par_str, log):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)

    move, placeholder = log[-1]
    log[-1] = (move, arg_0)
    count = process(log)
    if arg_0 == 2 :
        print(count)
        exit()
    return (index + 2), base

def em_input(code, index, base, par_str, log):
    move, placeholder = log[-1]

    if (par_str[2] =='0'):
        writeReference(code, index + 1, move)
    else:
        writeRelative(code, index + 1, base, move)

    return (index + 2), base

def em_multiplication(code, index, base, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)

    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    elif (par_str[1] == '2'):
        arg_1 = relativeValue(code, index + 2, base)
    else:
        arg_1 = directValue(code, index + 2)

    if (par_str[2] =='0'):
        writeReference(code, index + 3, arg_0*arg_1)
    else:
        writeRelative(code, index + 3, base, arg_0*arg_1)

    return (index + 4), base

def em_addition(code, index, base, par_str):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)

    if (par_str[1] == '0'):
        arg_1 = referencedValue(code, index + 2)
    elif (par_str[1] == '2'):
        arg_1 = relativeValue(code, index + 2, base)
    else:
        arg_1 = directValue(code, index + 2)

    if (par_str[2] =='0'):
        writeReference(code, index + 3, arg_0 + arg_1)
    else:
        writeRelative(code, index + 3, base, arg_0 + arg_1)

    return (index + 4), base

def directValue(code, index):
    return int(code[index])

def referencedValue(code, index):
    return int(code[code[index]])

def relativeValue(code, index, base):
    return int(code[base + code[index]])

def writeReference(code, index, value):
    code[code[index]] = value

def writeRelative(code, index, base, value):
    code[base + code[index]] = value

def process(log):
    map = defaultdict(lambda: ' ')
    crumbs = 0
    x_loc = 0
    y_loc = 0
    for move, result in log:
        if int(move) == 1:
            x_pot = x_loc
            y_pot = y_loc - 1
        elif int(move) == 2:
            x_pot = x_loc
            y_pot = y_loc + 1
        elif int(move) == 3:
            x_pot = x_loc - 1
            y_pot = y_loc
        elif int(move) == 4:
            x_pot = x_loc + 1
            y_pot = y_loc
        else:
            print("Bad move")
            exit()
        if int(result) == 0:
            map[(x_pot, y_pot)] = '█'
        elif int(result) == 1:
            if map[(x_pot, y_pot)] == '°':
                map[(x_loc, y_loc)] = '■'
                crumbs -= 1
            else:
                map[(x_pot, y_pot)] = '°'
                crumbs += 1
            x_loc = x_pot
            y_loc = y_pot
        else:
            map[(x_pot, y_pot)] = 'O'
            crumbs += 1
    options = [map[(x_loc, y_loc - 1)], map[(x_loc, y_loc + 1)], map[(x_loc - 1, y_loc)], map[(x_loc + 1, y_loc)]]
    try:
        next = options.index(' ') + 1
    except ValueError:
        next = options.index('°') + 1
    finally:
        log.append((next, -1))
    return crumbs


def emulate(code, index, base, log):
    op_str = str(code[index]).zfill(5)
    op = int(op_str[3:])
    par_str = op_str[2::-1]
    if (op == 99):
        index = -1
    elif (op == 9):
        index, base = em_adjust_base(code, index, base, par_str)
    elif (op == 8):
        index, base = em_equals(code, index, base, par_str)
    elif (op == 7):
        index, base = em_less_than(code, index, base, par_str)
    elif (op == 6):
        index, base = em_jump_if_false(code, index, base, par_str)
    elif (op == 5):
        index, base = em_jump_if_true(code, index, base, par_str)
    elif (op == 4):
        index, base = em_output(code, index, base, par_str, log)
    elif (op == 3):
        index, base = em_input(code, index, base, par_str, log)
    elif (op == 2):
        index, base = em_multiplication(code, index, base, par_str)
    elif (op == 1):
        index, base = em_addition(code, index, base, par_str)
    else:
        print(">>><<<")
        index = -1
    return index, base

raw_intcode = input()
str_intcode = raw_intcode.split(',')
intcode = list(map(int, str_intcode))
for i in range (0,1024):
    intcode.append(0)


i = 0
b = 0
l = [(1,-1)]
while (i != -1):
    i, b = emulate(intcode, i, b, l)

