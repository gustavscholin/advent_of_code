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

    for cd in corner_dirs:
        # Corner plant
        c_plant = get_plant((pos[0] + cd[0], pos[1] + cd[1]))
        # Vertical corner neighbor plant
        vcn_plant = get_plant((pos[0] + cd[0], pos[1]))
        # Horizontal corner neighbor plant
        hcn_plant = get_plant((pos[0], pos[1] + cd[1]))

        # Check outer and inner corner
        if plant not in (vcn_plant, hcn_plant):
            regions[region]["sides"] += 1
        elif vcn_plant == hcn_plant == plant and c_plant != plant:
            regions[region]["sides"] += 1

    for n in get_neighbors(pos):
        if n in found:
            continue
        if iob(n) and get_plant(n) == plant:
            discover(n, region)


if __name__ == "__main__":
    garden_map = read_input_as_matrix("2024/day_12/input.txt")
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    corner_dirs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    found = {}
    regions = defaultdict(lambda: {"area": 0, "sides": 0})
    region_cnt = 0
    for i in range(len(garden_map)):
        for j in range(len(garden_map)):
            if (i, j) not in found:
                discover((i, j), region_cnt)
                region_cnt += 1

    print(sum([v["area"] * v["sides"] for v in regions.values()]))
