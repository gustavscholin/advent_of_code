import numpy as np


def read_input(path: str):
    with open(path) as f:
        return [np.array([int(i) for i in l.split(",")]) for l in f.read().splitlines()]


if __name__ == "__main__":
    droplet_coords = read_input("2022/day_18/input.txt")

    open_sides = len(droplet_coords) * 6
    for i in range(len(droplet_coords)):
        for j in range(i + 1, len(droplet_coords)):
            if sum(np.abs(droplet_coords[i] - droplet_coords[j])) == 1:
                open_sides -= 2

    print(open_sides)
