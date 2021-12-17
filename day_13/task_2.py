from copy import deepcopy


def read_input(path: str):
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    coords, folds = read_input("day_13/input.txt")
    folds = [fold.strip("fold along ").split("=") for fold in folds.splitlines()]
    coords = [[int(i) for i in coord.split(",")] for coord in coords.splitlines()]

    for axis, line in folds:
        line = int(line)
        new_coords = []
        dim = 0 if axis == "x" else 1
        for coord in coords:
            if coord[dim] <= line:
                new_coords.append(coord)
            elif coord[dim] > line:
                new_coord = deepcopy(coord)
                new_coord[dim] = line - (coord[dim] - line)
                new_coords.append(new_coord)
        coords = new_coords

    x_max = max([coord[0] for coord in coords])
    y_max = max([coord[1] for coord in coords])

    for i in range(y_max + 1):
        line = []
        for j in range(x_max + 1):
            if [j, i] in coords:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
