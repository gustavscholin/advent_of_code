def read_input(path: str):
    with open(path, "r") as f:
        return [int(s.split(": ")[1]) for s in f.read().splitlines()]


def one_based_modulo(a, n):
    return ((a - 1) % n) + 1


if __name__ == "__main__":
    pos = read_input("2021/day_21/input.txt")
    scores = [0, 0]
    turn = 0
    dice_rolls = 0

    while all(s < 1000 for s in scores):
        roll = one_based_modulo(dice_rolls, 100) * 3 + 6
        pos[turn] = one_based_modulo(pos[turn] + roll, 10)
        scores[turn] += pos[turn]

        dice_rolls += 3
        turn = 0 if turn else 1

    print(scores[turn] * dice_rolls)
