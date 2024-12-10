import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import deque

from utils.api import get_input

inp = get_input(10)
grid = {}
queue = deque()
trailheads = {}
for i, line in enumerate(inp.splitlines()):
    for j, char in enumerate(line):
        char = int(char)
        grid[(i, j)] = char
        if char == 0:
            queue.append((i, j, (i, j)))
            trailheads[(i, j)] = set()
total = 0
while queue:
    i, j, head = queue.popleft()
    value = grid.get((i, j))
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new = (i + direction[0], j + direction[1])
        new_value = grid.get(new)
        if new_value is None:
            continue
        if new_value == value + 1:
            if new_value == 9:
                if new not in trailheads[head]:
                    total += 1
                    trailheads[head].add(new)
            else:
                queue.append(new + (head,))
print(total)
