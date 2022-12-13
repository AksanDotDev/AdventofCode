import sys

with open(sys.argv[1]) as file:
    raw = list(map(lambda x: x.strip(), file.readlines()))


def aoc_zip(left, right):

    n = min(len(left), len(right))
    for i in range(n):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                return False
            else:
                continue
        elif isinstance(left[i], list) and isinstance(right[i], list):
            z = aoc_zip(left[i], right[i])
            if z is None:
                continue
            else:
                return z
        elif isinstance(left[i], list) and isinstance(right[i], int):
            z = aoc_zip(left[i], [right[i]])
            if z is None:
                continue
            else:
                return z
        elif isinstance(left[i], int) and isinstance(right[i], list):
            z = aoc_zip([left[i]], right[i])
            if z is None:
                continue
            else:
                return z
        else:
            raise Exception("Panic!")

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    else:
        return None


ordered = 0

for left, right, i in zip(raw[0::3], raw[1::3], range(1, len(raw))):
    left = eval(left)
    right = eval(right)
    if aoc_zip(left, right):
        ordered += i

print(ordered)
