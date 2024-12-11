from collections import defaultdict
from itertools import permutations

from utils.read_input import read_input_as_matrix


def oob(pos):
    limit = len(antennas_map)
    return any(0 > i or i >= limit for i in pos)


if __name__ == "__main__":
    antennas_map = read_input_as_matrix("2024/day_8/input.txt")
    antennas = defaultdict(list)
    for i, line in enumerate(antennas_map):
        for j, char in enumerate(line):
            if char != ".":
                antennas[char].append((i, j))

    anti_nodes = set()
    for antenna, positions in antennas.items():
        for a, b in permutations(positions, 2):
            dx, dy = a[0] - b[0], a[1] - b[1]
            if not oob((a[0] + dx, a[1] + dy)):
                anti_nodes.add((a[0] + dx, a[1] + dy))
    print(len(anti_nodes))