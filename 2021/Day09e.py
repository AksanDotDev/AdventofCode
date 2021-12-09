def gen_options(point, basin, data):
    i, j = point
    n = len(data)
    m = len(data[i])

    options = []

    if i > 0 and (i-1, j) not in basin and data[i-1][j] != 9:
        options.append((i-1, j))
    if j > 0 and (i, j-1) not in basin and data[i][j-1] != 9:
        options.append((i, j-1))
    if i + 1 < n and (i+1, j) not in basin and data[i+1][j] != 9:
        options.append((i+1, j))
    if j + 1 < m and (i, j+1) not in basin and data[i][j+1] != 9:
        options.append((i, j+1))
    
    return options


with open("Input09.txt") as raw:
    data = []
    for line in raw:
        row = list(map(int, list(line.strip())))
        data.append(row)

    low_points = []
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
                low_points.append((i, j))

    sizes = []
    for point in low_points:
        basin = [point]
        options = gen_options(point, basin, data)
        while options:
            new_point = options.pop()
            if new_point in basin:
                continue
            basin.append(new_point)
            options.extend(gen_options(new_point, basin, data))

        sizes.append(len(basin))

    sizes.sort(reverse=True)
    x, y, z = sizes[:3]

    print(x*y*z)
