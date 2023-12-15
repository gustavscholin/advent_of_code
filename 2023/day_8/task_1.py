import re

from utils.read_input import read_input

if __name__ == "__main__":
    docs = read_input("2023/day_8/input.txt")
    instructions = docs[0]
    nodes = {}
    for line in docs[2:]:
        key = re.findall(r"(\w+)", line)
        nodes[key[0]] = (key[1], key[2])

    node = "AAA"
    steps = 0
    while node != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        node = nodes[node][0] if instruction == "L" else nodes[node][1]
        steps += 1
    print(steps)
