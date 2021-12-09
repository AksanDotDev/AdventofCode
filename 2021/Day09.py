with open("Input09.txt") as raw:
    data = []
    for line in raw:
        row = list(map(int, list(line.strip())))
        data.append(row)

    risk = 0
    n = len(data)
    for i in range(n):
        m = len(data[i])
        for j in range(m):
            height = data[i][j]
            if i > 0 and data[i-1][j] <= height:
                continue
            elif j > 0 and data[i][j-1] <= height:
                continue
            elif i + 1 < n and data[i+1][j] <= height:
                continue
            elif j + 1 < m and data[i][j+1] <= height:
                continue
            else:
                risk += 1 + height

    print(risk)
