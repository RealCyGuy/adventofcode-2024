import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import re

from utils.api import get_input

inp = get_input(3)
regex = r"mul\(\d+\,\d+\)"
matches = re.findall(regex, inp)
total = 0
for match in matches:
    split = match[4:-1].split(",")
    total += int(split[0]) * int(split[1])
print(total)
