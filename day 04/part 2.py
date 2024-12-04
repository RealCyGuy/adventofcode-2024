import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import re

from utils.api import get_input

inp = get_input(4)
count = 0

grid = []
for line in inp.splitlines():
    grid.append(list(line))

for i, col in enumerate(inp.splitlines()[0]):
    diagonal = ""
    for j, row in enumerate(inp.splitlines()):
        if i + j < len(row):
            diagonal += row[i + j]
            if re.match(r"MAS|SAM", diagonal[-3:]):
                grid[j - 1][i + j - 1] = "b"
columns = []
for line in grid:
    for i, char in enumerate(line):
        if len(columns) < i + 1:
            columns.append("")
        columns[i] += char
for i, row in enumerate(inp.splitlines()):
    if i == 0:
        continue
    diagonal = ""
    for j, col in enumerate(columns):
        if i + j < len(col):
            diagonal += col[i + j]
            if re.match(r"MAS|SAM", diagonal[-3:]):
                grid[i + j - 1][j - 1] = "b"
lines = []
for line in grid:
    for i, char in enumerate(line):
        if len(lines) < i + 1:
            lines.append("")
        lines[i] += char
for i, row in enumerate(inp.splitlines()):
    if i == 0:
        continue
    diagonal = ""
    diagonal2 = ""
    for j, col in enumerate(reversed(lines)):
        if i + j < len(col):
            diagonal += col[i + j]
            if re.match(r"MbS|SbM", diagonal[-3:]):
                count += 1
for i, col in enumerate(inp.splitlines()[0]):
    diagonal = ""
    for j, row in enumerate(grid):
        if i - j >= 0:
            diagonal += row[i - j]
            if re.match(r"MbS|SbM", diagonal[-3:]):
                count += 1
print(count)
