import re
from utils.read_input import read_input


def compare_ranges(x, y):
    return bool(range(max(x[0], y[0]), min(x[-1], y[-1]) + 1))


if __name__ == "__main__":
    schema_lines = read_input("2023/day_3/input.txt")
    new_line = "." * len(schema_lines[0])
    schema_lines = [new_line] + schema_lines + [new_line]
    schema_lines = ["." + line + "." for line in schema_lines]
    sum = 0
    for i, line in enumerate(schema_lines[1:-1], 1):
        for gear_match in re.finditer(r"\*", line):
            gear_idx = gear_match.start(0)
            adjacent_numbers = []
            for neighbour_line in (schema_lines[i - 1], line, schema_lines[i + 1]):
                for number_match in re.finditer(r"\d+", neighbour_line):
                    if compare_ranges(
                        range(gear_idx - 1, gear_idx + 2),
                        range(number_match.start(0), number_match.end(0)),
                    ):
                        adjacent_numbers.append(int(number_match.group(0)))
            if len(adjacent_numbers) == 2:
                sum += adjacent_numbers[0] * adjacent_numbers[1]
    print(sum)
