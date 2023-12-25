import re
from itertools import combinations

from utils.read_input import read_input

if __name__ == "__main__":
    arrangements = 0
    for line in read_input("2023/day_12/input.txt"):
        conditions = line.split()[0]
        groups = [int(i) for i in line.split()[1].split(",")]
        filled = [i for i, c in enumerate(conditions) if c == "#"]
        unknowns = [i for i, c in enumerate(conditions) if c == "?"]
        for p in combinations(unknowns, sum(groups) - len(filled)):
            filled_conditions = [c for c in conditions]
            for i in unknowns:
                filled_conditions[i] = "#" if i in p else "."
            if [
                len(g) for g in re.split(r"\.+", "".join(filled_conditions).strip("."))
            ] == groups:
                arrangements += 1

    print(arrangements)
