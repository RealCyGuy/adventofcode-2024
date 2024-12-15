import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(15)

in_grid = True
grid = {}
directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

for i, line in enumerate(inp.splitlines()):
    if line == "":
        in_grid = False
        continue
    if in_grid:
        for j, value in enumerate(line):
            if value == "@":
                robot = (j, i)
                value = "."
            grid[(j, i)] = value
    else:
        for move in line:
            dx, dy = directions[move]
            position = robot
            while True:
                position = (position[0] + dx, position[1] + dy)
                if grid[position] != "O":
                    break
            if grid[position] == ".":
                grid[position] = "O"
                robot = (robot[0] + dx, robot[1] + dy)
                grid[robot] = "."
total = 0
for coord, value in grid.items():
    if value == "O":
        total += 100 * coord[1] + coord[0]

print(total)
