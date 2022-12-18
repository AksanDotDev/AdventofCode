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


total_free_sides = 0

for chunk in chunks:
    free_sides = 6
    for offset in offsets:
        if tuple((x + y for (x, y) in zip(chunk, offset))) in chunks:
            free_sides -= 1
    total_free_sides += free_sides

print(total_free_sides)
