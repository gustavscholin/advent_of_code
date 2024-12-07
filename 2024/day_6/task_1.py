import numpy as np

from utils.read_input import read_input_as_matrix


def add(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


def oob(pos):
    limit = len(guard_map)
    return any(0 > i or i >= limit for i in pos)


if __name__ == "__main__":
    guard_map = np.array(read_input_as_matrix("2024/day_6/input.txt"))
    starting_pos = tuple(i[0] for i in np.where(guard_map == "^"))
    pos = starting_pos
    dir = (-1, 0)
    positions = {starting_pos}
    turn_map = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }
    while not oob(add(pos, dir)):
        while guard_map[add(pos, dir)] == "#":
            dir = turn_map[dir]
        pos = add(pos, dir)
        positions.add(pos)
    print(len(positions))
