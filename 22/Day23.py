import sys


with open(sys.argv[1]) as file:
    raw = file.readlines()

grove = []
limits = (0, 0, 0, 0)

for i, line in enumerate(raw):
    for j, char in enumerate(line.strip()):
        if char == "#":
            grove.append((i, j))
            limits = (
                min(limits[0], i),
                min(limits[1], j),
                max(limits[2], i),
                max(limits[3], j)
            )

direction_priority = [3, 1, 2, 0]


def get_proposed_move(grove, i, j):
    neighbouring_positions = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
        (i, j - 1),
    ]
    if any(map(lambda x: x in grove, neighbouring_positions)):
        for direction in direction_priority:
            if direction == 0 and all(map(
                lambda x: x not in grove,
                neighbouring_positions[2:5]
            )):
                return (i, j + 1)

            elif direction == 1 and all(map(
                lambda x: x not in grove,
                neighbouring_positions[4:7]
            )):
                return (i + 1, j)

            elif direction == 2 and all(map(
                lambda x: x not in grove,
                neighbouring_positions[0:1] + neighbouring_positions[6:8]
            )):
                return (i, j - 1)

            elif direction == 3 and all(map(
                lambda x: x not in grove,
                neighbouring_positions[0:3]
            )):
                return (i - 1, j)

    else:
        return False


for _ in range(10):
    proposed = []
    for elf in grove:
        proposed.append(get_proposed_move(grove, *elf))

    for proposal in proposed:
        if proposal:
            c = proposed.count(proposal)
            if c > 1:
                for e in range(c):
                    proposed[proposed.index(proposal)] = False

    grove = list(map(lambda x, y: y if y else x, grove, proposed))

    for elf in grove:
        limits = (
                min(limits[0], elf[0]),
                min(limits[1], elf[1]),
                max(limits[2], elf[0]),
                max(limits[3], elf[1])
            )

    direction_priority = direction_priority[1:] + direction_priority[:1]


def get_result(limits, grove):
    return (
        (limits[2] - limits[0] + 1)
        * (limits[3] - limits[1] + 1)
        - len(grove)
    )


print(get_result(limits, grove))
