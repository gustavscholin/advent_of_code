import re
from math import lcm

from utils.read_input import read_input

if __name__ == "__main__":
    docs = read_input("2023/day_8/input.txt")
    instructions = docs[0]
    node_map = {}
    for line in docs[2:]:
        key = re.findall(r"(\w+)", line)
        node_map[key[0]] = (key[1], key[2])

    # It turns out that for each path, there's only one **Z node before it loops,
    # and the loop destination is always N steps from the start, while the point it
    # loops from is always N steps after the **Z node.
    # So the solution just becomes lcm(steps_to_first_z for each path)
    nodes = [n for n in node_map.keys() if n[-1] == "A"]
    periods = []
    steps = 0
    while nodes:
        instruction = instructions[steps % len(instructions)]
        new_nodes = [node_map[n][0 if instruction == "L" else 1] for n in nodes]
        [periods.append(steps + 1) for n in new_nodes if n[-1] == "Z"]
        nodes = [n for n in new_nodes if n[-1] != "Z"]
        steps += 1
    print(lcm(*periods))
