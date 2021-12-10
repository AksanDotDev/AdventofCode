def update_board(d, b):
    for row in b:
        for i in range(5):
            if row[i] == d:
                row[i] = -1


def check_board(b):
    for row in b:
        if sum(row) == -5:
            return True
    for column in zip(*b):
        if sum(column) == -5:
            return True
    return False


def sum_board(b):
    total = 0
    for row in b:
        for value in row:
            if value > 0:
                total += value
    return total


with open("Input04.txt") as raw:
    lines = raw.readlines()

    drawn = map(lambda x: int(x.strip()), lines[0].split(","))

    n = len(lines)//6
    boards = []
    for i in range(n):
        rows = []
        for j in range(5):
            rows.append(list(map(int, lines[2+(i*6)+j].split())))
        boards.append(rows)

    for draw in drawn:
        for board in boards:
            update_board(draw, board)
            if check_board(board):
                print(sum_board(board)*draw)
                exit(0)
