from collections import defaultdict


with open("Input13.txt") as raw:
    folds = []
    dots = defaultdict(lambda: 0)
    m_x = 0
    m_y = 0
    for line in raw:
        if line.startswith("fold along"):
            axis, value = line.strip().split()[2].split("=")
            folds.append((axis, int(value)))
        elif line.strip():
            x, y = map(int, line.strip().split(","))
            m_x = max(x, m_x)
            m_y = max(y, m_y)
            dots[(x, y)] = 1

    for axis, value in folds:
        dot_locations = list(dots.keys())
        if axis == "x":
            for x, y in dot_locations:
                if x > value:
                    dots[(2*value - x, y)] = 1
                    del dots[(x, y)]
            m_x = value - 1
        else:
            for x, y in dot_locations:
                if y > value:
                    dots[(x, 2*value - y)] = 1
                    del dots[(x, y)]
            m_y = value - 1

    for j in range(m_y + 1):
        for i in range(m_x + 1):
            print("#" if dots[(i, j)] else " ", end="")
        print()
