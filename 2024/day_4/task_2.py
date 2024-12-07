import numpy as np

from utils.read_input import read_input_as_matrix


def find_word(words):
    if "".join(np.diag(words)) in ["MAS", "SAM"] and "".join(
        np.diag(np.fliplr(words))
    ) in ["MAS", "SAM"]:
        return 1
    return 0


if __name__ == "__main__":
    found_words = 0
    words = np.array(read_input_as_matrix("2024/day_4/input.txt"))
    for i in range(len(words) - 2):
        for j in range(len(words) - 2):
            found_words += find_word(words[i : i + 3, j : j + 3])
    print(found_words)
