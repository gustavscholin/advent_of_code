from copy import deepcopy


def read_input(path: str):
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    coords, folds = read_input("day_13/input.txt")
    fold = folds.splitlines()[0].strip("fold along ").split("=")
    coords = [[int(i) for i in coord.split(",")] for coord in coords.splitlines()]

    line = int(fold[1])
    axis = fold[0]
    new_coords = set()
    dim = 0 if axis == "x" else 1
    for coord in coords:
        if coord[dim] <= line:
            new_coords.add(tuple(coord))
        elif coord[dim] > line:
            new_coord = deepcopy(coord)
            new_coord[dim] = line - (coord[dim] - line)
            new_coords.add(tuple(new_coord))

    print(len(new_coords))
