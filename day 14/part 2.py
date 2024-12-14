import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import re

from utils.api import get_input

inp = get_input(14)
w, h = 101, 103
robots = []
for line in inp.splitlines():
    robots.append(list(map(int, re.findall(r"-?\d+", line))))
overlap = True
i = 0
while overlap:
    i += 1
    overlap = False
    grid = set()
    j = 0
    new_robots = []
    for x, y, dx, dy in robots:
        x = (x + dx) % w
        y = (y + dy) % h
        if (x, y) in grid:
            overlap = True
        grid.add((x, y))
        new_robots.append([x, y, dx, dy])
        j += 1
    robots = new_robots
# for a in range(w):
#     output = ""
#     for b in range(h):
#         if (a, b) not in grid:
#             output += " "
#         else:
#             output += "#"
#     print(output)
print(i)
