import sys

with open(sys.argv[1]) as file:
    raw = list(map(
        lambda x: list(map(int, x.strip())),
        file.readlines()
    ))

trr = list(map(list, zip(*raw)))

n = len(raw)
m = len(raw[0])

best_scenic = 0


def view_dist(t, v):
    n = 0
    for tree in v:
        if tree < t:
            n += 1
        else:
            return n + 1
    return n


for i in range(1, n-1):
    for j in range(1, m-1):
        t = raw[i][j]
        scenic = 1
        scenic *= view_dist(t, raw[i][j-1::-1])
        scenic *= view_dist(t, raw[i][j+1:])
        scenic *= view_dist(t, trr[j][i-1::-1])
        scenic *= view_dist(t, trr[j][i+1:])

        best_scenic = max(scenic, best_scenic)

print(best_scenic)
