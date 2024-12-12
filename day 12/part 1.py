import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import defaultdict, deque

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
    queue = deque([location])
    area = 0
    perimeter = 0
    while queue:
        x, y = queue.popleft()
        if grid.get((x, y)) != plant:
            perimeter += 1
            continue
        if (x, y) in checked:
            continue
        area += 1
        checked.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            queue.append((x + dx, y + dy))
    total += area * perimeter
print(total)
