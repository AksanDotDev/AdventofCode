with open("Input08.txt") as raw:
    total = 0
    for line in raw:
        relevant = line.split("|")[1].split()

        for digit in relevant:
            if len(digit) in [2, 4, 3, 7]:
                total += 1

    print(total)
