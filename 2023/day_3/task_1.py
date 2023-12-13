import re

from utils.read_input import read_input


def check_for_symbol(sub_str):
    return bool(re.search(r"[^.\d]", sub_str))


if __name__ == "__main__":
    schema_lines = read_input("2023/day_3/input.txt")
    new_line = "." * len(schema_lines[0])
    schema_lines = [new_line] + schema_lines + [new_line]
    schema_lines = ["." + line + "." for line in schema_lines]
    sum = 0
    for i, line in enumerate(schema_lines[1:-1], 1):
        for number_match in re.finditer(r"\d+", line):
            s = number_match.start(0)
            e = number_match.end(0)
            neighbours = (
                schema_lines[i - 1][s - 1 : e + 1]
                + schema_lines[i + 1][s - 1 : e + 1]
                + line[s - 1]
                + line[e]
            )
            if check_for_symbol(neighbours):
                sum += int(line[s:e])
    print(sum)
