import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from sympy import Matrix

from utils.api import get_input

inp = get_input(13)
total = 0
for i, line in enumerate(inp.splitlines()):
    n = i % 4
    if n == 0:
        ax, ay = [
            int("".join([y for y in x if y.isnumeric()])) for x in line.split(", Y+")
        ]
    elif n == 1:
        bx, by = [
            int("".join([y for y in x if y.isnumeric()])) for x in line.split(", Y+")
        ]
    elif n == 2:
        goalx, goaly = [
            int("".join([y for y in x if y.isnumeric()])) + 10000000000000
            for x in line.split(", Y")
        ]

        # a = np.array([[ax, bx], [ay, by]])
        # b = np.array([goalx, goaly])
        # solution = np.linalg.solve(a, b)

        a = Matrix([[ax, bx], [ay, by]])
        b = Matrix([goalx, goaly])
        solution = a.solve(b)
        if solution[0].is_integer and solution[1].is_integer:
            total += int(solution[0]) * 3 + int(solution[1])
print(total)
