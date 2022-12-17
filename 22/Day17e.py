import sys
from itertools import cycle
from collections import defaultdict, namedtuple

with open(sys.argv[1]) as file:
    raw = list(file.read().strip())


n = len(raw)
winds = cycle(raw)


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


class Rock():

    def __init__(self, rock_type, height):
        self.parts = []
        if rock_type == 0:
            self.parts.append(Coord(2, height + 4))
            self.parts.append(Coord(3, height + 4))
            self.parts.append(Coord(4, height + 4))
            self.parts.append(Coord(5, height + 4))
        elif rock_type == 1:
            self.parts.append(Coord(2, height + 5))
            self.parts.append(Coord(3, height + 4))
            self.parts.append(Coord(3, height + 5))
            self.parts.append(Coord(4, height + 5))
            self.parts.append(Coord(3, height + 6))
        elif rock_type == 2:
            self.parts.append(Coord(2, height + 4))
            self.parts.append(Coord(3, height + 4))
            self.parts.append(Coord(4, height + 4))
            self.parts.append(Coord(4, height + 5))
            self.parts.append(Coord(4, height + 6))
        elif rock_type == 3:
            self.parts.append(Coord(2, height + 4))
            self.parts.append(Coord(2, height + 5))
            self.parts.append(Coord(2, height + 6))
            self.parts.append(Coord(2, height + 7))
        elif rock_type == 4:
            self.parts.append(Coord(2, height + 4))
            self.parts.append(Coord(2, height + 5))
            self.parts.append(Coord(3, height + 4))
            self.parts.append(Coord(3, height + 5))
        else:
            NotImplemented

    def test_move(self, p_parts, world):
        for part in p_parts:
            if part.x < 0 or part.x > 6 or world[part]:
                return False
        else:
            return True

    def move(self, movement, world):
        p_parts = list(map(lambda x: x + movement, self.parts))
        valid = self.test_move(p_parts, world)
        if valid:
            self.parts = p_parts
        return valid

    def move_left(self, world):
        return self.move(Coord(-1, 0), world)

    def move_right(self, world):
        return self.move(Coord(1, 0), world)

    def move_down(self, world):
        return self.move(Coord(0, -1), world)

    def commit_rock(self, world):
        for part in self.parts:
            world[part] = True

    def get_peak(self):
        return self.parts[-1].y


def snapshot(world, height):
    snapshot = []
    for i in range(7):
        d = 0
        while not world[Coord(i, height - d)]:
            d += 1
        snapshot.append(d)
    return snapshot


WorldState = namedtuple(
    "WorldState",
    ["snapshot", "height", "rock", "wind"]
)

world = defaultdict(lambda: False)
for i in range(7):
    world[Coord(i, 0)] = True
height = 0
r = 0
w = 0

searching = True

potentials = [
    WorldState([0]*7, 0, 0, 0)
]

while searching:
    rock = Rock(r % 5, height)

    for wind in winds:
        w += 1
        if wind == "<":
            rock.move_left(world)
        elif wind == ">":
            rock.move_right(world)
        else:
            raise Exception("Panic!")

        if rock.move_down(world):
            continue
        else:
            rock.commit_rock(world)
            height = max(height, rock.get_peak())
            break

    r += 1

    if r % 5 == 0:
        current = WorldState(
            snapshot(world, height), height, r, (w % n)
        )
        for ws in potentials:
            if ws.snapshot == current.snapshot and ws.wind == current.wind:
                searching -= 1
                start_loop = ws
                end_loop = current
                break
        else:
            potentials.append(current)


short_circuit = (
    end_loop.height - start_loop.height,
    end_loop.rock - start_loop.rock,
    end_loop.wind - start_loop.wind
)

skips = (1000000000000 - r) // short_circuit[1]
short_circuit = tuple(map(lambda x: x * skips, short_circuit))

height += short_circuit[0]
r += short_circuit[1]

for i, d in enumerate(end_loop.snapshot):
    world[Coord(i, height - d)] = True

while r < 1000000000000:
    rock = Rock(r % 5, height)
    for wind in winds:
        if wind == "<":
            rock.move_left(world)
        elif wind == ">":
            rock.move_right(world)
        else:
            raise Exception("Panic!")

        if rock.move_down(world):
            continue
        else:
            rock.commit_rock(world)
            height = max(height, rock.get_peak())
            break
    r += 1

print(height)
