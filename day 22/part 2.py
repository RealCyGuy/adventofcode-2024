import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import defaultdict

from utils.api import get_input

inp = get_input(22)

sequences = defaultdict(int)
for line in inp.splitlines():
    secret = int(line)
    previous_price = secret % 10
    changes = []
    visited = set()
    nums = [previous_price]
    for i in range(2000):
        secret ^= secret * 64
        secret %= 16777216

        secret ^= secret // 32
        secret %= 16777216

        secret ^= secret * 2048
        secret %= 16777216

        price = secret % 10
        changes.append(price - previous_price)
        nums.append(price)
        if len(changes) > 4:
            changes.pop(0)
        if len(changes) == 4:
            c = tuple(changes)
            if c not in visited:
                visited.add(c)
                sequences[c] += price
        previous_price = price
print(max(sequences.values()))
