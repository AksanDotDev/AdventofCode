from sys import stdin
from collections import Counter
from math import ceil



reactions = dict()

for reaction in stdin:
    split_reaction = reaction.rstrip().split(" => ")
    split_reagents = split_reaction[0].split(", ")
    reagents = Counter()
    for reagent_str in split_reagents:
        str_parts = reagent_str.split(" ")
        reagents[str_parts[1]] = int(str_parts[0])
    products = Counter()
    product_str = split_reaction[1].split(" ")
    products[product_str[1]] = int(product_str[0])
    product = list(products)[0]
    reactions[product] = (products, reagents)

def produceMaterial(goal, materials):
    goal_product, goal_reagents = reactions[goal]
    for reagent in goal_reagents:
        while materials[reagent] < goal_reagents[reagent]:
            if reagent == "ORE" or not produceMaterial(reagent, materials):
                return False
    materials -= goal_reagents
    materials += goal_product
    return True

def produceBulkMaterial(goal, quantity, materials):
    goal_product, goal_reagents = reactions[goal]
    batches = ceil(quantity/goal_product[goal])
    for reagent in goal_reagents:
        if reagent == "ORE":
            if goal_reagents[reagent] * batches <= materials[reagent]:
                materials[reagent] -= goal_reagents[reagent] * batches
            else:
                return False
        elif produceBulkMaterial(reagent, goal_reagents[reagent] * batches, materials):
            materials[reagent] -= goal_reagents[reagent] * batches
        else:
            return False
    materials[goal] += goal_product[goal] * batches
    return True


climbing = True
upper = 1
while climbing:
    materials = Counter({"ORE" : 1000000000000})
    if produceBulkMaterial("FUEL", upper, materials):
        if not produceMaterial("FUEL", materials):
            print(upper)
            exit()
        upper *= 2        
    else:
        climbing = False
    print(upper)

lower = upper//2
while True:
    materials = Counter({"ORE" : 1000000000000})
    mid = (upper + lower)//2
    if produceBulkMaterial("FUEL", mid, materials):
        if not produceMaterial("FUEL", materials):
            print(mid)
            exit()
        lower = mid     
    else:
        upper = mid
