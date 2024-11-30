import os

for x in range(1, 33):
    path = os.path.join(os.path.dirname(__file__), f"../day {x:02d}")
    if not os.path.exists(path):
        os.mkdir(path)
        for part in range(1, 3):
            with open(os.path.join(path, f"part {part}.py"), "w") as f:
                f.write(
                    f'import os\nimport sys\n\nsys.path.append(os.path.join(os.path.dirname(__file__), "../"))\n\nfrom utils.api import get_input\n\ninp = get_input({x})\n'
                )
        print(f"Created day {x}! Good luck.")
        break
