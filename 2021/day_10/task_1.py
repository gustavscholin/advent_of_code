from collections import deque
from utils.read_input import read_input

if __name__ == "__main__":
    lines = read_input("day_10/input.txt")

    signs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    total_score = 0
    for line in lines:
        queue = deque()
        for c in line:
            if c in signs.keys():
                queue.append(c)
            elif c == signs[queue[-1]]:
                queue.pop()
            else:
                total_score += scores[c]
                break

    print(total_score)
