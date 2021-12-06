import numpy as np
from utils.read_input import read_input_single_line

if __name__ == "__main__":
    fishes = np.array(read_input_single_line("day_6/input.txt", "int"))
    for _ in range(80):
        fishes -= 1
        due_fishes = np.where(fishes == -1)
        fishes[due_fishes] = 6
        fishes = np.append(fishes, np.ones(len(due_fishes[0]), int) * 8)

    print(len(fishes))
