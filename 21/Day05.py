from collections import defaultdict

with open("Input05.txt") as raw:
    display = defaultdict(lambda: 0)

    for line in raw:
        start, end = line.strip().split(" -> ")
        x0, y0 = map(int, start.split(","))
        x1, y1 = map(int, end.split(","))
        if x0 == x1:
            for i in range(min(y0, y1), max(y0, y1) + 1):
                display[(x0, i)] += 1
        elif y0 == y1:
            for i in range(min(x0, x1), max(x0, x1) + 1):
                display[(i, y0)] += 1

    collisions = 0
    for value in display.values():
        if value > 1:
            collisions += 1

    print(collisions)
