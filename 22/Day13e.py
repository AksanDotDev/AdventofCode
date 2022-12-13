import sys
from functools import cmp_to_key

with open(sys.argv[1]) as file:
    raw = list(map(lambda x: x.strip(), file.readlines()))


def aoc_zip(left, right):

    n = min(len(left), len(right))
    for i in range(n):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
            else:
                continue
        elif isinstance(left[i], list) and isinstance(right[i], list):
            z = aoc_zip(left[i], right[i])
            if z == 0:
                continue
            else:
                return z
        elif isinstance(left[i], list) and isinstance(right[i], int):
            z = aoc_zip(left[i], [right[i]])
            if z == 0:
                continue
            else:
                return z
        elif isinstance(left[i], int) and isinstance(right[i], list):
            z = aoc_zip([left[i]], right[i])
            if z == 0:
                continue
            else:
                return z
        else:
            raise Exception("Panic!")

    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1
    else:
        return 0


divider_packets = [[[2]], [[6]]]
packets = divider_packets.copy()

for left, right, i in zip(raw[0::3], raw[1::3], range(1, len(raw))):
    packets.append(eval(left))
    packets.append(eval(right))


decoder_key = 1
for i, packet in enumerate(sorted(
            packets, key=cmp_to_key(aoc_zip), reverse=True
        )):
    if packet in divider_packets:
        decoder_key *= i + 1

print(decoder_key)
