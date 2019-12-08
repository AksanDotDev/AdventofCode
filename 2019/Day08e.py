from collections import Counter

img_sif = input()

img_layers = [img_sif[s:s+(150)] for s in range(0, len(img_sif), 150)]

final_img = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

def getPixel(index):
    row = index//25
    column = index%25
    return final_img[row][column]

def setPixel(index, value):
    row = index//25
    column = index%25
    final_img[row][column] = value

for img_layer in img_layers:
    for index in range(0,150):
        if(getPixel(index) == ' ' and img_layer[index] != '2'):
            setPixel(index, '█' if (img_layer[index] == '1') else ' ')

for stripe in final_img:
    print("".join(stripe))