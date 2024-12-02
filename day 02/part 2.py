import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(2)
total = 0
for line in inp.splitlines():
    safe = False
    items = [int(x) for x in line.split()]
    for x in range(len(items)):
        new_items = items.copy()
        new_items.pop(x)
        way1 = 0
        way2 = 0
        for i, item in enumerate(new_items[1:]):
            diff = item - new_items[i]
            if diff > 0:
                way1 += 1
            else:
                way2 += 1
            if abs(diff) > 3 or diff == 0:
                way1 = 1
                way2 = 1
                break
        if way1 == 0 or way2 == 0:
            safe = True
    if safe:
        total += 1
print(total)
