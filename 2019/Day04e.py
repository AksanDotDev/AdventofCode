from collections import Counter

def valid(potential_pass):
    increasing = True
    double = False
    digits = Counter()
    for i in range(0, len(potential_pass)):
        if (i > 0) and (int(potential_pass[i-1]) > int(potential_pass [i])):
            increasing = False
        digits.update({int(potential_pass [i]) : 1})
    return (increasing and (2 in digits.values()))

range_raw = input()
range_split = range_raw.split('-')
range_test = range(int(range_split[0]), int(range_split[1])+1)

potential_passes = list()
for potential_int in range_test:
    if valid(str(potential_int)):
        potential_passes.append(potential_int)
    
print(len(potential_passes))