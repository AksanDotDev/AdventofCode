import sys
from itertools import cycle
from collections import defaultdict

with open(sys.argv[1]) as file:
    raw = list(file.read().strip())

winds = cycle(raw)
rocks = cycle([0, 1, 2, 3, 4])


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
            if part.x < 0 or part.x > 6 or part.y == 0 or world[part]:
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


world = defaultdict(lambda: False)
height = 0

for i in range(2022):
    rock = Rock(i % 5, height)
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

print(height)
