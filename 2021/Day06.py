with open("Input06.txt") as raw:
    periods = map(int, raw.read().split(","))
    rep0 = [0]*9
    for period in periods:
        rep0[period] += 1
    for _ in range(256):
        rep1 = [0]*9
        rep1[6] = rep1[8] = rep0[0]
        for i in range(8):
            rep1[i] += rep0[i+1]
        rep0 = rep1
    print(sum(rep0))
