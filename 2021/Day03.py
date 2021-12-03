def s_rnd(x):
    if x < 0.5:
        return 0
    return 1


with open("Input03.txt") as raw:

    binary_arrays = []
    for line in raw:
        binary_arrays.append(list(map(int, list(line.strip()))))

    gamma = []
    for column in zip(*binary_arrays):
        gamma.append(s_rnd(sum(column)/len(column)))
    epsilon = list(map(lambda x: 0 if x else 1, gamma))

    gamma = int("".join(map(str, gamma)), 2)
    epsilon = int("".join(map(str, epsilon)), 2)

    print(gamma*epsilon)
