def valid(potential_pass):
    double = False
    increasing = True
    for i in range(1, len(potential_pass)):
        if (int(potential_pass[i-1]) > int(potential_pass [i])):
            increasing = False
        if (int(potential_pass[i-1]) == int(potential_pass [i])):
            double = True
    return (double and increasing)

range_raw = input()
range_split = range_raw.split('-')
range_test = range(int(range_split[0]), int(range_split[1])+1)

potential_passes = list()
for potential_int in range_test:
    if valid(str(potential_int)):
        potential_passes.append(potential_int)
    
print(len(potential_passes))