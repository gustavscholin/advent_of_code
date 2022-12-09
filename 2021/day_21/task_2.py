from collections import defaultdict


def read_input(path: str):
    with open(path, "r") as f:
        return [int(s.split(": ")[1]) for s in f.read().splitlines()]


def one_based_modulo(a, n):
    return ((a - 1) % n) + 1


if __name__ == "__main__":
    p1, p2 = read_input("2021/day_21/input.txt")
    universes = defaultdict(int)
    universes[((p1, 0), (p2, 0))] = 1
    turn = 0
    wins = [0, 0]
    rolls = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }

    while universes:
        new_universes = defaultdict(int)
        for state in universes.keys():
            for roll, multiplier in rolls.items():
                new_pos = one_based_modulo(state[turn][0] + roll, 10)
                new_score = state[turn][1] + new_pos
                if new_score >= 21:
                    wins[turn] += universes[state] * multiplier
                else:
                    new_state = (
                        (state[0], (new_pos, new_score))
                        if turn
                        else ((new_pos, new_score), state[1])
                    )
                    new_universes[new_state] += universes[state] * multiplier
        turn = 0 if turn else 1
        universes = new_universes

    print(max(wins))
