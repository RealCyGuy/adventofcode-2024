import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import itertools

from utils.api import get_input

inp = get_input(7)

total = 0
for line in inp.splitlines():
    split = line.split(": ")
    value = int(split[0])
    numbers = [int(x) for x in split[1].split(" ")]
    for operations in itertools.product(["+", "*", "|"], repeat=len(numbers) - 1):
        calc = 0
        for i, number in enumerate(numbers):
            if i == 0:
                calc = number
                continue
            if operations[i - 1] == "+":
                calc += number
            elif operations[i - 1] == "*":
                calc *= number
            else:
                calc = int(f"{calc}{number}")
        if calc == value:
            total += value
            break

print(total)
