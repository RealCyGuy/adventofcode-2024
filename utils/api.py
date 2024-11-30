import os
from typing import AnyStr


def get_input(day: int) -> AnyStr:
    path = os.path.join(os.path.dirname(__file__), f"../inputs/day {day}.txt")

    if not os.path.exists(path):
        import requests

        with open(os.path.join(os.path.dirname(__file__), "../cookie.txt")) as f:
            cookies = {"session": f.read().strip()}
        response = requests.get(
            f"https://adventofcode.com/2024/day/{day}/input", cookies=cookies
        )
        if not response.ok:
            raise RuntimeError("not ok")
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()
