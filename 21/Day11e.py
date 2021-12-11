with open("Input11.txt") as raw:
    octopodes = []
    for line in raw:
        row = list(map(int, list(line.strip())))
        octopodes.append(row)

    n = len(octopodes)
    m = len(octopodes[0])

    dark = True
    step = 0
    while dark:
        step += 1

        for i in range(n):
            for j in range(m):
                octopodes[i][j] += 1

        active = True
        while active:
            active = False
            for i in range(n):
                for j in range(m):
                    if octopodes[i][j] > 9:
                        octopodes[i][j] = 0
                        for i_m in range(-1, 2):
                            for j_m in range(-1, 2):
                                x = i + i_m
                                y = j + j_m
                                if 0 <= x < n and 0 <= y < m \
                                        and octopodes[x][y]:
                                    octopodes[x][y] += 1
                        active = True

        if not any(map(any, octopodes)):
            dark = False

    print(step)
