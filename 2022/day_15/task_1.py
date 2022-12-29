import re
from collections import defaultdict
from utils.read_input import read_input

if __name__ == "__main__":
    lines = read_input("2022/day_15/input.txt")
    positions = defaultdict(str)
    pos_cnt = 0
    y_line = 2_000_000

    for l in lines:
        s_x, s_y, b_x, b_y = map(int, re.findall(r"\d+", l))
        positions[(s_x, s_y)] = "S"
        positions[(b_x, b_y)] = "B"
        dist = abs(s_x - b_x) + abs(s_y - b_y)
        y_dist = abs(s_y - y_line)
        if dist >= y_dist:
            for x in range(s_x - (dist - y_dist), s_x + (dist - y_dist) + 1):
                if not positions[(x, y_line)]:
                    positions[(x, y_line)] = "#"
                    pos_cnt += 1

    print(pos_cnt)
