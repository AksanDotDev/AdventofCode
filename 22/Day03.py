import sys

with open(sys.argv[1]) as file:
    raw = map(lambda x: x.strip(), file.readlines())


lc_base = ord('a') - 1
uc_base = ord('A') - 1 - 26


def get_priority(c):
    if c.isupper():
        return ord(c) - uc_base
    elif c.islower():
        return ord(c) - lc_base
    else:
        return 0


overlaps = []

for line in raw:
    n = len(line)//2
    overlap = set(line[:n]) & set(line[n:])
    overlaps.extend(overlap)

print(sum(map(get_priority, overlaps)))
