import sys

with open(sys.argv[1]) as file:
    raw = map(lambda x: map(int, x.split(",")), file.readlines())


chunks = set()
for line in raw:
    chunks.add(tuple(line))

offsets = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

limits = tuple([
    tuple([
        min(map(lambda x: x[0], chunks)) - 1,
        min(map(lambda x: x[1], chunks)) - 1,
        min(map(lambda x: x[2], chunks)) - 1,
    ]),
    tuple([
        max(map(lambda x: x[0], chunks)) + 1,
        max(map(lambda x: x[1], chunks)) + 1,
        max(map(lambda x: x[2], chunks)) + 1,
    ])
])

pond = set()

for i in range(limits[0][0], limits[1][0] + 1):
    for j in range(limits[0][1], limits[1][1] + 1):
        pond.add(tuple([i, j, limits[0][2]]))
        pond.add(tuple([i, j, limits[1][2]]))

for j in range(limits[0][1], limits[1][1] + 1):
    for k in range(limits[0][2], limits[1][2] + 1):
        pond.add(tuple([limits[0][0], j, k]))
        pond.add(tuple([limits[1][0], j, k]))

for i in range(limits[0][0], limits[1][0] + 1):
    for k in range(limits[0][2], limits[1][2] + 1):
        pond.add(tuple([i, limits[0][1], k]))
        pond.add(tuple([i, limits[1][1], k]))

filling = True

while filling:
    prev_pond = frozenset(pond)

    for i in range(limits[0][0], limits[1][0] + 1):
        for j in range(limits[0][1], limits[1][1] + 1):
            for k in range(limits[0][2], limits[1][2] + 1):
                current = tuple([i, j, k])
                if current in chunks:
                    continue
                for offset in offsets:
                    if tuple(
                        (x + y for (x, y) in zip(current, offset))
                    ) in pond:
                        pond.add(current)
                        continue

    if pond == prev_pond:
        filling = False

total_free_sides = 0

for chunk in chunks:
    free_sides = 6
    for offset in offsets:
        if tuple(
            (x + y for (x, y) in zip(chunk, offset))
        ) not in pond:
            free_sides -= 1
    total_free_sides += free_sides

print(total_free_sides)
