import re

from utils.read_input import read_input

if __name__ == "__main__":
    sum = 0
    enabled = True
    for line in read_input("2024/day_3/input.txt"):
        for n1, n2, do, dont in re.findall(
            r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", line
        ):
            if do:
                enabled = True
            elif dont:
                enabled = False
            elif enabled:
                sum += int(n1) * int(n2)
    print(sum)
