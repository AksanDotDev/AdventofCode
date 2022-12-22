import sys
from functools import cache


with open(sys.argv[1]) as file:
    raw = file.readlines()

board = dict()
limits = (0, len(raw) - 2)

for i, line in enumerate(raw[:-2]):
    limits = (max(limits[0], len(line) - 1), limits[1])
    for j, char in enumerate(line[:-1]):
        if char == ".":
            board[(j, i)] = 1
        elif char == "#":
            board[(j, i)] = 2

side = 50
limits = (limits[0] - 1, limits[1] - 1)


def get_face(x, y):
    f_x = x // side
    f_y = y // side
    if f_y == 0:
        if f_x == 1:
            return 1
        elif f_x == 2:
            return 2
    elif f_y == 1 and f_x == 1:
        return 3
    elif f_y == 2:
        if f_x == 0:
            return 4
        elif f_x == 1:
            return 5
    elif f_y == 3 and f_x == 0:
        return 6
    raise Exception("Panic!")


def get_face_to_face(x, y, d):
    f = get_face(x, y)
    if f == 1:
        if d == 2:
            pot = board[(0, limits[1] - side - y)]
            if pot == 2:
                return False
            elif pot == 1:
                return (0, limits[1] - side - y), 0
        elif d == 3:
            pot = board[(0, x + 2 * side)]
            if pot == 2:
                return False
            elif pot == 1:
                return (0, x + 2 * side), 0
    elif f == 2:
        if d == 0:
            pot = board[(limits[0] - side, limits[1] - side - y)]
            if pot == 2:
                return False
            elif pot == 1:
                return (limits[0] - side, limits[1] - side - y), 2
        if d == 1:
            pot = board[(limits[0] - side, x - side)]
            if pot == 2:
                return False
            elif pot == 1:
                return (limits[0] - side, x - side), 2
        if d == 3:
            pot = board[(x - 2 * side, limits[1])]
            if pot == 2:
                return False
            elif pot == 1:
                return (x - 2 * side, limits[1]), 3
    elif f == 3:
        if d == 0:
            pot = board[(y + side, limits[1] - 3 * side)]
            if pot == 2:
                return False
            elif pot == 1:
                return (y + side, limits[1] - 3 * side), 3
        elif d == 2:
            pot = board[(y - side, 2 * side)]
            if pot == 2:
                return False
            elif pot == 1:
                return (y - side, 2 * side), 1
    elif f == 4:
        if d == 2:
            pot = board[(side,  limits[1] - side - y)]
            if pot == 2:
                return False
            elif pot == 1:
                return (side,  limits[1] - side - y), 0
        elif d == 3:
            pot = board[(side, side + x)]
            if pot == 2:
                return False
            elif pot == 1:
                return (side, side + x), 0
    elif f == 5:
        if d == 0:
            pot = board[(limits[0],  limits[1] - side - y)]
            if pot == 2:
                return False
            elif pot == 1:
                return (limits[0],  limits[1] - side - y), 2
        elif d == 1:
            pot = board[(limits[0] - 2 * side, x + 2 * side)]
            if pot == 2:
                return False
            elif pot == 1:
                return (limits[0] - 2 * side, x + 2 * side), 2
    elif f == 6:
        if d == 0:
            pot = board[(y - 2 * side,  limits[1] - side)]
            if pot == 2:
                return False
            elif pot == 1:
                return (y - 2 * side,  limits[1] - side), 3
        elif d == 1:
            pot = board[(x + 2 * side, 0)]
            if pot == 2:
                return False
            elif pot == 1:
                return (x + 2 * side, 0), 1
        elif d == 2:
            pot = board[(y - 2 * side, 0)]
            if pot == 2:
                return False
            elif pot == 1:
                return (y - 2 * side, 0), 1
    raise Exception("Panic!")


@cache
def get_next_tile(x, y, d):
    if d == 0:
        pot = board.get((x + 1, y), 0)
        if pot == 0:
            return get_face_to_face(x, y, d)
        elif pot == 1:
            return (x + 1, y), d
        elif pot == 2:
            return False
        else:
            raise Exception("Panic")
    elif d == 1:
        pot = board.get((x, y + 1), 0)
        if pot == 0:
            return get_face_to_face(x, y, d)
        elif pot == 1:
            return (x, y + 1), d
        elif pot == 2:
            return False
        else:
            raise Exception("Panic")
    if d == 2:
        pot = board.get((x - 1, y), 0)
        if pot == 0:
            return get_face_to_face(x, y, d)
        elif pot == 1:
            return (x - 1, y), d
        elif pot == 2:
            return False
        else:
            raise Exception("Panic")
    elif d == 3:
        pot = board.get((x, y - 1), 0)
        if pot == 0:
            return get_face_to_face(x, y, d)
        elif pot == 1:
            return (x, y - 1), d
        elif pot == 2:
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
loc = (side, 0)

for ins in instructions:
    if ins == "R":
        d = 0 if d == 3 else d + 1
    elif ins == "L":
        d = 3 if d == 0 else d - 1
    elif isinstance(ins, int):
        for _ in range(ins):
            if pot := get_next_tile(*loc, d):
                loc, d = pot
            else:
                break


def get_result(x, y, d):
    return ((y + 1) * 1000) + ((x + 1) * 4) + d


print(get_result(*loc, d))
