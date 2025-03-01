def follow_step(inx, iny, dir):
    x, y = inx + dir[0], iny + dir[1]
    while robot_map[y][x] == "O":
        x, y = x + dir[0], y + dir[1]
    return x, y


if __name__ == "__main__":
    with open("2024/day_15/input.txt") as f:
        robot_map, steps = f.read().split("\n\n")
    robot_map = [list(line) for line in robot_map.splitlines()]
    steps = steps.replace("\n", "")

    dirs = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}

    for j in range(len(robot_map)):
        for i in range(len(robot_map[j])):
            if robot_map[j][i] == "@":
                rx, ry = i, j

    for step in steps:
        dir = dirs[step]
        nx, ny = follow_step(rx, ry, dir)
        if robot_map[ny][nx] == ".":
            robot_map[ny][nx] = "O"
            robot_map[ry][rx] = "."
            rx, ry = rx + dir[0], ry + dir[1]
            robot_map[ry][rx] = "@"

    print(
        sum(
            [
                j * 100 + i
                for j in range(len(robot_map))
                for i in range(len(robot_map[j]))
                if robot_map[j][i] == "O"
            ]
        )
    )
