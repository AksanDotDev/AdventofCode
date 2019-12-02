raw_intcode = input()
str_intcode = raw_intcode.split(',')
intcode = list(map(int, str_intcode))
intcode[1] = 12
intcode[2] = 2

for i in range(0, len(intcode), 4):
    op = intcode[i]
    if (op == 99):
        break
    la = intcode[intcode[i+1]]
    lr = intcode[intcode[i+2]]
    ta = intcode[i+3]
    if (op == 2):
        intcode[ta] = la * lr
    elif (op == 1):
        intcode[ta] = la + lr
    else:
        print("Invalid code" + op)

print(intcode[0])