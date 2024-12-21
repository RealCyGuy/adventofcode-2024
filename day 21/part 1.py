import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import itertools
from collections import deque

from utils.api import get_input

inp = get_input(21)


def convert_to_grid(s):
    grid = {}
    for i, line in enumerate(s.splitlines()):
        for j, char in enumerate(line):
            if char == " ":
                continue
            grid[(j, i)] = char
    return grid


directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def get_sequence(codes, grid):
    sequences = []
    for code in codes:
        for k, v in grid.items():
            if v == "A":
                position = k
        sequence = []
        for char in code:
            visited = {}
            queue = deque()
            queue.append((position[0], position[1], "", "v"))
            while queue:
                x, y, steps, prev_direction = queue.popleft()
                distance = len(steps)
                if (x, y) in visited and len(visited[(x, y)]) <= distance:
                    continue
                visited[(x, y)] = steps
                ds = [
                    (prev_direction, directions[prev_direction]),
                ]
                for b in list(directions.items()):
                    if b not in ds:
                        ds.append(b)
                for d, (dx, dy) in ds:
                    step = (x + dx, y + dy)
                    if grid.get(step):
                        queue.append((step[0], step[1], steps + d, d))
            for k, v in grid.items():
                if v == char:
                    sequence.append([])
                    if len(set(visited[k])) > 1:
                        visited[k] = "".join(sorted(visited[k]))
                        for test in [visited[k], visited[k][::-1]]:
                            step = position
                            for d in test:
                                dx, dy = directions[d]
                                step = (step[0] + dx, step[1] + dy)
                                if step not in grid:
                                    break
                            else:
                                sequence[-1].append(test)
                    else:
                        sequence[-1].append(visited[k])
                    position = k
                    break
        for s in itertools.product(*sequence):
            g = ""
            for b in s:
                g += b + "A"
            sequences.append(g)
    return sequences


numeric_keypad = convert_to_grid(
    """789
456
123
 0A"""
)
directional_keypad = convert_to_grid(
    """ ^A
<v>"""
)

total = 0
for line in inp.splitlines():
    total += int(line[:-1]) * len(
        sorted(
            get_sequence(
                get_sequence(get_sequence([line], numeric_keypad), directional_keypad),
                directional_keypad,
            ),
            key=lambda x: len(x),
        )[0]
    )
print(total)
