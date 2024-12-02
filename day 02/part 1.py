import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(2)
safe = 0
for line in inp.splitlines():
    items = [int(x) for x in line.split()]
    way1 = 0
    way2 = 0
    for i, item in enumerate(items[1:]):
        diff = item - items[i]
        if diff > 0:
            way1 += 1
        else:
            way2 += 1
        if abs(diff) > 3 or diff == 0:
            way1 = 1
            way2 = 1
            break
    if way1 == 0 or way2 == 0:
        safe += 1
print(safe)
