with open("Input07.txt") as raw:
    positions = list(map(int, raw.read().split(",")))
    length = max(positions)
    pos_array = [0] * (length + 1)
    for position in positions:
        pos_array[position] += 1

    best_cost = 10**18
    for i, value in enumerate(pos_array):
        cost = 0
        for j, quant in enumerate(pos_array):
            d = abs(i - j)
            cost += ((d * (d + 1))//2) * quant
        if cost < best_cost:
            best_cost = cost

    print(best_cost)
