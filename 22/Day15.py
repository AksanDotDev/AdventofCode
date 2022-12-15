import sys

with open(sys.argv[1]) as file:
    raw = map(lambda x: x.split(), file.readlines())


target = 2000000
dead_cells = set()
target_beacons = set()


for line in raw:
    s_x = int(line[2].strip(",").split("=")[1])
    s_y = int(line[3].strip(":").split("=")[1])
    b_x = int(line[8].strip(",").split("=")[1])
    b_y = int(line[9].split("=")[1])

    dead_range = abs(s_x - b_x) + abs(s_y - b_y)
    to_target = abs(s_y - target)

    if to_target <= dead_range:
        dead_cells.add(s_x)
        for i in range(dead_range - to_target + 1):
            dead_cells.add(s_x + i)
            dead_cells.add(s_x - i)

    if b_y == target:
        target_beacons.add(b_y)

print(len(dead_cells - target_beacons))
