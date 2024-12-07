from copy import deepcopy

import numpy as np

from utils.read_input import read_input_as_matrix


def add(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


def oob(pos):
    limit = len(guard_map)
    return any(0 > i or i >= limit for i in pos)


def loop(new_map, pos, dir):
    hist = {(pos, dir)}
    while not oob(add(pos, dir)):
        while new_map[add(pos, dir)] == "#":
            dir = turn_map[dir]
        if (add(pos, dir), dir) in hist:
            return True
        else:
            hist.add((pos, dir))
            pos = add(pos, dir)
    return False


if __name__ == "__main__":
    guard_map = np.array(read_input_as_matrix("2024/day_6/input.txt"))
    starting_pos = tuple(i[0] for i in np.where(guard_map == "^"))
    pos = starting_pos
    dir = (-1, 0)
    turn_map = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }
    path = {starting_pos}
    positions = set()
    while not oob(add(pos, dir)):
        while guard_map[add(pos, dir)] == "#":
            dir = turn_map[dir]
        if add(pos, dir) != starting_pos and add(pos, dir) not in path:
            new_map = deepcopy(guard_map)
            new_map[add(pos, dir)] = "#"
            if loop(new_map, pos, dir):
                positions.add(add(pos, dir))
        pos = add(pos, dir)
        path.add(pos)
    print(len(positions))
