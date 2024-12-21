import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import deque

from utils.api import get_input

inp = get_input(18)
size = 70
grid = {}
for i in range(size + 1):
    for j in range(size + 1):
        grid[(i, j)] = True
for byte in inp.splitlines():
    x, y = [int(x) for x in byte.split(",")]
    grid[(x, y)] = False
    queue = deque()
    visited = {}
    queue.append((0, 0, 0))
    while queue:
        nx, ny, distance = queue.popleft()
        if (nx, ny) in visited and visited[(nx, ny)] <= distance:
            continue
        visited[(nx, ny)] = distance
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            step = (nx + dx, ny + dy)
            if grid.get(step):
                queue.append((step[0], step[1], distance + 1))
    if (size, size) not in visited:
        print(f"{x},{y}")
        break
