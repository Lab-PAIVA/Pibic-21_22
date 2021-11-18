import json
from random import random


array_len = 10000

width = 1280
height = 720

points = []
for i in range(array_len):
    x = random() * width
    y = random() * height
    points.append([x, y])

with open(f'../data/{array_len}.json', 'w', encoding='utf-8') as f:
    json.dump(points, f, ensure_ascii=False, indent=4)
