import re


def read_input(path: str):
    with open(path, "r") as f:
        return [int(i) for i in re.findall(r"-?\d+", f.read())]


def traj_in_target(x_vel, y_vel):
    if sum(range(x_vel + 1)) < x_range[0]:
        return False
    step = 0
    x = 0
    y = 0
    while True:
        x += max(x_vel - step, 0)
        y += y_vel - step
        if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
            return True
        if x > x_range[1] or y < y_range[0]:
            return False
        step += 1


if __name__ == "__main__":
    target = read_input("day_17/input.txt")
    x_range = target[:2]
    y_range = target[2:]

    x_min = 1
    x_max = x_range[1]
    y_min = y_range[0]
    y_max = abs(y_range[0]) - 1

    valid_vels = []
    for x_vel in range(x_min, x_max + 1):
        for y_vel in range(y_min, y_max + 1):
            if traj_in_target(x_vel, y_vel):
                valid_vels.append((x_vel, y_vel))

    print(len(valid_vels))
