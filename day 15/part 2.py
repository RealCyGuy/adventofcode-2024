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
                robot = (j * 2, i)
                value = "."
            if value == "O":
                grid[(j * 2, i)] = "["
                grid[(j * 2 + 1, i)] = "]"
            else:
                grid[(j * 2, i)] = value
                grid[(j * 2 + 1, i)] = value
    else:
        for move in line:
            dx, dy = directions[move]
            to_move = {}
            to_check = [(robot[0] + dx, robot[1] + dy, True)]
            can_move = True
            while to_check:
                x, y, check_lr = to_check.pop()
                value = grid[(x, y)]

                if value == ".":
                    continue
                if value == "#":
                    can_move = False
                    break
                if move in "^v" and check_lr:
                    if value == "[":
                        to_check.append((x + 1, y, False))
                    elif value == "]":
                        to_check.append((x - 1, y, False))
                to_check.append((x + dx, y + dy, True))
                to_move[(x + dx, y + dy)] = value
            if can_move:
                for x, y in to_move.keys():
                    grid[(x - dx, y - dy)] = "."
                for coord, value in to_move.items():
                    grid[coord] = value
                robot = (robot[0] + dx, robot[1] + dy)

total = 0
for coord, value in grid.items():
    if value == "[":
        total += 100 * coord[1] + coord[0]

print(total)
