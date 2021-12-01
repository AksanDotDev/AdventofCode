with open("Input01.txt") as raw:
    depth = []
    for line in raw:
        depth.append(int(line))
    previous = depth[0] + depth[1] + depth[2]
    total = 0
    for i in range(0, len(depth) - 3):
        current = previous - depth[i] + depth[i + 3]
        if current > previous:
            total += 1
        previous = current
    print(total)
