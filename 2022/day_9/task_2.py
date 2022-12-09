from utils.read_input import read_input


def is_connected(pos_1, pos_2):
    for i in range(pos_2[0] - 1, pos_2[0] + 2):
        for j in range(pos_2[1] - 1, pos_2[1] + 2):
            if pos_1 == (i, j):
                return True
    return False


def get_straight_coord(follower_coord, lead_coord):
    if follower_coord < lead_coord:
        return 1
    elif follower_coord > lead_coord:
        return -1
    return 0


if __name__ == "__main__":
    motions = read_input("2022/day_9/input.txt")
    dirs = {
        "U": (1, 0),
        "R": (0, 1),
        "L": (0, -1),
        "D": (-1, 0),
    }
    knots = {i: (0, 0) for i in range(10)}
    positions = {knots[9]}
    for motion in motions:
        dir, steps = motion.split()
        for _ in range(int(steps)):
            knots[0] = tuple(knots[0][i] + dirs[dir][i] for i in range(2))
            for k in range(1, 10):
                if not is_connected(knots[k - 1], knots[k]):
                    if sum(abs(knots[k - 1][i] - knots[k][i]) for i in range(2)) == 2:
                        straight = tuple(
                            get_straight_coord(knots[k][i], knots[k - 1][i])
                            for i in range(2)
                        )
                        knots[k] = tuple(knots[k][i] + straight[i] for i in range(2))
                    else:
                        diag = tuple(
                            1 if knots[k][i] < knots[k - 1][i] else -1 for i in range(2)
                        )
                        knots[k] = tuple(knots[k][i] + diag[i] for i in range(2))
            positions.add(knots[9])
    print(len(positions))
