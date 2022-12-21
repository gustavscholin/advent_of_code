import re


def read_input(path: str):
    with open(path, "r") as f:
        monkeys = []
        for monkey_str in f.read().split("\n\n"):
            monkeys.append(
                {
                    "items": [
                        int(i)
                        for i in re.search(r"Starting items: (.*)", monkey_str)
                        .group(1)
                        .split(", ")
                    ],
                    "operation": re.search(r"Operation: (.*)", monkey_str).group(1),
                    "div": int(
                        re.search(r"Test: divisible by (\d+)", monkey_str).group(1)
                    ),
                    "true_monkey": int(
                        re.search(r"If true: throw to monkey (\d+)", monkey_str).group(
                            1
                        )
                    ),
                    "false_monkey": int(
                        re.search(r"If false: throw to monkey (\d+)", monkey_str).group(
                            1
                        )
                    ),
                }
            )
        return monkeys


if __name__ == "__main__":
    monkeys = read_input("2022/day_11/input.txt")
    inspects = [0] * len(monkeys)
    for _ in range(20):
        for i in range(len(monkeys)):
            items = monkeys[i]["items"]
            while items:
                old = items.pop()
                exec(monkeys[i]["operation"])
                new = new // 3
                if new % monkeys[i]["div"] == 0:
                    monkeys[monkeys[i]["true_monkey"]]["items"].append(new)
                else:
                    monkeys[monkeys[i]["false_monkey"]]["items"].append(new)
                inspects[i] += 1
    inspects.sort(reverse=True)
    print(inspects[0] * inspects[1])
