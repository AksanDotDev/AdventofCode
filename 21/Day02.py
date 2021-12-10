with open("Input02.txt") as raw:
    h = 0
    d = 0
    for line in raw:
        command, value = line.split()
        if command == "forward":
            h += int(value)
        elif command == "down":
            d += int(value)
        elif command == "up":
            d -= int(value)
    print(h*d)
