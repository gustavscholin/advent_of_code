from itertools import combinations


def read_input(path):
    with open(path, "r") as f:
        input_list = f.read().splitlines()
    return [int(i) for i in input_list]


if __name__ == "__main__":
    exp_rep = read_input("2020/day_1/input.txt")
    prod = None
    for ent_1, ent_2 in combinations(exp_rep, 2):
        if ent_1 + ent_2 == 2020:
            prod = ent_1 * ent_2

    print(prod)
