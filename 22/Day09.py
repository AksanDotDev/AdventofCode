import sys

with open(sys.argv[1]) as file:
    raw = map(lambda x: x.split(), file.readlines())


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


head_moves = {
    "U": Coord(0, 1),
    "D": Coord(0, -1),
    "R": Coord(1, 0),
    "L": Coord(-1, 0)
}


def generate_move(s):
    if abs(s.x) < 2 and abs(s.y) < 2:
        return Coord(0, 0)
    elif abs(s.x) == 2 and s.y == 0:
        return Coord(s.x//abs(s.x), 0)
    elif abs(s.y) == 2 and s.x == 0:
        return Coord(0, s.y//abs(s.y))
    else:
        return Coord(s.x//abs(s.x), s.y//abs(s.y))


locations = set()
head = Coord(0, 0)
tail = Coord(0, 0)

for r, s in raw:
    for _ in range(int(s)):
        head += head_moves[r]
        tail += generate_move(head-tail)
        locations.add(tail)

print(len(locations))
