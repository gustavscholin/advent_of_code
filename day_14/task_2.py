from collections import Counter, defaultdict


def read_input(path: str):
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    template, rules = read_input("day_14/input.txt")
    rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.splitlines()}

    char_counts = defaultdict(int)
    pair_counts = defaultdict(int)

    for i in range(len(template) - 1):
        pair_counts[template[i : i + 2]] += 1
        char_counts[template[i]] += 1
    char_counts[template[-1]] += 1

    for _ in range(40):
        new_pair_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            new_pair_1 = pair[0] + rules[pair]
            new_pair_2 = rules[pair] + pair[1]
            if pair == new_pair_1:
                new_pair_counts[new_pair_1] = count
            else:
                new_pair_counts[new_pair_1] = (pair_counts.get(new_pair_1) or 0) + count
                new_pair_counts[pair] = 0
            if pair == new_pair_2:
                new_pair_counts[new_pair_2] = count
            else:
                new_pair_counts[new_pair_2] = (pair_counts.get(new_pair_2) or 0) + count
                new_pair_counts[pair] = 0
        pair_counts = new_pair_counts

    pass

    c = Counter(template).most_common()
    print(c[0][1] - c[-1][1])
