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

    sign_scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    scores = []
    for line in lines:
        queue = deque()
        corrupted = False
        score = 0
        for c in line:
            if c in signs.keys():
                queue.append(c)
            elif c == signs[queue[-1]]:
                queue.pop()
            else:
                corrupted = True
                break
        if corrupted:
            continue
        for _ in range(len(queue)):
            score *= 5
            score += sign_scores[signs[queue.pop()]]
        scores.append(score)

    print(sorted(scores)[len(scores) // 2])
