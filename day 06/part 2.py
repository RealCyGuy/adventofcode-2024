import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import Counter

from utils.api import get_input

inp = get_input(6)
grid = {}
start_pos = (0, 0)
for i, line in enumerate(inp.splitlines()):
    for j, char in enumerate(line):
        if char == "^":
            start_pos = (i, j)
        grid[(i, j)] = char

total = 0
for block, char in grid.items():
    if char == "#":
        continue
    grid[block] = "#"
    direction = 0
    pos = start_pos
    visited = Counter()
    while True:
        if direction == 0:
            next_pos = (pos[0] - 1, pos[1])
        elif direction == 1:
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 2:
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 3:
            next_pos = (pos[0], pos[1] - 1)
        char = grid.get(next_pos, "")
        if not char:
            break
        if char == "#":
            direction = (direction + 1) % 4
        else:
            pos = next_pos
            visited[pos] += 1
            if visited[pos] > 3:
                total += 1
                break
    grid[block] = "."

print(total)
