with open("Input07.txt") as raw:
    positions = list(map(int, raw.read().split(",")))
    length = max(positions)
    pos_array = [0] * (length + 1)
    for position in positions:
        pos_array[position] += 1

    best_candidate = 0
    best_imbalance = sum(pos_array)
    for i, value in enumerate(pos_array):
        imbalance = abs(sum(pos_array[:i]) - sum(pos_array[i+1:]))
        if imbalance < best_imbalance:
            best_candidate = i
            best_imbalance = imbalance

    fuel = 0
    for i, value in enumerate(pos_array):
        fuel += abs(best_candidate - i)*value

    print(fuel)
