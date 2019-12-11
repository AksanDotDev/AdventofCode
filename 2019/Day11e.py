from collections import defaultdict

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

def em_output(code, index, base, par_str, painting, canvas):
    if (par_str[0] == '0'):
        arg_0 = referencedValue(code, index + 1)
    elif (par_str[0] == '2'):
        arg_0 = relativeValue(code, index + 1, base)
    else:
        arg_0 = directValue(code, index + 1)

    if (painting):
        paint(arg_0, canvas)
        painting = False
    else:
        move(arg_0, canvas)
        painting = True
    
    return (index + 2), base, painting, canvas

def em_input(code, index, base, par_str, canvas):
    if (par_str[2] =='0'):
        writeReference(code, index + 1, observe(canvas))
    else:
        writeRelative(code, index + 1, base, observe(canvas))
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

def paint(colour, canvas):
    x, y, d = canvas["loc"]
    canvas["("+str(x)+","+str(y)+")"] = '█' if (int(colour) == 0) else ' '

def move(direction, canvas):
    x, y, d = canvas["loc"]
    d = (d + (1 if int(direction) == 1 else -1)) % 4
    if (d == 0):
        y -= 1
    elif (d == 1):
        x += 1
    elif (d == 2):
        y += 1
    elif (d == 3):
        x -= 1
    canvas["loc"] = (x, y, d)

def observe(canvas):
    x, y, d = canvas["loc"]
    return 1 if (canvas["("+str(x)+","+str(y)+")"] == ' ') else 0
    

def emulate(code, index, base, painting, canvas):
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
        index, base, painting, canvas = em_output(code, index, base, par_str, painting, canvas)
    elif (op == 3):
        index, base = em_input(code, index, base, par_str, canvas)
    elif (op == 2):
        index, base = em_multiplication(code, index, base, par_str)
    elif (op == 1):
        index, base = em_addition(code, index, base, par_str)
    else:
        print(">>><<<")
        index = -1
    return index, base, painting, canvas

def canvasPrint(canvas):
    for i in range(-1, 7):
        for j in range(0, 41):
            print(canvas["("+str(j)+","+str(i)+")"], end='')
        print()

raw_intcode = input()
str_intcode = raw_intcode.split(',')
intcode = list(map(int, str_intcode))
for i in range (0,1024):
    intcode.append(0)

i = 0
b = 0
p = True
c = defaultdict(lambda: '█')
c["loc"] = (0,0,0)
c["(0,0)"] = ' '
while (i != -1):
    i, b, p, c = emulate(intcode, i, b, p, c)

canvasPrint(c)