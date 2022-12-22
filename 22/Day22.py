import sys


with open(sys.argv[1]) as file:
    raw = file.readlines()

board = dict()
limits = (0, len(raw) - 2)

for i, line in enumerate(raw[:-2]):
    limits = (max(limits[0], len(line)), limits[1])
    for j, char in enumerate(line[:-1]):
        if char == " ":
            board[(j, i)] = 0
        elif char == ".":
            board[(j, i)] = 1
        elif char == "#":
            board[(j, i)] = 2
        else:
            raise Exception("Panic!")


def get_next_tile(x, y, d):
    if d == 0:
        if board.get((x + 1, y), 0) == 0:
            i = 0
            while board.get((i, y), 0) == 0:
                i += 1
            if board[(i, y)] == 1:
                return (i, y)
            elif board[(i, y)] == 2:
                return False
            else:
                raise Exception("Panic")
        elif board[(x + 1, y)] == 1:
            return (x + 1, y)
        elif board[(x + 1, y)] == 2:
            return False
        else:
            raise Exception("Panic")
    elif d == 1:
        if board.get((x, y + 1), 0) == 0:
            i = 0
            while board.get((x, i), 0) == 0:
                i += 1
            if board[(x, i)] == 1:
                return (x, i)
            elif board[(x, i)] == 2:
                return False
            else:
                raise Exception("Panic")
        elif board[(x, y + 1)] == 1:
            return (x, y + 1)
        elif board[(x, y + 1)] == 2:
            return False
        else:
            raise Exception("Panic")
    if d == 2:
        if board.get((x - 1, y), 0) == 0:
            i = limits[0]
            while board.get((i, y), 0) == 0:
                i -= 1
            if board[(i, y)] == 1:
                return (i, y)
            elif board[(i, y)] == 2:
                return False
            else:
                raise Exception("Panic")
        elif board[(x - 1, y)] == 1:
            return (x - 1, y)
        elif board[(x - 1, y)] == 2:
            return False
        else:
            raise Exception("Panic")
    elif d == 3:
        if board.get((x, y - 1), 0) == 0:
            i = limits[1]
            while board.get((x, i), 0) == 0:
                i -= 1
            if board[(x, i)] == 1:
                return (x, i)
            elif board[(x, i)] == 2:
                return False
            else:
                raise Exception("Panic")
        elif board[(x, y - 1)] == 1:
            return (x, y - 1)
        elif board[(x, y - 1)] == 2:
            return False
        else:
            raise Exception("Panic")
    else:
        raise Exception("Panic")


def tokenize_ins(ins):
    t_ins = []
    for ele in ins:
        if ele.isdigit():
            if t_ins and isinstance(t_ins[-1], int):
                t_ins[-1] *= 10
                t_ins[-1] += int(ele)
            else:
                t_ins.append(int(ele))
        else:
            t_ins.append(ele)
    return t_ins


instructions = tokenize_ins(raw[-1])

d = 0
loc = get_next_tile(0, 0, d)

for ins in instructions:
    if ins == "R":
        d = 0 if d == 3 else d + 1
    elif ins == "L":
        d = 3 if d == 0 else d - 1
    elif isinstance(ins, int):
        for _ in range(ins):
            if pot := get_next_tile(*loc, d):
                loc = pot
            else:
                break


def get_result(x, y, d):
    return ((y + 1) * 1000) + ((x + 1) * 4) + d


print(get_result(*loc, d))
