import re
from utils.read_input import read_input

if __name__ == "__main__":
    calibration_document = read_input("2023/day_1/input.txt")
    numbers_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    sum = 0
    for s in calibration_document:
        numbers = re.findall(r"(?=(\d|" + r"|".join(numbers_dict.keys()) + r"))", s)
        first, last = "".join(
            [
                numbers_dict[numbers[i]] if numbers[i] in numbers_dict else numbers[i]
                for i in [0, -1]
            ]
        )
        sum += int(first + last)
    print(sum)
