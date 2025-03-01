import re

from utils.read_input import read_input


def print_robots():
    for j in range(y_len):
        s = ""
        for i in range(x_len):
            s += "#" if (i, j) in poses else "."
        print(s)
    print()
    print()
    print()


def get_neighbors(pos):
    return [(pos[0] + dir[0], pos[1] + dir[1]) for dir in dirs]


def discover(pos):
    found.add(pos)
    cluster.add(pos)
    for n in get_neighbors(pos):
        if n in poses and n not in found:
            discover(n)


if __name__ == "__main__":
    robots = [
        [
            list(map(int, g.split(",")))
            for g in re.match(r"p=(\d+,\d+) v=(-?\d+,-?\d+)", s).groups()
        ]
        for s in read_input("2024/day_14/input.txt")
    ]
    x_len = 101
    y_len = 103
    sec = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while True:
        poses = set()
        for i in range(len(robots)):
            p, v = robots[i]
            robots[i][0] = [(p[0] + v[0]) % x_len, (p[1] + v[1]) % y_len]
            poses.add(tuple(robots[i][0]))
        sec += 1

        found = set()
        for pos in poses:
            cluster = set()
            if pos not in found:
                discover(pos)

            if len(cluster) > 50:
                break

        if len(cluster) > 50:
            break

    print_robots()
    print(sec)
