import numpy as np

from utils.read_input import read_input

if __name__ == "__main__":
    digit_list = read_input("day_8/input.txt")
    digit_list = np.array([[len(i) for i in digits.split("|")[1].split()] for digits in digit_list])

    digit_list = np.where(np.isin(digit_list, [2, 3, 4, 7]), 1, 0)
    print(np.sum(digit_list))
