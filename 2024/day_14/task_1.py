import re

from utils.read_input import read_input

if __name__ == "__main__":
    robots = [
        [
            list(map(int, g.split(",")))
            for g in re.match(r"p=(\d+,\d+) v=(-?\d+,-?\d+)", s).groups()
        ]
        for s in read_input("2024/day_14/input.txt")
    ]
    x_len = 101
    y_len = 103
    x_middle = x_len // 2
    y_middle = y_len // 2
    quad_00, quad_10, quad_01, quad_11 = 0, 0, 0, 0
    for p, v in robots:
        px, py = [(p[0] + v[0] * 100) % x_len, (p[1] + v[1] * 100) % y_len]
        if px < x_middle and py < y_middle:
            quad_00 += 1
        elif px > x_middle and py < y_middle:
            quad_10 += 1
        elif px < x_middle and py > y_middle:
            quad_01 += 1
        elif px > x_middle and py > y_middle:
            quad_11 += 1
    print(quad_00 * quad_10 * quad_01 * quad_11)
