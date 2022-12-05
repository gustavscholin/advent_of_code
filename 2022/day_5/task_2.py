import re
from collections import defaultdict


def read_input(path: str):
    with open(path, "r") as f:
        stacks_str, procedure_str = f.read().split("\n\n")

        stacks = defaultdict(list)
        stacks_lines = stacks_str.splitlines()
        stack_ref = stacks_lines.pop(-1)

        for line in stacks_lines:
            for i, c in enumerate(line):
                if stack_ref[i] != " " and c != " ":
                    stacks[stack_ref[i]].append(c)

        steps = [re.findall(r"\d+", s) for s in procedure_str.splitlines()]
        return stacks, steps


if __name__ == "__main__":
    stacks, steps = read_input("2022/day_5/input.txt")
    for num, from_stack, to_stack in steps:
        crates = stacks[from_stack][: int(num)]
        stacks[from_stack] = stacks[from_stack][int(num) :]
        stacks[to_stack] = crates + stacks[to_stack]
    print("".join([stacks[stack][0] for stack in sorted(stacks.keys())]))
