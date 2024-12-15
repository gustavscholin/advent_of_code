from collections import defaultdict

from utils.read_input import read_input_as_matrix


def get_neighbors(pos):
    return [(pos[0] + dir[0], pos[1] + dir[1]) for dir in dirs]


def get_plant(pos):
    return garden_map[pos[0]][pos[1]] if iob(pos) else None


def iob(pos):
    return 0 <= pos[0] < len(garden_map) and 0 <= pos[1] < len(garden_map)


def discover(pos, region):
    plant = get_plant(pos)
    found[pos] = region
    regions[region]["area"] += 1
    for n in get_neighbors(pos):
        n_plant = get_plant(n)
        if not iob(n) or n_plant != plant:
            regions[region]["perimeter"] += 1
        if n in found:
            continue
        if iob(n) and n_plant == plant:
            discover(n, region)


if __name__ == "__main__":
    garden_map = read_input_as_matrix("2024/day_12/input.txt")
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    found = {}
    regions = defaultdict(lambda: {"area": 0, "perimeter": 0})
    region_cnt = 0
    for i in range(len(garden_map)):
        for j in range(len(garden_map)):
            if (i, j) not in found:
                discover((i, j), region_cnt)
                region_cnt += 1

    print(sum([v["area"] * v["perimeter"] for v in regions.values()]))
