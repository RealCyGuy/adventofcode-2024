import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(6)
grid = {}
pos = (0, 0)
for i, line in enumerate(inp.splitlines()):
    for j, char in enumerate(line):
        if char == "^":
            pos = (i, j)
            char = "0"
        grid[(i, j)] = char

direction = 0
total = 1
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
    if char == ".":
        total += 1
        grid[next_pos] = "0"
    if char == "#":
        direction = (direction + 1) % 4
    else:
        pos = next_pos

print(total)
