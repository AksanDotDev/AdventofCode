with open("Input02.txt") as raw:
    h = 0
    a = 0
    d = 0
    for line in raw:
        command, value = line.split()
        if command == "forward":
            v = int(value)
            h += v
            d += v*a
        elif command == "down":
            a += int(value)
        elif command == "up":
            a -= int(value)
    print(h*d)
