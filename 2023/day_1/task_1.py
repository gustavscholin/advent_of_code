import re

from utils.read_input import read_input

if __name__ == "__main__":
    calibration_document = read_input("2023/day_1/input.txt")
    sum = 0
    for s in calibration_document:
        numbers = re.findall(r"\d", s)
        sum += int("".join([numbers[0], numbers[-1]]))
    print(sum)
