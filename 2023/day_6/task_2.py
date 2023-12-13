from math import ceil, floor, sqrt

from utils.read_input import read_input

if __name__ == "__main__":
    time, record = [
        int(line.split(":")[1].replace(" ", ""))
        for line in read_input("2023/day_6/input.txt")
    ]
    x1 = ceil((time / 2) - sqrt((time / 2) ** 2 - record))
    x2 = floor((time / 2) + sqrt((time / 2) ** 2 - record))
    print(x2 - x1 + 1)
