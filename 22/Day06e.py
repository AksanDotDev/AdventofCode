import sys

with open(sys.argv[1]) as file:
    raw = file.readlines()[0]

for i in range(len(raw)-14):
    if len(set(raw[i:i+14])) == 14:
        break
    else:
        continue

print(i+14)
