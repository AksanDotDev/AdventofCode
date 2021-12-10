with open("Input02.txt") as raw:
    h1 = 0
    h2 = 0
    a = 0
    d1 = 0
    d2 = 0
    for command, value in map(str.split, raw):
        v = int(value)
        if command == "forward":
            h1 += v
            h2 += v
            d2 += v*a
        elif command == "down":
            a += v
            d1 += v
        elif command == "up":
            a -= v
            d1 -= v
    print(h1*d1)
    print(h2*d2)
