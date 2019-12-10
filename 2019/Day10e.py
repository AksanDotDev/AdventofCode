import sys
from math import gcd, atan2, pi

def int2coord(loc):
    return loc % loc_slice, loc // loc_slice

def getVectorRail(x1, y1, x2, y2):
    x_dif = x2 - x1
    y_dif = y2 - y1
    fact = gcd(x_dif, y_dif)
    if (fact == 0):
        if(x_dif > 0 and y_dif > 0):
            return list()
        elif (x_dif == 0):
            x_step = 0
            y_step = 1
            fact = y_dif
        elif (y_dif == 0):
            x_step = 1
            y_step = 0
            fact = x_dif
    else:
        x_step = x_dif // fact
        y_step = y_dif // fact
    vectors = list()
    for i in range(1, fact):
        vectors.append((x1 + (x_step*i), y1 + (y_step*i)))
    return vectors

def getAngle(x1, y1, x2, y2):
    x_dif = x2 - x1
    y_dif = y1 - y2
    raw = atan2(x_dif, y_dif)
    return raw if raw >= 0 else raw + 2*pi

map = list()

for line in sys.stdin:
    map.append(line.rstrip())

loc_count = len(map)*len(map[0])
loc_slice = len(map)


max_result = 0
for loc in range(0,loc_count):
    x_loc, y_loc = int2coord(loc)
    if(map[y_loc][x_loc] == '#'):
        result = 0
        targets = list()
        for tar in range(0,loc_count):
            x_tar, y_tar = int2coord(tar)
            if(map[y_tar][x_tar] == '#' and not (x_loc == x_tar and y_loc == y_tar)):
                rail = getVectorRail(x_loc, y_loc, x_tar, y_tar)
                for point in rail:
                    if (map[point[1]][point[0]] == '#'):
                        break
                else:
                    result += 1
                    targets.append((x_tar, y_tar))
        if (max_result < result):
            x_sta, y_sta = x_loc, y_loc
            max_targets = targets
            max_result = result


angles = list()
for target in max_targets:
    angles.append((getAngle(x_sta, y_sta, target[0], target[1]), target))
angles.sort(key = lambda x: x[0])
print(angles[199][1][0]*100 + angles[199][1][1])

