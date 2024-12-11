import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from collections import defaultdict

from utils.api import get_input

inp = get_input(11)
stone_list = [int(x) for x in inp.split()]

stones = defaultdict(int)

for stone in stone_list:
    stones[stone] += 1

for _ in range(75):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                new_stones[int(s[: len(s) // 2])] += count
                new_stones[int(s[len(s) // 2 :])] += count
            else:
                new_stones[stone * 2024] += count
    stones = new_stones

print(sum(stones.values()))
