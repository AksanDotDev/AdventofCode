from sys import stdin
from itertools import product
from math import gcd

systems = [list(),list(),list()]
combinations = [(x,y) for x in range(0,4) for y in range(0,4) if x < y]

for raw_line in stdin:
    trimmed_line = raw_line.rstrip()[1:-1]
    split_line = trimmed_line.split(',')
    systems[0].append((int(split_line[0].lstrip()[2:]),0))
    systems[1].append((int(split_line[1].lstrip()[2:]),0))
    systems[2].append((int(split_line[2].lstrip()[2:]),0))

def solve_system(system):
    base_state = system[:]
    i = 1
    sim_sys_step(system)
    while (system != base_state):
        sim_sys_step(system)
        i += 1
    return i

def sim_sys_step(system):
    for combination in combinations:
        p1, v1 = system[combination[0]]
        p2, v2 = system[combination[1]]
        vd = 0 if p1 == p2 else (1 if p1 < p2 else -1)
        system[combination[0]] = (p1, v1 + vd)
        system[combination[1]] = (p2, v2 - vd)
    for i in range(0,4):
        p,v = system[i]
        system[i] = (p+v, v)

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

solutions = list()

for i in range(0,3):
    sol = solve_system(systems[i])
    solutions.append(sol)

print(lcm(lcm(solve_system(systems[0]), solve_system(systems[1])), solve_system(systems[2])))

