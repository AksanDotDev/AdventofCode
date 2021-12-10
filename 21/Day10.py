pair = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

with open("Input10.txt") as raw:
    total = 0
    for line in raw:
        buffer = []
        for character in line.strip():
            if character in pair:
                buffer.append(character)
            elif character == pair[buffer[-1]]:
                buffer.pop()
            else:
                total += score[character]
                break

    print(total)
