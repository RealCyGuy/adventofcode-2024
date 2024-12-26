import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import math
import re

from utils.api import get_input

inp = get_input(17)

nums = list(map(int, re.findall(r"\d+", inp)))
a = nums[0]
b = nums[1]
c = nums[2]
instructions = nums[3:]
pointer = 0
output = []
while pointer < len(instructions):
    instruction = instructions[pointer]
    operand = instructions[pointer + 1]
    if operand <= 3:
        combo = operand
    elif operand == 4:
        combo = a
    elif operand == 5:
        combo = b
    elif operand == 6:
        combo = c
    if instruction == 0:
        a = math.trunc(a / 2**combo)
    elif instruction == 1:
        b = b ^ operand
    elif instruction == 2:
        b = combo % 8
    elif instruction == 3:
        if a != 0:
            pointer = operand
            continue
    elif instruction == 4:
        b = b ^ c
    elif instruction == 5:
        output.append(combo % 8)
    elif instruction == 6:
        b = math.trunc(a / 2**combo)
    elif instruction == 7:
        c = math.trunc(a / 2**combo)
    pointer += 2
print(",".join(map(str, output)))
