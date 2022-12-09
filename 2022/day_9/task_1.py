from utils.read_input import read_input


def is_connected(pos_1, pos_2):
    for i in range(pos_2[0] - 1, pos_2[0] + 2):
        for j in range(pos_2[1] - 1, pos_2[1] + 2):
            if pos_1 == (i, j):
                return True
    return False


if __name__ == "__main__":
    motions = read_input("2022/day_9/input.txt")
    dirs = {
        "U": (1, 0),
        "R": (0, 1),
        "L": (0, -1),
        "D": (-1, 0),
    }
    head_pos, tail_pos = (0, 0), (0, 0)
    positions = {tail_pos}
    for motion in motions:
        dir, steps = motion.split()
        for _ in range(int(steps)):
            head_pos = tuple(head_pos[i] + dirs[dir][i] for i in range(2))
            if not is_connected(head_pos, tail_pos):
                if sum(abs(head_pos[i] - tail_pos[i]) for i in range(2)) == 2:
                    tail_pos = tuple(tail_pos[i] + dirs[dir][i] for i in range(2))
                else:
                    diag = tuple(
                        1 if tail_pos[i] < head_pos[i] else -1 for i in range(2)
                    )
                    tail_pos = tuple(tail_pos[i] + diag[i] for i in range(2))
                positions.add(tail_pos)
    print(len(positions))
