import sys
from collections import defaultdict, deque

with open(sys.argv[1]) as file:
    raw = file.readlines()

stacks = defaultdict(lambda: deque())
actions = []
crates = True
instructions = False
for line in raw:
    if crates:
        for col, char in enumerate(line[1::4]):
            if char.isdigit():
                crates = False
                break
            elif char.isupper():
                stacks[col+1].append(char)
    elif instructions:
        tokens = line.split()
        actions.append(tuple(map(int, (tokens[1], tokens[3], tokens[5]))))
    else:
        instructions = True
        continue

crane = []
for action in actions:
    for i in range(action[0]):
        crane.append(stacks[action[1]].popleft())
    while crane:
        stacks[action[2]].appendleft(crane.pop())

answer = []

for i in range(len(stacks)):
    answer.append(stacks[i+1][0])

print("".join(answer))
