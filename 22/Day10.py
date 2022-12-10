import sys

with open(sys.argv[1]) as file:
    raw = map(lambda x: x.split(), file.readlines())


x = 1
clock = 1
measures = [20, 60, 100, 140, 180, 220]
result = 0


def inc_clock():
    global clock, result
    clock += 1
    if clock in measures:
        result += (clock * x)


for line in raw:
    if line[0] == "noop":
        inc_clock()
    elif line[0] == "addx":
        inc_clock()
        x += int(line[1])
        inc_clock()

print(result)
