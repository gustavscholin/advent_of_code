import numpy as np

from utils.read_input import read_input


def get_basin(point):
    if heightmap[point[0]][point[1]] == 9 or point[0] < 0 or point[1] < 0:
        return None
    for basin in basins:
        if point in basin:
            return basin
    return None


if __name__ == "__main__":
    heightmap = read_input("day_9/input.txt")
    heightmap = [[int(i) for i in row] for row in heightmap]

    basins = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if heightmap[i][j] == 9:
                continue
            x = get_basin((i, j - 1))
            y = get_basin((i - 1, j))
            if x is None and y is None:
                basins.append(set([(i, j)]))
            elif x == y or y is None:
                basins.remove(x)
                x.add((i, j))
                basins.append(x)
            elif x is None:
                basins.remove(y)
                y.add((i, j))
                basins.append(y)
            elif x != y:
                basins.remove(x)
                basins.remove(y)
                basins.append(set.union(x, y, set([(i, j)])))

    basin_sizes = sorted([len(b) for b in basins], reverse=True)
    basin_1, basin_2, basin_3 = basin_sizes[:3]
    print(basin_1 * basin_2 * basin_3)
