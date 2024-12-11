import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(11)
stones = [int(x) for x in inp.split()]
for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                new_stones.append(int(s[: len(s) // 2]))
                new_stones.append(int(s[len(s) // 2 :]))
            else:
                new_stones.append(stone * 2024)
    stones = new_stones
print(len(stones))
