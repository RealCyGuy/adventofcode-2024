import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import defaultdict

from utils.api import get_input

inp = get_input(12)

grid = {}
for i, line in enumerate(inp.splitlines()):
    for j, char in enumerate(line):
        grid[(j, i)] = char
prices = defaultdict(int)
checked = set()
total = 0
for location, plant in grid.items():
    if location in checked:
        continue
    queue = [(location + (None,))]
    area = 0
    sides = 0
    adjacent_sides = set()
    while queue:
        queue.sort(key=lambda x: x[0])
        queue.sort(key=lambda x: x[1])
        x, y, direction = queue.pop()
        if grid.get((x, y)) != plant:
            dx, dy, old_x, old_y = direction
            if direction not in adjacent_sides:
                sides += 1
            if dy == 0:
                adjacent_sides.add((dx, dy, old_x, old_y + 1))
                adjacent_sides.add((dx, dy, old_x, old_y - 1))
            else:
                adjacent_sides.add((dx, dy, old_x + 1, old_y))
                adjacent_sides.add((dx, dy, old_x - 1, old_y))
            continue
        if (x, y) in checked:
            continue
        area += 1
        checked.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            queue.append((x + dx, y + dy, (dx, dy, x, y)))
    total += area * sides
print(total)
