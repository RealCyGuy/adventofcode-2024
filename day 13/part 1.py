import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(13)
total = 0
for i, line in enumerate(inp.splitlines()):
    n = i % 4
    if n == 0:
        ax, ay = [
            int("".join([y for y in x if y.isnumeric()])) for x in line.split(", Y+")
        ]
    elif n == 1:
        bx, by = [
            int("".join([y for y in x if y.isnumeric()])) for x in line.split(", Y+")
        ]
    elif n == 2:
        goalx, goaly = [
            int("".join([y for y in x if y.isnumeric()])) for x in line.split(", Y")
        ]
        min_tokens = 0
        for j in range(1, 100 + 1):
            x, y = ax * j, ay * j
            tokens = 3 * j
            while x < goalx and y < goaly:
                x += bx
                y += by
                tokens += 1
            if x == goalx and y == goaly:
                if min_tokens == 0 or tokens < min_tokens:
                    min_tokens = tokens
        total += min_tokens
print(total)
