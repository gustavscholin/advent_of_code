from collections import defaultdict


def read_input(path: str):
    with open(path) as f:
        return [tuple([int(i) for i in l.split(",")]) for l in f.read().splitlines()]


if __name__ == "__main__":
    droplet_coords = read_input("2022/day_18/input.txt")

    air_coords = defaultdict(int)

    for coord in droplet_coords:
        air_coords[coord] = -1

    open_sides = 0
    for coord in droplet_coords:
        for d in (-1, 1):
            for d_coord in [
                (coord[0] + d, coord[1], coord[2]),
                (coord[0], coord[1] + d, coord[2]),
                (coord[0], coord[1], coord[2] + d),
            ]:
                if air_coords[d_coord] != -1:
                    air_coords[d_coord] += 1
                    open_sides += 1
                    if air_coords[d_coord] == 6:
                        open_sides -= 6

    print(open_sides)
