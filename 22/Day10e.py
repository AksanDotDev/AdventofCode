import sys

with open(sys.argv[1]) as file:
    raw = map(lambda x: x.split(), file.readlines())


x = 1
clock = 1


def print_crt():
    global clock
    if x - clock in [-2, -1, 0]:
        print("#", end="")
    else:
        print(".", end="")
    clock += 1
    if clock % 40 == 1:
        clock = 1
        print()


for line in raw:
    if line[0] == "noop":
        print_crt()
    elif line[0] == "addx":
        print_crt()
        print_crt()
        x += int(line[1])
