from utils.read_input import read_input_single_line
from copy import deepcopy

if __name__ == "__main__":
    fishes = read_input_single_line("day_6/input.txt", "int")
    fishes = {i: fishes.count(i) for i in range(9)}
    for _ in range(256):
        due_fishes = fishes[0]
        old_fishes = deepcopy(fishes)
        for i in range(8):
            fishes[i] = old_fishes[i + 1]
        fishes[6] += due_fishes
        fishes[8] = due_fishes

    print(sum(fishes.values()))
