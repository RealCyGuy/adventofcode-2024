import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import re

from utils.api import get_input

inp = get_input(14)
w, h = 101, 103
w2, h2 = w // 2, h // 2
quadrants = [0] * 4
for line in inp.splitlines():
    x, y, dx, dy = map(int, re.findall(r"-?\d+", line))
    x = (x + dx * 100) % w
    y = (y + dy * 100) % h
    if x < w2:
        if y < h2:
            quadrants[0] += 1
        elif y > h2:
            quadrants[2] += 1
    elif x > w2:
        if y < h2:
            quadrants[1] += 1
        elif y > h2:
            quadrants[3] += 1
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
