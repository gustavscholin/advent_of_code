import re
from utils.read_input import read_input
from collections import Counter


def get_range(a, b):
    if a <= b:
        return range(a, b + 1)
    else:
        return range(a, b - 1, -1)


if __name__ == "__main__":
    lines = read_input("day_5/input.txt")
    points = []
    for line in lines:
        coords = [int(i) for i in re.findall(r"\d+", line)]
        if coords[0] == coords[2]:
            points.extend([(coords[0], i) for i in get_range(coords[1], coords[3])])
        elif coords[1] == coords[3]:
            points.extend([(i, coords[1]) for i in get_range(coords[0], coords[2])])
        else:
            points.extend([(i, j) for i, j in zip(get_range(coords[0], coords[2]), get_range(coords[1], coords[3]))])
            pass

    c = Counter(points)

    overlaps = 0
    for point, count in c.most_common():
        if count > 1:
            overlaps += 1
        else:
            break

    print(overlaps)
