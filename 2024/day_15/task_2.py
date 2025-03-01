from copy import deepcopy


def follow_hdir(inx, iny, dir):
    x = inx + dir
    while warehouse[iny][x] in ("[", "]"):
        x = x + dir
    return x


def follow_vdir(x, y, dir):
    if moving_from:
        loc = warehouse[y][x]
        if loc == "#":
            moving_from.clear()
        elif loc in ("[", "]"):
            moving_from.add((x, y))
            follow_vdir(x, y + dir, dir)
            nx = x + 1 if loc == "[" else x - 1
            if (nx, y) not in moving_from:
                follow_vdir(nx, y, dir)


if __name__ == "__main__":
    with open("2024/day_15/input.txt") as f:
        lines, steps = f.read().split("\n\n")

    warehouse = []
    for j, line in enumerate(lines.splitlines()):
        new_line = line.replace("#", "##")
        new_line = new_line.replace("O", "[]")
        new_line = new_line.replace(".", "..")
        new_line = new_line.replace("@", "@.")
        warehouse.append(list(new_line))
        if "@" in line:
            i = line.index("@")
            rx, ry = i * 2, j

    steps = steps.replace("\n", "")

    dirs = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}
    for step in steps:
        hdir, vdir = dirs[step]
        if vdir == 0:
            nx = follow_hdir(rx, ry, hdir)
            if warehouse[ry][nx] == ".":
                if hdir == 1:
                    warehouse[ry].insert(rx, ".")
                    del warehouse[ry][nx + 1]
                else:
                    warehouse[ry].insert(rx + 1, ".")
                    del warehouse[ry][nx]
                rx += hdir
        else:
            moving_from = {(rx, ry)}
            follow_vdir(rx, ry + vdir, vdir)
            if moving_from:
                moving_to = set()
                new_warehouse = deepcopy(warehouse)
                for x, y in moving_from:
                    new_warehouse[y + vdir][x] = warehouse[y][x]
                    moving_to.add((x, y + vdir))
                for x, y in moving_from - moving_to:
                    new_warehouse[y][x] = "."
                warehouse = new_warehouse
                ry += vdir

    print(
        sum(
            [
                j * 100 + i
                for j in range(len(warehouse))
                for i in range(len(warehouse[j]))
                if warehouse[j][i] == "["
            ]
        )
    )
