import sys
from collections import deque

with open(sys.argv[1]) as file:
    raw = list(map(int, file.readlines()))

n = len(raw)
volatile = deque(enumerate(raw))

for idx_i, v in enumerate(raw):
    idx_v = volatile.index((idx_i, v))
    volatile.rotate(-1*idx_v)
    p = volatile.popleft()
    volatile.rotate(-1*v)
    volatile.appendleft(p)

frozen = list(map(lambda x: x[1], volatile))
base = frozen.index(0)
print(sum(frozen[(i + base) % n] for i in [1000, 2000, 3000]))
