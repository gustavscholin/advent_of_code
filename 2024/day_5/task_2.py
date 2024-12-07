def check_rule(rule, pages: list):
    x, y = rule
    if x in pages and y in pages:
        return pages.index(x) < pages.index(y)
    return True


if __name__ == "__main__":
    with open("2024/day_5/input.txt", "r") as f:
        rules_list, pages_list = f.read().split("\n\n")
        rules = [
            [int(r) for r in rules.split("|")] for rules in rules_list.splitlines()
        ]
        pages_list = [
            [int(p) for p in pages.split(",")] for pages in pages_list.splitlines()
        ]

    middle_correct = 0
    for i in range(len(pages_list)):
        if not all([check_rule(rule, pages_list[i]) for rule in rules]):
            j = 0
            while j < len(rules):
                if not check_rule(rules[j], pages_list[i]):
                    x_idx = pages_list[i].index(rules[j][0])
                    y_idx = pages_list[i].index(rules[j][1])
                    pages_list[i][x_idx] = rules[j][1]
                    pages_list[i][y_idx] = rules[j][0]
                    j = 0
                else:
                    j += 1

            middle_correct += pages_list[i][(len(pages_list[i]) - 1) // 2]
    print(middle_correct)
