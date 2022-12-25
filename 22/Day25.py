import sys


def snafu2dec(xs: str):
    conversion = 0
    for x in xs:
        conversion *= 5
        if x.isdigit():
            conversion += int(x)
        elif x == "-":
            conversion += -1
        elif x == "=":
            conversion += -2
        else:
            raise ValueError
    return conversion


def dec2snafu(x: int):
    if x == 0:
        return "0"

    n = 0
    while abs(x) > 2*5**n + (5**n // 2):
        n += 1

    if abs(x) > 5**n + (5**n // 2):
        if x > 0:
            first = "2"
        else:
            first = "="
    else:
        if x > 0:
            first = "1"
        else:
            first = "-"

    if n > 0:
        remainder = dec2snafu(x - snafu2dec(first + "0" * n))
        return first + "0" * (n - len(remainder)) + remainder
    else:
        return first


with open(sys.argv[1]) as file:
    conv = map(lambda x: snafu2dec(x.strip()), file.readlines())


print(dec2snafu(sum(conv)))
