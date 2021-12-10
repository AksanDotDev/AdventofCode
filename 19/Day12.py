from sys import stdin
from itertools import product

moons = list()

def sim_step(moons, velocities, combinations):
    for combination in combinations:
        x1, y1, z1 = moons[combination[0]]
        x2, y2, z2 = moons[combination[1]]
        xv, yv, zv = velocities[combination[0]]
        xv += 0 if x1 == x2 else (1 if x1 < x2 else -1)
        yv += 0 if y1 == y2 else (1 if y1 < y2 else -1)
        zv += 0 if z1 == z2 else (1 if z1 < z2 else -1)
        velocities[combination[0]] = (xv, yv, zv)
    for i in range(0,4):
        x, y, z = moons[i]
        xv, yv, zv = velocities[i]
        moons[i] = (x+xv,y+yv,z+zv)

def calculate_energy(moons, velocities):
    energy = 0
    for i in range(0,4):
        x, y, z = moons[i]
        xv, yv, zv = velocities[i]
        energy += (abs(x)+abs(y)+abs(z))*(abs(xv)+abs(yv)+abs(zv))
    return energy

for raw_line in stdin:
    trimmed_line = raw_line.rstrip()[1:-1]
    split_line = trimmed_line.split(',')
    moons.append((int(split_line[0].lstrip()[2:]),int(split_line[1].lstrip()[2:]),int(split_line[2].lstrip()[2:])))

velocities = [(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
raw_combinations = list(product(range(0,4), range(0,4)))
combinations = list(filter(lambda x: (x[0] != x[1]), raw_combinations))

for i in range(0,1000):
    sim_step(moons, velocities, combinations)

print(calculate_energy(moons, velocities))