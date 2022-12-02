import sys

outcomes = {
    ("A", "X"): (1+3),
    ("A", "Y"): (2+6),
    ("A", "Z"): (3+0),
    ("B", "X"): (1+0),
    ("B", "Y"): (2+3),
    ("B", "Z"): (3+6),
    ("C", "X"): (1+6),
    ("C", "Y"): (2+0),
    ("C", "Z"): (3+3),
}

with open(sys.argv[1]) as file:
    raw = file.readlines()

total = 0

for line in raw:
    l, r = line.split()
    total += outcomes[(l, r)]

print(total)
