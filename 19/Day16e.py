raw = input()
rep_digits = list(map(int, raw))

digits = list()
for i in range(0,10000):
    digits.extend(rep_digits)

offset = int(''.join(list(map(str,digits[0:7]))))

for i in range(0,100):
    runningTotal = sum(digits[offset:])
    for j in range(offset, len(digits)):
        current = digits[j]
        digits[j] = runningTotal % 10
        runningTotal -= current

print(''.join(list(map(str,digits[offset:offset+8]))))
