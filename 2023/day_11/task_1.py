from copy import deepcopy
from itertools import combinations

from utils.read_input import read_input

if __name__ == "__main__":
    image = read_input("2023/day_11/input.txt")

    expanded_image = deepcopy(image)
    h_insert_idxs = []
    v_insert_idxs = []

    for i in range(len(image)):
        if not "#" in image[i]:
            h_insert_idxs.append(i)
        if not "#" in "".join([l[i] for l in image]):
            v_insert_idxs.append(i)

    for i, insert_idx in enumerate(h_insert_idxs):
        expanded_image.insert(insert_idx + i, "." * len(expanded_image[0]))
    for i, insert_idx in enumerate(v_insert_idxs):
        for j in range(len(expanded_image)):
            expanded_image[j] = (
                expanded_image[j][: insert_idx + i]
                + "."
                + expanded_image[j][insert_idx + i :]
            )

    galaxies = []
    for i in range(len(expanded_image)):
        for j in range(len(expanded_image[0])):
            if expanded_image[i][j] == "#":
                galaxies.append((i, j))

    path_sum = 0
    for x, y in combinations(galaxies, 2):
        path_sum += abs(x[0] - y[0]) + abs(x[1] - y[1])
    print(path_sum)
