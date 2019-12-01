import sys

fuel_t = 0

for mass_raw in sys.stdin:
    mass = int(mass_raw)
    fuel = max((mass//3)-2, 0)
    fuel_u = fuel
    fuel_a = 0
    while (fuel_u > 0):
        fuel_n = max((fuel_u//3)-2, 0)
        fuel_a += fuel_u
        fuel_u = fuel_n
    fuel_t += fuel_a



print(fuel_t)