pair = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

score = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

with open("Input10.txt") as raw:
    scores = []
    for line in raw:
        buffer = []
        for character in line.strip():
            if character in pair:
                buffer.append(character)
            elif character == pair[buffer[-1]]:
                buffer.pop()
            else:
                break
        else:
            total = 0
            while buffer:
                total *= 5
                total += score[pair[buffer.pop()]]
            scores.append(total)

    scores.sort()
    print(scores[len(scores)//2])
