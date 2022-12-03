import sys

with open(sys.argv[1]) as file:
    raw = list(map(lambda x: x.strip(), file.readlines()))

lc_base = ord('a') - 1
uc_base = ord('A') - 1 - 26


def get_priority(c):
    if c.isupper():
        return ord(c) - uc_base
    elif c.islower():
        return ord(c) - lc_base
    else:
        return 0


badges = []

for a, b, c in zip(raw[0::3], raw[1::3], raw[2::3]):
    badge = set(a) & set(b) & set(c)
    badges.extend(badge)


print(sum(map(get_priority, badges)))
