from collections import defaultdict

from utils.read_input import read_input


def get_range(a, b):
    return range(a, b + 1) if a < b else range(b, a + 1)


if __name__ == "__main__":
    structures = read_input("2022/day_14/input.txt")
    cave = defaultdict(str)
    start = (500, 0)
    max_vertical = 0
    for structure in structures:
        corners = [eval(s) for s in structure.split(" -> ")]
        for i in range(len(corners) - 1):
            for j in get_range(corners[i][0], corners[i + 1][0]):
                for k in get_range(corners[i][1], corners[i + 1][1]):
                    cave[(j, k)] = "#"
                    if k > max_vertical:
                        max_vertical = k

    resting_sands = 0
    static = False
    while not static:
        sand_pos = start
        moving = True
        while moving:
            if sand_pos[1] > max_vertical:
                moving = False
                static = True
            elif not cave[(sand_pos[0], sand_pos[1] + 1)]:
                sand_pos = (sand_pos[0], sand_pos[1] + 1)
            elif not cave[(sand_pos[0] - 1, sand_pos[1] + 1)]:
                sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
            elif not cave[(sand_pos[0] + 1, sand_pos[1] + 1)]:
                sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
            else:
                cave[sand_pos] = "o"
                resting_sands += 1
                moving = False
    print(resting_sands)
