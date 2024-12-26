import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from utils.api import get_input

inp = get_input(24)
in_gates = False
wires = {}
operations = []
for line in inp.splitlines():
    if not line:
        in_gates = True
    elif not in_gates:
        split = line.split(": ")
        wires[split[0]] = True if split[1] == "1" else False
    else:
        operations.append(line)
while operations:
    operation = operations.pop(0)
    a, op, b, _, c = operation.split(" ")
    if a not in wires or b not in wires:
        operations.append(operation)
        continue
    a = wires[a]
    b = wires[b]
    if op == "AND":
        wires[c] = a and b
    elif op == "OR":
        wires[c] = a or b
    elif op == "XOR":
        wires[c] = a ^ b
total = 0
for i in range(100):
    var = f"z{i:02}"
    if var not in wires:
        break
    total += int(wires[var]) << i
print(total)
