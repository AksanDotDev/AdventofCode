import sys
from collections import deque
from math import lcm

with open(sys.argv[1]) as file:
    raw = file.readlines()

dims = [0, 0, len(raw[0]) - 2, len(raw) - 1]


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


class Blizzard(Coord):

    def __init__(self, x, y, d):
        super().__init__(x, y)
        self.d = d

    def step(self):
        if self.d == 0:
            self.x += 1
            if self.x == dims[2]:
                self.x = dims[0] + 1
        elif self.d == 1:
            self.y += 1
            if self.y == dims[3]:
                self.y = dims[1] + 1
        elif self.d == 2:
            self.x -= 1
            if self.x == dims[0]:
                self.x = dims[2] - 1
        elif self.d == 3:
            self.y -= 1
            if self.y == dims[1]:
                self.y = dims[3] - 1

    def __repr__(self):
        return f"Blizzard({self.x}, {self.y}, {self.d})"


start = Coord(dims[0] + 1, dims[1])
end = Coord(dims[2] - 1, dims[3])

blizzards = []
initial = []

for y, line in enumerate(raw):
    for x, char in enumerate(line):
        if char == ">":
            blizzards.append(Blizzard(x, y, 0))
            initial.append(Blizzard(x, y, 0))
        elif char == "v":
            blizzards.append(Blizzard(x, y, 1))
            initial.append(Blizzard(x, y, 1))
        elif char == "<":
            blizzards.append(Blizzard(x, y, 2))
            initial.append(Blizzard(x, y, 2))
        elif char == "^":
            blizzards.append(Blizzard(x, y, 3))
            initial.append(Blizzard(x, y, 3))

loop_len = lcm(dims[2] - dims[0] - 1, dims[3] - dims[1] - 1)
ground = set([start, end])
for x in range(dims[0] + 1, dims[2]):
    for y in range(dims[1] + 1, dims[3]):
        ground.add(Coord(x, y))
ground = frozenset(ground)


def get_passable():
    passable = set(ground)
    return passable.difference(blizzards)


passable_ground = [get_passable()]


for i in range(loop_len - 1):
    for blizz in blizzards:
        blizz.step()
    passable = set(ground)
    passable_ground.append(passable.difference(blizzards))

current_best = 4_000_000_000_000
directions = [
    Coord(1, 0),
    Coord(0, 1),
    Coord(-1, 0),
    Coord(0, -1),
    Coord(0, 0)
]


def expand(pos: Coord, time: int):
    potentials = []
    for direction in directions:
        pot_pos = pos + direction
        if pot_pos in passable_ground[(time + 1) % loop_len]:
            potentials.append((pot_pos, time + 1))
    return potentials


def solve(start, end, start_time):
    q = deque()
    q.append((start, start_time))
    while q:
        con = q.popleft()
        if con[0] == end:
            return con[1]
        else:
            q.extend(filter(lambda x: x not in q, expand(*con)))


there = solve(start, end, 0)
back_again = solve(end, start, there)
print(solve(start, end, back_again))
