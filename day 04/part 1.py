import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import re

from utils.api import get_input

inp = get_input(4)
count = 0
lines = []
for line in inp.splitlines():
    for i, char in enumerate(line):
        if len(lines) < i + 1:
            lines.append("")
        lines[i] += char
diagonals = []
for i, col in enumerate(inp.splitlines()[0]):
    diagonal = ""
    diagonal2 = ""
    for j, row in enumerate(inp.splitlines()):
        if i + j < len(row):
            diagonal += row[i + j]
        if i - j >= 0:
            diagonal2 += row[i - j]
    diagonals.append(diagonal)
    diagonals.append(diagonal2)
for i, row in enumerate(inp.splitlines()):
    if i == 0:
        continue
    diagonal = ""
    diagonal2 = ""
    for j, col in enumerate(lines):
        if i + j < len(col):
            diagonal += col[i + j]
    for j, col in enumerate(reversed(lines)):
        if i + j < len(col):
            diagonal2 += col[i + j]
    diagonals.append(diagonal)
    diagonals.append(diagonal2)
for line in lines + diagonals + inp.splitlines():
    count += len(re.findall(r"(?=XMAS|SAMX)", line))
print(count)
