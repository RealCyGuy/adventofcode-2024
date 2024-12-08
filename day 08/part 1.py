import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import itertools
from collections import defaultdict

from utils.api import get_input

inp = get_input(8)
grid = {}
signals = defaultdict(list)
for i, line in enumerate(inp.splitlines()):
    for j, char in enumerate(line):
        grid[(i, j)] = char
        if char != ".":
            signals[char].append((i, j))
antinodes = set()
for coords in signals.values():
    for s1, s2 in itertools.combinations(coords, 2):
        diff = (s1[0] - s2[0], s1[1] - s2[1])
        p1 = (s1[0] + diff[0], s1[1] + diff[1])
        p2 = (s2[0] - diff[0], s2[1] - diff[1])
        if grid.get(p1):
            antinodes.add(p1)
        if grid.get(p2):
            antinodes.add(p2)
print(len(antinodes))
