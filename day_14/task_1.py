from collections import Counter


def read_input(path: str):
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    template, rules = read_input("day_14/input.txt")
    rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.splitlines()}

    for _ in range(10):
        new_template = template[0]
        for i in range(len(template) - 1):
            pair = template[i : i + 2]
            if rules.get(pair):
                new_template += rules[pair] + pair[1]
            else:
                new_template += pair[1]
        template = new_template

    c = Counter(template).most_common()
    print(c[0][1] - c[-1][1])
