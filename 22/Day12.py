import sys
from queue import PriorityQueue
from dataclasses import dataclass, field

with open(sys.argv[1]) as file:
    raw = list(map(lambda x: list(x.strip()), file.readlines()))


class Coord():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Coord({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return isinstance(other, Coord) \
            and self.x == other.x and self.y == other.y


@dataclass(order=True)
class QItem:
    priority: int
    loc: Coord = field(compare=False)


n = len(raw)
m = len(raw[0])

distances = []
for i in range(n):
    distances.append([])
    for j in range(m):
        distances[i].append(None)

start = Coord(-1, -1)
end = Coord(-1, -1)


for i, line in enumerate(raw):
    for j, char in enumerate(line):
        if char == "S":
            start = Coord(i, j)
            distances[i][j] = 0
            raw[i][j] = "a"
        elif char == "E":
            end = Coord(i, j)
            raw[i][j] = "z"


def h(c):
    o = end - c
    return abs(o.x) + abs(o.y)


def reachable(loc, n):
    return (ord(raw[n.x][n.y]) - ord(raw[loc.x][loc.y])) <= 1


def get_neighbours(loc):
    result = []
    options = map(
        lambda x: x + loc,
        [
            Coord(-1, 0),
            Coord(1, 0),
            Coord(0, 1),
            Coord(0, -1)
        ]
    )
    for o in options:
        if o.x >= 0 and o.x < n and\
                o.y >= 0 and o.y < m and\
                (distances[o.x][o.y] is None or
                 distances[o.x][o.y] > (1 + distances[loc.x][loc.y])) and \
                reachable(loc, o):
            result.append(o)
    return result


q = PriorityQueue()
q.put(QItem(0, start))
end_not_reached = True

while not q.empty() and end_not_reached:
    expand = q.get().loc
    expand_dist = distances[expand.x][expand.y]
    for neighbour in get_neighbours(expand):
        distances[neighbour.x][neighbour.y] = 1 + expand_dist
        if neighbour == end:
            end_not_reached = False
            break
        q.put(QItem(h(neighbour) + expand_dist, neighbour))


print(distances[end.x][end.y])
