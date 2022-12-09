import sys

with open(sys.argv[1]) as file:
    raw = list(map(
        lambda x: list(map(int, x.strip())),
        file.readlines()
    ))

trr = list(map(list, zip(*raw)))

n = len(raw)
m = len(raw[0])
visible = 2*n + 2*m - 4

for i in range(1, n-1):
    for j in range(1, m-1):
        t = raw[i][j]
        if (all(map(lambda x: x < t, raw[i][:j])) or
                all(map(lambda x: x < t, raw[i][j+1:])) or
                all(map(lambda x: x < t, trr[j][:i])) or
                all(map(lambda x: x < t, trr[j][i+1:]))):
            visible += 1
            continue

print(visible)
