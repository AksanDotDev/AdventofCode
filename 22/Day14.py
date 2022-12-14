import sys

with open(sys.argv[1]) as file:
    raw = map(lambda x: x.split(" -> "), file.readlines())

limits = [None, None, None]
lines = []

for line in raw:
    new_line = []
    for point in line:
        x, y = map(lambda x: int(x.strip()), point.split(","))
        new_line.append((x, y))
        if limits[0] is None or x < limits[0]:
            limits[0] = x
        if limits[1] is None or x > limits[1]:
            limits[1] = x
        if limits[2] is None or y > limits[2]:
            limits[2] = y
    lines.append(new_line)

lines = list(map(
        lambda x: list(map(lambda y: (y[0]-limits[0], y[1]), x)),
        lines
    ))


origin = 500 - limits[0]
limits = (limits[1] - limits[0], limits[2])

matrix = []
for i in range(limits[1]+1):
    matrix_line = []
    for j in range(limits[0]+1):
        matrix_line.append(" ")
    matrix.append(matrix_line)

matrix[0][origin] = "+"

for line in lines:
    for start, end in zip(line[0:], line[1:]):
        if start[0] < end[0]:
            for i in range(start[0], end[0] + 1):
                matrix[start[1]][i] = "█"
        elif start[0] > end[0]:
            for i in range(end[0], start[0] + 1):
                matrix[start[1]][i] = "█"
        elif start[1] < end[1]:
            for i in range(start[1], end[1] + 1):
                matrix[i][start[0]] = "█"
        elif start[1] > end[1]:
            for i in range(end[1], start[1] + 1):
                matrix[i][start[0]] = "█"
        else:
            raise Exception("Panic")

settled = True
sand = 0

while settled:
    x = origin
    y = 0
    searching = True
    while searching:
        if y == limits[1]:
            settled = False
            break
        elif matrix[y + 1][x] == " ":
            y += 1
            continue
        elif matrix[y + 1][x] in "█░":
            if x == 0:
                settled = False
                break
            elif matrix[y + 1][x - 1] == " ":
                y += 1
                x -= 1
                continue
            elif x == limits[0]:
                settled = False
                break
            elif matrix[y + 1][x + 1] == " ":
                y += 1
                x += 1
                continue
            else:
                settled = True
                matrix[y][x] = "░"
                sand += 1
                break

print(sand)
