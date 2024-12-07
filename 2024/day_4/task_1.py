import re

import numpy as np

from utils.read_input import read_input_as_matrix


def find_word(words):
    return len(re.findall(r"XMAS", "".join(words)))


if __name__ == "__main__":
    found_words = 0
    words = np.array(read_input_as_matrix("2024/day_4/input.txt"))
    for i in range(len(words)):
        found_words += find_word(words[i, :])
        found_words += find_word(np.flip(words[i, :]))
        found_words += find_word(words[:, i])
        found_words += find_word(np.flip(words[:, i]))
        found_words += find_word(np.diag(words, i))
        found_words += find_word(np.flip(np.diag(words, i)))
        found_words += find_word(np.diag(np.fliplr(words), i))
        found_words += find_word(np.flip(np.diag(np.fliplr(words), i)))
        if i > 0:
            found_words += find_word(np.diag(words, -i))
            found_words += find_word(np.flip(np.diag(words, -i)))
            found_words += find_word(np.diag(np.fliplr(words), -i))
            found_words += find_word(np.flip(np.diag(np.fliplr(words), -i)))
    print(found_words)
