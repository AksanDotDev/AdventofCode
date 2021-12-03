def lst_cmp(xs):
    def f(ys):
        for x, y in zip(xs, ys):
            if x != y:
                return False
        return True
    return f


def s_rnd(x):
    if x < 0.5:
        return 0
    return 1


with open("Input03.txt") as raw:

    binary_arrays = []
    for line in raw:
        binary_arrays.append(list(map(int, list(line.strip()))))

    oxygen = []
    co2 = []
    for i in range(len(binary_arrays[0])):
        total = 0
        filtered = list(filter(lst_cmp(oxygen), binary_arrays))
        for array in filtered:
            total += array[i]
        oxygen.append(s_rnd(total/(len(filtered))))
        total = 0
        filtered = list(filter(lst_cmp(co2), binary_arrays))
        for array in filtered:
            total += array[i]
        length = len(filtered)
        if length == 1:
            co2.append(total)
        else:
            co2.append(0 if s_rnd(total/length) else 1)

    oxygen = int("".join(map(str, oxygen)), 2)
    co2 = int("".join(map(str, co2)), 2)

    print(oxygen*co2)
