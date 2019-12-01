import sys

fuel_t = 0

for mass_raw in sys.stdin:
    mass = int(mass_raw)
    fuel = max((mass//3)-2, 0)
    fuel_t += fuel

print(fuel_t)