import sys

with open(sys.argv[1]) as file:
    raw = file.readlines()

max_cal = 0
current = 0
for line in raw:
    if line.strip():
        current += int(line)
        max_cal = max(max_cal, current)
    else:
        current = 0

print(max_cal)
