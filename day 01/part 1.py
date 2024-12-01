import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(1)
list1 = []
list2 = []
for line in inp.splitlines():
    split = line.split()
    list1.append(int(split[0]))
    list2.append(int(split[1]))
list1.sort()
list2.sort()
distance = 0
for x, y in zip(list1, list2):
    distance += abs(x - y)
print(distance)
