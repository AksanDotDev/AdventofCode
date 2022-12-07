import sys

with open(sys.argv[1]) as file:
    raw = map(lambda s: s.split(), file.readlines())


class AoCObject():

    def __init__(
        self,
        name,
        parent,
        children,
        size
    ) -> None:
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size


class AoCFile(AoCObject):

    def __init__(self, name, parent, size) -> None:
        super().__init__(name, parent, None, size)

    def __repr__(self) -> str:
        return f"AoCFile({self.name}, size={self.size})"

    def populate_size(self):
        return self.size


class AoCDir(AoCObject):

    def __init__(self, name, parent) -> None:
        super().__init__(name, parent, dict(), None)

    def __repr__(self) -> str:
        return f"AoCFile({self.name}, contains=" \
            f"{self.children.values()}, size={self.size})"

    def populate_size(self):
        if self.size is not None:
            return self.size
        elif self.children:
            self.size = sum(map(
                lambda x: x.populate_size(),
                self.children.values()
            ))
            return self.size
        else:
            self.size = 0
            return self.size


root = AoCDir("/", None)

location = None

for line in raw:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "/":
                location = root
            elif line[2] == "..":
                location = location.parent
            else:
                location = location.children[line[2]]
        else:
            continue
    elif line[0] == "dir":
        location.children[line[1]] = AoCDir(line[1], location)
    elif line[0].isnumeric():
        location.children[line[1]] = AoCFile(line[1], location, int(line[0]))


def part_one(x):
    if isinstance(x, AoCDir):
        s = sum(map(part_one, x.children.values()))
        if x.size <= 100_000:
            return s + x.size
        else:
            return s
    else:
        return 0


root.populate_size()

print(part_one(root))
