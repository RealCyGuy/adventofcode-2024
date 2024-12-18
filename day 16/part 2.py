import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import deque

from utils.api import get_input

inp = get_input(16)
grid = {}
queue = deque()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i, line in enumerate(inp.splitlines()):
    for j, char in enumerate(line):
        if char == "S":
            queue.append((j, i, 1, 0))
        grid[(j, i)] = char
visited = {}
scores = []
while queue:
    x, y, direction, score = queue.popleft()
    if (x, y, direction) in visited and visited[(x, y, direction)] <= score:
        continue
    visited[(x, y, direction)] = score
    char = grid[(x, y)]
    if char == "E":
        scores.append((score, x, y))
    for d, (dx, dy) in enumerate(directions):
        step = (x + dx, y + dy)
        if grid.get(step) == "#" or step in visited:
            continue
        dr = abs(d - direction)
        if dr == 3:
            dr = 1
        queue.append((step[0], step[1], d, score + dr * 1000 + 1))
min_score, end_x, end_y = min(scores, key=lambda x: x[0])
tiles = set()
queue = deque()
queue.append((end_x, end_y, min_score))
while queue:
    x, y, score = queue.popleft()
    for direction in directions:
        step = (x + direction[0], y + direction[1])
        if grid.get(step) == "#" or step in tiles:
            continue
        step_score = 1e6
        for (sx, sy, _), s in visited.items():
            if (sx, sy) == step:
                if s == score - 1001 or s == score - 1:
                    tiles.add(step)
                    queue.append((step[0], step[1], s))
print(len(tiles) + 1)
