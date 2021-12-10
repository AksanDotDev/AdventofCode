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

def em_output(code, index, base, par_str, map):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)

    setResult(map, arg_0)
    return (index + 2), base

def em_input(code, index, base, par_str, map):
    move = getMove(map)

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

def getMove(map):
    moves = defaultdict(lambda:0)
    if getUnex(map):
        return map["LGM"]
    else:
        print(floodFill(map))
        exit()

def setResult(map, result):
    x, y = map["LOC"]
    m = map["LGM"]

    if int(m) == 1:
        x_pot = x
        y_pot = y - 1
    elif int(m) == 2:
        x_pot = x
        y_pot = y + 1
    elif int(m) == 3:
        x_pot = x - 1
        y_pot = y
    elif int(m) == 4:
        x_pot = x + 1
        y_pot = y

    if int(result) == 0:
        map[(x_pot, y_pot)] = '█'
    elif int(result) == 1:
        map[(x_pot, y_pot)] = '°'
        x = x_pot
        y = y_pot
    else:
        map[(x_pot, y_pot)] = 'O'
        x = x_pot
        y = y_pot
    
    map["LOC"] = (x,y)
    x_min, y_min, x_max, y_max = map["LIM"]
    map["LIM"] = (min(x, x_min), min(y, y_min), max(x, x_max), max(y, y_max))

def getUnex(map):
    x, y = map["LOC"]
    searchSpace = defaultdict(lambda: -1)
    searchSpace[(x,y)] = (0, [])
    searching = True
    while searching:
        searching = False
        iterSpace = list(searchSpace.keys())
        for loc in iterSpace:
            search, route = searchSpace[loc]
            if search == 0:
                searchSpace[loc] = (1, route)
                x_ser, y_ser = loc
                for d in range(1,5):
                    if d == 1:
                        x_pot = x_ser
                        y_pot = y_ser - 1
                    elif d == 2:
                        x_pot = x_ser
                        y_pot = y_ser + 1
                    elif d == 3:
                        x_pot = x_ser - 1
                        y_pot = y_ser
                    elif d == 4:
                        x_pot = x_ser + 1
                        y_pot = y_ser
                    route_pot = route[:]
                    route_pot.append(d)
                    if map[(x_pot, y_pot)] == ' ':
                        map["LGM"] = route_pot[0]
                        return True
                    elif map[(x_pot, y_pot)] != '█' and searchSpace[(x_pot, y_pot)] == -1:
                        searchSpace[(x_pot,y_pot)] = (0,route_pot)
                        searching = True
    return False

            
def neighbours(x, y, map):
    return [map[(x-1, y)], map[(x+1,y)], map[(x,y-1)], map[(x,y+1)]]


def floodFill(map):
    x_min, y_min, x_max, y_max = map["LIM"]
    minutes = 0
    while '°' in map.values():
        for i in range (y_min, y_max + 1):
            for j in range (x_min, x_max + 1):
                if 'O' in neighbours(j, i, map) and map[(j,i)] == '°':
                    map[(j,i)] = 'o'
        for i in range (y_min, y_max + 1):
            for j in range (x_min, x_max + 1):
                if map[(j,i)] == 'o':
                    map[(j,i)] = 'O'
       
        minutes += 1
    return minutes
    

def emulate(code, index, base, map):
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
        index, base = em_output(code, index, base, par_str, map)
    elif (op == 3):
        index, base = em_input(code, index, base, par_str, map)
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
m = defaultdict(lambda: ' ')
m['LOC'] = (0,0)
m['LIM'] = (0,0,0,0)
m[(0,0)] = '°'
while (i != -1):
    i, b = emulate(intcode, i, b, m)

