from collections import Counter

img_sif = input()

img_layers = [img_sif[s:s+(150)] for s in range(0, len(img_sif), 150)]

img_layer_data = list()

for img_layer in img_layers:
    img_layer_data.append(Counter(img_layer))

min_zeroes = 151

for img_layer_datum in img_layer_data:
    if (img_layer_datum['0'] < min_zeroes):
        min_zeroes = img_layer_datum['0']
        target_layer = img_layer_datum

print(target_layer['1']*target_layer['2'])