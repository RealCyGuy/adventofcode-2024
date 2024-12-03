import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import re

from utils.api import get_input

inp = get_input(3)
regex = r"(mul\(\d+\,\d+\))|(do\(\))|(don't\(\))"
matches = re.findall(regex, inp)
total = 0
do = True
for match in matches:
    if match[0]:
        if do:
            split = match[0][4:-1].split(",")
            total += int(split[0]) * int(split[1])
    elif match[1]:
        do = True
    elif match[2]:
        do = False
print(total)
