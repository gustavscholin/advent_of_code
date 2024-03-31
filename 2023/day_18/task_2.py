import re

from utils.read_input import read_input

if __name__ == "__main__":
    dig_plan = read_input("2023/day_18/input.txt")
    area = 0
    nb_edge_points = 0
    p1 = (0, 0)
    for edge in dig_plan:
        instruction = re.search(r"\(\#(.*?)\)", edge).group(1)
        length = int(instruction[:-1], base=16)
        dir = int(instruction[-1])

        if dir == 0:
            p2 = (p1[0] + length, p1[1])
        elif dir == 2:
            p2 = (p1[0] - length, p1[1])
        elif dir == 3:
            p2 = (p1[0], p1[1] + length)
        elif dir == 1:
            p2 = (p1[0], p1[1] - length)

        area += 0.5 * (p1[0] * p2[1] - p1[1] * p2[0])
        nb_edge_points += length
        p1 = p2

    # Modified Pick's theorem, i + b = A + b/2 + 1
    print(int(abs(area) + 0.5 * nb_edge_points + 1))
