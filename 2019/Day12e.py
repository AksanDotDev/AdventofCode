from sys import stdin
from itertools import product

systems = [list(),list(),list()]
combinations = [(x,y) for x in range(0,4) for y in range(0,4) if x < y]

for raw_line in stdin:
    trimmed_line = raw_line.rstrip()[1:-1]
    split_line = trimmed_line.split(',')
    systems[0].append((int(split_line[0].lstrip()[2:]),0))
    systems[1].append((int(split_line[1].lstrip()[2:]),0))
    systems[2].append((int(split_line[2].lstrip()[2:]),0))

def solve_system(system):
    states = list()
    while (system not in states):
        states.append(system[:])
        sim_sys_step(system)
    offset = states.index(system)
    loop = len(states) - offset

    return (offset, loop)

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

solutions = list()

determining_loop = 0
for i in range(0,3):
    sol = solve_system(systems[i])
    solutions.append(sol)
    if (sol[1] > determining_loop):
        determining_loop = sol[1]
        determining_solution = sol

searching = True
step = determining_solution[1]
i = determining_solution[0] 
while(searching):
    i += step
    if ((i - solutions[0][0]) % solutions[0][1] == 0 and (i - solutions[1][0]) % solutions[1][1] == 0 and (i - solutions[2][0]) % solutions[2][1] == 0):
        searching = False
    

print(i)

