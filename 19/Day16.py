raw = input()
digits = list(map(int, raw))

pattern = [0,1,0,-1]
for i in range(0,4):
    for j in range(0, len(digits)):
        acc = 0
        for k in range(0, len(digits)):
            acc += digits[k]*pattern[((k+1)//(j+1))%len(pattern)]
        digits[j] = abs(acc)%10

answer = ''.join(list(map(str,digits[0:8])))
print(answer)