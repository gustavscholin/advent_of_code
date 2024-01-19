from collections import defaultdict

import numpy as np


def read_input(path: str):
    with open(path, "r") as f:
        return f.read().strip()


def get_rock(num_rocks, top):
    rock_index = num_rocks % 5
    rock_bottom = top + 4

    match rock_index:
        case 0:
            rock = np.array(
                [[2, rock_bottom], [3, rock_bottom], [4, rock_bottom], [5, rock_bottom]]
            )
        case 1:
            rock = np.array(
                [
                    [2, rock_bottom + 1],
                    [3, rock_bottom + 2],
                    [3, rock_bottom + 1],
                    [3, rock_bottom],
                    [4, rock_bottom + 1],
                ]
            )
        case 2:
            rock = np.array(
                [
                    [2, rock_bottom],
                    [3, rock_bottom],
                    [4, rock_bottom],
                    [4, rock_bottom + 1],
                    [4, rock_bottom + 2],
                ]
            )
        case 3:
            rock = np.array(
                [
                    [2, rock_bottom],
                    [2, rock_bottom + 1],
                    [2, rock_bottom + 2],
                    [2, top + 7],
                ]
            )
        case 4:
            rock = np.array(
                [
                    [2, rock_bottom],
                    [2, rock_bottom + 1],
                    [3, rock_bottom],
                    [3, rock_bottom + 1],
                ]
            )
    return rock


if __name__ == "__main__":
    jet_pattern = read_input("2022/day_17/input.txt")
    time = 0
    rocks = 0
    top_points = [0] * 7
    new_rock = True
    rested_rock = defaultdict(bool)
    for i in range(7):
        rested_rock[(i, 0)] = True

    while rocks <= 2022:
        if new_rock:
            rock = get_rock(rocks, max(top_points))
            rocks += 1
            new_rock = False

        jet_push = jet_pattern[time % len(jet_pattern)]
        if (
            jet_push == "<"
            and min(rock[:, 0]) > 0
            and not any([rested_rock[(i - 1, j)] for i, j in rock])
        ):
            rock[:, 0] -= 1
        elif (
            jet_push == ">"
            and max(rock[:, 0]) < 6
            and not any([rested_rock[(i + 1, j)] for i, j in rock])
        ):
            rock[:, 0] += 1

        if any([rested_rock[(i, j - 1)] for i, j in rock]):
            for i in range(7):
                pot_tops = rock[rock[:, 0] == i]
                if pot_tops.size > 0 and max(pot_tops[:, 1]) > top_points[i]:
                    top_points[i] = max(pot_tops[:, 1])
            for i, j in rock:
                rested_rock[(i, j)] = True
            new_rock = True
        else:
            rock[:, 1] -= 1
        time += 1

    print(max(top_points))
