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
    for pages in pages_list:
        if all([check_rule(rule, pages) for rule in rules]):
            middle_correct += pages[(len(pages) - 1) // 2]
    print(middle_correct)
