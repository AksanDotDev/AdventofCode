from collections import defaultdict

connections = defaultdict(lambda: [])

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
        candidates = filter(
            lambda x: x.isupper() or x not in focus,
            connections[current]
        )
        expansions = list(map(lambda x: focus.copy() + [x], candidates))
        options.extend(expansions)

    print(paths)
