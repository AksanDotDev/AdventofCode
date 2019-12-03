raw_wire1 = input()
tok_wire1 = raw_wire1.split(',')
raw_wire2 = input()
tok_wire2 = raw_wire2.split(',')

head_wire1 = (0,0)
points_wire1 = list()
points_wire1.append(head_wire1)
for run in tok_wire1:
    if (run[0] == 'R'):
        for i in range(int(run[1:])):
            head_wire1 = (head_wire1[0] + 1, head_wire1[1])
            points_wire1.append(head_wire1)
    if (run[0] == 'L'):
        for i in range(int(run[1:])):
            head_wire1 = (head_wire1[0] - 1, head_wire1[1])
            points_wire1.append(head_wire1)
    if (run[0] == 'U'):
        for i in range(int(run[1:])):
            head_wire1 = (head_wire1[0], head_wire1[1] + 1)
            points_wire1.append(head_wire1)
    if (run[0] == 'D'):
        for i in range(int(run[1:])):
            head_wire1 = (head_wire1[0], head_wire1[1] - 1)
            points_wire1.append(head_wire1)

head_wire2 = (0,0)
points_wire2 = list()
points_wire2.append(head_wire2)
for run in tok_wire2:
    if (run[0] == 'R'):
        for i in range(int(run[1:])):
            head_wire2 = (head_wire2[0] + 1, head_wire2[1])
            points_wire2.append(head_wire2)
    if (run[0] == 'L'):
        for i in range(int(run[1:])):
            head_wire2 = (head_wire2[0] - 1, head_wire2[1])
            points_wire2.append(head_wire2)
    if (run[0] == 'U'):
        for i in range(int(run[1:])):
            head_wire2 = (head_wire2[0], head_wire2[1] + 1)
            points_wire2.append(head_wire2)
    if (run[0] == 'D'):
        for i in range(int(run[1:])):
            head_wire2 = (head_wire2[0], head_wire2[1] - 1)
            points_wire2.append(head_wire2)


intersections = list(set(points_wire1) & set(points_wire2))
intersections.remove((0,0))
distances = list()
for point in intersections:
    distances.append(abs(point[0]) + abs(point[1]))
print(min(distances))