from collections import defaultdict

connections = defaultdict(lambda: [])


def validate(candidates):
    small_caves = []
    duplicate = False
    for loc in candidates:
        if loc.islower():
            if loc not in small_caves:
                small_caves.append(loc)
            elif not duplicate and loc != "start":
                duplicate = True
            else:
                return False
    return True


with open("Input12.txt") as raw:
    for line in raw:
        a, b = line.strip().split("-")
        connections[a].append(b)
        connections[b].append(a)

    paths = 0
    options = [["start"]]
    while options:
        focus = options.pop()
        current = focus[-1]
        if current == "end":
            paths += 1
            continue
        expansions = map(
            lambda x: focus.copy() + [x],
            connections[current]
        )
        expansions = filter(validate, expansions)
        options.extend(expansions)

    print(paths)
