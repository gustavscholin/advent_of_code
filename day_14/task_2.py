from collections import defaultdict
from copy import deepcopy


def read_input(path: str):
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    template, rules = read_input("day_14/input.txt")
    rules = {
        rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.splitlines()
    }

    char_counts = defaultdict(int)
    pair_counts = defaultdict(int)

    for i in range(len(template) - 1):
        pair_counts[template[i : i + 2]] += 1
        char_counts[template[i]] += 1
    char_counts[template[-1]] += 1

    for _ in range(40):
        new_pair_counts = deepcopy(pair_counts)
        for pair, count in pair_counts.items():
            new_pair_1 = pair[0] + rules[pair]
            new_pair_2 = rules[pair] + pair[1]
            new_pair_counts[new_pair_1] += count
            new_pair_counts[new_pair_2] += count
            new_pair_counts[pair] -= count
            char_counts[rules[pair]] += count
        pair_counts = new_pair_counts

    counts = sorted(char_counts.values())
    print(counts[-1] - counts[0])
