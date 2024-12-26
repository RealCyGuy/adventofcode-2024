import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(22)

total = 0
for line in inp.splitlines():
    secret = int(line)
    val = secret
    for _ in range(2000):
        val ^= val * 64
        val %= 16777216

        val ^= val // 32
        val %= 16777216

        val ^= val * 2048
        val %= 16777216
    total += val
print(total)
