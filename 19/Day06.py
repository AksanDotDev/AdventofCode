import sys
from  collections import defaultdict

orbits = dict()
bodies = set()
bodies.add("COM")

for orbit_raw in sys.stdin:
    orbit = orbit_raw.rstrip().split(')', 2)
    orbits[orbit[1]] = orbit[0]
    bodies.add(orbit[1])

orbit_count = 0

for body in bodies:
    index = body
    while (index != "COM"):
        orbit_count += 1
        index = orbits[index]

print(orbit_count)