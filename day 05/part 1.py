import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(5)
rules = []
updates = []
section = 0
for line in inp.splitlines():
    if not line:
        section += 1
    elif section == 0:
        rules.append([int(x) for x in line.split("|")])
    else:
        updates.append([int(x) for x in line.split(",")])
total = 0
for update in updates:
    correct = True
    for rule in rules:
        try:
            if update.index(rule[0]) > update.index(rule[1]):
                correct = False
                break
        except ValueError:
            pass
    if correct:
        total += update[int((len(update) - 1) / 2)]
print(total)
