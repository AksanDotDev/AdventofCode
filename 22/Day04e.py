import sys

with open(sys.argv[1]) as file:
    raw = file.readlines()

overlaps = 0

for line in raw:
    (l1, l2), (r1, r2) = map(lambda p: map(int, p.split("-")), line.split(","))
    if (l1 <= r1 and l2 >= r1) or \
            (r1 <= l1 and r2 >= l1):
        overlaps += 1

print(overlaps)
