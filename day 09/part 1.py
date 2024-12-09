import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(9)
blocks = []
id_number = 0
for i, char in enumerate(inp):
    if i % 2 == 0:
        blocks.extend([id_number] * int(char))
        id_number += 1
    else:
        blocks.extend([None] * int(char))
end = len(blocks) - 1
total = 0
for i, block in enumerate(blocks):
    if block is None:
        while blocks[end] is None:
            end -= 1
        if i >= end:
            break
        total += i * blocks[end]
        end -= 1
    else:
        total += i * block
print(total)
