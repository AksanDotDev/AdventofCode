import sys
from  collections import defaultdict

orbits = dict()

for orbit_raw in sys.stdin:
    orbit = orbit_raw.rstrip().split(')', 2)
    orbits[orbit[1]] = orbit[0]

target_chain = list()

index = "SAN"
while index != "COM":
    body = orbits[index]
    target_chain.append(body)
    index = body

hops = 0
index = orbits["YOU"]
while index not in target_chain:
    hops += 1
    index = orbits[index]

hops += target_chain.index(index)


print(hops)