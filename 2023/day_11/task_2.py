from itertools import combinations

from utils.read_input import read_input


def get_path_length(val_1, val_2, insert_idxs):
    return abs(val_1 - val_2) + 999_999 * sum(
        [1 for i in insert_idxs if val_1 < i < val_2 or val_2 < i < val_1]
    )


if __name__ == "__main__":
    image = read_input("2023/day_11/input.txt")

    h_insert_idxs = []
    v_insert_idxs = []

    for i in range(len(image)):
        if not "#" in image[i]:
            h_insert_idxs.append(i)
        if not "#" in "".join([l[i] for l in image]):
            v_insert_idxs.append(i)

    galaxies = []
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == "#":
                galaxies.append((i, j))

    path_sum = 0
    for gal_1, gal_2 in combinations(galaxies, 2):
        path_sum += get_path_length(
            gal_1[1], gal_2[1], v_insert_idxs
        ) + get_path_length(gal_1[0], gal_2[0], h_insert_idxs)
    print(path_sum)
