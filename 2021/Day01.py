with open("Input01.txt") as raw:
    previous = 2**18
    total = 0
    for line in raw:
        current = int(line)
        if current > previous:
            total += 1
        previous = current

    print(total)
