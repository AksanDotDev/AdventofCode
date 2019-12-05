raw_intcode = input()
str_intcode = raw_intcode.split(',')
intcode = list(map(int, str_intcode))

processing = True
i = 0

while processing:
    op = intcode[i]
    op_str = str(op).zfill(5)
    op = int(op_str[3:])
    if (op == 99):
        print("halt")
        processing = False
    elif (op == 4):
        if (op_str[2] == '0'):
            sa = int(intcode[intcode[i+1]])
        else:
            sa = int(intcode[i+1])
        print(sa)
        i += 2
    elif (op == 3):
        input_IO = input()
        tl = intcode[i+1]
        intcode[tl] = input_IO
        i += 2
    else:
        if (op_str[2] == '0'):
            la = int(intcode[intcode[i+1]])
        else:
            la = int(intcode[i+1])
        if (op_str[1] == '0'):
            ra = int(intcode[intcode[i+2]])
        else:
            ra = int(intcode[i+2])
        op = int(op_str[3:])
        if (op == 2):
            ov = la*ra
        elif (op == 1):
            ov = la+ra
        tl = intcode[i+3]
        intcode[tl] = ov
        i += 4