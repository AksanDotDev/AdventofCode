with open("Input08.txt") as raw:
    total = 0
    for line in raw:
        bulk, final = map(
            lambda x: list(map(frozenset, x.split())),
            line.split("|")
        )

        data = set(bulk + final)
        mapping = [None]*10
        fives = []
        sixes = []
        for datum in data:
            live = len(datum)
            if live == 2:
                mapping[1] = datum
            elif live == 3:
                mapping[7] = datum
            elif live == 4:
                mapping[4] = datum
            elif live == 5:
                fives.append(datum)
            elif live == 6:
                sixes.append(datum)
            elif live == 7:
                mapping[8] = datum

        for datum in fives:
            if mapping[1].issubset(datum):
                mapping[3] = datum
            elif len(mapping[4].intersection(datum)) == 2:
                mapping[2] = datum
            else:
                mapping[5] = datum

        for datum in sixes:
            if mapping[4].issubset(datum):
                mapping[9] = datum
            elif mapping[1].issubset(datum):
                mapping[0] = datum
            else:
                mapping[6] = datum

        line_total = 0
        for digit in final:
            line_total = line_total*10 + mapping.index(digit)

        total += line_total

    print(total)
