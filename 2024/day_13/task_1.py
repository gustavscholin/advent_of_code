import re

import numpy as np


def check_integer(num):
    return abs(num - round(num)) < 0.0001


if __name__ == "__main__":
    with open("2024/day_13/input.txt", "r") as f:
        machines = [m.splitlines() for m in f.read().split("\n\n")]

    prize_sum = 0
    for machine in machines:
        ax, ay = [int(i) for i in re.findall("\d+", machine[0])]
        bx, by = [int(i) for i in re.findall("\d+", machine[1])]
        px, py = [int(i) for i in re.findall("\d+", machine[2])]
        a, b = np.linalg.solve(np.array([[ax, bx], [ay, by]]), np.array([px, py]))

        if check_integer(a) and check_integer(b):
            prize_sum += round(a) * 3 + round(b)

    print(prize_sum)
