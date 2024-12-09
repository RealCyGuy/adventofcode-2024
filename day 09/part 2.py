import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(9)

blocks = []
id_number = 0
for i, char in enumerate(inp):
    if i % 2 == 0:
        blocks.append((id_number, int(char)))
        id_number += 1
    else:
        if int(char):
            blocks.append((None, int(char)))

total = 0
x = 1
while x < len(blocks):
    if blocks[-x][0] is not None:
        start = 0
        while start < len(blocks) and start < len(blocks) - x:
            block, amount = blocks[start]
            if block is None and blocks[-x][1] <= blocks[start][1]:
                popped_block, popped_amount = blocks[-x]
                blocks[-x] = (None, popped_amount)
                amount -= popped_amount
                blocks[start] = (popped_block, popped_amount)
                if amount:
                    blocks.insert(start + 1, (None, amount))
                break
            start += 1
    x += 1

i = 0
start = 0
while start < len(blocks):
    block, amount = blocks[start]
    if block is None:
        i += amount
        start += 1
    else:
        for _ in range(amount):
            total += i * block
            i += 1
        start += 1
print(total)
