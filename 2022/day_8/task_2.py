import numpy as np
from utils.read_input import read_input_as_matrix


def get_score(view_tree, tree_list):
    visable_trees = 0
    for tree in tree_list:
        if tree < view_tree:
            visable_trees += 1
        else:
            visable_trees += 1
            break
    return visable_trees


if __name__ == "__main__":
    forest = np.array(read_input_as_matrix("2022/day_8/input.txt", "int"))
    width, height = forest.shape
    scenic_scores = []
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            tree = forest[i, j]
            left_score = get_score(tree, np.flip(forest[i, :j]))
            right_score = get_score(tree, forest[i, j + 1 :])
            up_score = get_score(tree, np.flip(forest[:i, j]))
            down_score = get_score(tree, forest[i + 1 :, j])
            scenic_scores.append(left_score * right_score * up_score * down_score)
    print(max(scenic_scores))
