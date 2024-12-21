import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import deque

from utils.api import get_input

inp = get_input(18)
size = 70
_bytes = 1024
grid = {}
for i in range(size + 1):
    for j in range(size + 1):
        grid[(i, j)] = True
for i, byte in enumerate(inp.splitlines()):
    if i == _bytes:
        break
    x, y = [int(x) for x in byte.split(",")]
    grid[(x, y)] = False
queue = deque()
visited = {}
queue.append((0, 0, 0))
while queue:
    x, y, distance = queue.popleft()
    if (x, y) in visited and visited[(x, y)] <= distance:
        continue
    visited[(x, y)] = distance
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        step = (x + dx, y + dy)
        if grid.get(step):
            queue.append((step[0], step[1], distance + 1))
print(visited[(size, size)])
