with open("Input01.txt") as raw:
    depth = []
    for line in raw:
        depth.append(int(line))
    # Task One
    print(sum(map(
        lambda x: 1 if x[0] < x[1] else 0,
        zip(depth[:-1], depth[1:])
    )))
    # Task Two
    rolling_sums = list(map(sum, zip(depth[:-2], depth[1:-1], depth[2:])))
    print(sum(map(
        lambda x: 1 if x[0] < x[1] else 0,
        zip(rolling_sums[:-1], rolling_sums[1:])
    )))
