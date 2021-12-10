from sys import stdin
from collections import Counter


reactions = dict()
materials = Counter()
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

reactions["ORE"] = (Counter(["ORE"]),Counter())

def produceMaterial(goal, materials):
    goal_product, goal_reagents = reactions[goal]
    ore = 0
    consuming = True
    while consuming:
        consuming = False
        for reagent in goal_reagents:
            while materials[reagent] < goal_reagents[reagent]:
                consuming = True
                ore += produceMaterial(reagent, materials)
    materials -= goal_reagents
    materials += goal_product
    return ore + (1 if goal == "ORE" else 0)



print(produceMaterial("FUEL", materials))
