import sys

with open(sys.argv[1]) as file:
    raw = file.readlines()

cals = []
current = 0
for line in raw:
    if line.strip():
        current += int(line)
    else:
        cals.append(current)
        current = 0
cals.append(current)

print(sum(sorted(cals)[-3:]))
