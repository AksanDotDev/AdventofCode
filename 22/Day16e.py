import sys
from collections import defaultdict
from itertools import combinations

with open(sys.argv[1]) as file:
    raw = map(lambda x: x.split(), file.readlines())


class Valve():

    def __init__(self, name, flow_rate, tunnels):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels
        self.dist = defaultdict(lambda: 1_000_000)
        for location in self.tunnels:
            self.dist[location] = 1
        self.dist[self.name] = 0

    def pot(self, time):
        return self.flow_rate * time

    def update_distances(self, new_valve):
        best_d = min((self.dist[n] for n in new_valve.tunnels)) + 1
        update = False
        if best_d < self.dist[new_valve.name]:
            update = True
            self.dist[new_valve.name] = best_d
        if best_d < new_valve.dist[self.name]:
            update = True
            new_valve.dist[self.name] = best_d
        return update

    def __repr__(self):
        return f"Valve({self.flow_rate}, {self.tunnels}," +\
                f" {self.dist})"


system = dict()

for line in raw:
    new_valve = Valve(
        line[1],
        int(line[4].split("=")[1].strip(";")),
        list(map(lambda x: x.strip(","), line[9:]))
    )

    system[new_valve.name] = new_valve

update = True
while update:
    update = False
    for valve in system.values():
        for valve_2 in system.values():
            if valve.update_distances(valve_2):
                update = True

system = dict(filter(lambda i: i[1].flow_rate, system.items()))


def recursive_solve(closed, time=26, loc="AA", vent=0):
    children = []
    for dest in closed:
        valve = system[dest]
        p_time = time - valve.dist[loc] - 1
        if p_time >= 0:
            p_vent = vent + valve.pot(p_time)
            children.append(recursive_solve(
                closed.difference([dest]),
                time=p_time,
                loc=dest,
                vent=p_vent
            ))
    if children:
        return max(children)
    else:
        return vent


key_valves = system.keys()
best = 0

for i in range(len(key_valves)//2 + 1):
    for perms in combinations(key_valves, i):
        closed_a = set(perms)
        closed_b = key_valves - closed_a
        best = max(
            best,
            recursive_solve(closed_a) + recursive_solve(closed_b)
        )


print(best)
