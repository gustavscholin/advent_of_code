import numpy as np
from utils.read_input import read_input_as_matrix

if __name__ == "__main__":
    forest = np.array(read_input_as_matrix("2022/day_8/input.txt", "int"))
    width, height = forest.shape
    visable_trees = width * 2 + height * 2 - 4
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            tree = forest[i, j]
            if (
                np.all(forest[i, :j] < tree)
                or np.all(forest[i, j + 1 :] < tree)
                or np.all(forest[:i, j] < tree)
                or np.all(forest[i + 1 :, j] < tree)
            ):
                visable_trees += 1
    print(visable_trees)
