import sys

with open(sys.argv[1]) as file:
    raw = map(lambda x: x.split(), file.readlines())


target = 4000000
sensors = []

for line in raw:
    s_x = int(line[2].strip(",").split("=")[1])
    s_y = int(line[3].strip(":").split("=")[1])
    b_x = int(line[8].strip(",").split("=")[1])
    b_y = int(line[9].split("=")[1])

    sensors.append((s_x, s_y, abs(s_x - b_x) + abs(s_y - b_y)))


def full_test(p):
    for sensor in sensors:
        if (abs(sensor[0] - p[0]) + abs(sensor[1] - p[1])) <= sensor[2]:
            break
    else:
        print(p[0], p[1])
        print(p[0] * 4000000 + p[1])
        exit()


edges = set()
for i in range(target + 1):
    edges.add((0, i))
    edges.add((i, 0))
    edges.add((target, i))
    edges.add((i, target))


potentials = [edges]

for s in sensors:
    local_potential = set()
    for i in range(s[2]):
        local_potential.add((s[0] - s[2] - 1 + i, s[1] + i))
        local_potential.add((s[0] + i, s[1] + s[2] + 1 - i))
        local_potential.add((s[0] + s[2] + 1 - i, s[1] - i))
        local_potential.add((s[0] - i, s[1] - s[2] - 1 + i))
    local_potential = set(
        p for p in local_potential
        if p[0] >= 0 and p[0] <= target and p[1] >= 0 and p[1] <= target
    )
    for potential in potentials:
        for point in (local_potential & potential):
            full_test(point)
    potentials.append(local_potential)
