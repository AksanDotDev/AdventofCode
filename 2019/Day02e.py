target = int(input())
raw_intcode = input()
str_intcode = raw_intcode.split(',')
intcode_base = list(map(int, str_intcode))
for n in range(0, 99):
    for v in range(0, 99):
        intcode = list(intcode_base)
        intcode[1] = n
        intcode[2] = v

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
        if (intcode[0] == target):
            break
    if(intcode[0] == target):
        break
        

print(n * 100 + v)