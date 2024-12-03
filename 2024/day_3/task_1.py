import re

from utils.read_input import read_input

if __name__ == "__main__":
    sum = 0
    for line in read_input("2024/day_3/input.txt"):
        enabled = True
        for n1, n2 in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line):
            sum += int(n1) * int(n2)
    print(sum)
