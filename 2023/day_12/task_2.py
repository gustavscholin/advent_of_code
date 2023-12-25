from functools import cache

from utils.read_input import read_input


@cache
def get_arrangements(conditions, groups, condition_idx, group_idx, current_group_len):
    if condition_idx == len(conditions):
        if current_group_len == 0 and group_idx == len(groups):
            return 1
        elif group_idx == len(groups) - 1 and current_group_len == groups[group_idx]:
            return 1
        else:
            return 0

    arrangements = 0
    possible_conditions = (
        ["#", "."] if conditions[condition_idx] == "?" else conditions[condition_idx]
    )
    for c in possible_conditions:
        if c == "#":
            arrangements += get_arrangements(
                conditions, groups, condition_idx + 1, group_idx, current_group_len + 1
            )
        elif current_group_len == 0:
            arrangements += get_arrangements(
                conditions, groups, condition_idx + 1, group_idx, current_group_len
            )
        elif group_idx < len(groups) and current_group_len == groups[group_idx]:
            arrangements += get_arrangements(
                conditions, groups, condition_idx + 1, group_idx + 1, 0
            )
    return arrangements


if __name__ == "__main__":
    total_arrangements = 0
    for line in read_input("2023/day_12/input.txt"):
        conditions = "?".join([line.split()[0]] * 5)
        groups = tuple(int(i) for i in line.split()[1].split(",")) * 5
        total_arrangements += get_arrangements(conditions, groups, 0, 0, 0)

    print(total_arrangements)
